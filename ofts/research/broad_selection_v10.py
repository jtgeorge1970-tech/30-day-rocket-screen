"""Broad OFTS v1.0 test selection from entire locked 5,502-symbol universe.

The cached OHLCV is ONLY a discovery prefilter, never a current buy signal.
Fresh audit re-downloads each candidate independently before any rank.
"""
import csv,json,pathlib,statistics
from collections import defaultdict,Counter
from ofts.research.three_clear_cycles_v09 import three_clear_cycles
from ofts.research.security_regimes import post_identity_bars

ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=ROOT/"ofts-output"
BASELINE="XPRO CLW CSPI PAHC HRI VSAT ATEX AVIR CAT WRD CTOS INTS BXC HYLN EVI PATH".split()
CAP=160

def build():
    with (ROOT/"ofts/universe.csv").open(newline="",encoding="utf-8-sig") as f:
        universe=[(r.get("Symbol") or r.get("symbol") or r.get("Ticker") or "").strip().upper() for r in csv.DictReader(f)]
    if len(universe)!=5502 or len(set(universe))!=5502:raise RuntimeError("UNIVERSE_NOT_5502_UNIQUE")
    groups=defaultdict(list)
    with (OUT/"universe_ohlcv.csv").open(newline="",encoding="utf-8-sig") as f:
        for bar in csv.DictReader(f):
            sym=(bar.get("symbol") or bar.get("Symbol") or "").strip().upper()
            if sym:groups[sym].append(bar)
    measured=[]; states=Counter(); failures=Counter()
    for sym in universe:
        try:
            data=sorted(groups.get(sym,[]),key=lambda r:r.get("date",""))
            data,regime=post_identity_bars(sym,data)
            if len(data)<180:
                states["INSUFFICIENT_HISTORY"]+=1
                continue
            closes=[float(r["close"]) for r in data]
            audit=three_clear_cycles(closes)
            state=audit["state"]
            states[state]+=1
            cycles=audit["cycles"]
            if len(cycles)<3:continue
            rise=[x["rise_pct"] for x in cycles]
            efficiencies=[x["rise_path_efficiency"] for x in cycles]+[x["fall_path_efficiency"] for x in cycles]
            measured.append(dict(symbol=sym,discovery_state=state,
                                 discovery_asof=data[-1].get("date",""),
                                 discovery_last3_up_pct=json.dumps(rise),
                                 discovery_last3_down_pct=json.dumps([x["fall_pct"] for x in cycles]),
                                 discovery_median_path_efficiency=round(statistics.median(efficiencies),4),
                                 discovery_worst_path_efficiency=min(efficiencies),
                                 discovery_median_up_pct=round(statistics.median(rise),3),
                                 discovery_age=audit.get("last_completed_trough_age_sessions"),
                                 discovery_max_drawdown_pct=audit.get("max_drawdown_pct"),
                                 discovery_worst_daily_pct=audit.get("worst_daily_return_pct")))
        except (ValueError,KeyError,TypeError,IndexError) as e:
            failures[type(e).__name__]+=1
    # Full population is screened without using legacy scores. Top clean candidates
    # and near misses both tested; near misses reveal false negatives and overfitting.
    passing=sorted((x for x in measured if x["discovery_state"]=="THREE_CLEAR_CYCLES"),
                   key=lambda x:(-x["discovery_median_path_efficiency"],-x["discovery_worst_path_efficiency"],-x["discovery_median_up_pct"],x["symbol"]))
    near=sorted((x for x in measured if x["discovery_state"]!="THREE_CLEAR_CYCLES"),
                key=lambda x:(-x["discovery_median_path_efficiency"],-x["discovery_worst_path_efficiency"],-x["discovery_median_up_pct"],x["symbol"]))
    selected=[];seen=set()
    def add(row,group):
        if row["symbol"] not in seen:
            seen.add(row["symbol"]);selected.append(dict(row,selection_group=group))
    for row in passing[:100]:add(row,"NEW_CLEAR_CYCLES")
    for row in near[:60]:add(row,"NEAR_MISS_CONTROL")
    for sym in BASELINE:
        row=next((x for x in measured if x["symbol"]==sym),None)
        add(row or dict(symbol=sym,discovery_state="UNMEASURED"),"OLD16_CONTROL")
    if len(selected)<CAP:
        for row in passing[100:]+near[60:]:
            if len(selected)>=CAP:break
            add(row,"FILLER_DIVERSE")
    OUT.mkdir(parents=True,exist_ok=True)
    with (OUT/"broad_v10_selection.csv").open("w",newline="") as f:
        fields=["symbol","selection_group","discovery_state","discovery_asof",
                "discovery_last3_up_pct","discovery_last3_down_pct",
                "discovery_median_path_efficiency","discovery_worst_path_efficiency",
                "discovery_median_up_pct","discovery_age","discovery_max_drawdown_pct","discovery_worst_daily_pct"]
        w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore");w.writeheader();w.writerows(selected)
    summary=dict(universe=5502,history_symbols=len(groups),scoreable_cycle_evaluations=sum(states.values()),
                 state_counts=dict(states),exceptions=dict(failures),clean_historical=len(passing),
                 near_miss_historical=len(near),fresh_refresh_requested=len(selected),
                 groups=dict(Counter(x["selection_group"] for x in selected)),
                 note="Historical prefilter only. No score/BUY from cached bars. Fresh provider re-audit mandatory.")
    (OUT/"broad_v10_selection_summary.json").write_text(json.dumps(summary,indent=2)+"\n")
    print("BROAD_V10_DISCOVERY",json.dumps(summary),flush=True)
    print("BROAD_V10_HISTORICAL_TOP",json.dumps(selected[:30]),flush=True)
    if len(selected)<100:raise RuntimeError("INSUFFICIENT_BROAD_TEST_POPULATION")
if __name__=="__main__":build()
