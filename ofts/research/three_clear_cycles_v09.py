"""OFTS v0.9 experimental: three clear, recent 5% peak-valley cycles.

Uses close-confirmed ZigZag 5% reversals to suppress sub-5% noise.
A cycle is LOW -> HIGH -> LOW: both its rise and fall must clear 5%.
Separately rejects exceptional loss events and persistent drawdowns.
No future data, no trade approval; thresholds require holdout calibration.
"""
from ofts.research.candidate_components import detect_turns
from statistics import median

VERSION="v0.9-three-clear-cycles-experimental"
PIVOT_PCT=5.0
MIN_LEG_PCT=5.0
MAX_CYCLE_BARS=45
MIN_CYCLE_BARS=8
MAX_LAST_TROUGH_AGE=40
MAX_ONE_DAY_LOSS_PCT=12.0
MAX_WINDOW_DRAWDOWN_PCT=25.0
LOSS_RISK_WINDOW=60
MAX_UP_OUTLIER_RATIO=3.0
MAX_SINGLE_DOWN_LEG_PCT=20.0

def three_clear_cycles(closes,lookback=126):
    p=[float(x) for x in closes]
    base=dict(version=VERSION,approved_buy=False,lookback=lookback)
    if len(p)<lookback or any(x<=0 for x in p):
        return dict(base,state="INSUFFICIENT",reason="NEED_VALID_126_CLOSES",cycles=[])
    prices=p[-lookback:]
    turns=detect_turns(prices,PIVOT_PCT)
    cycles=[]
    for a,b,c in zip(turns,turns[1:],turns[2:]):
        if (a[1],b[1],c[1])!=("L","H","L"):continue
        rise=100*(b[2]/a[2]-1)
        fall=100*(1-c[2]/b[2])
        length=c[0]-a[0]
        cycles.append(dict(trough_start_index=a[0],peak_index=b[0],
                           trough_end_index=c[0],
                           low=round(a[2],4),high=round(b[2],4),
                           next_low=round(c[2],4),
                           rise_pct=round(rise,3),fall_pct=round(fall,3),
                           cycle_sessions=length,
                           qualifies=(rise>=MIN_LEG_PCT and fall>=MIN_LEG_PCT
                                      and MIN_CYCLE_BARS<=length<=MAX_CYCLE_BARS)))
    latest=cycles[-3:]
    age=lookback-1-latest[-1]["trough_end_index"] if latest else None
    # Loss veto is CURRENT, not an ancient six-month decline that could
    # disqualify a subsequently healthy oscillator. Keep the older chart for audit.
    loss_window=prices[-LOSS_RISK_WINDOW:]
    peak=loss_window[0]
    max_dd=0.0
    for x in loss_window:
        peak=max(peak,x)
        max_dd=max(max_dd,100*(1-x/peak))
    worst_day=min(100*(b/a-1) for a,b in zip(loss_window,loss_window[1:]))
    rises=[x['rise_pct'] for x in latest]
    up_outlier_ratio=max(rises)/median(rises) if len(rises)==3 else None
    worst_completed_fall=max((x["fall_pct"] for x in latest),default=0.0)
    info=dict(base,cycles=latest,completed_cycles=len(cycles),
              qualifying_last_three=sum(x["qualifies"] for x in latest),
              last_completed_trough_age_sessions=age,
              max_drawdown_pct=round(max_dd,3),
              drawdown_window_sessions=LOSS_RISK_WINDOW,
              largest_rise_to_median_ratio=round(up_outlier_ratio,3) if up_outlier_ratio else None,
              worst_daily_return_pct=round(worst_day,3),
              largest_recent_peak_to_valley_loss_pct=round(worst_completed_fall,3))
    if worst_day<=-MAX_ONE_DAY_LOSS_PCT:
        return dict(info,state="REJECT_BIG_LOSS",reason="ONE_DAY_DROP_EXCEEDS_12_PERCENT")
    if max_dd>MAX_WINDOW_DRAWDOWN_PCT:
        return dict(info,state="REJECT_BIG_LOSS",reason="LAST_60_SESSION_DRAWDOWN_EXCEEDS_25_PERCENT")
    if len(latest)<3:
        return dict(info,state="REJECT_TOO_FEW_CYCLES",reason="FEWER_THAN_THREE_COMPLETE_LOW_HIGH_LOW_CYCLES")
    if any(x["fall_pct"]>MAX_SINGLE_DOWN_LEG_PCT for x in latest):
        return dict(info,state="REJECT_BIG_LOSS",reason="RECENT_PEAK_TO_VALLEY_DROP_EXCEEDS_20_PERCENT")
    if up_outlier_ratio is not None and up_outlier_ratio>MAX_UP_OUTLIER_RATIO:
        return dict(info,state="REJECT_ONE_OFF_SPIKE",reason="ONE_RISE_OVER_3X_TYPICAL_RECENT_RISE")
    if not all(x["qualifies"] for x in latest):
        return dict(info,state="REJECT_NOISY_OR_IRREGULAR",reason="EACH_OF_LAST_THREE_CYCLES_MUST_HAVE_5_PERCENT_UP_AND_DOWN_AND_8_TO_45_SESSIONS")
    if age>MAX_LAST_TROUGH_AGE:
        return dict(info,state="REJECT_STALE_CYCLES",reason="LATEST_COMPLETED_CYCLE_TOO_OLD")
    return dict(info,state="THREE_CLEAR_CYCLES",reason="THREE_RECENT_COMPLETE_5_PERCENT_UP_AND_DOWN_CYCLES")
