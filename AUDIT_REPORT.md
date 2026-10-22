# OFTS saved-evidence report card

Audit UTC: 2026-10-22T08:57:39.833763+00:00
Market as-of: 2026-10-21; qualified cohorts: 9; cohort rows: 1149; attempts retained: 88.
Outcome counts: {'MATURE': 480, 'PENDING': 4833, 'INELIGIBLE_DATA': 430, 'CORPORATE_ACTION_REVIEW': 2}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 124, 'selected': 129}.
Cycle ledger: {'complete_signal_cohorts': 9, 'pending_entries': 1, 'open_positions': 15, 'closed_trades': 0, 'benchmark_pairs': 0, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 480 | 581 | 86 | 2 | 2026-10-16 |
| 10 | 0 | 1063 | 86 | 0 | 2026-10-23 |
| 20 | 0 | 1063 | 86 | 0 | 2026-11-06 |
| 30 | 0 | 1063 | 86 | 0 | 2026-11-20 |
| 60 | 0 | 1063 | 86 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-10-22T06:34:39.459851+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 10.938289701919537, 'observed_max': 62.6355613204075, 'scored_rows': 95, 'distribution': {'BELOW_40': 17, '40_TO_49_999': 30, '50_TO_59_999': 40, '60_TO_69_999': 8, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| ASO | 62.636 | CANDIDATE |
| RERE | 62.140 | CANDIDATE |
| TGS | 61.845 | CANDIDATE |
| Q | 61.726 | CANDIDATE |
| SCYX | 61.434 | CANDIDATE |
| FUBO | 61.054 | CANDIDATE |
| NYAX | 60.468 | CANDIDATE |
| CHTR | 60.104 | CANDIDATE |
| AKAM | 59.864 | CANDIDATE |
| ATGL | 59.835 | CANDIDATE |
| SPGI | 59.556 | CANDIDATE |
| SMMT | 59.082 | CANDIDATE |
| CHPT | 59.066 | CANDIDATE |
| DKNG | 58.557 | CANDIDATE |
| XPRO | 58.533 | CANDIDATE |
| GLW | 57.855 | CANDIDATE |
| ACDC | 57.800 | CANDIDATE |
| CCS | 57.706 | CANDIDATE |
| LFCR | 57.650 | CANDIDATE |
| VIRC | 57.374 | CANDIDATE |
| EPM | 57.342 | CANDIDATE |
| MESO | 57.019 | CANDIDATE |
| FERG | 57.003 | CANDIDATE |
| TT | 56.965 | CANDIDATE |
| CRNC | 56.829 | CANDIDATE |

## Source failures
- GS.PRA: ValueError: EMPTY_PROVIDER_RESPONSE
- NVNI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SB.PRC: ValueError: EMPTY_PROVIDER_RESPONSE
- SLP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
