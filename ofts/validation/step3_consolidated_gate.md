# OFTS Step 3 — consolidated research gate

## Reconstructed replacement scoring
v2.3 research implementation: seven explicitly specified components, 90-day recent window, 75/25 structural/recent blend. Historical v2.2 formulas are not represented as recovered.

## Execution
10 historical controls scored and persisted in `ofts/validation/v23_candidate_results.csv`.
3 independent holdout symbols (MU, STX, HOOD) scored and persisted in `ofts/validation/v23_holdout_results.csv`.
The 13-stock computation has been performed in an independent JavaScript implementation. The Python runner is committed but its successful execution has not been independently verified from GitHub Actions logs.

## Results
- MU: 56.993, 21 swings.
- STX: 53.834, 18 swings.
- HOOD: 56.177, 16 swings.
- 10 historical controls scored; no original-v2.2 parity claim.

## Decision
Step 3 **RESEARCH SCORING REBUILD COMPLETE**: code and 13 calculated examples saved.
Step 3 **PRODUCTION VALIDATION NOT COMPLETE**: no walk-forward trade-outcome backtest, no negative-control cohort, and no verified Python integration execution.
DO NOT claim predictive accuracy, deploy production scoring, or label this locked v2.2. Promotion requires validation evidence and owner approval.
