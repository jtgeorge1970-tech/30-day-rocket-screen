"""Experimental v0.6 opportunity component regression tests."""
import unittest
from ofts.research.opportunity_v06 import opportunity_partial

class OpportunityV06Tests(unittest.TestCase):
    def _data(self,ups,peaks=(10,10,10),troughs=(10,10,10),cadence=1.0):
        return {"last_three_up_pct":list(ups),
                "last_three_peak_to_peak_sessions":list(peaks),
                "last_three_trough_to_trough_sessions":list(troughs),
                "recent_vs_prior_cadence_ratio":cadence}
    def test_repeatable_swings_outscore_shrinking_ups(self):
        healthy=opportunity_partial(self._data([9,9,9]),{"state":"STABLE_RANGE"})
        shrinking=opportunity_partial(self._data([27,18,14]),{"state":"DOWNTREND"})
        self.assertGreater(healthy["measured_score"],shrinking["measured_score"])
        self.assertEqual(healthy["measured_max"],80)
        self.assertIsNone(healthy["entry_points"])
        self.assertIsNone(healthy["eligibility_score"])
        self.assertFalse(healthy["production_approved"])
    def test_consecutive_decline_penalty(self):
        x=opportunity_partial(self._data([30,18,8]),{"state":"STABLE_RANGE"})
        self.assertEqual(x["health_deductions"]["three_shrinking_ups"],8)
        self.assertEqual(x["health_deductions"]["latest_bounce_weak"],4)
    def test_fail_closed_without_three_cycles(self):
        x=opportunity_partial(self._data([9,9],peaks=(10,10)),{"state":"STABLE_RANGE"})
        self.assertEqual(x["status"],"INSUFFICIENT")
        self.assertIsNone(x["measured_score"])
    def test_partial_never_becomes_buy_or_eligible(self):
        x=opportunity_partial(self._data([15,15,15]),{"state":"STABLE_RANGE"})
        self.assertEqual(x["eligibility_status"],"PENDING_ELIGIBILITY")
        self.assertEqual(x["status"],"PARTIAL_RESEARCH_ONLY")
        self.assertLessEqual(x["measured_score"],80)
