import unittest
from ofts.research.three_clear_cycles_v09 import three_clear_cycles

def series_from_knots(knots):
    out=[knots[0][1]]
    for (a,x),(b,y) in zip(knots,knots[1:]):
        for i in range(1,b-a+1):
            out.append(x+(y-x)*i/(b-a))
    return out

class ThreeClearCycleTests(unittest.TestCase):
    def good(self):
        knots=[(0,10),(10,11.1),(20,10.1),(30,11.2),(40,10.2),
               (50,11.3),(60,10.3),(70,11.4),(80,10.4),
               (90,11.5),(100,10.5),(110,11.6),(125,10.6)]
        return series_from_knots(knots)
    def test_three_clear_cycles_with_small_noise(self):
        p=self.good()
        r=three_clear_cycles(p)
        self.assertEqual(r["state"],"THREE_CLEAR_CYCLES")
        self.assertEqual(r["qualifying_last_three"],3)
        self.assertTrue(all(c["rise_pct"]>=5 and c["fall_pct"]>=5 for c in r["cycles"]))
    def test_one_large_upward_spike_is_not_three_cycles(self):
        p=[10.0]*60+[12.0]*20+[11.0]*46
        r=three_clear_cycles(p)
        self.assertNotEqual(r["state"],"THREE_CLEAR_CYCLES")
    def test_big_loss_vetoes_three_good_cycles(self):
        p=self.good()
        p[119]=p[118]*.82
        r=three_clear_cycles(p)
        self.assertEqual(r["state"],"REJECT_BIG_LOSS")
    def test_drawdown_veto(self):
        p=self.good()
        p[70:85]=[15.0]*15
        r=three_clear_cycles(p)
        self.assertEqual(r["state"],"REJECT_BIG_LOSS")
    def test_old_loss_does_not_veto_recent_clean_cycles(self):
        p=self.good()
        p[:15]=[15.0]*15
        self.assertEqual(three_clear_cycles(p)["state"],"THREE_CLEAR_CYCLES")
    def test_one_giant_rally_among_three_cycles_is_outlier(self):
        p=self.good()
        for i in range(21,41):p[i]*=1.7
        self.assertNotEqual(three_clear_cycles(p)["state"],"THREE_CLEAR_CYCLES")
    def test_insufficient(self):
        self.assertEqual(three_clear_cycles([10.0]*100)["state"],"INSUFFICIENT")

if __name__=="__main__":unittest.main()
