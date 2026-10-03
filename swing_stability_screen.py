from __future__ import annotations

import io, json, math, time
from pathlib import Path
import numpy as np
import pandas as pd
import requests
import yfinance as yf

OUT=Path("output/swing_stability")
OUT.mkdir(parents=True, exist_ok=True)

MIN_PRICE=5.0
MIN_DOLLAR_VOL=20_000_000.0
LOOKBACK_DAYS=120
PIVOT_WINDOW=2
MIN_SWING_PCT=4.0
MIN_SWINGS=4

def universe():
    urls=[
      "https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt",
      "https://www.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt",
    ]
    fs=[]
    h={"User-Agent":"Mozilla/5.0 swing-stability-screen"}
    for u in urls:
        r=requests.get(u,headers=h,timeout=30); r.raise_for_status()
        fs.append(pd.read_csv(io.StringIO(r.text),sep="|"))
    a,b=fs
    a=a.rename(columns={"Symbol":"ticker","Security Name":"name","ETF":"etf","Test Issue":"test"})
    b=b.rename(columns={"ACT Symbol":"ticker","Security Name":"name","ETF":"etf","Test Issue":"test"})
    x=pd.concat([a[["ticker","name","etf","test"]],b[["ticker","name","etf","test"]]],ignore_index=True)
    x=x[(x.etf=="N")&(x.test=="N")].dropna(subset=["ticker"])
    x["ticker"]=x.ticker.astype(str).str.upper().str.strip()
    x=x[~x.ticker.str.contains(r"[.$]",regex=True)]
    bad=r"Warrant|Right| Unit|Preferred|Depositary Shares|Acquisition Corp|SPAC"
    x=x[~x.name.str.contains(bad,case=False,na=False,regex=True)]
    return x.drop_duplicates("ticker").reset_index(drop=True)

def extract(data,t):
    if data is None or data.empty: return pd.DataFrame()
    if isinstance(data.columns,pd.MultiIndex):
        try:
            if t in data.columns.get_level_values(1): return data.xs(t,axis=1,level=1).copy()
            if t in data.columns.get_level_values(0): return data.xs(t,axis=1,level=0).copy()
        except Exception: return pd.DataFrame()
        return pd.DataFrame()
    return data.copy()

def pivots(frame):
    h=pd.to_numeric(frame["High"],errors="coerce").to_numpy(float)
    l=pd.to_numeric(frame["Low"],errors="coerce").to_numpy(float)
    c=pd.to_numeric(frame["Close"],errors="coerce").to_numpy(float)
    idx=list(frame.index)
    raw=[]
    w=PIVOT_WINDOW
    for i in range(w,len(frame)-w):
        hi=h[i]; lo=l[i]
        if math.isfinite(hi) and hi>=np.nanmax(h[i-w:i+w+1]): raw.append([i,"H",hi,idx[i]])
        if math.isfinite(lo) and lo<=np.nanmin(l[i-w:i+w+1]): raw.append([i,"L",lo,idx[i]])
    raw.sort(key=lambda x:(x[0],0 if x[1]=="L" else 1))
    alt=[]
    for p in raw:
        if not alt: alt.append(p); continue
        if p[1]==alt[-1][1]:
            if (p[1]=="H" and p[2]>alt[-1][2]) or (p[1]=="L" and p[2]<alt[-1][2]): alt[-1]=p
        else:
            prev=alt[-1]
            pct=abs(p[2]/prev[2]-1)*100 if prev[2]>0 else 0
            if pct>=MIN_SWING_PCT: alt.append(p)
    swings=[]
    for a,b in zip(alt,alt[1:]):
        pct=abs(b[2]/a[2]-1)*100
        days=max(1,b[0]-a[0])
        direction="UP" if a[1]=="L" and b[1]=="H" else "DOWN"
        swings.append({"from_type":a[1],"to_type":b[1],"swing_pct":pct,"days":days,
                       "from_date":str(pd.Timestamp(a[3]).date()),"to_date":str(pd.Timestamp(b[3]).date())})
    return swings

def score_one(t,name,frame):
    if frame.empty or len(frame)<60: return None
    frame=frame.dropna(subset=["High","Low","Close","Volume"]).tail(LOOKBACK_DAYS)
    if len(frame)<60: return None
    close=pd.to_numeric(frame.Close,errors="coerce")
    vol=pd.to_numeric(frame.Volume,errors="coerce")
    px=float(close.iloc[-1])
    dv=float((close.tail(20)*vol.tail(20)).mean())
    if not (px>=MIN_PRICE and dv>=MIN_DOLLAR_VOL): return None
    ss=pivots(frame)
    if len(ss)<MIN_SWINGS: return None
    p=np.array([x["swing_pct"] for x in ss],float)
    d=np.array([x["days"] for x in ss],float)
    med=float(np.median(p)); avg=float(np.mean(p))
    cv=float(np.std(p,ddof=0)/avg) if avg>0 else 99
    dcv=float(np.std(d,ddof=0)/np.mean(d)) if np.mean(d)>0 else 99
    repeat=max(0.0,1.0-cv)
    duration_cons=max(0.0,1.0-dcv)
    score=med*(0.55+0.45*repeat)*(0.65+0.35*duration_cons)*min(1.25,len(ss)/6)
    return {
      "ticker":t,"name":name,"price":round(px,2),"avg20_dollar_volume":round(dv,0),
      "swing_count":len(ss),"avg_swing_pct":round(avg,2),"median_swing_pct":round(med,2),
      "min_swing_pct":round(float(np.min(p)),2),"max_swing_pct":round(float(np.max(p)),2),
      "swing_pct_cv":round(cv,3),"avg_duration_days":round(float(np.mean(d)),2),
      "duration_cv":round(dcv,3),"repeatability":round(repeat,3),
      "duration_consistency":round(duration_cons,3),"stable_swing_score":round(score,2),
      "recent_swings":ss[-6:]
    }

u=universe()
name_map=dict(zip(u.ticker,u.name))
symbols=u.ticker.tolist()
rows=[]
batch=80
for i in range(0,len(symbols),batch):
    b=symbols[i:i+batch]
    try:
        data=yf.download(b,period="6mo",interval="1d",group_by="column",auto_adjust=True,
                         actions=False,threads=True,progress=False,timeout=30)
    except Exception as e:
        print("batch_error",i,str(e),flush=True); continue
    for t in b:
        f=extract(data,t)
        if f.empty: continue
        r=score_one(t,name_map.get(t,""),f)
        if r: rows.append(r)
    print(json.dumps({"processed":min(i+batch,len(symbols)),"universe":len(symbols),"qualified_so_far":len(rows)}),flush=True)
    time.sleep(0.35)

df=pd.DataFrame(rows)
if df.empty: raise RuntimeError("No qualified swing stocks")
df=df.sort_values(["stable_swing_score","median_swing_pct","repeatability"],ascending=False).reset_index(drop=True)
# daily-ish: median duration <= 7; weekly-ish: >7
daily=df[df.avg_duration_days<=7].head(30).copy()
weekly=df[df.avg_duration_days>7].head(30).copy()
df.to_csv(OUT/"all_ranked.csv",index=False)
daily.to_csv(OUT/"daily_swing_top30.csv",index=False)
weekly.to_csv(OUT/"weekly_swing_top30.csv",index=False)
summary={
 "universe_common_adr":len(u),"liquid_with_4plus_swings":len(df),
 "rules":{"lookback_days":LOOKBACK_DAYS,"pivot_window":PIVOT_WINDOW,"minimum_swing_pct":MIN_SWING_PCT,
          "minimum_swings":MIN_SWINGS,"minimum_price":MIN_PRICE,"minimum_avg20_dollar_volume":MIN_DOLLAR_VOL},
 "top_overall":df.head(20)[["ticker","price","swing_count","median_swing_pct","avg_swing_pct","avg_duration_days","repeatability","stable_swing_score"]].to_dict("records"),
 "top_daily":daily.head(15)[["ticker","price","swing_count","median_swing_pct","avg_duration_days","repeatability","stable_swing_score"]].to_dict("records"),
 "top_weekly":weekly.head(15)[["ticker","price","swing_count","median_swing_pct","avg_duration_days","repeatability","stable_swing_score"]].to_dict("records")
}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
