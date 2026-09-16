import math

import pandas as pd

import engine4_recovery as recovery


def _fps_style_frame():
    idx = pd.date_range("2026-09-16 09:30", periods=30, freq="1min", tz="America/New_York")
    opens = [34.10, 34.40, 33.60, 33.10] + [33.60] * 17 + [33.62, 33.70, 33.82, 33.76, 33.88, 33.92, 34.02, 34.00, 34.10]
    closes = [34.30, 33.70, 33.15, 33.55] + [33.70] * 17 + [33.68, 33.78, 33.75, 33.85, 33.82, 33.98, 34.00, 34.12, 34.18]
    highs = [34.49, 34.42, 33.70, 33.65] + [33.78] * 17 + [33.75, 33.84, 33.88, 33.90, 33.95, 34.05, 34.08, 34.22, 34.30]
    lows = [34.00, 33.60, 33.00, 33.40] + [33.55] * 17 + [33.60, 33.65, 33.68, 33.70, 33.75, 33.80, 33.88, 33.95, 34.00]
    volumes = [800000, 500000, 400000, 300000] + [50000] * 17 + [50000, 50000, 50000, 50000, 50000, 120000, 130000, 140000, 150000]
    return pd.DataFrame({"Open": opens, "High": highs, "Low": lows, "Close": closes, "Volume": volumes}, index=idx)


def test_fps_style_extended_recovery_fails_closed(monkeypatch):
    monkeypatch.setattr(recovery, "_current_mid", lambda symbol: (33.84, 33.80, 33.88, 0.24))
    metrics = recovery.recovery_metrics(
        "FPS",
        _fps_style_frame(),
        pd.Timestamp("2026-09-16").date(),
        previous_close=31.36,
    )
    assert metrics["entry_trigger"] > metrics["session_high"]
    assert "recovery_entry_excessively_extended" in metrics["failures"]
    assert metrics["setup_ready"] is False
    assert metrics["state"] == "WATCH"


def test_max_fill_preserves_two_to_one_reward_risk(monkeypatch):
    monkeypatch.setattr(recovery, "_current_mid", lambda symbol: (33.84, 33.80, 33.88, 0.24))
    metrics = recovery.recovery_metrics(
        "SAFE",
        _fps_style_frame(),
        pd.Timestamp("2026-09-16").date(),
        previous_close=33.00,
    )
    assert metrics["entry_trigger"] > metrics["session_high"]
    assert metrics["max_allowed_buy_price"] <= metrics["raw_max_allowed_buy_price"]
    assert math.isclose(metrics["reward_risk_at_max_fill"], 2.0, rel_tol=1e-9)
    assert "insufficient_reward_risk_at_max_fill" not in metrics["failures"]


def test_missing_previous_close_fails_closed(monkeypatch):
    monkeypatch.setattr(recovery, "_current_mid", lambda symbol: (33.84, 33.80, 33.88, 0.24))
    metrics = recovery.recovery_metrics(
        "TEST",
        _fps_style_frame(),
        pd.Timestamp("2026-09-16").date(),
    )
    assert "missing_previous_close_for_extension" in metrics["failures"]
    assert metrics["setup_ready"] is False
