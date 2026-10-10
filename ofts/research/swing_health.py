"""OFTS experimental, point-in-time swing-health diagnostic v0.1.

Independent of the locked v2.3 quality score and the original research
BUY/SELL states. Proposed trade-readiness classifications are hypotheses,
NOT approved production orders or calibrated probabilities.
"""
from statistics import median
from ofts.research.candidate_components import detect_turns


def _relative_mad(values):
    if len(values) < 3:
        return None
    center = median(values)
    return median(abs(x - center) for x in values) / max(abs(center), 1e-9)


def _direction(prices):
    """Two successive lower (or higher) pivot comparisons, not one noise bar."""
    if len(prices) < 3:
        return 'INSUFFICIENT'
    a, b, c = prices[-3:]
    if a > b > c:
        return 'FALLING'
    if a < b < c:
        return 'RISING'
    return 'MIXED'


def recent_swing_health(closes, threshold_pct, recent_bars=90):
    """Assess ONLY fully confirmed ZigZag pivots in an as-of close series.

    Output contains last-four leg amplitudes/durations, high/low progressions,
    shrinking/irregular cycle warnings and a separately labelled experimental
    entry gate. No later bars are read. Current unconfirmed extreme is excluded.
    """
    prices = [float(x) for x in closes]
    if len(prices) < 3:
        return {'version': 'swing-health-v0.1-experimental',
                'state': 'INSUFFICIENT', 'proposed_entry': 'NO_TRADE',
                'reason': 'TOO_FEW_BARS', 'production_approved': False}
    offset = max(0, len(prices) - recent_bars)
    turns = [(i + offset, k, p) for i, k, p in
             detect_turns(prices[offset:], threshold_pct)]
    highs = [t for t in turns if t[1] == 'H']
    lows = [t for t in turns if t[1] == 'L']
    legs = [{'kind': 'UP' if a[1] == 'L' else 'DOWN',
             'start_index': a[0], 'end_index': b[0],
             'duration': b[0] - a[0],
             'amplitude_pct': 100 * abs(b[2] / a[2] - 1)}
            for a, b in zip(turns, turns[1:])]
    latest = legs[-4:]
    older = legs[-8:-4]
    amps = [r['amplitude_pct'] for r in latest]
    durations = [r['duration'] for r in latest]
    amplitude_mad = _relative_mad(amps)
    cadence_mad = _relative_mad(durations)
    older_median = median(r['amplitude_pct'] for r in older) if len(older) == 4 else None
    latest_median = median(amps) if len(amps) == 4 else None
    shrink_ratio = (latest_median / older_median
                    if older_median and latest_median is not None else None)
    # Need 3 highs, 3 lows and 4 recent complete legs for meaningful
    # recent swing + structural direction conclusions.
    enough = len(latest) == 4 and len(highs) >= 3 and len(lows) >= 3
    high_direction = _direction([r[2] for r in highs])
    low_direction = _direction([r[2] for r in lows])
    downward_structure = high_direction == low_direction == 'FALLING'
    upward_structure = high_direction == low_direction == 'RISING'
    decaying = shrink_ratio is not None and shrink_ratio < 0.70
    irregular = (amplitude_mad is not None and amplitude_mad > 0.35 or
                 cadence_mad is not None and cadence_mad > 0.45)
    # Weak recovery relative to prior complete rising legs, only if a
    # fully confirmed up leg exists. Otherwise don't infer a recovery.
    rising = [r['amplitude_pct'] for r in legs if r['kind'] == 'UP']
    weak_recovery = (len(rising) >= 3 and latest and
                     latest[-1]['kind'] == 'UP' and
                     latest[-1]['amplitude_pct'] < 0.60 * median(rising[:-1]))
    if not enough:
        state, proposed, reason = 'INSUFFICIENT', 'NO_TRADE', 'NEED_3_HIGHS_3_LOWS_4_LEGS'
    elif decaying:
        state, proposed, reason = 'DECAYING', 'NO_TRADE', 'RECENT_SWING_AMPLITUDE_SHRINKING'
    elif irregular:
        state, proposed, reason = 'IRREGULAR', 'NO_TRADE', 'RECENT_AMPLITUDE_OR_CADENCE_UNSTABLE'
    elif downward_structure and weak_recovery:
        state, proposed, reason = 'DOWNTREND_WEAK_BOUNCE', 'NO_TRADE', 'LOWER_HIGHS_LOWER_LOWS_WEAK_BOUNCE'
    elif downward_structure:
        state, proposed, reason = 'DOWNTREND', 'REVIEW', 'LOWER_HIGHS_LOWER_LOWS_RISK'
    elif upward_structure:
        state, proposed, reason = 'STABLE_UPTREND', 'REVIEW', 'CHECK_ENTRY_TIMING'
    else:
        state, proposed, reason = 'STABLE_RANGE', 'REVIEW', 'CHECK_ENTRY_TIMING'
    return {'version': 'swing-health-v0.1-experimental',
            'state': state, 'proposed_entry': proposed, 'reason': reason,
            'production_approved': False,
            'confirmed_turns_recent': len(turns),
            'recent_completed_legs': len(latest),
            'last_four_legs': latest,
            'recent_median_amplitude_pct': latest_median,
            'prior_four_median_amplitude_pct': older_median,
            'recent_to_prior_amplitude_ratio': shrink_ratio,
            'recent_amplitude_relative_mad': amplitude_mad,
            'recent_duration_relative_mad': cadence_mad,
            'last_three_highs': [r[2] for r in highs[-3:]],
            'last_three_lows': [r[2] for r in lows[-3:]],
            'high_progression': high_direction,
            'low_progression': low_direction,
            'downward_structure': downward_structure,
            'weak_recovery': bool(weak_recovery),
            'decaying': bool(decaying),
            'irregular': bool(irregular)}
