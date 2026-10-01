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

