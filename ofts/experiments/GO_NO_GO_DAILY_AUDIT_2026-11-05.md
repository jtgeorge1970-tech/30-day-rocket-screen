# OFTS November 5, 2026 independent daily validation audit

RESEARCH ONLY; no orders or production changes.

Sources: `ofts-daily-state/cycle_ledger.json` generated 2026-11-05 11:39:51 UTC (morning snapshot), Alpaca SIP daily OHLC 2026-10-09 through 2026-11-05 for 46 ledger symbols plus SPY and IWM (48 symbols, 960 bars), fetched after Nov 5 close. Bars not verified execution fills. Daily market date Nov 5.

## Completed ledger exits through November 4

Ten completed ledger trades: YDES -39.144%, MF -23.840%, CCS -4.367%, MH -8.009%, AKAM -11.168%, XPRO -15.734%, ACDC -9.961%, ATGL +25.660%, BETR +77.234%, MATV -3.190%. All use recorded next-session entry open and exit open, less assumed 0.20 percentage points roundtrip. Two wins and eight losses. Equal-weight mean -1.252%; median -8.985%. Same-date SPY matched average -1.365%, IWM +1.429%. Excluding three best trades (BETR, ATGL, MATV) gives -16.032% mean across seven. Results are strongly dependent on two outlier winners and fail robustness and IWM benchmark. Ten of 100 required completed trades; trades can overlap and are not necessarily statistically independent.

Four OPEN_PENDING_EXIT as of morning ledger (ATEX, CQP, EME, LTRX) scheduled November 5. Their Nov 5 open hypothetical returns, if subsequently ledger-confirmed, would be -12.641%, -12.508%, -8.981%, -12.740% respectively, after assumed costs. **Do not count as completed until ledger confirms**. New Nov 4 ledger-confirmed entries EME $670 and GEV $855.245; Nov 5 closes $595.32 and $770.51, giving open mark-to-market -11.346% and -10.108%, respectively. These are NOT completed trades. Five additional pending Nov 5 entries are not yet ledger-confirmed.

## Fresh same-stock equal-horizon entry-timing screen

42 recorded entry events through Nov 4, filtered within each horizon to those with complete 3/5/8 trading-session future OHLC and eligible original, two-session delay, and bullish reversal confirmation. Entry original at recorded entry date open; delay at two sessions later open; reversal requires first of original or following session with close > open and close > preceding close, then buy following open. Equal 3/5/8 sessions after each respective entry. 6% initial stop, activate 8% trailing after prior high reaches +10%; if next open gaps below stop fill at open, otherwise optimistic stop-level fill on low breach; daily high/low ordering not known. Close at last session if no stop. Deduct 0.20 pp. Samples differ across horizons; all in-sample and overlap.

| Horizon | Common N | Original mean | Delay2 mean | Reversal mean | Delay2 mean excluding top three |
| 3 sessions | 25 | +2.171% | +1.147% | +0.907% | -2.029% |
| 5 sessions | 23 | +1.312% | +2.096% | +1.225% | -1.666% |
| 8 sessions | 14 | +3.016% | +9.342% | +6.620% | +2.768% |

At 3 sessions delay2 loses to original. At 5 sessions delay2 advantage is outlier-dependent; 8-session N14 remains too small. The reversal signal is not reliably superior. No validated prospective edge. The OHLC stop simulation is optimistic and not a real fill model.

## Risk and decision

At least one completed trade (YDES) lost -39.14%; fixed 6% stops would have altered the path, but they are not approved and do not guarantee a maximum loss due to overnight gaps. November 5 ACDC price fell from Nov 4 close $3.97 to Nov 5 open $3.77 and close $2.71 (post-exit risk illustration, not ledger P&L). Thin names such as ATGL have extremely low daily share volume (2,914 on Nov 5); no verified bid/ask slippage or feasible size. Stop-limit and market-stop fills cannot be inferred from OHLC. No production orders or rule changes.

Locked protocol: day 10 target 20–30 independent completed trades; day 30 50; day 60 minimum 100 and primary GO/NO-GO; day 90 150+ only if promising. Current ledger 10/100 completed (2 wins, 8 losses). **RESEARCH_ONLY_NO_GO**. Need prospective frozen strategy, completed exit reconciliation, spreads and matched benchmarks; do not move criteria.
