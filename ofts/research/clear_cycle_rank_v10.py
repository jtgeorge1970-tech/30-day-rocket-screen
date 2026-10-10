"""Experimental v0.10 rank of independently clear cycles.

Does not inherit legacy shortlist or v0.6 quality ordering.
Old model state is a diagnostic, not a hidden hard veto.
Not a predictive probability or actionable BUY signal.
"""
from statistics import median

VERSION="v0.10-clean-cycle-research"
def clip(x):
    return max(0.0,min(1.0,float(x)))

def regularity(values):
    if len(values)!=3 or min(values)<=0:
        return 0.0
    m=median(values)
    return clip(1-median(abs(x-m) for x in values)/m)

def score_clear_cycles(clear, eligibility="PENDING_ELIGIBILITY"):
    if clear.get("state")!="THREE_CLEAR_CYCLES":
        return {"version":VERSION,"score":None,"status":"NOT_QUALIFIED"}
    cycles=clear["cycles"]
    rises=[c["rise_pct"] for c in cycles]
    falls=[c["fall_pct"] for c in cycles]
    spans=[c["cycle_sessions"] for c in cycles]
    efficiencies=[e for c in cycles for e in
                  (c["rise_path_efficiency"],c["fall_path_efficiency"])]
    age=clear["last_completed_trough_age_sessions"]
    parts={
        "amplitude_consistency_25":25*(regularity(rises)+regularity(falls))/2,
        "cycle_timing_consistency_20":20*regularity(spans),
        "median_path_smoothness_25":25*median(efficiencies),
        "worst_leg_smoothness_10":10*min(efficiencies),
        "typical_upside_15":15*clip(median(rises)/15),
        "cycle_freshness_5":5*clip(1-age/40),
    }
    raw=sum(parts.values())
    eligibility_penalty=0 if eligibility=="PASS" else 8 if eligibility=="PENDING_ELIGIBILITY" else 100
    result=max(0,raw-eligibility_penalty)
    return {"version":VERSION,"score":round(result,3),
            "raw_score":round(raw,3),
            "eligibility_penalty":eligibility_penalty,
            "status":"RESEARCH_ONLY" if eligibility!="INELIGIBLE" else "INELIGIBLE",
            "components":{k:round(v,3) for k,v in parts.items()},
            "median_rise_pct":round(median(rises),3),
            "median_fall_pct":round(median(falls),3),
            "median_cycle_sessions":round(median(spans),3),
            "median_path_efficiency":round(median(efficiencies),3),
            "worst_path_efficiency":round(min(efficiencies),3),
            "last_trough_age_sessions":age}
