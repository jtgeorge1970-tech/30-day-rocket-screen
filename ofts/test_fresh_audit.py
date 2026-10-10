import unittest
from ofts.research.fresh_audit import window_stats

def bars(values):
    return [{"date":f"2026-01-{i+1:02d}","open":x,"high":x*1.01,
             "low":x*.99,"close":x,"volume":1000} for i,x in enumerate(values)]

class TestChartShape(unittest.TestCase):
    def test_window_high_low_and_return(self):
        b=bars([10.0]*26+[9.0,9.5,9.2,9.25])
        w=window_stats(b,30)
        self.assertEqual(w["sessions"],30)
        self.assertAlmostEqual(w["high"],10.1)
        self.assertAlmostEqual(w["low"],8.91)
        self.assertAlmostEqual(w["return_pct"],-7.5)
    def test_one_rally_not_repeatable_oscillator(self):
        b=bars([10.0]*20+[12.0]*20)
        w=window_stats(b,30)
        self.assertEqual(w["confirmed_up_legs"],0)
        self.assertIsNone(w["up_median_pct"])
    def test_insufficient_window(self):
        self.assertEqual(window_stats(bars([10.0]*20),30)["status"],"INSUFFICIENT")

if __name__=="__main__":unittest.main()
