import os
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import patch

import numpy as np
import pandas as pd

import rocket_screen as engine


class QualityLoserEngineTests(unittest.TestCase):
    def test_insufficient_history_never_scores(self):
        frame = pd.DataFrame({
            "Close": np.arange(100, 200), "High": np.arange(101, 201),
            "Low": np.arange(99, 199), "Volume": np.full(100, 1_000_000),
        })
        self.assertIsNone(engine.technical_snapshot(frame))

    def test_stability_requires_two_of_three_sessions(self):
        dates = pd.date_range("2025-01-01", periods=260, freq="B")
        one = pd.DataFrame({
            ("Close", "ABC"): np.arange(260) + 10,
            ("High", "ABC"): np.arange(260) + 11,
            ("Low", "ABC"): np.arange(260) + 9,
            ("Volume", "ABC"): np.full(260, 1_000_000),
        }, index=dates)
        passing = {"technical_setup_pass": True, "price": 10}
        failing = {"technical_setup_pass": False, "price": 10}
        with patch.object(engine, "technical_snapshot", side_effect=[passing, passing, failing, failing]):
            result = engine.price_rows_from_download(one, ["ABC"])[0]
        self.assertEqual(result["setup_pass_sessions_3"], 1)
        self.assertFalse(result["stability_pass"])

    def test_collapsing_revenue_is_a_veto_not_a_score_penalty(self):
        frame = pd.DataFrame([{
            "revenue_growth": -0.40, "total_cash": 10, "total_debt": 1,
            "operating_cashflow": 1, "current_ratio": 2,
        }])
        checked = engine.automated_quality(frame)
        self.assertFalse(bool(checked.loc[0, "automated_quality_pass"]))

    def test_missing_fundamentals_do_not_receive_an_invented_pass(self):
        frame = pd.DataFrame([{
            "revenue_growth": np.nan, "total_cash": np.nan, "total_debt": np.nan,
            "operating_cashflow": np.nan, "current_ratio": np.nan,
        }])
        checked = engine.automated_quality(frame)
        self.assertEqual(checked.loc[0, "fundamental_coverage"], 0)
        self.assertFalse(bool(checked.loc[0, "automated_quality_pass"]))

    def _verification_row(self, verified_at, catalyst="PASS"):
        row = {column: "PASS" for column in engine.VERIFICATION_FIELDS}
        row.update({
            "ticker": "ABC", "verified_at": verified_at, "reviewer": "test",
            "selloff_reason": "known non-thesis event", "catalyst_date": "2026-09-12",
            "catalyst_description": "specific future event", "source_urls": "https://example.test",
            "future_catalyst_pass": catalyst, "final_status": "APPROVED",
        })
        return row

    def test_fresh_all_pass_verification_can_advance(self):
        with tempfile.TemporaryDirectory() as folder:
            old = os.getcwd()
            try:
                os.chdir(folder)
                pd.DataFrame([self._verification_row(datetime.now(timezone.utc).isoformat())]).to_csv("current_verification.csv", index=False)
                _, valid = engine.load_current_verification(["ABC"])
            finally:
                os.chdir(old)
        self.assertEqual(valid, {"ABC"})

    def test_stale_or_failed_catalyst_cannot_advance(self):
        stale = (datetime.now(timezone.utc) - timedelta(hours=25)).isoformat()
        with tempfile.TemporaryDirectory() as folder:
            old = os.getcwd()
            try:
                os.chdir(folder)
                rows = [self._verification_row(stale), self._verification_row(datetime.now(timezone.utc).isoformat(), catalyst="FAIL")]
                pd.DataFrame(rows).to_csv("current_verification.csv", index=False)
                _, valid = engine.load_current_verification(["ABC"])
            finally:
                os.chdir(old)
        self.assertEqual(valid, set())


if __name__ == "__main__":
    unittest.main()
