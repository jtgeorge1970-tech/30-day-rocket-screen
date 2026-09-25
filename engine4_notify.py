from __future__ import annotations

"""Engine 4 notification recorder.

Trading logic is untouched. Every notification that previously went to SMS is
preserved verbatim as an on-screen/audit artifact. Notification transport can
never stop the engine.
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

OUT = Path("output/engine4")
ET = ZoneInfo("America/New_York")


def _read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _signal_for(kind: str, supplied: str | None) -> dict:
    if kind == "final":
        return _read_json(OUT / "final_signal.json")
    if kind == "recovery":
        return _read_json(OUT / "recovery_signal.json")
    if kind == "complete":
        primary = _read_json(OUT / "final_signal.json")
        recovery = _read_json(OUT / "recovery_signal.json")
        bench = _read_json(OUT / "watch_bench_report.json")
        ps = str(primary.get("status") or "UNAVAILABLE").upper()
        rs = str(recovery.get("status") or "UNAVAILABLE").upper()
        outcome = "BUY/ARM SIGNAL PRESENT" if {ps, rs} & {"BUY", "ARM"} else "NO BUY SIGNAL TODAY"
        watch = ", ".join(str(r.get("ticker")) for r in bench.get("candidates", []) if r.get("ticker")) or "NONE"
        return {"status": "COMPLETE", "ticker": "SYSTEM", "message": supplied or f"{outcome}\nPrimary: {ps}\nRecovery: {rs}\nWatchlist: {watch}"}
    defaults = {
        "preflight": ("CHECKING", "SYSTEM", "Engine 4 early preflight is active."),
        "launch": ("DISPATCHED", "SYSTEM", "Engine 4 early controller dispatched production."),
        "watchdog": ("RECOVERY_DISPATCHED", "SYSTEM", "Engine 4 watchdog dispatched a recovery wake."),
        "start": ("STARTED", "SYSTEM", "Engine 4 scheduled run started."),
        "prescreen": ("COMPLETED", "MARKET", "Engine 4 prescreen stage completed."),
        "deep": ("COMPLETED", "MARKET", "Engine 4 deep stage completed."),
        "freeze": ("COMPLETED", "MARKET", "Engine 4 freeze stage completed."),
        "bench": ("COMPLETED", "MARKET", "Engine 4 bench stage completed."),
        "failure": ("PIPELINE_FAILURE", "SYSTEM", "ENGINE 4 DATA/PIPELINE FAILURE"),
        "test": ("TEST", "SYSTEM", "Engine 4 notification test."),
    }
    status, ticker, message = defaults.get(kind, ("UNKNOWN", "MARKET", "Engine 4 notification."))
    return {"status": status, "ticker": ticker, "message": supplied or message}


def notify(kind: str, supplied: str | None = None, dry_run: bool = False) -> dict:
    OUT.mkdir(parents=True, exist_ok=True)
    signal = _signal_for(kind, supplied)
    status = str(signal.get("status") or "UNKNOWN").upper()
    ticker = str(signal.get("ticker") or "MARKET").upper()
    message = str(signal.get("message") or signal.get("reason") or supplied or "No message supplied.")
    date_et = str(signal.get("target_date_et") or datetime.now(ET).date())
    run_id = os.getenv("GITHUB_RUN_ID", "").strip()
    generated = datetime.now(ET).strftime("%Y-%m-%d %I:%M:%S %p ET")
    heading = f"ENGINE 4 {kind.upper()}: {status} — {ticker}"
    progress = "The full Engine 4 run is NOT complete. Recovery watch and terminal verification continue." if kind == "final" else ""
    text = "\n".join(x for x in (heading, message, progress, f"Run {run_id}" if run_id else "", f"Generated {generated}", "Confirm the live broker quote before any order.") if x)
    marker = f"ENGINE4-ALERT:{date_et}:{kind}:{status}:{ticker}:RUN:{run_id or 'NO-RUN'}"
    record = {"delivery": "SAVED_ONSCREEN", "marker": marker, "kind": kind, "status": status, "ticker": ticker, "target_date_et": date_et, "generated_et": generated, "run_id": run_id, "message": message, "notification_text": text, "dry_run": dry_run}
    (OUT / f"notification_{kind}.txt").write_text(text + "\n", encoding="utf-8")
    (OUT / f"notification_{kind}.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    (OUT / "notification_audit.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    log_path = OUT / "notification_audit_log.json"
    try:
        history = json.loads(log_path.read_text(encoding="utf-8"))
        if not isinstance(history, list): history = []
    except Exception:
        history = []
    history.append(record)
    log_path.write_text(json.dumps(history, indent=2), encoding="utf-8")
    print("=== ENGINE 4 ON-SCREEN NOTIFICATION ===", flush=True)
    print(text, flush=True)
    print("=== END ENGINE 4 NOTIFICATION ===", flush=True)
    return record


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=("preflight","launch","watchdog","start","prescreen","deep","freeze","bench","final","recovery","complete","failure","test"))
    parser.add_argument("--message")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--require-delivery", action="store_true")
    args = parser.parse_args()
    result = notify(args.kind, args.message, args.dry_run)
    print(json.dumps(result, indent=2), flush=True)
    # Saved on-screen notification is the delivery contract. It never depends on SMS.
    if args.require_delivery and result.get("delivery") != "SAVED_ONSCREEN":
        raise SystemExit(1)

if __name__ == "__main__":
    main()
