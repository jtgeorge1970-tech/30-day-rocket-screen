"""Fetch reproducible dated OHLCV for the OFTS research cohort.

Provider: Yahoo Finance via yfinance; unavailable tickers are explicitly logged.
No fabricated bars, and no synthetic fallback.
"""
import csv
from datetime import datetime, timezone
from pathlib import Path
import yfinance as yf

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"ofts/research/extended_history_ohlcv.csv"
REPORT=ROOT/"ofts/validation/history_acquisition.txt"
SYMBOLS=["CBRS","AAL","KBR","ROCK","WW","AEHR","AXTI","BKSY","PLTR","CHPT","AIP","MU","STX","HOOD"]
FIELDS=["symbol","date","open","high","low","close","volume"]
def main():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    records=[]; status=[]
    for symbol in SYMBOLS:
        try:
            df=yf.download(symbol,start="2020-01-01",end="2026-10-08",auto_adjust=False,actions=False,progress=False,threads=False)
            if df.empty:
                status.append((symbol,0,"NO DATA"));continue
            count=0
            for date,row in df.iterrows():
                def val(k):
                    v=row[k]
                    return float(v.iloc[0] if hasattr(v,"iloc") else v)
                o,h,l,c=[val(k) for k in ("Open","High","Low","Close")]
                if not (0<l<=h and l<=o<=h and l<=c<=h):continue
                v=val("Volume")
                records.append(dict(symbol=symbol,date=date.strftime("%Y-%m-%d"),open=round(o,6),high=round(h,6),low=round(l,6),close=round(c,6),volume=int(v)))
                count+=1
            status.append((symbol,count,"OK" if count>=200 else "SHORT HISTORY"))
        except Exception as e:
            status.append((symbol,0,"FETCH ERROR: "+str(e)[:180]))
    with OUT.open("w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=FIELDS);writer.writeheader();writer.writerows(records)
    REPORT.write_text("OFTS historical acquisition | Yahoo Finance | raw unadjusted OHLCV | 2020-01-01 through 2026-10-07\\n"+"\\n".join(f"{s}: {n} bars; {state}" for s,n,state in status)+"\\nTotal bars: "+str(len(records))+"\\n")
    print(REPORT.read_text())
    if len(records)<1000:raise RuntimeError("Insufficient authentic historical OHLCV downloaded")
if __name__=="__main__":main()
