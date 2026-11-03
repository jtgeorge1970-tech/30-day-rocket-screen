# OFTS fresh-data entry validation — November 3, 2026

Research-only; no production changes or orders. Source ledger: ofts-daily-state/cycle_ledger.json, generated 2026-11-03T11:21:37Z. Frozen development SIP OHLC: ofts/experiments/SIP_DAILY_BARS_2026-10-09_TO_2026-10-30.csv. New independent Alpaca SIP 1Day OHLC: Oct 28-Nov 3 inclusive, fetched November 3 after market close. 39 ledger symbols plus SPY/IWM returned.

The ledger currently reports 34 open, 4 closed, 2 pending, 17 completed signal cohorts. Two newly executed Nov 2 hypothetical entries: NIPG $4.14, TARS $74.88. November 3 close NIPG $3.80 (-8.21% gross, -8.41% with assumed 0.20% round-trip cost), TARS $72.64 (-2.99% gross, -3.19% after cost). Both remain open in ledger; not realized. NIPG Nov 2 low $3.60 already below a 6% initial stop of $3.8916. On daily OHLC this indicates stop breach, but exact fill unverified and NIPG liquidity is extremely low (Nov 3 volume 6,427 shares); modeled threshold fills may be unrealistic.

Comparison: same eligible trades within each row, fixed 3, 5, or 8-session holding horizons counted from each variant's own entry. Original entry = original signal next-session open; two-day delay = open 2 sessions after original entry; confirmed reversal = buy next open after first of original-entry day or next day showing close > open and close > prior daily close. Only trades with enough observed daily bars for all 3 variants and whose fixed horizon does not extend past the recorded actual exit date are included. Each variant has fixed initial 6% stop and trailing 8% after prior observed high >=10% gain, with original floor; gap below stop uses worse open, intraday breach uses optimistic stop level, no reentry, assumed 0.20 percentage points costs. All values hypothetical and selected in-sample.

| Horizon | Common N | Original mean | Delay2 mean | Reversal mean | Original excluding top 3 | Delay2 excluding top 3 | Reversal excluding top 3 |
| 3 | 23 | +2.414% | +1.138% | +0.793% | +0.356% | -2.083% | -2.810% |
| 5 | 15 | +3.030% | +5.884% | +4.549% | +0.771% | +0.561% | -0.786% |
| 8 | 8 | +2.091% | +13.153% | +6.637% | -3.806% | +1.516% | -5.151% |

The previous two-day-delay advantage does NOT persist at the 3-session horizon with more data: original +2.414% vs delay +1.138%. Delay retains a lead at 5 and 8 sessions but tiny samples and outlier sensitivity. Not a robust confirmed edge. The 8-session delayed variant has 7 positive / 8 and worst -1.394%, but N=8 is far below 100 independent completed trades. Different horizons have different eligible sets; multiple entries in the same stock and overlapping periods are not independent. The reported horizon closes are hypothetical exits, not completed ledger trades.

SPY Oct30 close 755.72 -> Nov3 close 754.35 (-0.181%); IWM 279.33 -> 279.79 (+0.165%). These market moves are context, NOT matched entry-date benchmarks. Matched per-entry SPY/IWM controls remain to be implemented. Real spread/fees/slippage and intraday stop order cannot be proven from daily bars. Some symbols are extremely illiquid.

**Locked GO/NO-GO:** Day 10 target 20-30 independent completed; day 30 target 50; day 60 require 100 independent completed; day 90 only if promising and inconclusive. Must outperform benchmarks net of realistic costs, protect downside and remain profitable without 2-3 outliers. Current ledger: 4 completed, not 100. RESEARCH_ONLY_NO_GO. Continue fresh forward testing with frozen entry rules and same-stock paired controls; no live trading.
