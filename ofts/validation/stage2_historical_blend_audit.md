# OFTS v2.2 historical validation — 2026-10-07

Source: OFTS_Quality_v2_SSOT_Log.xlsx, Scores tab (first 97 historical SCORED records).

Test: predicted = 0.75 * Structural Quality + 0.25 * Recent Quality.

- 97 records examined.
- 86 records within 0.101 score points of reported v2.2 score.
- 11 records outside tolerance.
- Largest absolute deviation: AEHR 2.025 points.
- Other exceptions: WW 1.175; ROCK 0.700; CHPT 0.375; AIOS 0.700; AIP 0.725; BKSY 1.500; AIFU 0.350.

**Conclusion:** 75/25 blending is substantially confirmed for ordinary historical rows but is NOT sufficient to reproduce all locked historical outputs. The control-38 records have unexplained deviations. Do not deploy a purported locked scorer until exceptions and all seven underlying component formulas are recovered and validated. These are historical scores, not newly processed symbols.

## Second-pass reconciliation

The 11 blend exceptions all come from the historical **Control-38** cohort (WW, ROCK, CHPT, AIOS, AEHR, AIP, BKSY, AIFU, AXTI, PLTR, BVC). This isolates the mismatch to a specific cohort rather than random formula errors. Their score fields cannot be accepted as proof of the 75/25 blend without identifying the original version/column lineage.

The authoritative workbook's **Quality v2 Spec** tab specifies seven weighted components (20/10/10/15/15/10/20), 180 trading-day minimum, $3 price gate, common/ADR types only, 90-day recent window, 11% recent median swing gate, and 75/25 structural/recent blending. The component **descriptions** are present, but executable definitions/normalization functions are absent from the extracted specification. Adaptive ATR threshold and 8% median swing are marked CURRENT TEST, not LOCKED.

**Production decision:** exact locked scoring remains unimplemented. Do not substitute a guessed formula or count old scored records as new. Next step: recover actual implementation from source artifacts or independently reproduce and explicitly approve a new version after controlled regression tests.
