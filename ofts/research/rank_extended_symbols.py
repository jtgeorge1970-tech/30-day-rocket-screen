"""Rank confirmed historical OFTS swing fingerprints by 20-day outcomes.
Research-only descriptive analysis; do not infer executable fills or production signals.
"""
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean
ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/"ofts/validation/extended_fingerprint_events.csv"
OUT=ROOT/"ofts/validation/extended_symbol_results.csv"
REPORT=ROOT/"ofts/validation/extended_symbol_summary.txt"
def main():
    with SRC.open(newline="") as f: rows=list(csv.DictReader(f))
    grouped=defaultdict(list)
    for r in rows:grouped[(r["symbol"],"BUY" if r["pivot_type"]=="L" else "SELL")].append(r)
    result=[]
    for (symbol,side),events in grouped.items():
        sign=1 if side=="BUY" else -1
        values=[sign*float(r["future_20d_pct"]) for r in events]
        result.append(dict(symbol=symbol,side=side,events=len(events),win_rate_pct=round(100*sum(v>0 for v in values)/len(values),2),mean_directional_20d_pct=round(mean(values),3),median_score=round(sorted(float(r["quality_score_asof_confirmation"]) for r in events)[len(events)//2],3),status="RESEARCH_ONLY"))
    result.sort(key=lambda r:(r["side"],-r["mean_directional_20d_pct"]))
    with OUT.open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(result[0]));w.writeheader();w.writerows(result)
    REPORT.write_text("Historical events: "+str(len(rows))+"\nSymbols: "+str(len({r["symbol"] for r in rows}))+"\nResearch rankings: "+str(len(result))+"\nIndependent holdout: NOT COMPLETE\nProduction signals: NOT APPROVED\n")
    print(REPORT.read_text())
if __name__=="__main__":main()
