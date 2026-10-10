"""OFTS v0.7: as-of freshness and present-price entry diagnostic.

Not a BUY predictor. All decisions use closes available at the as-of date.
Confirmed completed swings remain separate from live unfinished price action.
"""
from datetime import date
from statistics import median

VERSION="entry-diagnostic-v0.7-experimental"

def entry_diagnostic(closes, dates, *, today=None):
    prices=[float(x) for x in closes]
    if len(prices)<25 or len(dates)!=len(prices) or any(x<=0 for x in prices):
        return dict(version=VERSION,state="INSUFFICIENT_DATA",entry_points=None,entry_confirmed=False)
    asof=str(dates[-1])[:10]
    now=today or date.today()
    try:
        age=(now-date.fromisoformat(asof)).days
    except ValueError:
        return dict(version=VERSION,state="INVALID_ASOF_DATE",entry_points=None,entry_confirmed=False)
    last=prices[-1]
    five=100*(last/prices[-6]-1)
    twenty=100*(last/prices[-21]-1)
    prior20low=min(prices[-21:-1])
    prior20high=max(prices[-21:-1])
    band=(last-prior20low)/(prior20high-prior20low) if prior20high>prior20low else None
    drawdown=100*(last/prior20high-1)
    two_day_recovery=prices[-1]>prices[-2]>prices[-3]
    broke_support=last<prior20low
    # An unconfirmed selloff must never be described as a confirmed trough.
    if age<0 or age>5:
        state="STALE_DATA"
    elif broke_support:
        state="BREAKDOWN_NO_TRADE"
    elif five<=-4 or (drawdown<=-6 and not two_day_recovery):
        state="FALLING_WAIT"
    elif band is None:
        state="INSUFFICIENT_RANGE"
    elif band>=0.80:
        state="CHASE_RISK_WAIT"
    elif band<=0.35 and not two_day_recovery:
        state="UNCONFIRMED_TROUGH_WAIT"
    elif band<=0.55 and two_day_recovery and five>0:
        state="REVERSAL_REVIEW"
    else:
        state="MID_CYCLE_WAIT"
    # No numeric entry score until as-of freshness and trade execution are validated.
    return dict(version=VERSION,state=state,entry_points=None,
                entry_confirmed=(state=="REVERSAL_REVIEW"),
                asof_date=asof,calendar_age_days=age,close=last,
                return_5_sessions_pct=round(five,3),
                return_20_sessions_pct=round(twenty,3),
                prior_20_close_low=round(prior20low,4),
                prior_20_close_high=round(prior20high,4),
                position_in_prior20_band=round(band,4) if band is not None else None,
                drawdown_from_prior20high_pct=round(drawdown,3),
                two_day_recovery=two_day_recovery,
                broke_prior20_close_low=broke_support,
                production_approved=False)
