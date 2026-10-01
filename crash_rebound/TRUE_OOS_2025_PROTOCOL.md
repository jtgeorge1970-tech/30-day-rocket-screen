# Crash Rebound — Frozen True Out-of-Sample Validation Protocol

## Freeze timestamp
Rule frozen before opening any 2025 post-signal outcomes.

## Untouched validation period
Calendar year 2025. No 2025 data was used in development, targeted expansion, threshold selection, or Day-1 technical rule construction.

## Source universe
For each month January–December 2025:
- StockTitan monthly Top News Losers final board
- Top 100 ranked events per month where available under the same source acceptance gate used in 2026 work

## Frozen mechanical pre-screen
An event qualifies for Day-1 technical evaluation only if:
1. Crash magnitude <= -30%
2. Crash-day relative volume >= 5.0x the prior-20-session median daily volume
3. RSP prior-5-session return > -1.0%

No headline/news classification is used.

## Frozen Day-1 confirmation signal
Signal is TRUE only when all three are true on the first trading session after the crash:
1. Day-1 low >= crash-day low
2. Day-1 close > crash-day midpoint, where midpoint = (crash-day high + crash-day low) / 2
3. Day-1 opening gap versus crash-day close > -5.0%

## Frozen trade measurement
- Entry: Day-1 close
- Primary exit: Day-10 close
- Secondary reported horizons: Day-3 and Day-5 close
- No stop-loss optimization is part of the primary validation rule
- No slippage/commissions are included in raw research returns; this must be stated in interpretation

## Acceptance reporting
Report, without changing the rule:
- Total source events
- Mechanical pre-screen count
- Day-1 signal count
- Day-3, Day-5, Day-10 post-entry positive-return rate
- Median and mean post-entry return at each horizon
- Worst post-entry return
- Maximum adverse excursion from entry where available
- Month distribution
- Any missing-data cases

## Integrity rule
Do not alter thresholds, signal conditions, entry, exit, or validation period after outcomes are viewed. Any later variant is a new hypothesis and must be tested on a different untouched sample.
