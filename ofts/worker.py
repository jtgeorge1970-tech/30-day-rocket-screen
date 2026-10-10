#!/usr/bin/env python3
"""OFTS v2.3 reproducible research worker. Never represents v2.2 or live BUY signals."""
import csv,json,pathlib,sys
from collections import defaultdict
from ofts.research.v23_replacement import evaluate
from ofts.research.security_regimes import post_identity_bars
from ofts.research.swing_health import recent_swing_health
from ofts.research.recent_viability import recent_swing_viability
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
                viability=recent_swing_viability(series[2],score["threshold_pct"])
                row.update(viability_state=viability["state"],
                           viability_entry=viability["proposed_entry"],
                           viability_reason=viability["reason"],
                           recent_three_swing_pct=viability.get("last_three_median_swing_pct"),
                           recent_two_up_pct=viability.get("recent_up_median_pct"),
                           last_three_up_pct=json.dumps(viability.get("last_three_up_pct",[])),
                           last_up_pct=viability.get("last_up_pct"),
                           repeated_up_pass_count=viability.get("repeated_up_pass_count"),
                           recent_up_repeatability=viability.get("recent_up_repeatability"),
                           peak_intervals=json.dumps(viability.get("last_three_peak_to_peak_sessions",[])),
                           trough_intervals=json.dumps(viability.get("last_three_trough_to_trough_sessions",[])),
                           peak_cycle_median=viability.get("peak_cycle_median_sessions"),
                           trough_cycle_median=viability.get("trough_cycle_median_sessions"),
                           cycle_timing_pass=viability.get("cycle_timing_pass"),
                           up_progression=viability.get("up_progression"),
                           historical_mean_swing_pct=viability.get("historical_mean_swing_pct"),
                           recent_capture_net_pct=viability.get("hypothetical_net_capture_pct"),
                           viability_json=json.dumps(viability,sort_keys=True),
                           combined_research_entry=(
                               "REVIEW" if health["proposed_entry"]=="REVIEW"
                               and viability["proposed_entry"]=="REVIEW"
                               and score["status"]=="CANDIDATE" else "NO_TRADE"))
    except (ValueError,KeyError,TypeError) as e:
        row.update(status="DATA_ERROR",error=str(e))
    results.append(row)
fields=["run","symbol","bars","raw_bars","regime_start","status","score","version","error",
        "swing_state","swing_entry","swing_reason","high_progression","low_progression",
        "recent_swing_pct","amplitude_ratio","swing_health_json",
        "viability_state","viability_entry","viability_reason","recent_three_swing_pct",
        "recent_two_up_pct","last_three_up_pct","last_up_pct",
        "repeated_up_pass_count","recent_up_repeatability","peak_intervals","trough_intervals",
        "peak_cycle_median","trough_cycle_median","cycle_timing_pass","up_progression","historical_mean_swing_pct","recent_capture_net_pct",
        "combined_research_entry","viability_json"]
with (OUT/"v23_research_universe.csv").open("w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=fields,extrasaction="ignore");w.writeheader();w.writerows(results)
ranked=sorted((r for r in results if isinstance(r["score"],(int,float))),key=lambda r:r["score"],reverse=True)
with (OUT/"v23_research_ranked.csv").open("w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=["rank","symbol","score","status","bars","version",
            "swing_state","swing_entry","swing_reason","high_progression","low_progression",
            "recent_swing_pct","amplitude_ratio","viability_state","viability_entry",
            "viability_reason","recent_three_swing_pct","recent_two_up_pct",
            "last_three_up_pct","last_up_pct","repeated_up_pass_count","recent_up_repeatability",
            "peak_intervals","trough_intervals","peak_cycle_median","trough_cycle_median","cycle_timing_pass","up_progression",
            "historical_mean_swing_pct","recent_capture_net_pct","combined_research_entry"],extrasaction="ignore")
    w.writeheader()
    for rank,r in enumerate(ranked,1):
        w.writerow({"rank":rank,**r})
viable=[r for r in ranked if r.get("combined_research_entry")=="REVIEW"]
with (OUT/"v23_research_recent_viability_shortlist.csv").open("w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=["research_rank","symbol","score","status",
         "swing_state","viability_state","recent_three_swing_pct","recent_two_up_pct",
         "last_three_up_pct","last_up_pct","repeated_up_pass_count","recent_up_repeatability",
         "peak_intervals","trough_intervals","peak_cycle_median","trough_cycle_median","cycle_timing_pass","up_progression",
         "historical_mean_swing_pct","recent_capture_net_pct",
         "combined_research_entry"],extrasaction="ignore")
    w.writeheader()
    for rank,r in enumerate(viable,1):
        w.writerow({"research_rank":rank,**r})
print("RECENT_VIABILITY_SHORTLIST",json.dumps([
    {"rank":i+1,"symbol":r["symbol"],"score":round(r["score"],3),
     "last_three_swing_pct":r.get("recent_three_swing_pct"),
     "last_three_up_pct":r.get("last_three_up_pct"),
     "repeated_up_pass_count":r.get("repeated_up_pass_count"),
     "recent_up_repeatability":r.get("recent_up_repeatability"),
     "peak_intervals":r.get("peak_intervals"),"trough_intervals":r.get("trough_intervals"),
     "cycle_timing_pass":r.get("cycle_timing_pass"),
     "last_up_pct":r.get("last_up_pct"),
     "state":r.get("viability_state")} for i,r in enumerate(viable[:25])]))
print("RECENT_VIABILITY_COUNTS",json.dumps({
    state:sum(r.get("viability_state")==state for r in ranked)
    for state in sorted({r.get("viability_state") for r in ranked})}))
print("TOP_RESEARCH_RANKINGS",json.dumps([{"rank":i+1,"symbol":r["symbol"],"score":round(r["score"],3),"status":r["status"],"bars":r["bars"],"swing_state":r.get("swing_state"),"swing_entry":r.get("swing_entry"),"viability":r.get("viability_state"),"combined_entry":r.get("combined_research_entry") } for i,r in enumerate(ranked[:25])]))
status={"universe":5502,"rows_written":len(results),"candidate_scores":sum(isinstance(r["score"],(int,float)) for r in results),"version":"v2.3-research","production_approved":False,"history_symbols":len(groups),"experimental_recent_viability_review":len(viable),
        "experimental_only":True}
(OUT/"status.json").write_text(json.dumps(status,indent=2)+"\n")
print(json.dumps(status))
if not status["candidate_scores"]: raise SystemExit("NO_RESEARCH_SCORES_FROM_AVAILABLE_HISTORY")
