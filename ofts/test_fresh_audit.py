import unittest
from ofts.research.fresh_audit import window_stats,keeper_status

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
    def test_evi_single_spike_and_downtrend_never_keeper(self):
        evi=dict(symbol="EVI",viability="REVIEW",swing_health="DOWNTREND",
                 entry_state="MID_CYCLE_WAIT",quality_v06=52.9703,
                 three_clear_cycles="THREE_CLEAR_CYCLES",
                 w30=dict(status="MEASURED",confirmed_up_legs=1),
                 w60=dict(status="MEASURED",confirmed_up_legs=3,
                          completed_peak_intervals=3,completed_trough_intervals=2))
        self.assertEqual(keeper_status(evi),"REJECT_RECENT_REPEATABILITY")
        evi["w30"]["confirmed_up_legs"]=3
        self.assertEqual(keeper_status(evi),"WATCH_TREND_OR_SWING_HEALTH")
    def test_failing_health_vetoes_big_score(self):
        self.assertEqual(keeper_status(dict(viability="DISSIPATING",three_clear_cycles="THREE_CLEAR_CYCLES",quality_v06=79.99)),
                         "REJECT_OSCILLATION_HEALTH")
    def test_three_clear_gate_blocks_historical_score(self):
        self.assertEqual(keeper_status(dict(three_clear_cycles="REJECT_BIG_LOSS",quality_v06=79.99)),
                         "REJECT_BIG_LOSS")
        self.assertEqual(keeper_status(dict(three_clear_cycles="REJECT_TOO_FEW_CYCLES",quality_v06=79.99)),
                         "REJECT_NO_THREE_CLEAR_5PCT_CYCLES")
    def test_insufficient_window(self):
        self.assertEqual(window_stats(bars([10.0]*20),30)["status"],"INSUFFICIENT")

if __name__=="__main__":unittest.main()
