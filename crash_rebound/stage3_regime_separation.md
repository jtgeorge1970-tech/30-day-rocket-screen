# Crash Rebound — Step 3 Regime Separation

## Scope
Frozen development sample: March, April, August, September 2026. 400 crash events total. No pre-rebound classification labels were changed after outcome review.

## Event-level market regime counts
- Broad risk-off: 11
- Mild risk-off: 229
- Mild risk-on: 109
- Broad risk-on: 51

Regime is defined from the average prior-5-session return of SPY, IWM, and RSP:
- <= -3%: BROAD_RISK_OFF
- < 0%: MILD_RISK_OFF
- >= 3%: BROAD_RISK_ON
- otherwise: MILD_RISK_ON

## Main regime-separation finding
The simple market-regime flag alone is not sufficient as a standalone trade switch. Probable Overreaction cases do not uniformly improve in risk-on conditions, and Broad Risk-On has only 4 Probable Overreaction observations.

### Probable Overreaction by event-level regime
| Regime | N | D1 median | D1 positive | D5 median | D5 positive | D10 median | D10 positive | Median max downside D10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Broad risk-off | 2 | -1.19% | 50.0% | -3.54% | 0.0% | -10.27% | 0.0% | -11.73% |
| Mild risk-off | 47 | +1.11% | 59.57% | -0.43% | 48.78% | -1.45% | 45.95% | -9.61% |
| Mild risk-on | 17 | -0.17% | 47.06% | -3.50% | 29.41% | -2.61% | 50.0% | -10.11% |
| Broad risk-on | 4 | -4.91% | 25.0% | -12.37% | 25.0% | -14.73% | 25.0% | -20.32% |

## Stronger pre-entry separators inside Probable Overreaction
Fixed buckets were tested from the already-identified candidate ingredients; thresholds were not optimized after seeing outcomes.

| Condition | N | D1 median | D3 median | D5 median | D10 median | D10 excess vs SPY | Median max downside D10 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Relative volume >= 5x | 37 | +2.31% | +1.64% | -1.88% | +0.94% | +1.70% | -8.88% |
| Relative volume < 5x | 27 | +0.52% | -2.79% | -3.77% | -4.18% | -5.93% | -11.10% |
| Crash <= -30% | 17 | +0.15% | +1.65% | +3.99% | +4.90% | +4.56% | -9.35% |
| Crash > -30% | 20 | +0.82% | -1.32% | -3.31% | -6.88% | -7.31% | -10.92% |
| Risk-off prior 5d | 49 | +1.11% | -0.25% | -0.52% | -4.17% | -5.77% | -9.86% |
| Risk-on prior 5d | 21 | -0.66% | -1.39% | -3.73% | -9.60% | -12.57% | -13.25% |

## Candidate intersection
Probable Overreaction + crash <= -30% + relative volume >= 5x:
- N = 12
- Day 1 positive rate = 66.67%; median = +4.07%; median excess vs SPY = +3.58%
- Day 3 positive rate = 83.33%; median = +5.54%; median excess vs SPY = +3.57%
- Day 5 positive rate = 75.00%; median = +12.47%; median excess vs SPY = +9.90%
- Day 10 positive rate = 75.00%; median = +12.78%; median excess vs SPY = +8.12%
- Median maximum additional downside through Day 10 = -5.75%

### Same candidate by development month
| Month | N | D1 median | D3 median | D5 median | D10 median |
|---|---:|---:|---:|---:|---:|
| March | 5 | +2.58% | +1.65% | -8.89% | -12.28% |
| April | 2 | +5.34% | +9.86% | +19.90% | +20.81% |
| August | 5 | +7.17% | +23.87% | +19.14% | +18.47% |
| September | 0 | — | — | — | — |

This is the key warning: the pooled result is strong, but March reverses sharply after Day 3. Therefore the candidate is not a universal standalone rule.

## Event-level risk split inside the candidate
- Candidate + risk-off: N=7; Day 10 median +12.74%, positive rate 71.43%, excess vs SPY +4.61%, median max downside -9.35%.
- Candidate + risk-on: N=5; Day 10 median +18.47%, positive rate 80.0%, excess vs SPY +19.32%, median max downside -0.41%.

The risk-on subset is extremely small and must not be treated as validated.

## Next-session confirmation
For the 12-event candidate above, 8 had a positive Day-1 close (66.67%). If entry is delayed until after a positive Day-1 confirmation:
- Day 1 close to Day 3: N=8, 62.5% positive, median +2.34%
- Day 1 close to Day 5: N=8, 62.5% positive, median +7.94%
- Day 1 close to Day 10: N=8, 62.5% positive, median +7.18%

This suggests next-session confirmation may retain meaningful upside while avoiding some immediate failures, but N=8 is too small for a trigger decision.

## Step 3 interpretation
1. The three-way headline classification alone is not sufficient.
2. Event-level regime alone is not sufficient.
3. Crash magnitude and relative volume show stronger separation within Probable Overreaction cases.
4. The intersection of Probable Overreaction + >=30% crash + >=5x relative volume is the strongest current development candidate, but its month-to-month behavior is unstable.
5. March demonstrates that regime/context can overwhelm the candidate after the first few sessions.
6. No trigger should be frozen until the regime/context interaction is stress-tested without changing the frozen classifications.
7. September long-horizon cells remain right-censored and must continue to mature.

## Forensic split of the 12-event candidate
Candidate definition remained unchanged: Probable Overreaction + crash <= -30% + relative volume >= 5x.

### Continuous correlations with Day-10 return inside the 12-event candidate
Because N=12 is very small, these are exploratory only:
- RSP prior-5-session return: Pearson +0.554; Spearman +0.504
- QQQ prior-5-session return: Pearson +0.426; Spearman +0.483
- SPY prior-5-session return: Pearson +0.394; Spearman +0.392
- Day-1 stock return: Pearson +0.322; Spearman +0.343
- Relative volume: Pearson +0.319; Spearman +0.210
- Crash size showed essentially no monotonic relationship inside this already-filtered subset (Spearman -0.021)

### Simple zero-line breadth test
No threshold was optimized. The test used the natural 0% line for the prior-5-session benchmark return.

- Candidate with RSP prior-5 > 0: N=5, 5/5 positive at Day 10, median Day-10 return +18.47%, median max additional downside through Day 10 -0.41%.
- Candidate with RSP prior-5 <= 0: N=7, 4/7 positive at Day 10, median Day-10 return +4.90%, median max additional downside -9.35%.
- Candidate with SPY prior-5 > 0: N=5, 5/5 positive, median Day-10 +18.47%.
- Candidate with QQQ prior-5 > 0: N=5, 5/5 positive, median Day-10 +18.47%.
- Candidate with both SPY and RSP prior-5 > 0: N=4, 4/4 positive, median Day-10 +19.57%, median max additional downside +0.92%.

Important: 5/5 versus 4/7 is not statistically decisive at this sample size (two-sided Fisher exact p ≈ 0.205). Treat this as a candidate interaction, not a validated filter.

### Critical falsification check
Positive prior-5 market breadth is NOT generally helpful across all Probable Overreaction cases:
- All PO with RSP prior-5 > 0: Day-10 N=16, positive rate 43.8%, median -7.55%.
- All PO with RSP prior-5 <= 0: Day-10 N=39, positive rate 43.6%, median -4.17%.

Therefore the possible breadth effect is conditional on the extreme-crash/high-volume candidate, not a general bullish-regime effect.

### Current interpretation
The most plausible development hypothesis is an interaction:
1. Probable Overreaction classification
2. Crash magnitude at least 30%
3. Relative volume at least 5x
4. Supportive broad-market/equal-weight context may improve persistence and reduce adverse excursion

The fourth item is not yet validated. It should be treated as a candidate regime modifier to stress-test, not a rule to retroactively impose.

## Threshold robustness stress test
Purpose: determine whether the candidate edge is a broad zone or a fragile artifact of the exact 30% crash / 5x relative-volume thresholds. Pre-rebound classifications remained frozen.

### Crash and relative-volume neighborhood
Without applying the breadth modifier:
- Crash >=25%, RV >=5x: N=13, Day-10 win rate 69.23%, median +12.74%, median excess vs SPY +5.58%, median max downside -3.14%.
- Crash >=30%, RV >=3x: N=14, Day-10 win rate 64.29%, median +8.82%, median excess vs SPY +5.10%, median max downside -8.86%.
- Crash >=30%, RV >=5x: N=12, Day-10 win rate 75.00%, median +12.78%, median excess vs SPY +8.12%, median max downside -5.75%.
- Crash >=30%, RV >=7x: N=8, Day-10 win rate 75.00%, median +10.44%, median excess vs SPY +8.12%, median max downside -3.02%.
- Crash >=35%, RV >=5x: N=8, Day-10 win rate 75.00%, median +8.82%, median excess vs SPY +8.12%, median max downside -6.25%.
- Crash >=40%, RV >=5x: N=5, 100% positive, median +15.97%, but N=5 is too small and should not be treated as a superior cutoff.

Interpretation: performance remains positive across nearby crash and volume thresholds. The evidence favors a broad extreme-crash/high-volume zone rather than one exact optimized boundary.

### Breadth neighborhood
The exact RSP > 0% split was month-confounded because all five qualifying cases were August. Therefore the more useful robustness check is the pre-specified nearby threshold RSP prior-5 > -1%.

For Probable Overreaction + crash >=30% + RV >=5x + RSP prior-5 > -1%:
- N=8 across March, April, and August
- Day 3: 87.5% positive, median +11.67%
- Day 5: 87.5% positive, median +18.41%
- Day 10: 87.5% positive, median +15.61%
- Median max additional downside through Day 10: -1.99%

The eight cases were MAZE, ERAS, ORIC, NCMI, VATE, CDNL, UWMC, and SLE. MAZE was the single Day-10 loser.

### Nearby thresholds with RSP prior-5 > -1%
The edge remains positive across the nearby grid:
- Crash >=25%, RV >=3x: N=13, Day-10 61.54% positive, median +4.34%
- Crash >=25%, RV >=5x: N=9, Day-10 77.78% positive, median +12.74%
- Crash >=30%, RV >=3x: N=10, Day-10 70.00% positive, median +8.82%
- Crash >=30%, RV >=5x: N=8, Day-10 87.50% positive, median +15.61%
- Crash >=30%, RV >=7x: N=6, Day-10 83.33% positive, median +11.68%
- Crash >=35%, RV >=5x: N=6, Day-10 83.33% positive, median +8.82%

This is evidence of local robustness, not proof. Tighter thresholds above 40% and/or 10x quickly reduce N and should not be selected merely because the observed win rate rises.

### Leave-one-month-out check for the RSP > -1% candidate
Base: Probable Overreaction + crash >=30% + RV >=5x + RSP prior-5 > -1%.

- Excluding March: N=7, 100% Day-10 positive, median +18.47%
- Excluding April: N=6, 83.33% positive, median +15.61%
- Excluding August: N=3, 66.67% positive, median +4.90%

The edge survives removal of any one month directionally, but excluding August leaves only three observations. August still contributes heavily to the apparent strength.

### Day-1 confirmation within the RSP > -1% candidate
- Base N=8.
- Five had a positive Day-1 close.
- For those five, entering after Day 1:
  - Day 1 to Day 3: 80% positive, median +2.61%
  - Day 1 to Day 5: 80% positive, median +16.71%
  - Day 1 to Day 10: 80% positive, median +12.61%

This suggests positive Day-1 confirmation can preserve a substantial portion of the move, but it also excludes CDNL and ERAS, both of which ultimately became winners after negative Day 1. Confirmation therefore trades false-positive reduction for missed rebounds.

## Stress-test interpretation
The current development evidence supports a robust candidate zone rather than a single overfit threshold:
- Probable Overreaction
- crash magnitude roughly 30% or greater
- relative volume roughly 5x or greater
- supportive-to-neutral equal-weight breadth, with RSP prior-5 above roughly -1% emerging as the strongest non-month-confounded modifier tested

Do not tighten to 40% crash, 10x volume, or RSP > 0 merely because those smaller samples look cleaner. Those would be classic sample-size overfit.

