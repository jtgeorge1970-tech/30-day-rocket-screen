from __future__ import annotations

"""Engine 4 post-open hook-set / recovery monitor.

This module does not replace the primary 09:45 breakout engine. It watches only a
small set of already-ranked, officially tradable names that failed the first setup.
Its job is to recognize the VERA-style sequence: hard opening flush -> exhaustion
base -> higher low -> improving demand -> reclaim trigger. Once a base is valid it
can arm a broker-side stop-limit order so the user does not have to stare at charts.
"""

import argparse
import json
import math
import time
from datetime import datetime, timezone

import pandas as pd

import engine4_live
import engine4_pipeline_runner as base
from engine4_config import (
    ET,
    MAX_SPREAD_PCT,
    MAX_TRADABLE_PRICE,
    RECOVERY_END_HOUR_ET,
    RECOVERY_END_MINUTE_ET,
    RECOVERY_HIGHER_LOW_BUFFER_PCT,
    RECOVERY_MAX_BASE_RANGE_PCT,
    RECOVERY_MAX_CHASE_PCT,
    RECOVERY_MAX_EXTENSION_PCT,
    RECOVERY_MIN_BARS_SINCE_LOW,
    RECOVERY_MIN_FLUSH_PCT,
    RECOVERY_MIN_GREEN_BARS,
    RECOVERY_MIN_VOLUME_EXPANSION,
    RECOVERY_SCAN_INTERVAL_SECONDS,
    RECOVERY_STOP_BUFFER_PCT,
    RECOVERY_TARGET_R,
    RECOVERY_TRIGGER_BUFFER_PCT,
    MIN_REWARD_RISK,
)
from engine4_data import download_intraday, now_et
from engine4_intraday import OUT, serializable


PROFIT_LOCK_R = 0.50


def _read_json(path):
    if not path.exists() or path.stat().st_size < 3:
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _current_mid(symbol: str) -> tuple[float, float, float, float]:
    bid, ask, spread = engine4_live.quote_spread(symbol)
    if not (math.isfinite(bid) and math.isfinite(ask) and bid > 0 and ask >= bid):
        return math.nan, bid, ask, spread
    return (bid + ask) / 2.0, bid, ask, spread


def _precalculated_profit_stop(trigger: float, stop: float) -> float:
    if not (math.isfinite(trigger) and math.isfinite(stop) and trigger > stop):
        return math.nan
    return trigger + PROFIT_LOCK_R * (trigger - stop)


def recovery_metrics(
    symbol: str,
    frame: pd.DataFrame,
    date_et,
    previous_close: float = math.nan,
    resistance_price: float = math.nan,
) -> dict:
    if frame is None or frame.empty:
        return {"ticker": symbol, "data_ok": False, "failures": ["missing_live_data"]}

    same_day = frame[frame.index.date == date_et]
    if same_day.empty:
        return {"ticker": symbol, "data_ok": False, "failures": ["missing_same_day_data"]}
    regular = same_day.between_time("09:30", "11:30", inclusive="both").copy()
    if len(regular) < 20:
        return {"ticker": symbol, "data_ok": False, "failures": ["insufficient_recovery_bars"]}

    close = pd.to_numeric(regular["Close"], errors="coerce")
    opening = pd.to_numeric(regular["Open"], errors="coerce")
    high = pd.to_numeric(regular["High"], errors="coerce")
    low = pd.to_numeric(regular["Low"], errors="coerce")
    volume = pd.to_numeric(regular["Volume"], errors="coerce").fillna(0)
    valid = close.notna() & high.notna() & low.notna()
    regular = regular.loc[valid]
    close = close.loc[valid]
    opening = opening.loc[valid]
    high = high.loc[valid]
    low = low.loc[valid]
    volume = volume.loc[valid]
    if len(regular) < 20:
        return {"ticker": symbol, "data_ok": False, "failures": ["insufficient_valid_recovery_bars"]}

    current_bar_close = float(close.iloc[-1])
    session_high = float(high.max())
    session_low = float(low.min())
    low_pos = int(low.to_numpy().argmin())
    bars_since_low = len(low) - 1 - low_pos
    flush_pct = (session_high / session_low - 1.0) * 100.0 if session_low > 0 else math.nan

    post_low = regular.iloc[low_pos:]
    post_low_close = close.iloc[low_pos:]
    post_low_high = high.iloc[low_pos:]
    post_low_low = low.iloc[low_pos:]
    post_low_volume = volume.iloc[low_pos:]

    lookback = min(10, len(post_low))
    base_high = float(post_low_high.iloc[-lookback:].max()) if lookback >= 2 else math.nan
    base_low = float(post_low_low.iloc[-lookback:].min()) if lookback >= 2 else math.nan
    base_range_pct = ((base_high - base_low) / current_bar_close * 100.0) if current_bar_close > 0 and math.isfinite(base_high) else math.nan

    recent_lows = post_low_low.iloc[-5:] if len(post_low_low) >= 5 else post_low_low
    recent_low = float(recent_lows.min()) if len(recent_lows) else math.nan
    higher_low = bool(
        math.isfinite(recent_low)
        and recent_low >= session_low * (1.0 + RECOVERY_HIGHER_LOW_BUFFER_PCT / 100.0)
    )

    recent = regular.iloc[-4:]
    green_bars = int((pd.to_numeric(recent["Close"], errors="coerce") > pd.to_numeric(recent["Open"], errors="coerce")).sum())

    prior_vol = volume.iloc[-9:-4] if len(volume) >= 9 else volume.iloc[:-4]
    recent_vol = volume.iloc[-4:]
    prior_vol_mean = float(prior_vol.mean()) if len(prior_vol) else math.nan
    recent_vol_mean = float(recent_vol.mean()) if len(recent_vol) else math.nan
    volume_expansion = (
        recent_vol_mean / prior_vol_mean
        if math.isfinite(prior_vol_mean) and prior_vol_mean > 0 and math.isfinite(recent_vol_mean)
        else math.nan
    )

    # A recovery entry must clear both the recent base and the existing session high.
    # The old base-only trigger could buy directly into the session-high resistance,
    # as happened in the verified FPS September 16 dry run.
    breakout_level = max(base_high, session_high) if math.isfinite(base_high) else session_high
    trigger = breakout_level * (1.0 + RECOVERY_TRIGGER_BUFFER_PCT / 100.0) if math.isfinite(breakout_level) else math.nan
    raw_max_allowed = trigger * (1.0 + RECOVERY_MAX_CHASE_PCT / 100.0) if math.isfinite(trigger) else math.nan
    stop = recent_low * (1.0 - RECOVERY_STOP_BUFFER_PCT / 100.0) if math.isfinite(recent_low) else math.nan
    if math.isfinite(stop) and math.isfinite(trigger) and stop >= trigger:
        stop = session_low * (1.0 - RECOVERY_STOP_BUFFER_PCT / 100.0)
    risk = trigger - stop if math.isfinite(trigger) and math.isfinite(stop) else math.nan
    formula_target = trigger + RECOVERY_TARGET_R * risk if math.isfinite(risk) and risk > 0 else math.nan
    if math.isfinite(resistance_price) and resistance_price > trigger:
        first_target = min(formula_target, resistance_price)
    else:
        first_target = formula_target

    # The maximum permitted fill must still preserve the locked 2R minimum. Shrink
    # the chase band when necessary; if even the trigger lacks 2R, fail closed.
    rr_max_fill_price = (
        (first_target + MIN_REWARD_RISK * stop) / (1.0 + MIN_REWARD_RISK)
        if math.isfinite(first_target) and math.isfinite(stop)
        else math.nan
    )
    max_allowed = min(raw_max_allowed, rr_max_fill_price) if math.isfinite(rr_max_fill_price) else math.nan
    reward_risk_at_trigger = (
        (first_target - trigger) / (trigger - stop)
        if math.isfinite(first_target) and math.isfinite(trigger) and math.isfinite(stop) and trigger > stop
        else math.nan
    )
    reward_risk_at_max_fill = (
        (first_target - max_allowed) / (max_allowed - stop)
        if math.isfinite(first_target) and math.isfinite(max_allowed) and math.isfinite(stop) and max_allowed > stop
        else math.nan
    )
    extension_at_trigger_pct = (
        (trigger / previous_close - 1.0) * 100.0
        if math.isfinite(previous_close) and previous_close > 0 and math.isfinite(trigger)
        else math.nan
    )
    profit_stop = _precalculated_profit_stop(trigger, stop)

    current_vwap = engine4_live.vwap(regular)
    recovery_from_low_pct = (current_bar_close / session_low - 1.0) * 100.0 if session_low > 0 else math.nan

    current, bid, ask, spread = _current_mid(symbol)
    if not math.isfinite(current):
        current = current_bar_close

    failures = []
    if not math.isfinite(flush_pct) or flush_pct < RECOVERY_MIN_FLUSH_PCT:
        failures.append("opening_flush_not_large_enough")
    if bars_since_low < RECOVERY_MIN_BARS_SINCE_LOW:
        failures.append("low_not_old_enough_to_confirm_base")
    if not higher_low:
        failures.append("no_confirmed_higher_low")
    if not math.isfinite(base_range_pct) or base_range_pct > RECOVERY_MAX_BASE_RANGE_PCT:
        failures.append("base_not_tight_enough")
    if green_bars < RECOVERY_MIN_GREEN_BARS:
        failures.append("insufficient_green_bars")
    if not math.isfinite(volume_expansion) or volume_expansion < RECOVERY_MIN_VOLUME_EXPANSION:
        failures.append("demand_volume_not_improving")
    if not math.isfinite(spread) or spread > MAX_SPREAD_PCT:
        failures.append("spread")
    if not math.isfinite(current) or current > MAX_TRADABLE_PRICE:
        failures.append("price_above_trade_cap")
    if math.isfinite(current) and current < session_low:
        failures.append("new_structural_low")
    if not math.isfinite(previous_close) or previous_close <= 0:
        failures.append("missing_previous_close_for_extension")
    elif not math.isfinite(extension_at_trigger_pct) or extension_at_trigger_pct > RECOVERY_MAX_EXTENSION_PCT:
        failures.append("recovery_entry_excessively_extended")
    if not math.isfinite(reward_risk_at_trigger) or reward_risk_at_trigger < MIN_REWARD_RISK:
        failures.append("insufficient_reward_risk_before_resistance")
    if not math.isfinite(reward_risk_at_max_fill) or reward_risk_at_max_fill + 1e-9 < MIN_REWARD_RISK:
        failures.append("insufficient_reward_risk_at_max_fill")
    if not math.isfinite(max_allowed) or max_allowed < trigger:
        failures.append("no_safe_chase_band")

    setup_ready = len(failures) == 0
    if setup_ready and current < trigger:
        state = "ARM"
    elif setup_ready and trigger <= current <= max_allowed:
        state = "BUY"
    elif setup_ready and current > max_allowed:
        state = "MISSED"
    else:
        state = "WATCH"

    return {
        "ticker": symbol,
        "data_ok": True,
        "state": state,
        "setup_ready": setup_ready,
        "current_price": current,
        "current_bar_close": current_bar_close,
        "live_bid": bid,
        "live_ask": ask,
        "live_spread_pct": spread,
        "session_high": session_high,
        "session_low": session_low,
        "flush_pct": flush_pct,
        "bars_since_low": bars_since_low,
        "higher_low": higher_low,
        "base_high": base_high,
        "base_low": base_low,
        "base_range_pct": base_range_pct,
        "breakout_level": breakout_level,
        "session_high_clearance_required": True,
        "green_bars_last4": green_bars,
        "volume_expansion_ratio": volume_expansion,
        "recovery_from_low_pct": recovery_from_low_pct,
        "vwap": current_vwap,
        "entry_trigger": trigger,
        "raw_max_allowed_buy_price": raw_max_allowed,
        "max_allowed_buy_price": max_allowed,
        "initial_stop": stop,
        "first_target": first_target,
        "reward_risk_at_trigger": reward_risk_at_trigger,
        "reward_risk_at_max_fill": reward_risk_at_max_fill,
        "previous_close": previous_close,
        "extension_at_trigger_pct": extension_at_trigger_pct,
        "max_extension_pct": RECOVERY_MAX_EXTENSION_PCT,
        "resistance_price": resistance_price,
        "precalculated_profit_stop": profit_stop,
        "failures": failures,
    }


def _write_outputs(date_et, audit: list[dict], result: dict) -> dict:
    (OUT / "recovery_audit.json").write_text(json.dumps({
        "target_date_et": str(date_et),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "max_tradable_price": MAX_TRADABLE_PRICE,
        "candidates": [{k: serializable(v) for k, v in row.items()} for row in audit],
    }, indent=2), encoding="utf-8")
    result = {k: serializable(v) for k, v in result.items()}
    result["target_date_et"] = str(date_et)
    result["generated_at_utc"] = datetime.now(timezone.utc).isoformat()
    (OUT / "recovery_signal.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    (OUT / "recovery_alert.txt").write_text(str(result.get("message", "")) + "\n", encoding="utf-8")
    return result


def scan_once(date_override: str | None = None) -> dict:
    reference = now_et() if date_override is None else datetime.fromisoformat(date_override + "T10:30:00").replace(tzinfo=ET)
    date_et = reference.date()
    watch = _read_json(OUT / "recovery_watch.json")
    candidates = watch.get("candidates", [])
    if not candidates:
        return _write_outputs(date_et, [], {
            "status": "NO_RECOVERY_WATCH",
            "message": "RECOVERY WATCH — no eligible failed top candidates to monitor.",
        })

    # Do not create a competing recovery order if an official <=$100 primary trade
    # is already live/armed. Shadow-only >$100 primary names do not block recovery.
    final = _read_json(OUT / "final_signal.json")
    if final.get("status") in {"BUY", "ARM"}:
        live_price = final.get("live_price")
        if isinstance(live_price, (int, float)) and live_price <= MAX_TRADABLE_PRICE:
            return _write_outputs(date_et, [], {
                "status": "BLOCKED_BY_PRIMARY",
                "ticker": final.get("ticker"),
                "message": "RECOVERY WATCH STANDBY — an official primary Engine 4 trade/order is already active.",
            })

    symbols = [str(c.get("ticker")) for c in candidates if c.get("ticker")]
    frames = download_intraday(symbols, period="1d", interval="1m", prepost=False, date_et=date_et, lookback_days=0)
    audit = []
    ready = []
    for candidate in candidates:
        symbol = str(candidate.get("ticker"))
        previous_close = candidate.get("previous_close", math.nan)
        resistance_price = candidate.get("resistance_price", math.nan)
        try:
            previous_close = float(previous_close)
        except (TypeError, ValueError):
            previous_close = math.nan
        try:
            resistance_price = float(resistance_price)
        except (TypeError, ValueError):
            resistance_price = math.nan
        metrics = recovery_metrics(
            symbol,
            frames.get(symbol),
            date_et,
            previous_close=previous_close,
            resistance_price=resistance_price,
        )
        metrics["premarket_rank"] = candidate.get("rank")
        metrics["premarket_score"] = candidate.get("score")
        metrics["primary_failures"] = candidate.get("primary_failures", [])
        audit.append(metrics)
        if metrics.get("state") in {"ARM", "BUY"}:
            rank = candidate.get("rank")
            rank_value = float(rank) if isinstance(rank, (int, float)) else 999.0
            score = candidate.get("score")
            score_value = float(score) if isinstance(score, (int, float)) else 0.0
            ready.append((rank_value, -score_value, metrics))

    if ready:
        ready.sort(key=lambda x: (x[0], x[1]))
        metrics = ready[0][2]
        symbol = metrics["ticker"]
        if metrics["state"] == "BUY":
            message = (
                f"RECOVERY BUY {symbol} NOW\n"
                f"BUY BETWEEN ${metrics['entry_trigger']:.2f} AND ${metrics['max_allowed_buy_price']:.2f}\n"
                f"AFTER PURCHASE, ENTER GTC SELL STOP AT ${metrics['initial_stop']:.2f}\n"
                f"IF PRICE RISES TO ${metrics['first_target']:.2f}, MOVE SELL STOP TO ${metrics['precalculated_profit_stop']:.2f}\n"
                f"CURRENT PRICE: ${metrics['current_price']:.2f}\n"
                f"DO NOT BUY ABOVE ${metrics['max_allowed_buy_price']:.2f}"
            )
            return _write_outputs(date_et, audit, {
                "status": "BUY",
                "reason": "recovery_trigger_confirmed",
                "ticker": symbol,
                "message": message,
                "order_instruction": "BUY_NOW",
                **{k: metrics[k] for k in ("current_price", "entry_trigger", "max_allowed_buy_price", "initial_stop", "first_target", "precalculated_profit_stop")},
            })

        message = (
            f"PLACE RECOVERY BUY STOP-LIMIT NOW — {symbol}\n"
            f"STOP PRICE: ${metrics['entry_trigger']:.2f}\n"
            f"LIMIT PRICE: ${metrics['max_allowed_buy_price']:.2f}\n"
            f"TIME IN FORCE: DAY\n"
            f"CURRENT PRICE: ${metrics['current_price']:.2f}\n"
            f"IF FILLED, ENTER GTC SELL STOP AT ${metrics['initial_stop']:.2f}\n"
            f"IF PRICE THEN RISES TO ${metrics['first_target']:.2f}, MOVE SELL STOP TO ${metrics['precalculated_profit_stop']:.2f}\n"
            f"DO NOT CHASE ABOVE ${metrics['max_allowed_buy_price']:.2f}"
        )
        return _write_outputs(date_et, audit, {
            "status": "ARM",
            "reason": "recovery_base_confirmed_trigger_not_reached",
            "ticker": symbol,
            "message": message,
            "order_instruction": "ARM_STOP_LIMIT_DAY",
            **{k: metrics[k] for k in ("current_price", "entry_trigger", "max_allowed_buy_price", "initial_stop", "first_target", "precalculated_profit_stop")},
        })

    return _write_outputs(date_et, audit, {
        "status": "WATCH",
        "reason": "recovery_not_ready",
        "message": "RECOVERY WATCH ACTIVE — no second-chance base has fully confirmed yet.",
    })


def monitor(date_override: str | None = None, interval_seconds: int = RECOVERY_SCAN_INTERVAL_SECONDS) -> dict:
    base.install_repairs()
    base.assert_provider_health()

    if date_override is not None and str(date_override) != str(now_et().date()):
        # Historical overrides are one-shot by design so CI never sleeps.  A
        # same-day override locks production to its ET market date while keeping
        # the live recovery monitor active.
        return scan_once(date_override)

    last_result = {}
    while True:
        now = now_et()
        end = now.replace(hour=RECOVERY_END_HOUR_ET, minute=RECOVERY_END_MINUTE_ET, second=0, microsecond=0)
        if now > end:
            return _write_outputs(now.date(), _read_json(OUT / "recovery_audit.json").get("candidates", []), {
                "status": "TIMEOUT",
                "reason": "recovery_window_expired",
                "message": "RECOVERY WATCH CLOSED — no valid second-chance trigger before 11:30 ET.",
            })

        last_result = scan_once(date_override)
        if last_result.get("status") in {"ARM", "BUY", "BLOCKED_BY_PRIMARY", "NO_RECOVERY_WATCH"}:
            return last_result
        time.sleep(max(30, int(interval_seconds)))


def self_test() -> None:
    assert MAX_TRADABLE_PRICE == 100.0
    assert RECOVERY_MIN_FLUSH_PCT > 0
    assert RECOVERY_MIN_BARS_SINCE_LOW >= 5
    assert RECOVERY_SCAN_INTERVAL_SECONDS >= 60
    assert RECOVERY_MAX_EXTENSION_PCT > 0
    assert RECOVERY_TARGET_R >= MIN_REWARD_RISK
    print("ENGINE4_RECOVERY_SELF_TEST_PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    m = sub.add_parser("monitor")
    m.add_argument("--date")
    m.add_argument("--interval-seconds", type=int, default=RECOVERY_SCAN_INTERVAL_SECONDS)
    s = sub.add_parser("scan-once")
    s.add_argument("--date")
    sub.add_parser("self-test")
    args = parser.parse_args()

    base.install_repairs()
    if args.command == "monitor":
        monitor(args.date, args.interval_seconds)
    elif args.command == "scan-once":
        base.assert_provider_health()
        scan_once(args.date)
    else:
        self_test()


if __name__ == "__main__":
    main()
