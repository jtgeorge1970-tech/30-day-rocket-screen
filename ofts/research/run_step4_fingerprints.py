"""Step 4: rebuild chronological confirmed-pivot fingerprint observations for quality oscillators.

Research only. No forward-looking pivots: confirmation occurs only after a reversal.
"""
import csv
from collections import defaultdict
from pathlib import Path
from statistics import median
from ofts.research.v23_replacement import evaluate
from ofts.research.candidate_components import detect_turns, atr_percent

ROOT=Path(__file__).resolve().parents[2]
SOURCES=["historical_controls_206bars_asof_2026-10-02.csv","v23_holdout_206bars_asof_2026-10-02.csv"]
OUT=ROOT/"ofts/validation/step4_fingerprint_events.csv"
FIELDS=["symbol","pivot_index","confirmation_index","pivot_type","pivot_price","confirmation_price","confirmation_lag_bars","reversal_threshold_pct","quality_score_asof_confirmation","candidate_status_asof_confirmation","preceding_swing_pct","preceding_swing_bars","future_5d_pct","future_10d_pct","future_20d_pct","research_only"]
def main():
    groups=defaultdict(list)
    for name in SOURCES:
        with (ROOT/"ofts/research"/name).open(newline="") as f:
            for row in csv.DictReader(f):groups[row["symbol"]].append(row)
    assert len(groups)==13
    out=[]
    eligible=set()
    for symbol,bars in sorted(groups.items()):
        assert len(bars)==206,(symbol,len(bars))
        h=[float(x["high"]) for x in bars];l=[float(x["low"]) for x in bars];c=[float(x["close"]) for x in bars]
        for end in range(180,len(c)+1):
            result=evaluate(h[:end],l[:end],c[:end])
            if result["status"]!="CANDIDATE":continue
            eligible.add(symbol)
            threshold=result["threshold_pct"]
            pts=detect_turns(c[:end],threshold)
            if not pts:continue
            pivot=pts[-1]
            # A pivot first appears at this close: the earliest valid confirmation.
            if end>180 and pivot in detect_turns(c[:end-1],threshold):continue
            # Recomputed ATR thresholds may move. Ensure the pivot is truly confirmed
            # at this observation under the SAME threshold on the prior day.
            if pivot in detect_turns(c[:end-1],threshold):continue
            pidx,kind,price=pivot
            prior=pts[-2] if len(pts)>1 else None
            preceding_pct=100*abs(price/prior[2]-1) if prior else None
            preceding_bars=pidx-prior[0] if prior else None
            entry=c[end-1]
            future=lambda d: round(100*(c[end-1+d]/entry-1),6) if end-1+d<len(c) else ""
            out.append(dict(symbol=symbol,pivot_index=pidx,confirmation_index=end-1,
                pivot_type=kind,pivot_price=round(price,6),confirmation_price=round(entry,6),
                confirmation_lag_bars=end-1-pidx,reversal_threshold_pct=round(threshold,6),
                quality_score_asof_confirmation=round(result["candidate_score"],6),
                candidate_status_asof_confirmation=result["status"],
                preceding_swing_pct=round(preceding_pct,6) if preceding_pct is not None else "",
                preceding_swing_bars=preceding_bars if preceding_bars is not None else "",
                future_5d_pct=future(5),future_10d_pct=future(10),future_20d_pct=future(20),
                research_only=True))
    assert all(x["confirmation_index"]>=x["pivot_index"] for x in out)
    assert len({(x["symbol"],x["confirmation_index"],x["pivot_type"]) for x in out})==len(out)
    OUT.parent.mkdir(parents=True,exist_ok=True)
    with OUT.open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(out)
    report=ROOT/"ofts/validation/step4_acceptance.txt"
    report.write_text(f"STEP 4: RESEARCH DATASET GENERATED\\nStocks examined: {len(groups)}\\nEligible symbols: {len(eligible)}\\nConfirmed pivot events: {len(out)}\\nEvent file: ofts/validation/step4_fingerprint_events.csv\\nProduction approval: NOT GRANTED\\nSample size and future outcomes must be evaluated before model training.\\n")
    print("STEP4",len(groups),"stocks",len(eligible),"eligible",len(out),"events")
    if not out:print("NO CONFIRMED EVENTS: INSUFFICIENT SAMPLE; NOT A SUCCESSFUL FINGERPRINT DATASET")
if __name__=="__main__":main()
