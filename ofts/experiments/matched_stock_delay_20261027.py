#!/usr/bin/env python3
"""Research-only paired same-stock entry-delay diagnostic (2026-10-27).
Run from repository root: python ofts/experiments/matched_stock_delay_20261027.py
No production scoring changes, no brokerage activity.
"""
import csv
from pathlib import Path
from statistics import mean, median

ROOT = Path("ofts")
bars = {}
for filename in ("research/historical_control_bars_2025-10_to_2026-09.csv",
                 "research/historical_controls_206bars_asof_2026-10-02.csv"):
    with (ROOT / filename).open(newline="") as f:
        for row in csv.DictReader(f):
            bars.setdefault(row["symbol"], {})[row["date"]] = row

with (ROOT / "validation/cycle_execution_trades.csv").open(newline="") as f:
    trades = list(csv.DictReader(f))

pairs = []
for trade in trades:
    history = bars.get(trade["symbol"], {})
    dates = sorted(history)
    entry = trade["entry_date"]
    exit_date = trade["exit_date"]
    if entry not in history or exit_date not in history:
        continue
    index = dates.index(entry)
    if index + 1 >= len(dates) or dates[index + 1] >= exit_date:
        continue
    original_open = float(history[entry]["open"])
    delayed_open = float(history[dates[index + 1]]["open"])
    exit_open = float(history[exit_date]["open"])
    baseline = 100 * (exit_open / original_open - 1) - 0.20
    delayed = 100 * (exit_open / delayed_open - 1) - 0.20
    entry_discrepancy = 100 * (original_open / float(trade["entry_open"]) - 1)
    exit_discrepancy = 100 * (exit_open / float(trade["exit_open"]) - 1)
    pairs.append((trade["symbol"], entry, baseline, delayed,
                  baseline - delayed, entry_discrepancy, exit_discrepancy))

assert len(pairs) == 15, f"Expected 15 matched historical trades; found {len(pairs)}"
print("Matched trades:", len(pairs), "of", len(trades))
print("Symbols:", sorted({p[0] for p in pairs}))
for name, index in (("Baseline", 2), ("One-session-delayed", 3)):
    values = [p[index] for p in pairs]
    print(name, "mean", round(mean(values), 6), "median", round(median(values), 6),
          "winners", sum(v > 0 for v in values), "worst", round(min(values), 6))
deltas = [p[4] for p in pairs]
print("Baseline minus delay mean", round(mean(deltas), 6),
      "median", round(median(deltas), 6),
      "baseline better pairs", sum(v > 0 for v in deltas))
print("Entry discrepancies >0.5pp", sum(abs(p[5]) > 0.5 for p in pairs))
print("Exit discrepancies >0.5pp", sum(abs(p[6]) > 0.5 for p in pairs))
print("Mean absolute entry discrepancy", round(mean(abs(p[5]) for p in pairs), 6))
for p in pairs:
    print("%s %s baseline=%+.3f%% delayed=%+.3f%% delta=%+.3fpp entry_gap=%+.3fpp exit_gap=%+.3fpp" % p)
