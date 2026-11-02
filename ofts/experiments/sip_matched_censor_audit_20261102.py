#!/usr/bin/env python3
"""Read-only OFTS SIP-marked same-stock benchmark and stop sensitivity.

Usage:
  python ofts/experiments/sip_matched_censor_audit_20261102.py \
      /path/to/checkout-of-ofts-daily-state \
      ofts/experiments/SIP_DAILY_BARS_2026-10-09_TO_2026-10-30.csv

State checkout must be the 2026-10-30 frozen commit eb05038a4e793e5ecb844b8fcd321e3ccb8e9db9.
Data are independent Alpaca SIP daily bars, saved separately for reproducibility.
Open positions are censored at October 30 close; never call this realized P&L.
"""
import collections
import csv
import json
import pathlib
import statistics
import sys

CUTOFF = "2026-10-30"
COST_PCT = 0.20


def load_bars(path):
    out = collections.defaultdict(dict)
    with path.open(newline="") as f:
        for row in csv.DictReader(f):
            out[row["symbol"]][row["date"]] = {
                k: float(row[k]) for k in ("open", "high", "low", "close")
            }
    return out


def mean(xs):
    return statistics.mean(xs) if xs else None


def summarize(rows, key):
    xs = [r[key] for r in rows if r.get(key) is not None]
    return {"n": len(xs), "mean_pct": mean(xs),
            "median_pct": statistics.median(xs) if xs else None,
            "positive": sum(x > 0 for x in xs)}


def audit(state_dir, bars_csv):
    ledger = json.loads((state_dir / "cycle_ledger.json").read_text())
    bars = load_bars(bars_csv)
    positions = [
        dict(x, _closed=False) for x in ledger["positions"]
        if x.get("entry_date") and x.get("entry_open")
        and x["status"] != "PENDING_ENTRY"
    ]
    trades = [dict(x, _closed=True) for x in ledger["trades"]]
    rows, exceptions = [], []
    for p in positions + trades:
        sym, entry_date = p["symbol"], p["entry_date"]
        end_date = p["exit_date"] if p["_closed"] else CUTOFF
        needed = [(sym, entry_date), (sym, end_date),
                  ("SPY", entry_date), ("SPY", end_date),
                  ("IWM", entry_date), ("IWM", end_date)]
        if any(d not in bars[s] for s, d in needed):
            exceptions.append({"symbol": sym, "reason": "MISSING_BAR"})
            continue
        entry = float(p["entry_open"])
        exit_price = float(p["exit_open"]) if p["_closed"] else bars[sym][end_date]["close"]
        entry_difference_pct = 100 * (bars[sym][entry_date]["open"] / entry - 1)
        exit_difference_pct = (100 * (bars[sym][end_date]["open"] / exit_price - 1)
                               if p["_closed"] else None)
        if abs(entry_difference_pct) > .5 or (
            exit_difference_pct is not None and abs(exit_difference_pct) > .5
        ):
            exceptions.append({"symbol": sym, "reason": "LEDGER_SIP_PRICE_MISMATCH",
                               "entry_difference_pct": entry_difference_pct,
                               "exit_difference_pct": exit_difference_pct})
            continue
        sessions = sorted(d for d in bars[sym] if entry_date <= d <= end_date)
        delayed = next((d for d in sessions if entry_date < d < end_date), None)
        net = 100 * (exit_price / entry - 1) - COST_PCT
        def bench(sym_b):
            buy = bars[sym_b][entry_date]["open"]
            sell = bars[sym_b][end_date]["open" if p["_closed"] else "close"]
            return 100 * (sell / buy - 1)
        stop_returns = {}
        for pct in (5, 10, 12):
            stop = entry * (1 - pct / 100)
            fill = None
            for d in sessions:
                if p["_closed"] and d == end_date:
                    break  # Original SELL executes at this day's open.
                bar = bars[sym][d]
                if bar["open"] <= stop:
                    fill = bar["open"]  # Gap-through at opening price.
                    break
                if bar["low"] <= stop:
                    fill = stop  # Optimistic intraday stop fill.
                    break
            stop_returns[str(pct)] = (
                100 * (fill / entry - 1) - COST_PCT if fill is not None else net
            )
        rows.append({
            "symbol": sym, "entry_date": entry_date, "end_date": end_date,
            "closed": p["_closed"], "net_pct": net, "spy_pct": bench("SPY"),
            "iwm_pct": bench("IWM"),
            "delayed_net_pct": (100 * (exit_price / bars[sym][delayed]["open"] - 1)
                                - COST_PCT) if delayed else None,
            "stop_net_pct": stop_returns,
        })
    ranked = sorted(rows, key=lambda x: x["net_pct"], reverse=True)
    return {
        "market_cutoff": CUTOFF,
        "sample": {"total_executed": len(positions) + len(trades),
                   "verified": len(rows), "closed": len(trades),
                   "open_censored": len(positions)},
        "exceptions": exceptions,
        "all": {k: summarize(rows, k) for k in
                ("net_pct", "spy_pct", "iwm_pct", "delayed_net_pct")},
        "paired_delay_advantage_pct": mean([
            x["net_pct"] - x["delayed_net_pct"] for x in rows
            if x["delayed_net_pct"] is not None
        ]),
        "stops": {str(pct): summarize([
            {"value": x["stop_net_pct"][str(pct)]} for x in rows
        ], "value") for pct in (5, 10, 12)},
        "exclude_top": {
            str(n): {"remaining": len(ranked[n:]),
                     "net_mean_pct": mean([x["net_pct"] for x in ranked[n:]]),
                     "spy_mean_pct": mean([x["spy_pct"] for x in ranked[n:]]),
                     "iwm_mean_pct": mean([x["iwm_pct"] for x in ranked[n:]])}
            for n in (0, 1, 2, 3, 5)
        },
        "closed": [x for x in rows if x["closed"]],
        "top": ranked[:5],
        "warning": "Open positions are censored and marked to the cutoff close. "
                   "Fixed stop fills assume intraday execution at the trigger, "
                   "which is optimistic; no spread, impact, or position sizing. "
                   "This is retrospective and not a chronological untouched holdout.",
    }


if __name__ == "__main__":
    root = pathlib.Path(sys.argv[1])
    bars_path = pathlib.Path(sys.argv[2])
    print(json.dumps(audit(root, bars_path), indent=2, sort_keys=True))
