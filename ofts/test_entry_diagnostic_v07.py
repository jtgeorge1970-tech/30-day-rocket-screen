import unittest
from datetime import date, timedelta
from ofts.research.entry_diagnostic_v07 import entry_diagnostic

def dates(n, today=date(2026,10,9)):
    return [(today-timedelta(days=n-i-1)).isoformat() for i in range(n)]

class TestEntryDiagnostic(unittest.TestCase):
    def test_breakdown_never_buy(self):
        c=[10.0]*27+[9.7,9.5,9.25]
        r=entry_diagnostic(c,dates(len(c)),today=date(2026,10,10))
        self.assertEqual(r['state'],'BREAKDOWN_NO_TRADE')
        self.assertFalse(r['entry_confirmed'])
    def test_falling_wait_even_if_old_swings_great(self):
        c=[9.0]*10+[10.0]*14+[9.8,9.7,9.6,9.5,9.4,9.3]
        r=entry_diagnostic(c,dates(len(c)),today=date(2026,10,10))
        self.assertIn(r['state'],('FALLING_WAIT','BREAKDOWN_NO_TRADE'))
        self.assertIsNone(r['entry_points'])
    def test_stale_data_is_not_current_buy(self):
        c=[9.0]*15+[9.5]*15
        r=entry_diagnostic(c,dates(len(c),date(2026,9,20)),today=date(2026,10,10))
        self.assertEqual(r['state'],'STALE_DATA')
        self.assertFalse(r['entry_confirmed'])
    def test_unconfirmed_trough(self):
        c=[9.0]*10+[9.6]*10+[9.2]*10
        r=entry_diagnostic(c,dates(len(c)),today=date(2026,10,10))
        self.assertEqual(r['state'],'UNCONFIRMED_TROUGH_WAIT')
    def test_no_future_dates(self):
        c=[9.0]*30
        r=entry_diagnostic(c,dates(len(c),date(2026,10,20)),today=date(2026,10,10))
        self.assertEqual(r['state'],'STALE_DATA')
    def test_short(self):
        self.assertEqual(entry_diagnostic([9.0]*5,dates(5),today=date(2026,10,10))['state'],'INSUFFICIENT_DATA')
if __name__=='__main__': unittest.main()
