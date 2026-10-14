# OFTS saved-evidence report card

Audit UTC: 2026-10-14T02:15:04.286066+00:00
Market as-of: 2026-10-13; qualified cohorts: 3; cohort rows: 388; attempts retained: 56.
Outcome counts: {'PENDING': 1825, 'INELIGIBLE_DATA': 115}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 138, 'selected': 138}.
Cycle ledger: {'complete_signal_cohorts': 3, 'pending_entries': 3, 'open_positions': 3, 'closed_trades': 0, 'benchmark_pairs': 0, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 0 | 365 | 23 | 0 | 2026-10-16 |
| 10 | 0 | 365 | 23 | 0 | 2026-10-23 |
| 20 | 0 | 365 | 23 | 0 | 2026-11-06 |
| 30 | 0 | 365 | 23 | 0 | 2026-11-20 |
| 60 | 0 | 365 | 23 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-10-14T02:08:32.416008+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 11.592486710257095, 'observed_max': 73.1936069532354, 'scored_rows': 110, 'distribution': {'BELOW_40': 16, '40_TO_49_999': 39, '50_TO_59_999': 42, '60_TO_69_999': 12, '70_TO_79_999': 1, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| SCYX | 73.194 | CANDIDATE |
| FIX | 62.883 | CANDIDATE |
| WULF | 62.282 | CANDIDATE |
| RERE | 62.272 | CANDIDATE |
| AKAM | 62.071 | CANDIDATE |
| CSIQ | 61.708 | CANDIDATE |
| NYAX | 61.678 | CANDIDATE |
| FUBO | 61.618 | CANDIDATE |
| SPGI | 61.230 | CANDIDATE |
| DDD | 60.541 | CANDIDATE |
| EPOW | 60.497 | CANDIDATE |
| CHTR | 60.453 | CANDIDATE |
| MESO | 60.090 | CANDIDATE |
| LE | 59.955 | CANDIDATE |
| JACK | 59.529 | CANDIDATE |
| MH | 59.366 | CANDIDATE |
| ATGL | 59.233 | CANDIDATE |
| IDR | 59.213 | CANDIDATE |
| Q | 58.835 | CANDIDATE |
| EPM | 58.639 | CANDIDATE |
| CSPI | 58.206 | CANDIDATE |
| SFM | 58.162 | CANDIDATE |
| XPRO | 57.648 | CANDIDATE |
| AXIL | 57.625 | CANDIDATE |
| LFCR | 57.537 | CANDIDATE |

## Source failures

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
