# OFTS saved-evidence report card

Audit UTC: 2026-10-15T06:23:14.447662+00:00
Market as-of: 2026-10-14; qualified cohorts: 4; cohort rows: 513; attempts retained: 62.
Outcome counts: {'PENDING': 2410, 'INELIGIBLE_DATA': 155}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 124, 'selected': 125}.
Cycle ledger: {'complete_signal_cohorts': 4, 'pending_entries': 0, 'open_positions': 6, 'closed_trades': 0, 'benchmark_pairs': 0, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 0 | 482 | 31 | 0 | 2026-10-16 |
| 10 | 0 | 482 | 31 | 0 | 2026-10-23 |
| 20 | 0 | 482 | 31 | 0 | 2026-11-06 |
| 30 | 0 | 482 | 31 | 0 | 2026-11-20 |
| 60 | 0 | 482 | 31 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-10-14T21:31:43.451736+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 11.235538634532235, 'observed_max': 64.06132890468938, 'scored_rows': 97, 'distribution': {'BELOW_40': 14, '40_TO_49_999': 31, '50_TO_59_999': 40, '60_TO_69_999': 12, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| SCYX | 64.061 | CANDIDATE |
| FIX | 62.816 | CANDIDATE |
| XPRO | 62.298 | CANDIDATE |
| RERE | 62.254 | CANDIDATE |
| WULF | 62.144 | CANDIDATE |
| AKAM | 61.893 | CANDIDATE |
| CSIQ | 61.683 | CANDIDATE |
| NYAX | 61.655 | CANDIDATE |
| FUBO | 61.612 | CANDIDATE |
| SPGI | 61.200 | CANDIDATE |
| BXC | 60.617 | CANDIDATE |
| CHTR | 60.414 | CANDIDATE |
| JACK | 59.954 | CANDIDATE |
| ATGL | 59.377 | CANDIDATE |
| MH | 59.334 | CANDIDATE |
| INTJ | 59.075 | CANDIDATE |
| Q | 58.805 | CANDIDATE |
| EPM | 58.582 | CANDIDATE |
| MESO | 58.301 | CANDIDATE |
| SFM | 58.122 | CANDIDATE |
| ACDC | 57.566 | CANDIDATE |
| LFCR | 57.524 | CANDIDATE |
| CSPI | 57.142 | CANDIDATE |
| SGRY | 56.881 | CANDIDATE |
| SRAD | 56.756 | CANDIDATE |

## Source failures
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
