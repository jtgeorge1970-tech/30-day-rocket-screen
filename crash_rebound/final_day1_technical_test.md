# Crash Rebound — Final Day-1 Technical Filter Test

## Fixed base Day-1 setup
Mechanical crash universe only; no news classification used in the decision layer.

Base setup:
- crash >=30%
- initial mechanical screen retained
- Day 1 holds the crash-day low
- Day 1 closes above the crash-day midpoint
- Day 1 opening gap is better than -5%
- entry measured at Day-1 close
- outcome measured from Day-1 close to Day 10

Base result:
- N=22
- win rate 63.6%
- median +8.07%
- mean +5.74%
- lower quartile -5.12%
- worst -19.85%

## Final natural-filter test
The only filter that materially improved the setup without collapsing sample size was crash-day relative volume.

### Relative-volume neighborhood
| Crash RV threshold | N | Win rate | Median Day1→Day10 | Mean | Lower quartile | Worst |
|---|---:|---:|---:|---:|---:|---:|
| >=8x | 17 | 70.6% | +9.61% | +8.39% | 0.00% | -19.85% |
| >=10x | 14 | 78.6% | +9.81% | +11.29% | +4.72% | -13.47% |
| >=12x | 11 | 72.7% | +8.16% | +10.94% | 0.00% | -13.47% |
| >=15x | 10 | 70.0% | +8.83% | +11.22% | 0.00% | -13.47% |
| >=20x | 9 | 66.7% | +7.98% | +11.39% | 0.00% | -13.47% |

Interpretation: the edge does not exist only at exactly 10x. Nearby high-relative-volume thresholds remain positive. The 10x line is the strongest balance of sample size and observed payoff in this development/expansion sample, but should be treated as a candidate threshold, not an optimized truth.

## Leave-one-month-out robustness for RV>=10x candidate
Candidate:
- Day 1 holds crash low
- Day 1 closes above crash midpoint
- Day 1 gap > -5%
- crash-day relative volume >=10x
- entry at Day-1 close
- exit at Day 10 close

Results:
- Excluding January: N=11, 90.9% winners, median +9.95%
- Excluding February: N=12, 75.0% winners, median +9.81%
- Excluding May: N=13, 76.9% winners, median +9.68%
- Excluding June: N=9, 77.8% winners, median +11.30%
- Excluding July: N=11, 72.7% winners, median +8.16%

The candidate remains directionally positive after excluding any single month.

## Month-level warning
- January: N=3, 33.3% winners, median 0.00%
- February: N=2, 100% winners, median +10.56%
- May: N=1, 100% winner, median +9.95%
- June: N=5, 80% winners, median +8.16%
- July: N=3, 100% winners, median +33.70%

January is a clear weak spot and several month subsamples are tiny. Therefore this is not validated.

## Conclusion
The final Day-1 technical test did not kill the project. It produced the strongest executable candidate found so far using technical data only.

Candidate to carry forward for formal trigger work:
- large crash mechanical universe
- crash-day relative volume in the high-volume zone, provisionally >=10x
- Day 1 does not break the crash low
- Day 1 closes above the crash-day midpoint
- Day 1 gap is not worse than -5%
- entry at Day-1 close
- Day-10 close as the current development exit horizon

This candidate must now be frozen before true out-of-sample validation. Do not add headline interpretation back into the trigger and do not retune thresholds after seeing OOS results.
