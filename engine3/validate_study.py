"""Fail-closed validator for the 30-session winner-continuation cohort."""
import json
from pathlib import Path

import pandas as pd

import extreme_winner_engine as engine
import winner_continuation_study as study


def require(condition, message):
    if not bool(condition):
        raise AssertionError(message)


def validate(out=Path("study_output")):
    audit_path = out / "audit_winner_cohort.json"
    require(audit_path.exists(), "missing winner-cohort audit")
    audit = json.loads(audit_path.read_text())
    universe = pd.read_csv(out / "01_current_universe.csv")
    events = pd.read_csv(out / "02_winner_event_ledger.csv")
    failures = pd.read_csv(out / "02_price_failures.csv")
    resolved = pd.read_csv(out / "03_resolved_outcomes.csv")
    open_events = pd.read_csv(out / "04_open_cohorts.csv")
    exit_summary = pd.read_csv(out / "06_exit_policy_summary_EXPLORATORY.csv")
    current = pd.read_csv(out / "08_CURRENT_OPEN_EVENTS_NOT_BUY.csv")

    require(len(universe) >= 5_000, "winner study did not process a 5,000+ universe")
    require(len(universe) == audit["current_universe_count"], "universe audit mismatch")
    require(len(failures) == audit["price_failures"], "failure audit mismatch")
    require(audit["price_failure_rate"] <= engine.MAX_PRICE_REQUEST_FAILURE_RATE, "price failure cap exceeded")
    require(not events.duplicated(["ticker", "event_date"]).any(), "duplicate event key")
    if len(events):
        qualifying = (events.day_return >= engine.ONE_DAY_EVENT) | (events.five_day_return >= engine.FIVE_DAY_EVENT)
        require(qualifying.all(), "ledger contains non-qualifying winner event")
        require((events.event_close >= engine.MIN_PRICE).all(), "ledger contains sub-$3 event")
        require((events.event_dollar_volume_20 >= engine.MIN_DOLLAR_VOLUME).all(), "ledger contains illiquid event")
        require((events.available_forward_sessions <= 30).all(), "outcome exceeded 30 sessions")
    allowed = {"WIN_10_BEFORE_10", "LOSS_10_BEFORE_10", "AMBIGUOUS_SAME_BAR", "NEITHER_WITHIN_30"}
    require(set(resolved.primary_outcome) <= allowed, "invalid resolved label")
    require(set(open_events.primary_outcome) <= {"OPEN"}, "open file contains resolved event")
    require(len(events) == len(resolved) + len(open_events), "event partition mismatch")
    require(set(current.ticker) <= set(open_events.ticker), "current research file contains resolved event")
    require(set(exit_summary.policy) == {"day_30_close", "trail_7_after_10", "trail_10_after_10"}, "exit policies missing")
    require(audit["entry_ready_created_by_study"] == 0, "study improperly created an entry-ready stock")
    require(audit["lookback_event_sessions"] == study.LOOKBACK_SESSIONS == 30, "study is not the locked 30-session cohort")
    print(
        "WINNER-COHORT VALIDATION PASSED",
        json.dumps({"universe": len(universe), "events": len(events), "resolved": len(resolved), "open": len(open_events)}, indent=2),
    )


if __name__ == "__main__":
    validate()
