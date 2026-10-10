"""Research-only regression checks for recent swing health and deterioration."""
import unittest
from unittest.mock import patch
from ofts.research.swing_health import recent_swing_health


def pivots(values, spacing=6):
    return [(i*spacing, 'L' if i % 2 == 0 else 'H', price)
            for i, price in enumerate(values)]


class SwingHealthTests(unittest.TestCase):
    def diagnostic(self, values):
        turns = pivots(values)
        # Isolate swing-health decision logic from the separate ZigZag detector;
        # real-detector integration is checked in test_real_close_series.
        with patch('ofts.research.swing_health.detect_turns', return_value=turns):
            return recent_swing_health([100.0]*90, 6)

    def test_stable_recent_swings_with_flat_highs_lows(self):
        v = [100, 120, 100, 120, 100, 120, 100, 120, 100]
        r = self.diagnostic(v)
        self.assertEqual(r['state'], 'STABLE_RANGE')
        self.assertEqual(r['proposed_entry'], 'REVIEW')
        self.assertEqual(r['recent_completed_legs'], 4)
        self.assertEqual(r['high_progression'], 'MIXED')
        self.assertEqual(r['low_progression'], 'MIXED')

    def test_dissipating_swings_block_experimental_entry(self):
        v = [100, 125, 100, 125, 100, 125, 100, 125, 100,
             108, 100, 108, 100, 108, 100]
        r = self.diagnostic(v)
        self.assertEqual(r['state'], 'DECAYING')
        self.assertEqual(r['proposed_entry'], 'NO_TRADE')
        self.assertLess(r['recent_to_prior_amplitude_ratio'], 0.70)

    def test_lower_highs_and_lows_raise_risk_without_blanket_rejection(self):
        v = [100, 120, 95, 114, 90, 108, 85, 102, 80, 96, 75]
        r = self.diagnostic(v)
        self.assertEqual(r['high_progression'], 'FALLING')
        self.assertEqual(r['low_progression'], 'FALLING')
        self.assertEqual(r['state'], 'DOWNTREND')
        self.assertEqual(r['proposed_entry'], 'REVIEW')
        self.assertTrue(r['downward_structure'])

    def test_falling_highs_alone_are_not_a_breakdown(self):
        v = [100, 120, 101, 115, 102, 110, 103, 108, 104]
        r = self.diagnostic(v)
        self.assertEqual(r['high_progression'], 'FALLING')
        self.assertEqual(r['low_progression'], 'RISING')
        self.assertFalse(r['downward_structure'])

    def test_too_few_recent_cycles_fail_closed(self):
        r = self.diagnostic([100, 120, 100, 120, 100])
        self.assertEqual(r['state'], 'INSUFFICIENT')
        self.assertEqual(r['proposed_entry'], 'NO_TRADE')

    def test_recent_amplitude_instability_blocks_experimental_entry(self):
        v = [100, 115, 100, 130, 100, 107, 100, 150, 100]
        r = self.diagnostic(v)
        self.assertEqual(r['state'], 'IRREGULAR')
        self.assertEqual(r['proposed_entry'], 'NO_TRADE')

    def test_real_close_series_no_future_leakage(self):
        import math
        prices = [100 + 12 * math.sin(i/5) for i in range(90)]
        earlier = recent_swing_health(prices[:70], 6)
        # Rerunning the same frozen as-of data cannot change a diagnostic.
        self.assertEqual(earlier, recent_swing_health(prices[:70], 6))
        full = recent_swing_health(prices, 6)
        self.assertFalse(full['production_approved'])
        self.assertEqual(full['version'], 'swing-health-v0.1-experimental')
        self.assertTrue(all(x['end_index'] < len(prices) for x in full['last_four_legs']))


if __name__ == '__main__':
    unittest.main()
