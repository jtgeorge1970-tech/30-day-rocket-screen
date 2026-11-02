# OFTS preliminary entry-delay comparison — 2026-11-02

Read-only experiment. No production scoring changes or orders.

Sources: frozen `ofts-daily-state/cycle_ledger.json` as read November 2 and independent SIP `ofts/experiments/SIP_DAILY_BARS_2026-10-09_TO_2026-10-30.csv` (October 30 cutoff). Same 36 eligible historical original entries as the prior 12-grid test, but delayed alternatives have fewer eligible entries if original holding period ended before delayed entry. Entry delay d = buy at open d sessions after original entry open. Original exit date unchanged (shorter holding period). Apply 6% fixed initial stop, switching after prior observed high has reached +10% to 8% trailing from prior observed high, with initial stop floor. If gap below threshold, exit at worse next open; otherwise assume optimistic intraday threshold fill. Deduct 0.20 percentage points round-trip. Censor unclosed at October 30 close.

| Entry delay | N | Mean net % | Median net % | Worst net % | Positive |
|---|---:|---:|---:|---:|---:|
| 0 | 36 | +0.496 | -0.578 | -8.424 | 16 |
| 1 session | 35 | +1.116 | -1.963 | -9.609 | 13 |
| 2 sessions | 33 | +2.136 | -0.374 | -8.603 | 16 |
| 3 sessions | 27 | +0.312 | -1.041 | -8.475 | 12 |

Important: these rows have DIFFERENT sample sizes; apparent advantage of 2 sessions is NOT a paired improvement. The delayed variants also have shorter exposure and different entry prices, so this is a screening diagnostic, not a same-horizon fair comparison. Historical observations overlap and remain censored. Potential look-ahead in selecting best delay after seeing outcomes; must lock and prospectively test. Further compare all delays on common eligible trades, and separately compare fixed horizons and contemporaneous matched-stock passive, SPY, IWM. Thin-stock spreads and realistic stop fills are not validated. No strategy GO.
