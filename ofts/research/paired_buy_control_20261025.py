#!/usr/bin/env python3
"""Exploratory OFTS matched-date BUY diagnostic; never a production signal.
Usage: python ofts/research/paired_buy_control_20261025.py /path/to/ofts-state
Input must be the frozen 2026-10-24 state artifact (asof 2026-10-23).
"""
import json, statistics, sys
from pathlib import Path

state=Path(sys.argv[1])
outcomes=json.loads((state/"outcomes.json").read_text())
predictions={}
rows=[]
for o in outcomes:
    if o.get("status")!="MATURE" or o.get("horizon")!=5:
        continue
    if o.get("model_hash")!="a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b":
        continue
    date=o["asof"]
    if date not in predictions:
        f=state/"predictions"/(date+"-qualified.json")
        if not f.exists(): f=state/"predictions"/(date+".json")
        predictions[date]={p["symbol"]:p for p in json.loads(f.read_text())["rows"]}
    p=predictions[date].get(o["symbol"],{})
    if p.get("score") is None: continue
    rows.append({**o,"signal":p.get("signal",{}).get("state"),"confidence":p.get("cycle",{}).get("confidence")})
buys=[x for x in rows if x["signal"]=="BUY"]
def paired(width=None):
    pairs=[]
    for b in buys:
        controls=[x for x in rows if x["asof"]==b["asof"] and x["signal"]=="NO_TRADE"
                  and x["classification"]=="CANDIDATE" and x["symbol"]!=b["symbol"]
                  and (width is None or abs(x["score"]-b["score"])<=width)]
        if not controls: continue
        base=statistics.mean(x["net_assumed_return_pct"] for x in controls)
        pairs.append({"date":b["asof"],"symbol":b["symbol"],"buy_net_pct":b["net_assumed_return_pct"],
                      "control_count":len(controls),"control_mean_pct":base,
                      "excess_pp":b["net_assumed_return_pct"]-base})
    return pairs
for label,width in [("same_day",None),("same_day_score_pm10",10)]:
    pairs=paired(width)
    print(label,"N",len(pairs),"mean_excess_pp",statistics.mean(x["excess_pp"] for x in pairs),
          "median_excess_pp",statistics.median(x["excess_pp"] for x in pairs),
          "ex_BETR_mean_excess_pp",statistics.mean(x["excess_pp"] for x in pairs if x["symbol"]!="BETR"))
    for p in pairs:print(p)
print("WARNING: exploratory, 9 BUY observations across 3 dates; overlapping, not independent trades.")
print("Control is DIFFERENT stocks on same signal date, not same-stock passive or alternate-entry benchmark.")
