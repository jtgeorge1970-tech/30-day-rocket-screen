# OFTS saved-evidence report card

Audit UTC: 2026-10-12T01:13:24.190397+00:00
Market as-of: 2026-10-09; qualified cohorts: 1; cohort rows: 125; attempts retained: 49.
Outcome counts: {'PENDING': 605, 'INELIGIBLE_DATA': 20}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 124, 'selected': 125}.
Cycle ledger: {'complete_signal_cohorts': 1, 'pending_entries': 1, 'open_positions': 0, 'closed_trades': 0, 'benchmark_pairs': 0, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 0 | 121 | 4 | 0 | 2026-10-16 |
| 10 | 0 | 121 | 4 | 0 | 2026-10-23 |
| 20 | 0 | 121 | 4 | 0 | 2026-11-06 |
| 30 | 0 | 121 | 4 | 0 | 2026-11-20 |
| 60 | 0 | 121 | 4 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-10-10T06:55:07.723271+00:00; model: 2efb29d640e0ca751d9f8d30781f9021b2e38310114999e253e7b21b7283c3c6.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 10.884069079004723, 'observed_max': 62.584482993236065, 'scored_rows': 97, 'distribution': {'BELOW_40': 9, '40_TO_49_999': 37, '50_TO_59_999': 40, '60_TO_69_999': 11, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| AKAM | 62.584 | CANDIDATE |
| WULF | 62.154 | CANDIDATE |
| FUBO | 61.675 | CANDIDATE |
| SPGI | 61.624 | CANDIDATE |
| SFM | 60.946 | CANDIDATE |
| CSIQ | 60.765 | CANDIDATE |
| XPRO | 60.556 | CANDIDATE |
| MESO | 60.506 | CANDIDATE |
| CHTR | 60.500 | CANDIDATE |
| EPOW | 60.482 | CANDIDATE |
| HLIT | 60.440 | CANDIDATE |
| NYAX | 59.939 | CANDIDATE |
| JACK | 59.553 | CANDIDATE |
| TBLA | 59.542 | CANDIDATE |
| ATGL | 59.058 | CANDIDATE |
| FMC | 58.873 | CANDIDATE |
| NX | 58.802 | CANDIDATE |
| LE | 58.526 | CANDIDATE |
| SRAD | 58.359 | CANDIDATE |
| OWLT | 58.302 | CANDIDATE |
| IDR | 58.294 | CANDIDATE |
| BE | 58.108 | CANDIDATE |
| HNRG | 57.976 | CANDIDATE |
| MBLY | 57.385 | CANDIDATE |
| CGNX | 56.788 | CANDIDATE |

## Source failures
- AKO.A: ValueError: EMPTY_PROVIDER_RESPONSE

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
