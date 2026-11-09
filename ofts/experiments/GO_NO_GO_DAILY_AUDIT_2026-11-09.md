# OFTS read-only validation audit — 2026-11-09

Sources: `ofts-daily-state/cycle_ledger.json` generated 2026-11-07T10:44:00Z; independently retrieved Alpaca SIP daily bars for 47 ledger symbols plus SPY and IWM through 2026-11-06 (1029 total bars). November 9 SIP request returned `sip_delay_window`; IEX November 9 observations are separate and NOT used as SIP-equivalent executions. No orders or production changes.

## Completed frozen ledger trades
19 closed hypothetical trades, 3 wins / 16 losses, mean -5.1673% per trade after 0.20 percentage-point assumed roundtrip costs, median -9.9614%. Excluding top 2: -11.8278%; excluding top 3: -12.9133%. Same-date matched benchmark open-to-open mean after same assumed 0.20pp costs: SPY -1.9996% and IWM +0.0013%, 19/19 available. Compared with Nov 6 report's 14 closed, 5 newly ledger-confirmed Nov 6 exits: CIM -3.4099%, GEV -6.9834%, MESO +5.5402%, NIPG -16.6251%, RELL -17.3115%. None of these are real fills.

## Same-stock equal-horizon entry comparisons
Original: ledger entry open. Delay-two: open 2 trading sessions later. Reversal: first bullish daily close > open and > previous close on original entry day or following session; enter subsequent open. Require all 3 alternatives available for each event/horizon. Initial stop 6%, trailing 8% activated at +10% observed high, gap-through at next open, otherwise optimistic threshold stop. Horizon exit at last session close. 0.20pp assumed costs. Highly overlapping in-sample observations.

| Horizon | N | Original mean | Delay-two mean | Reversal mean | Delay-two ex top 3 |
|---|---:|---:|---:|---:|---:|
| 3 sessions | 25 | +2.171% | +1.147% | +0.907% | -2.029% |
| 5 sessions | 24 | +0.999% | +1.750% | +0.916% | -1.882% |
| 8 sessions | 15 | +4.167% | +8.306% | +7.016% | +2.021% |

No new SIP sessions since the Nov 6 report, so these figures independently reproduce rather than extend the prior timing audit.

## November 9 IEX-only preliminary observations
MLP scheduled entry Nov 9: no IEX daily bar returned, so no entry confirmation. YDES scheduled exit Nov 9: IEX bar open $6.68 with only 368 IEX shares, NOT a confirmed full-market SIP exit. IEX closes: ACRE $3.695, AUGO $87.03, PTRN $19.42, TARS $70.85, EEFT $70.96. GDEV no IEX bar. These are exchange-limited indications, not complete-market marks and are excluded from trade metrics.

## Risk / locked decision
NIPG original entry $4.14, Nov 6 SIP exit open $3.46 (-16.63% net), versus 6% theoretical stop $3.8916; daily OHLC cannot establish stop execution. Spreads and realistic market impact not verified. No evidence of a robust repeatable entry edge. Only 19 of >=100 independent completed trades (independence not established). 10-day 20–30, 30-day 50, 60-day >=100, optional 90-day 150+ if promising remain LOCKED. **RESEARCH_ONLY_NO_GO**.