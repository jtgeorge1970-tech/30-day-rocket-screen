"""Independent fail-closed validation of a completed V2 output directory."""
from __future__ import annotations

import json
import os
from pathlib import Path

import pandas as pd

import rocket_screen as engine


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def read(path):
    require(path.exists(), f"missing required artifact: {path}")
    return pd.read_csv(path)


def validate(out=Path("output")):
    audit_path = out / "audit_quality_loser.json"
    require(audit_path.exists(), "missing V2 audit JSON")
    audit = json.loads(audit_path.read_text())
    require(audit.get("engine") == "Quality Loser Reversal V2", "wrong engine identity")
    require(audit.get("starting_universe", 0) >= 5_000, "official run did not cover at least 5,000 securities")
    require(audit.get("price_request_failure_rate", 1) <= engine.MAX_PRICE_REQUEST_FAILURE_RATE, "price request failure rate exceeded cap")

    universe = read(out / "01_starting_universe.csv")
    scored = read(out / "04_all_quality_loser_scored.csv")
    pool = read(out / "05_quality_loser_pool.csv")
    bottoms = read(out / "06_bottom_confirmed.csv")
    geometry = read(out / "07_entry_geometry_pass.csv")
    research = read(out / "08_research_candidates.csv")
    ready = read(out / "09_ENTRY_READY.csv")
    positions = read(out / "10_active_positions_audit.csv")

    require(len(universe) == audit["starting_universe"], "universe count differs from audit")
    for label, frame in [("universe", universe), ("scored", scored), ("pool", pool), ("bottoms", bottoms), ("geometry", geometry), ("research", research)]:
        require(not frame.ticker.duplicated().any(), f"duplicate ticker in {label}")
    require(set(pool.ticker) <= set(scored.ticker), "loser pool is not a subset of scored universe")
    require(set(bottoms.ticker) <= set(pool.ticker), "bottom stage is not a subset of loser pool")
    require(set(geometry.ticker) <= set(bottoms.ticker), "geometry stage is not a subset of confirmed bottoms")
    require(set(research.ticker) <= set(geometry.ticker), "research stage is not a subset of geometry pass")
    require(set(ready.ticker) <= set(research.ticker), "entry-ready stage is not a subset of research")

    if len(pool):
        require(bool((pool.loser_event & pool.near_bottom & pool.automated_quality_pass).all()), "loser pool contains a hard-gate failure")
    if len(bottoms):
        require(bool(bottoms.bottom_confirmed.all()), "bottom stage contains an unconfirmed bottom")
    if len(geometry):
        require(bool((geometry.headroom_pass & geometry.stop_geometry_pass & geometry.stability_pass).all()), "entry geometry contains a failed gate")
        require(bool((geometry.headroom >= engine.MIN_HEADROOM).all()), "entry geometry violates headroom threshold")
        require(bool((geometry.support_distance <= engine.MAX_SUPPORT_DISTANCE).all()), "entry geometry violates support-distance threshold")
    if len(ready):
        require(bool(ready.current_verification_pass.all()), "entry-ready contains an unverified stock")

    private_path = Path(os.environ.get("ROCKET_ACTIVE_POSITIONS_FILE", "private/active_positions.csv"))
    source = private_path if private_path.exists() else Path("active_positions.template.csv")
    active_expected = set(pd.read_csv(source).ticker)
    require(active_expected <= set(positions.ticker), "an active holding is absent from the mandatory audit")
    require(len(research) <= 25, "research set exceeded locked maximum")
    require(len(ready) == audit["entry_ready"], "entry-ready count differs from audit")
    print("VALIDATION PASSED", json.dumps({
        "universe": len(universe), "scored": len(scored), "pool": len(pool),
        "bottoms": len(bottoms), "geometry": len(geometry), "research": len(research),
        "entry_ready": len(ready), "active_positions_audited": sorted(active_expected),
    }, indent=2))


if __name__ == "__main__":
    validate()
