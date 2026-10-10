"""Fresh OHLCV independent audit for OFTS research candidates.

Downloads its OWN current bars; rejects stale, incomplete or inconsistent dates.
No chart screenshot dependency. Never promotes quality to a trading BUY.
"""
import argparse,csv,json,math,pathlib,time
from datetime import datetime,timedelta,timezone
from statistics import median
from ofts.research.candidate_components import detect_turns
from ofts.research.recent_viability import recent_swing_viability
from ofts.research.swing_health import recent_swing_health
from ofts.research.opportunity_v06 import opportunity_partial,eligibility_status
from ofts.research.entry_diagnostic_v07 import entry_diagnostic
from ofts.research.v23_replacement import evaluate

def window_stats(bars, sessions):
    window=bars[-sessions:]
    if len(window)<sessions: return {"sessions":sessions,"status":"INSUFFICIENT"}
    closes=[float(r["close"]) for r in window]
    highs=[float(r["high"]) for r in window]
    lows=[float(r["low"]) for r in window]
    pivots=detect_turns(closes,3.0)
    ups=[100*(b[2]/a[2]-1) for a,b in zip(pivots,pivots[1:]) if a[1]=="L" and b[1]=="H"]
    peaks=[x[0] for x in pivots if x[1]=="H"]
    troughs=[x[0] for x in pivots if x[1]=="L"]
    return dict(sessions=sessions,status="MEASURED",
        high=round(max(highs),4),low=round(min(lows),4),
        high_low_range_pct=round(100*(max(highs)/min(lows)-1),3),
        return_pct=round(100*(closes[-1]/closes[0]-1),3),
        confirmed_up_legs=len(ups),recent_up_pct=[round(x,3) for x in ups[-5:]],
        up_median_pct=round(median(ups),3) if ups else None,
        completed_peak_intervals=len(peaks)-1,completed_trough_intervals=len(troughs)-1,
        latest_confirmed_pivot_age_sessions=(len(closes)-1-pivots[-1][0]) if pivots else None)

def audit_symbol(symbol, target, yf, calendar, expected):
    frame=yf.download(symbol,period="2y",interval="1d",auto_adjust=False,
                      actions=False,progress=False,threads=False,timeout=25,group_by="ticker")
    if frame is None or frame.empty: raise ValueError("EMPTY_PROVIDER")
    if getattr(frame.columns,"nlevels",1)>1: frame=frame[symbol]
    bars=[]
    for idx,r in frame.iterrows():
        dt=str(idx.date())
        if dt>target:continue
        vals={k.lower():float(r[k]) for k in ("Open","High","Low","Close")}
        if not all(math.isfinite(v) and v>0 for v in vals.values()):continue
        if not vals["low"]<=min(vals["open"],vals["close"])<=max(vals["open"],vals["close"])<=vals["high"]:continue
        bars.append(dict(date=dt,**vals,volume=float(r.get("Volume",0))))
    if not bars: raise ValueError("NO_VALID_BARS")
    latest=bars[-1]["date"]
    if latest!=target: raise ValueError(f"STALE_OR_MISSING_TARGET expected={target} got={latest}")
    if len(bars)<180:raise ValueError(f"INSUFFICIENT_HISTORY_{len(bars)}")
    closes=[r["close"] for r in bars]
    highs=[r["high"] for r in bars]
    lows=[r["low"] for r in bars]
    v23=evaluate(highs,lows,closes)
    if v23.get("candidate_score") is None:raise ValueError(f"NOT_SCOREABLE_{v23['status']}")
    viability=recent_swing_viability(closes,v23["threshold_pct"])
    health=recent_swing_health(closes,v23["threshold_pct"])
    opportunity=opportunity_partial(viability,health)
    entry=entry_diagnostic(closes,[r["date"] for r in bars])
    return dict(symbol=symbol,source="Yahoo Finance via yfinance; unadjusted OHLC",
        asof=latest,bars=len(bars),close=round(closes[-1],4),
        score_v23=round(v23["candidate_score"],4),quality_v06=opportunity.get("measured_score"),
        eligibility=eligibility_status(symbol,latest,closes[-1])["state"],
        swing_health=health["state"],viability=viability["state"],
        entry_state=entry["state"],entry_5d_pct=entry.get("return_5_sessions_pct"),
        entry_20d_pct=entry.get("return_20_sessions_pct"),
        w30=window_stats(bars,30),w60=window_stats(bars,60),
        w126=window_stats(bars,126),w252=window_stats(bars,252),
        verified_trade_candidate=False)

def main():
    import yfinance as yf
    import pandas_market_calendars as pmc
    ap=argparse.ArgumentParser()
    ap.add_argument("--research-file",default="ofts-output/v06_opportunity_research_ranked.csv")
    ap.add_argument("--output",default="ofts-output/fresh_oscillator_audit.json")
    args=ap.parse_args()
    with open(args.research_file,newline="") as f:
        research=list(csv.DictReader(f))
    # All active research names, plus prior known high-scoring false-positive controls.
    # Controls do not enter the production ranking just by being audited.
    controls="XPRO CLW CSPI PAHC HRI VSAT ATEX AVIR CAT WRD".split()
    names=list(dict.fromkeys([r["symbol"] for r in research]+controls))
    now=datetime.now(timezone.utc)
    calendar=pmc.get_calendar("NYSE")
    schedule=calendar.schedule(start_date=(now-timedelta(days=20)).date(),end_date=now.date())
    completed=schedule[schedule.market_close<=now-timedelta(minutes=30)]
    target=str(completed.index[-1].date())
    results=[]
    for symbol in names:
        last_error=""
        for attempt in range(2):
            try:
                record=audit_symbol(symbol,target,yf,calendar,None)
                results.append(record)
                print("FRESH_AUDIT",symbol,target,record["close"],record["entry_state"],flush=True)
                break
            except Exception as e:
                last_error=f"{type(e).__name__}: {e}"
        else:
            results.append(dict(symbol=symbol,status="DATA_ERROR",error=last_error,verified_trade_candidate=False))
            print("FRESH_AUDIT_ERROR",symbol,last_error,flush=True)
    out=dict(version="v0.8-fresh-independent-audit",target_session=target,
             research_symbols=[r["symbol"] for r in research],
             controls=controls,source="yfinance, independent fresh provider requests",
             data_errors=sum("error" in r for r in results),
             records=results,production_approved=False,
             note="Current data plus independent 30/60/126/252-day chart-shape audits; no trading BUY")
    pathlib.Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    pathlib.Path(args.output).write_text(json.dumps(out,indent=2)+"\n")
    with open(pathlib.Path(args.output).with_suffix(".csv"),"w",newline="") as f:
        keys=["symbol","asof","close","score_v23","quality_v06","eligibility","swing_health",
              "viability","entry_state","entry_5d_pct","entry_20d_pct","status","error",
              "w30_high","w30_low","w30_swing_pct","w30_up_legs","w60_high","w60_low",
              "w60_swing_pct","w60_up_legs","w126_high","w126_low","w126_swing_pct",
              "w126_up_legs","w252_high","w252_low","w252_swing_pct","w252_up_legs"]
        w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
        for record in results:
            row={k:v for k,v in record.items() if k in keys}
            for n in (30,60,126,252):
                win=record.get(f"w{n}",{})
                row.update({f"w{n}_high":win.get("high"),f"w{n}_low":win.get("low"),
                            f"w{n}_swing_pct":win.get("high_low_range_pct"),
                            f"w{n}_up_legs":win.get("confirmed_up_legs")})
            w.writerow(row)
    print("FRESH_AUDIT_SUMMARY",json.dumps({"target":target,"total":len(names),
        "fresh":len(names)-out["data_errors"],"errors":out["data_errors"]}),flush=True)
    # Never silently pass a missing data feed.
    if out["data_errors"]:raise SystemExit("FRESH_AUDIT_INCOMPLETE")
if __name__=="__main__":main()
