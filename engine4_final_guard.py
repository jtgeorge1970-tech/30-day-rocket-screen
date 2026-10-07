from __future__ import annotations

import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

import engine4_live
from engine4_config import (
    ET,
    MAX_BREAKOUT_CHASE_PCT,
    MAX_SPREAD_PCT,
    MAX_PREMARKET_DEFERRED_SPREAD_PCT,
    MAX_TRADABLE_PRICE,
    MIN_ATR_PCT,
    MIN_SCORE,
    RECOVERY_WATCH_COUNT,
    SECTOR_ETF,
)
from engine4_data import download_intraday, now_et
from engine4_intraday import OUT, serializable, write_final
from engine4_live import live_quality, market_context, opening_structure


PROFIT_LOCK_R = 0.50
BENCH_STATE = Path("state/engine4/watch_bench.json")

# These conditions are deliberately re-checked at the actual breakout instead of
# permanently vetoing a high-quality finalist from one 09:45 snapshot.
DEFERRED_TRIGGER_FAILURES = frozenset({
    "not_attacking_breakout",
    "breakout_volume_not_expanding",
    "spread",
    "reward_risk_below_2",
})


def _split_opening_failures(failures: list[str]) -> tuple[list[str], list[str]]:
    hard = [f for f in failures if f not in DEFERRED_TRIGGER_FAILURES and f != "entry_missed"]
    deferred = [f for f in failures if f in DEFERRED_TRIGGER_FAILURES]
    return hard, deferred


def _artifact_bool(value) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)) and math.isfinite(float(value)):
        return bool(value)
    return str(value).strip().lower() in {"true", "1", "yes"}


def _premarket_eligibility_failures(row: pd.Series) -> list[str]:
    """Revalidate selection quality without confusing selection with execution.

    Fresh >=80 launchpad names may defer an authoritative premarket spread up to
    the configured research cap; the live quote still must be <= MAX_SPREAD_PCT
    before a BUY. Prior HOT continuation candidates use their proven origin B
    score and are judged by the live continuation structure instead of being
    forced to recreate yesterday's catalyst/volume profile.
    """
    failures = []
    continuation = _artifact_bool(row.get("continuation_candidate", False))
    score = pd.to_numeric(pd.Series([row.get("score")]), errors="coerce").iloc[0]
    spread = pd.to_numeric(pd.Series([row.get("spread_pct")]), errors="coerce").iloc[0]

    if continuation:
        origin_score = pd.to_numeric(
            pd.Series([row.get("continuation_origin_score")]), errors="coerce"
        ).iloc[0]
        last_price = pd.to_numeric(
            pd.Series([row.get("last_premarket")]), errors="coerce"
        ).iloc[0]
        if not math.isfinite(origin_score) or origin_score < MIN_SCORE:
            failures.append("continuation_origin_below_80")
        if not math.isfinite(last_price) or last_price > MAX_TRADABLE_PRICE:
            failures.append("continuation_price_above_cap")
        if math.isfinite(spread) and spread > MAX_PREMARKET_DEFERRED_SPREAD_PCT:
            failures.append("continuation_premarket_spread_excessive")
        return failures

    catalyst = pd.to_numeric(pd.Series([row.get("catalyst_quality")]), errors="coerce").iloc[0]
    atr_pct = pd.to_numeric(pd.Series([row.get("atr_pct")]), errors="coerce").iloc[0]
    room = pd.to_numeric(pd.Series([row.get("resistance_room_pct")]), errors="coerce").iloc[0]

    if not _artifact_bool(row.get("premarket_eligible", False)):
        failures.append("not_launchpad_eligible")
    if not math.isfinite(score) or score < MIN_SCORE:
        failures.append("premarket_score_below_80")
    if not math.isfinite(catalyst) or catalyst <= 0:
        failures.append("missing_verified_catalyst")
    if not _artifact_bool(row.get("premarket_volume_gate_pass", False)):
        failures.append("premarket_volume_strength")
    if not math.isfinite(atr_pct) or atr_pct < MIN_ATR_PCT:
        failures.append("premarket_atr")
    if not math.isfinite(room) or room <= 0:
        failures.append("premarket_room")
    if not _artifact_bool(row.get("spread_order_authoritative", False)):
        failures.append("premarket_spread_not_authoritative")
    if not math.isfinite(spread) or spread > MAX_PREMARKET_DEFERRED_SPREAD_PCT:
        failures.append("premarket_spread_excessive")
    return failures


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
            "previous_close": serializable(row.get("previous_close")),
            "resistance_price": serializable(row.get("resistance_price")),
            "primary_failures": list(metrics.get("failures", [])),
            "deferred_trigger_checks": list(metrics.get("deferred_trigger_checks", [])),
            "continuation_candidate": _artifact_bool(row.get("continuation_candidate", False)),
            "continuation_origin_score": serializable(row.get("continuation_origin_score")),
            "continuation_entry_mode": row.get("continuation_entry_mode"),
            "frozen_entry_trigger": (
                None
                if _artifact_bool(row.get("continuation_candidate", False))
                else serializable(metrics.get("frozen_entry_trigger"))
            ),
            "frozen_breakout_level": serializable(metrics.get("frozen_breakout_level")),
            "candidate_source": row.get("candidate_source", "TODAY_LAUNCHPAD"),
        })
    (OUT / "recovery_watch.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _hot_bench(date_et) -> pd.DataFrame:
    try:
        payload = json.loads(BENCH_STATE.read_text(encoding="utf-8"))
    except Exception:
        return pd.DataFrame()
    if payload.get("target_date_et") != str(date_et):
        return pd.DataFrame()
    rows = [
        row for row in payload.get("candidates", [])
        if row.get("tier") == "HOT" or _artifact_bool(row.get("continuation_candidate", False))
    ]
    rows.sort(key=lambda row: float(row.get("watch_priority") or 0.0), reverse=True)
    return pd.DataFrame(rows[:5])


def guarded_final_stage(date_override: str | None = None) -> dict:
    """Final stage: today's launchpad plus the freshly scored Hot-5 Bench."""
    started = time.monotonic()
    reference = now_et() if date_override is None else datetime.fromisoformat(date_override + "T09:45:00").replace(tzinfo=ET)
    date_et = reference.date()
    def finish(payload: dict) -> dict:
        payload["target_date_et"] = str(date_et)
        return write_final(payload)

    frozen_json = OUT / "top25_frozen.json"
    if not frozen_json.exists():
        return finish({
            "status": "PIPELINE_FAILURE",
            "reason": "missing_frozen_artifact",
            "message": "ENGINE 4 DATA/PIPELINE FAILURE — dated freeze artifact unavailable.",
            "order_instruction": "NO_ORDER",
            "runtime_seconds": round(time.monotonic() - started, 3),
        })
    frozen_meta = json.loads(frozen_json.read_text(encoding="utf-8"))
    if frozen_meta.get("target_date_et") != str(date_et):
        return finish({
            "status": "PIPELINE_FAILURE",
            "reason": "frozen_artifact_date_mismatch",
            "message": "ENGINE 4 DATA/PIPELINE FAILURE — frozen shortlist date does not match the active ET market date.",
            "order_instruction": "NO_ORDER",
            "runtime_seconds": round(time.monotonic() - started, 3),
        })
    frozen_path = OUT / "top25_frozen.csv"
    if not frozen_path.exists() or frozen_path.stat().st_size < 5:
        return finish({
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
    if "ticker" not in top.columns:
        return finish({
            "status": "PIPELINE_FAILURE",
            "reason": "invalid_top25",
            "message": "ENGINE 4 DATA/PIPELINE FAILURE — frozen launchpad artifact is invalid.",
            "order_instruction": "NO_ORDER",
            "runtime_seconds": round(time.monotonic() - started, 3),
        })
    if not top.empty:
        top["candidate_source"] = "TODAY_LAUNCHPAD"
    bench_hot = _hot_bench(date_et)
    if not bench_hot.empty:
        bench_hot["candidate_source"] = "BENCH_HOT"
        if top.empty:
            top = bench_hot.copy()
        else:
            top = pd.concat([top, bench_hot], ignore_index=True)
            top = top.drop_duplicates(subset=["ticker"], keep="first").reset_index(drop=True)

    if top.empty:
        _write_recovery_watch(date_et, [])
        (OUT / "final_live_audit.json").write_text(json.dumps({
            "target_date_et": str(date_et),
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "max_tradable_price": MAX_TRADABLE_PRICE,
            "status": "NO_QUALIFIED_LAUNCHPAD_OR_HOT_BENCH",
            "candidates": [],
        }, indent=2), encoding="utf-8")
        return finish({
            "status": "NO_TRADE",
            "reason": "no_b_or_better_premarket_candidates",
            "message": "NO TRADE — no B-or-better premarket candidates. DO NOT BUY.",
            "order_instruction": "NO_ORDER",
            "max_tradable_price": MAX_TRADABLE_PRICE,
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
        premarket_failures = _premarket_eligibility_failures(row)
        if premarket_failures:
            audit.append({
                "ticker": symbol,
                "pass": False,
                "failures": premarket_failures,
                "stage": "premarket_eligibility_recheck",
            })
            continue
        frame = candidate_frames.get(symbol)
        if frame is None or frame.empty:
            audit.append({"ticker": symbol, "pass": False, "failures": ["missing_live_data"]})
            continue

        metrics = opening_structure(symbol, frame, row, market, date_et)
        metrics["candidate_source"] = row.get("candidate_source", "TODAY_LAUNCHPAD")
        metrics["max_tradable_price"] = MAX_TRADABLE_PRICE
        opening_last = float(metrics.get("last", math.nan))
        officially_tradable = bool(math.isfinite(opening_last) and opening_last <= MAX_TRADABLE_PRICE)
        metrics["officially_tradable"] = officially_tradable

        opening_failures = list(metrics.get("failures", []))
        hard_failures, deferred_failures = _split_opening_failures(opening_failures)
        metrics["failures_before_current_price_guard"] = list(opening_failures)
        metrics["hard_opening_failures"] = list(hard_failures)
        metrics["deferred_trigger_checks"] = list(deferred_failures)

        if hard_failures:
            # Hard structural failures still fail closed. They may remain on the
            # recovery watch only if they are an otherwise valid, affordable
            # finalist and the broad market has not hard-reversed.
            metrics["pass"] = False
            metrics["failures"] = list(hard_failures)
            if metrics.get("data_ok") and officially_tradable and not metrics.get("hard_market_reversal", False):
                try:
                    recovery_quality = live_quality(float(row.get("score", 0)), metrics)
                except Exception:
                    recovery_quality = float(row.get("score", 0) or 0)
                recovery_pool.append((recovery_quality, row, metrics.copy()))
            audit.append(metrics)
            continue

        current, bid, ask, spread = _current_mid(symbol)
        trigger = float(metrics.get("entry_trigger", math.nan))
        initial_stop = float(metrics.get("initial_stop", math.nan))
        max_allowed = trigger * (1.0 + MAX_BREAKOUT_CHASE_PCT / 100.0) if math.isfinite(trigger) else math.nan
        profit_protection_stop = _precalculated_profit_stop(trigger, initial_stop)
        seen = _trigger_seen(frame, date_et, trigger)
        current_tradable = bool(math.isfinite(current) and current <= MAX_TRADABLE_PRICE)
        reward_risk = float(metrics.get("reward_risk", math.nan))
        spread_ok_now = bool(math.isfinite(spread) and spread <= MAX_SPREAD_PCT)
        reward_risk_ok_now = bool(math.isfinite(reward_risk) and reward_risk >= 2.0)
        opening_breakout_volume_ok = "breakout_volume_not_expanding" not in deferred_failures
        metrics.update({
            "current_live_price": current,
            "current_bid": bid,
            "current_ask": ask,
            "current_spread_pct": spread,
            "current_spread_ok": spread_ok_now,
            "reward_risk_ok": reward_risk_ok_now,
            "opening_breakout_volume_ok": opening_breakout_volume_ok,
            "max_allowed_buy_price": max_allowed,
            "precalculated_profit_stop": profit_protection_stop,
            "profit_lock_r": PROFIT_LOCK_R,
            "trigger_seen_today": seen,
            "officially_tradable": current_tradable,
            # Freeze the primary breakout line now. Stage 5 may improve the stop
            # after a retest, but it must not chase this trigger upward.
            "frozen_entry_trigger": trigger,
            "frozen_breakout_level": float(metrics.get("opening_range_high", math.nan)),
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
            else:
                metrics["failures"] = ["frozen_trigger_wait"]
                watches.append((quality, row, metrics))
            recovery_pool.append((quality, row, metrics.copy()))
        elif current > max_allowed:
            metrics["pass"] = False
            metrics["failures"] = ["entry_missed_chase_band"]
            missed.append((quality, row, metrics))
            recovery_pool.append((quality, row, metrics.copy()))
        else:
            trigger_failures = []
            # The spread is intentionally re-checked from the fresh quote at the
            # trigger; the earlier 09:45 spread snapshot is not a permanent veto.
            if not spread_ok_now:
                trigger_failures.append("spread_at_trigger")
            # Keep the locked 2R discipline. If the opening stop is too wide,
            # Stage 5 waits for a higher-low/retest and recalculates risk.
            if not reward_risk_ok_now:
                trigger_failures.append("reward_risk_below_2_at_trigger")
            # If breakout demand was not confirmed in the opening snapshot, do not
            # buy blindly; Stage 5 re-evaluates improving demand every minute.
            if not opening_breakout_volume_ok:
                trigger_failures.append("breakout_volume_not_confirmed")

            if trigger_failures:
                metrics["pass"] = False
                metrics["failures"] = trigger_failures
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
        "today_launchpad_count": int((top.candidate_source == "TODAY_LAUNCHPAD").sum()),
        "bench_hot_count": int((top.candidate_source == "BENCH_HOT").sum()),
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
            f"Reason: B-or-better premarket eligibility and all required live entry gates passed; fresh live price is inside the valid buy range; R:R {metrics['reward_risk']:.2f}:1."
        )
        return finish({
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
            "selection_source": row.get("candidate_source", "TODAY_LAUNCHPAD"),
        })

    if watches:
        watches.sort(key=lambda item: item[0], reverse=True)
        _, row, metrics = watches[0]
        symbol = str(row.ticker)
        message = (
            f"FROZEN BREAKOUT WATCH — {symbol}\n"
            f"TRIGGER: ${metrics['entry_trigger']:.2f}\n"
            f"CURRENT PRICE: ${metrics['current_live_price']:.2f}\n"
            "NO BROKER ORDER YET — Engine 4 will re-check live spread, breakout demand, "
            "and >=2R risk/reward at the trigger. Stage 5 monitors the fixed trigger every minute."
        )
        return finish({
            "status": "WATCH_TRIGGER",
            "reason": "frozen_breakout_trigger_wait",
            "ticker": symbol,
            "message": message,
            "order_instruction": "NO_ORDER_MONITOR_TRIGGER",
            "live_price": metrics["current_live_price"],
            "entry_trigger": metrics["entry_trigger"],
            "frozen_entry_trigger": metrics["frozen_entry_trigger"],
            "max_allowed_buy_price": metrics["max_allowed_buy_price"],
            "initial_stop": metrics["initial_stop"],
            "first_target": metrics["first_target"],
            "precalculated_profit_stop": metrics["precalculated_profit_stop"],
            "profit_lock_r": PROFIT_LOCK_R,
            "max_tradable_price": MAX_TRADABLE_PRICE,
            "runtime_seconds": round(time.monotonic() - started, 3),
            "selection_source": row.get("candidate_source", "TODAY_LAUNCHPAD"),
        })

    if missed:
        missed.sort(key=lambda item: item[0], reverse=True)
        _, row, metrics = missed[0]
        return finish({
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
        return finish({
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

    return finish({
        "status": "NO_TRADE",
        "reason": "no_live_entry_setup_recovery_watch_active",
        "message": "NO PRIMARY TRADE — no B-or-better candidate passed all required live entry gates. Eligible top candidates remain on RECOVERY WATCH until the locked timeout.",
        "order_instruction": "NO_ORDER",
        "max_tradable_price": MAX_TRADABLE_PRICE,
        "runtime_seconds": round(time.monotonic() - started, 3),
    })
