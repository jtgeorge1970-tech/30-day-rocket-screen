# OFTS research audit — 2026-11-06

Read-only validation; no production changes or trading orders. Sources: frozen OFTS ledger branch `ofts-daily-state/cycle_ledger.json` generated 2026-11-06 11:33:30 UTC, and fresh Alpaca SIP 1Day bars from 2026-10-09 to 2026-11-06 for 48 symbols (1007 records). Ledger is a morning snapshot, so Nov 6 scheduled exits are NOT counted completed.

## Completed ledger trades through Nov 5
14 completed (2 wins, 12 losses); mean -4.2421%, after 0.20 percentage points assumed roundtrip costs; median approximately -11.5%. Same-date matched SPY average -1.2063%; IWM +1.3979% (each benchmark also charged 0.20 pp). Excluding best two: -13.5236%; excluding best three: -14.4630%. Newly completed vs Nov 5: ATEX -12.6406%, CQP -12.5077%, EME -8.9806%, LTRX -12.7397%. These are ledger-confirmed hypothetical open-to-open, not actual fills.

## Five planned Nov 6 exits, NOT ledger-confirmed
Nov 6 SIP opening prices imply (after 0.20 pp): CIM -3.4099%; GEV -6.9834%; MESO +5.5402%; NIPG -16.6251%; RELL -17.3115%. Exclude from completed count until ledger reconciliation.

## Five ledger-confirmed Nov 5 entries
ACRE 3.54; AUGO 74.395; CIM 8.10; GDEV 8.59; PTRN 18.50. Nov 6 close hypothetical marks after 0.20 pp: ACRE +2.9073%; AUGO +4.4038%; CIM -9.9531%; PTRN -1.4432%. No SIP Nov 6 bar returned for GDEV, so no mark inferred. These are not completed trades.

## Equal-horizon, same-stock research entry-timing screen
For each 3/5/8-session horizon, retain only ledger entry events where original, delay-two, and reversal confirmation all have sufficient observed bars. Original: recorded entry open; delay: open two sessions later; reversal: bullish daily close > open and previous close on original or following session, buy next open. 6% initial stop, 8% trailing once high reaches +10%; gap-through filled at open, otherwise optimistic stop threshold fill. Exit final horizon close if no stop; 0.20 pp costs. In-sample and overlapping.

| Horizon | Common events | Original avg | Delay-two avg | Reversal avg | Delay-two excluding top 3 |
|---|---:|---:|---:|---:|---:|
| 3 | 25 | +2.171% | +1.147% | +0.907% | -2.029% |
| 5 | 24 | +0.999% | +1.750% | +0.916% | -1.882% |
| 8 | 15 | +4.167% | +8.306% | +7.016% | +2.021% |

No robust entry edge: delay-two loses at 3 sessions; at 5 sessions its mean turns negative without top three. At 8 sessions sample only 15 and optimistic stop fills.

## Risk and locked decision
NIPG Nov 6: open $3.46, low $3.20, close $3.72, 6,288 shares and 193 trades; prior original entry $4.14, theoretical 6% stop $3.8916, demonstrating gap/slippage exposure. Daily OHLC cannot verify executable stop or spreads. 14/100 required independent completed trades (independence not yet established); 10-day 20–30, 30-day 50, 60-day >=100, optional 90-day 150+ only if promising. Benchmark outperformance, outlier robustness, and execution realism FAIL or unverified. **RESEARCH_ONLY_NO_GO**.
