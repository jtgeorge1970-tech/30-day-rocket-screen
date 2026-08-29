"""30-Day Rocket Screen — market-wide quantitative funnel.

This program deliberately separates quantitative screening from FINAL verification.
A stock cannot be labeled FINAL solely from this output.
"""
from __future__ import annotations
import io, json, math, time
from pathlib import Path
import numpy as np
import pandas as pd
import requests
import yfinance as yf

OUT = Path("output"); OUT.mkdir(exist_ok=True)
UA={"User-Agent":"Mozilla/5.0 rocket-screen research"}

# Three independent opportunity lenses. 0-100 each.
LENSES=("leadership_momentum","beaten_down_reversal","fresh_catalyst_acceleration")

def universe():
    """Broad US-listed common-stock/ADR starting universe from NASDAQ Trader files."""
    urls=["https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt",
          "https://www.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"]
    frames=[]
    for u in urls:
        txt=requests.get(u,headers=UA,timeout=30).text
        df=pd.read_csv(io.StringIO(txt),sep="|")
        frames.append(df)
    a,b=frames
    a=a.rename(columns={"Symbol":"ticker","Security Name":"name","ETF":"etf","Test Issue":"test"})
    b=b.rename(columns={"ACT Symbol":"ticker","Security Name":"name","ETF":"etf","Test Issue":"test"})
    x=pd.concat([a[["ticker","name","etf","test"]],b[["ticker","name","etf","test"]]],ignore_index=True)
    x=x[(x.etf=="N")&(x.test=="N")].dropna(subset=["ticker"])
    x=x[~x.ticker.str.contains(r"[.$]",regex=True)]
    # obvious warrants/units/rights/preferred/shell-like security labels
    bad=r"Warrant|Right| Unit|Preferred|Depositary Shares|Acquisition Corp|SPAC"
    x=x[~x.name.str.contains(bad,case=False,na=False,regex=True)]
    return x.drop_duplicates("ticker").reset_index(drop=True)

def zclip(s):
    s=pd.to_numeric(s,errors="coerce")
    z=(s-s.median())/(s.std()+1e-9)
    return z.clip(-3,3)

def pct_rank(s): return pd.to_numeric(s,errors="coerce").rank(pct=True)*100

def fundamentals(tickers):
    rows=[]
    # yfinance quoteSummary calls can throttle; batching keeps a durable audit trail.
    for i,t in enumerate(tickers):
        try:
            q=yf.Ticker(t)
            fi=q.fast_info
            info=q.info
            rows.append(dict(ticker=t,market_cap=info.get("marketCap"),avg_volume=info.get("averageVolume"),
                revenue_growth=info.get("revenueGrowth"),earnings_growth=info.get("earningsGrowth"),
                earnings_q_growth=info.get("earningsQuarterlyGrowth"),forward_pe=info.get("forwardPE"),
                target_upside=(info.get("targetMeanPrice")/info.get("currentPrice")-1) if info.get("targetMeanPrice") and info.get("currentPrice") else np.nan,
                recommendation=info.get("recommendationMean"),sector=info.get("sector"),industry=info.get("industry")))
        except Exception: rows.append({"ticker":t})
        if i and i%100==0: time.sleep(2)
    return pd.DataFrame(rows)

def prices(tickers):
    data=yf.download(tickers,period="1y",interval="1d",group_by="column",auto_adjust=True,threads=True,progress=False)
    close=data["Close"] if isinstance(data.columns,pd.MultiIndex) else data[["Close"]]
    vol=data["Volume"] if isinstance(data.columns,pd.MultiIndex) else data[["Volume"]]
    rows=[]
    for t in tickers:
        try:
            c=close[t].dropna(); v=vol[t].reindex(c.index)
            if len(c)<130: continue
            p=c.iloc[-1]; hi=c.tail(252).max(); lo=c.tail(252).min()
            rows.append(dict(ticker=t,price=p,ret_5=p/c.iloc[-6]-1,ret_20=p/c.iloc[-21]-1,
              ret_60=p/c.iloc[-61]-1,ret_120=p/c.iloc[-121]-1,drawdown_52=p/hi-1,
              off_low_52=p/lo-1,ma20=p/c.tail(20).mean()-1,ma50=p/c.tail(50).mean()-1,
              vol_ratio=v.tail(10).mean()/(v.tail(60).mean()+1e-9),dollar_volume=(c.tail(20)*v.tail(20)).mean(),
              volatility=c.pct_change().tail(60).std()*math.sqrt(252)))
        except Exception: pass
    return pd.DataFrame(rows)

def score(df):
    # sector/industry relative strength proxy: compare 60d return with sector median.
    sec=df.groupby("sector")["ret_60"].transform("median")
    df["sector_rs"]=df.ret_60-sec
    growth=(pct_rank(df.revenue_growth).fillna(35)+pct_rank(df.earnings_growth).fillna(35))/2
    valuation=(100-pct_rank(df.forward_pe)).fillna(45)
    analyst=pct_rank(df.target_upside).fillna(45)
    liquidity=pct_rank(df.dollar_volume).fillna(0)
    df["leadership_momentum"]=(.22*pct_rank(df.ret_60)+.13*pct_rank(df.ret_20)+.10*pct_rank(df.sector_rs)+.18*growth+.10*pct_rank(df.vol_ratio)+.10*analyst+.07*valuation+.10*liquidity)
    # Rewards meaningful drawdowns only when price is stabilizing/reversing; avoids pure falling knives.
    draw=pct_rank(-df.drawdown_52)
    reversal=(pct_rank(df.ret_5)+pct_rank(df.ret_20)+pct_rank(df.ma20))/3
    df["beaten_down_reversal"]=(.25*draw+.25*reversal+.15*growth+.10*pct_rank(df.sector_rs)+.10*analyst+.05*valuation+.10*liquidity)
    # Quantitative proxy for fresh catalyst/acceleration. News/filing verification is mandatory later.
    acceleration=pct_rank(df.ret_20-df.ret_60/3)
    df["fresh_catalyst_acceleration"]=(.20*acceleration+.15*pct_rank(df.vol_ratio)+.20*growth+.10*pct_rank(df.earnings_q_growth).fillna(40)+.10*pct_rank(df.ret_20)+.10*pct_rank(df.sector_rs)+.05*valuation+.10*liquidity)
    df["best_lens"]=df[list(LENSES)].max(axis=1)
    df["lens_winner"]=df[list(LENSES)].idxmax(axis=1)
    # Downside penalty: excessive volatility, weak 20d trend, very low liquidity.
    risk=(.40*pct_rank(df.volatility)+.35*(100-pct_rank(df.ret_20))+.25*(100-liquidity))
    df["risk_score"]=risk
    df["final_quant_score"]=(df.best_lens*.78 + df[list(LENSES)].mean(axis=1)*.22 - np.maximum(risk-65,0)*.25).clip(0,100)
    return df

def main():
    u=universe(); u.to_csv(OUT/"01_starting_universe.csv",index=False)
    p=prices(u.ticker.tolist()); p.to_csv(OUT/"02_price_metrics.csv",index=False)
    # Investability funnel before expensive fundamentals.
    e=u.merge(p,on="ticker",how="inner")
    e=e[(e.price>=3)&(e.dollar_volume>=2_000_000)]
    e.to_csv(OUT/"03_investable.csv",index=False)
    f=fundamentals(e.ticker.tolist()); e=e.merge(f,on="ticker",how="left")
    e=e[(e.market_cap.fillna(0)>=200_000_000)]
    # Predominantly binary clinical/regulatory gambles cannot be reliably inferred from price alone.
    # Biotechnology names are flagged for mandatory human/company-source verification, not silently promoted FINAL.
    e["binary_risk_review"]=(e.sector.eq("Healthcare") & e.industry.fillna("").str.contains("Biotech",case=False))
    s=score(e).sort_values("final_quant_score",ascending=False)
    s.to_csv(OUT/"04_all_scored.csv",index=False)
    # preserve each lens independently so one style cannot crowd out another
    semis=pd.concat([s.nlargest(40,l) for l in LENSES]).drop_duplicates("ticker")
    semis=semis.sort_values("final_quant_score",ascending=False)
    semis.to_csv(OUT/"05_semifinalists.csv",index=False)
    finalists=semis[~semis.binary_risk_review].head(20)
    finalists.to_csv(OUT/"06_quant_finalists_REQUIRES_CURRENT_VERIFICATION.csv",index=False)
    audit={"starting_universe":len(u),"price_eligible":len(p),"investable_before_marketcap":len(u.merge(p,on='ticker').query('price>=3 and dollar_volume>=2000000')),"fully_scored":len(s),"semifinalists":len(semis),"quant_finalists":len(finalists),"FINAL_LABEL_ALLOWED":False,"note":"Top candidates require fresh earnings/guidance, revisions, catalyst, downside, and binary-risk verification before FINAL ranking."}
    (OUT/"audit.json").write_text(json.dumps(audit,indent=2))
    print(json.dumps(audit,indent=2)); print(finalists[["ticker","lens_winner","final_quant_score"]].to_string(index=False))
if __name__=="__main__": main()
