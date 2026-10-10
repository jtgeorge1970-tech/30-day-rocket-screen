import unittest
from ofts.research.fresh_audit import window_stats,keeper_status,entry_priority

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
    def test_evi_single_spike_cannot_be_keeper(self):
        evi=dict(symbol="EVI",viability="REVIEW",swing_health="DOWNTREND",
                 three_clear_cycles="REJECT_TOO_FEW_CYCLES",
                 clean_cycle_v10={"score":None},eligibility="PENDING_ELIGIBILITY")
        self.assertEqual(keeper_status(evi),"REJECT_NEW_CYCLE_GATE")
    def test_old_health_not_hard_veto(self):
        row=dict(viability="DISSIPATING",swing_health="IRREGULAR",
                 three_clear_cycles="THREE_CLEAR_CYCLES",
                 clean_cycle_v10={"score":70.0},eligibility="PENDING_ELIGIBILITY")
        self.assertEqual(keeper_status(row),"RESEARCH_KEEPER_NOT_VERIFIED_BUY")
    def test_new_gate_and_known_ineligibility_veto(self):
        row=dict(three_clear_cycles="REJECT_BIG_LOSS",
                 clean_cycle_v10={"score":None},eligibility="PENDING_ELIGIBILITY")
        self.assertEqual(keeper_status(row),"REJECT_NEW_CYCLE_GATE")
        row.update(three_clear_cycles="THREE_CLEAR_CYCLES",
                   clean_cycle_v10={"score":79.0},eligibility="INELIGIBLE")
        self.assertEqual(keeper_status(row),"INELIGIBLE")
    def test_chasing_never_entry_candidate(self):
        row=dict(current_keeper_status="RESEARCH_KEEPER_NOT_VERIFIED_BUY",
                 entry_state="CHASE_RISK_WAIT")
        self.assertEqual(entry_priority(row),"NO_CHASE")
        row["entry_state"]="REVERSAL_REVIEW"
        self.assertEqual(entry_priority(row),"REVERSAL_REVIEW_NOT_BUY")
        row["entry_state"]="UNCONFIRMED_TROUGH_WAIT"
        self.assertEqual(entry_priority(row),"TROUGH_WATCH_NOT_BUY")
    def test_insufficient_window(self):
        self.assertEqual(window_stats(bars([10.0]*20),30)["status"],"INSUFFICIENT")

if __name__=="__main__":unittest.main()
