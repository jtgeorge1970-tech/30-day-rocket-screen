# OFTS saved-evidence report card

Audit UTC: 2026-11-05T08:37:00.872142+00:00
Market as-of: 2026-11-04; qualified cohorts: 19; cohort rows: 2486; attempts retained: 132.
Outcome counts: {'MATURE': 2691, 'PENDING': 8418, 'INELIGIBLE_DATA': 1310, 'CORPORATE_ACTION_REVIEW': 11}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 123, 'selected': 139}.
Cycle ledger: {'complete_signal_cohorts': 19, 'pending_entries': 5, 'open_positions': 32, 'closed_trades': 10, 'benchmark_pairs': 10, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 1634 | 585 | 262 | 5 | 2026-10-16 |
| 10 | 1057 | 1161 | 262 | 6 | 2026-10-23 |
| 20 | 0 | 2224 | 262 | 0 | 2026-11-06 |
| 30 | 0 | 2224 | 262 | 0 | 2026-11-20 |
| 60 | 0 | 2224 | 262 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-11-05T02:51:09.471048+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 10.40137643498515, 'observed_max': 67.73065868382596, 'scored_rows': 92, 'distribution': {'BELOW_40': 14, '40_TO_49_999': 40, '50_TO_59_999': 32, '60_TO_69_999': 6, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| AKAM | 67.731 | CANDIDATE |
| EEFT | 64.855 | CANDIDATE |
| SCYX | 64.089 | CANDIDATE |
| TBI | 63.432 | CANDIDATE |
| ASO | 62.784 | CANDIDATE |
| SPGI | 60.419 | CANDIDATE |
| XPRO | 59.632 | CANDIDATE |
| TT | 59.304 | CANDIDATE |
| EPM | 58.707 | CANDIDATE |
| TARS | 58.408 | CANDIDATE |
| METCB | 58.155 | CANDIDATE |
| ATGL | 57.958 | CANDIDATE |
| CRNC | 57.599 | CANDIDATE |
| LOMA | 57.089 | CANDIDATE |
| ROOT | 56.741 | CANDIDATE |
| VST | 56.604 | CANDIDATE |
| MESO | 56.398 | CANDIDATE |
| CRD.B | 56.174 | CANDIDATE |
| CCK | 55.660 | CANDIDATE |
| SAIL | 55.407 | CANDIDATE |
| OABI | 55.287 | CANDIDATE |
| SLDE | 55.188 | CANDIDATE |
| IDYA | 55.167 | CANDIDATE |
| GLW | 55.156 | CANDIDATE |
| BRCB | 55.150 | CANDIDATE |

## Source failures
- MS.PRF: ValueError: EMPTY_PROVIDER_RESPONSE
- PSKY: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ALL.PRI: ValueError: EMPTY_PROVIDER_RESPONSE
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
- KVUE: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
