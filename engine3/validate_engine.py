"""Fail-closed validator for Engine #3 live-screen artifacts."""
import json
from pathlib import Path

import pandas as pd

import extreme_winner_engine as engine


def require(condition, message):
    if not bool(condition):
        raise AssertionError(message)


def validate(out=Path("output")):
    audit_path = out / "audit_extreme_winner.json"
    require(audit_path.exists(), "missing Engine #3 audit")
    audit = json.loads(audit_path.read_text())
    universe = pd.read_csv(out / "01_starting_universe.csv")
    metrics = pd.read_csv(out / "02_price_metrics.csv")
    failures = pd.read_csv(out / "02_price_failures.csv")
    events = pd.read_csv(out / "03_extreme_winner_events.csv")
    investable = pd.read_csv(out / "04_investable_events.csv")
    scored = pd.read_csv(out / "05_all_scored_events.csv")
    top50 = pd.read_csv(out / "06_top50.csv")
    top25 = pd.read_csv(out / "07_top25.csv")
    top10 = pd.read_csv(out / "08_top10.csv")
    top5 = pd.read_csv(out / "08_top5.csv")
    top3 = pd.read_csv(out / "09_top3_REQUIRES_CURRENT_VERIFICATION.csv")
    entries = pd.read_csv(out / "11_ENTRY_READY.csv")

    require(len(universe) >= 5_000, "Engine #3 did not process the full 5,000+ listed universe")
    require(len(universe) == audit["starting_universe"], "starting universe audit mismatch")
    require(not universe.ticker.duplicated().any(), "duplicate universe ticker")
    require(not universe.name.str.contains(r"Warrant|Right| Unit|Units|Preferred|Acquisition Corp|SPAC", case=False, na=False, regex=True).any(), "non-common structure survived universe filter")
    require(len(failures) == audit["price_failures"], "price failure audit mismatch")
    require(audit["price_failure_rate"] <= engine.MAX_PRICE_REQUEST_FAILURE_RATE, "price failure cap exceeded")
    require(len(metrics) == audit["price_metrics"], "price metric audit mismatch")
    require(not events.duplicated("ticker").any(), "live event file must contain latest event per ticker only")
    if len(events):
        detected = (events.event_day_return >= engine.ONE_DAY_EVENT) | (events.event_five_day_return >= engine.FIVE_DAY_EVENT)
        require(detected.all(), "non-qualifying event entered the event pool")
        require((events.event_age_sessions < engine.LOOKBACK_EVENT_SESSIONS).all(), "event outside 30-session window")
    if len(investable):
        require((investable.price >= engine.MIN_PRICE).all(), "sub-$3 event survived")
        require((investable.event_dollar_volume_20 >= engine.MIN_DOLLAR_VOLUME).all(), "illiquid event survived")
        require((investable.market_cap >= engine.MIN_MARKET_CAP).all(), "sub-$200M event survived")
        require(set(investable.ticker) <= set(events.ticker), "investable event not in event pool")
    if len(top50):
        require(top50.automated_gate_pass.astype(bool).all(), "failed automated gate entered Top 50")
        require((top50.event_close_location >= engine.MIN_CLOSE_LOCATION).all(), "weak close entered Top 50")
        require((top50.event_volume_ratio_20 >= engine.MIN_VOLUME_RATIO).all(), "low-volume event entered Top 50")
        require((top50.current_extension_ma20 <= engine.MAX_EXTENSION_MA20).all(), "overextended event entered Top 50")
        require((top50.event_atr14_pct <= engine.MAX_ATR14_PCT).all(), "stop geometry volatility gate broken")
    require(len(top50) <= 50 and len(top25) <= 25 and len(top10) <= 10 and len(top5) <= 5 and len(top3) <= 3, "funnel stage size exceeded")
    require(set(top25.ticker) <= set(top50.ticker), "Top 25 is not subset of Top 50")
    require(set(top10.ticker) <= set(top25.ticker), "Top 10 is not subset of Top 25")
    require(set(top5.ticker) <= set(top10.ticker), "Top 5 is not subset of Top 10")
    require(set(top3.ticker) <= set(top5.ticker), "Top 3 is not subset of Top 5")
    require(set(entries.ticker) <= set(top3.ticker), "entry-ready stock is outside Top 3")
    if len(entries):
        require((entries.final_status.str.upper() == "APPROVED").all(), "entry-ready row lacks approval")
        for gate in engine.VERIFICATION_GATES:
            require((entries[gate].str.upper() == "PASS").all(), f"entry-ready row failed {gate}")
    require(audit["entry_ready"] == len(entries), "entry-ready audit mismatch")
    require(audit["FINAL_LABEL_ALLOWED"] == bool(len(entries)), "FINAL label invariant broken")
    require(audit["orders_placed_automatically"] is False, "engine may not place orders")
    print(
        "EXTREME-WINNER ENGINE VALIDATION PASSED",
        json.dumps({"universe": len(universe), "events": len(events), "automated_pass": len(top50), "top3": len(top3), "entry_ready": len(entries)}, indent=2),
    )


if __name__ == "__main__":
    validate()
