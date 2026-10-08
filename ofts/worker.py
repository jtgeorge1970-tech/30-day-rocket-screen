#!/usr/bin/env python3
"""OFTS v2.3 reproducible research worker. Never represents v2.2 or live BUY signals."""
import csv,json,pathlib,sys
from collections import defaultdict
from ofts.research.v23_replacement import evaluate
ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/"ofts-output"
OUT.mkdir(exist_ok=True)
universe=ROOT/"ofts/universe.csv"
with universe.open(newline="",encoding="utf-8-sig") as fh:
    rows=list(csv.DictReader(fh))
symbols=[(r.get("Symbol") or r.get("symbol") or r.get("Ticker") or "").strip().upper() for r in rows]
if len(symbols)!=5502 or len(set(symbols))!=5502:
    raise SystemExit("INVALID_UNIVERSE")
history=OUT/"universe_ohlcv.csv"
if not history.exists(): raise SystemExit("MISSING_DOWNLOADED_HISTORY")
with history.open(newline="",encoding="utf-8-sig") as fh:
    bars=list(csv.DictReader(fh))
if not bars: raise SystemExit("EMPTY_HISTORY")
print("HISTORY_COLUMNS",list(bars[0]))
groups=defaultdict(list)
for bar in bars:
    s=(bar.get("symbol") or bar.get("Symbol") or "").upper().strip()
    if s: groups[s].append(bar)
results=[]
for ix in range(5502):
    sym=symbols[(ix*137)%5502]
    data=groups.get(sym,[])
    row={"run":ix+1,"symbol":sym,"bars":len(data),"status":"NO_USABLE_HISTORY","score":""}
    if len(data)>=180:
        try:
            if "date" in data[0]: data=sorted(data,key=lambda r:r["date"])
            score=evaluate(*[[float(b[k]) for b in data] for k in ("high","low","close")])
            row.update(status=score["status"],score=score.get("candidate_score",""),version="v2.3-research")
        except (ValueError,KeyError,TypeError) as e:
            row.update(status="DATA_ERROR",error=str(e))
    results.append(row)
fields=["run","symbol","bars","status","score","version","error"]
with (OUT/"v23_research_universe.csv").open("w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=fields,extrasaction="ignore");w.writeheader();w.writerows(results)
ranked=sorted((r for r in results if isinstance(r["score"],(int,float))),key=lambda r:r["score"],reverse=True)
with (OUT/"v23_research_ranked.csv").open("w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=["rank","symbol","score","status","bars","version"])
    w.writeheader()
    for rank,r in enumerate(ranked,1):
        w.writerow({"rank":rank,**r})
print("TOP_RESEARCH_RANKINGS",json.dumps([{"rank":i+1,"symbol":r["symbol"],"score":round(r["score"],3),"status":r["status"],"bars":r["bars"]} for i,r in enumerate(ranked[:25])]))
status={"universe":5502,"rows_written":len(results),"candidate_scores":sum(isinstance(r["score"],(int,float)) for r in results),"version":"v2.3-research","production_approved":False,"history_symbols":len(groups)}
(OUT/"status.json").write_text(json.dumps(status,indent=2)+"\n")
print(json.dumps(status))
if not status["candidate_scores"]: raise SystemExit("NO_RESEARCH_SCORES_FROM_AVAILABLE_HISTORY")
