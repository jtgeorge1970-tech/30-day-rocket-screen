# OFTS saved-evidence report card

Audit UTC: 2026-10-17T06:06:50.864541+00:00
Market as-of: 2026-10-16; qualified cohorts: 6; cohort rows: 765; attempts retained: 74.
Outcome counts: {'MATURE': 121, 'PENDING': 3454, 'INELIGIBLE_DATA': 250}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 124, 'selected': 126}.
Cycle ledger: {'complete_signal_cohorts': 6, 'pending_entries': 0, 'open_positions': 10, 'closed_trades': 0, 'benchmark_pairs': 0, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 121 | 594 | 50 | 0 | 2026-10-16 |
| 10 | 0 | 715 | 50 | 0 | 2026-10-23 |
| 20 | 0 | 715 | 50 | 0 | 2026-11-06 |
| 30 | 0 | 715 | 50 | 0 | 2026-11-20 |
| 60 | 0 | 715 | 50 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-10-16T20:39:52.370840+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 11.97800709772383, 'observed_max': 64.03291587648434, 'scored_rows': 100, 'distribution': {'BELOW_40': 12, '40_TO_49_999': 40, '50_TO_59_999': 39, '60_TO_69_999': 9, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| SCYX | 64.033 | CANDIDATE |
| RERE | 63.366 | CANDIDATE |
| AKAM | 62.298 | CANDIDATE |
| XPRO | 61.780 | CANDIDATE |
| SPGI | 61.135 | CANDIDATE |
| MESO | 60.952 | CANDIDATE |
| NYAX | 60.871 | CANDIDATE |
| MH | 60.550 | CANDIDATE |
| CHTR | 60.539 | CANDIDATE |
| FUBO | 59.883 | CANDIDATE |
| CCS | 59.411 | CANDIDATE |
| Q | 58.692 | CANDIDATE |
| INTJ | 58.580 | CANDIDATE |
| ATGL | 58.523 | CANDIDATE |
| CHPT | 58.277 | CANDIDATE |
| WULF | 58.157 | CANDIDATE |
| CRNC | 58.122 | CANDIDATE |
| SFM | 58.115 | CANDIDATE |
| LFCR | 57.583 | CANDIDATE |
| ACDC | 57.492 | CANDIDATE |
| SGRY | 57.117 | CANDIDATE |
| NUAI | 56.991 | CANDIDATE |
| EPM | 56.727 | CANDIDATE |
| DKNG | 56.603 | CANDIDATE |
| CIGI | 56.463 | CANDIDATE |

## Source failures
- SLP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
