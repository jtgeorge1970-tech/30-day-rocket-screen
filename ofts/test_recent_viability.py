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
        self.assertIn(result['state'],('TOO_SMALL','TOO_SMALL_UPSIDE'))
        self.assertEqual(result['proposed_entry'],'NO_TRADE')

    def test_repeatable_recent_healthy_swings_remain_review_not_buy(self):
        result=recent_swing_viability(series([100,115]*8+[100]),6)
        self.assertEqual(result['state'],'REVIEW')
        self.assertEqual(result['proposed_entry'],'REVIEW')
        self.assertFalse(result['production_approved'])

    def test_big_down_swings_do_not_substitute_for_small_buyable_upswings(self):
        result=recent_swing_viability(series([100,105,80,84,60,63,45,47,30,31.5,20]),6)
        # Multiple independent reasons can block the same weak setup.
        # Historical downside outliers may take precedence over tiny upside.
        self.assertIn(result['state'],('FOOLS_GOLD','TOO_SMALL_UPSIDE'))
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
        self.assertIn(result['state'],('TOO_SMALL','TOO_SMALL_UPSIDE'))

    def test_two_of_three_up_swings_is_watch_not_buy(self):
        # Earlier stable 10% legs; last three UP swings 10%, 4%, 10%.
        # Last three completed overall legs are not tiny, but repeatability fails.
        p=series([100,110,100,110,100,110,100,104,100,110,100,110])
        r=recent_swing_viability(p,6)
        self.assertEqual(r['repeated_up_pass_count'],2)
        self.assertEqual(r['recent_up_repeatability'],'WATCH_2_OF_3')
        self.assertIn(r['state'],('WATCH','TOO_SMALL'))
        self.assertEqual(r['proposed_entry'],'NO_TRADE')

    def test_latest_up_under_five_kills_even_if_mean_high(self):
        p=series([100,115,100,115,100,115,100,115,100,104,100])
        r=recent_swing_viability(p,6)
        self.assertEqual(r['repeated_up_pass_count'],2)
        self.assertLess(r['last_up_pct'],5)
        self.assertEqual(r['state'],'TOO_SMALL_UPSIDE')
        self.assertEqual(r['proposed_entry'],'NO_TRADE')

    def test_three_up_swings_repeated_but_net_hurdle_still_matters(self):
        p=series([100,105.1,100,105.1,100,105.1,100,105.1,100,105.1,100])
        r=recent_swing_viability(p,6)
        self.assertEqual(r['repeated_up_pass_count'],3)
        self.assertIn(r['state'],('TOO_SMALL','TOO_SMALL_UPSIDE'))
        self.assertLess(r['hypothetical_net_capture_pct'],2.5)

    def test_three_strong_up_swings_pass_as_research_only(self):
        p=series([100,108]*8+[100])
        r=recent_swing_viability(p,6)
        self.assertEqual(r['repeated_up_pass_count'],3)
        self.assertEqual([round(x,1) for x in r['last_three_up_pct']],[8,8,8])
        self.assertEqual(r['state'],'REVIEW')
        self.assertEqual(r['recent_up_repeatability'],'STABLE_3_OF_3')
        self.assertFalse(r['production_approved'])

    def test_repeated_five_percent_swings_six_weeks_apart_fail_cycle_timing(self):
        # 48 trading sessions peak-to-peak: above the 40-session preferred
        # maximum, despite three strong 8% UP legs.
        p=series([100,108,100,108,100,108,100,108,100,108,100],spacing=24)
        r=recent_swing_viability(p,6,lookback=400)
        self.assertEqual(r['repeated_up_pass_count'],3)
        self.assertEqual(r['last_three_peak_to_peak_sessions'],[48,48,48])
        self.assertFalse(r['cycle_timing_pass'])
        self.assertEqual(r['state'],'CYCLE_TIMING')
        self.assertEqual(r['proposed_entry'],'NO_TRADE')

    def test_repeated_ups_and_twelve_session_cycles_remain_research_review(self):
        p=series([100,108]*8+[100],spacing=6)
        r=recent_swing_viability(p,6)
        self.assertEqual(r['last_three_peak_to_peak_sessions'],[12,12,12])
        self.assertEqual(r['last_three_trough_to_trough_sessions'],[12,12,12])
        self.assertEqual(r['peak_cycle_median_sessions'],12)
        self.assertTrue(r['cycle_timing_pass'])
        self.assertEqual(r['state'],'REVIEW')

    def test_irregular_cycle_intervals_fail_even_when_median_is_in_range(self):
        # Recent 24/36/12-session cycles: median 24 passes range, but
        # relative MAD=0.5 fails regularity.
        pivot_prices=[100,108,100,108,100,108,100,108,100,108,100]
        spans=[6,6,6,6,18,6,30,6,6,6]
        p=[100.0]
        for a,b,span in zip(pivot_prices,pivot_prices[1:],spans):
            p.extend(a+(b-a)*i/span for i in range(1,span+1))
        r=recent_swing_viability(p,6)
        self.assertEqual(r['repeated_up_pass_count'],3)
        self.assertFalse(r['cycle_timing_pass'])
        self.assertEqual(r['state'],'CYCLE_TIMING')

    def test_recent_up_amplitude_shrinks_vs_immediately_prior_three(self):
        # Three recent 7% rebounds still pass >=5% and 12-day cycles,
        # but prior three rebounds were 11%, hence 7/11 < 0.70.
        ups=[11,11,11,11,11,7,7,7]
        values=[100]
        for x in ups: values.extend([100+x,100])
        r=recent_swing_viability(series(values),6)
        self.assertEqual([round(x,3) for x in r['preceding_three_up_pct']],[11,11,11])
        self.assertEqual([round(x,3) for x in r['last_three_up_pct']],[7,7,7])
        self.assertAlmostEqual(r['recent_vs_prior_up_ratio'],7/11)
        self.assertEqual(r['recent_vs_prior_state'],'DISSIPATING')
        self.assertEqual(r['state'],'DISSIPATING')
        self.assertEqual(r['proposed_entry'],'NO_TRADE')

    def test_recent_cycles_slow_vs_preceding_three_even_with_good_amplitude(self):
        values=[100,110]*8+[100]
        # Early cycles 12 sessions, latest cycles 24 sessions.
        spans=[6]*10+[12]*6
        prices=[100.]
        for a,b,n in zip(values,values[1:],spans):
            prices.extend(a+(b-a)*i/n for i in range(1,n+1))
        r=recent_swing_viability(prices,6,lookback=400)
        self.assertEqual([round(x,3) for x in r['last_three_up_pct']],[10,10,10])
        self.assertGreater(r['recent_vs_prior_cadence_ratio'],1.5)
        self.assertEqual(r['recent_vs_prior_state'],'DISSIPATING')
        self.assertEqual(r['state'],'DISSIPATING')

    def test_three_up_swings_without_prior_three_fail_closed(self):
        r=recent_swing_viability(series([100,108]*5+[100]),6)
        self.assertEqual(r['recent_vs_prior_state'],'INSUFFICIENT')
        self.assertEqual(r['state'],'INSUFFICIENT_COMPARISON')
        self.assertEqual(r['proposed_entry'],'NO_TRADE')

    def test_frozen_asof_result_reproducible(self):
        prices=series([100,115,100,115,100,115,100,115,100,115,100])
        before=recent_swing_viability(prices[:-6],6)
        self.assertEqual(before,recent_swing_viability(prices[:-6],6))
        self.assertFalse(before['production_approved'])


if __name__=='__main__':
    unittest.main()
