# OFTS saved-evidence report card

Audit UTC: 2026-10-31T07:34:04.725590+00:00
Market as-of: 2026-10-30; qualified cohorts: 16; cohort rows: 2073; attempts retained: 121.
Outcome counts: {'MATURE': 2000, 'PENDING': 7346, 'INELIGIBLE_DATA': 1010, 'CORPORATE_ACTION_REVIEW': 9}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 124, 'selected': 135}.
Cycle ledger: {'complete_signal_cohorts': 16, 'pending_entries': 2, 'open_positions': 33, 'closed_trades': 3, 'benchmark_pairs': 3, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 1289 | 577 | 202 | 5 | 2026-10-16 |
| 10 | 711 | 1156 | 202 | 4 | 2026-10-23 |
| 20 | 0 | 1871 | 202 | 0 | 2026-11-06 |
| 30 | 0 | 1871 | 202 | 0 | 2026-11-20 |
| 60 | 0 | 1871 | 202 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-10-30T23:05:18.621149+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 11.58497992944324, 'observed_max': 66.73869727478981, 'scored_rows': 99, 'distribution': {'BELOW_40': 11, '40_TO_49_999': 41, '50_TO_59_999': 39, '60_TO_69_999': 8, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| SCYX | 66.739 | CANDIDATE |
| ASO | 63.005 | CANDIDATE |
| CRNC | 62.626 | CANDIDATE |
| AKAM | 62.339 | CANDIDATE |
| EEFT | 62.063 | CANDIDATE |
| SPGI | 61.808 | CANDIDATE |
| TT | 60.524 | CANDIDATE |
| ADXN | 60.410 | CANDIDATE |
| MESO | 59.975 | CANDIDATE |
| NYAX | 59.813 | CANDIDATE |
| XPRO | 59.688 | CANDIDATE |
| EE | 59.567 | CANDIDATE |
| GLW | 59.292 | CANDIDATE |
| ATGL | 59.027 | CANDIDATE |
| PLBL | 59.018 | CANDIDATE |
| FUBO | 58.549 | CANDIDATE |
| BRCB | 58.409 | CANDIDATE |
| EME | 58.130 | CANDIDATE |
| TARS | 57.906 | CANDIDATE |
| VST | 57.804 | CANDIDATE |
| EPM | 57.494 | CANDIDATE |
| BMBL | 57.354 | CANDIDATE |
| LOMA | 57.140 | CANDIDATE |
| METCB | 56.852 | CANDIDATE |
| VIRC | 56.822 | CANDIDATE |

## Source failures
- USB.PRH: ValueError: EMPTY_PROVIDER_RESPONSE
- ACA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- QRVO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- PERF: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- GAM.PRB: ValueError: EMPTY_PROVIDER_RESPONSE
- SPG.PRJ: ValueError: EMPTY_PROVIDER_RESPONSE
- GS.PRA: ValueError: EMPTY_PROVIDER_RESPONSE
- NVNI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SB.PRC: ValueError: EMPTY_PROVIDER_RESPONSE
- SLP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- LNAI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
