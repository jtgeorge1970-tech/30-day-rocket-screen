# Crash Rebound — Targeted Expansion Check

## Purpose
Test the frozen candidate outside the original March/April/August/September development months without changing thresholds after seeing outcomes.

Frozen mechanical screen:
- Crash >= 30%
- Relative volume >= 5x prior-20-session median
- RSP prior-5-session return > -1%

Untouched 2026 source months screened:
- January
- February
- May
- June
- July

## Screen result
- 500 source events reviewed mechanically
- 142 had crash >=30%
- 111 passed the full numeric screen
- Pre-outcome classification frozen before opening outcomes:
  - Probable Overreaction: 17
  - Justified: 19
  - Uncertain: 75

## Fresh outcome result
### Probable Overreaction (N=17)
- Day 1: 35.3% positive; median -1.52%
- Day 3: 29.4% positive; median -2.36%
- Day 5: 35.3% positive; median -1.48%
- Day 10: 35.3% positive; median -2.53%
- Day 10 median excess vs SPY: -0.75%
- Median maximum additional downside through Day 10: -17.45%

This materially fails to replicate the original development candidate.

### Same numeric setup, Justified (N=19)
- Day 10: 68.4% positive
- Median Day 10: +8.04%
- Median Day 10 excess vs SPY: +8.97%
- Median maximum additional downside through Day 10: -5.78%

This is the opposite of the earlier simple long/short interpretation and further weakens the original classification-based thesis.

## Catalyst breakdown inside fresh Probable Overreaction cases
- Clinical Trial Results: N=12, 50.0% positive at Day 10, median +1.83%
- Earnings: N=5, 0% positive at Day 10, median -3.26%

Interpretation:
- The headline-based Probable Overreaction label is not reliable enough by itself.
- Explicitly positive/record/strong earnings headlines that still crash >=30% and trade on >=5x relative volume performed especially poorly in this fresh sample.
- Clinical cases were mixed rather than strongly positive.
- The original 8-case pocket was likely overfit or regime/sample-specific.
- The project should not advance the old candidate to a frozen trading trigger.

## Integrity
Classification was committed before outcome calculation:
- Numeric screen commit: fbd0041ed23e67ade3095028361344a2b19967a2
- Frozen pre-outcome classification commit: 72ec426efcee599169359de06728136762869754
- Outcome commit: ecc5911eba02c23904a9a98b0e79263d83575b1c
