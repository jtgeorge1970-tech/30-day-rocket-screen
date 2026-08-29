"""30-Day Rocket Screen — market-wide quantitative funnel.

This program deliberately separates quantitative screening from FINAL verification.
A stock cannot be labeled FINAL solely from this output.
"""
from __future__ import annotations
import io, json, math, time, random
from pathlib import Path
import numpy as np
import pandas as pd
import requests
import yfinance as yf

OUT = Path("output"); OUT.mkdir(exist_ok=True)
UA={"User-Agent":"Mozilla/5.0 rocket-screen research"}
LENSES=("leadership_momentum","beaten_down_reversal","fresh_catalyst_acceleration")
YAHOO_MIN_INTERVAL = 60.0 / 100.0
_last_yahoo_call = 0.0

def yahoo_pace():
    global _last_yahoo_call
    wait=YAHOO_MIN_INTERVAL-(time.monotonic()-_last_yahoo_call)
    if wait>0: time.sleep(wait)
    _last_yahoo_call=time.monotonic()

def retry_yahoo(fn,label,attempts=6):
    last=None
    for attempt in range(attempts):
        yahoo_pace()
        try: return fn()
        except Exception as exc:
            last=exc
            if attempt==attempts-1: break
            delay=min(60,3*(2**attempt))+random.uniform(0,2)
            print(f"Yahoo retry {attempt+1}/{attempts-1} for {label}: {exc}; sleeping {delay:.1f}s",flush=True)
            time.sleep(delay)
    print(f"Yahoo failed after retries for {label}: {last}",flush=True); return None

def universe():
    urls=["https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt","https://www.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"]
    frames=[]
    for u in urls:
        txt=requests.get(u,headers=UA,timeout=30).text; frames.append(pd.read_csv(io.StringIO(txt),sep="|"))
    a,b=frames
    a=a.rename(columns={"Symbol":"ticker","Security Name":"name","ETF":"etf","Test Issue":"test"})
    b=b.rename(columns={"ACT Symbol":"ticker","Security Name":"name","ETF":"etf","Test Issue":"test"})
    x=pd.concat([a[["ticker","name","etf","test"]],b[["ticker","name","etf","test"]]],ignore_index=True)
    x=x[(x.etf=="N")&(x.test=="N")].dropna(subset=["ticker"]); x=x[~x.ticker.str.contains(r"[.$]",regex=True)]
    bad=r"Warrant|Right| Unit|Preferred|Depositary Shares|Acquisition Corp|SPAC"
    x=x[~x.name.str.contains(bad,case=False,na=False,regex=True)]
    return x.drop_duplicates("ticker").reset_index(drop=True)

def pct_rank(s): return pd.to_numeric(s,errors="coerce").rank(pct=True)*100

def fundamentals(tickers):
    cols=["ticker","market_cap","avg_volume","revenue_growth","earnings_growth","earnings_q_growth","forward_pe","target_upside","recommendation","sector","industry"]
    rows=[]; checkpoint=OUT/"fundamentals_checkpoint.csv"; done={}
    if checkpoint.exists():
        try: done={r["ticker"]:r for r in pd.read_csv(checkpoint).to_dict("records")}
        except Exception: done={}
    for i,t in enumerate(tickers,1):
        if t in done: rows.append(done[t]); continue
        info=retry_yahoo(lambda: yf.Ticker(t).info,f"fundamentals {t}"); row={"ticker":t}
        if info:
            row.update(market_cap=info.get("marketCap"),avg_volume=info.get("averageVolume"),revenue_growth=info.get("revenueGrowth"),earnings_growth=info.get("earningsGrowth"),earnings_q_growth=info.get("earningsQuarterlyGrowth"),forward_pe=info.get("forwardPE"),target_upside=(info.get("targetMeanPrice")/info.get("currentPrice")-1) if info.get("targetMeanPrice") and info.get("currentPrice") else np.nan,recommendation=info.get("recommendationMean"),sector=info.get("sector"),industry=info.get("industry"))
        rows.append(row)
        if i%25==0:
            pd.DataFrame(rows).reindex(columns=cols).to_csv(checkpoint,index=False); print(f"Fundamentals progress: {i}/{len(tickers)}",flush=True)
    df=pd.DataFrame(rows).reindex(columns=cols); df.to_csv(checkpoint,index=False); return df

def prices(tickers):
    rows=[]; batch_size=20
    for start in range(0,len(tickers),batch_size):
        batch=tickers[start:start+batch_size]
        data=retry_yahoo(lambda: yf.download(batch,period="1y",interval="1d",group_by="column",auto_adjust=True,threads=False,progress=False,timeout=30),f"prices batch {start//batch_size+1}")
        if data is None or data.empty: print(f"Skipping failed price batch after retries: {batch}",flush=True); continue
        try: close=data["Close"] if isinstance(data.columns,pd.MultiIndex) else data[["Close"]]; vol=data["Volume"] if isinstance(data.columns,pd.MultiIndex) else data[["Volume"]]
        except Exception: continue
        for t in batch:
            try:
                if isinstance(close,pd.Series): c=close.dropna(); v=vol.reindex(c.index)
                else: c=close[t].dropna(); v=vol[t].reindex(c.index)
                if len(c)<130: continue
                p=c.iloc[-1]; hi=c.tail(252).max(); lo=c.tail(252).min()
                rows.append(dict(ticker=t,price=p,ret_5=p/c.iloc[-6]-1,ret_20=p/c.iloc[-21]-1,ret_60=p/c.iloc[-61]-1,ret_120=p/c.iloc[-121]-1,drawdown_52=p/hi-1,off_low_52=p/lo-1,ma20=p/c.tail(20).mean()-1,ma50=p/c.tail(50).mean()-1,vol_ratio=v.tail(10).mean()/(v.tail(60).mean()+1e-9),dollar_volume=(c.tail(20)*v.tail(20)).mean(),volatility=c.pct_change().tail(60).std()*math.sqrt(252)))
            except Exception as exc: print(f"Price metric skip {t}: {exc}",flush=True)
        if (start//batch_size+1)%10==0: print(f"Price progress: {min(start+batch_size,len(tickers))}/{len(tickers)}",flush=True)
    return pd.DataFrame(rows)

def score(df):
    sec=df.groupby("sector")["ret_60"].transform("median"); df["sector_rs"]=df.ret_60-sec
    growth=(pct_rank(df.revenue_growth).fillna(35)+pct_rank(df.earnings_growth).fillna(35))/2
    valuation=(100-pct_rank(df.forward_pe)).fillna(45); analyst=pct_rank(df.target_upside).fillna(45); liquidity=pct_rank(df.dollar_volume).fillna(0)
    df["leadership_momentum"]=(.22*pct_rank(df.ret_60)+.13*pct_rank(df.ret_20)+.10*pct_rank(df.sector_rs)+.18*growth+.10*pct_rank(df.vol_ratio)+.10*analyst+.07*valuation+.10*liquidity)
    draw=pct_rank(-df.drawdown_52); reversal=(pct_rank(df.ret_5)+pct_rank(df.ret_20)+pct_rank(df.ma20))/3
    df["beaten_down_reversal"]=(.25*draw+.25*reversal+.15*growth+.10*pct_rank(df.sector_rs)+.10*analyst+.05*valuation+.10*liquidity)
    acceleration=pct_rank(df.ret_20-df.ret_60/3)
    df["fresh_catalyst_acceleration"]=(.20*acceleration+.15*pct_rank(df.vol_ratio)+.20*growth+.10*pct_rank(df.earnings_q_growth).fillna(40)+.10*pct_rank(df.ret_20)+.10*pct_rank(df.sector_rs)+.05*valuation+.10*liquidity)
    # Pandas 3 raises on idxmax when an entire row is NA. Keep the ticker auditable,
    # but never let it crash the market-wide run or accidentally promote it.
    lens_values=df[list(LENSES)].apply(pd.to_numeric,errors="coerce")
    all_na=lens_values.isna().all(axis=1)
    df["best_lens"]=lens_values.max(axis=1,skipna=True)
    df["lens_winner"]=pd.Series(pd.NA,index=df.index,dtype="object")
    if (~all_na).any(): df.loc[~all_na,"lens_winner"]=lens_values.loc[~all_na].idxmax(axis=1,skipna=True)
    df["lens_data_missing"]=all_na
    risk=(.40*pct_rank(df.volatility)+.35*(100-pct_rank(df.ret_20))+.25*(100-liquidity)); df["risk_score"]=risk
    df["final_quant_score"]=(df.best_lens*.78+lens_values.mean(axis=1,skipna=True)*.22-np.maximum(risk-65,0)*.25).clip(0,100)
    df.loc[all_na,"final_quant_score"]=np.nan
    return df

def main():
    u=universe(); u.to_csv(OUT/"01_starting_universe.csv",index=False); print(f"Starting universe: {len(u)}",flush=True)
    p=prices(u.ticker.tolist()); p.to_csv(OUT/"02_price_metrics.csv",index=False)
    if p.empty or not {"ticker","price","dollar_volume"}.issubset(p.columns): raise RuntimeError("Price stage produced insufficient schema; refusing incomplete FINAL screen")
    e=u.merge(p,on="ticker",how="inner"); e=e[(e.price>=3)&(e.dollar_volume>=2_000_000)]; e.to_csv(OUT/"03_investable.csv",index=False)
    f=fundamentals(e.ticker.tolist()); e=e.merge(f,on="ticker",how="left")
    if "market_cap" not in e.columns: raise RuntimeError("market_cap unavailable; refusing incomplete FINAL screen")
    missing_mc=int(e.market_cap.isna().sum()); print(f"Fundamentals coverage: {len(e)-missing_mc}/{len(e)} market caps",flush=True)
    e=e[e.market_cap.fillna(0)>=200_000_000]; e["binary_risk_review"]=(e.sector.eq("Healthcare")&e.industry.fillna("").str.contains("Biotech",case=False))
    if e.empty: raise RuntimeError("No fully eligible securities after data-quality filters")
    s=score(e); missing_lens=int(s.lens_data_missing.sum()); print(f"All-lens missing rows safely excluded: {missing_lens}",flush=True)
    s=s.sort_values("final_quant_score",ascending=False,na_position="last"); s.to_csv(OUT/"04_all_scored.csv",index=False)
    scoreable=s[s.final_quant_score.notna()].copy()
    if scoreable.empty: raise RuntimeError("No securities have scoreable three-lens data")
    semis=pd.concat([scoreable.nlargest(40,l) for l in LENSES]).drop_duplicates("ticker").sort_values("final_quant_score",ascending=False); semis.to_csv(OUT/"05_semifinalists.csv",index=False)
    finalists=semis[~semis.binary_risk_review].head(20); finalists.to_csv(OUT/"06_quant_finalists_REQUIRES_CURRENT_VERIFICATION.csv",index=False)
    audit={"starting_universe":len(u),"price_eligible":len(p),"investable_before_marketcap":len(u.merge(p,on='ticker').query('price>=3 and dollar_volume>=2000000')),"fundamentals_requested":len(f),"market_cap_missing":missing_mc,"all_lens_missing":missing_lens,"fully_scored":len(scoreable),"semifinalists":len(semis),"quant_finalists":len(finalists),"yahoo_rate_cap_per_minute":100,"three_lenses":list(LENSES),"FINAL_LABEL_ALLOWED":False,"note":"Top candidates require fresh earnings/guidance, revisions, catalyst, downside, and binary-risk verification before FINAL ranking."}
    (OUT/"audit.json").write_text(json.dumps(audit,indent=2)); print(json.dumps(audit,indent=2)); print(finalists[["ticker","lens_winner","final_quant_score"]].to_string(index=False))
if __name__=="__main__": main()
