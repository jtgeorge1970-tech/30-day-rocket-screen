"""Generate extended confirmed swing observations from authentic dated OHLCV.
Research-only. Every feature is computed from bars available at confirmation.
"""
import csv
from collections import defaultdict
from pathlib import Path
from ofts.research.v23_replacement import evaluate
from ofts.research.candidate_components import detect_turns
ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/"ofts/research/extended_history_ohlcv.csv"
OUT=ROOT/"ofts/validation/extended_fingerprint_events.csv"
REPORT=ROOT/"ofts/validation/extended_fingerprint_acceptance.txt"
FIELDS=["symbol","pivot_index","confirmation_index","pivot_type","pivot_price","confirmation_price","confirmation_lag_bars","reversal_threshold_pct","quality_score_asof_confirmation","candidate_status_asof_confirmation","preceding_swing_pct","preceding_swing_bars","future_5d_pct","future_10d_pct","future_20d_pct","research_only"]
def main():
    groups=defaultdict(list)
    with SRC.open(newline="") as f:
        for r in csv.DictReader(f):groups[r["symbol"]].append(r)
    output=[];seen=set();skipped=[]
    for sym,bars in sorted(groups.items()):
        bars.sort(key=lambda r:r["date"])
        h=[float(r["high"]) for r in bars]
        l=[float(r["low"]) for r in bars]
        c=[float(r["close"]) for r in bars]
        if len(c)<201:
            skipped.append(sym);continue
        for end in range(180,len(c)-20):
            # Fixed-length past-only history prevents lookahead and keeps cost bounded.
            begin=max(0,end-260)
            result=evaluate(h[begin:end],l[begin:end],c[begin:end])
            if result["status"]!="CANDIDATE":continue
            threshold=result["threshold_pct"]
            turns=detect_turns(c[begin:end],threshold)
            if len(turns)<2:continue
            idx,kind,price=turns[-1]
            idx+=begin
            key=(sym,idx,kind)
            if key in seen:continue
            # Confirm first appearance at the same threshold, not a changed threshold artifact.
            if (idx-begin,kind,price) in detect_turns(c[begin:end-1],threshold):continue
            prev=turns[-2]
            lag=end-1-idx
            prior_bars=idx-(prev[0]+begin)
            if prior_bars<=0:continue
            seen.add(key)
            entry=c[end-1]
            future=lambda n:round(100*(c[end-1+n]/entry-1),6)
            output.append(dict(symbol=sym,pivot_index=idx,confirmation_index=end-1,pivot_type=kind,pivot_price=round(price,6),confirmation_price=round(entry,6),confirmation_lag_bars=lag,reversal_threshold_pct=round(threshold,6),quality_score_asof_confirmation=round(result["candidate_score"],6),candidate_status_asof_confirmation=result["status"],preceding_swing_pct=round(100*abs(price/prev[2]-1),6),preceding_swing_bars=prior_bars,future_5d_pct=future(5),future_10d_pct=future(10),future_20d_pct=future(20),research_only=True))
    assert len({(r["symbol"],r["pivot_index"],r["pivot_type"]) for r in output})==len(output)
    with OUT.open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(output)
    REPORT.write_text("Extended fingerprint events: "+str(len(output))+"\\nSymbols: "+str(len({r["symbol"] for r in output}))+"\\nSymbols lacking 201 bars: "+",".join(skipped)+"\\nAll event labels 20d available: "+str(all(r["future_20d_pct"]!="" for r in output))+"\\nProduction authorization: NO\\n")
    print(REPORT.read_text())
    if len(output)<100:raise RuntimeError("Historical cohort still too small for training; expand symbol coverage")
if __name__=="__main__":main()
