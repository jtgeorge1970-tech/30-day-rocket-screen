"""Chronological out-of-sample check of per-symbol OFTS directional swing outcomes.

70% earlier events train; later 30% test, with a 20-bar embargo.
An event is selected only when the training portion's directional mean > 0
and training count >= 8. All decisions are fixed before testing.
"""
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean
ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/"ofts/validation/extended_fingerprint_events.csv"
OUT=ROOT/"ofts/validation/chronological_holdout_results.csv"
REPORT=ROOT/"ofts/validation/chronological_holdout_acceptance.txt"
def main():
    with SRC.open(newline="") as f: rows=list(csv.DictReader(f))
    bysymbol=defaultdict(list)
    for r in rows: bysymbol[r["symbol"]].append(r)
    results=[]
    for symbol,all_events in sorted(bysymbol.items()):
        all_events.sort(key=lambda r:int(r["confirmation_index"]))
        split=int(len(all_events)*.7)
        if split<8 or split>=len(all_events):continue
        boundary=int(all_events[split]["confirmation_index"])
        train=[r for r in all_events[:split] if int(r["confirmation_index"])+20<boundary]
        test=all_events[split:]
        for side,kind,sign in (("BUY","L",1),("SELL","H",-1)):
            a=[sign*float(r["future_20d_pct"]) for r in train if r["pivot_type"]==kind]
            b=[sign*float(r["future_20d_pct"]) for r in test if r["pivot_type"]==kind]
            eligible=len(a)>=8 and mean(a)>0 if a else False
            results.append(dict(symbol=symbol,side=side,train_events=len(a),train_mean_20d_pct=round(mean(a),3) if a else "",selected_by_train=eligible,test_events=len(b),test_mean_20d_pct=round(mean(b),3) if b else "",test_win_rate_pct=round(100*sum(x>0 for x in b)/len(b),2) if b else ""))
    assert results
    with OUT.open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(results[0]));w.writeheader();w.writerows(results)
    selected=[r for r in results if r["selected_by_train"] and r["test_events"]]
    buy=[r for r in selected if r["side"]=="BUY"]
    sell=[r for r in selected if r["side"]=="SELL"]
    REPORT.write_text("\n".join(["Chronological 70/30 holdout with 20-bar embargo","Research cohort symbols: "+str(len(bysymbol)),"Side-specific holdout rows: "+str(len(results)),"Selected rows with test observations: "+str(len(selected)),"Selected positive test means: "+str(sum(r["test_mean_20d_pct"]>0 for r in selected)),"Selected BUY groups: "+str(len(buy)),"Selected BUY positive test means: "+str(sum(r["test_mean_20d_pct"]>0 for r in buy)),"Selected SELL groups: "+str(len(sell)),"Selected SELL positive test means: "+str(sum(r["test_mean_20d_pct"]>0 for r in sell)),"Independent untouched dataset: NOT ESTABLISHED","SELL research gate: REJECT - only "+str(sum(r["test_mean_20d_pct"]>0 for r in sell))+"/"+str(len(sell))+" selected groups positive","BUY research gate: PROMISING - NOT PRODUCTION APPROVED","Production approval: NO",""]))
    print(REPORT.read_text())
if __name__=="__main__":main()
