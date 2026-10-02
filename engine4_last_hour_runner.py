from __future__ import annotations

import argparse, json, math
from datetime import datetime, time
from pathlib import Path
import numpy as np
import pandas as pd

import engine4_pipeline as core
import engine4_pipeline_runner as runner
from engine4_config import (
    BROAD_POOL_SIZE, DEEP_POOL_SIZE, MAX_SPREAD_PCT, MAX_TRADABLE_PRICE,
    MIN_ATR_PCT, MIN_PREMARKET_RVOL, MIN_SCORE, SECTOR_ETF
)
from engine4_data import download_intraday, download_daily_metrics, slice_window
from engine4_score import preliminary_activity_score, score_candidate, premarket_grade

OUT = Path("output/engine4_last_hour")
OUT.mkdir(parents=True, exist_ok=True)
WINDOW_START = "15:00"
WINDOW_END = "16:00"
BENCH_CAP = 25

def finite(x, default=math.nan):
    try:
        v=float(x)
        return v if math.isfinite(v) else default
    except Exception:
        return default

def recs(df):
    out=[]
    for r in df.to_dict("records"):
        z={}
        for k,v in r.items():
            if isinstance(v,(np.integer,)): v=int(v)
            if isinstance(v,(np.floating,)): v=float(v)
            if isinstance(v,float) and not math.isfinite(v): v=None
            z[k]=v
        out.append(z)
    return out

def ref(date_et):
    return datetime.combine(date_et, time(16,0), tzinfo=core.ET)

def window_metrics(frame, date_et):
    w=slice_window(frame,date_et,WINDOW_START,WINDOW_END)
    if w.empty or "Close" not in w or "Volume" not in w: return None
    c=pd.to_numeric(w["Close"],errors="coerce").dropna()
    v=pd.to_numeric(w["Volume"],errors="coerce").fillna(0)
    if len(c)<2: return None
    first=float(c.iloc[0]); last=float(c.iloc[-1]); vol=float(v.sum())
    if first<=0 or last<=0: return None
    return {"first":first,"last":last,"volume":vol,"return_pct":(last/first-1)*100,
            "dollar_volume":vol*last,"bars":int(len(c)),
            "last_timestamp":str(pd.Timestamp(c.index[-1]))}

def historical_last_hour_rvol(frame,date_et,current_volume):
    vols=[]
    for d in sorted(set(frame.index.date)):
        if d>=date_et: continue
        m=window_metrics(frame,d)
        if m and m["volume"]>0: vols.append(m["volume"])
    if not vols: return math.nan
    base=float(np.median(vols[-5:]))
    return current_volume/base if base>0 else math.nan

def stage1(date_s):
    runner.install_repairs()
    date_et=pd.Timestamp(date_s).date()
    base=core.eligible_baseline().copy()
    symbols=base.ticker.astype(str).tolist()
    frames=download_intraday(symbols,period="1d",interval="1m",prepost=False,date_et=date_et,lookback_days=0)
    idx=base.set_index("ticker")
    rows=[]
    for s in symbols:
        m=window_metrics(frames.get(s,pd.DataFrame()),date_et)
        if not m: continue
        adv_dollar=finite(idx.at[s,"dollar_volume"],0)
        adv_shares=adv_dollar/m["last"] if m["last"]>0 else math.nan
        intensity=m["volume"]/adv_shares*100 if adv_shares>0 else math.nan
        strict=bool(0.50<=m["return_pct"]<=25.0 and m["dollar_volume"]>=500000)
        rows.append({"ticker":s,"name":str(idx.at[s,"name"]),"sector":str(idx.at[s,"sector"]),
          "market_cap":finite(idx.at[s,"market_cap"]),"avg_daily_dollar_volume":adv_dollar,
          "last_hour_start":m["first"],"last_hour_close":m["last"],"last_premarket":m["last"],
          "last_hour_return_pct":m["return_pct"],"gap_pct":m["return_pct"],
          "last_hour_volume":m["volume"],"premarket_volume":m["volume"],
          "last_hour_dollar_volume":m["dollar_volume"],"premarket_dollar_volume":m["dollar_volume"],
          "last_hour_volume_intensity_pct":intensity,"premarket_volume_intensity_pct":intensity,
          "strict_activity_pass":strict,"activity_score":preliminary_activity_score(m["return_pct"],max(m["dollar_volume"],1),max(adv_dollar,1)),
          "selection_bar_timestamp":m["last_timestamp"],"snapshot_mode":"LAST_HOUR_1500_1600_ET"})
    all_df=pd.DataFrame(rows)
    if all_df.empty: raise RuntimeError("No trustworthy last-hour observations")
    retained=all_df.sort_values(["strict_activity_pass","premarket_volume_intensity_pct","activity_score","last_hour_dollar_volume","last_hour_return_pct"],ascending=False,na_position="last").head(BROAD_POOL_SIZE).reset_index(drop=True)
    retained.to_csv(OUT/"stage1_retained.csv",index=False)
    meta={"target_date_et":date_s,"window":"15:00-16:00 ET","baseline_eligible":len(base),
      "trustworthy_last_hour_observations":len(all_df),"strict_activity_count":int(all_df.strict_activity_pass.sum()),
      "retained_by_top100_cap":len(retained),"symbols":retained.ticker.tolist()}
    (OUT/"stage1_report.json").write_text(json.dumps(meta,indent=2))
    print(json.dumps(meta,indent=2))

def score_pool(seed,date_s):
    date_et=pd.Timestamp(date_s).date(); reference=ref(date_et)
    seed=seed.head(DEEP_POOL_SIZE).copy(); syms=seed.ticker.astype(str).tolist()
    hist=download_intraday(syms,period="7d",interval="1m",prepost=False,date_et=date_et,lookback_days=7)
    daily=download_daily_metrics(syms,asof_date=date_et)
    bench_syms=["SPY","QQQ"]+sorted({SECTOR_ETF[s] for s in seed.sector if s in SECTOR_ETF})
    bench=download_intraday(bench_syms,period="1d",interval="1m",prepost=False,date_et=date_et,lookback_days=0)
    rets={}
    for s,f in bench.items():
        m=window_metrics(f,date_et)
        if m: rets[s]=m["return_pct"]
    market=np.nanmean([rets.get("SPY",np.nan),rets.get("QQQ",np.nan)])
    if not math.isfinite(market): market=0.0
    rows=[]
    for row in seed.to_dict("records"):
        s=row["ticker"]; h=hist.get(s)
        if h is None or h.empty: continue
        rvol=historical_last_hour_rvol(h,date_et,finite(row.get("last_hour_volume"),0))
        intensity=finite(row.get("last_hour_volume_intensity_pct"))
        volume_gate=(math.isfinite(rvol) and rvol>=MIN_PREMARKET_RVOL) or (math.isfinite(intensity) and intensity>=2.0)
        dm=daily.get(s,{})
        atr=finite(dm.get("atr")); px=finite(row.get("last_hour_close"))
        atr_pct=atr/px*100 if atr>0 and px>0 else math.nan
        levels=[finite(dm.get(k)) for k in ("high_5","high_20","high_60")]
        overhead=[x for x in levels if math.isfinite(x) and x>px]
        resistance=min(overhead) if overhead else math.nan
        room=(resistance/px-1)*100 if math.isfinite(resistance) else 10.0
        sector_ret=rets.get(SECTOR_ETF.get(row.get("sector")),market)
        cat,headline,age,cat_source=runner.provider_catalyst_with_source(s,reference,row.get("name"))
        bid,ask,spread,spread_source=runner.quote_spread_with_source(s)
        auth=spread_source in {"Nasdaq quote","Yahoo quote fallback"}
        row.update({"premarket_rvol":rvol,"premarket_volume_metric_source":"historical_last_hour_rvol" if math.isfinite(rvol) else "last_hour_volume_pct_adv",
          "premarket_volume_gate_pass":bool(volume_gate),"atr_pct":atr_pct,"resistance_price":resistance,
          "resistance_room_pct":room,"market_relative_strength_pct":finite(row.get("last_hour_return_pct"),0)-market,
          "sector_relative_strength_pct":finite(row.get("last_hour_return_pct"),0)-sector_ret,
          "catalyst_quality":cat,"catalyst_headline":headline,"catalyst_age_hours":age,"catalyst_source":cat_source,
          "bid":bid,"ask":ask,"spread_pct":spread,"spread_source":spread_source,"spread_order_authoritative":auth})
        score,comp=score_candidate(row); row["score"]=score
        for k,v in comp.items(): row["pts_"+k]=v
        evidence={"catalyst":cat>0,"last_hour_volume_strength":bool(volume_gate),"atr":math.isfinite(atr_pct) and atr_pct>=MIN_ATR_PCT,
          "room":room>0,"spread":math.isfinite(spread) and spread<=MAX_SPREAD_PCT and auth,
          "price_cap":math.isfinite(px) and px<=MAX_TRADABLE_PRICE}
        mandatory=all(evidence.values()); gates={**evidence,"score80":score>=MIN_SCORE}
        row["premarket_eligible"]=bool(mandatory and score>=MIN_SCORE)
        row["premarket_grade"]=premarket_grade(score,mandatory)
        row["premarket_gate_count"]=sum(gates.values())
        row["premarket_failures"]=",".join(k for k,v in gates.items() if not v)
        rows.append(row)
    df=pd.DataFrame(rows)
    if df.empty: return df
    return df.sort_values(["premarket_eligible","score","premarket_gate_count","last_hour_volume_intensity_pct","last_hour_dollar_volume"],ascending=False,na_position="last").reset_index(drop=True)

def stage2(date_s):
    seed=pd.read_csv(OUT/"stage1_retained.csv")
    ranked=score_pool(seed,date_s)
    ranked.to_csv(OUT/"stage2_ranked.csv",index=False)
    elig=ranked[ranked.premarket_eligible==True] if not ranked.empty else ranked
    meta={"target_date_et":date_s,"selected_for_deep_analysis":min(DEEP_POOL_SIZE,len(seed)),"actually_analyzed":len(ranked),
      "score_ge_80":int((ranked.score>=80).sum()) if not ranked.empty else 0,"launchpad_eligible":len(elig),
      "eligible_symbols":[{"ticker":r["ticker"],"score":r["score"],"grade":r["premarket_grade"],"failures":r["premarket_failures"]} for r in recs(elig)]}
    (OUT/"stage2_report.json").write_text(json.dumps(meta,indent=2)); print(json.dumps(meta,indent=2))

def stage3(date_s):
    seed=pd.read_csv(OUT/"stage1_retained.csv")
    ranked=score_pool(seed,date_s); ranked.to_csv(OUT/"stage3_ranked.csv",index=False)
    elig=ranked[ranked.premarket_eligible==True].head(25).copy() if not ranked.empty else ranked
    if not elig.empty:
        elig.insert(0,"rank",range(1,len(elig)+1))
    elig.to_csv(OUT/"top25_frozen.csv",index=False)
    payload={"target_date_et":date_s,"window":"15:00-16:00 ET","actual_count":len(elig),"candidates":recs(elig)}
    (OUT/"top25_frozen.json").write_text(json.dumps(payload,indent=2))
    print(json.dumps({"target_date_et":date_s,"score_ge_80":int((ranked.score>=80).sum()) if not ranked.empty else 0,
      "launchpad_eligible":len(elig),"frozen_finalists":[{"ticker":r["ticker"],"score":r["score"],"grade":r["premarket_grade"]} for r in recs(elig)]},indent=2))

def bench(date_s):
    frozen=pd.read_csv(OUT/"top25_frozen.csv") if (OUT/"top25_frozen.csv").stat().st_size>1 else pd.DataFrame()
    prior_path=Path("state/engine4/watch_bench.json")
    prior=json.loads(prior_path.read_text()) if prior_path.exists() else {"candidates":[]}
    prior_syms=[str(x.get("ticker")) for x in prior.get("candidates",[]) if x.get("ticker")]
    frozen_syms=frozen.ticker.astype(str).tolist() if not frozen.empty and "ticker" in frozen else []
    union=list(dict.fromkeys(frozen_syms+prior_syms))
    source=pd.read_csv(OUT/"stage3_ranked.csv")
    known=source[source.ticker.astype(str).isin(union)].copy() if union else pd.DataFrame()
    qualified=known[(known.premarket_eligible==True)&(known.score>=80)].copy() if not known.empty else known
    qualified=qualified.sort_values("score",ascending=False).head(BENCH_CAP)
    if not qualified.empty:
        qualified["bench_rank"]=range(1,len(qualified)+1)
        qualified["tier"]=qualified.bench_rank.map(lambda x:"HOT" if x<=5 else ("DEVELOPING" if x<=15 else "RESERVE"))
    qualified.to_csv(OUT/"watch_bench.csv",index=False)
    meta={"target_date_et":date_s,"competition_universe_count":len(union),"freshly_scored_count":len(known),
      "retained_by_top25_bench_cap":len(qualified),"hot_count":int((qualified.tier=="HOT").sum()) if not qualified.empty else 0,
      "developing_count":int((qualified.tier=="DEVELOPING").sum()) if not qualified.empty else 0,
      "reserve_count":int((qualified.tier=="RESERVE").sum()) if not qualified.empty else 0,
      "candidates":[{"ticker":r["ticker"],"score":r["score"],"grade":r["premarket_grade"],"tier":r["tier"]} for r in recs(qualified)]}
    (OUT/"stage_bench_report.json").write_text(json.dumps(meta,indent=2)); print(json.dumps(meta,indent=2))

def stage4(date_s):
    frozen=pd.read_csv(OUT/"top25_frozen.csv") if (OUT/"top25_frozen.csv").stat().st_size>1 else pd.DataFrame()
    checks=[]
    for r in recs(frozen):
        checks.append({"ticker":r.get("ticker"),"score":r.get("score"),"grade":r.get("premarket_grade"),
          "last_hour_close":r.get("last_hour_close"),"status":"QUALIFIED_CLOSE_WATCH","execution":"MARKET_CLOSED"})
    payload={"target_date_et":date_s,"status":"NO_LIVE_EXECUTION","reason":"market_closed_last_hour_snapshot",
      "qualified_close_watch":checks}
    (OUT/"stage4_report.json").write_text(json.dumps(payload,indent=2)); print(json.dumps(payload,indent=2))

def stage5(date_s):
    b=pd.read_csv(OUT/"watch_bench.csv") if (OUT/"watch_bench.csv").exists() and (OUT/"watch_bench.csv").stat().st_size>1 else pd.DataFrame()
    syms=b.ticker.astype(str).tolist() if not b.empty and "ticker" in b else []
    payload={"target_date_et":date_s,"status":"NO_RECOVERY_SCAN","reason":"market_closed_after_last_hour_snapshot","watch_symbols":syms}
    (OUT/"stage5_report.json").write_text(json.dumps(payload,indent=2)); print(json.dumps(payload,indent=2))

def verify(date_s):
    req=["stage1_report.json","stage2_report.json","top25_frozen.json","stage_bench_report.json","stage4_report.json","stage5_report.json"]
    missing=[x for x in req if not (OUT/x).exists()]
    if missing: raise RuntimeError("Missing artifacts: "+",".join(missing))
    payload={"target_date_et":date_s,"status":"COMPLETE","mode":"LAST_HOUR_1500_1600_ET_SNAPSHOT",
      "verified_artifacts":req,"generated_at_et":datetime.now(core.ET).isoformat()}
    (OUT/"complete_report.json").write_text(json.dumps(payload,indent=2)); print(json.dumps(payload,indent=2))

def main():
    p=argparse.ArgumentParser(); p.add_argument("stage",choices=["stage1","stage2","stage3","bench","stage4","stage5","verify"]); p.add_argument("--date",required=True)
    a=p.parse_args()
    globals()[a.stage](a.date)

if __name__=="__main__": main()
