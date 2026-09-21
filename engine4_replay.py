from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import engine4_feed as feed

ET = ZoneInfo("America/New_York")


def _parse_date(value: str) -> date:
    parsed = date.fromisoformat(value)
    if parsed.weekday() >= 5:
        raise SystemExit(f"REPLAY REFUSED — {value} is not a weekday")
    return parsed


def replay_manifest(value: str) -> dict:
    d = _parse_date(value)
    stages = [
        ("PRE-SCREEN", "08:55"),
        ("DEEP 100-POINT ANALYSIS", "09:05"),
        ("REFRESH + TOP-25 FREEZE", "09:18"),
        ("FINAL CONFIRMATION", "09:45"),
    ]
    return {
        "mode": "INSTANT_REPLAY",
        "market_date_et": value,
        "production_state_writes": False,
        "production_sms": False,
        "live_provider_fallback": False,
        "stages": [
            {"stage": name, "asof_et": f"{value}T{hhmm}:00-04:00"}
            for name, hhmm in stages
        ],
    }


def preflight(value: str) -> None:
    d = _parse_date(value)
    asof = datetime(d.year, d.month, d.day, 8, 55, tzinfo=ET)
    feed.configure_replay(d, asof)

    # This is the critical isolation proof. Until a real point-in-time source is
    # installed, replay MUST fail rather than touch a live provider.
    failures = []
    for kind in ("catalyst", "quote", "premarket"):
        try:
            feed.require_replay_source(kind)
        except feed.ReplayDataUnavailable:
            failures.append(kind)
    if failures != ["catalyst", "quote", "premarket"]:
        raise RuntimeError(f"Replay fail-closed guard failed: {failures}")

    out = Path("output/engine4-replay") / value
    out.mkdir(parents=True, exist_ok=True)
    (out / "replay_manifest.json").write_text(
        json.dumps(replay_manifest(value), indent=2), encoding="utf-8"
    )
    print(f"ENGINE4_REPLAY_PREFLIGHT_PASS date={value}")
    print("LIVE_FALLBACK_FORBIDDEN")
    print("PRODUCTION_STATE_ISOLATED")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["preflight"])
    parser.add_argument("--date", required=True)
    args = parser.parse_args()
    preflight(args.date)
