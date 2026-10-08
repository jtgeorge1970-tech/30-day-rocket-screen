# Stage 2 Step 2 — Historical inputs reconstructed

**Status: completed for ten controls; expanded controls can follow in regression.**

- Original as-of date identified: **2026-10-02**.
- Evidence: saved SSOT last prices agree with retrieved Alpaca IEX closing prices on that date for all ten controls: AAL 12.94 (IEX raw 12.935), KBR 34.25, ROCK 40.09, WW 14.69, AEHR 107.34, AXTI 85.87, BKSY 21.90, PLTR 188.80, CHPT 9.30, AIP 24.70.
- Window: **206 trading days**, from **2025-12-08 through 2026-10-02** inclusive, extracted from daily OHLCV.
- Coverage: **10/10** controls, **206/206** bars each, **2,060** saved rows.
- Source: Alpaca IEX 1Day unadjusted OHLCV; query 2025-11-01 to 2026-10-02; last 206 bars per symbol.
- Dataset: `ofts/research/historical_controls_206bars_asof_2026-10-02.csv`.
- Note: raw AAL close 12.935 rounds to 12.94 in SSOT. Original feed identity, historical adjustment settings, and original exact pivot logic remain unverified; do not assert exact historical score parity yet.
- Control diversity: baseline AAL/KBR, historical Control-38 ROCK/WW/AEHR/AXTI/BKSY/PLTR/CHPT/AIP.
- Step 3 next: execute candidate scoring on these same 206-bar series, compare pivots, swings, structural/recent scores, and diagnose divergences.

No new production scores have been generated.
