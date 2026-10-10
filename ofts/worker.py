#!/usr/bin/env python3
"""OFTS v2.3 reproducible research worker. Never represents v2.2 or live BUY signals."""
import csv,json,pathlib,sys
from collections import defaultdict
from ofts.research.v23_replacement import evaluate
from ofts.research.security_regimes import post_identity_bars
from ofts.research.swing_health import recent_swing_health
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
    raw=groups.get(sym,[])
    data=sorted(raw,key=lambda r:r.get("date",""))
    row={"run":ix+1,"symbol":sym,"bars":len(data),"raw_bars":len(raw),
         "regime_start":"","status":"NO_USABLE_HISTORY","score":""}
    try:
        data,regime=post_identity_bars(sym,data)
        row["bars"]=len(data)
        if regime:
            row["regime_start"]=regime["start"]
        if len(data)<180:
            row["status"]="INSUFFICIENT_POST_REGIME_HISTORY" if regime else "NO_USABLE_HISTORY"
        else:
            series=[[float(b[k]) for b in data] for k in ("high","low","close")]
            score=evaluate(*series)
            row.update(status=score["status"],score=score.get("candidate_score",""),version="v2.3-research")
            if score.get("candidate_score") is not None:
                health=recent_swing_health(series[2],score["threshold_pct"])
                row.update(swing_state=health["state"],swing_entry=health["proposed_entry"],
                           swing_reason=health["reason"],high_progression=health["high_progression"],
                           low_progression=health["low_progression"],
                           recent_swing_pct=health["recent_median_amplitude_pct"],
                           amplitude_ratio=health["recent_to_prior_amplitude_ratio"],
                           swing_health_json=json.dumps(health,sort_keys=True))
    except (ValueError,KeyError,TypeError) as e:
        row.update(status="DATA_ERROR",error=str(e))
    results.append(row)
fields=["run","symbol","bars","raw_bars","regime_start","status","score","version","error",
        "swing_state","swing_entry","swing_reason","high_progression","low_progression",
        "recent_swing_pct","amplitude_ratio","swing_health_json"]
with (OUT/"v23_research_universe.csv").open("w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=fields,extrasaction="ignore");w.writeheader();w.writerows(results)
ranked=sorted((r for r in results if isinstance(r["score"],(int,float))),key=lambda r:r["score"],reverse=True)
with (OUT/"v23_research_ranked.csv").open("w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=["rank","symbol","score","status","bars","version",
            "swing_state","swing_entry","swing_reason","high_progression","low_progression",
            "recent_swing_pct","amplitude_ratio"],extrasaction="ignore")
    w.writeheader()
    for rank,r in enumerate(ranked,1):
        w.writerow({"rank":rank,**r})
print("TOP_RESEARCH_RANKINGS",json.dumps([{"rank":i+1,"symbol":r["symbol"],"score":round(r["score"],3),"status":r["status"],"bars":r["bars"],"swing_state":r.get("swing_state"),"swing_entry":r.get("swing_entry") } for i,r in enumerate(ranked[:25])]))
status={"universe":5502,"rows_written":len(results),"candidate_scores":sum(isinstance(r["score"],(int,float)) for r in results),"version":"v2.3-research","production_approved":False,"history_symbols":len(groups)}
(OUT/"status.json").write_text(json.dumps(status,indent=2)+"\n")
print(json.dumps(status))
if not status["candidate_scores"]: raise SystemExit("NO_RESEARCH_SCORES_FROM_AVAILABLE_HISTORY")
