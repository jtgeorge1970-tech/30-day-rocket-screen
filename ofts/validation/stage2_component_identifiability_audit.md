# Stage 2 reconstruction — component identifiability audit

## Verified control comparisons
Ten 206-bar control datasets are available as-of 2026-10-02. Candidate and historical comparisons:
- AAL: candidate median swing 20.26%, historical 20.3%; historical swing count not independently confirmed in this audit.
- KBR: candidate 16 swings vs historical 16; candidate median 10.33%, historical 11.0%.
- ROCK: candidate 19 swings vs historical 19; candidate median 11.05%, historical 11.1%.
- WW: candidate 13 swings vs historical 15.
- AEHR: candidate 21 swings vs historical 20.
- AXTI: candidate 28 swings vs historical 28.
- BKSY: candidate 23 swings vs historical 15.
- PLTR: candidate 24 swings vs historical 15.
- CHPT: candidate 11 swings vs historical 15.
- AIP: candidate 21 swings vs historical 13.

## Mathematical identifiability
The historical SSOT supplies **seven component weights** and aggregate structural scores, but not the seven per-stock component scores or their executable calculation rules. One aggregate per stock cannot uniquely determine seven unknown components, much less seven unknown functions. Even with ten controls, infinitely many component functions reproduce those ten aggregate targets. Calibrating directly to those ten targets would be overfitting and would not establish recovery of locked v2.2.

## Acceptance
- Price-window reconstruction: PASS for ten controls.
- Swing-count parity: 3 exact matches out of nine controls with confirmed counts (KBR, ROCK, AXTI).
- Median-swing parity: not established globally.
- Structural score parity: FAIL, all ten overestimated.
- Seven-component formula equivalence: UNVERIFIABLE from available artifacts.
- Recent-window score implementation and validation: NOT DONE.
- Locked v2.2 production promotion: BLOCKED.

## Correct next decision
Retrieve the original executable scoring implementation or explicit seven-component formulas. If unavailable, develop and separately label a replacement v2.3 specification with out-of-sample testing and owner approval. Do not call fitted replacements 'recovered v2.2'.
