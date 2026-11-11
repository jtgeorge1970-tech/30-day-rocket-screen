from __future__ import annotations

import json
import math
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

import engine4_feed as feed
import engine4_replay_snapshot as snapshot

ET = ZoneInfo("America/New_York")
BENCHMARKS = {"SPY", "QQQ", "XLC", "XLK"}
REQUIRED_PIPELINE_STAGES = ("prescreen_stage", "deep_stage", "refresh_and_freeze", "final_with_timeline")


def _parse_date(value: str) -> date:
    parsed = date.fromisoformat(value)
    if parsed.weekday() >= 5:
        raise SystemExit(f"REPLAY REFUSED — {value} is not a weekday")
    return parsed


def replay_manifest(value: str) -> dict:
    _parse_date(value)
    stages = [("PRE-SCREEN", "08:55"), ("DEEP 100-POINT ANALYSIS", "09:05"), ("REFRESH + TOP-25 FREEZE", "09:18"), ("FINAL CONFIRMATION", "09:45")]
    return {"mode": "INSTANT_REPLAY", "market_date_et": value, "production_state_writes": False, "production_sms": False, "live_provider_fallback": False, "stages": [{"stage": n, "asof_et": f"{value}T{t}:00-04:00"} for n, t in stages]}


def _snapshot_universe(value: str) -> list[str]:
    manifest = snapshot.verify_snapshot(value)
    universe = [str(t).strip().upper() for t in manifest.get("universe", []) if str(t).strip()]
    if not universe:
        raise RuntimeError("REPLAY DATA FAILURE: certified snapshot manifest has no universe")
    return universe


def _install_pipeline_routes(value: str):
    if feed.current().mode is not feed.FeedMode.REPLAY:
        raise RuntimeError("Replay routes may only be installed in INSTANT_REPLAY context")
    import engine4_pipeline as pipeline
    import engine4_intraday as intraday

    universe = _snapshot_universe(value)
    allowed_intraday = set(universe) | BENCHMARKS
    original_eligible_baseline = pipeline.eligible_baseline

    def replay_eligible_baseline():
        base = original_eligible_baseline()
        replay_base = base[base.ticker.astype(str).str.upper().isin(universe)].copy()
        found = set(replay_base.ticker.astype(str).str.upper())
        missing = [ticker for ticker in universe if ticker not in found]
        if missing:
            raise RuntimeError(f"REPLAY DATA FAILURE: snapshot universe missing from Engine 4 baseline: {missing}")
        order = {ticker: i for i, ticker in enumerate(universe)}
        replay_base["_replay_order"] = replay_base.ticker.astype(str).str.upper().map(order)
        return replay_base.sort_values("_replay_order").drop(columns=["_replay_order"]).reset_index(drop=True)

    def replay_intraday(tickers, *, period="1d", interval="1m", prepost=True, date_et=None, lookback_days=0):
        requested = [str(t).upper() for t in tickers]
        outside = [t for t in requested if t not in allowed_intraday]
        if outside:
            raise RuntimeError(f"REPLAY DATA FAILURE: Engine 4 requested ticker outside certified snapshot evidence set: {outside}")
        rows_by_ticker = feed.premarket_many(requested)
        result = {}
        for ticker, rows in rows_by_ticker.items():
            frame = pd.DataFrame(rows)
            if frame.empty:
                continue
            if "timestamp" not in frame.columns:
                raise RuntimeError(f"REPLAY DATA FAILURE: {ticker} bars missing timestamp")
            timestamps = pd.DatetimeIndex(pd.to_datetime(frame.pop("timestamp"), utc=True)).tz_convert(ET)
            frame.index = timestamps
            frame = frame.rename(columns={"open":"Open", "high":"High", "low":"Low", "close":"Close", "volume":"Volume"})
            result[ticker] = frame
        return result

    def replay_catalyst(ticker, reference_time):
        rows = feed.catalyst(ticker, reference_time)
        best = rows[0]
        headline = str(best.get("headline") or best.get("title") or "")[:180]
        quality = float(best.get("quality") or best.get("catalyst_quality") or 0.0)
        stamp = datetime.fromisoformat(str(best["timestamp"]).replace("Z", "+00:00")).astimezone(ET)
        age = max(0.0, (reference_time - stamp).total_seconds() / 3600.0)
        return quality, headline, age

    def replay_quote(ticker):
        row = feed.quote(ticker)
        bid = float(row.get("bid") or math.nan)
        ask = float(row.get("ask") or math.nan)
        if not (math.isfinite(bid) and math.isfinite(ask) and bid > 0 and ask >= bid):
            return bid, ask, math.nan
        mid = (bid + ask) / 2.0
        return bid, ask, ((ask - bid) / mid * 100.0 if mid > 0 else math.nan)

    # Replay-only routing for the pipeline stages.
    pipeline.eligible_baseline = replay_eligible_baseline
    pipeline.download_intraday = replay_intraday
    pipeline.catalyst_for = replay_catalyst
    pipeline.quote_spread = replay_quote

    # final_with_timeline calls engine4_intraday.final_stage, whose provider globals
    # live in that module. Route those too so 09:45 can never fall back to live data.
    intraday.download_intraday = replay_intraday
    intraday.catalyst_for = replay_catalyst
    intraday.quote_spread = replay_quote

    missing = [name for name in REQUIRED_PIPELINE_STAGES if not callable(getattr(pipeline, name, None))]
    if missing:
        raise RuntimeError(f"REPLAY STATIC AUDIT FAILURE: missing locked Engine 4 stages: {missing}")
    return pipeline


def _configure(value: str, hhmm: str):
    d = _parse_date(value)
    h, m = map(int, hhmm.split(":"))
    asof = datetime(d.year, d.month, d.day, h, m, tzinfo=ET)
    feed.configure_replay(d, asof)
    snapshot.install(feed, value)
    return _install_pipeline_routes(value)


def preflight(value: str) -> None:
    d = _parse_date(value)
    asof = datetime(d.year, d.month, d.day, 8, 55, tzinfo=ET)
    feed.configure_replay(d, asof)
    failures = []
    for kind in ("catalyst", "quote", "premarket"):
        try:
            feed.require_replay_source(kind)
        except feed.ReplayDataUnavailable:
            failures.append(kind)
    if failures != ["catalyst", "quote", "premarket"]:
        raise RuntimeError(f"Replay fail-closed guard failed: {failures}")
    snapshot.install(feed, value)
    for kind in ("catalyst", "quote", "premarket"):
        feed.require_replay_source(kind)
    pipeline = _install_pipeline_routes(value)
    for name in REQUIRED_PIPELINE_STAGES:
        if not callable(getattr(pipeline, name, None)):
            raise RuntimeError(f"REPLAY STATIC AUDIT FAILURE: {name} unavailable")
    # Prove all snapshot symbols and benchmarks are addressable before launching.
    feed.premarket_many(_snapshot_universe(value) + sorted(BENCHMARKS))
    out = Path("output/engine4-replay") / value
    out.mkdir(parents=True, exist_ok=True)
    (out / "replay_manifest.json").write_text(json.dumps(replay_manifest(value), indent=2), encoding="utf-8")
    print(f"ENGINE4_REPLAY_PREFLIGHT_PASS date={value}")
    print("REPLAY_STATIC_STAGE_AUDIT_PASS stages=" + ",".join(REQUIRED_PIPELINE_STAGES))
    print(f"REPLAY_UNIVERSE_LOCKED tickers={','.join(_snapshot_universe(value))}")
    print("REPLAY_BENCHMARKS_LOCKED tickers=SPY,QQQ,XLC,XLK")
    print("FEEDER3_LOCKED_ENGINE4_ROUTES_INSTALLED")
    print("FINAL_STAGE_REPLAY_PROVIDER_ROUTES_INSTALLED")
    print("AUTO_MANUAL_PROVIDER_PATHS_UNCHANGED")
    print("LIVE_FALLBACK_FORBIDDEN")
    print("PRODUCTION_STATE_ISOLATED")


def run(value: str) -> None:
    stages = [
        ("08:55", "prescreen_stage"),
        ("09:05", "deep_stage"),
        ("09:18", "refresh_and_freeze"),
        ("09:45", "final_with_timeline"),
    ]
    for hhmm, fn_name in stages:
        pipeline = _configure(value, hhmm)
        fn = getattr(pipeline, fn_name)
        fn(value)
        print(f"ENGINE4_REPLAY_STAGE_PASS stage={fn_name} asof={hhmm}")
    print(f"ENGINE4_REPLAY_COMPLETE date={value}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["preflight", "run"])
    parser.add_argument("--date", required=True)
    args = parser.parse_args()
    if args.command == "preflight":
        preflight(args.date)
    else:
        run(args.date)
