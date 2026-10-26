#!/usr/bin/env python3
"""OFTS exploratory historical exit-rule sensitivity; NOT prospective validation.

Usage: python ofts/experiments/historical_exit_sensitivity_20261026.py
Input: ofts/validation/cycle_execution_trades.csv from v2.3 research branch.
Compares IDENTICAL 24 historical trades with original exits vs fixed/trailing 12% exits.
Assumes 0.20 percentage-point round-trip cost for all three return series.
The source's stop fills, fees, liquidity, and corporate actions are not independently revalidated.
"""
import csv
import statistics
from pathlib import Path

p=Path("ofts/validation/cycle_execution_trades.csv")
rows=list(csv.DictReader(p.open(newline="")))
assert len(rows)==24, f"Expected frozen historical 24 trades; found {len(rows)}"
assert len({r["symbol"] for r in rows})==6
series={
    "original_net": [float(r["net_20bp_pct"]) for r in rows],
    "fixed_12pct_net": [float(r["fixed_stop_12_pct"])-0.20 for r in rows],
    "trailing_12pct_net": [float(r["trailing_stop_12_pct"])-0.20 for r in rows],
}
for name,returns in series.items():
    sorted_best=sorted(returns,reverse=True)
    print(name, {
        "n":len(returns),
        "mean_pct":round(statistics.mean(returns),6),
        "median_pct":round(statistics.median(returns),6),
        "positive":sum(x>0 for x in returns),
        "worst_pct":round(min(returns),6),
        "mean_without_top3_pct":round(statistics.mean(sorted_best[3:]),6),
        "losses_below_minus20pct":sum(x < -20 for x in returns),
    })
original=series["original_net"]
for key in ("fixed_12pct_net","trailing_12pct_net"):
    diff=[a-b for a,b in zip(series[key],original)]
    print(key+"_paired_change",{"mean_pp":round(statistics.mean(diff),6),
                                 "median_pp":round(statistics.median(diff),6),
                                 "better_count":sum(x>0 for x in diff)})
for symbol in sorted({r["symbol"] for r in rows}):
    keep=[float(r["net_20bp_pct"]) for r in rows if r["symbol"]!=symbol]
    print("leave_one_symbol_out",symbol, len(keep),round(statistics.mean(keep),6))
print("WARNING: TRAINING-SELECTED historical symbols; reused sample, not independent holdout.")
print("No same-stock passive benchmark, SPY/IWM pairing, verified execution, or portfolio drawdown.")
