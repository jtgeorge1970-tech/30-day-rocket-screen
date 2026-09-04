"""Fail-closed validation for the 30-session loser cohort study."""
import json
from pathlib import Path

import pandas as pd

import loser_cohort_study as study


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def validate(out=Path("cohort_output")):
    audit_path = out / "audit_loser_cohort.json"
    require(audit_path.exists(), "missing cohort audit")
    audit = json.loads(audit_path.read_text())
    universe = pd.read_csv(out / "01_current_universe.csv")
    events = pd.read_csv(out / "02_loser_event_ledger.csv")
    resolved = pd.read_csv(out / "03_resolved_outcomes.csv")
    open_events = pd.read_csv(out / "04_open_cohorts.csv")
    strict = pd.read_csv(out / "07_CURRENT_RESEARCH_CANDIDATES_NOT_BUY.csv")
    require(len(universe) >= 5_000, "study did not process a 5,000+ universe")
    require(len(universe) == audit["current_universe_count"], "universe audit mismatch")
    require(not events.duplicated(["ticker", "event_date"]).any(), "duplicate event key")
    require(set(resolved.primary_outcome) <= {"WIN_10_BEFORE_10", "LOSS_10_BEFORE_10", "AMBIGUOUS_SAME_BAR", "NEITHER_WITHIN_30"}, "invalid resolved label")
    require(set(open_events.primary_outcome) <= {"OPEN"}, "open file contains resolved label")
    require(len(events) == len(resolved) + len(open_events), "event partition mismatch")
    require((events.available_forward_sessions <= 30).all(), "outcome exceeded 30-session horizon")
    require(audit["entry_ready_created_by_study"] == 0, "study improperly created entry-ready status")
    if len(strict):
        require(set(strict.status) == {"RESEARCH_ONLY_NOT_BUY"}, "strict candidate received prohibited status")
        require(set(strict.ticker) <= set(open_events.ticker), "strict candidate is not an open cohort member")
    require(audit["price_failure_rate"] <= study.MAX_EVENT_FAILURE_RATE, "price failure cap exceeded")
    print("COHORT VALIDATION PASSED", json.dumps({"events": len(events), "resolved": len(resolved), "open": len(open_events), "strict_research": len(strict)}, indent=2))


if __name__ == "__main__":
    validate()
