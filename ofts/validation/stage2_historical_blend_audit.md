# OFTS v2.2 historical validation — 2026-10-07

Source: OFTS_Quality_v2_SSOT_Log.xlsx, Scores tab (first 97 historical SCORED records).

Test: predicted = 0.75 * Structural Quality + 0.25 * Recent Quality.

- 97 records examined.
- 86 records within 0.101 score points of reported v2.2 score.
- 11 records outside tolerance.
- Largest absolute deviation: AEHR 2.025 points.
- Other exceptions: WW 1.175; ROCK 0.700; CHPT 0.375; AIOS 0.700; AIP 0.725; BKSY 1.500; AIFU 0.350.

**Conclusion:** 75/25 blending is substantially confirmed for ordinary historical rows but is NOT sufficient to reproduce all locked historical outputs. The control-38 records have unexplained deviations. Do not deploy a purported locked scorer until exceptions and all seven underlying component formulas are recovered and validated. These are historical scores, not newly processed symbols.
