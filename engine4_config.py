from __future__ import annotations

from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")

TOP_N = 25
MIN_PRICE = 5.0
MAX_TRADABLE_PRICE = 100.0
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

# Engine 4 post-open hook-set / recovery watch.
# High-priced names may remain in shadow/audit rankings, but can never become
# official live trades while the account is sized at roughly $200-$300/trade.
RECOVERY_WATCH_COUNT = 5
RECOVERY_END_HOUR_ET = 11
RECOVERY_END_MINUTE_ET = 30
RECOVERY_SCAN_INTERVAL_SECONDS = 300
RECOVERY_MIN_FLUSH_PCT = 3.0
RECOVERY_MIN_BARS_SINCE_LOW = 8
RECOVERY_HIGHER_LOW_BUFFER_PCT = 0.20
RECOVERY_MAX_BASE_RANGE_PCT = 3.0
RECOVERY_MIN_GREEN_BARS = 2
RECOVERY_MIN_VOLUME_EXPANSION = 1.05
RECOVERY_TRIGGER_BUFFER_PCT = 0.05
RECOVERY_MAX_CHASE_PCT = 0.50
RECOVERY_STOP_BUFFER_PCT = 0.20
RECOVERY_MAX_EXTENSION_PCT = 8.0
RECOVERY_TARGET_R = 2.5

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
