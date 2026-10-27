# OFTS research-only reentry cooldown sensitivity — 2026-10-27

**Verdict: NO-GO unchanged.** This is a new *exploratory*, chronological replay of the existing 24 historical hypothetical trades from six training-selected stocks (AEHR, AXTI, HOOD, PLTR, ROCK, STX). It is **not** a new unseen out-of-sample experiment, and it does not change production logic. Source is `ofts/validation/cycle_execution_trades.csv` on the isolated `ofts-go-no-go-20261025` research branch.

## Method
Sort original next-open BUY entries by entry date. After a retained trade exits, suppress the next entry in the **same symbol** if its entry date falls within 7, 14, or 30 **calendar days** of the last *retained* exit. Blocked signals do not start new positions or reset the cooldown. Use each original saved net return (0.20 percentage point assumed round-trip cost). This does **not** model altered positions, trading-day calendars, spread/slippage, or portfolio capital constraints. Blocked signals are assigned zero return only for the *per-original-opportunity* arithmetic sensitivity; that measure is not a portfolio return. Parameter choices and analysis are post-hoc.

| Cooldown calendar days | Retained/24 | Winners | Mean net per retained trade | Median net | Worst trade | Mean if blocked opportunities earn 0% |
|---|---:|---:|---:|---:|---:|---:|
| 0 (unchanged) | 24 | 12 | +13.252% | -0.825% | -66.227% | +13.252% |
| 7 | 19 | 11 | +21.495% | +2.460% | -35.291% | +17.017% |
| 14 | 17 | 8 | +7.178% | -2.615% | -66.227% | +5.085% |
| 30 | 16 | 8 | +8.630% | -0.825% | -66.227% | +5.753% |

Seven-calendar-day cooldown blocks five original trades: AEHR 2026-03-11 (-13.867%), AXTI 2026-05-26 (-66.227%), AEHR 2026-06-03 (-11.943%), STX 2026-06-15 (-23.993%), and AEHR 2026-07-31 (**+25.673%**). The seven-day improvement is highly sample-dependent and does not justify adopting that threshold. The 14-day rule blocks the +137.112% STX and +94.001% AXTI winners while retaining the -66.227% AXTI loss, illustrating unstable parameter sensitivity.

**Prospective concern:** In the separate frozen October 2026 hypothetical ledger, YDES closed at -39.144% net on October 23 and was hypothetically reentered on October 26 (three calendar days later). A seven-day cooldown would have blocked that *reentry*, but its subsequent outcome is not yet known. This is a hypothesis, not validated protection.


## Chronological stress split (still not independent holdout)

As a separate diagnostic, order the 24 trades by entry date and split the first 16 opportunities (through the sixteenth entry) from the last eight (starting with the April 17, 2026 PLTR entry). Retain cooldown state from earlier accepted trades across the split. Report mean net return per **original opportunity**, assigning 0% to blocked entries (not a portfolio return):

| Calendar-day cooldown | First 16 opportunities | Last 8 opportunities |
|---|---:|---:|
| 0 days | +27.983% | **-16.210%** |
| 7 days | +28.849% | **-6.648%** |
| 14 days | +11.861% | **-8.467%** |
| 30 days | +11.861% | **-6.462%** |

The seven-day cooldown improves the latter segment relative to unchanged baseline but the latter segment **remains substantially negative**. These eight observations are not untouched holdout evidence because the six symbols were training-selected, the experiment was proposed after reviewing earlier results, and there is no liquidity, SPY/IWM, same-stock passive, or portfolio drawdown control. No GO.

## Decision
These training-selected, post-hoc results are **not a basis for GO**. The original mean is concentrated in three extreme winners. Require a prespecified cooldown rule tested chronologically on unseen symbols/dates with realistic fills, identical trade opportunities, same-stock passive controls, SPY/IWM, tail risk and drawdowns. Preserve unchanged baseline and do not deploy any experimental rule.

Reproduce: `python ofts/experiments/reentry_cooldown_calendar_20261027.py`.
