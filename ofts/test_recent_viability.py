"""Regression tests: stale big historical swings must not masquerade as profit."""
import unittest
from ofts.research.recent_viability import recent_swing_viability


def series(pivots, spacing=6):
    """Deterministic close-only path with confirmed reversals, no price feed."""
    prices=[float(pivots[0])]
    for a,b in zip(pivots,pivots[1:]):
        prices.extend(a+(b-a)*i/spacing for i in range(1,spacing+1))
    return prices


class RecentViabilityTests(unittest.TestCase):
    def test_big_old_swings_then_tiny_swings_are_fools_gold(self):
        prices=series([100,160,100,155,100,105,100,104,100,103,100])
        result=recent_swing_viability(prices,6)
        self.assertEqual(result['state'],'FOOLS_GOLD')
        self.assertEqual(result['proposed_entry'],'NO_TRADE')
        self.assertGreater(result['historical_mean_swing_pct'],
                           result['last_three_median_swing_pct']*3)
        self.assertTrue(result['outlier_foolsgold'])

    def test_repeated_small_swings_fail_even_without_old_outliers(self):
        result=recent_swing_viability(series([100,104,100,105,100,104,100,105,100,104,100]),6)
        self.assertEqual(result['state'],'TOO_SMALL')
        self.assertEqual(result['proposed_entry'],'NO_TRADE')

    def test_repeatable_recent_healthy_swings_remain_review_not_buy(self):
        result=recent_swing_viability(series([100,115,100,115,100,115,100,115,100,115,100]),6)
        self.assertEqual(result['state'],'REVIEW')
        self.assertEqual(result['proposed_entry'],'REVIEW')
        self.assertFalse(result['production_approved'])

    def test_big_down_swings_do_not_substitute_for_small_buyable_upswings(self):
        result=recent_swing_viability(series([100,105,80,84,60,63,45,47,30,31.5,20]),6)
        self.assertEqual(result['state'],'TOO_SMALL_UPSIDE')
        self.assertEqual(result['proposed_entry'],'NO_TRADE')
        self.assertLess(result['recent_up_median_pct'], result['minimum_gross_upside_pct'])

    def test_old_pivots_fail_recency_gate(self):
        prices=series([100,115,100,115,100,115,100,115,100,115,100])+[100]*90
        result=recent_swing_viability(prices,6)
        self.assertEqual(result['state'],'STALE_SWINGS')
        self.assertEqual(result['proposed_entry'],'NO_TRADE')

    def test_short_history_fails_closed(self):
        result=recent_swing_viability([100,101],6)
        self.assertEqual(result['state'],'INSUFFICIENT')
        self.assertEqual(result['proposed_entry'],'NO_TRADE')

    def test_micro_detector_sees_swings_below_major_threshold(self):
        result=recent_swing_viability(series([100,104,100,105,100,104,100,105,100,104,100]),12)
        self.assertEqual(result['micro_pivot_threshold_pct'],3.5)
        self.assertGreaterEqual(result['confirmed_minor_legs'],6)
        self.assertEqual(result['state'],'TOO_SMALL')

    def test_frozen_asof_result_reproducible(self):
        prices=series([100,115,100,115,100,115,100,115,100,115,100])
        before=recent_swing_viability(prices[:-6],6)
        self.assertEqual(before,recent_swing_viability(prices[:-6],6))
        self.assertFalse(before['production_approved'])


if __name__=='__main__':
    unittest.main()
