#!/usr/bin/env python3
"""Exploratory calendar-day reentry cooldown sensitivity, NOT an out-of-sample test.

Uses frozen historical training-selected cycle trades (24 trades, 6 stocks).
No live orders, no production scoring changes. Run from repository root:
python ofts/experiments/reentry_cooldown_calendar_20261027.py
"""
import csv
from datetime import date
from pathlib import Path
from statistics import mean, median

source = Path("ofts/validation/cycle_execution_trades.csv")
rows = sorted(list(csv.DictReader(source.open(newline=""))), key=lambda x: x["entry_date"])
assert len(rows) == 24 and len({r["symbol"] for r in rows}) == 6

for cooldown in (0, 7, 14, 30):
    last_kept_exit = {}
    kept, blocked = [], []
    for r in rows:
        symbol = r["symbol"]
        gap = ((date.fromisoformat(r["entry_date"]) - last_kept_exit[symbol]).days
               if symbol in last_kept_exit else float("inf"))
        if gap <= cooldown:
            blocked.append((r, gap))
        else:
            kept.append(r)
            last_kept_exit[symbol] = date.fromisoformat(r["exit_date"])
    vals = [float(r["net_20bp_pct"]) for r in kept]
    weighted = sum(vals) / len(rows)  # blocked opportunities assigned 0% (cash)
    print({"cooldown_calendar_days": cooldown, "kept": len(kept),
           "blocked": len(blocked), "mean_net_pct": mean(vals),
           "median_net_pct": median(vals), "winners": sum(v > 0 for v in vals),
           "worst_net_pct": min(vals), "per_original_opportunity_cash_pct": weighted,
           "mean_excluding_top3_pct": mean(sorted(vals, reverse=True)[3:])})
    for r, gap in blocked:
        print("BLOCKED", r["symbol"], r["entry_date"], "days_since_last_kept_exit", gap,
              "original_net_pct", r["net_20bp_pct"])

# Chronological 16/8 split stress check. The same six stocks remain training-selected.
for cooldown in (0, 7, 14, 30):
    last_kept_exit = {}
    accepted = []
    for r in rows:
        symbol = r["symbol"]
        gap = ((date.fromisoformat(r["entry_date"]) - last_kept_exit[symbol]).days
               if symbol in last_kept_exit else float("inf"))
        keep = gap > cooldown
        accepted.append((r, keep))
        if keep:
            last_kept_exit[symbol] = date.fromisoformat(r["exit_date"])
    for label, subset in (("first_16", accepted[:16]), ("last_8", accepted[16:])):
        returns = [float(r["net_20bp_pct"]) if keep else 0.0 for r, keep in subset]
        print("chronological_stress", cooldown, label,
              "kept", sum(keep for _, keep in subset),
              "mean_per_original_opportunity_pct", mean(returns))

print("WARNING: Post-hoc training-selected six-symbol experiment; calendar days, not NYSE sessions.")
print("No portfolio compounding, realistic spreads, IWM, same-stock passive control, or untouched holdout.")
