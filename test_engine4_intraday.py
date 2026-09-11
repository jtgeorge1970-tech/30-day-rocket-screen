import json
from pathlib import Path
import pandas as pd
import numpy as np

import engine4_intraday as e4


def test_locked_constants():
    assert e4.TOP_N == 25
    assert e4.MIN_PRICE == 5.0
    assert e4.MIN_MARKET_CAP == 300_000_000
    assert e4.MIN_RR == 2.0
    assert sum(e4.WEIGHTS.values()) == 100.0


def test_math_helpers():
    assert round(e4.pct(105, 100), 6) == 5.0
    assert np.isnan(e4.pct(1, 0))
    assert e4.clamp(-1) == 0.0
    assert e4.clamp(2) == 1.0


def test_final_fail_closed_without_top25(tmp_path, monkeypatch):
    monkeypatch.setattr(e4, "OUT", tmp_path)
    result = e4.final_scan()
    assert result["action"] == "NO_TRADE"
    assert "Top 25 unavailable" in result["message"]


def test_score_balance_rule_formula():
    # Sanity-check the intended score is a 100-point framework.
    assert e4.WEIGHTS == {
        "catalyst": 25.0,
        "premarket_rvol": 20.0,
        "gap_quality": 15.0,
        "liquidity": 15.0,
        "resistance_room": 10.0,
        "atr": 5.0,
        "relative_strength": 5.0,
        "execution": 5.0,
    }


if __name__ == "__main__":
    test_locked_constants()
    test_math_helpers()
    e4.self_test()
    print("ENGINE4_TESTS_PASS")
