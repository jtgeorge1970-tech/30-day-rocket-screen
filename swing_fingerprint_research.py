from __future__ import annotations

import io, json, math, time
from pathlib import Path
import numpy as np
import pandas as pd
import requests
import yfinance as yf

OUT = Path("output/swing_fingerprint")
OUT.mkdir(parents=True, exist_ok=True)

LOOKBACK_YEARS = 2
MIN_PRICE = 5.0
MIN_DOLLAR_VOL = 20_000_000.0
MIN_HISTORY = 180
FORWARD_WINDOWS = [3,5,10]
TOP_UNIVERSE = 250

def rsi(s, n=14):
    s=pd.to_numeric(s,errors="coerce")
    d=s.diff(); up=d.clip(lower=0); dn=-d.clip(upper=0)
    au=up.ewm(alpha=1/n,adjust=False,min_periods=n).mean()
    ad=dn.ewm(alpha=1/n,adjust=False,min_periods=n).mean()
    rs=au/ad.replace(0,np.nan)
    return 100-(100/(1+rs))

def ema(s,n): return pd.to_numeric(s,errors="coerce").ewm(span=n,adjust=False).mean()

def atr(frame,n=14):
    h=pd.to_numeric(frame.High,errors="coerce"); l=pd.to_numeric(frame.Low,errors="coerce"); c=pd.to_numeric(frame.Close,errors="coerce")
    pc=c.shift(1)
    tr=pd.concat([(h-l).abs(),(h-pc).abs(),(l-pc).abs()],axis=1).max(axis=1)
    return tr.rolling(n).mean()

def adx(frame,n=14):
    h=pd.to_numeric(frame.High,errors="coerce"); l=pd.to_numeric(frame.Low,errors="coerce"); c=pd.to_numeric(frame.Close,errors="coerce")
    up=h.diff(); dn=-l.diff()
    plus_dm=up.where((up>dn)&(up>0),0.0); minus_dm=dn.where((dn>up)&(dn>0),0.0)
    pc=c.shift(1)
    tr=pd.concat([(h-l).abs(),(h-pc).abs(),(l-pc).abs()],axis=1).max(axis=1)
    atrn=tr.rolling(n).mean()
    plus=100*(plus_dm.rolling(n).mean()/atrn.replace(0,np.nan))
    minus=100*(minus_dm.rolling(n).mean()/atrn.replace(0,np.nan))
    dx=(100*(plus-minus).abs()/(plus+minus).replace(0,np.nan))
    return dx.rolling(n).mean()

def stoch_rsi(r,n=14):
    lo=r.rolling(n).min(); hi=r.rolling(n).max()
    return 100*(r-lo)/(hi-lo).replace(0,np.nan)

def williams_r(frame,n=14):
    hh=pd.to_numeric(frame.High,errors="coerce").rolling(n).max()
    ll=pd.to_numeric(frame.Low,errors="coerce").rolling(n).min()
    c=pd.to_numeric(frame.Close,errors="coerce")
    return -100*(hh-c)/(hh-ll).replace(0,np.nan)

def pivots(frame, window=2, min_swing_pct=4.0):
    h=pd.to_numeric(frame.High,errors="coerce").to_numpy(float)
    l=pd.to_numeric(frame.Low,errors="coerce").to_numpy(float)
    idx=list(frame.index); raw=[]
    for i in range(window,len(frame)-window):
        if math.isfinite(h[i]) and h[i]>=np.nanmax(h[i-window:i+window+1]): raw.append([i,"H",h[i],idx[i]])
        if math.isfinite(l[i]) and l[i]<=np.nanmin(l[i-window:i+window+1]): raw.append([i,"L",l[i],idx[i]])
    raw.sort(key=lambda x:(x[0],0 if x[1]=="L" else 1))
    alt=[]
    for p in raw:
        if not alt: alt.append(p); continue
        if p[1]==alt[-1][1]:
            if (p[1]=="H" and p[2]>alt[-1][2]) or (p[1]=="L" and p[2]<alt[-1][2]): alt[-1]=p
        else:
            pct=abs(p[2]/alt[-1][2]-1)*100 if alt[-1][2] else 0
            if pct>=min_swing_pct: alt.append(p)
    return alt

def extract(data,t):
    if data is None or data.empty: return pd.DataFrame()
    if isinstance(data.columns,pd.MultiIndex):
        try:
            if t in data.columns.get_level_values(1): return data.xs(t,axis=1,level=1).copy()
            if t in data.columns.get_level_values(0): return data.xs(t,axis=1,level=0).copy()
        except Exception: return pd.DataFrame()
        return pd.DataFrame()
    return data.copy()

# Prefer the prior swing screen's ranked output if present in repo checkout artifacts is unavailable.
# Rebuild liquid universe, then rank by recent swing repeatability quickly.
def universe():
    urls=["https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt","https://www.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"]
    fs=[]; headers={"User-Agent":"Mozilla/5.0 swing-fingerprint"}
    for u in urls:
        r=requests.get(u,headers=headers,timeout=30); r.raise_for_status()
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

def recent_rank(t,name,f):
    if f.empty or len(f)<80: return None
    f=f.dropna(subset=["High","Low","Close","Volume"]).tail(120)
    if len(f) < 60:
        return None
    c=pd.to_numeric(f.Close,errors="coerce"); v=pd.to_numeric(f.Volume,errors="coerce")
    c=c.dropna()
    v=v.reindex(c.index).fillna(0)
    if c.empty:
        return None
    px=float(c.iloc[-1]); dv=float((c.tail(20)*v.tail(20)).mean())
    if px<MIN_PRICE or dv<MIN_DOLLAR_VOL: return None
    ps=pivots(f,2,4.0)
    if len(ps)<5: return None
    swings=[]
    for a,b in zip(ps,ps[1:]):
        swings.append(abs(b[2]/a[2]-1)*100)
    arr=np.array(swings,float)
    med=float(np.median(arr)); cv=float(np.std(arr)/np.mean(arr)) if np.mean(arr)>0 else 9
    repeat=max(0,1-cv)
    score=med*(0.5+0.5*repeat)*min(1.25,len(arr)/6)
    return {"ticker":t,"name":name,"rank_score":score,"median_swing":med,"repeatability":repeat,"swing_count":len(arr)}

u=universe(); names=dict(zip(u.ticker,u.name)); syms=u.ticker.tolist()
rank=[]
for i in range(0,len(syms),100):
    b=syms[i:i+100]
    try:
        data=yf.download(b,period="6mo",interval="1d",group_by="column",auto_adjust=True,actions=False,threads=False,progress=False,timeout=30)
    except Exception:
        continue
    for t in b:
        rr=recent_rank(t,names.get(t,""),extract(data,t))
        if rr: rank.append(rr)
    print(json.dumps({"phase":"rank","processed":min(i+100,len(syms)),"qualified":len(rank)}),flush=True)
    time.sleep(0.2)

rank_df=pd.DataFrame(rank).sort_values("rank_score",ascending=False).head(TOP_UNIVERSE)
rank_df.to_csv(OUT/"universe_top250.csv",index=False)

events=[]
for batch_no,i in enumerate(range(0,len(rank_df),50),1):
    b=rank_df.ticker.iloc[i:i+50].tolist()
    try:
        data=yf.download(b,period=f"{LOOKBACK_YEARS}y",interval="1d",group_by="column",auto_adjust=True,actions=False,threads=True,progress=False,timeout=30)
    except Exception:
        continue
    for t in b:
        f=extract(data,t).dropna(subset=["High","Low","Close","Volume"]).copy()
        if len(f)<MIN_HISTORY: continue
        c=pd.to_numeric(f.Close,errors="coerce"); h=pd.to_numeric(f.High,errors="coerce"); l=pd.to_numeric(f.Low,errors="coerce"); v=pd.to_numeric(f.Volume,errors="coerce")
        R=rsi(c); S=stoch_rsi(R); W=williams_r(f); A=atr(f); D=adx(f)
        e5,e10,e20,e50=ema(c,5),ema(c,10),ema(c,20),ema(c,50)
        macd=ema(c,12)-ema(c,26); sig=ema(macd,9); hist=macd-sig
        vz=(v-v.rolling(20).mean())/v.rolling(20).std().replace(0,np.nan)
        ret1=c.pct_change()*100; ret3=c.pct_change(3)*100; ret5=c.pct_change(5)*100
        ps=pivots(f,2,4.0)
        for p in ps:
            j,typ,price,dt=p
            if j<55 or j+10>=len(f): continue
            row={
              "ticker":t,"date":str(pd.Timestamp(dt).date()),"event_type":typ,"pivot_price":float(price),
              "close":float(c.iloc[j]),"rsi14":float(R.iloc[j]) if pd.notna(R.iloc[j]) else np.nan,
              "rsi_slope1":float(R.iloc[j]-R.iloc[j-1]) if pd.notna(R.iloc[j]) and pd.notna(R.iloc[j-1]) else np.nan,
              "stoch_rsi":float(S.iloc[j]) if pd.notna(S.iloc[j]) else np.nan,
              "williams_r":float(W.iloc[j]) if pd.notna(W.iloc[j]) else np.nan,
              "adx14":float(D.iloc[j]) if pd.notna(D.iloc[j]) else np.nan,
              "atr_pct":float(A.iloc[j]/c.iloc[j]*100) if pd.notna(A.iloc[j]) and c.iloc[j] else np.nan,
              "dist_ema5_pct":float((c.iloc[j]/e5.iloc[j]-1)*100),
              "dist_ema10_pct":float((c.iloc[j]/e10.iloc[j]-1)*100),
              "dist_ema20_pct":float((c.iloc[j]/e20.iloc[j]-1)*100),
              "dist_ema50_pct":float((c.iloc[j]/e50.iloc[j]-1)*100),
              "macd_hist":float(hist.iloc[j]) if pd.notna(hist.iloc[j]) else np.nan,
              "macd_hist_slope1":float(hist.iloc[j]-hist.iloc[j-1]) if pd.notna(hist.iloc[j]) and pd.notna(hist.iloc[j-1]) else np.nan,
              "volume_z20":float(vz.iloc[j]) if pd.notna(vz.iloc[j]) else np.nan,
              "ret1_pct":float(ret1.iloc[j]) if pd.notna(ret1.iloc[j]) else np.nan,
              "ret3_pct":float(ret3.iloc[j]) if pd.notna(ret3.iloc[j]) else np.nan,
              "ret5_pct":float(ret5.iloc[j]) if pd.notna(ret5.iloc[j]) else np.nan,
              "lower_wick_pct":float((min(c.iloc[j],f.Open.iloc[j])-l.iloc[j])/(h.iloc[j]-l.iloc[j])*100) if (h.iloc[j]-l.iloc[j])>0 else np.nan,
              "upper_wick_pct":float((h.iloc[j]-max(c.iloc[j],f.Open.iloc[j]))/(h.iloc[j]-l.iloc[j])*100) if (h.iloc[j]-l.iloc[j])>0 else np.nan,
            }
            for fw in FORWARD_WINDOWS:
                future=c.iloc[j+1:j+fw+1]
                row[f"fwd_{fw}d_close_pct"]=float((c.iloc[j+fw]/c.iloc[j]-1)*100)
                row[f"fwd_{fw}d_max_pct"]=float((future.max()/c.iloc[j]-1)*100)
                row[f"fwd_{fw}d_min_pct"]=float((future.min()/c.iloc[j]-1)*100)
            events.append(row)
    print(json.dumps({"phase":"fingerprints","batch":batch_no,"events":len(events)}),flush=True)

ev=pd.DataFrame(events)
ev.to_csv(OUT/"pivot_fingerprints.csv",index=False)

# Define successful buy/sell outcomes without using indicators themselves.
# Buy success: pivot low with >=8% max gain within 5d and no worse than -6% excursion.
# Sell success: pivot high with <=-8% min return within 5d and no >6% upside continuation.
ev["successful_buy"]=(ev.event_type.eq("L") & (ev["fwd_5d_max_pct"]>=8) & (ev["fwd_5d_min_pct"]>=-6))
ev["successful_sell"]=(ev.event_type.eq("H") & (ev["fwd_5d_min_pct"]<=-8) & (ev["fwd_5d_max_pct"]<=6))

features=["rsi14","rsi_slope1","stoch_rsi","williams_r","adx14","atr_pct",
          "dist_ema5_pct","dist_ema10_pct","dist_ema20_pct","dist_ema50_pct",
          "macd_hist","macd_hist_slope1","volume_z20","ret1_pct","ret3_pct","ret5_pct",
          "lower_wick_pct","upper_wick_pct"]

def summarize(mask_pos, mask_all):
    out=[]
    pos=ev[mask_pos]; base=ev[mask_all]
    for col in features:
        a=pd.to_numeric(pos[col],errors="coerce").dropna()
        b=pd.to_numeric(base[col],errors="coerce").dropna()
        if len(a)<10 or len(b)<20: continue
        out.append({
          "feature":col,
          "success_median":float(a.median()),
          "all_median":float(b.median()),
          "success_q25":float(a.quantile(.25)),
          "success_q75":float(a.quantile(.75)),
          "median_shift":float(a.median()-b.median()),
          "success_n":len(a),"all_n":len(b)
        })
    return pd.DataFrame(out).sort_values("median_shift", key=lambda s:s.abs(), ascending=False)

buy_summary=summarize(ev.successful_buy, ev.event_type.eq("L"))
sell_summary=summarize(ev.successful_sell, ev.event_type.eq("H"))
buy_summary.to_csv(OUT/"buy_fingerprint_feature_summary.csv",index=False)
sell_summary.to_csv(OUT/"sell_fingerprint_feature_summary.csv",index=False)

summary={
  "top_universe":int(len(rank_df)),
  "total_pivot_events":int(len(ev)),
  "low_events":int(ev.event_type.eq("L").sum()),
  "high_events":int(ev.event_type.eq("H").sum()),
  "successful_buy_events":int(ev.successful_buy.sum()),
  "successful_sell_events":int(ev.successful_sell.sum()),
  "buy_success_rate_pct":round(100*ev.successful_buy.sum()/max(1,ev.event_type.eq("L").sum()),2),
  "sell_success_rate_pct":round(100*ev.successful_sell.sum()/max(1,ev.event_type.eq("H").sum()),2),
  "buy_top_feature_shifts":buy_summary.head(10).to_dict("records"),
  "sell_top_feature_shifts":sell_summary.head(10).to_dict("records"),
  "label_definition":{
    "buy":"pivot low; >=8% max gain within next 5 sessions; no worse than -6% excursion",
    "sell":"pivot high; <=-8% min return within next 5 sessions; no more than +6% upside continuation"
  }
}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
