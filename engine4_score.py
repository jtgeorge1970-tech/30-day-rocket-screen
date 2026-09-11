from __future__ import annotations

import math
from typing import Dict, Tuple

import numpy as np

from engine4_config import MAX_SPREAD_PCT, WEIGHTS


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, float(value)))


def score_gap(gap_pct: float) -> float:
    # Highest-quality zone is a controlled 2–10% positive gap.
    if gap_pct <= 0:
        return 0.0
    if gap_pct < 2.0:
        return 15.0 * gap_pct / 2.0
    if gap_pct <= 10.0:
        return 15.0
    if gap_pct <= 15.0:
        return 15.0 - 3.0 * (gap_pct - 10.0) / 5.0
    return max(0.0, 12.0 * (25.0 - gap_pct) / 10.0)


def score_candidate(row: dict) -> Tuple[float, Dict[str, float]]:
    catalyst = 25.0 * clamp(row["catalyst_quality"])
    rvol = 20.0 * clamp((row["premarket_rvol"] - 1.0) / 4.0) if math.isfinite(row["premarket_rvol"]) else 0.0
    gap = score_gap(row["gap_pct"])
    liquidity = 15.0 * clamp((math.log10(max(row["avg_daily_dollar_volume"], 1.0)) - 7.3) / (9.0 - 7.3))
    room = 10.0 * clamp(row["resistance_room_pct"] / 8.0)
    atr = 5.0 * clamp((row["atr_pct"] - 1.5) / (5.0 - 1.5)) if math.isfinite(row["atr_pct"]) else 0.0
    rs_input = 0.6 * row["market_relative_strength_pct"] + 0.4 * row["sector_relative_strength_pct"]
    relative_strength = 5.0 * clamp((rs_input + 1.0) / 5.0)
    spread = row["spread_pct"]
    execution = 5.0 * clamp(1.0 - spread / MAX_SPREAD_PCT) if math.isfinite(spread) else 0.0

    components = {
        "catalyst_quality": round(catalyst, 3),
        "relative_premarket_volume": round(rvol, 3),
        "gap_quality": round(gap, 3),
        "liquidity_dollar_volume": round(liquidity, 3),
        "room_to_resistance": round(room, 3),
        "atr_suitability": round(atr, 3),
        "sector_market_relative_strength": round(relative_strength, 3),
        "execution_spread": round(execution, 3),
    }
    assert set(components) == set(WEIGHTS)
    return round(sum(components.values()), 3), components


def preliminary_activity_score(gap_pct: float, premarket_dollar_volume: float, avg_daily_dollar_volume: float) -> float:
    # Fast narrowing score only; never used as the final 100-point rank.
    return (
        0.45 * np.log10(max(premarket_dollar_volume, 1.0))
        + 0.35 * min(max(gap_pct, 0.0), 15.0)
        + 0.20 * np.log10(max(avg_daily_dollar_volume, 1.0))
    )
