# OFTS saved-evidence report card

Audit UTC: 2026-10-24T06:26:06.702016+00:00
Market as-of: 2026-10-23; qualified cohorts: 11; cohort rows: 1410; attempts retained: 96.
Outcome counts: {'MATURE': 834, 'PENDING': 5634, 'INELIGIBLE_DATA': 580, 'CORPORATE_ACTION_REVIEW': 2}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 125, 'selected': 130}.
Cycle ledger: {'complete_signal_cohorts': 11, 'pending_entries': 1, 'open_positions': 22, 'closed_trades': 1, 'benchmark_pairs': 1, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 713 | 579 | 116 | 2 | 2026-10-16 |
| 10 | 121 | 1173 | 116 | 0 | 2026-10-23 |
| 20 | 0 | 1294 | 116 | 0 | 2026-11-06 |
| 30 | 0 | 1294 | 116 | 0 | 2026-11-20 |
| 60 | 0 | 1294 | 116 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-10-23T23:03:05.620618+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 13.729695932252008, 'observed_max': 68.87575634703964, 'scored_rows': 90, 'distribution': {'BELOW_40': 10, '40_TO_49_999': 42, '50_TO_59_999': 30, '60_TO_69_999': 8, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| SCYX | 68.876 | CANDIDATE |
| AKAM | 65.013 | CANDIDATE |
| ASO | 62.946 | CANDIDATE |
| SPGI | 61.938 | CANDIDATE |
| Q | 61.631 | CANDIDATE |
| FUBO | 61.064 | CANDIDATE |
| RERE | 60.792 | CANDIDATE |
| NYAX | 60.621 | CANDIDATE |
| TT | 59.611 | CANDIDATE |
| ATGL | 59.523 | CANDIDATE |
| ACDC | 58.984 | CANDIDATE |
| CHPT | 58.750 | CANDIDATE |
| LFCR | 58.698 | CANDIDATE |
| XPRO | 58.521 | CANDIDATE |
| GLW | 58.510 | CANDIDATE |
| KTB | 57.717 | CANDIDATE |
| EPM | 57.644 | CANDIDATE |
| VIRC | 57.467 | CANDIDATE |
| DJT | 57.178 | CANDIDATE |
| FERG | 57.085 | CANDIDATE |
| MESO | 57.080 | CANDIDATE |
| CHTR | 56.936 | CANDIDATE |
| DKNG | 56.932 | CANDIDATE |
| CCS | 56.799 | CANDIDATE |
| CRNC | 56.601 | CANDIDATE |

## Source failures
- GS.PRA: ValueError: EMPTY_PROVIDER_RESPONSE
- NVNI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SB.PRC: ValueError: EMPTY_PROVIDER_RESPONSE
- SLP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
