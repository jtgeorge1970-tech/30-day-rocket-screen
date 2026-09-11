from __future__ import annotations

import math
from typing import Dict

import numpy as np
import pandas as pd

from engine4_config import (
    HARD_MARKET_REVERSAL_PCT,
    MAX_BREAKOUT_CHASE_PCT,
    MAX_PULLBACK_VOLUME_RATIO,
    MAX_SPREAD_PCT,
    MAX_VWAP_EXTENSION_PCT,
    MIN_BREAKOUT_VOLUME_RATIO,
    MIN_REWARD_RISK,
    SECTOR_ETF,
)
from engine4_data import ensure_et_index, quote_spread, slice_window


def vwap(frame: pd.DataFrame) -> float:
    if frame is None or frame.empty:
        return np.nan
    high = pd.to_numeric(frame["High"], errors="coerce")
    low = pd.to_numeric(frame["Low"], errors="coerce")
    close = pd.to_numeric(frame["Close"], errors="coerce")
    volume = pd.to_numeric(frame["Volume"], errors="coerce").fillna(0)
    denominator = volume.sum()
    if denominator <= 0:
        return np.nan
    return float((((high + low + close) / 3.0) * volume).sum() / denominator)


def market_context(frames: Dict[str, pd.DataFrame], date_et) -> Dict[str, float]:
    out: Dict[str, float] = {}
    for symbol, frame in frames.items():
        regular = slice_window(frame, date_et, "09:30", "09:45", inclusive="left")
        if regular.empty:
            continue
        close = pd.to_numeric(regular["Close"], errors="coerce").dropna()
        opening = pd.to_numeric(regular["Open"], errors="coerce").dropna()
        if close.empty or opening.empty:
            continue
        out[f"{symbol}_ret"] = (float(close.iloc[-1]) / float(opening.iloc[0]) - 1.0) * 100.0
        out[f"{symbol}_last"] = float(close.iloc[-1])
        out[f"{symbol}_vwap"] = vwap(regular)
        if len(close) >= 5:
            out[f"{symbol}_last5_ret"] = (float(close.iloc[-1]) / float(close.iloc[-5]) - 1.0) * 100.0
    return out


def opening_structure(symbol: str, frame: pd.DataFrame, row: pd.Series, market: Dict[str, float], date_et) -> dict:
    regular = slice_window(frame, date_et, "09:30", "09:45", inclusive="left")
    if len(regular) < 10:
        return {"ticker": symbol, "data_ok": False, "failures": ["insufficient_opening_bars"]}

    close = pd.to_numeric(regular["Close"], errors="coerce").dropna()
    high = pd.to_numeric(regular["High"], errors="coerce")
    low = pd.to_numeric(regular["Low"], errors="coerce")
    volume = pd.to_numeric(regular["Volume"], errors="coerce").fillna(0)
    opening = pd.to_numeric(regular["Open"], errors="coerce").dropna()
    if close.empty or opening.empty:
        return {"ticker": symbol, "data_ok": False, "failures": ["missing_price_data"]}

    last = float(close.iloc[-1])
    open_price = float(opening.iloc[0])
    current_vwap = vwap(regular)
    opening_range_high = float(high.max())
    first5_low = float(low.iloc[:5].min())
    recent_low = float(low.iloc[-5:].min())
    higher_low = recent_low > first5_low
    lower_low_deterioration = float(low.iloc[-1]) <= float(low.iloc[:-1].min())

    first_range = max(1e-9, float(high.iloc[:5].max() - low.iloc[:5].min()))
    recent_range = float(high.iloc[-5:].max() - low.iloc[-5:].min())
    tight_base = recent_range <= 0.35 * first_range
    structure = higher_low or tight_base

    pullback_window = volume.iloc[-7:-2] if len(volume) >= 7 else volume.iloc[:-2]
    pullback_mean = float(pullback_window.mean()) if len(pullback_window) else np.nan
    impulse_mean = float(volume.iloc[:5].mean()) if len(volume) >= 5 else np.nan
    pullback_ratio = pullback_mean / impulse_mean if impulse_mean and math.isfinite(impulse_mean) and impulse_mean > 0 else np.nan

    breakout_window = volume.iloc[-2:]
    breakout_ratio = float(breakout_window.mean() / pullback_mean) if pullback_mean and math.isfinite(pullback_mean) and pullback_mean > 0 else np.nan

    attack_breakout = last >= opening_range_high * (1.0 - 0.0035)
    extension_vwap_pct = (last / current_vwap - 1.0) * 100.0 if current_vwap and math.isfinite(current_vwap) else np.nan
    entry_trigger = opening_range_high * 1.0005
    entry_missed = last > entry_trigger * (1.0 + MAX_BREAKOUT_CHASE_PCT / 100.0)

    stop = max(current_vwap * 0.999 if math.isfinite(current_vwap) else 0.0, recent_low * 0.999)
    if stop >= entry_trigger:
        stop = min(current_vwap, recent_low) * 0.999
    risk = entry_trigger - stop
    resistance = float(row.get("resistance_price", np.nan))
    target = entry_trigger + 2.5 * risk if risk > 0 else np.nan
    if math.isfinite(resistance) and resistance > entry_trigger:
        target = min(target, resistance)
    reward_risk = (target - entry_trigger) / risk if risk > 0 and target > entry_trigger else np.nan

    spy_ret = market.get("SPY_ret", 0.0)
    qqq_ret = market.get("QQQ_ret", 0.0)
    stock_ret = (last / open_price - 1.0) * 100.0
    relative_market = stock_ret - np.nanmean([spy_ret, qqq_ret])

    sector_etf = SECTOR_ETF.get(str(row.get("sector", "")))
    sector_ret = market.get(f"{sector_etf}_ret", 0.0) if sector_etf else 0.0
    relative_sector = stock_ret - sector_ret

    hard_market_reversal = (
        spy_ret <= HARD_MARKET_REVERSAL_PCT
        and qqq_ret <= HARD_MARKET_REVERSAL_PCT
        and market.get("SPY_last5_ret", 0.0) < 0
        and market.get("QQQ_last5_ret", 0.0) < 0
    )

    bid, ask, spread = quote_spread(symbol)

    failures = []
    if relative_market <= 0:
        failures.append("relative_strength_market")
    if relative_sector <= 0:
        failures.append("relative_strength_sector")
    if not math.isfinite(current_vwap) or last < current_vwap:
        failures.append("below_vwap")
    if lower_low_deterioration:
        failures.append("lower_low_deterioration")
    if not structure:
        failures.append("no_higher_low_or_tight_base")
    if not attack_breakout:
        failures.append("not_attacking_breakout")
    if not math.isfinite(pullback_ratio) or pullback_ratio > MAX_PULLBACK_VOLUME_RATIO:
        failures.append("pullback_volume_not_contracting")
    if not math.isfinite(breakout_ratio) or breakout_ratio < MIN_BREAKOUT_VOLUME_RATIO:
        failures.append("breakout_volume_not_expanding")
    if not math.isfinite(spread) or spread > MAX_SPREAD_PCT:
        failures.append("spread")
    if not math.isfinite(extension_vwap_pct) or extension_vwap_pct > MAX_VWAP_EXTENSION_PCT:
        failures.append("extended_from_vwap")
    if not math.isfinite(reward_risk) or reward_risk < MIN_REWARD_RISK:
        failures.append("reward_risk_below_2")
    if hard_market_reversal:
        failures.append("broad_market_hard_reversal")
    if entry_missed:
        failures.append("entry_missed")

    return {
        "ticker": symbol,
        "data_ok": True,
        "last": last,
        "vwap": current_vwap,
        "opening_range_high": opening_range_high,
        "higher_low": higher_low,
        "tight_base": tight_base,
        "pullback_volume_ratio": pullback_ratio,
        "breakout_volume_ratio": breakout_ratio,
        "entry_trigger": entry_trigger,
        "initial_stop": stop,
        "first_target": target,
        "reward_risk": reward_risk,
        "relative_strength_market_pct": relative_market,
        "relative_strength_sector_pct": relative_sector,
        "extension_vwap_pct": extension_vwap_pct,
        "live_bid": bid,
        "live_ask": ask,
        "live_spread_pct": spread,
        "hard_market_reversal": hard_market_reversal,
        "failures": failures,
        "pass": len(failures) == 0,
    }


def live_quality(premarket_score: float, metrics: dict) -> float:
    return (
        0.40 * premarket_score
        + 20.0 * min(max(metrics["relative_strength_market_pct"], 0.0), 5.0) / 5.0
        + 20.0 * min(max(metrics["breakout_volume_ratio"] - 1.0, 0.0), 2.0) / 2.0
        + 20.0 * (1.0 if metrics["higher_low"] else 0.7)
    )
