#!/usr/bin/env python3
"""Point-in-time OFTS BUY vs experimental viability-veto audit.

Run with a checkout of the durable ofts-daily-state branch:
  python viability_veto_audit_20261102.py /path/to/ofts-daily-state

Read-only. No market-data download, brokerage orders, or production changes.
"""
import collections
import json
import pathlib
import sys


def audit(state_dir: pathlib.Path) -> dict:
    ledger = json.loads((state_dir / "cycle_ledger.json").read_text())
    positions = list(ledger["positions"])
    trades = list(ledger["trades"])
    all_entries = positions + trades
    entry_keys = {(p["entry_signal_date"], p["symbol"]) for p in all_entries}
    buy_rows = []
    for path in sorted((state_dir / "signals").glob("????-??-??.json")):
        payload = json.loads(path.read_text())
        day = payload["asof"]
        for row in payload.get("rows", []):
            if (row.get("signal") or {}).get("state") != "BUY":
                continue
            viability = row.get("recent_viability") or {}
            buy_rows.append({
                "date": day,
                "symbol": row["symbol"],
                "score": row.get("score"),
                "confidence": (row.get("cycle") or {}).get("confidence"),
                "viability_state": viability.get("state", "NOT_RECORDED"),
                "proposed_entry": viability.get("proposed_entry", "NOT_RECORDED"),
                "reason": viability.get("reason", "NOT_RECORDED"),
                "ledger_entry": (day, row["symbol"]) in entry_keys,
            })
    vetoes = [r for r in buy_rows if r["proposed_entry"] == "NO_TRADE"]
    missing = [r for r in buy_rows if r["proposed_entry"] == "NOT_RECORDED"]
    accepted = [r for r in buy_rows if r["proposed_entry"] not in ("NO_TRADE", "NOT_RECORDED")]
    duplicates = [r for r in buy_rows if not r["ledger_entry"]]
    return {
        "source_market_session": max(r["date"] for r in buy_rows),
        "buy_events": len(buy_rows),
        "ledger_entries": len(all_entries),
        "vetoed_buy_events": len(vetoes),
        "unassessed_buy_events": len(missing),
        "accepted_buy_events": len(accepted),
        "veto_reason_counts": dict(collections.Counter(r["viability_state"] for r in vetoes)),
        "confidence_counts": dict(collections.Counter(r["confidence"] for r in buy_rows)),
        "no_new_entry_events": duplicates,
        "completed_trades": [
            {"symbol": t["symbol"], "entry_signal_date": t["entry_signal_date"],
             "net_pct": t["net_assumed_return_pct"]}
            for t in trades
        ],
        "lyel_buy": [r for r in buy_rows if r["symbol"] == "LYEL"],
        "assessed_buy_events": len(vetoes) + len(accepted),
        "warning": "Experimental viability veto is not a validated strategy. "
                   "Open positions have no realized outcome. Do not infer returns "
                   "from filtering completed losers or hindsight winners.",
    }


if __name__ == "__main__":
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    print(json.dumps(audit(root), indent=2, sort_keys=True))
