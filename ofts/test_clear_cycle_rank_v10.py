import unittest
from ofts.research.clear_cycle_rank_v10 import score_clear_cycles
from ofts.research.three_clear_cycles_v09 import three_clear_cycles
from ofts.test_three_clear_cycles_v09 import ThreeClearCycleTests

class RankTests(unittest.TestCase):
    def test_not_qualified_cannot_score(self):
        self.assertIsNone(score_clear_cycles({"state":"REJECT_CHOPPY_SWINGS"})["score"])
    def test_clean_score_components_and_eligibility(self):
        clear=three_clear_cycles(ThreeClearCycleTests().good())
        self.assertEqual(clear["state"],"THREE_CLEAR_CYCLES")
        pending=score_clear_cycles(clear)
        verified=score_clear_cycles(clear,"PASS")
        self.assertEqual(round(verified["score"]-pending["score"],3),8)
        self.assertEqual(len(pending["components"]),6)
        self.assertLessEqual(pending["score"],100)
    def test_known_ineligible(self):
        clear=three_clear_cycles(ThreeClearCycleTests().good())
        self.assertEqual(score_clear_cycles(clear,"INELIGIBLE")["status"],"INELIGIBLE")
if __name__=="__main__":unittest.main()
