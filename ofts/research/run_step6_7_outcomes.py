import csv
from pathlib import Path
from statistics import mean
root=Path(__file__).resolve().parents[2]
source=root/"ofts/validation/step5_fingerprint_scores.csv"
dest=root/"ofts/validation/step6_7_outcomes.csv"
report=root/"ofts/validation/step6_7_acceptance.txt"
with source.open(newline="") as f: rows=list(csv.DictReader(f))
assert rows
result=[]
for side in ("BUY","SELL"):
    for days in (5,10,20):
        field=f"future_{days}d_pct"
        subset=[r for r in rows if r[field]!=" " and r[field]!=""]
        subset=[r for r in subset if r["signal_side"]==side]
        sign=1 if side=="BUY" else -1
        vals=[sign*float(r[field]) for r in subset]
        result.append({"side":side,"horizon":days,"count":len(vals),"win_rate":round(sum(v>0 for v in vals)/len(vals),4) if vals else "","mean_directional_return":round(mean(vals),4) if vals else ""})
with dest.open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(result[0]));w.writeheader();w.writerows(result)
n20=sum(r["future_20d_pct"]!="" for r in rows)
cbrs=any(r["symbol"]=="CBRS" for r in rows)
report.write_text(f"Research events: {len(rows)}\\n20-day labeled: {n20}\\nCBRS present: {cbrs}\\nStep 6: {'REQUIRES DEDICATED CBRS TEST' if cbrs else 'BLOCKED - CBRS data absent'}\\nStep 7: BLOCKED - independent untouched validation not established\\nProduction authorization: NO\\n")
print(report.read_text())
