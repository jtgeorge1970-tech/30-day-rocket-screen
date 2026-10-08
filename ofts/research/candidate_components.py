"""OFTS Stage-2 candidate scoring math. NOT approved locked v2.2 production logic.

All functions are deterministic and dependency-free. Explicit candidate assumptions
must pass historical control regression and owner approval before promotion.
"""
from statistics import median

WEIGHTS={"amplitude":.20,"peak_timing":.10,"trough_timing":.10,
         "alternation":.15,"drift_resistance":.15,"outlier_independence":.10,
         "capture":.20}

def clamp(x): return max(0.0,min(100.0,float(x)))

def robust_consistency(values):
    """CANDIDATE: score via median absolute deviation / median."""
    values=[float(v) for v in values if v is not None and float(v)>0]
    if len(values)<3: return 0.0
    center=median(values)
    mad=median(abs(v-center) for v in values)
    return clamp(100*(1-mad/max(center,1e-9)))

def alternation_purity(kinds):
    """CANDIDATE: adjacent turning points should alternate H/L."""
    if len(kinds)<3: return 0.0
    return clamp(100*sum(a!=b for a,b in zip(kinds,kinds[1:]))/(len(kinds)-1))

def outlier_independence(swings):
    """CANDIDATE: robustly penalize top two oversized swings."""
    vals=sorted((abs(float(x)) for x in swings),reverse=True)
    if len(vals)<4: return 0.0
    typical=median(vals)
    excess=sum(max(0,v-typical) for v in vals[:2])
    return clamp(100*(1-excess/max(sum(vals),1e-9)))

def drift_resistance(closes,swings):
    """CANDIDATE: net displacement relative to traversed swing movement."""
    if len(closes)<2 or not swings: return 0.0
    displacement=abs(float(closes[-1])-float(closes[0]))
    traveled=sum(abs(float(x)) for x in swings)
    return clamp(100*(1-displacement/max(traveled,1e-9)))

def oscillation_capture(swings,closes):
    """CANDIDATE: pivot movement divided by full close-to-close path."""
    if len(closes)<2: return 0.0
    path=sum(abs(float(b)-float(a)) for a,b in zip(closes,closes[1:]))
    return clamp(100*sum(abs(float(x)) for x in swings)/max(path,1e-9))

def weighted_quality(components):
    missing=set(WEIGHTS)-set(components)
    if missing: raise ValueError(f"Missing components: {sorted(missing)}")
    return sum(WEIGHTS[k]*clamp(components[k]) for k in WEIGHTS)

def blend(structural,recent):
    return .75*float(structural)+.25*float(recent)

def atr_percent(highs,lows,closes,period=14):
    """Candidate median true-range percent of close, over the latest period."""
    n=len(closes)
    if len(highs)!=n or len(lows)!=n or n<period+1:
        raise ValueError("OHLC lengths mismatch or insufficient history")
    ranges=[]
    for i in range(1,n):
        h,l,c,prev=map(float,(highs[i],lows[i],closes[i],closes[i-1]))
        if min(h,l,c,prev)<=0 or h<l: raise ValueError("Invalid OHLC bar")
        ranges.append(100*max(h-l,abs(h-prev),abs(l-prev))/prev)
    return median(ranges[-period:])

def adaptive_threshold(highs,lows,closes):
    """CURRENT TEST, NOT LOCKED: 2.2 x median ATR%, bounded 6%-16%."""
    return min(16.0,max(6.0,2.2*atr_percent(highs,lows,closes)))

def detect_turns(closes,threshold_pct):
    """Candidate percentage-reversal ZigZag, confirmed turns only.

    Each pivot is (index, 'H'|'L', price); never uses a future pivot
    without the requisite reversal. The last unconfirmed extreme is omitted.
    """
    prices=[float(x) for x in closes]
    if len(prices)<3 or any(x<=0 for x in prices):
        raise ValueError("At least 3 positive closes required")
    if not 0<float(threshold_pct)<100: raise ValueError("Invalid threshold")
    threshold=float(threshold_pct)/100
    turns=[]
    low_i=high_i=0
    low=high=prices[0]
    direction=0
    for i,p in enumerate(prices[1:],1):
        if direction==0:
            if p<low: low,low_i=p,i
            if p>high: high,high_i=p,i
            if low_i<high_i and high/low-1>=threshold:
                turns.append((low_i,"L",low))
                direction=1
                high,high_i=p,i
            elif high_i<low_i and 1-low/high>=threshold:
                turns.append((high_i,"H",high))
                direction=-1
                low,low_i=p,i
        elif direction==1:
            if p>high: high,high_i=p,i
            elif 1-p/high>=threshold:
                turns.append((high_i,"H",high))
                direction=-1
                low,low_i=p,i
        else:
            if p<low: low,low_i=p,i
            elif p/low-1>=threshold:
                turns.append((low_i,"L",low))
                direction=1
                high,high_i=p,i
    return turns

def swing_features(turns):
    """Candidate swing percentages and same-side timing intervals."""
    swings=[]
    for a,b in zip(turns,turns[1:]):
        if a[1]==b[1] or b[0]<=a[0]: raise ValueError("Invalid pivot sequence")
        swings.append({"start":a[0],"end":b[0],"kind":"UP" if a[1]=="L" else "DOWN",
                       "pct":100*abs(b[2]/a[2]-1),"price_delta":b[2]-a[2]})
    highs=[p[0] for p in turns if p[1]=="H"]
    lows=[p[0] for p in turns if p[1]=="L"]
    return {"swings":swings,"peak_intervals":[b-a for a,b in zip(highs,highs[1:])],
            "trough_intervals":[b-a for a,b in zip(lows,lows[1:])]}

def candidate_components(highs,lows,closes):
    """All seven candidate scores; does not imply locked v2.2 equivalence."""
    turns=detect_turns(closes,adaptive_threshold(highs,lows,closes))
    features=swing_features(turns)
    swings=features["swings"]
    pcts=[x["pct"] for x in swings]
    deltas=[x["price_delta"] for x in swings]
    scores={"amplitude":robust_consistency(pcts),
            "peak_timing":robust_consistency(features["peak_intervals"]),
            "trough_timing":robust_consistency(features["trough_intervals"]),
            "alternation":alternation_purity([x[1] for x in turns]),
            "drift_resistance":drift_resistance(closes,deltas),
            "outlier_independence":outlier_independence(pcts),
            "capture":oscillation_capture(deltas,closes)}
    saturated = scores["alternation"] >= 99.99 or scores["capture"] >= 99.99
    return {"turns":turns,"features":features,"components":scores,
            "structural_quality":weighted_quality(scores),
            "production_eligible":False,
            "reason":"Candidate not parity validated; mechanically inflated components" if saturated else "Candidate not parity validated"}

def diagnostic_components(highs,lows,closes):
    """Research-only: exposes unvalidated metrics and saturation warnings.

    Deliberately does NOT issue a replacement v2.2 score.
    """
    result=candidate_components(highs,lows,closes)
    comp=result["components"]
    warnings=[]
    if comp["alternation"]>=99.99:
        warnings.append("alternation_mechanically_perfect_under_zigzag")
    if comp["capture"]>=99.99:
        warnings.append("capture_saturated")
    if len(result["features"]["swings"])<4:
        warnings.append("insufficient_swings_for_outlier_component")
    return {"components":comp,"warnings":warnings,
            "confirmed_swings":len(result["features"]["swings"]),
            "candidate_structural":result["structural_quality"],
            "approved_v22_score":None}
