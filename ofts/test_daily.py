import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import Mock, patch
import contextlib
import io
import json
import pandas as pd
from ofts.daily import (save_history, read_history, merge_history, refresh,
                        frozen_snapshot, outcomes, completed_session, market_schedule,
                        snapshot_is_qualified, load_qualified_snapshots,
                        cycle_fingerprint)


def bar(date, close=100, split=0):
    return dict(date=date, open=100, high=max(101, close), low=min(99, close), close=close, volume=1000, split=split)


class PersistenceTests(unittest.TestCase):
    def test_restart_and_new_day_merge_deduplicates(self):
        with tempfile.TemporaryDirectory() as d:
            state = Path(d)
            save_history(state, 'ABC', [bar('2026-10-07')])
            loaded = read_history(Path(d), 'ABC')
            merged = merge_history(loaded, [bar('2026-10-07', 102), bar('2026-10-08'), bar('2026-10-09')], '2026-10-08')
            save_history(state, 'ABC', merged)
            restored = read_history(Path(d), 'ABC')
            self.assertEqual([r['date'] for r in restored], ['2026-10-07', '2026-10-08'])
            self.assertEqual(float(restored[0]['close']), 102)

    def test_failed_download_preserves_history_and_retries(self):
        with tempfile.TemporaryDirectory() as d:
            state = Path(d)
            save_history(state, 'ABC', [bar('2026-10-07')])
            provider = Mock(side_effect=RuntimeError('network failed'))
            audit = refresh(state, ['ABC'], '2026-10-08', provider)
            self.assertEqual(audit['ABC']['status'], 'ERROR')
            self.assertEqual(provider.call_count, 2)
            self.assertEqual(read_history(state, 'ABC')[-1]['date'], '2026-10-07')

    def test_empty_then_single_ticker_multiindex_recovers(self):
        with tempfile.TemporaryDirectory() as d:
            cols = pd.MultiIndex.from_product([['ABC'], ['Open', 'High', 'Low', 'Close', 'Volume', 'Stock Splits']])
            frame = pd.DataFrame([[100, 101, 99, 100, 1000, 0]], columns=cols, index=pd.to_datetime(['2026-10-08']))
            provider = Mock(side_effect=[pd.DataFrame(), frame])
            audit = refresh(Path(d), ['ABC'], '2026-10-08', provider)
            self.assertEqual(audit['ABC']['status'], 'FRESH')
            self.assertEqual(provider.call_count, 2)

    def test_failed_coverage_is_preserved_but_not_used_as_forward_cohort(self):
        with tempfile.TemporaryDirectory() as d:
            predictions = Path(d)
            failed = dict(asof='2026-10-09', rows=[
                dict(symbol=f'S{i}', score=None, classification='STALE_DATA', asof='2026-10-08')
                for i in range(125)])
            frozen_snapshot(predictions / '2026-10-09.json', failed)
            self.assertFalse(snapshot_is_qualified(failed))
            self.assertEqual(load_qualified_snapshots(predictions), [])
            recovered = dict(asof='2026-10-09', coverage={'fresh': 124}, rows=[])
            frozen_snapshot(predictions / '2026-10-09-qualified.json', recovered)
            self.assertEqual(load_qualified_snapshots(predictions), [recovered])
            self.assertTrue((predictions / '2026-10-09.json').exists())

    def test_cycle_fingerprint_is_point_in_time_and_describes_cadence(self):
        import math
        closes = [100 + 15 * math.sin(i / 8) for i in range(260)]
        highs = [c + 2 for c in closes]
        lows = [c - 2 for c in closes]
        result = __import__('ofts.research.v23_replacement', fromlist=['evaluate']).evaluate(highs, lows, closes)
        fp = cycle_fingerprint(closes, result['threshold_pct'], result['structural'])
        self.assertGreater(fp['cycle_sessions'], 0)
        self.assertGreaterEqual(fp['completed_cycle_intervals'], 4)
        self.assertGreater(fp['median_swing_pct'], 0)
        # Repeating the same as-of slice must be deterministic; later bars are
        # never supplied to the function and cannot rewrite the fingerprint.
        self.assertEqual(fp, cycle_fingerprint(closes, result['threshold_pct'], result['structural']))

    def test_saved_prediction_is_immutable(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / 'prediction.json'
            frozen_snapshot(path, {'score': 60})
            original = path.read_bytes()
            frozen_snapshot(path, {'score': 90})
            self.assertEqual(original, path.read_bytes())

    def test_complete_cycle_restart_and_next_session(self):
        import ofts.daily as daily
        import sys
        schedule = market_schedule(datetime(2026, 10, 9, 23, tzinfo=timezone.utc))
        sessions = [str(d.date()) for d in schedule.index]
        target = ['2026-10-07']
        def provider(symbol, **kwargs):
            end = sessions.index(target[0])
            dates = pd.to_datetime(sessions[end-500:end+1])
            values = [[100, 112, 88, 100 + 10 * __import__('math').sin(i / 8), 1000, 0] for i in range(len(dates))]
            cols = pd.MultiIndex.from_product([[symbol], ['Open', 'High', 'Low', 'Close', 'Volume', 'Stock Splits']])
            return pd.DataFrame(values, index=dates, columns=cols)
        with tempfile.TemporaryDirectory() as d:
            state = Path(d)
            with patch.object(sys, 'argv', ['daily', '--state', d, '--batch-size', '1']), patch.object(daily, 'market_schedule', return_value=schedule), patch.object(daily, 'completed_session', side_effect=lambda *a: target[0]), patch('yfinance.download', side_effect=provider), contextlib.redirect_stdout(io.StringIO()):
                daily.main()
                prediction = state / 'predictions/2026-10-07.json'
                original = prediction.read_bytes()
                daily.main()
                self.assertEqual(prediction.read_bytes(), original)
                self.assertEqual(json.loads((state / 'control.json').read_text())['cursor'], 1)
                target[0] = '2026-10-08'
                daily.main()
                self.assertEqual(prediction.read_bytes(), original)
                self.assertEqual(json.loads((state / 'control.json').read_text())['cursor'], 2)
                self.assertEqual(len(list((state / 'predictions').glob('*.json'))), 2)
                self.assertEqual(len(list((state / 'attempts').glob('*.json'))), 3)
                history = read_history(state, 'HLIT')
                self.assertEqual(len({r['date'] for r in history}), len(history))
                self.assertEqual(history[-1]['date'], '2026-10-08')

    def test_calendar_holiday_and_early_close(self):
        now = datetime(2026, 11, 27, 18, 45, tzinfo=timezone.utc)
        schedule = market_schedule(now)
        self.assertEqual(completed_session(schedule, now), '2026-11-27')
        before_early_close = datetime(2026, 11, 27, 17, 0, tzinfo=timezone.utc)
        self.assertEqual(completed_session(schedule, before_early_close), '2026-11-25')


class OutcomeTests(unittest.TestCase):
    def setUp(self):
        self.schedule = market_schedule(datetime(2026, 10, 9, 23, tzinfo=timezone.utc))
        self.dates = [str(d.date()) for d in self.schedule.index]
        start = self.dates.index('2026-09-01')
        self.future = self.dates[start+1:start+61]
        self.snapshot = dict(asof='2026-09-01', recorded_at='2026-09-01T23:00:00+00:00', model_hash='frozen',
                             rows=[dict(symbol='ABC', score=65, classification='CANDIDATE')])

    def test_future_is_pending_not_zero_or_win(self):
        result = outcomes(self.snapshot, {'ABC': []}, self.schedule)
        self.assertTrue(all(r['status'] == 'PENDING' for r in result))
        self.assertTrue(all('net_assumed_return_pct' not in r for r in result))

    def test_next_open_costs_and_benchmark(self):
        history = [bar(d, 110) for d in self.future[:5]]
        result = outcomes(self.snapshot, {'ABC': history, 'SPY': [bar(d, 102) for d in self.future[:5]]}, self.schedule)
        row = result[0]
        self.assertEqual(row['status'], 'MATURE')
        self.assertAlmostEqual(row['net_assumed_return_pct'], 9.8)
        self.assertAlmostEqual(row['excess_gross_pct'], 8)
        self.assertEqual(result[1]['status'], 'PENDING')

    def test_late_recording_not_prospective(self):
        self.snapshot['recorded_at'] = '2026-09-02T15:00:00+00:00'
        result = outcomes(self.snapshot, {'ABC': [bar(d) for d in self.future]}, self.schedule)
        self.assertTrue(all(r['status'] == 'NOT_PROSPECTIVE_RECORDED_AFTER_ENTRY' for r in result))

    def test_split_or_missing_session_not_valid_return(self):
        history = [bar(d) for d in self.future[:5]]
        history[2]['split'] = 2
        self.assertEqual(outcomes(self.snapshot, {'ABC': history}, self.schedule)[0]['status'], 'CORPORATE_ACTION_REVIEW')
        history.pop(2)
        self.assertEqual(outcomes(self.snapshot, {'ABC': history}, self.schedule)[0]['status'], 'MISSING_SESSIONS')

if __name__ == '__main__':
    unittest.main()
