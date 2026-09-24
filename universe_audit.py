from __future__ import annotations
import io,json,math,time
from pathlib import Path
import pandas as pd
import numpy as np
import requests
import yfinance as yf

OUT=Path("output"); OUT.mkdir(exist_ok=True)
MIN_PRICE=5.0; MIN_DV=20_000_000.0; MIN_MC=300_000_000.0

def universe():
    h={"User-Agent":"Mozilla/5.0 engine4-universe-audit"}
    fs=[]
    for u in ["https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt","https://www.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"]:
        r=requests.get(u,headers=h,timeout=30); r.raise_for_status()
        fs.append(pd.read_csv(io.StringIO(r.text),sep="|"))
    a,b=fs
    a=a.rename(columns={"Symbol":"ticker","Security Name":"name","ETF":"etf","Test Issue":"test"})
    b=b.rename(columns={"ACT Symbol":"ticker","Security Name":"name","ETF":"etf","Test Issue":"test"})
    x=pd.concat([a[["ticker","name","etf","test"]],b[["ticker","name","etf","test"]]],ignore_index=True)
    raw=len(x)
    x=x[(x.etf=="N")&(x.test=="N")].dropna(subset=["ticker"]).copy()
    x["ticker"]=x.ticker.astype(str).str.upper().str.strip()
    x=x[~x.ticker.str.contains(r"[.$]",regex=True)]
    x=x[~x.name.str.contains(r"Warrant|Right| Unit|Preferred|Depositary Shares|Acquisition Corp|SPAC",case=False,na=False,regex=True)]
    return raw,x.drop_duplicates("ticker").reset_index(drop=True)

def legacy_meta():
    inv=OUT/"03_investable.csv"; fund=OUT/"fundamentals_checkpoint.csv"
    if not inv.exists(): return pd.DataFrame()
    a=pd.read_csv(inv); a["ticker"]=a.ticker.astype(str).str.upper()
    if fund.exists():
        f=pd.read_csv(fund); f["ticker"]=f.ticker.astype(str).str.upper()
        keep=[c for c in ["ticker","market_cap","sector"] if c in f.columns]
        if "ticker" in keep: a=a.merge(f[keep].drop_duplicates("ticker"),on="ticker",how="left",suffixes=("","_fund"))
    return a.drop_duplicates("ticker").set_index("ticker")

def frame_for(data,t):
    if data is None or data.empty:return pd.DataFrame()
    if isinstance(data.columns,pd.MultiIndex):
        try:
            if t in set(map(str,data.columns.get_level_values(1))): return data.xs(t,axis=1,level=1)
            if t in set(map(str,data.columns.get_level_values(0))): return data.xs(t,axis=1,level=0)
        except Exception:return pd.DataFrame()
        return pd.DataFrame()
    return data.copy()

def main():
    started=time.monotonic(); raw,u=universe(); legacy=legacy_meta(); syms=u.ticker.tolist()
    rows=[]; failed_batches=0
    for i in range(0,len(syms),200):
        batch=syms[i:i+200]
        try:
            d=yf.download(batch,period="1mo",interval="1d",group_by="column",auto_adjust=True,actions=False,threads=True,progress=False,timeout=30)
        except Exception:
            failed_batches+=1; continue
        for t in batch:
            f=frame_for(d,t)
            if f.empty or "Close" not in f or "Volume" not in f: continue
            c=pd.to_numeric(f["Close"],errors="coerce").dropna()
            if c.empty: continue
            v=pd.to_numeric(f["Volume"],errors="coerce").reindex(c.index).fillna(0)
            rows.append({"ticker":t,"price":float(c.iloc[-1]),"dollar_volume":float((c.tail(20)*v.tail(20)).mean())})
    m=pd.DataFrame(rows).drop_duplicates("ticker")
    liquid=m[(m.price>=MIN_PRICE)&(m.dollar_volume>=MIN_DV)].copy()
    caps={}; legacy_caps=0; fetched_caps=0; missing_caps=0
    for t in liquid.ticker:
        mc=np.nan
        if not legacy.empty and t in legacy.index:
            old=legacy.loc[t]; mc=pd.to_numeric(old.get("market_cap"),errors="coerce")
            if pd.notna(mc) and math.isfinite(float(mc)): legacy_caps+=1
        if pd.isna(mc) or not math.isfinite(float(mc)):
            try:
                fi=yf.Ticker(t).fast_info
                mc=float(fi.get("market_cap") or fi.get("marketCap") or np.nan)
                if math.isfinite(mc): fetched_caps+=1
            except Exception: mc=np.nan
        if pd.isna(mc) or not math.isfinite(float(mc)): missing_caps+=1
        caps[t]=mc
    liquid["market_cap"]=liquid.ticker.map(caps)
    eligible=liquid[liquid.market_cap>=MIN_MC].copy()
    old=set(legacy.index) if not legacy.empty else set()
    new=set(eligible.ticker)
    recovered=sorted(new-old); old_missing=sorted(old-new)
    report={
      "raw_exchange_rows":raw,"exchange_common_adr_count":len(u),"market_data_count":len(m),
      "below_price_or_dollar_volume_count":len(m)-len(liquid),
      "price_and_dollar_volume_survivors":len(liquid),"legacy_market_caps_used":legacy_caps,
      "fresh_market_caps_fetched":fetched_caps,"missing_market_cap_count":missing_caps,
      "engine4_eligible_count":len(eligible),"old_investable_count":len(old),
      "recovered_vs_old_count":len(recovered),"recovered_tickers":recovered,
      "old_not_in_new_count":len(old_missing),"old_not_in_new_tickers":old_missing,
      "failed_market_data_batches":failed_batches,"runtime_seconds":round(time.monotonic()-started,2),
      "locked_gates":{"min_price":MIN_PRICE,"min_market_cap":MIN_MC,"min_dollar_volume":MIN_DV}
    }
    (OUT/"engine4_universe_audit.json").write_text(json.dumps(report,indent=2))
    eligible.sort_values("dollar_volume",ascending=False).to_csv(OUT/"engine4_universe_eligible.csv",index=False)
    print(json.dumps(report,indent=2))
if __name__=="__main__": main()
