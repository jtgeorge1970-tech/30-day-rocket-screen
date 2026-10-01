# Crash Rebound — True Untouched 2025 OOS Validation

## Frozen rule
Frozen before viewing 2025 outcomes in commit:
14eff642193414457de894239939eee0d4693fca

Mechanical event screen:
1. Crash >= 30%
2. Crash-day relative volume >= 5x prior-20-session median
3. RSP prior-5-session return > -1%

Day-1 confirmation:
4. Day-1 low holds crash-day low
5. Day-1 close above crash-day midpoint
6. Day-1 opening gap vs crash close > -5%

Execution:
- Entry: Day-1 close
- Primary exit: Day-10 close
- Secondary: Day-3 and Day-5 close
- No news/headline classification used

## Validation universe
- Calendar year 2025 only
- 12 untouched months
- 1,200 source events
- 342 crashes >=30%
- 205 passed the mechanical base screen
- 204 had Day-1 data
- 51 triggered the full frozen Day-1 rule
- Trigger candidates were committed before outcomes:
  e7bb41bad89d63d48e4f99109918a32c708208b8

## Untouched results
### Day 3 from Day-1 close
- N=51
- Positive: 43.1%
- Median: -1.09%
- Worst: -26.12%
- Best: +1549.17%

### Day 5 from Day-1 close
- N=51
- Positive: 41.2%
- Median: -1.85%
- Worst: -47.60%
- Best: +1602.45%

### Day 10 from Day-1 close
- N=51
- Positive: 41.2%
- Median: -3.14%
- Worst: -45.95%
- Best: +1705.74%

### Risk
- Median maximum adverse excursion through Day 10: -10.70%
- Worst maximum adverse excursion: -64.59%

## Interpretation
The frozen technical rule fails the pre-specified validation gate:
- Day-10 median is negative.
- Day-10 positive-trade rate is below 50%.
- Performance is inconsistent across months.
- Downside is materially worse than the development sample.

The very large positive outliers make arithmetic means misleading and should not be used to claim success. Median and win-rate behavior are unfavorable.

Conclusion: this exact crash-rebound trigger is NOT validated and should not be promoted to a live trading rule.
