"""Run v2.3 research candidate against ten historical controls; never promote automatically."""
import csv, pathlib, sys
from ofts.research.v23_replacement import evaluate
root=pathlib.Path(__file__).resolve().parents[2]
source=root/"ofts/research/historical_controls_206bars_asof_2026-10-02.csv"
target=root/"ofts/validation/v23_candidate_results.csv"
groups={}
with source.open(newline="") as f:
    for row in csv.DictReader(f):
        groups.setdefault(row["symbol"],[]).append(row)
expected={"AAL":58.3,"KBR":57.9,"ROCK":48.2,"WW":46.9,"AEHR":34.9,
          "AXTI":40.7,"BKSY":53.2,"PLTR":53.0,"CHPT":50.3,"AIP":49.3}
out=[]
for symbol,bars in sorted(groups.items()):
    if len(bars)!=206: raise AssertionError(f"{symbol}: {len(bars)} bars, expected 206")
    result=evaluate(*[[float(b[k]) for b in bars] for k in ("high","low","close")])
    structural=result["structural"]["quality"]
    recent=result["recent"]["quality"]
    out.append({"symbol":symbol,"bars":len(bars),"status":result["status"],
                "candidate_structural":round(structural,3),
                "ssot_structural":expected[symbol],
                "structural_delta":round(structural-expected[symbol],3),
                "recent":round(recent,3),"candidate_final":round(result["candidate_score"],3),
                "confirmed_swings":result["structural"]["swings"],
                "median_swing_pct":round(result["structural"]["median_swing_pct"],3),
                "production_eligible":result["production_eligible"]})
    assert result["production_eligible"] is False
    assert abs(result["candidate_score"]-(.75*structural+.25*recent))<1e-9
with target.open("w",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=list(out[0]))
    writer.writeheader()
    writer.writerows(out)
print("RESEARCH TEST COMPLETE:",len(out),"controls")
for row in out: print(row)
print("PRODUCTION APPROVAL: BLOCKED; OUT-OF-SAMPLE VALIDATION NOT DONE")
