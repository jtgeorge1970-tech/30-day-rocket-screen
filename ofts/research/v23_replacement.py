"""OFTS v2.3 RESEARCH candidate. NOT locked v2.2; no production authorization."""
from statistics import median
from .candidate_components import detect_turns, swing_features, atr_percent, clamp, WEIGHTS

def _consistency(xs):
    if len(xs)<3: return 0.0
    m=median(xs)
    return clamp(100*(1-1.4826*median(abs(x-m) for x in xs)/max(m,1e-9)))

def _score(highs,lows,closes,threshold):
    turns=detect_turns(closes,threshold)
    feats=swing_features(turns)
    swings=feats["swings"]
    pcts=[s["pct"] for s in swings]
    intervals_h=feats["peak_intervals"]
    intervals_l=feats["trough_intervals"]
    # Alternation must measure cycle regularity, not the ZigZag invariant.
    # Reward balanced up/down magnitudes and timing; avoid automatic 100%.
    up=[s["pct"] for s in swings if s["kind"]=="UP"]
    down=[s["pct"] for s in swings if s["kind"]=="DOWN"]
    balance=0.0 if not up or not down else clamp(100*min(median(up),median(down))/max(median(up),median(down)))
    cadence=( _consistency(intervals_h)+_consistency(intervals_l))/2
    purity=balance*cadence/100
    # Penalize directional drift relative to TOTAL close-to-close movement.
    path=sum(abs(b-a) for a,b in zip(closes,closes[1:]))
    displacement=abs(closes[-1]-closes[0])
    drift=clamp(100*(1-displacement/max(path,1e-9)))
    # Fraction of total price travel occurring in fully confirmed pivot legs.
    # No score saturation: reward coverage AND regularity.
    confirmed=sum(abs(s["price_delta"]) for s in swings)
    coverage=clamp(100*min(1,confirmed/max(path,1e-9)))
    capture=coverage*_consistency(pcts)/100
    if len(pcts)<4: outlier=0.0
    else:
        ordered=sorted(pcts,reverse=True)
        typical=median(pcts)
        extra=sum(max(0,x-typical) for x in ordered[:2])
        outlier=clamp(100*(1-extra/max(sum(pcts),1e-9)))
    components={
      "amplitude":_consistency(pcts),
      "peak_timing":_consistency(intervals_h),
      "trough_timing":_consistency(intervals_l),
      "alternation":purity,
      "drift_resistance":drift,
      "outlier_independence":outlier,
      "capture":capture
    }
    quality=sum(WEIGHTS[k]*v for k,v in components.items())
    return {"quality":quality,"components":components,"swings":len(swings),
            "median_swing_pct":median(pcts) if pcts else 0.0,
            "confirmed_turns":len(turns)}

def evaluate(highs,lows,closes):
    """180+ daily OHLC bars; recent window 90 bars; fail closed on missing evidence."""
    if not(len(highs)==len(lows)==len(closes)) or len(closes)<180:
        raise ValueError("Requires 180+ matching daily OHLC bars")
    highs,lows,closes=([float(x) for x in seq] for seq in (highs,lows,closes))
    if any(min(h,l,c)<=0 or l>h or not l<=c<=h for h,l,c in zip(highs,lows,closes)):
        raise ValueError("Invalid OHLC")
    if closes[-1]<3: return {"status":"REJECT_PRICE","production_eligible":False}
    threshold=min(16.0,max(6.0,2.2*atr_percent(highs,lows,closes)))
    structural=_score(highs,lows,closes,threshold)
    recent=_score(highs[-90:],lows[-90:],closes[-90:],threshold)
    blended=.75*structural["quality"]+.25*recent["quality"]
    # Reject daily flip-flop noise: confirmed pivots must have meaningful time separation.
    recent_turns=detect_turns(closes[-90:],threshold)
    pivot_intervals=[b[0]-a[0] for a,b in zip(recent_turns,recent_turns[1:])]
    minimum_cadence=median(pivot_intervals)>=3 if pivot_intervals else False
    status="CANDIDATE" if structural["swings"]>=4 and recent["median_swing_pct"]>=11 and minimum_cadence else "REJECT_CANDIDATE_GATE"
    return {"status":status,"production_eligible":False,"version":"v2.3-research",
            "threshold_pct":threshold,"structural":structural,"recent":recent,
            "candidate_score":blended,"ssot_parity_claim":False}
