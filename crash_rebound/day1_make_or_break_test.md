# Crash Rebound — Make-or-Break Day-1 Technical Test

## Universe
111 mechanically selected crash events from untouched Jan/Feb/May/Jun/Jul 2026 months:
- crash >=30%
- relative volume >=5x
- RSP prior-5 > -1%
No news/opinion classification used in the technical decision layer.

## Day-1 executable signal search
Returns below are measured from the Day-1 close forward, so the signal is known before entry.

### Strongest broad Day-1 condition
Hold crash-day low + close above crash-day midpoint + Day-1 gap no worse than -5%:
- N=22
- Day-1 close to Day-10 win rate: 63.6%
- Median return: +8.07%
- Mean return: +5.74%
- 25th percentile: -5.12%
- Worst observed: -19.85%
- Best observed: +45.52%

Nearby natural refinements did NOT materially improve the setup:
- add Day-1 return >0: N=20, 65.0% win, median +8.07%
- add Day-1 return >2%: N=19, 63.2% win, median +7.98%
- add Day-1 close position >=0.5: N=18, 61.1% win, median +8.07%
- add Day-1 high > crash close +5%: N=18, 61.1% win, median +7.18%
- add Day-1 volume <=0.5x crash volume: N=11, 72.7% win, median +8.16%, but smaller sample and worse lower-tail concentration

This suggests the broad Day-1 condition is more credible than tighter refinements.

## Risk-control check
A stop at the original crash-day low was too loose because the low can be far below the Day-1 entry.
Fixed stops:
- 5% stop: N=22, 40.9% win, median -5.00%, worst about -6.18%
- 7% stop: 45.5% win, median -2.47%, worst -7.00%
- 10% stop: 50.0% win, median +2.36%, worst about -10.96%

Simple fixed stops materially reduce expectancy and do not improve the setup enough.

## Interpretation
The project is not validated, but the Day-1 technical setup is materially more promising than the news-classification approach because:
1. it uses only observable technical data;
2. it is executable after the signal exists;
3. it preserves a positive median post-entry return;
4. nearby natural refinements do not improve it much, reducing concern that one exact threshold is carrying the result.

The major unresolved issue is risk dispersion: 36.4% of trades are non-winners and the worst observed Day-10 return is -19.85%.

## Next required test
Freeze the broad Day-1 candidate and validate it on a completely untouched historical period before any further tuning:
- crash >=30%
- crash-day relative volume >=5x
- RSP prior-5 > -1%
- Day 1 low holds crash-day low
- Day 1 close reclaims crash-day midpoint
- Day 1 opening gap > -5%
- Entry: Day-1 close
- Primary exit horizon: Day 10
No rule changes after seeing validation outcomes.
