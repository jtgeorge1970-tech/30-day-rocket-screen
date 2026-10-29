# OFTS saved-evidence report card

Audit UTC: 2026-10-29T07:42:15.640588+00:00
Market as-of: 2026-10-28; qualified cohorts: 14; cohort rows: 1802; attempts retained: 111.
Outcome counts: {'MATURE': 1538, 'PENDING': 6650, 'INELIGIBLE_DATA': 815, 'CORPORATE_ACTION_REVIEW': 7}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 122, 'selected': 132}.
Cycle ledger: {'complete_signal_cohorts': 14, 'pending_entries': 2, 'open_positions': 31, 'closed_trades': 2, 'benchmark_pairs': 2, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 1060 | 576 | 163 | 3 | 2026-10-16 |
| 10 | 478 | 1157 | 163 | 4 | 2026-10-23 |
| 20 | 0 | 1639 | 163 | 0 | 2026-11-06 |
| 30 | 0 | 1639 | 163 | 0 | 2026-11-20 |
| 60 | 0 | 1639 | 163 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-10-29T02:02:11.567272+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 10.745352243166598, 'observed_max': 67.47318717243705, 'scored_rows': 95, 'distribution': {'BELOW_40': 10, '40_TO_49_999': 39, '50_TO_59_999': 36, '60_TO_69_999': 10, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| SCYX | 67.473 | CANDIDATE |
| ASO | 64.477 | CANDIDATE |
| MESO | 64.299 | CANDIDATE |
| AKAM | 62.402 | CANDIDATE |
| SPGI | 61.989 | CANDIDATE |
| TT | 60.950 | CANDIDATE |
| WOR | 60.595 | CANDIDATE |
| LOMA | 60.402 | CANDIDATE |
| TARS | 60.198 | CANDIDATE |
| ATGL | 59.787 | CANDIDATE |
| NYAX | 59.689 | CANDIDATE |
| GLW | 59.333 | CANDIDATE |
| XPRO | 59.004 | CANDIDATE |
| EEFT | 58.842 | CANDIDATE |
| LFCR | 58.721 | CANDIDATE |
| FUBO | 58.515 | CANDIDATE |
| OMC | 57.817 | CANDIDATE |
| DKNG | 57.811 | CANDIDATE |
| CRNC | 57.763 | CANDIDATE |
| CCS | 57.616 | CANDIDATE |
| EPM | 57.583 | CANDIDATE |
| FERG | 57.133 | CANDIDATE |
| METCB | 56.797 | CANDIDATE |
| FISV | 56.472 | CANDIDATE |
| VIRC | 56.419 | CANDIDATE |

## Source failures
- ACA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- QRVO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- PERF: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- GAM.PRB: ValueError: EMPTY_PROVIDER_RESPONSE
- SPG.PRJ: ValueError: EMPTY_PROVIDER_RESPONSE
- GS.PRA: ValueError: EMPTY_PROVIDER_RESPONSE
- NVNI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SB.PRC: ValueError: EMPTY_PROVIDER_RESPONSE
- SLP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
