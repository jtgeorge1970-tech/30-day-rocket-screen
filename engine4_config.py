from __future__ import annotations

from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")

TOP_N = 25
MIN_PRICE = 5.0
MIN_MARKET_CAP = 300_000_000.0
MIN_DOLLAR_VOLUME = 20_000_000.0
MIN_PREMARKET_DOLLAR_VOLUME = 500_000.0
MIN_PREMARKET_RVOL = 1.5
MIN_ATR_PCT = 1.5
MIN_SCORE = 70.0
MIN_REWARD_RISK = 2.0
MAX_GAP_PCT = 25.0
MIN_GAP_PCT = 0.5
MAX_SPREAD_PCT = 0.60
MAX_VWAP_EXTENSION_PCT = 1.50
MAX_BREAKOUT_CHASE_PCT = 0.50
MIN_BREAKOUT_VOLUME_RATIO = 1.20
MAX_PULLBACK_VOLUME_RATIO = 0.85
HARD_MARKET_REVERSAL_PCT = -0.60
BROAD_POOL_SIZE = 100
DEEP_POOL_SIZE = 60
YAHOO_RATE_CAP_PER_MINUTE = 100
BATCH_SIZE_BROAD = 50
BATCH_SIZE_DEEP = 25

WEIGHTS = {
    "catalyst_quality": 25.0,
    "relative_premarket_volume": 20.0,
    "gap_quality": 15.0,
    "liquidity_dollar_volume": 15.0,
    "room_to_resistance": 10.0,
    "atr_suitability": 5.0,
    "sector_market_relative_strength": 5.0,
    "execution_spread": 5.0,
}

SECTOR_ETF = {
    "Technology": "XLK",
    "Healthcare": "XLV",
    "Financial Services": "XLF",
    "Consumer Cyclical": "XLY",
    "Communication Services": "XLC",
    "Industrials": "XLI",
    "Consumer Defensive": "XLP",
    "Energy": "XLE",
    "Basic Materials": "XLB",
    "Real Estate": "XLRE",
    "Utilities": "XLU",
}

assert abs(sum(WEIGHTS.values()) - 100.0) < 1e-9
