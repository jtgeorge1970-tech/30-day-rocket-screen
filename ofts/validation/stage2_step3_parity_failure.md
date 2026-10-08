# Stage 2 Step 3 — Historical head-to-head scoring

**Result: FAIL — candidate is not SSOT-parity compliant.**

Ran ten 206-bar historical controls as-of 2026-10-02 through the candidate pivot and structural scoring calculations. Machine-readable outputs are in `ofts/validation/stage2_step3_candidate_comparison.csv`.

## Confirmed issues
- Candidate structural scores exceed SSOT scores on all ten controls by **20.94 to 38.13 points**.
- Candidate swing counts differ from SSOT: AAL candidate 14 vs SSOT historical swing count needs confirmation; KBR 16 vs 16; ROCK 19 vs 19; WW 13 vs 15; AEHR 21 vs 20; AXTI 28 vs 28; BKSY 23 vs 15; PLTR 24 vs 15; CHPT 11 vs 15; AIP 21 vs 13.
- Several median swing percentages are different despite matching final prices; investigate reversal threshold, pivot confirmation, OHLC vs close basis, and feed conventions.
- Candidate `capture` score is susceptible to saturating at 100 and candidate alternation purity can be mechanically 100 because ZigZag enforces alternation. These two components have combined 35% weight, a likely contributor to inflated structural scores.
- Exact locked v2.2 seven-component mathematical formulas have not been recovered. No unjustified calibration is permitted.
- The 75/25 final blend cannot be validated from the current candidate: recent-window component scoring has not been separately implemented.

## Gate decision
Step 3 head-to-head comparison has been executed, but **Step 3 cannot be marked PASS/complete**. Next is targeted implementation repair and recovery of original component math; rerun comparisons and only advance when reproducibility criteria pass. Production score count remains zero.

This audit does not establish that the experimental candidate reproduces locked v2.2.
