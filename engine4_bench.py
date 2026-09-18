from __future__ import annotations

"""Persistent, date-locked Engine 4 Top-25 candidate Bench.

The Bench is a capacity-limited development queue, never a trade approval.  It
combines yesterday's Bench with today's launchpad, refreshes every candidate
with current evidence, and retains only the strongest 25 for at most five
completed market sessions.  Only the Hot 5 are exposed to the existing 09:45
live-entry guard, which still revalidates every mandatory gate.
"""

import argparse
import json
import math
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

import engine4_pipeline as core
import engine4_pipeline_runner as runner
from engine4_config import MAX_TRADABLE_PRICE, MIN_SCORE
from engine4_data import download_intraday, prior_regular_close, slice_window
from engine4_score import preliminary_activity_score


OUT = Path("output/engine4")
STATE = Path("state/engine4/watch_bench.json")
BENCH_CAP = 25
HOT_CAP = 5
DEVELOPING_CAP = 10
RESERVE_CAP = 10
MAX_WATCH_SESSIONS = 5
GENERAL_ADMISSION_SCORE = 85.0
TOP3_ADMISSION_SCORE = MIN_SCORE


def _read(path: Path) -> dict:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        return payload if isinstance(payload, dict) else {}
    except Exception:
        return {}


def _finite(value, default=math.nan) -> float:
    try:
        result = float(value)
        return result if math.isfinite(result) else default
    except (TypeError, ValueError):
        return default


def _serializable(value):
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        value = float(value)
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if isinstance(value, (np.bool_, bool)):
        return bool(value)
    return value


def _records(frame: pd.DataFrame) -> list[dict]:
    return [
        {key: _serializable(value) for key, value in row.items()}
        for row in frame.to_dict("records")
    ]


def _fresh_seed_rows(symbols: list[str], date_et, cutoff: str) -> tuple[pd.DataFrame, list[str]]:
    baseline = core.eligible_baseline().set_index("ticker")
    symbols = [symbol for symbol in symbols if symbol in baseline.index]
    frames = download_intraday(
        symbols,
        period="1d",
        interval="1m",
        prepost=True,
        date_et=date_et,
        lookback_days=1,
    )
    snapshots = runner.nasdaq_premarket_many(symbols, max_workers=12)
    rows: list[dict] = []
    missing: list[str] = []

    for symbol in symbols:
        frame = frames.get(symbol)
        snap = snapshots.get(symbol, {})
        yahoo_price = math.nan
        if frame is not None and not frame.empty:
            pm = slice_window(frame, date_et, "04:00", cutoff)
            if not pm.empty and "Close" in pm.columns:
                close = pd.to_numeric(pm["Close"], errors="coerce").dropna()
                if not close.empty:
                    yahoo_price = float(close.iloc[-1])
        nasdaq_price = _finite(snap.get("premarket_price"))
        current = nasdaq_price if math.isfinite(nasdaq_price) else yahoo_price
        if not math.isfinite(current) or current <= 0:
            missing.append(symbol)
            continue

        previous = prior_regular_close(frame, date_et) if frame is not None else math.nan
        if not math.isfinite(previous) or previous <= 0:
            previous = _finite(baseline.at[symbol, "price"])
        if not math.isfinite(previous) or previous <= 0:
            missing.append(symbol)
            continue

        volume = _finite(snap.get("premarket_volume"), 0.0)
        daily_dollar = _finite(baseline.at[symbol, "dollar_volume"], 0.0)
        adv_shares = daily_dollar / current if current > 0 else math.nan
        intensity = volume / adv_shares * 100.0 if adv_shares > 0 else math.nan
        gap = (current / previous - 1.0) * 100.0
        pm_dollar = volume * current
        strict = bool(0.50 <= gap <= 25.0 and pm_dollar >= 500_000)
        rows.append(
            {
                "ticker": symbol,
                "name": str(baseline.at[symbol, "name"]),
                "sector": str(baseline.at[symbol, "sector"]),
                "market_cap": _finite(baseline.at[symbol, "market_cap"]),
                "avg_daily_dollar_volume": daily_dollar,
                "previous_close": previous,
                "last_premarket": current,
                "premarket_volume": volume,
                "premarket_dollar_volume": pm_dollar,
                "premarket_volume_intensity_pct": intensity,
                "gap_pct": gap,
                "broad_qualifier": True,
                "strict_activity_pass": strict,
                "nasdaq_premarket_ok": bool(math.isfinite(nasdaq_price)),
                "activity_score": preliminary_activity_score(
                    gap, max(pm_dollar, 1.0), max(daily_dollar, 1.0)
                ),
            }
        )
    return pd.DataFrame(rows), missing


def _tier(rank: int) -> str:
    if rank <= HOT_CAP:
        return "HOT"
    if rank <= HOT_CAP + DEVELOPING_CAP:
        return "DEVELOPING"
    return "RESERVE"


def update_bench(date_override: str | None = None, state_path: Path = STATE) -> dict:
    runner.install_repairs()
    reference = core._reference(date_override, "09:18")
    date_et = reference.date()
    expected = str(date_et)

    frozen = _read(OUT / "top25_frozen.json")
    if str(frozen.get("target_date_et") or "") != expected:
        raise RuntimeError(
            "ENGINE 4 BENCH FAILURE — current dated top25_frozen.json is required"
        )
    today = frozen.get("candidates", [])
    previous = _read(state_path)
    previous_rows = previous.get("candidates", [])
    previous_by_ticker = {
        str(row.get("ticker")): row for row in previous_rows if row.get("ticker")
    }
    today_rank = {
        str(row.get("ticker")): int(row.get("rank") or index)
        for index, row in enumerate(today, start=1)
        if row.get("ticker")
    }
    symbols = list(dict.fromkeys([*previous_by_ticker, *today_rank]))

    core.log_event(
        "TOP-25 MULTI-DAY BENCH",
        "STARTED",
        f"Daily Bench competition started for {len(symbols)} unique prior/new candidates.",
        tickers=symbols,
        details={"bench_competition_universe": len(symbols), "bench_cap": BENCH_CAP},
    )

    seed, missing = _fresh_seed_rows(symbols, date_et, "09:18")
    ranked = runner.repaired_score_pool(seed, date_et, reference, "09:18")
    if ranked.empty and symbols:
        raise RuntimeError("ENGINE 4 BENCH FAILURE — no Bench candidates could be refreshed")

    refreshed = {str(row["ticker"]): row for row in _records(ranked)}
    qualified: list[dict] = []
    removed: list[dict] = []
    for symbol in symbols:
        row = refreshed.get(symbol)
        prior = previous_by_ticker.get(symbol)
        if row is None:
            removed.append({"ticker": symbol, "reason": "missing_current_trustworthy_data"})
            continue

        score = _finite(row.get("score"), 0.0)
        eligible = bool(row.get("premarket_eligible"))
        is_top3 = today_rank.get(symbol, 999) <= 3
        was_benched = prior is not None
        admission = None
        if eligible and score >= GENERAL_ADMISSION_SCORE:
            admission = "current_score_85_plus"
        elif eligible and is_top3 and score >= TOP3_ADMISSION_SCORE:
            admission = "current_launchpad_top3"
        elif eligible and was_benched and score >= MIN_SCORE:
            admission = "retained_current_b_grade"
        if admission is None:
            reason = "below_current_B_grade" if score < MIN_SCORE else "current_mandatory_gate_failure"
            removed.append({"ticker": symbol, "reason": reason, "current_score": score})
            continue

        last_date = str((prior or {}).get("last_refreshed_date") or "")
        age = int((prior or {}).get("age_sessions") or 0)
        if last_date != expected:
            age += 1
        if age > MAX_WATCH_SESSIONS:
            removed.append({"ticker": symbol, "reason": "five_session_watch_expired", "age_sessions": age})
            continue

        gate_count = _finite(row.get("premarket_gate_count"), 0.0)
        activity = _finite(row.get("activity_score"), 0.0)
        priority = score + (5.0 if is_top3 else 0.0) + min(gate_count, 7.0) * 0.10 + min(activity, 10.0) * 0.01
        row.update(
            {
                "age_sessions": age,
                "first_added_date": str((prior or {}).get("first_added_date") or expected),
                "last_refreshed_date": expected,
                "today_launchpad_rank": today_rank.get(symbol),
                "admission_reason": admission,
                "watch_priority": round(priority, 6),
                "max_tradable_price": MAX_TRADABLE_PRICE,
                "official_trade_eligible_by_price": _finite(row.get("last_premarket"), math.inf) <= MAX_TRADABLE_PRICE,
            }
        )
        qualified.append(row)

    qualified.sort(
        key=lambda row: (
            _finite(row.get("watch_priority"), 0.0),
            _finite(row.get("score"), 0.0),
        ),
        reverse=True,
    )
    natural_qualified = len(qualified)
    selected = qualified[:BENCH_CAP]
    displaced = qualified[BENCH_CAP:]
    removed.extend(
        {"ticker": row.get("ticker"), "reason": "displaced_by_Top25_Bench_cap"}
        for row in displaced
    )

    prior_tiers = {ticker: row.get("tier") for ticker, row in previous_by_ticker.items()}
    additions: list[str] = []
    promotions: list[str] = []
    demotions: list[str] = []
    for rank, row in enumerate(selected, start=1):
        tier = _tier(rank)
        old_tier = prior_tiers.get(str(row.get("ticker")))
        row["bench_rank"] = rank
        row["tier"] = tier
        row["watch_status"] = f"{tier}_WATCH"
        if old_tier is None:
            additions.append(str(row.get("ticker")))
        elif (old_tier, tier) in {("RESERVE", "DEVELOPING"), ("RESERVE", "HOT"), ("DEVELOPING", "HOT")}:
            promotions.append(str(row.get("ticker")))
        elif old_tier != tier:
            demotions.append(str(row.get("ticker")))

    payload = {
        "target_date_et": expected,
        "generated_at_et": datetime.now(core.ET).isoformat(),
        "bench_cap": BENCH_CAP,
        "bench_cap_is_quota": False,
        "max_watch_sessions": MAX_WATCH_SESSIONS,
        "general_admission_score": GENERAL_ADMISSION_SCORE,
        "top3_admission_score": TOP3_ADMISSION_SCORE,
        "competition_universe_count": len(symbols),
        "freshly_scored_count": len(refreshed),
        "naturally_watch_qualified_count": natural_qualified,
        "retained_by_top25_bench_cap": len(selected),
        "hot_count": sum(row.get("tier") == "HOT" for row in selected),
        "developing_count": sum(row.get("tier") == "DEVELOPING" for row in selected),
        "reserve_count": sum(row.get("tier") == "RESERVE" for row in selected),
        "missing_current_data": missing,
        "additions": additions,
        "promotions": promotions,
        "demotions": demotions,
        "removals": removed,
        "candidates": selected,
    }
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "watch_bench_report.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    pd.DataFrame(selected).to_csv(OUT / "watch_bench.csv", index=False)

    summary = (
        f"BENCH: {natural_qualified} naturally watch-qualified; {len(selected)} retained by configured "
        f"Top-{BENCH_CAP} Bench cap; Hot {payload['hot_count']}, Developing "
        f"{payload['developing_count']}, Reserve {payload['reserve_count']}."
    )
    (OUT / "watch_bench_summary.txt").write_text(summary + "\n", encoding="utf-8")
    core.log_event(
        "TOP-25 MULTI-DAY BENCH",
        "COMPLETED",
        summary,
        tickers=[str(row.get("ticker")) for row in selected],
        details={
            "naturally_watch_qualified_count": natural_qualified,
            "retained_by_top25_bench_cap": len(selected),
            "hot_count": payload["hot_count"],
            "developing_count": payload["developing_count"],
            "reserve_count": payload["reserve_count"],
        },
    )
    print(summary, flush=True)
    return payload


def self_test() -> None:
    assert BENCH_CAP == HOT_CAP + DEVELOPING_CAP + RESERVE_CAP
    assert BENCH_CAP == 25
    assert MAX_WATCH_SESSIONS == 5
    assert GENERAL_ADMISSION_SCORE == 85.0
    assert TOP3_ADMISSION_SCORE == MIN_SCORE == 80.0
    print("ENGINE4_BENCH_SELF_TEST_PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    update = sub.add_parser("update")
    update.add_argument("--date")
    update.add_argument("--state-path", type=Path, default=STATE)
    sub.add_parser("self-test")
    args = parser.parse_args()
    if args.command == "update":
        update_bench(args.date, args.state_path)
    else:
        self_test()


if __name__ == "__main__":
    main()
