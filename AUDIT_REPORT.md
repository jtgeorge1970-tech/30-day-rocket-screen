# OFTS saved-evidence report card

Audit UTC: 2026-10-23T15:28:19.920552+00:00
Market as-of: 2026-10-22; qualified cohorts: 10; cohort rows: 1280; attempts retained: 93.
Outcome counts: {'MATURE': 595, 'PENDING': 5293, 'INELIGIBLE_DATA': 510, 'CORPORATE_ACTION_REVIEW': 2}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 126, 'selected': 131}.
Cycle ledger: {'complete_signal_cohorts': 10, 'pending_entries': 7, 'open_positions': 16, 'closed_trades': 0, 'benchmark_pairs': 0, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 595 | 581 | 102 | 2 | 2026-10-16 |
| 10 | 0 | 1178 | 102 | 0 | 2026-10-23 |
| 20 | 0 | 1178 | 102 | 0 | 2026-11-06 |
| 30 | 0 | 1178 | 102 | 0 | 2026-11-20 |
| 60 | 0 | 1178 | 102 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-10-23T06:29:54.461379+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 12.131604219493404, 'observed_max': 65.02805126774665, 'scored_rows': 99, 'distribution': {'BELOW_40': 11, '40_TO_49_999': 48, '50_TO_59_999': 33, '60_TO_69_999': 7, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| AKAM | 65.028 | CANDIDATE |
| ASO | 62.434 | CANDIDATE |
| SCYX | 62.350 | CANDIDATE |
| RERE | 61.956 | CANDIDATE |
| Q | 61.773 | CANDIDATE |
| NYAX | 60.536 | CANDIDATE |
| FUBO | 60.530 | CANDIDATE |
| ATGL | 59.780 | CANDIDATE |
| SMMT | 59.071 | CANDIDATE |
| SPGI | 58.994 | CANDIDATE |
| ACDC | 58.794 | CANDIDATE |
| CHPT | 58.661 | CANDIDATE |
| GLW | 58.495 | CANDIDATE |
| DKNG | 58.245 | CANDIDATE |
| XPRO | 58.153 | CANDIDATE |
| CHTR | 58.118 | CANDIDATE |
| LFCR | 57.620 | CANDIDATE |
| VIRC | 57.485 | CANDIDATE |
| EPM | 57.359 | CANDIDATE |
| DJT | 57.225 | CANDIDATE |
| FERG | 56.989 | CANDIDATE |
| MESO | 56.979 | CANDIDATE |
| CCS | 56.747 | CANDIDATE |
| CRNC | 56.606 | CANDIDATE |
| TT | 56.273 | CANDIDATE |

## Source failures
- GS.PRA: ValueError: EMPTY_PROVIDER_RESPONSE
- NVNI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SB.PRC: ValueError: EMPTY_PROVIDER_RESPONSE
- SLP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
