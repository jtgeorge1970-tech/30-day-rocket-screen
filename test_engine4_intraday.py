import math
from pathlib import Path

import numpy as np
import pandas as pd

import engine4_config as cfg
import engine4_intraday as e4
import engine4_live as live
import engine4_score as score


def test_locked_constants():
    assert cfg.TOP_N == 25
    assert cfg.MIN_PRICE == 5.0
    assert cfg.MIN_MARKET_CAP == 300_000_000.0
    assert cfg.MIN_REWARD_RISK == 2.0
    assert cfg.MIN_SCORE == 70.0
    assert cfg.MAX_SPREAD_PCT == 0.60
    assert sum(cfg.WEIGHTS.values()) == 100.0


def test_premarket_score_strong_candidate():
    row = {
        "catalyst_quality": 1.0,
        "premarket_rvol": 5.0,
        "gap_pct": 6.0,
        "avg_daily_dollar_volume": 1_000_000_000.0,
        "resistance_room_pct": 8.0,
        "atr_pct": 5.0,
        "market_relative_strength_pct": 3.0,
        "sector_relative_strength_pct": 3.0,
        "spread_pct": 0.05,
    }
    total, components = score.score_candidate(row)
    assert total > 90
    assert abs(sum(components.values()) - total) < 0.01
    assert set(components) == set(cfg.WEIGHTS)


def test_no_catalyst_cannot_receive_perfect_score():
    row = {
        "catalyst_quality": 0.0,
        "premarket_rvol": 6.0,
        "gap_pct": 6.0,
        "avg_daily_dollar_volume": 2_000_000_000.0,
        "resistance_room_pct": 10.0,
        "atr_pct": 6.0,
        "market_relative_strength_pct": 4.0,
        "sector_relative_strength_pct": 4.0,
        "spread_pct": 0.02,
    }
    total, _ = score.score_candidate(row)
    assert total <= 75.0


def make_opening_frame():
    idx = pd.date_range("2026-09-10 09:30", periods=15, freq="1min", tz="America/New_York")
    close = [10.00,10.04,10.08,10.12,10.16,10.14,10.13,10.14,10.15,10.16,10.17,10.18,10.19,10.20,10.21]
    high = [x + 0.03 for x in close]
    low = [x - 0.03 for x in close]
    volume = [1000,950,900,850,800,500,450,420,400,380,450,500,650,800,1000]
    return pd.DataFrame({"Open":close,"High":high,"Low":low,"Close":close,"Volume":volume}, index=idx)


def test_vwap_math():
    frame = pd.DataFrame({"High":[10,11],"Low":[9,10],"Close":[9.5,10.5],"Volume":[100,100]})
    assert math.isclose(live.vwap(frame), 10.0, rel_tol=1e-9)


def test_live_full_a_plus_path_passes(monkeypatch):
    monkeypatch.setattr(live, "quote_spread", lambda ticker: (10.20, 10.21, 0.0979))
    frame = make_opening_frame()
    row = pd.Series({"sector":"Technology","resistance_price":11.50})
    market = {
        "SPY_ret":0.05,"QQQ_ret":0.08,"XLK_ret":0.05,
        "SPY_last5_ret":0.02,"QQQ_last5_ret":0.03,
    }
    metrics = live.opening_structure("TEST", frame, row, market, pd.Timestamp("2026-09-10").date())
    assert metrics["data_ok"]
    assert metrics["entry_trigger"] > 0
    assert metrics["initial_stop"] < metrics["entry_trigger"]
    assert metrics["reward_risk"] >= 2.0
    assert metrics["relative_strength_market_pct"] > 0
    assert metrics["relative_strength_sector_pct"] > 0
    assert metrics["failures"] == []
    assert metrics["pass"] is True


def test_live_fails_wide_spread(monkeypatch):
    monkeypatch.setattr(live, "quote_spread", lambda ticker: (10.00, 10.20, 1.98))
    frame = make_opening_frame()
    row = pd.Series({"sector":"Technology","resistance_price":11.50})
    market = {
        "SPY_ret":0.05,"QQQ_ret":0.08,"XLK_ret":0.05,
        "SPY_last5_ret":0.02,"QQQ_last5_ret":0.03,
    }
    metrics = live.opening_structure("TEST", frame, row, market, pd.Timestamp("2026-09-10").date())
    assert "spread" in metrics["failures"]
    assert not metrics["pass"]


def test_live_fails_hard_market_reversal(monkeypatch):
    monkeypatch.setattr(live, "quote_spread", lambda ticker: (10.20, 10.21, 0.0979))
    frame = make_opening_frame()
    row = pd.Series({"sector":"Technology","resistance_price":11.50})
    market = {
        "SPY_ret":-0.80,"QQQ_ret":-0.90,"XLK_ret":-0.75,
        "SPY_last5_ret":-0.20,"QQQ_last5_ret":-0.25,
    }
    metrics = live.opening_structure("TEST", frame, row, market, pd.Timestamp("2026-09-10").date())
    assert "broad_market_hard_reversal" in metrics["failures"]
    assert not metrics["pass"]


def test_final_fail_closed_without_top25(tmp_path, monkeypatch):
    monkeypatch.setattr(e4, "OUT", tmp_path)
    result = e4.final_stage()
    assert result["status"] == "NO_TRADE"
    assert "Top 25 unavailable" in result["message"]
    assert (tmp_path / "final_alert.txt").exists()


def test_self_test():
    e4.self_test()
