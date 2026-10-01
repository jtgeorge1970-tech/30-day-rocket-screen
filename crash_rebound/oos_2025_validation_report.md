# Crash Rebound — True Out-of-Sample Validation (2025)

## Frozen rule
The rule was frozen in CRASH_REBOUND_SSOT.md before 2025 forward outcomes were opened:
- Crash magnitude >= 30%
- Crash-day relative volume >= 5x prior-20-session median
- RSP prior-5-session return > -1%
- Day 1 low holds at or above the crash-day low
- Day 1 close above the crash-day midpoint
- Day 1 opening gap versus crash close better than -5%
- Entry: Day 1 close
- Evaluation exits: Day 5 and Day 10 closes
- No news classification used
- No threshold changes after validation outcomes

## Validation universe
- Calendar year 2025, untouched during development
- 1,200 monthly top-loser source events reconstructed
- 342 events had crash magnitude >=30%
- Split-adjusted Yahoo Finance daily bars were used as the primary validation feed to reduce corporate-action distortion and improve coverage versus Alpaca IEX
- 56 >=30% crash events still lacked sufficient adjusted data/window and remain unresolved
- 50 events passed the complete frozen rule
- Qualifiers appeared in 11 of 12 months

## Results
### Day 5 from Day-1 close
- N = 50
- Win rate = 36.0%
- Median return = -3.25%
- Mean return = -2.27%
- 25th percentile = -9.90%
- 75th percentile = +2.80%
- Worst = -32.89%
- Best = +36.00%

### Day 10 from Day-1 close
- N = 50
- Win rate = 38.0%
- Median return = -6.79%
- Mean return = -1.85%
- 25th percentile = -18.02%
- 75th percentile = +6.70%
- Worst = -45.24%
- Best = +89.51%

### Day-10 adverse excursion
- Median maximum additional downside = -13.50%
- 25th percentile maximum additional downside = -23.17%
- Worst maximum additional downside = -55.29%

## Month distribution
- Jan: 3
- Feb: 7
- Mar: 1
- Apr: 0
- May: 9
- Jun: 6
- Jul: 3
- Aug: 5
- Sep: 4
- Oct: 3
- Nov: 3
- Dec: 6

The rule did well in a few pockets (notably July/August) but failed across the full untouched year.

## Data-integrity note
The first Alpaca IEX pass found only 205 of 342 crash-day bars and produced 24 qualifiers. It also generated an obviously distorted MNTS forward return because MNTS executed a 1-for-17.85 reverse split on December 18, 2025. The adjusted validation feed corrected the MNTS distortion and increased the qualifying sample to 50. The company and Nasdaq both document the reverse split.

## Verdict on this candidate
The frozen Day-1 technical rule does not validate out of sample. Its development-period edge was regime/sample-specific and should not be promoted to a trading trigger.

Do not retune this same rule on 2025 and then call the result out-of-sample validation.
