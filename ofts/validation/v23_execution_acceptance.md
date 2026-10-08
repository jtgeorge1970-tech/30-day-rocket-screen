# v2.3 research execution and acceptance report

## Executed computations
- Ten historical controls: calculated and committed to [v23_candidate_results.csv](v23_candidate_results.csv). The candidate produces finite structural, recent, and 75/25 blended values for all ten.
- Three separate holdout symbols (206 daily bars each): calculated using an independent JavaScript translation of the Python candidate mathematics; output committed to [v23_holdout_results.csv](v23_holdout_results.csv).
- MU: structural 55.061, recent 62.791, blended 56.993; 21 confirmed swings.
- STX: structural 51.468, recent 60.934, blended 53.834; 18 confirmed swings.
- HOOD: structural 56.525, recent 55.134, blended 56.177; 16 confirmed swings.

## Verification distinctions
PASS: input record count (206 each), bounded finite candidate scores, calculated 75/25 blend, three holdout stocks scored without fitting to historical SSOT scores.

NOT VERIFIED: successful execution of the committed **Python** regression runner in GitHub Actions (no run logs obtained). JavaScript reimplementation is not a Python integration test.

NOT TESTED: predictive validity on untouched *future* returns, historical entry/exit trades, risk-adjusted performance, walk-forward stability, or whether oscillator selection beats random/trend controls. The three holdout stocks were selected manually, not a randomized or comprehensive negative-control set.

NOT RECOVERED: original locked v2.2 component formulas; historical structural parity still fails. v2.3 is explicitly a proposed replacement.

## Acceptance decision
**Research calculation milestone: PASS.**
**Historical v2.2 parity: FAIL.**
**Python integration verification: NOT VERIFIED.**
**Independent predictive validation: NOT DONE.**
**Production deployment: BLOCKED.**

Do not label the holdout arithmetic as proof of trading performance or treat any candidate scores as BUY signals.
