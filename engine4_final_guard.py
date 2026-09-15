from __future__ import annotations

import json
import math
import time
from datetime import datetime, timezone

import pandas as pd

import engine4_live
from engine4_config import ET, MAX_BREAKOUT_CHASE_PCT, MAX_TRADABLE_PRICE, RECOVERY_WATCH_COUNT, SECTOR_ETF
from engine4_data import download_intraday, now_et
from engine4_intraday import OUT, serializable, write_final
from engine4_live import live_quality, market_context, opening_structure


PROFIT_LOCK_R = 0.50


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


def _precalculated_profit_stop(trigger: float, initial_stop: float) -> float:
    if not (math.isfinite(trigger) and math.isfinite(initial_stop) and trigger > initial_stop):
        return math.nan
    risk_per_share = trigger - initial_stop
    return trigger + PROFIT_LOCK_R * risk_per_share


def _write_recovery_watch(date_et, candidates: list[tuple[float, pd.Series, dict]]) -> None:
    candidates.sort(key=lambda item: item[0], reverse=True)
    selected = candidates[:RECOVERY_WATCH_COUNT]
    payload = {
        "target_date_et": str(date_et),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "max_tradable_price": MAX_TRADABLE_PRICE,
        "requested_count": RECOVERY_WATCH_COUNT,
        "actual_count": len(selected),
        "candidates": [],
    }
    for quality, row, metrics in selected:
        payload["candidates"].append({
            "ticker": str(row.ticker),
            "rank": serializable(row.get("rank")),
            "score": serializable(row.get("score")),
            "premarket_grade": row.get("premarket_grade"),
            "sector": str(row.get("sector", "")),
            "quality_at_0945": serializable(quality),
            "last_0945": serializable(metrics.get("last")),
            "vwap_0945": serializable(metrics.get("vwap")),
            "opening_range_high": serializable(metrics.get("opening_range_high")),
            "primary_failures": list(metrics.get("failures", [])),
        })
    (OUT / "recovery_watch.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")


def guarded_final_stage(date_override: str | None = None) -> dict:
    """Final Engine 4 stage: frozen Top-25 only, with live entry guard and hook-set handoff."""
    started = time.monotonic()
    reference = now_et() if date_override is None else datetime.fromisoformat(date_override + "T09:45:00").replace(tzinfo=ET)
    date_et = reference.date()
    frozen_path = OUT / "top25_frozen.csv"
    if not frozen_path.exists() or frozen_path.stat().st_size < 5:
        return write_final({
            "status": "PIPELINE_FAILURE",
            "reason": "missing_top25",
            "message": "ENGINE 4 DATA/PIPELINE FAILURE — frozen Top 25 unavailable.",
            "order_instruction": "NO_ORDER",
            "runtime_seconds": round(time.monotonic() - started, 3),
        })

    try:
        top = pd.read_csv(frozen_path)
    except Exception:
        top = pd.DataFrame()
    if top.empty or "ticker" not in top.columns:
        return write_final({
            "status": "PIPELINE_FAILURE",
            "reason": "empty_top25",
            "message": "ENGINE 4 DATA/PIPELINE FAILURE — frozen Top 25 is empty or invalid.",
            "order_instruction": "NO_ORDER",
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
    shadow_only = []
    recovery_pool = []

    for _, row in top.iterrows():
        symbol = str(row.ticker)
        frame = candidate_frames.get(symbol)
        if frame is None or frame.empty:
            audit.append({"ticker": symbol, "pass": False, "failures": ["missing_live_data"]})
            continue

        metrics = opening_structure(symbol, frame, row, market, date_et)
        metrics["max_tradable_price"] = MAX_TRADABLE_PRICE
        opening_last = float(metrics.get("last", math.nan))
        officially_tradable = bool(math.isfinite(opening_last) and opening_last <= MAX_TRADABLE_PRICE)
        metrics["officially_tradable"] = officially_tradable

        failures = [f for f in list(metrics.get("failures", [])) if f != "entry_missed"]
        metrics["failures_before_current_price_guard"] = list(failures)

        # Preserve promising failed names under the account-size price cap so the
        # post-open recovery module can keep the fish on the hook instead of
        # permanently discarding a top-ranked candidate after one failed setup.
        if metrics.get("data_ok") and officially_tradable and not metrics.get("hard_market_reversal", False):
            try:
                recovery_quality = live_quality(float(row.get("score", 0)), metrics)
            except Exception:
                recovery_quality = float(row.get("score", 0) or 0)
            if failures:
                recovery_pool.append((recovery_quality, row, metrics.copy()))

        if failures:
            metrics["pass"] = False
            audit.append(metrics)
            continue

        current, bid, ask, spread = _current_mid(symbol)
        trigger = float(metrics.get("entry_trigger", math.nan))
        initial_stop = float(metrics.get("initial_stop", math.nan))
        max_allowed = trigger * (1.0 + MAX_BREAKOUT_CHASE_PCT / 100.0) if math.isfinite(trigger) else math.nan
        profit_protection_stop = _precalculated_profit_stop(trigger, initial_stop)
        seen = _trigger_seen(frame, date_et, trigger)
        current_tradable = bool(math.isfinite(current) and current <= MAX_TRADABLE_PRICE)
        metrics.update({
            "current_live_price": current,
            "current_bid": bid,
            "current_ask": ask,
            "current_spread_pct": spread,
            "max_allowed_buy_price": max_allowed,
            "precalculated_profit_stop": profit_protection_stop,
            "profit_lock_r": PROFIT_LOCK_R,
            "trigger_seen_today": seen,
            "officially_tradable": current_tradable,
        })

        if not math.isfinite(current):
            metrics["pass"] = False
            metrics["failures"] = ["missing_current_live_price"]
            audit.append(metrics)
            continue

        quality = live_quality(float(row.get("score", 0)), metrics)

        # $100 is an execution gate, not a research gate. High-priced names stay
        # in the audit as shadow validation but can never become the official trade.
        if not current_tradable:
            metrics["pass"] = False
            metrics["shadow_only"] = True
            metrics["failures"] = ["price_above_trade_cap"]
            shadow_only.append((quality, row, metrics))
            audit.append(metrics)
            continue

        if current < trigger:
            metrics["pass"] = False
            if seen:
                metrics["failures"] = ["entry_missed_breakout_failed"]
                missed.append((quality, row, metrics))
                recovery_pool.append((quality, row, metrics.copy()))
            else:
                metrics["failures"] = ["trigger_not_reached"]
                watches.append((quality, row, metrics))
        elif current > max_allowed:
            metrics["pass"] = False
            metrics["failures"] = ["entry_missed_chase_band"]
            missed.append((quality, row, metrics))
            recovery_pool.append((quality, row, metrics.copy()))
        else:
            metrics["pass"] = True
            metrics["failures"] = []
            buyable.append((quality, row, metrics))
        audit.append(metrics)

    _write_recovery_watch(date_et, recovery_pool)

    (OUT / "final_live_audit.json").write_text(json.dumps({
        "target_date_et": str(date_et),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "max_tradable_price": MAX_TRADABLE_PRICE,
        "market": {k: serializable(v) for k, v in market.items()},
        "shadow_only_count": len(shadow_only),
        "recovery_watch_count": min(len(recovery_pool), RECOVERY_WATCH_COUNT),
        "candidates": [{k: serializable(v) for k, v in item.items()} for item in audit],
    }, indent=2), encoding="utf-8")

    if buyable:
        buyable.sort(key=lambda item: item[0], reverse=True)
        _, row, metrics = buyable[0]
        symbol = str(row.ticker)
        message = (
            f"BUY {symbol} NOW\n"
            f"BUY BETWEEN ${metrics['entry_trigger']:.2f} AND ${metrics['max_allowed_buy_price']:.2f}\n"
            f"AFTER PURCHASE, ENTER SELL STOP AT ${metrics['initial_stop']:.2f}\n"
            f"IF PRICE RISES TO ${metrics['first_target']:.2f}, MOVE SELL STOP TO ${metrics['precalculated_profit_stop']:.2f}\n"
            f"DO NOT BUY ABOVE ${metrics['max_allowed_buy_price']:.2f}\n"
            f"Current price: ${metrics['current_live_price']:.2f}\n"
            f"Reason: full A+ gates passed and fresh live price is inside the valid buy range; R:R {metrics['reward_risk']:.2f}:1."
        )
        return write_final({
            "status": "BUY",
            "reason": "live_trigger_confirmed",
            "ticker": symbol,
            "message": message,
            "order_instruction": "BUY_NOW",
            "live_price": metrics["current_live_price"],
            "entry_trigger": metrics["entry_trigger"],
            "max_allowed_buy_price": metrics["max_allowed_buy_price"],
            "initial_stop": metrics["initial_stop"],
            "first_target": metrics["first_target"],
            "precalculated_profit_stop": metrics["precalculated_profit_stop"],
            "profit_lock_r": PROFIT_LOCK_R,
            "reward_risk": metrics["reward_risk"],
            "max_tradable_price": MAX_TRADABLE_PRICE,
            "runtime_seconds": round(time.monotonic() - started, 3),
        })

    if watches:
        watches.sort(key=lambda item: item[0], reverse=True)
        _, row, metrics = watches[0]
        symbol = str(row.ticker)
        message = (
            f"PLACE BUY STOP-LIMIT NOW — {symbol}\n"
            f"STOP PRICE: ${metrics['entry_trigger']:.2f}\n"
            f"LIMIT PRICE: ${metrics['max_allowed_buy_price']:.2f}\n"
            f"TIME IN FORCE: DAY\n"
            f"CURRENT PRICE: ${metrics['current_live_price']:.2f}\n"
            f"IF FILLED, ENTER GTC SELL STOP AT ${metrics['initial_stop']:.2f}\n"
            f"IF PRICE THEN RISES TO ${metrics['first_target']:.2f}, MOVE SELL STOP TO ${metrics['precalculated_profit_stop']:.2f}\n"
            f"DO NOT CHASE ABOVE ${metrics['max_allowed_buy_price']:.2f}"
        )
        return write_final({
            "status": "ARM",
            "reason": "trigger_not_reached",
            "ticker": symbol,
            "message": message,
            "order_instruction": "ARM_STOP_LIMIT_DAY",
            "live_price": metrics["current_live_price"],
            "stop_price": metrics["entry_trigger"],
            "limit_price": metrics["max_allowed_buy_price"],
            "entry_trigger": metrics["entry_trigger"],
            "max_allowed_buy_price": metrics["max_allowed_buy_price"],
            "initial_stop": metrics["initial_stop"],
            "first_target": metrics["first_target"],
            "precalculated_profit_stop": metrics["precalculated_profit_stop"],
            "profit_lock_r": PROFIT_LOCK_R,
            "max_tradable_price": MAX_TRADABLE_PRICE,
            "runtime_seconds": round(time.monotonic() - started, 3),
        })

    if missed:
        missed.sort(key=lambda item: item[0], reverse=True)
        _, row, metrics = missed[0]
        return write_final({
            "status": "NO_TRADE",
            "reason": "entry_missed_recovery_watch_active",
            "ticker": str(row.ticker),
            "message": "NO PRIMARY TRADE — entry missed / breakout failed. RECOVERY WATCH remains active on eligible top candidates.",
            "order_instruction": "NO_ORDER",
            "live_price": metrics.get("current_live_price"),
            "entry_trigger": metrics.get("entry_trigger"),
            "max_tradable_price": MAX_TRADABLE_PRICE,
            "runtime_seconds": round(time.monotonic() - started, 3),
        })

    if shadow_only:
        shadow_only.sort(key=lambda item: item[0], reverse=True)
        _, row, metrics = shadow_only[0]
        return write_final({
            "status": "NO_TRADE",
            "reason": "best_setup_above_trade_cap",
            "ticker": str(row.ticker),
            "message": (
                f"NO OFFICIAL TRADE — strongest live setup is above the ${MAX_TRADABLE_PRICE:.0f} share-price cap. "
                "It remains shadow-tracked for Engine 4 validation."
            ),
            "order_instruction": "NO_ORDER",
            "live_price": metrics.get("current_live_price"),
            "max_tradable_price": MAX_TRADABLE_PRICE,
            "runtime_seconds": round(time.monotonic() - started, 3),
        })

    return write_final({
        "status": "NO_TRADE",
        "reason": "no_a_plus_recovery_watch_active",
        "message": "NO PRIMARY TRADE — no A+ setup. Eligible top candidates remain on RECOVERY WATCH until the locked timeout.",
        "order_instruction": "NO_ORDER",
        "max_tradable_price": MAX_TRADABLE_PRICE,
        "runtime_seconds": round(time.monotonic() - started, 3),
    })
