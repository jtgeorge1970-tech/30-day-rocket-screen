"""Regression checks for the opt-in clean manual selection snapshot.

Load the real pool builder in isolation so provider requests are deterministic.
These tests make no network calls and do not change trading gates.
"""
import ast
import math
import os
import unittest
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
from zoneinfo import ZoneInfo

import pandas as pd


class ManualFreshnessTests(unittest.TestCase):
    def setUp(self):
        source = Path(__file__).with_name("engine4_pipeline_runner.py").read_text()
        tree = ast.parse(source)
        function = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "repaired_build_broad_pool")
        self.frame = pd.DataFrame({"Close": [10.1, 11.5]}, index=pd.to_datetime(["2026-10-02T09:00:00-04:00", "2026-10-02T12:59:00-04:00"]))
        self.cutoffs = []
        def window(frame, date, start, end):
            self.cutoffs.append(end)
            return frame.between_time(start, end)
        base = pd.DataFrame([{"ticker": "TEST", "name": "Fixture", "sector": "Technology", "market_cap": 1e9, "dollar_volume": 1e7, "price": 10.0}])
        core = SimpleNamespace(now_et=lambda: datetime(2026, 10, 2, 13, 0, tzinfo=ZoneInfo("America/New_York")), eligible_baseline=lambda: base.copy(), download_intraday=lambda *args, **kwargs: {"TEST": self.frame}, slice_window=window, prior_regular_close=lambda *args: 10.0)
        namespace = {"os": os, "pd": pd, "math": math, "core": core, "MIN_PRICE": 2.0, "NASDAQ_ENRICH_CAP": 500, "BROAD_POOL_SIZE": 100, "preliminary_activity_score": lambda *args: 1.0, "_estimated_avg_daily_shares": lambda *args: 1e6, "nasdaq_premarket_many": lambda *args, **kwargs: {"TEST": {"ok": True, "premarket_price": 9.2, "premarket_volume": 100000.0}}}
        exec(compile(ast.Module(body=[function], type_ignores=[]), "actual_pool_builder", "exec"), namespace)
        self.build = namespace["repaired_build_broad_pool"]
        self.date = core.now_et().date()

    def run_pool(self, requested, manual="1"):
        env = {"ENGINE4_MANUAL_CURRENT_SNAPSHOT": manual}
        if requested is not None:
            env["ENGINE4_FRESH_REQUESTED_AT"] = requested
        with patch.dict(os.environ, env, clear=True):
            return self.build(self.date, "09:05")

    def test_current_price_cannot_be_overwritten_by_old_premarket_price(self):
        pool, counts = self.run_pool("2026-10-02T16:58:00Z")
        self.assertEqual(len(pool), 1)
        self.assertEqual(pool.iloc[0]["selection_price"], 11.5)
        self.assertEqual(pool.iloc[0]["last_premarket"], 11.5)
        self.assertEqual(pool.iloc[0]["snapshot_mode"], "CURRENT_LIVE_MANUAL")
        self.assertEqual(self.cutoffs, ["13:00"])
        self.assertEqual(counts["trustworthy_observed"], 1)

    def test_bar_before_request_is_rejected(self):
        pool, counts = self.run_pool("2026-10-02T17:00:00Z")
        self.assertTrue(pool.empty)
        self.assertEqual(counts["trustworthy_observed"], 0)

    def test_naive_bar_time_is_rejected(self):
        self.frame.index = self.frame.index.tz_localize(None)
        pool, counts = self.run_pool("2026-10-02T16:58:00Z")
        self.assertTrue(pool.empty)
        self.assertEqual(counts["trustworthy_observed"], 0)

    def test_missing_request_boundary_fails_explicitly(self):
        with self.assertRaisesRegex(RuntimeError, "missing requested-at freshness boundary"):
            self.run_pool(None)

    def test_normal_premarket_path_keeps_original_cutoff_and_provider_price(self):
        pool, _ = self.run_pool(None, manual="0")
        self.assertEqual(self.cutoffs, ["09:05"])
        self.assertEqual(pool.iloc[0]["last_premarket"], 9.2)
        self.assertEqual(pool.iloc[0]["snapshot_mode"], "PREMARKET")


if __name__ == "__main__":
    unittest.main()
