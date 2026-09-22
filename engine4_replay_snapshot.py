from __future__ import annotations

"""Historical snapshot providers for Engine 4 Instant Replay.

Strategy-free adapter. Reads only certified replay files under
replay_snapshots/YYYY-MM-DD and never falls back to live providers.
"""

import csv
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")


class SnapshotError(RuntimeError):
    pass


def _root(day: str) -> Path:
    return Path("replay_snapshots") / day


def _read_csv(path: Path) -> list[dict]:
    if not path.exists():
        raise SnapshotError(f"missing certified replay file: {path}")
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _as_dt(value: str) -> datetime:
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return dt.astimezone(ET)


def verify_snapshot(day: str) -> dict:
    root = _root(day)
    manifest_path = root / "manifest.json"
    if not manifest_path.exists():
        raise SnapshotError(f"missing certified replay manifest: {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("market_date_et") != day:
        raise SnapshotError("manifest market date mismatch")
    for name in ("bars.csv", "quotes.csv", "catalysts.csv"):
        if not (root / name).exists():
            raise SnapshotError(f"missing certified replay file: {root / name}")
    return manifest


def install(feed, day: str) -> None:
    verify_snapshot(day)
    root = _root(day)
    bars = _read_csv(root / "bars.csv")
    quotes = _read_csv(root / "quotes.csv")
    catalysts = _read_csv(root / "catalysts.csv")

    def quote(ticker: str, asof):
        rows = [r for r in quotes if r.get("ticker") == ticker and _as_dt(r["timestamp"]) <= asof]
        if not rows:
            raise SnapshotError(f"no point-in-time quote for {ticker} at {asof.isoformat()}")
        return max(rows, key=lambda r: _as_dt(r["timestamp"]))

    def premarket(tickers, asof):
        result = {}
        for ticker in tickers:
            rows = [r for r in bars if r.get("ticker") == ticker and _as_dt(r["timestamp"]) <= asof]
            if not rows:
                raise SnapshotError(f"no point-in-time premarket bars for {ticker} at {asof.isoformat()}")
            result[ticker] = rows
        return result

    def catalyst(ticker: str, reference_time, company_name=None):
        rows = [r for r in catalysts if r.get("ticker") == ticker and _as_dt(r["timestamp"]) <= reference_time]
        if not rows:
            raise SnapshotError(f"no point-in-time catalyst for {ticker} at {reference_time.isoformat()}")
        return sorted(rows, key=lambda r: _as_dt(r["timestamp"]), reverse=True)

    feed.install_replay_sources(catalyst=catalyst, quote=quote, premarket=premarket)
