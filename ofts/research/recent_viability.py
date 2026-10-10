"""OFTS research challenger v0.3: recent swing viability / 'fool's gold' audit.

Prevents a few large OLD swings from masquerading as CURRENT tradable
oscillations. Uses a separate 2.5%-3.5% diagnostic pivot detector so that
small recent moves are visible even when the official ZigZag threshold is
6%-16%. Never modifies the frozen v2.3 score or original BUY/SELL ledger.
All cutoffs and capture assumptions are experimental, NOT validated.
"""
from statistics import median
from ofts.research.candidate_components import detect_turns

VERSION = 'recent-viability-v0.3-experimental'
MIN_REPEATED_UP_PCT = 5.0
MIN_CONFIRMED_UP_LEGS = 3
ROUND_TRIP_COST_PCT = 0.20
CAPTURE_FRACTION = 0.50
MIN_NET_CAPTURE_PCT = 2.50
MIN_GROSS_UPSIDE_PCT = (MIN_NET_CAPTURE_PCT + ROUND_TRIP_COST_PCT) / CAPTURE_FRACTION


def _result(state, reason, **extra):
    return dict(version=VERSION, state=state, reason=reason,
                proposed_entry='NO_TRADE' if state != 'REVIEW' else 'REVIEW',
                production_approved=False, **extra)


def recent_swing_viability(closes, major_threshold_pct, lookback=252):
    """Point-in-time audit of last THREE completed swings and last THREE UP legs.

    No future bars; never treats DOWN legs as buyable upside. Uses identical
    minor-pivot threshold over old and recent legs for valid comparison.
    Requires fresh pivots and sufficient independent upside legs.
    """
    prices = [float(p) for p in closes]
    if len(prices) < 3 or any(p <= 0 for p in prices):
        return _result('INSUFFICIENT', 'INVALID_OR_SHORT_CLOSE_SERIES')
    start = max(0, len(prices)-lookback)
    micro_threshold = min(3.5, max(2.5, float(major_threshold_pct)/3))
    turns = [(i+start, k, p) for i,k,p in
             detect_turns(prices[start:], micro_threshold)]
    legs = [{'kind':'UP' if a[1]=='L' else 'DOWN',
             'start_index':a[0], 'end_index':b[0],
             'amplitude_pct':100*abs(b[2]/a[2]-1),
             'duration':b[0]-a[0]}
            for a,b in zip(turns,turns[1:])]
    recent = legs[-3:]
    older = legs[:-3]
    up = [l for l in legs if l['kind']=='UP']
    recent_up = up[-3:]
    up_values = [l['amplitude_pct'] for l in recent_up]
    up_pass_count = sum(p >= MIN_REPEATED_UP_PCT for p in up_values)
    latest_up_age = len(prices)-1-recent_up[-1]['end_index'] if recent_up else None
    up_trend = ('SHRINKING' if len(up_values)==3 and up_values[0]>up_values[1]>up_values[2]
                else 'GROWING' if len(up_values)==3 and up_values[0]<up_values[1]<up_values[2]
                else 'MIXED' if len(up_values)==3 else 'INSUFFICIENT')
    amplitudes = [l['amplitude_pct'] for l in legs]
    latest = [l['amplitude_pct'] for l in recent]
    prior = [l['amplitude_pct'] for l in older]
    recent_median = median(latest) if len(latest)==3 else None
    prior_median = median(prior) if len(prior)>=3 else None
    all_mean = sum(amplitudes)/len(amplitudes) if amplitudes else None
    all_median = median(amplitudes) if amplitudes else None
    recent_ratio = (recent_median/prior_median if prior_median and
                    recent_median is not None else None)
    top_two_share = (sum(sorted(amplitudes, reverse=True)[:2])/sum(amplitudes)
                     if len(amplitudes)>=2 and sum(amplitudes)>0 else None)
    recent_up_median = (median(l['amplitude_pct'] for l in recent_up)
                        if len(recent_up)==3 else None)
    hypothetical_net = (CAPTURE_FRACTION*recent_up_median-ROUND_TRIP_COST_PCT
                        if recent_up_median is not None else None)
    last_turn_age = len(prices)-1-turns[-1][0] if turns else None
    # Historical mean can be large despite untradeable recent bounces.
    outlier_foolsgold = bool(len(older)>=3 and top_two_share is not None and
                            top_two_share>=0.45 and recent_ratio is not None and
                            recent_ratio<0.60)
    recent_shrinking = bool(len(recent)==3 and
                            latest[0]>latest[1]>latest[2] and
                            recent_ratio is not None and recent_ratio<0.80)
    fading = bool(recent_ratio is not None and recent_ratio<0.60)
    info = dict(micro_pivot_threshold_pct=micro_threshold,
                confirmed_minor_pivots=len(turns),
                confirmed_minor_legs=len(legs),
                last_three_completed_legs=recent,
                last_three_up_legs=recent_up,
                last_three_up_pct=up_values,
                last_up_pct=up_values[-1] if up_values else None,
                repeated_up_min_pct=MIN_REPEATED_UP_PCT,
                repeated_up_pass_count=up_pass_count,
                repeated_up_required=MIN_CONFIRMED_UP_LEGS,
                up_progression=up_trend,
                latest_confirmed_up_age_sessions=latest_up_age,
                last_three_median_swing_pct=recent_median,
                earlier_median_swing_pct=prior_median,
                historical_mean_swing_pct=all_mean,
                historical_median_swing_pct=all_median,
                recent_to_earlier_ratio=recent_ratio,
                largest_two_swing_share=top_two_share,
                recent_up_median_pct=recent_up_median,
                hypothetical_net_capture_pct=hypothetical_net,
                assumed_capture_fraction=CAPTURE_FRACTION,
                assumed_round_trip_cost_pct=ROUND_TRIP_COST_PCT,
                minimum_gross_upside_pct=MIN_GROSS_UPSIDE_PCT,
                last_confirmed_pivot_age_sessions=last_turn_age,
                outlier_foolsgold=outlier_foolsgold,
                recent_shrinking=recent_shrinking)
    if len(recent)<3 or len(older)<3:
        return _result('INSUFFICIENT', 'NEED_THREE_RECENT_AND_THREE_EARLIER_LEGS', **info)
    if last_turn_age is None or last_turn_age>60 or recent[0]['end_index']<len(prices)-180:
        return _result('STALE_SWINGS', 'RECENT_COMPLETED_SWINGS_TOO_OLD', **info)
    if outlier_foolsgold:
        return _result('FOOLS_GOLD', 'OLD_OUTLIERS_DOMINATE_RECENT_TINY_SWINGS', **info)
    if len(recent_up)>=MIN_CONFIRMED_UP_LEGS and up_values[-1]<MIN_REPEATED_UP_PCT:
        return _result('TOO_SMALL_UPSIDE', 'LATEST_CONFIRMED_UP_SWING_BELOW_FIVE_PERCENT', **info)
    if recent_median<MIN_GROSS_UPSIDE_PCT:
        return _result('TOO_SMALL', 'LAST_THREE_SWINGS_NOT_ECONOMICALLY_MEANINGFUL', **info)
    if fading or recent_shrinking:
        return _result('FADING', 'RECENT_SWINGS_SHRINKING_VS_EARLIER', **info)
    if len(recent_up)<MIN_CONFIRMED_UP_LEGS:
        return _result('INSUFFICIENT_UPSIDE', 'NEED_THREE_CONFIRMED_RISING_SWINGS', **info)
    if latest_up_age is None or latest_up_age>45:
        return _result('STALE_UPSIDE', 'LATEST_CONFIRMED_RISING_SWING_TOO_OLD', **info)
    if up_pass_count<2:
        return _result('TOO_SMALL_UPSIDE', 'FEWER_THAN_TWO_OF_THREE_UP_SWINGS_ABOVE_FIVE_PERCENT', **info)
    if up_pass_count==2:
        return _result('WATCH', 'TWO_OF_THREE_UP_SWINGS_ABOVE_FIVE_PERCENT_NOT_REPEATABLE_ENOUGH', **info)
    if hypothetical_net<MIN_NET_CAPTURE_PCT:
        return _result('TOO_SMALL_UPSIDE', 'THREE_UP_SWINGS_PASS_FIVE_PERCENT_BUT_ASSUMED_NET_CAPTURE_TOO_SMALL', **info)
    return _result('REVIEW', 'THREE_REPEATED_UP_SWINGS_PASS_MINIMUM_AND_EXPERIMENTAL_ECONOMIC_GATE', **info)
