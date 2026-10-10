#!/usr/bin/env python3
"""OFTS v2.3 reproducible research worker. Never represents v2.2 or live BUY signals."""
import csv,json,pathlib,sys
from collections import defaultdict
from ofts.research.v23_replacement import evaluate
from ofts.research.security_regimes import post_identity_bars
from ofts.research.swing_health import recent_swing_health
from ofts.research.recent_viability import recent_swing_viability
from ofts.research.opportunity_v06 import opportunity_partial, eligibility_status, VERSION as OPPORTUNITY_VERSION
from ofts.research.entry_diagnostic_v07 import entry_diagnostic, VERSION as ENTRY_VERSION
from ofts.research.three_clear_cycles_v09 import three_clear_cycles, VERSION as CLEAR_VERSION
from ofts.research.clear_cycle_rank_v10 import score_clear_cycles, VERSION as RANK_VERSION
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
                clear=three_clear_cycles(series[2])
                row.update(clear_v09_state=clear['state'],clear_v09_reason=clear['reason'],
                           clear_v09_cycles=clear.get('completed_cycles'),
                           clear_v09_worst_efficiency=clear.get('worst_leg_path_efficiency'),
                           clear_v09_median_efficiency=clear.get('median_leg_path_efficiency'),
                           clear_v09_json=json.dumps(clear,sort_keys=True))
                viability=recent_swing_viability(series[2],score["threshold_pct"])
                opportunity=opportunity_partial(viability,health)
                entry=entry_diagnostic(series[2],[b.get('date','') for b in data])
                row.update(entry_v07_state=entry['state'],entry_v07_asof=entry.get('asof_date'),
                           entry_v07_close=entry.get('close'),entry_v07_return5=entry.get('return_5_sessions_pct'),
                           entry_v07_position=entry.get('position_in_prior20_band'),
                           entry_v07_json=json.dumps(entry,sort_keys=True))
                eligible=eligibility_status(sym,data[-1].get('date',''),series[2][-1])
                new_rank=score_clear_cycles(clear,eligible['state'])
                row.update(clear_v10_score=new_rank['score'],clear_v10_json=json.dumps(new_rank,sort_keys=True))
                opportunity['eligibility_status']=eligible['state']
                opportunity['eligibility_evidence']=eligible
                row.update(opportunity_v06_score=opportunity.get("measured_score"),
                           opportunity_v06_status=opportunity["status"],
                           opportunity_v06_eligibility=opportunity.get("eligibility_status","PENDING_ELIGIBILITY"),
                           opportunity_v06_json=json.dumps(opportunity,sort_keys=True))
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
                           prior_three_up_pct=json.dumps(viability.get("preceding_three_up_pct",[])),
                           prior_peak_intervals=json.dumps(viability.get("preceding_three_peak_to_peak_sessions",[])),
                           prior_trough_intervals=json.dumps(viability.get("preceding_three_trough_to_trough_sessions",[])),
                           up_amplitude_ratio=viability.get("recent_vs_prior_up_ratio"),
                           cadence_ratio=viability.get("recent_vs_prior_cadence_ratio"),
                           recent_vs_prior_state=viability.get("recent_vs_prior_state"),
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
        "peak_cycle_median","trough_cycle_median","cycle_timing_pass",
        "prior_three_up_pct","prior_peak_intervals","prior_trough_intervals",
        "up_amplitude_ratio","cadence_ratio","recent_vs_prior_state","up_progression","historical_mean_swing_pct","recent_capture_net_pct",
        "combined_research_entry","viability_json",
        "opportunity_v06_score","opportunity_v06_status","opportunity_v06_eligibility","opportunity_v06_json",
        "entry_v07_state","entry_v07_asof","entry_v07_close","entry_v07_return5","entry_v07_position","entry_v07_json",
        "clear_v09_state","clear_v09_reason","clear_v09_cycles","clear_v09_worst_efficiency","clear_v09_median_efficiency","clear_v09_json","clear_v10_score","clear_v10_json"]
with (OUT/"v23_research_universe.csv").open("w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=fields,extrasaction="ignore");w.writeheader();w.writerows(results)
ranked=sorted((r for r in results if isinstance(r["score"],(int,float))),key=lambda r:r["score"],reverse=True)
with (OUT/"v23_research_ranked.csv").open("w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=["rank","symbol","score","status","bars","version",
            "swing_state","swing_entry","swing_reason","high_progression","low_progression",
            "recent_swing_pct","amplitude_ratio","viability_state","viability_entry",
            "viability_reason","recent_three_swing_pct","recent_two_up_pct",
            "last_three_up_pct","last_up_pct","repeated_up_pass_count","recent_up_repeatability",
            "peak_intervals","trough_intervals","peak_cycle_median","trough_cycle_median","cycle_timing_pass",
            "prior_three_up_pct","prior_peak_intervals","prior_trough_intervals",
            "up_amplitude_ratio","cadence_ratio","recent_vs_prior_state","up_progression",
            "historical_mean_swing_pct","recent_capture_net_pct","combined_research_entry",
            "opportunity_v06_score","opportunity_v06_status","opportunity_v06_eligibility",
            "entry_v07_state","entry_v07_asof","entry_v07_close","entry_v07_return5","entry_v07_position"],extrasaction="ignore")
    w.writeheader()
    for rank,r in enumerate(ranked,1):
        w.writerow({"rank":rank,**r})
viable=[r for r in ranked if r.get("combined_research_entry")=="REVIEW"]
with (OUT/"v23_research_recent_viability_shortlist.csv").open("w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=["research_rank","symbol","score","status",
         "swing_state","viability_state","recent_three_swing_pct","recent_two_up_pct",
         "last_three_up_pct","last_up_pct","repeated_up_pass_count","recent_up_repeatability",
         "peak_intervals","trough_intervals","peak_cycle_median","trough_cycle_median","cycle_timing_pass","prior_three_up_pct","prior_peak_intervals","prior_trough_intervals",
             "up_amplitude_ratio","cadence_ratio","recent_vs_prior_state","up_progression",
         "historical_mean_swing_pct","recent_capture_net_pct",
         "combined_research_entry"],extrasaction="ignore")
    w.writeheader()
    for rank,r in enumerate(viable,1):
        w.writerow({"research_rank":rank,**r})
# Experimental v0.6 opportunity ranking is the primary research review order.
# Original v2.3 score and frozen cohorts remain unchanged for benchmarking.
opportunity_ranked=sorted(
    (r for r in viable if isinstance(r.get("opportunity_v06_score"),(int,float))
     and r.get("opportunity_v06_eligibility")!="INELIGIBLE"),
    key=lambda r:(-r["opportunity_v06_score"],r["symbol"]))
opportunity_fields=["opportunity_rank","symbol","opportunity_v06_score",
    "opportunity_v06_status","opportunity_v06_eligibility","score","status",
    "swing_state","viability_state","last_three_up_pct","peak_intervals",
    "trough_intervals","up_amplitude_ratio","cadence_ratio",
    "combined_research_entry","opportunity_v06_json",
    "entry_v07_state","entry_v07_asof","entry_v07_close","entry_v07_return5","entry_v07_position","entry_v07_json"]
with (OUT/"v06_opportunity_research_ranked.csv").open("w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=opportunity_fields,extrasaction="ignore")
    w.writeheader()
    for rank,r in enumerate(opportunity_ranked,1):
        w.writerow({"opportunity_rank":rank,**r})
# v0.9b independent FULL-UNIVERSE three-cycle audit. This does NOT inherit the
# old 16-stock shortlist. All 5,502 symbols are considered, with all 3,977
# scoreable symbols independently checked. Frozen benchmark outputs untouched.
clear_states=defaultdict(int)
for row in results:
    clear_states[row.get('clear_v09_state') or row['status']]+=1
clear_pass=sorted((row for row in results
    if row.get('clear_v09_state')=='THREE_CLEAR_CYCLES'),
    key=lambda row:(-float(row['clear_v10_score']) if isinstance(row.get('clear_v10_score'),(int,float)) else 9999,row['symbol']))
clear_fields=['symbol','bars','status','score','opportunity_v06_score',
    'opportunity_v06_eligibility','viability_state','swing_state',
    'entry_v07_state','entry_v07_asof','entry_v07_close',
    'clear_v09_state','clear_v09_reason','clear_v09_cycles',
    'clear_v09_worst_efficiency','clear_v09_median_efficiency','clear_v09_json',
    'clear_v10_score','clear_v10_json']
with (OUT/'v09_full_universe_cycle_audit.csv').open('w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=clear_fields,extrasaction='ignore')
    w.writeheader();w.writerows(results)
with (OUT/'v09_full_universe_clear_cycle_pass.csv').open('w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=['research_rank']+clear_fields,extrasaction='ignore')
    w.writeheader()
    for i,row in enumerate(clear_pass,1):
        w.writerow({'research_rank':i,**row})
# v0.10 research keepers are determined by NEW clear-cycle evidence only.
# Legacy viability and swing-health labels remain visible BENCHMARKS, not
# disqualifying gates. Independently confirmed security ineligibility remains a veto.
# This is a RESEARCH list, never a verified BUY or entry signal.
keepers=[row for row in clear_pass
    if row.get('opportunity_v06_eligibility')!='INELIGIBLE']
with (OUT/'v09_full_universe_keepers.csv').open('w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=['research_rank']+clear_fields,extrasaction='ignore')
    w.writeheader()
    for i,row in enumerate(keepers,1):
        w.writerow({'research_rank':i,**row})
report={'version':CLEAR_VERSION,'ranking_version':RANK_VERSION,'universe':len(results),
    'scoreable':sum(isinstance(x.get('score'),(int,float)) for x in results),
    'history_latest_dates':sorted({groups[x['symbol']][-1].get('date','') for x in results if groups.get(x['symbol'])})[-5:],
    'clear_states':dict(sorted(clear_states.items())),
    'three_clear_pass':len(clear_pass),'keepers':len(keepers),
    'legacy_filters_applied_to_keeper_rank':False,
    'keeper_symbols':[x['symbol'] for x in keepers],
    'keepers_top50':[{'rank':i+1,'symbol':x['symbol'],
        'new_score_out_of_100':x['clear_v10_score'],
        'eligibility':x.get('opportunity_v06_eligibility'),
        'legacy_viability_benchmark':x.get('viability_state'),
        'legacy_swing_benchmark':x.get('swing_state')}
        for i,x in enumerate(keepers[:50])],
    'clear_pass_top50':[{'rank':i+1,'symbol':x['symbol'],
        'new_clean_cycle_score_out_of_100':x.get('clear_v10_score'),
        'new_components':json.loads(x['clear_v10_json'])['components'],
        'opportunity_score_out_of_80':x.get('opportunity_v06_score'),
        'old_v23_score':x.get('score'),
        'viability':x.get('viability_state'),
        'swing_health':x.get('swing_state'),
        'entry':x.get('entry_v07_state'),
        'eligibility':x.get('opportunity_v06_eligibility'),
        'cycles':json.loads(x['clear_v09_json'])['cycles'],
        'median_efficiency':x.get('clear_v09_median_efficiency')}
        for i,x in enumerate(clear_pass[:50])],
    'production_approved':False,
    'caution':'Cached historical research bars; not verified current prices or BUY signals'}
(OUT/'v09_full_universe_report.json').write_text(json.dumps(report,indent=2)+'\n')
print('V09_FULL_UNIVERSE_AUDIT',json.dumps({'scoreable':report['scoreable'],
    'states':report['clear_states'],'pass':len(clear_pass),'keepers':len(keepers),
    'keeper_symbols':report['keeper_symbols'],
    'top20':report['clear_pass_top50'][:20]}),flush=True)
print("V06_OPPORTUNITY_RESEARCH_TOP",json.dumps([
    {"rank":i+1,"symbol":r["symbol"],"score_out_of_80":r["opportunity_v06_score"],
     "old_v23_score":round(r["score"],3),"eligibility":r["opportunity_v06_eligibility"]}
    for i,r in enumerate(opportunity_ranked[:25])]))
# The current actionable shortlist is deliberately empty until every required gate
# is verified on fresh dated data; stale research names remain audit-visible.
current_ready=[r for r in opportunity_ranked
    if r.get("entry_v07_state")=="REVERSAL_REVIEW"
    and r.get("opportunity_v06_eligibility")=="PASS"
    and r.get("opportunity_v06_status")=="COMPLETE"]
with (OUT/"v07_current_verified_trading_candidates.csv").open("w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=["rank","symbol","opportunity_v06_score",
        "opportunity_v06_eligibility","entry_v07_state","entry_v07_asof",
        "entry_v07_close","entry_v07_return5"],extrasaction="ignore")
    w.writeheader()
    for i,r in enumerate(current_ready,1): w.writerow({"rank":i,**r})
print("V07_CURRENT_VERIFIED_TRADING_CANDIDATES",len(current_ready))
print("V07_ENTRY_DIAGNOSTIC",json.dumps([{"symbol":r["symbol"],"entry_state":r.get("entry_v07_state"),"asof":r.get("entry_v07_asof"),"close":r.get("entry_v07_close"),"five_day_pct":r.get("entry_v07_return5")} for r in opportunity_ranked[:25]]))
print("V06_VERIFIED_ELIGIBLE",0,"market_cap_and_liquidity_data_not_present_in_OHLCV")
print("V06_EXCLUDED_INELIGIBLE",json.dumps([{"symbol":r["symbol"],"reason":json.loads(r["opportunity_v06_json"]).get("eligibility_evidence",{}).get("reason")} for r in viable if r.get("opportunity_v06_eligibility")=="INELIGIBLE"]))
print("RECENT_VIABILITY_SHORTLIST",json.dumps([
    {"rank":i+1,"symbol":r["symbol"],"score":round(r["score"],3),
     "last_three_swing_pct":r.get("recent_three_swing_pct"),
     "last_three_up_pct":r.get("last_three_up_pct"),
     "repeated_up_pass_count":r.get("repeated_up_pass_count"),
     "recent_up_repeatability":r.get("recent_up_repeatability"),
     "peak_intervals":r.get("peak_intervals"),"trough_intervals":r.get("trough_intervals"),
     "cycle_timing_pass":r.get("cycle_timing_pass"),
     "prior_three_up_pct":r.get("prior_three_up_pct"),
     "prior_peak_intervals":r.get("prior_peak_intervals"),
     "prior_trough_intervals":r.get("prior_trough_intervals"),
     "up_amplitude_ratio":r.get("up_amplitude_ratio"),
     "cadence_ratio":r.get("cadence_ratio"),
     "recent_vs_prior_state":r.get("recent_vs_prior_state"),
     "last_up_pct":r.get("last_up_pct"),
     "state":r.get("viability_state")} for i,r in enumerate(viable[:25])]))
print("RECENT_VIABILITY_COUNTS",json.dumps({
    state:sum(r.get("viability_state")==state for r in ranked)
    for state in sorted({r.get("viability_state") for r in ranked})}))
print("TOP_RESEARCH_RANKINGS",json.dumps([{"rank":i+1,"symbol":r["symbol"],"score":round(r["score"],3),"status":r["status"],"bars":r["bars"],"swing_state":r.get("swing_state"),"swing_entry":r.get("swing_entry"),"viability":r.get("viability_state"),"combined_entry":r.get("combined_research_entry") } for i,r in enumerate(ranked[:25])]))
status={"universe":5502,"rows_written":len(results),"candidate_scores":sum(isinstance(r["score"],(int,float)) for r in results),"version":"v2.3-research","production_approved":False,"history_symbols":len(groups),"experimental_recent_viability_review":len(viable),
        "experimental_only":True,"v06_opportunity_research_ranked":len(opportunity_ranked),
        "v06_verified_eligible":0,"v06_version":OPPORTUNITY_VERSION,"v07_entry_version":ENTRY_VERSION,
        "v07_entry_current_confirmed":sum(r.get("entry_v07_state")=="REVERSAL_REVIEW" for r in opportunity_ranked)}
(OUT/"status.json").write_text(json.dumps(status,indent=2)+"\n")
print(json.dumps(status))
if not status["candidate_scores"]: raise SystemExit("NO_RESEARCH_SCORES_FROM_AVAILABLE_HISTORY")
