"""OFTS research-only next-open execution audit. No production authorization."""
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean, median

ROOT = Path(__file__).resolve().parents[2]
BARS = ROOT / "ofts/research/extended_history_ohlcv.csv"
EVENTS = ROOT / "ofts/validation/extended_fingerprint_events.csv"
OUT = ROOT / "ofts/validation/execution_audit_trades.csv"
SUMMARY = ROOT / "ofts/validation/execution_audit_summary.txt"

def grouped(path):
    out = defaultdict(list)
    with path.open(newline="") as f:
        for row in csv.DictReader(f):
            out[row["symbol"]].append(row)
    return out

def stop_return(bars, entry_idx, exit_idx, stop_pct):
    entry = float(bars[entry_idx]["open"])
    stop_price = entry * (1-stop_pct/100)
    for i in range(entry_idx, exit_idx+1):
        day = bars[i]
        if i > entry_idx and float(day["open"]) <= stop_price:
            return 100*(float(day["open"])/entry-1)
        if float(day["low"]) <= stop_price:
            return -stop_pct
    return 100*(float(bars[exit_idx]["close"])/entry-1)

def main():
    bars = grouped(BARS)
    events = grouped(EVENTS)
    for b in bars.values():
        b.sort(key=lambda r:r["date"])
    results = []
    for symbol, ev in sorted(events.items()):
        ev.sort(key=lambda r:int(r["confirmation_index"]))
        cut = int(.7*len(ev))
        if cut < 8 or cut >= len(ev): continue
        boundary = int(ev[cut]["confirmation_index"])
        train = [float(r["future_20d_pct"]) for r in ev[:cut]
                 if r["pivot_type"]=="L" and
                 int(r["confirmation_index"])+20 < boundary]
        if len(train)<8 or mean(train)<=0: continue
        b=bars.get(symbol,[])
        last_exit=-1
        for r in ev[cut:]:
            if r["pivot_type"]!="L": continue
            i=int(r["confirmation_index"])
            entry_idx, exit_idx = i+1, i+21
            if i<=last_exit or exit_idx>=len(b): continue
            if abs(float(r["confirmation_price"])/float(b[i]["close"])-1)>.01:
                raise AssertionError(f"Confirmation close mismatch {symbol} {i}")
            entry=float(b[entry_idx]["open"])
            if entry<=0: raise AssertionError(f"Invalid entry {symbol} {i}")
            ret=100*(float(b[exit_idx]["close"])/entry-1)
            suspect=any(
                float(b[j]["close"])/float(b[j-1]["close"])<.55 or
                float(b[j]["close"])/float(b[j-1]["close"])>1.8
                for j in range(entry_idx,exit_idx+1))
            results.append(dict(
                symbol=symbol,confirmation_date=b[i]["date"],
                entry_date=b[entry_idx]["date"],exit_date=b[exit_idx]["date"],
                entry_open=round(entry,6),
                gross_20session_pct=round(ret,6),
                stop_8_pct=round(stop_return(b,entry_idx,exit_idx,8),6),
                stop_12_pct=round(stop_return(b,entry_idx,exit_idx,12),6),
                stop_16_pct=round(stop_return(b,entry_idx,exit_idx,16),6),
                assumed_25bp_roundtrip_pct=round(ret-.25,6),
                assumed_50bp_roundtrip_pct=round(ret-.50,6),
                possible_split_window=suspect))
            last_exit=exit_idx
    if not results: raise RuntimeError("No auditable signals")
    OUT.parent.mkdir(parents=True,exist_ok=True)
    with OUT.open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(results[0]))
        w.writeheader();w.writerows(results)
    returns=sorted(r["gross_20session_pct"] for r in results)
    affordable=sorted(r["gross_20session_pct"] for r in results if r["entry_open"]<=150)
    lines=[
        f"Audited nonoverlapping BUY trades: {len(results)}",
        f"Winners: {sum(v>0 for v in returns)}",
        f"Mean gross 20-session return pct: {mean(returns):.6f}",
        f"Median gross 20-session return pct: {median(returns):.6f}",
        f"Mean excluding five largest winners pct: {mean(returns[:-5]):.6f}",
        f"Under $150 entry: {len(affordable)} trades, {sum(v>0 for v in affordable)} winners",
        f"Under $150 mean pct: {mean(affordable):.6f}",
        f"Under $150 median pct: {median(affordable):.6f}",
        f"Under $150 excluding top five pct: {mean(affordable[:-5]):.6f}",
        f"Potential split windows: {sum(r['possible_split_window'] for r in results)}",
        "WARNING: raw unadjusted prices; corporate actions and real transaction costs NOT reconciled.",
        "Chronological 70/30 holdout; 20-bar training embargo; no overlapping positions per symbol.",
        "Production approval: NO"]
    for pct in (8,12,16):
        lines.append(f"Stop {pct}% mean pct: {mean(r[f'stop_{pct}_pct'] for r in results):.6f}")
    SUMMARY.write_text("\n".join(lines)+"\n")
    print(SUMMARY.read_text())

if __name__=="__main__": main()
