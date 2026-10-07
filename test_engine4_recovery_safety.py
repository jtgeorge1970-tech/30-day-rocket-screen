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


def test_frozen_recovery_trigger_does_not_ratchet_with_new_highs(monkeypatch):
    monkeypatch.setattr(recovery, "_current_mid", lambda symbol: (34.40, 34.38, 34.42, 0.12))
    frame = _fps_style_frame()
    frozen = 34.50

    first = recovery.recovery_metrics(
        "FIXED",
        frame,
        pd.Timestamp("2026-09-16").date(),
        previous_close=33.00,
        frozen_entry_trigger=frozen,
    )
    assert math.isclose(first["entry_trigger"], frozen, rel_tol=1e-12)
    assert first["trigger_frozen"] is True

    # Add two later bars with materially higher highs. The dynamic candidate line
    # is allowed to rise, but the executable trigger must remain frozen.
    last = frame.index[-1]
    extra_idx = pd.date_range(last + pd.Timedelta(minutes=1), periods=2, freq="1min", tz="America/New_York")
    extra = pd.DataFrame({
        "Open": [34.60, 35.05],
        "High": [35.00, 35.40],
        "Low": [34.45, 34.90],
        "Close": [34.90, 35.20],
        "Volume": [180000, 220000],
    }, index=extra_idx)
    extended = pd.concat([frame, extra])

    second = recovery.recovery_metrics(
        "FIXED",
        extended,
        pd.Timestamp("2026-09-16").date(),
        previous_close=33.00,
        frozen_entry_trigger=frozen,
    )
    assert second["candidate_entry_trigger"] > frozen
    assert math.isclose(second["entry_trigger"], frozen, rel_tol=1e-12)
    assert second["trigger_frozen"] is True


def test_recovery_monitor_checks_each_minute():
    assert recovery.RECOVERY_SCAN_INTERVAL_SECONDS == 60


def _continuation_frame():
    idx = pd.date_range("2026-10-07 09:30", periods=30, freq="1min", tz="America/New_York")
    closes = [
        48.10,48.05,47.98,47.92,47.86,47.82,47.88,47.94,47.98,48.02,
        48.00,48.04,48.08,48.06,48.10,48.12,48.14,48.13,48.16,48.18,
        48.17,48.19,48.21,48.20,48.22,48.23,48.24,48.26,48.28,48.30,
    ]
    opens = [
        48.08,48.07,48.02,47.96,47.90,47.84,47.84,47.90,47.96,48.00,
        48.02,48.02,48.05,48.08,48.08,48.10,48.12,48.15,48.14,48.16,
        48.18,48.17,48.19,48.22,48.20,48.21,48.22,48.24,48.25,48.27,
    ]
    highs = [max(o,c)+0.04 for o,c in zip(opens, closes)]
    lows = [min(o,c)-0.04 for o,c in zip(opens, closes)]
    volumes = [
        150000,130000,120000,110000,100000,95000,90000,85000,80000,78000,
        76000,75000,74000,73000,72000,71000,70000,69000,68000,70000,
        72000,74000,76000,78000,90000,105000,120000,145000,170000,200000,
    ]
    return pd.DataFrame({"Open":opens,"High":highs,"Low":lows,"Close":closes,"Volume":volumes}, index=idx)


def test_hot_continuation_can_buy_without_three_percent_opening_flush(monkeypatch):
    monkeypatch.setattr(recovery, "_current_mid", lambda symbol: (48.35, 48.34, 48.36, 0.041))
    frame = _continuation_frame()

    ordinary = recovery.recovery_metrics(
        "LW",
        frame,
        pd.Timestamp("2026-10-07").date(),
        previous_close=47.91,
        resistance_price=52.00,
        continuation_mode=False,
    )
    assert "opening_flush_not_large_enough" in ordinary["failures"]

    continuation = recovery.recovery_metrics(
        "LW",
        frame,
        pd.Timestamp("2026-10-07").date(),
        previous_close=47.91,
        resistance_price=52.00,
        continuation_mode=True,
    )
    assert continuation["continuation_mode"] is True
    assert "opening_flush_not_large_enough" not in continuation["failures"]
    assert continuation["higher_low"] is True
    assert continuation["candidate_breakout_level"] <= continuation["session_high"]
    assert continuation["entry_trigger"] > continuation["candidate_breakout_level"]
    assert continuation["reward_risk_at_trigger"] >= 2.0
    assert continuation["state"] == "BUY"
