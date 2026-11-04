# OFTS independent completed-trade and matched benchmark audit — November 4, 2026

RESEARCH ONLY. No production changes, orders, or rule changes.

Sources: GitHub frozen `ofts-daily-state/cycle_ledger.json` generated 2026-11-04 11:37:06 UTC, and independent Alpaca SIP daily OHLC data October 9 through November 4 fetched after the November 4 close for 41 ledger symbols plus SPY and IWM (43 symbols, 817 bars). The ledger is a morning snapshot and **does not yet establish November 4 completed exits**. All six completed entries/exits through November 3 are counted below. Each hypothetical trade uses its recorded entry-day open and exit-day open, less 0.20 percentage points assumed round-trip cost. SPY/IWM matched entry/exit open-to-open using identical dates and same assumed cost. This is equal-weight per-trade comparison, not portfolio P&L, not an investable benchmark portfolio, and not verified fills.

| Trade | Entry date | Exit date | Strategy net | SPY matched net | IWM matched net |
|---|---|---|---:|---:|---:|
| YDES | 2026-10-12 | 2026-10-23 | -39.14% | -2.62% | -1.50% |
| MF | 2026-10-16 | 2026-10-28 | -23.84% | -0.43% | +1.55% |
| CCS | 2026-10-23 | 2026-10-30 | -4.37% | 0.00% | +2.39% |
| MH | 2026-10-16 | 2026-11-02 | -8.01% | -1.98% | +2.02% |
| AKAM | 2026-10-27 | 2026-11-03 | -11.17% | -2.10% | +0.48% |
| XPRO | 2026-10-28 | 2026-11-03 | -15.73% | -2.62% | -0.38% |
| **Mean** | | | **-17.04%** | **-1.63%** | **+0.76%** |

Six of six completed trades lost. The median is about -13.45%. Even excluding the two worst losses (YDES, MF), the remaining four average -9.82%. This is a severe warning, though N=6 is below the locked minimum. No evidence of realized positive net edge or benchmark outperformance.

New entries in morning ledger: EEFT and PAMT on Nov 3, both open. EME and GEV were pending for Nov 4; market bars show EME open $670 and GEV open $855.245, but ledger **has not confirmed hypothetical execution**, so DO NOT count as entries. Nov 4 market close marks (not realized): EEFT entry $66.16 -> $70.65, net +6.59%; PAMT $12.28 -> $12.38, net +0.61%; NIPG $4.14 -> $4.16, net +0.28%; TARS $74.88 -> $69.07, net -7.96%. TARS Nov 4 low $65.3425 breached proposed 6% initial stop $70.3872; stop execution price cannot be verified from OHLC. NIPG Nov 2 low $3.60 breached its proposed stop $3.8916; Nov 4 volume only 14,004 shares, highly illiquid. Neither proposed stop is production active; these are counterfactuals.

Prior Nov 3 same-stock equal-horizon in-sample entry comparison, NOT rerun with Nov 4 data here:
3 sessions N23 original +2.414%, delay2 +1.138%, reversal +0.793%;
5 sessions N15 original +3.030%, delay2 +5.884%, reversal +4.549%;
8 sessions N8 original +2.091%, delay2 +13.153%, reversal +6.637%.
After excluding top 3, five-session delay2 +0.561%, and three-session delay2 -2.083%. This remains unstable and not independent prospective proof.

Execution caveats: SIP OHLC daily bars do not reveal bid/ask spread, order size, actual stop fills, or intraday high/low order. Initial/trailing stop rules remain unapproved and research-only. For some illiquid names stop level fills may be optimistic. Completed signal cohort and completed trades are distinct concepts.

LOCKED checkpoints: day 10 20–30 independent completed trades; day 30 50; day 60 100 required for GO/NO-GO; extend to day 90/150 only if promising and evidence insufficient. Currently 6/100 completed trades, all losing. **RESEARCH_ONLY_NO_GO**. No orders or production changes. Next: reconcile November 4 exits, freeze the prospective entry variant, collect sufficient independent closes, measure liquidity and matched benchmarks.