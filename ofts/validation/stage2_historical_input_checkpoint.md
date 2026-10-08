# Stage 2 historical input reconstruction checkpoint

## Retrieved and persisted
- Five controls: AAL, KBR, ROCK, WW, AEHR.
- Alpaca IEX daily OHLCV, October 1, 2025 through September 30, 2026.
- 251 bars per symbol; 1,255 rows total.
- Data: `ofts/research/historical_control_bars_2025-10_to_2026-09.csv`.

## Verification limitations
- Original historical workbook has ~206-bar control snapshots; their precise observation end date and price adjustment method are not established.
- This 251-bar sample is NOT asserted to reproduce the original 206-bar test window.
- IEX feed is not guaranteed identical to the historical feed used for the SSOT.
- No score parity has been claimed.
- To complete reconstruction, identify original as-of dates and adjustment convention, retrieve aligned ~206 bars, then compare prices and pivots.

## Decision
Data retrieval and persistence succeeded for the five-control initial cohort. Exact historical reconstruction remains incomplete pending original-date/feed identification.
