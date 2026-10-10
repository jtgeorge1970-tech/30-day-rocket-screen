"""OFTS conservative research liquidity gate, separate from cycle quality.

Historical daily OHLCV can screen traded liquidity but cannot prove current
bid/ask execution quality. A missing spread check must never approve a BUY.
"""
from statistics import median
import math

VERSION="v0.1-liquidity-research"
MIN_MEDIAN_20D_SHARES=20000
MIN_MEDIAN_20D_DOLLARS=1000000
MAX_ZERO_VOLUME_20D=1
MAX_SPREAD_PCT_FOR_BUY=2.0

def liquidity_gate(bars, bid=None, ask=None):
    base={"version":VERSION,"verified_buy_liquidity":False,
          "minimum_median_shares_20d":MIN_MEDIAN_20D_SHARES,
          "minimum_median_dollars_20d":MIN_MEDIAN_20D_DOLLARS}
    if len(bars)<20:
        return dict(base,state="INSUFFICIENT_LIQUIDITY_HISTORY")
    w=bars[-20:]
    try:
        vols=[float(x["volume"]) for x in w]
        closes=[float(x["close"]) for x in w]
        if any(not math.isfinite(v) or v<0 for v in vols) or any(not math.isfinite(c) or c<=0 for c in closes):
            return dict(base,state="INVALID_LIQUIDITY_DATA")
    except (KeyError,ValueError,TypeError):
        return dict(base,state="INVALID_LIQUIDITY_DATA")
    shares=median(vols)
    dollars=median(v*c for v,c in zip(vols,closes))
    zero_days=sum(v==0 for v in vols)
    info=dict(base,median_20d_shares=round(shares),median_20d_dollar_volume=round(dollars),
              zero_volume_days_20d=zero_days)
    if (shares<MIN_MEDIAN_20D_SHARES or dollars<MIN_MEDIAN_20D_DOLLARS
        or zero_days>MAX_ZERO_VOLUME_20D):
        return dict(info,state="REJECT_LOW_LIQUIDITY")
    if bid is None or ask is None:
        return dict(info,state="LIQUIDITY_HISTORY_PASS_SPREAD_UNVERIFIED")
    if not (0<bid<=ask):
        return dict(info,state="REJECT_INVALID_QUOTE")
    spread=100*(ask-bid)/((ask+bid)/2)
    info["bid_ask_spread_pct"]=round(spread,3)
    if spread>MAX_SPREAD_PCT_FOR_BUY:
        return dict(info,state="REJECT_WIDE_SPREAD")
    return dict(info,state="LIQUIDITY_PASS",verified_buy_liquidity=True)
