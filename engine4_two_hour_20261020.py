"""Isolated October 20 closing-session audit. No live order authorization."""
from __future__ import annotations

import argparse
import json
import math
import shutil
from datetime import datetime, time, date
from pathlib import Path

import pandas as pd
import engine4_last_hour_runner as lh
import engine4_pipeline as core
from engine4_data import slice_window as original_slice_window

TARGET = "2026-10-20"
OUT = Path("output/engine4_two_hour_20261020")
START = "14:00"
END = "16:00"

def _slice(frame, date_et, start_hhmm, end_hhmm, inclusive="both"):
    # 14:00 through 15:59:59 ET: do not include the 16:00 after-hours bar.
    return original_slice_window(frame, date_et, start_hhmm, end_hhmm,
                                 inclusive="left" if end_hhmm == END else inclusive)

def configure():
    lh.OUT = OUT
    lh.WINDOW_START = START
    lh.WINDOW_END = END
    lh.slice_window = _slice
    lh.ref = lambda d: datetime.combine(d, time(16, 0), tzinfo=core.ET)

def write(name, data):
    (OUT / name).write_text(json.dumps(data, indent=2, allow_nan=False, default=str))

def read(name):
    return json.loads((OUT / name).read_text())

def validate_timestamps():
    report = read("stage1_report.json")
    rows = pd.read_csv(OUT / "stage1_retained.csv")
    if len(rows) != report["retained_by_top100_cap"]:
        raise RuntimeError("Retained count mismatch")
    if list(rows.ticker.astype(str)) != report["symbols"]:
        raise RuntimeError("Retained ticker list mismatch")
    if not len(rows):
        raise RuntimeError("No valid intraday bars; this is DATA FAILURE, not NO TRADE")
    times = pd.to_datetime(rows.selection_bar_timestamp, utc=True).dt.tz_convert("America/New_York")
    if not all((times.dt.date == date.fromisoformat(TARGET)) &
               (times.dt.hour >= 14) & (times.dt.hour < 16)):
        raise RuntimeError("Stale or out-of-window retained bar timestamp")
    report["window"] = "14:00-16:00 ET, 16:00 bar excluded"
    report["source"] = "Yahoo Finance 1-minute historical OHLCV via engine4_data.download_intraday"
    report["retained_last_bar_min_et"] = str(times.min())
    report["retained_last_bar_max_et"] = str(times.max())
    report["analysis_type"] = "historical_closing_session_not_live_trade"
    write("stage1_report.json", report)
    rows["snapshot_mode"] = "HISTORICAL_1400_1600_ET"
    rows.to_csv(OUT / "stage1_retained.csv", index=False)
    print("VERIFIED STAGE1", json.dumps(report), flush=True)

def stage2_audit():
    report = read("stage2_report.json")
    ranked = pd.read_csv(OUT / "stage2_ranked.csv")
    if report["actually_analyzed"] != len(ranked):
        raise RuntimeError("Stage2 analyzed count mismatch")
    count = int((ranked.score >= 80).sum()) if len(ranked) else 0
    if count != report["score_ge_80"]:
        raise RuntimeError("Stage2 score >=80 count mismatch")
    if not len(ranked):
        raise RuntimeError("No analyzable Stage2 names: DATA FAILURE, not NO TRADE")
    columns = ["ticker", "score", "premarket_grade", "premarket_eligible",
               "premarket_failures", "selection_bar_timestamp",
               "last_hour_close", "last_hour_return_pct", "spread_source",
               "spread_order_authoritative"]
    for c in columns:
        if c not in ranked:
            raise RuntimeError("Missing mandatory Stage2 field: " + c)
    ts = pd.to_datetime(ranked.selection_bar_timestamp, utc=True).dt.tz_convert("America/New_York")
    if not all((ts.dt.date == date.fromisoformat(TARGET)) &
               (ts.dt.hour >= 14) & (ts.dt.hour < 16)):
        raise RuntimeError("Stage2 source timestamps invalid")
    entries = json.loads(ranked[columns].to_json(orient="records"))
    proof = {
        "target_date_et": TARGET,
        "window": "14:00-16:00 ET, 16:00 bar excluded",
        "source": "Yahoo Finance 1-minute OHLCV; historical quotes not substituted for live spread",
        "selected_for_deep_analysis": report["selected_for_deep_analysis"],
        "actually_analyzed": report["actually_analyzed"],
        "score80_count": count,
        "launchpad_eligible_count": report["launchpad_eligible"],
        "rankings": entries,
    }
    write("stage2_full_rankings.json", proof)
    print("VERIFIED STAGE2", json.dumps(proof), flush=True)
    return count

def verify():
    stage1 = read("stage1_report.json")
    stage2 = read("stage2_full_rankings.json")
    if stage1["target_date_et"] != TARGET or stage2["target_date_et"] != TARGET:
        raise RuntimeError("Wrong historical market date")
    if stage2["score80_count"] == 0:
        terminal = {"target_date_et": TARGET, "window": "14:00-16:00 ET",
                    "status": "NO_TRADE", "reason": "Stage2 score80_count=0",
                    "downstream_stages": "not run, per locked SSOT",
                    "mode": "historical_close_session_no_brokerage_orders"}
    else:
        required = ["top25_frozen.json", "stage_bench_report.json", "stage4_report.json", "stage5_report.json"]
        for name in required:
            if not (OUT / name).exists():
                raise RuntimeError("Missing downstream stage: " + name)
        final = read("stage4_report.json")
        terminal = {"target_date_et": TARGET, "window": "14:00-16:00 ET",
                    "status": "NO_LIVE_EXECUTION",
                    "reason": "Historical snapshot cannot prove contemporaneous executable spread",
                    "score80_count": stage2["score80_count"],
                    "launchpad_eligible_count": stage2["launchpad_eligible_count"],
                    "stage4_status": final["status"],
                    "mode": "historical_close_session_no_brokerage_orders"}
    write("terminal_report.json", terminal)
    print("VERIFIED TERMINAL", json.dumps(terminal), flush=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=["reset", "stage1", "stage2", "downstream", "verify"])
    args = parser.parse_args()
    configure()
    if args.stage == "reset":
        if OUT.exists():
            shutil.rmtree(OUT)
        OUT.mkdir(parents=True)
        write("run_manifest.json", {"target_date_et": TARGET, "window": "14:00-16:00 ET",
            "started_utc": datetime.utcnow().isoformat()+"Z",
            "isolation": "output/engine4_two_hour_20261020",
            "prior_engine4_outputs_reused": False,
            "no_live_trade_claim": True})
        print("RESET COMPLETE", flush=True)
    elif args.stage == "stage1":
        lh.stage1(TARGET)
        validate_timestamps()
    elif args.stage == "stage2":
        lh.stage2(TARGET)
        stage2_audit()
    elif args.stage == "downstream":
        if stage2_audit() == 0:
            print("STOP AT STAGE2: verified zero scores >=80", flush=True)
            return
        lh.stage3(TARGET)
        frozen = read("top25_frozen.json")
        frozen["window"] = "14:00-16:00 ET"
        write("top25_frozen.json", frozen)
        lh.bench(TARGET)
        lh.stage4(TARGET)
        lh.stage5(TARGET)
    elif args.stage == "verify":
        verify()

if __name__ == "__main__":
    main()
