# OFTS saved-evidence report card

Audit UTC: 2026-10-30T10:31:32.083537+00:00
Market as-of: 2026-10-29; qualified cohorts: 15; cohort rows: 1938; attempts retained: 117.
Outcome counts: {'MATURE': 1767, 'PENDING': 6990, 'INELIGIBLE_DATA': 925, 'CORPORATE_ACTION_REVIEW': 8}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 126, 'selected': 136}.
Cycle ledger: {'complete_signal_cohorts': 15, 'pending_entries': 1, 'open_positions': 33, 'closed_trades': 2, 'benchmark_pairs': 2, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 1174 | 575 | 185 | 4 | 2026-10-16 |
| 10 | 593 | 1156 | 185 | 4 | 2026-10-23 |
| 20 | 0 | 1753 | 185 | 0 | 2026-11-06 |
| 30 | 0 | 1753 | 185 | 0 | 2026-11-20 |
| 60 | 0 | 1753 | 185 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-10-29T23:10:12.896708+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 11.744188253821582, 'observed_max': 67.49615153894838, 'scored_rows': 89, 'distribution': {'BELOW_40': 14, '40_TO_49_999': 35, '50_TO_59_999': 32, '60_TO_69_999': 8, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| SCYX | 67.496 | CANDIDATE |
| ASO | 64.407 | CANDIDATE |
| MESO | 62.900 | CANDIDATE |
| AKAM | 62.427 | CANDIDATE |
| CRNC | 62.004 | CANDIDATE |
| SPGI | 61.931 | CANDIDATE |
| TT | 60.786 | CANDIDATE |
| TARS | 60.106 | CANDIDATE |
| LFCR | 59.773 | CANDIDATE |
| NYAX | 59.678 | CANDIDATE |
| FUBO | 59.475 | CANDIDATE |
| EEFT | 59.357 | CANDIDATE |
| PLBL | 59.049 | CANDIDATE |
| XPRO | 59.008 | CANDIDATE |
| ATGL | 58.886 | CANDIDATE |
| GLW | 58.550 | CANDIDATE |
| BRCB | 58.448 | CANDIDATE |
| RYAN | 57.742 | CANDIDATE |
| EPM | 57.533 | CANDIDATE |
| LOMA | 57.183 | CANDIDATE |
| FERG | 56.970 | CANDIDATE |
| WOR | 56.862 | CANDIDATE |
| METCB | 56.860 | CANDIDATE |
| VIRC | 56.857 | CANDIDATE |
| NBIS | 56.279 | CANDIDATE |

## Source failures
- ACA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- QRVO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- PERF: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- GAM.PRB: ValueError: EMPTY_PROVIDER_RESPONSE
- SPG.PRJ: ValueError: EMPTY_PROVIDER_RESPONSE
- GS.PRA: ValueError: EMPTY_PROVIDER_RESPONSE
- NVNI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SB.PRC: ValueError: EMPTY_PROVIDER_RESPONSE
- SLP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
