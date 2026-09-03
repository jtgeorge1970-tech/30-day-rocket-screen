import unittest
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import winner_continuation_study as study


def base_history(event_offset=-10, forward_highs=None, forward_lows=None, forward_closes=None):
    dates = pd.date_range("2025-01-01", periods=300, freq="B")
    close = np.full(300, 10.0)
    open_ = np.full(300, 10.0)
    high = np.full(300, 10.1)
    low = np.full(300, 9.9)
    volume = np.full(300, 1_000_000.0)
    event_idx = 300 + event_offset
    close[event_idx] = 12.2
    open_[event_idx] = 10.2
    high[event_idx] = 12.3
    low[event_idx] = 10.1
    volume[event_idx] = 5_000_000
    for idx in range(event_idx + 1, 300):
        close[idx] = 12.2
        open_[idx] = 12.2
        high[idx] = 12.25
        low[idx] = 12.15
    if forward_highs is not None:
        count = len(forward_highs)
        start = event_idx + 1
        open_[start:start + count] = 12.2
        high[start:start + count] = np.asarray(forward_highs) * 12.2
        low[start:start + count] = np.asarray(forward_lows) * 12.2
        if forward_closes is not None:
            close[start:start + count] = np.asarray(forward_closes) * 12.2
    return pd.DataFrame({"Open": open_, "High": high, "Low": low, "Close": close, "Volume": volume}, index=dates), event_idx


class WinnerContinuationStudyTests(unittest.TestCase):
    def test_next_open_is_measurement_entry(self):
        frame, event_idx = base_history()
        frame.iloc[event_idx + 1, frame.columns.get_loc("Open")] = 13.0
        result = study.outcome(frame, event_idx)
        self.assertEqual(result["next_open"], 13.0)

    def test_target_before_stop_is_win(self):
        frame, event_idx = base_history(forward_highs=[1.11, 1.02], forward_lows=[0.99, 0.89])
        result = study.outcome(frame, event_idx)
        self.assertEqual(result["primary_outcome"], "WIN_10_BEFORE_10")

    def test_same_bar_target_and_stop_is_ambiguous(self):
        frame, event_idx = base_history(forward_highs=[1.11], forward_lows=[0.89])
        result = study.outcome(frame, event_idx)
        self.assertEqual(result["primary_outcome"], "AMBIGUOUS_SAME_BAR")

    def test_immature_event_stays_open(self):
        frame, event_idx = base_history(event_offset=-5)
        result = study.outcome(frame, event_idx)
        self.assertEqual(result["primary_outcome"], "OPEN")
        self.assertTrue(np.isnan(result["return_10"]))

    def test_event_requires_liquidity(self):
        frame, _ = base_history()
        frame["Volume"] = 10
        self.assertEqual(study.event_rows(frame, "ABC"), [])

    def test_cooldown_prevents_duplicate_run_events(self):
        frame, event_idx = base_history(event_offset=-20)
        second = event_idx + 5
        frame.iloc[second, frame.columns.get_loc("Close")] = frame.Close.iloc[second - 1] * 1.25
        frame.iloc[second, frame.columns.get_loc("High")] = frame.Close.iloc[second] * 1.01
        frame.iloc[second, frame.columns.get_loc("Volume")] = 5_000_000
        rows = study.event_rows(frame, "ABC")
        self.assertEqual(len(rows), 1)

    def test_trailing_stop_uses_next_bar_after_activation(self):
        future = pd.DataFrame(
            {
                "Open": [10, 11, 10.3],
                "High": [11.1, 11.2, 10.5],
                "Low": [8.9, 10.8, 10.0],
                "Close": [10.8, 11.0, 10.2],
            }
        )
        value, status = study._trailing_result(future, 10.0, 1, np.nan, 0.07)
        self.assertEqual(status, "TRAIL_EXIT")
        # The third session opens below the computed stop, so the model uses
        # the worse opening fill instead of assuming execution at the trigger.
        self.assertAlmostEqual(value, 10.3 / 10.0 - 1)

    def test_trailing_policy_respects_disaster_stop_before_activation(self):
        future = pd.DataFrame(
            {
                "Open": [10.0, 8.5, 11.0],
                "High": [10.2, 9.0, 11.2],
                "Low": [9.8, 8.0, 10.8],
                "Close": [10.0, 8.7, 11.1],
            }
        )
        value, status = study._trailing_result(future, 10.0, 3, 2, 0.07)
        self.assertEqual(status, "DISASTER_STOP")
        self.assertAlmostEqual(value, -0.15)

    def test_same_bar_activation_and_disaster_stop_is_ambiguous(self):
        future = pd.DataFrame(
            {"Open": [10.0], "High": [11.1], "Low": [8.9], "Close": [10.0]}
        )
        value, status = study._trailing_result(future, 10.0, 1, 1, 0.07)
        self.assertTrue(np.isnan(value))
        self.assertEqual(status, "AMBIGUOUS_ACTIVATION_BAR")


if __name__ == "__main__":
    unittest.main()
