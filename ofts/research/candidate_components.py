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
