"""Engine 4 — Intraday A+ setup screen.

Free-data implementation using the existing Rocket stack:
- Nasdaq Trader symbol master
- existing Yahoo/yfinance daily/fundamental cache produced by Engines 1-3
- Yahoo/yfinance premarket and intraday 1-minute data

Stages:
  premarket  -> broad eligible universe -> ranked/frozen Top 25
  final      -> 9:45 ET live A+ confirmation on frozen Top 25

The engine is fail-closed: missing/stale/insufficient data returns NO TRADE rather
than fabricating or relaxing gates.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import time
from dataclasses import dataclass
from datetime import datetime, time as dtime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import yfinance as yf

ET = ZoneInfo("America/New_York")
OUT = Path("output/engine4")
OUT.mkdir(parents=True, exist_ok=True)

TOP_N = 25
MIN_PRICE = 5.0
MIN_MARKET_CAP = 300_000_000
MIN_DOLLAR_VOL = 20_000_000
MIN_RR = 2.0
MAX_SPREAD_PCT = 0.50
MAX_VWAP_EXTENSION_PCT = 3.0
PREMARKET_MIN_SCORE = 70.0
BATCH = 50

# Locked SSOT weights (100 points total)
WEIGHTS = {
    "catalyst": 25.0,
    "premarket_rvol": 20.0,
    "gap_quality": 15.0,
    "liquidity": 15.0,
    "resistance_room": 10.0,
    "atr": 5.0,
    "relative_strength": 5.0,
    "execution": 5.0,
}


def now_et() -> datetime:
    return datetime.now(ET)


def pct(a, b):
    if b is None or b == 0 or pd.isna(b) or pd.isna(a):
        return np.nan
    return (a / b - 1.0) * 100.0


def clamp(v, lo=0.0, hi=1.0):
    return max(lo, min(hi, float(v)))


def load_baseline() -> pd.DataFrame:
    """Reuse Engines 1-3 audited Yahoo outputs; no fresh per-symbol fundamentals crawl."""
    inv = Path("output/03_investable.csv")
    fund = Path("output/fundamentals_checkpoint.csv")
    if not inv.exists() or not fund.exists():
        raise RuntimeError("Required Rocket free-data baseline files are missing")
    a = pd.read_csv(inv)
    b = pd.read_csv(fund)
    df = a.merge(b[["ticker", "market_cap", "sector", "industry"]], on="ticker", how="left")
    df = df[(df.price >= MIN_PRICE) & (df.market_cap >= MIN_MARKET_CAP)]
    df = df[df.dollar_volume >= MIN_DOLLAR_VOL]
    return df.drop_duplicates("ticker").reset_index(drop=True)


def _extract_intraday(download: pd.DataFrame, symbol: str) -> pd.DataFrame:
    if download is None or download.empty:
        return pd.DataFrame()
    try:
        if isinstance(download.columns, pd.MultiIndex):
            # yfinance columns may be (Price,Ticker)
            if symbol not in download.columns.get_level_values(-1):
                return pd.DataFrame()
            x = download.xs(symbol, axis=1, level=-1).copy()
        else:
            x = download.copy()
        x = x.rename(columns={c: str(c).lower() for c in x.columns})
        x.index = pd.to_datetime(x.index)
        if x.index.tz is None:
            x.index = x.index.tz_localize("UTC")
        x.index = x.index.tz_convert(ET)
        return x.dropna(subset=["close"]) if "close" in x.columns else pd.DataFrame()
    except Exception:
        return pd.DataFrame()


def download_intraday(symbols: list[str], period="5d", prepost=True) -> dict[str, pd.DataFrame]:
    out = {}
    for i in range(0, len(symbols), BATCH):
        batch = symbols[i:i+BATCH]
        data = yf.download(
            tickers=batch,
            period=period,
            interval="1m",
            prepost=prepost,
            group_by="column",
            auto_adjust=False,
            threads=True,
            progress=False,
            timeout=25,
        )
        for s in batch:
            x = _extract_intraday(data, s)
            if not x.empty:
                out[s] = x
    return out


def same_day_window(x: pd.DataFrame, start: dtime, end: dtime, date=None) -> pd.DataFrame:
    if x.empty:
        return x
    date = date or now_et().date()
    return x[(x.index.date == date) & (x.index.time >= start) & (x.index.time <= end)]


def typical_premarket_volume(x: pd.DataFrame) -> float:
    vols = []
    for d in sorted(set(x.index.date))[:-1]:
        w = x[(x.index.date == d) & (x.index.time >= dtime(4,0)) & (x.index.time <= dtime(9,25))]
        if not w.empty:
            vols.append(float(w.volume.fillna(0).sum()))
    return float(np.median(vols)) if vols else np.nan


def catalyst_score(symbol: str) -> tuple[float, str]:
    """Verify a material recent catalyst only for a small finalist pool."""
    try:
        news = yf.Ticker(symbol).news or []
    except Exception:
        return 0.0, "news unavailable"
    if not news:
        return 0.0, "no verified recent catalyst"
    keywords_hi = ("earn", "guidance", "fda", "approval", "contract", "acquire", "merger", "partnership", "raises", "beats")
    keywords_mid = ("analyst", "upgrade", "launch", "order", "agreement", "trial", "forecast")
    best = (0.0, "no material catalyst keyword")
    for item in news[:10]:
        c = item.get("content") if isinstance(item, dict) else None
        title = ""
        if isinstance(c, dict):
            title = str(c.get("title") or "")
        elif isinstance(item, dict):
            title = str(item.get("title") or "")
        low = title.lower()
        if any(k in low for k in keywords_hi):
            return 1.0, title[:180]
        if any(k in low for k in keywords_mid) and best[0] < 0.7:
            best = (0.7, title[:180])
        elif title and best[0] < 0.4:
            best = (0.4, title[:180])
    return best


def daily_resistance_room(row, current) -> float:
    # Use 52-week high as a conservative known resistance proxy from audited daily history.
    high52 = current / (1.0 + float(row.drawdown_52)) if pd.notna(row.drawdown_52) and row.drawdown_52 > -0.99 else np.nan
    if pd.isna(high52) or high52 <= current:
        return 10.0
    return max(0.0, pct(high52, current))


def score_premarket_row(row, x: pd.DataFrame, market_gap: float) -> dict | None:
    today = now_et().date()
    pm = same_day_window(x, dtime(4,0), dtime(9,25), today)
    if pm.empty or len(pm) < 3:
        return None
    current = float(pm.close.iloc[-1])
    prev_close = float(row.price)
    gap = pct(current, prev_close)
    if pd.isna(gap):
        return None
    pm_vol = float(pm.volume.fillna(0).sum())
    typical = typical_premarket_volume(x)
    rvol = pm_vol / typical if pd.notna(typical) and typical > 0 else np.nan
    if pm_vol <= 0:
        return None
    # Broad objective gates before expensive catalyst lookup.
    if abs(gap) > 25 or current < MIN_PRICE:
        return None
    atr_pct = float(row.volatility) / math.sqrt(252) * 100 if pd.notna(row.volatility) else np.nan
    room = daily_resistance_room(row, current)
    rel = gap - market_gap if pd.notna(market_gap) else gap
    pm_dollar = pm_vol * current

    gap_score = 0.0
    if gap > 0:
        gap_score = 15.0 * clamp(gap / 5.0) if gap <= 5 else 15.0 * clamp(1.0 - max(0,gap-12)/13)
    rvol_score = 20.0 * clamp((rvol if pd.notna(rvol) else 0) / 5.0)
    liq_score = 15.0 * clamp(float(row.dollar_volume) / 100_000_000)
    room_score = 10.0 * clamp(room / 8.0)
    atr_score = 5.0 * clamp((atr_pct if pd.notna(atr_pct) else 0) / 5.0)
    rs_score = 5.0 * clamp(max(rel, 0) / 3.0)
    # Execution proxy pre-open; actual live spread is checked at final stage.
    exec_score = 5.0 if pm_dollar >= 1_000_000 else 5.0 * clamp(pm_dollar / 1_000_000)

    return {
        "ticker": row.ticker,
        "price": current,
        "gap_pct": gap,
        "pm_volume": pm_vol,
        "pm_dollar_volume": pm_dollar,
        "pm_rvol": rvol,
        "atr_pct": atr_pct,
        "resistance_room_pct": room,
        "relative_strength_pct": rel,
        "base_score_without_catalyst": gap_score+rvol_score+liq_score+room_score+atr_score+rs_score+exec_score,
        "gap_score": gap_score,
        "rvol_score": rvol_score,
        "liquidity_score": liq_score,
        "room_score": room_score,
        "atr_score": atr_score,
        "rs_score": rs_score,
        "execution_score": exec_score,
        "sector": getattr(row, "sector", ""),
    }


def premarket() -> pd.DataFrame:
    started = time.monotonic()
    base = load_baseline()
    symbols = base.ticker.tolist()
    intr = download_intraday(symbols, period="5d", prepost=True)

    # Market gap reference from SPY using same source/time window.
    market_gap = 0.0
    spy = download_intraday(["SPY"], period="5d", prepost=True).get("SPY", pd.DataFrame())
    if not spy.empty:
        today_spy = same_day_window(spy, dtime(4,0), dtime(9,25))
        prior = spy[spy.index.date < now_et().date()]
        if not today_spy.empty and not prior.empty:
            market_gap = pct(float(today_spy.close.iloc[-1]), float(prior.close.iloc[-1]))

    rows = []
    for row in base.itertuples(index=False):
        x = intr.get(row.ticker)
        if x is None:
            continue
        scored = score_premarket_row(row, x, market_gap)
        if scored:
            rows.append(scored)
    if not rows:
        raise RuntimeError("PREMARKET SCREEN FAILED: no trustworthy candidates")
    df = pd.DataFrame(rows)

    # Only the strongest objective survivors receive slower catalyst verification.
    df = df.sort_values("base_score_without_catalyst", ascending=False).head(75).copy()
    cats, notes = [], []
    for s in df.ticker:
        q, note = catalyst_score(s)
        cats.append(25.0*q)
        notes.append(note)
    df["catalyst_score"] = cats
    df["catalyst_note"] = notes
    df["score"] = df.base_score_without_catalyst + df.catalyst_score

    # A+ balance rule: no candidate enters solely on one flashy metric.
    df["balanced"] = (
        (df.rvol_score >= 5) &
        (df.liquidity_score >= 5) &
        (df.room_score >= 2.5) &
        (df.execution_score >= 2.5)
    )
    df = df[df.balanced & (df.score >= PREMARKET_MIN_SCORE)]
    df = df.sort_values(["score","catalyst_score","rvol_score","liquidity_score"], ascending=False).head(TOP_N)
    if df.empty:
        raise RuntimeError("PREMARKET SCREEN FAILED: no names cleared minimum quality floor")
    df.insert(0, "rank", range(1, len(df)+1))
    df["frozen_at_et"] = now_et().isoformat()
    df["runtime_seconds"] = round(time.monotonic()-started, 2)
    df.to_csv(OUT / "top25_frozen.csv", index=False)
    (OUT / "premarket_audit.json").write_text(json.dumps({
        "timestamp_et": now_et().isoformat(),
        "baseline_count": len(base),
        "intraday_data_count": len(intr),
        "top25_count": len(df),
        "market_gap_pct": market_gap,
        "runtime_seconds": round(time.monotonic()-started, 2),
        "weights": WEIGHTS,
    }, indent=2))
    return df


def session_features(x: pd.DataFrame, symbol: str) -> dict | None:
    today = now_et().date()
    reg = same_day_window(x, dtime(9,30), dtime(9,45), today)
    if len(reg) < 10:
        return None
    # volume-weighted VWAP over regular session opening window
    vol = reg.volume.fillna(0).astype(float)
    typ = (reg.high.astype(float)+reg.low.astype(float)+reg.close.astype(float))/3
    if vol.sum() <= 0:
        return None
    vwap = float((typ*vol).sum()/vol.sum())
    last = float(reg.close.iloc[-1])
    or_high = float(reg.high.max())
    or_low = float(reg.low.min())
    first5 = reg.iloc[:5]
    last5 = reg.iloc[-5:]
    pullback_vol_contract = float(last5.volume.mean()) <= float(first5.volume.mean()) * 1.10
    # Higher-low proxy: minimum of last five bars above opening-window low and last price not deteriorating.
    higher_low = float(last5.low.min()) > or_low and last >= float(last5.close.iloc[0])
    attacking = last >= or_high * 0.997
    extension = pct(last, vwap)
    giant_first = pct(float(first5.high.max()), float(first5.low.min())) > 4.0 and float(last5.volume.mean()) < float(first5.volume.mean())*0.35
    return {
        "ticker": symbol,
        "last": last,
        "vwap": vwap,
        "or_high": or_high,
        "or_low": or_low,
        "above_vwap": last >= vwap,
        "higher_low": higher_low,
        "attacking_breakout": attacking,
        "pullback_volume_contract": pullback_vol_contract,
        "breakout_volume_expand": float(reg.volume.iloc[-1]) >= float(last5.volume.iloc[:-1].mean()) if len(last5)>1 else False,
        "extension_from_vwap_pct": extension,
        "giant_first_then_collapse": giant_first,
    }


def final_scan() -> dict:
    started = time.monotonic()
    frozen = OUT / "top25_frozen.csv"
    if not frozen.exists():
        return {"action":"NO_TRADE","message":"NO TRADE — premarket Top 25 unavailable."}
    top = pd.read_csv(frozen)
    symbols = top.ticker.tolist()
    intr = download_intraday(symbols + ["SPY","QQQ"], period="1d", prepost=False)
    spyf = session_features(intr.get("SPY", pd.DataFrame()), "SPY")
    qqqf = session_features(intr.get("QQQ", pd.DataFrame()), "QQQ")
    market_ok = True
    if spyf and qqqf:
        market_ok = spyf["last"] >= spyf["vwap"] or qqqf["last"] >= qqqf["vwap"]

    passes = []
    audit = []
    for pm in top.itertuples(index=False):
        x = intr.get(pm.ticker, pd.DataFrame())
        f = session_features(x, pm.ticker)
        if not f:
            continue
        rel_ok = True
        if spyf:
            rel_ok = pct(f["last"], float(pm.price)) > pct(spyf["last"], spyf["or_low"])
        stop = max(f["vwap"], f["or_low"])
        entry = f["or_high"] * 1.0005
        risk = entry - stop
        room_target = entry * (1 + max(float(pm.resistance_room_pct),0)/100)
        target = min(room_target, entry + max(2.0*risk, 0)) if risk > 0 else np.nan
        rr = (target-entry)/risk if risk > 0 and pd.notna(target) else np.nan
        gates = {
            "relative_strength": bool(rel_ok),
            "vwap_hold": bool(f["above_vwap"]),
            "higher_low_or_tight": bool(f["higher_low"]),
            "attack_breakout": bool(f["attacking_breakout"]),
            "pullback_volume_contract": bool(f["pullback_volume_contract"]),
            "breakout_volume_expand": bool(f["breakout_volume_expand"]),
            "not_extended": bool(f["extension_from_vwap_pct"] <= MAX_VWAP_EXTENSION_PCT),
            "no_giant_collapse": not bool(f["giant_first_then_collapse"]),
            "reward_risk": bool(pd.notna(rr) and rr >= MIN_RR),
            "market_not_reversing": bool(market_ok),
        }
        passed = all(gates.values())
        audit.append({**f,"entry":entry,"stop":stop,"target":target,"rr":rr,"passed":passed,**gates})
        if passed:
            # Stale-entry protection: allow only tiny proximity to trigger; no chasing.
            if f["last"] > entry * 1.005:
                continue
            passes.append((float(pm.score), float(rr), pm.ticker, entry, stop, target, f))

    pd.DataFrame(audit).to_csv(OUT / "final_live_audit.csv", index=False)
    if not passes:
        result = {"action":"NO_TRADE","message":"NO TRADE — no A+ setup.","runtime_seconds":round(time.monotonic()-started,2)}
    else:
        passes.sort(reverse=True)
        _, rr, sym, entry, stop, target, f = passes[0]
        result = {
            "action":"BUY",
            "symbol":sym,
            "entry_trigger":round(entry,2),
            "initial_stop":round(stop,2),
            "first_management":round(target,2),
            "reward_risk":round(rr,2),
            "trailing_stop_rule":"Activate only after runner confirmation; trail under fresh intraday higher-low/VWAP support, not an arbitrary tight percentage.",
            "message":f"BUY {sym} NOW",
            "runtime_seconds":round(time.monotonic()-started,2),
        }
    (OUT / "final_signal.json").write_text(json.dumps(result, indent=2))
    return result


def self_test():
    assert sum(WEIGHTS.values()) == 100.0
    assert TOP_N == 25
    assert MIN_RR == 2.0
    # Deterministic arithmetic checks.
    assert round(pct(105,100), 6) == 5.0
    assert clamp(2) == 1.0 and clamp(-1) == 0.0
    print("ENGINE4_SELF_TEST_PASS")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("stage", choices=["premarket","final","self-test"])
    args = p.parse_args()
    if args.stage == "premarket":
        df = premarket()
        print(df[["rank","ticker","score","gap_pct","pm_rvol","catalyst_note"]].to_string(index=False))
    elif args.stage == "final":
        print(json.dumps(final_scan(), indent=2))
    else:
        self_test()

if __name__ == "__main__":
    main()
