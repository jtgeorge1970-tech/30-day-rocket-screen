# OFTS saved-evidence report card

Audit UTC: 2026-10-20T08:52:48.132045+00:00
Market as-of: 2026-10-19; qualified cohorts: 7; cohort rows: 891; attempts retained: 79.
Outcome counts: {'MATURE': 233, 'PENDING': 3906, 'INELIGIBLE_DATA': 315, 'CORPORATE_ACTION_REVIEW': 1}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 123, 'selected': 126}.
Cycle ledger: {'complete_signal_cohorts': 7, 'pending_entries': 1, 'open_positions': 10, 'closed_trades': 0, 'benchmark_pairs': 0, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 233 | 594 | 63 | 1 | 2026-10-16 |
| 10 | 0 | 828 | 63 | 0 | 2026-10-23 |
| 20 | 0 | 828 | 63 | 0 | 2026-11-06 |
| 30 | 0 | 828 | 63 | 0 | 2026-11-20 |
| 60 | 0 | 828 | 63 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-10-20T06:34:25.783944+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 10.85272562264587, 'observed_max': 63.9462796150476, 'scored_rows': 81, 'distribution': {'BELOW_40': 8, '40_TO_49_999': 30, '50_TO_59_999': 34, '60_TO_69_999': 9, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| SCYX | 63.946 | CANDIDATE |
| SB | 63.892 | CANDIDATE |
| RERE | 63.344 | CANDIDATE |
| AKAM | 62.306 | CANDIDATE |
| Q | 62.149 | CANDIDATE |
| MESO | 60.880 | CANDIDATE |
| CHTR | 60.584 | CANDIDATE |
| MH | 60.191 | CANDIDATE |
| XPRO | 60.035 | CANDIDATE |
| FUBO | 59.853 | CANDIDATE |
| NYAX | 59.715 | CANDIDATE |
| SPGI | 59.563 | CANDIDATE |
| ATGL | 58.437 | CANDIDATE |
| CHPT | 58.136 | CANDIDATE |
| SFM | 58.038 | CANDIDATE |
| CCS | 57.700 | CANDIDATE |
| LFCR | 57.677 | CANDIDATE |
| ACDC | 57.617 | CANDIDATE |
| VIRC | 57.231 | CANDIDATE |
| EPM | 56.875 | CANDIDATE |
| CRNC | 56.838 | CANDIDATE |
| DKNG | 56.630 | CANDIDATE |
| SGRY | 56.491 | CANDIDATE |
| WULF | 56.393 | CANDIDATE |
| FFBC | 56.306 | CANDIDATE |

## Source failures
- SB.PRC: ValueError: EMPTY_PROVIDER_RESPONSE
- SLP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
