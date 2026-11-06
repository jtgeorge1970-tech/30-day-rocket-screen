# OFTS saved-evidence report card

Audit UTC: 2026-11-06T11:33:25.888491+00:00
Market as-of: 2026-11-05; qualified cohorts: 20; cohort rows: 2626; attempts retained: 136.
Outcome counts: {'MATURE': 2916, 'PENDING': 8764, 'INELIGIBLE_DATA': 1435, 'CORPORATE_ACTION_REVIEW': 14, 'MISSING_SESSIONS': 1}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 121, 'selected': 140}.
Cycle ledger: {'complete_signal_cohorts': 20, 'pending_entries': 0, 'open_positions': 33, 'closed_trades': 14, 'benchmark_pairs': 14, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 1746 | 586 | 287 | 7 | 2026-10-16 |
| 10 | 1170 | 1161 | 287 | 8 | 2026-10-23 |
| 20 | 0 | 2339 | 287 | 0 | 2026-11-06 |
| 30 | 0 | 2339 | 287 | 0 | 2026-11-20 |
| 60 | 0 | 2339 | 287 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-11-06T02:55:20.549340+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 10.10326084401892, 'observed_max': 68.04345761267534, 'scored_rows': 98, 'distribution': {'BELOW_40': 11, '40_TO_49_999': 36, '50_TO_59_999': 42, '60_TO_69_999': 9, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| MWH | 68.043 | CANDIDATE |
| AKAM | 67.541 | CANDIDATE |
| ASO | 62.800 | CANDIDATE |
| TBI | 62.540 | CANDIDATE |
| SCYX | 62.471 | CANDIDATE |
| SPGI | 61.660 | CANDIDATE |
| TARS | 60.375 | CANDIDATE |
| XPRO | 59.597 | CANDIDATE |
| EPM | 59.576 | CANDIDATE |
| MESO | 59.264 | CANDIDATE |
| METCB | 58.967 | CANDIDATE |
| ASIC | 58.568 | CANDIDATE |
| CRD.B | 58.367 | CANDIDATE |
| TT | 57.981 | CANDIDATE |
| CRNC | 57.837 | CANDIDATE |
| ATGL | 57.817 | CANDIDATE |
| LOMA | 57.059 | CANDIDATE |
| GLW | 56.004 | CANDIDATE |
| CCK | 55.803 | CANDIDATE |
| DUOT | 55.786 | CANDIDATE |
| NU | 55.760 | CANDIDATE |
| SAIL | 55.441 | CANDIDATE |
| EEFT | 55.206 | CANDIDATE |
| BRCB | 55.194 | CANDIDATE |
| IDYA | 55.148 | CANDIDATE |

## Source failures
- INDV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- VSME: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- MAMK: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
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
- LNAI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- KVUE: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- ADIL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- CCXI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
