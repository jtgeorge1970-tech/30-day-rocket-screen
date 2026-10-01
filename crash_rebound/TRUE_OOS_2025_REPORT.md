# Crash Rebound — TRUE OOS 2025 Validation Result

## Frozen protocol
Protocol was frozen before 2025 outcomes were opened.
Protocol commit: d7e531a906586ac4b30ee3aa7da1b0277fcf3282

Frozen rules:
- Crash >=30%
- Crash-day relative volume >=5x prior-20-session median
- RSP prior-5 > -1%
- Day-1 low >= crash-day low
- Day-1 close > crash-day midpoint
- Day-1 opening gap > -5%
- Entry at Day-1 close
- Primary exit at Day-10 close

No news classification was used.

## Validation universe
- 12 untouched 2025 monthly source cohorts
- 1,200 source events
- 342 crashes >=30%
- 205 passed the full mechanical pre-screen
- 51 produced the frozen Day-1 technical signal
- 4 mechanically screened cases lacked enough future bars for the Day-10 signal evaluation stage and remained unavailable rather than guessed

## Primary result
### Day 1 close -> Day 10 close
- N = 51
- Positive-return rate = 41.2%
- Median return = -3.14%
- Mean return = +65.62% (not representative because of extreme outliers)
- Worst return = -45.95%
- Best return = +1705.74%
- Median maximum adverse excursion from Day 2 through Day 10 = -10.70%
- Mean maximum adverse excursion = -16.78%
- Worst maximum adverse excursion = -64.59%
- Median maximum favorable excursion = +9.75%

### Secondary horizons
Day 1 close -> Day 3 close:
- Positive-return rate = 43.1%
- Median = -1.09%

Day 1 close -> Day 5 close:
- Positive-return rate = 41.2%
- Median = -1.85%

## Outlier robustness
Several micro/small-cap moves created extreme positive arithmetic means:
- OTLY Day-10 +1705.74%
- MNTS Day-10 +884.23%
- UNCY Day-10 +876.98%

Removing only the single largest winner:
- N=50
- Positive-return rate=40.0%
- Median Day-10=-4.68%
- Mean Day-10=+32.82%

Restricting to observations below +500% solely as a robustness diagnostic, not as a rule change:
- N=48
- Positive-return rate=37.5%
- Median Day-10=-6.59%
- Mean Day-10=-2.51%

These robustness checks confirm that the positive raw mean is driven by rare extreme outliers and does not represent the typical trade.

## Conclusion
The frozen Day-1 technical setup FAILED true out-of-sample validation.

The typical trade was negative at Day 3, Day 5, and Day 10. The Day-10 median was -3.14%, only 41.2% of trades were positive, and adverse excursion was large. The large positive mean was produced by a few extreme outliers.

This result does not support promotion of the frozen Day-1 rule to a live trading trigger.

Any future variant must be treated as a new hypothesis and tested on a different untouched sample. Do not revise this 2025 validation rule after seeing the result.
