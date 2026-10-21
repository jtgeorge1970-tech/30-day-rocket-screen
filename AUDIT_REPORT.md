# OFTS saved-evidence report card

Audit UTC: 2026-10-21T06:33:41.828408+00:00
Market as-of: 2026-10-20; qualified cohorts: 8; cohort rows: 1020; attempts retained: 82.
Outcome counts: {'MATURE': 364, 'PENDING': 4370, 'INELIGIBLE_DATA': 365, 'CORPORATE_ACTION_REVIEW': 1}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 125, 'selected': 129}.
Cycle ledger: {'complete_signal_cohorts': 8, 'pending_entries': 4, 'open_positions': 11, 'closed_trades': 0, 'benchmark_pairs': 0, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 364 | 582 | 73 | 1 | 2026-10-16 |
| 10 | 0 | 947 | 73 | 0 | 2026-10-23 |
| 20 | 0 | 947 | 73 | 0 | 2026-11-06 |
| 30 | 0 | 947 | 73 | 0 | 2026-11-20 |
| 60 | 0 | 947 | 73 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-10-21T06:33:39.977822+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 11.788948608821608, 'observed_max': 63.975759674336935, 'scored_rows': 94, 'distribution': {'BELOW_40': 16, '40_TO_49_999': 33, '50_TO_59_999': 39, '60_TO_69_999': 6, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| SCYX | 63.976 | CANDIDATE |
| Q | 62.338 | CANDIDATE |
| RERE | 62.136 | CANDIDATE |
| CHTR | 60.545 | CANDIDATE |
| NYAX | 60.476 | CANDIDATE |
| XPRO | 60.028 | CANDIDATE |
| ATGL | 59.956 | CANDIDATE |
| AKAM | 59.861 | CANDIDATE |
| SPGI | 59.544 | CANDIDATE |
| FUBO | 59.426 | CANDIDATE |
| CHPT | 59.162 | CANDIDATE |
| CRNC | 58.702 | CANDIDATE |
| DKNG | 58.556 | CANDIDATE |
| CCS | 57.800 | CANDIDATE |
| LFCR | 57.680 | CANDIDATE |
| ACDC | 57.516 | CANDIDATE |
| VIRC | 57.365 | CANDIDATE |
| TT | 57.236 | CANDIDATE |
| FERG | 57.042 | CANDIDATE |
| MESO | 57.000 | CANDIDATE |
| MH | 56.993 | CANDIDATE |
| EPM | 56.923 | CANDIDATE |
| SGRY | 56.516 | CANDIDATE |
| FFBC | 56.261 | CANDIDATE |
| SFM | 54.859 | CANDIDATE |

## Source failures
- NVNI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SB.PRC: ValueError: EMPTY_PROVIDER_RESPONSE
- SLP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
