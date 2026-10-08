"""OFTS Step 5: distinct BUY/SELL fingerprint research scores, with strict abstention.

This is a diagnostic scorer, NOT a fitted predictive model. Labels use future
returns only for retrospective evaluation, never for signal feature creation.
"""
import csv, math, pathlib, statistics
from collections import defaultdict
ROOT=pathlib.Path(__file__).resolve().parents[2]
SOURCE=ROOT/"ofts/validation/step4_fingerprint_events.csv"
OUTPUT=ROOT/"ofts/validation/step5_fingerprint_scores.csv"
REPORT=ROOT/"ofts/validation/step5_acceptance.txt"
FIELDS=["symbol","confirmation_index","pivot_type","signal_side","quality","amplitude","cadence","confirmation_efficiency","research_score","future_5d_pct","future_10d_pct","future_20d_pct","label_20d","production_signal"]
def bound(v):return max(0.,min(100.,v))
def value(row,key):return float(row[key]) if row.get(key,"") not in ("",None) else None
def score(row):
    quality=value(row,"quality_score_asof_confirmation")
    amplitude=value(row,"preceding_swing_pct")
    bars=value(row,"preceding_swing_bars")
    lag=value(row,"confirmation_lag_bars")
    if any(v is None for v in (quality,amplitude,bars,lag)) or bars<=0:return None
    # Transparent heuristic features only; NOT optimized on forward returns.
    a=bound(100*amplitude/30)
    cadence=bound(100*min(bars,20)/20)
    efficiency=bound(100*(1-lag/max(1,bars+lag)))
    heuristic=.4*quality+.25*a+.15*cadence+.2*efficiency
    side="BUY" if row["pivot_type"]=="L" else "SELL"
    f20=value(row,"future_20d_pct")
    # Retrospective side-specific correctness, not a trading recommendation.
    label="" if f20 is None else int(f20>0 if side=="BUY" else f20<0)
    return dict(symbol=row["symbol"],confirmation_index=row["confirmation_index"],
        pivot_type=row["pivot_type"],signal_side=side,quality=round(quality,4),
        amplitude=round(a,4),cadence=round(cadence,4),
        confirmation_efficiency=round(efficiency,4),research_score=round(heuristic,4),
        future_5d_pct=row["future_5d_pct"],future_10d_pct=row["future_10d_pct"],
        future_20d_pct=row["future_20d_pct"],label_20d=label,
        production_signal="ABSTAIN")
def main():
    with SOURCE.open(newline="") as f:rows=list(csv.DictReader(f))
    assert rows,"Step 4 dataset missing"
    scored=[s for r in rows if (s:=score(r)) is not None]
    assert len(scored)==len(rows),"Incomplete Step 5 feature coverage"
    assert all(0<=r["research_score"]<=100 for r in scored)
    assert all(r["production_signal"]=="ABSTAIN" for r in scored)
    assert all((r["signal_side"]=="BUY")==(r["pivot_type"]=="L") for r in scored)
    # No future outcome may affect a score. Test by corrupting all forward labels.
    for row in rows:
        mutated=dict(row)
        for k in ("future_5d_pct","future_10d_pct","future_20d_pct"):mutated[k]="99999"
        assert score(row)["research_score"]==score(mutated)["research_score"],"Future leakage"
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    with OUTPUT.open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(scored)
    sides={side:[r for r in scored if r["signal_side"]==side] for side in ("BUY","SELL")}
    nlabels=sum(r["label_20d"]!="" for r in scored)
    # An independent chronological training/test split is impossible with only
    # four complete 20-day labels. Fail closed rather than fabricate accuracy.
    ready=nlabels>=100 and all(sum(r["label_20d"]!="" for r in rr)>=40 for rr in sides.values())
    report=(f"STEP 5 DIAGNOSTIC SCORING: PASS\\n"
        f"Events scored: {len(scored)}\\nBUY scores: {len(sides['BUY'])}\\n"
        f"SELL scores: {len(sides['SELL'])}\\n20-day labeled events: {nlabels}\\n"
        f"Feature/label leakage test: PASS\\n"
        f"Predictive training acceptance: {'READY FOR CHRONOLOGICAL TEST' if ready else 'BLOCKED - insufficient labeled history'}\\n"
        f"Production signals: NONE; all ABSTAIN\\n"
        f"Output: ofts/validation/step5_fingerprint_scores.csv\\n")
    REPORT.write_text(report)
    print(report)
if __name__=="__main__":main()
