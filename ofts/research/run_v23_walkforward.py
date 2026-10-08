"""Step 3 chronological, leakage-safe research validation and negative controls."""
import csv, pathlib, statistics
from ofts.research.v23_replacement import evaluate
ROOT=pathlib.Path(__file__).resolve().parents[2]
FILES=["historical_controls_206bars_asof_2026-10-02.csv","v23_holdout_206bars_asof_2026-10-02.csv"]
def read():
    grouped={}
    for name in FILES:
        with (ROOT/"ofts/research"/name).open(newline="") as f:
            for row in csv.DictReader(f):
                grouped.setdefault(row["symbol"],[]).append(row)
    return grouped
def eval_rows(rows):
    return evaluate(*[[float(r[k]) for r in rows] for k in ("high","low","close")])
def rolling(symbol,rows):
    # Score only with bars observable as of the signal date; forward returns are never inputs.
    out=[]
    for end in range(180,len(rows)-19,5):
        x=eval_rows(rows[:end])
        entry=float(rows[end-1]["close"])
        if entry<=0: continue
        future=[float(r["close"]) for r in rows[end:end+20]]
        out.append({"symbol":symbol,"end_index":end,"score":x.get("candidate_score"),
                    "status":x["status"],"forward_5d_pct":100*(future[4]/entry-1),
                    "forward_10d_pct":100*(future[9]/entry-1),
                    "forward_20d_pct":100*(future[19]/entry-1)})
    return out
def negative_controls():
    # Designed series: smooth trend, fixed oscillator, deterministic alternating noise.
    n=206
    scenarios={
      "monotonic_trend":[10+.2*i for i in range(n)],
      "regular_oscillation":[20+3*((i%20)/10 if i%20<=10 else (20-i%20)/10) for i in range(n)],
      "alternating_noise":[20+(2 if i%2 else -2) for i in range(n)]
    }
    out=[]
    for name,closes in scenarios.items():
        highs=[x*1.01 for x in closes]
        lows=[x*.99 for x in closes]
        r=evaluate(highs,lows,closes)
        out.append((name,r["status"],round(r.get("candidate_score",0),3),r.get("structural",{}).get("swings",0)))
        if name in ("monotonic_trend","alternating_noise"):
            assert r["status"]!="CANDIDATE", f"{name} negative control incorrectly passed"
        if name=="regular_oscillation":
            assert r["structural"]["swings"]>=4, "Regular oscillator was not detected"
    return out
def main():
    grouped=read()
    assert len(grouped)==13
    rows=[v for s,b in grouped.items() for v in rolling(s,b)]
    assert len(rows)>=13, "Not enough chronological observations"
    target=ROOT/"ofts/validation/v23_walkforward_results.csv"
    with target.open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    controls=negative_controls()
    print("WALKFORWARD",len(rows),"events across",len(grouped),"symbols")
    for name,status,score,swings in controls:print("NEGATIVE_CONTROL",name,status,score,swings)
    for horizon in ("forward_5d_pct","forward_10d_pct","forward_20d_pct"):
        eligible=[x[horizon] for x in rows if x["status"]=="CANDIDATE"]
        print(horizon,"candidate_n",len(eligible),"mean_pct",round(statistics.mean(eligible),3) if eligible else "NA")
    assert all(0<=v["score"]<=100 for v in rows), "Score outside 0-100 range"
    report=ROOT/"ofts/validation/step3_final_acceptance.txt"
    report.write_text("STEP 3 RESEARCH VALIDATION: PASS\\n"+f"Historical controls: {len(grouped)}\\nWalk-forward observations: {len(rows)}\\nNegative controls: {len(controls)}\\n"+ "Predictive profitability: NOT ESTABLISHED\\nProduction authorization: BLOCKED\\n")
    print("INTEGRATION TEST PASSED; PREDICTIVE VALIDITY NOT IMPLIED")
if __name__=="__main__":main()
