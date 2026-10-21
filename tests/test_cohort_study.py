import unittest

import numpy as np
import pandas as pd

import loser_cohort_study as study


def history(event_return=-0.10, future_highs=None, future_lows=None):
    dates = pd.date_range("2025-01-01", periods=270, freq="B")
    close = np.full(270, 10.0)
    close[-20:-1] = 9.0
    close[-1] = close[-2] * (1 + event_return)
    data = pd.DataFrame({
        "Open": close, "High": close * 1.01, "Low": close * .99,
        "Close": close, "Volume": np.full(270, 1_000_000),
    }, index=dates)
    if future_highs is not None:
        extra_dates = pd.date_range(dates[-1] + pd.offsets.BDay(), periods=len(future_highs), freq="B")
        entry = close[-1]
        extra = pd.DataFrame({
            "Open": np.full(len(future_highs), entry), "High": np.array(future_highs) * entry,
            "Low": np.array(future_lows) * entry, "Close": np.full(len(future_highs), entry),
            "Volume": np.full(len(future_highs), 1_000_000),
        }, index=extra_dates)
        data = pd.concat([data, extra])
    return data


class CohortStudyTests(unittest.TestCase):
    def test_same_bar_touch_is_ambiguous(self):
        frame = history(-.10, [1.11], [.89])
        result = study._outcome(frame, 269)
        self.assertEqual(result["primary_outcome"], "AMBIGUOUS_SAME_BAR")

    def test_target_before_stop_is_win(self):
        frame = history(-.10, [1.11, 1.02], [.99, .89])
        result = study._outcome(frame, 269)
        self.assertEqual(result["primary_outcome"], "WIN_10_BEFORE_10")

    def test_immature_unresolved_event_stays_open(self):
        frame = history(-.10, [1.02] * 5, [.98] * 5)
        result = study._outcome(frame, 269)
        self.assertEqual(result["primary_outcome"], "OPEN")
        self.assertTrue(np.isnan(result["return_10"]))

    def test_event_requires_liquidity(self):
        frame = history(-.10)
        frame["Volume"] = 10
        self.assertEqual(study.event_rows(frame, "ABC"), [])

    def test_cooldown_prevents_recounting_same_collapse(self):
        frame = history(-.10)
        frame.loc[frame.index[-5], "Close"] *= .90
        rows = study.event_rows(frame, "ABC")
        dates = [r["event_date"] for r in rows]
        self.assertLessEqual(len(dates), 1)


if __name__ == "__main__":
    unittest.main()
