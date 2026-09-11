from __future__ import annotations

import json
import math
import time
from datetime import datetime, timezone

import pandas as pd

import engine4_live
from engine4_config import ET, MAX_BREAKOUT_CHASE_PCT, SECTOR_ETF
from engine4_data import download_intraday, now_et
from engine4_intraday import OUT, serializable, write_final
from engine4_live import live_quality, market_context, opening_structure


def _current_mid(symbol: str) -> tuple[float, float, float, float]:
    bid, ask, spread = engine4_live.quote_spread(symbol)
    if not (math.isfinite(bid) and math.isfinite(ask) and bid > 0 and ask >= bid):
        return math.nan, bid, ask, spread
    return (bid + ask) / 2.0, bid, ask, spread


def _trigger_seen(frame: pd.DataFrame, date_et, trigger: float) -> bool:
    if frame is None or frame.empty or not math.isfinite(trigger):
        return False
    same_day = frame[frame.index.date == date_et]
    if same_day.empty or "High" not in same_day.columns:
        return False
    regular = same_day.between_time("09:30", "16:00", inclusive="both")
    if regular.empty:
        return False
    highs = pd.to_numeric(regular["High"], errors="coerce").dropna()
    return bool(not highs.empty and float(highs.max()) >= trigger)


def guarded_final_stage(date_override: str | None = None) -> dict:
    """Final Engine 4 stage with a mandatory current-price trigger guard.

    BUY NOW is impossible unless the fresh bid/ask midpoint is at/above the trigger
    and no more than the locked chase allowance above it. A stock below an untriggered
    breakout becomes WATCH. A stock that already touched the trigger and then fell
    back below it, or is now beyond the chase band, becomes entry missed.
    """
    started = time.monotonic()
    reference = now_et() if date_override is None else datetime.fromisoformat(date_override + "T09:45:00").replace(tzinfo=ET)
    date_et = reference.date()
    frozen_path = OUT / "top25_frozen.csv"
    if not frozen_path.exists() or frozen_path.stat().st_size < 5:
        return write_final({
            "status": "NO_TRADE",
            "reason": "missing_top25",
            "message": "NO TRADE — premarket Top 25 unavailable.",
            "runtime_seconds": round(time.monotonic() - started, 3),
        })

    try:
        top = pd.read_csv(frozen_path)
    except Exception:
        top = pd.DataFrame()
    if top.empty or "ticker" not in top.columns:
        return write_final({
            "status": "NO_TRADE",
            "reason": "empty_top25",
            "message": "NO TRADE — no A+ setup.",
            "runtime_seconds": round(time.monotonic() - started, 3),
        })

    symbols = top.ticker.astype(str).tolist()
    candidate_frames = download_intraday(symbols, period="1d", interval="1m", prepost=False, date_et=date_et, lookback_days=0)
    benchmark_symbols = ["SPY", "QQQ"] + sorted({SECTOR_ETF[s] for s in top.sector if s in SECTOR_ETF})
    benchmark_frames = download_intraday(benchmark_symbols, period="1d", interval="1m", prepost=False, date_et=date_et, lookback_days=0)
    market = market_context(benchmark_frames, date_et)

    audit = []
    buyable = []
    watches = []
    missed = []

    for _, row in top.iterrows():
        symbol = str(row.ticker)
        frame = candidate_frames.get(symbol)
        if frame is None or frame.empty:
            audit.append({"ticker": symbol, "pass": False, "failures": ["missing_live_data"]})
            continue

        metrics = opening_structure(symbol, frame, row, market, date_et)
        failures = list(metrics.get("failures", []))
        failures = [f for f in failures if f != "entry_missed"]
        metrics["failures_before_current_price_guard"] = list(failures)

        if failures:
            metrics["pass"] = False
            audit.append(metrics)
            continue

        current, bid, ask, spread = _current_mid(symbol)
        trigger = float(metrics.get("entry_trigger", math.nan))
        max_allowed = trigger * (1.0 + MAX_BREAKOUT_CHASE_PCT / 100.0) if math.isfinite(trigger) else math.nan
        seen = _trigger_seen(frame, date_et, trigger)
        metrics.update({
            "current_live_price": current,
            "current_bid": bid,
            "current_ask": ask,
            "current_spread_pct": spread,
            "max_allowed_buy_price": max_allowed,
            "trigger_seen_today": seen,
        })

        if not math.isfinite(current):
            metrics["pass"] = False
            metrics["failures"] = ["missing_current_live_price"]
            audit.append(metrics)
            continue

        quality = live_quality(float(row.get("score", 0)), metrics)
        if current < trigger:
            metrics["pass"] = False
            if seen:
                metrics["failures"] = ["entry_missed_breakout_failed"]
                missed.append((quality, row, metrics))
            else:
                metrics["failures"] = ["trigger_not_reached"]
                watches.append((quality, row, metrics))
        elif current > max_allowed:
            metrics["pass"] = False
            metrics["failures"] = ["entry_missed_chase_band"]
            missed.append((quality, row, metrics))
        else:
            metrics["pass"] = True
            metrics["failures"] = []
            buyable.append((quality, row, metrics))
        audit.append(metrics)

    (OUT / "final_live_audit.json").write_text(json.dumps({
        "target_date_et": str(date_et),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "market": {k: serializable(v) for k, v in market.items()},
        "candidates": [{k: serializable(v) for k, v in item.items()} for item in audit],
    }, indent=2), encoding="utf-8")

    if buyable:
        buyable.sort(key=lambda item: item[0], reverse=True)
        _, row, metrics = buyable[0]
        symbol = str(row.ticker)
        message = (
            f"BUY {symbol} NOW\n"
            f"BUY RANGE: ${metrics['entry_trigger']:.2f} to ${metrics['max_allowed_buy_price']:.2f}\n"
            f"Current price: ${metrics['current_live_price']:.2f}\n"
            f"DO NOT BUY ABOVE ${metrics['max_allowed_buy_price']:.2f}\n"
            f"Initial stop: ${metrics['initial_stop']:.2f}\n"
            f"First management level: ${metrics['first_target']:.2f}\n"
            "Trailing stop: activate only after +1R and a confirmed higher low forms above entry; then trail just below the newest confirmed higher-low/VWAP support and never loosen the stop.\n"
            f"Reason: full A+ gates passed AND fresh live price is inside the valid buy range; R:R {metrics['reward_risk']:.2f}:1."
        )
        return write_final({
            "status": "BUY",
            "reason": "live_trigger_confirmed",
            "ticker": symbol,
            "message": message,
            "order_instruction": "BUY_WITHIN_RANGE_NOW",
            "live_price": metrics["current_live_price"],
            "entry_trigger": metrics["entry_trigger"],
            "max_allowed_buy_price": metrics["max_allowed_buy_price"],
            "initial_stop": metrics["initial_stop"],
            "first_target": metrics["first_target"],
            "reward_risk": metrics["reward_risk"],
            "runtime_seconds": round(time.monotonic() - started, 3),
        })

    if watches:
        watches.sort(key=lambda item: item[0], reverse=True)
        _, row, metrics = watches[0]
        symbol = str(row.ticker)
        message = (
            f"WAIT — DO NOT BUY {symbol} YET\n"
            f"BUY ONLY IF PRICE REACHES ${metrics['entry_trigger']:.2f}\n"
            f"VALID BUY RANGE IF TRIGGERED: ${metrics['entry_trigger']:.2f} to ${metrics['max_allowed_buy_price']:.2f}\n"
            f"Current price: ${metrics['current_live_price']:.2f}\n"
            f"DO NOT BUY BELOW ${metrics['entry_trigger']:.2f}\n"
            f"DO NOT BUY ABOVE ${metrics['max_allowed_buy_price']:.2f}\n"
            "Status: setup remains valid, but the breakout has not confirmed yet."
        )
        return write_final({
            "status": "WATCH",
            "reason": "trigger_not_reached",
            "ticker": symbol,
            "message": message,
            "order_instruction": "WAIT_FOR_TRIGGER",
            "live_price": metrics["current_live_price"],
            "entry_trigger": metrics["entry_trigger"],
            "max_allowed_buy_price": metrics["max_allowed_buy_price"],
            "runtime_seconds": round(time.monotonic() - started, 3),
        })

    if missed:
        missed.sort(key=lambda item: item[0], reverse=True)
        _, row, metrics = missed[0]
        return write_final({
            "status": "NO_TRADE",
            "reason": "entry_missed",
            "ticker": str(row.ticker),
            "message": "NO TRADE — entry missed / breakout failed. DO NOT BUY.",
            "order_instruction": "NO_ORDER",
            "live_price": metrics.get("current_live_price"),
            "entry_trigger": metrics.get("entry_trigger"),
            "runtime_seconds": round(time.monotonic() - started, 3),
        })

    return write_final({
        "status": "NO_TRADE",
        "reason": "no_a_plus",
        "message": "NO TRADE — no A+ setup. DO NOT BUY.",
        "order_instruction": "NO_ORDER",
        "runtime_seconds": round(time.monotonic() - started, 3),
    })
