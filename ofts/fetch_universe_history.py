"""Download daily OHLC for the complete OFTS universe with durable batch checkpoints."""
import csv,json,pathlib,time
import yfinance as yf
ROOT=pathlib.Path(__file__).resolve().parents[1]
SRC=ROOT/"ofts/universe.csv"
OUT=ROOT/"ofts-output"
OUT.mkdir(exist_ok=True)
with SRC.open(newline="") as f:
    symbols=[r["symbol"].strip().upper() for r in csv.DictReader(f)]
assert len(symbols)==5502 and len(set(symbols))==5502
history=OUT/"universe_ohlcv.csv"
completed=OUT/"download_completed.txt"
done=set(completed.read_text().splitlines()) if completed.exists() else set()
if not history.exists():
    history.write_text("symbol,date,open,high,low,close,volume\n")
batch_size=40
for start in range(0,len(symbols),batch_size):
    batch=[s for s in symbols[start:start+batch_size] if s not in done]
    if not batch:continue
    try:
        frame=yf.download(batch,period="2y",interval="1d",auto_adjust=False,group_by="ticker",threads=True,progress=False,timeout=20)
        with history.open("a",newline="") as fh:
            w=csv.writer(fh)
            for s in batch:
                try:
                    df=frame[s] if len(batch)>1 else frame
                    if df.empty:continue
                    for dt,r in df.iterrows():
                        vals=[r.get(k) for k in ("Open","High","Low","Close","Volume")]
                        if any(v!=v for v in vals[:4]):continue
                        w.writerow([s,str(dt.date()),*vals])
                except (KeyError,ValueError,TypeError):pass
    except Exception as exc:
        print("BATCH_ERROR",start,str(exc)[:200],flush=True)
    done.update(batch)
    completed.write_text("\n".join(sorted(done))+"\n")
    print("DOWNLOAD_PROGRESS",len(done),len(symbols),flush=True)
print("DOWNLOAD_COMPLETE",len(done))
