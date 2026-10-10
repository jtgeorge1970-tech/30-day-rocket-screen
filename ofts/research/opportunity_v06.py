"""OFTS v0.6 experimental opportunity ranking; independent of frozen v2.3 scores.

80/100 observable points only. Never impute entry readiness, liquidity, or
market capitalization. A research rank is not a verified-eligible trading rank.
"""
from statistics import median

VERSION = "v0.6-opportunity-experimental"
MAX_MEASURED = 80.0

def _unit(value):
    return max(0.0, min(1.0, float(value)))

def _regularity(values):
    if len(values) != 3 or min(values) <= 0:
        return None
    center = median(values)
    return _unit(1.0 - median(abs(x - center) for x in values) / center)

def opportunity_partial(viability, health):
    """Use only as-of confirmed legs; no future price, cap or volume inference."""
    ups = viability.get("last_three_up_pct") or []
    peaks = viability.get("last_three_peak_to_peak_sessions") or []
    troughs = viability.get("last_three_trough_to_trough_sessions") or []
    if len(ups) != 3 or min(ups) <= 0:
        return {"version": VERSION, "status": "INSUFFICIENT", "measured_score": None,
                "reason": "NEED_THREE_COMPLETED_UP_LEGS", "production_approved": False}
    repeat = _regularity(ups)
    peak_reg, trough_reg = _regularity(peaks), _regularity(troughs)
    if repeat is None or peak_reg is None or trough_reg is None:
        return {"version": VERSION, "status": "INSUFFICIENT", "measured_score": None,
                "reason": "NEED_THREE_VALID_PEAK_AND_TROUGH_GAPS", "production_approved": False}
    swing_median = median(ups)
    components = {
        "repeatability_25": 25 * repeat,
        "upside_20": 20 * _unit(swing_median / 15.0),
        "timing_15": 7.5 * (peak_reg + trough_reg),
    }
    deductions = {}
    if ups[0] > ups[1] > ups[2]:
        deductions["three_shrinking_ups"] = 8
    if health.get("state") in ("DOWNTREND", "DOWNTREND_WEAK_BOUNCE"):
        deductions["lower_highs_and_lows"] = 7
    cadence_ratio = viability.get("recent_vs_prior_cadence_ratio")
    if cadence_ratio is not None and cadence_ratio >= 1.4:
        deductions["slowing_cadence"] = 4
    if ups[-1] < 0.70 * swing_median:
        deductions["latest_bounce_weak"] = 4
    if max(ups) > 3 * swing_median:
        deductions["one_large_up_outlier"] = 4
    components["health_20"] = max(0.0, 20.0 - sum(deductions.values()))
    measured = sum(components.values())
    return {"version": VERSION, "status": "PARTIAL_RESEARCH_ONLY",
            "measured_score": round(measured, 4), "measured_max": 80,
            "missing_points": 20, "entry_points": None,
            "execution_points": None, "eligibility_score": None,
            "eligibility_status": "PENDING_ELIGIBILITY",
            "production_approved": False,
            "components": {k: round(v, 4) for k, v in components.items()},
            "health_deductions": deductions,
            "reason": "NO_ASOF_MARKET_CAP_SPREAD_OR_ENTRY_METRICS"}
