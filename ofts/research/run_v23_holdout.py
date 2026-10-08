"""Research holdout: never fit parameters using these symbols."""
import csv,pathlib
from ofts.research.v23_replacement import evaluate
root=pathlib.Path(__file__).resolve().parents[2]
source=root/"ofts/research/v23_holdout_206bars_asof_2026-10-02.csv"
groups={}
with source.open(newline="") as f:
    for row in csv.DictReader(f):groups.setdefault(row["symbol"],[]).append(row)
assert set(groups)=={"MU","STX","HOOD"}
out=[]
for symbol,bars in sorted(groups.items()):
    assert len(bars)==206
    r=evaluate(*[[float(b[k]) for b in bars] for k in ("high","low","close")])
    assert r["production_eligible"] is False
    assert 0<=r["candidate_score"]<=100
    assert abs(r["candidate_score"]-(.75*r["structural"]["quality"]+.25*r["recent"]["quality"]))<1e-8
    out.append((symbol,r["status"],round(r["candidate_score"],3),r["structural"]["swings"],round(r["recent"]["median_swing_pct"],3)))
for x in out:print("HOLDOUT",*x)
print("RESEARCH ONLY — NO BUY SIGNALS")
