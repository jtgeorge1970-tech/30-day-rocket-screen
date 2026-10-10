"""Regression tests for identity-regime isolation (no hindsight rewriting)."""
import contextlib
import io
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

from ofts.research.security_regimes import post_identity_bars


class SecurityIdentityTests(unittest.TestCase):
    def test_iqmx_predecessor_spac_bars_are_excluded(self):
        before = [{'date': '2026-06-30'} for _ in range(270)]
        after = [{'date': '2026-07-02'} for _ in range(70)]
        kept, event = post_identity_bars('IQMX', before + after, '2026-10-09')
        self.assertEqual(len(kept), 70)
        self.assertEqual(event['start'], '2026-07-02')
        self.assertLess(len(kept), 180)

    def test_unrelated_stock_is_unchanged(self):
        bars = [{'date': '2026-06-30'}, {'date': '2026-10-09'}]
        kept, event = post_identity_bars('AKAM', bars, '2026-10-09')
        self.assertEqual(kept, bars)
        self.assertIsNone(event)

    def test_event_not_applied_before_effective_date(self):
        bars = [{'date': '2026-06-29'}]
        kept, event = post_identity_bars('IQMX', bars, '2026-06-29')
        self.assertEqual(kept, bars)
        self.assertIsNone(event)

    def test_missing_date_fails_closed(self):
        with self.assertRaisesRegex(ValueError, 'IDENTITY_BOUNDARY_REQUIRES_DATED_HISTORY'):
            post_identity_bars('IQMX', [{'close': 10}], '2026-10-09')

    def test_daily_cohort_rejects_iqmx_with_only_post_merger_70_bars(self):
        import pandas as pd
        import ofts.daily as daily
        import sys
        schedule = daily.market_schedule(datetime(2026, 10, 9, 23, tzinfo=timezone.utc))
        sessions = [str(d.date()) for d in schedule.index]
        target = '2026-10-09'
        end = sessions.index(target)
        # 340 pre+post bars: many historical predecessor bars, only ~70
        # after the verified July 2 identity change.
        dates = pd.to_datetime(sessions[end-339:end+1])
        self.assertEqual(len(dates), 340)
        self.assertLess(sum(str(d.date()) >= '2026-07-02' for d in dates), 180)
        def provider(symbol, **kwargs):
            values = [[10, 11, 9, 10, 1000, 0] for _ in dates]
            columns = pd.MultiIndex.from_product(
                [[symbol], ['Open', 'High', 'Low', 'Close', 'Volume', 'Stock Splits']])
            return pd.DataFrame(values, index=dates, columns=columns)
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp)
            with patch.object(sys, 'argv', ['daily', '--state', tmp, '--batch-size', '1']), \
                 patch.object(daily, 'WATCH', ['IQMX']), \
                 patch.object(daily, 'market_schedule', return_value=schedule), \
                 patch.object(daily, 'completed_session', return_value=target), \
                 patch('yfinance.download', side_effect=provider), \
                 contextlib.redirect_stdout(io.StringIO()):
                daily.main()
            frozen = json.loads((state / 'predictions/2026-10-09.json').read_text())
            row = frozen['rows'][0]
            self.assertEqual(row['symbol'], 'IQMX')
            self.assertEqual(row['classification'], 'INSUFFICIENT_POST_REGIME_HISTORY')
            self.assertIsNone(row['score'])
            self.assertEqual(row['signal']['state'], 'NO_TRADE')
            self.assertEqual(row['raw_bars'], 340)
            self.assertLess(row['bars'], 180)
            self.assertEqual(row['regime_start'], '2026-07-02')
            audits = daily.outcomes(frozen, {}, schedule)
            self.assertEqual(len(audits), 5)
            self.assertTrue(all(a['status'] == 'INELIGIBLE_DATA' for a in audits))


if __name__ == '__main__':
    unittest.main()
