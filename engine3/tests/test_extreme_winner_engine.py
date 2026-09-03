import tempfile
import unittest
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import extreme_winner_engine as engine


def price_history(event_offset=-3, event_return=0.22, volume_ratio=5.0):
    dates = pd.date_range("2025-01-01", periods=300, freq="B")
    close = np.full(300, 10.0)
    open_ = np.full(300, 10.0)
    high = np.full(300, 10.1)
    low = np.full(300, 9.9)
    volume = np.full(300, 1_000_000.0)
    idx = 300 + event_offset
    close[idx:] = 10.0 * (1 + event_return)
    open_[idx] = 10.2
    high[idx] = close[idx] * 1.01
    low[idx] = 10.1
    volume[idx] = 1_000_000 * volume_ratio
    for pos in range(idx + 1, 300):
        open_[pos] = close[pos] * 0.995
        high[pos] = close[pos] * 1.01
        low[pos] = close[pos] * 0.99
    return pd.DataFrame({"Open": open_, "High": high, "Low": low, "Close": close, "Volume": volume}, index=dates)


def scored_input(row):
    frame = pd.DataFrame([row])
    frame["name"] = "Example Corp"
    frame["market_cap"] = 500_000_000
    frame["float_shares"] = 30_000_000
    frame["shares_outstanding"] = 40_000_000
    frame["revenue_growth"] = 0.20
    frame["earnings_growth"] = 0.30
    frame["debt_to_equity"] = 20.0
    frame["current_ratio"] = 2.0
    frame["target_upside"] = 0.20
    frame["recommendation"] = 2.0
    frame["sector"] = "Technology"
    frame["industry"] = "Hardware"
    return frame


class ExtremeWinnerEngineTests(unittest.TestCase):
    def test_detects_one_day_extreme_winner_in_30_session_window(self):
        row = engine.analyze_history(price_history(), "ABC")
        self.assertTrue(row["event_detected"])
        self.assertEqual(row["event_type"], "ONE_DAY")
        self.assertGreaterEqual(row["event_day_return"], engine.ONE_DAY_EVENT)
        self.assertEqual(row["event_age_sessions"], 2)

    def test_does_not_detect_subthreshold_move(self):
        row = engine.analyze_history(price_history(event_return=0.10), "ABC")
        self.assertFalse(row["event_detected"])

    def test_gate_requires_abnormal_volume(self):
        row = engine.analyze_history(price_history(volume_ratio=1.5), "ABC")
        scored = engine.score_events(scored_input(row), 0.0)
        self.assertFalse(bool(scored.automated_gate_pass.iloc[0]))

    def test_strong_structure_passes_automated_gate(self):
        row = engine.analyze_history(price_history(), "ABC")
        scored = engine.score_events(scored_input(row), 0.0)
        self.assertTrue(bool(scored.automated_gate_pass.iloc[0]))

    def test_entry_ready_requires_fresh_all_pass_review(self):
        top3 = pd.DataFrame({"ticker": ["ABC"], "continuation_score": [90.0]})
        review = {"ticker": "ABC", "retrieved_at": datetime.now(timezone.utc).isoformat(), "final_status": "APPROVED"}
        review.update({gate: "PASS" for gate in engine.VERIFICATION_GATES})
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "review.csv"
            pd.DataFrame([review]).to_csv(path, index=False)
            entries = engine.approved_entries(top3, path)
        self.assertEqual(entries.ticker.tolist(), ["ABC"])

    def test_stale_review_cannot_create_entry(self):
        top3 = pd.DataFrame({"ticker": ["ABC"], "continuation_score": [90.0]})
        review = {
            "ticker": "ABC",
            "retrieved_at": (datetime.now(timezone.utc) - timedelta(hours=25)).isoformat(),
            "final_status": "APPROVED",
        }
        review.update({gate: "PASS" for gate in engine.VERIFICATION_GATES})
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "review.csv"
            pd.DataFrame([review]).to_csv(path, index=False)
            entries = engine.approved_entries(top3, path)
        self.assertTrue(entries.empty)


if __name__ == "__main__":
    unittest.main()
