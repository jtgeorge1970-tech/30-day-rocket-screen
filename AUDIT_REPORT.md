# OFTS saved-evidence report card

Audit UTC: 2026-11-20T12:12:34.961562+00:00
Market as-of: 2026-11-19; qualified cohorts: 30; cohort rows: 4146; attempts retained: 166.
Outcome counts: {'MATURE': 6409, 'PENDING': 11237, 'MISSING_SESSIONS': 9, 'INELIGIBLE_DATA': 3035, 'CORPORATE_ACTION_REVIEW': 40}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 122, 'selected': 159}.
Cycle ledger: {'complete_signal_cohorts': 30, 'pending_entries': 1, 'open_positions': 29, 'closed_trades': 35, 'benchmark_pairs': 35, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 2929 | 598 | 607 | 12 | 2026-10-16 |
| 10 | 2319 | 1200 | 607 | 20 | 2026-10-23 |
| 20 | 1161 | 2361 | 607 | 17 | 2026-11-06 |
| 30 | 0 | 3539 | 607 | 0 | 2026-11-20 |
| 60 | 0 | 3539 | 607 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-11-20T09:18:17.133325+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 8.950692912157539, 'observed_max': 69.26211444649539, 'scored_rows': 93, 'distribution': {'BELOW_40': 15, '40_TO_49_999': 33, '50_TO_59_999': 38, '60_TO_69_999': 7, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| CACC | 69.262 | CANDIDATE |
| MWH | 68.323 | CANDIDATE |
| WRBY | 63.225 | CANDIDATE |
| OBE | 62.746 | CANDIDATE |
| PLAB | 61.886 | CANDIDATE |
| SPGI | 60.850 | CANDIDATE |
| MIR | 60.657 | CANDIDATE |
| ESNT | 59.433 | CANDIDATE |
| MESO | 59.294 | CANDIDATE |
| METCB | 59.096 | CANDIDATE |
| LI | 58.618 | CANDIDATE |
| ATGL | 58.470 | CANDIDATE |
| TT | 58.027 | CANDIDATE |
| HLIT | 57.887 | CANDIDATE |
| TLN | 57.884 | CANDIDATE |
| ECG | 57.847 | CANDIDATE |
| XYL | 57.684 | CANDIDATE |
| STRZ | 57.453 | CANDIDATE |
| CLSK | 57.414 | CANDIDATE |
| CD | 57.100 | CANDIDATE |
| BFAM | 56.791 | CANDIDATE |
| SGML | 56.668 | CANDIDATE |
| AKAM | 56.202 | CANDIDATE |
| CRDO | 55.232 | CANDIDATE |
| LYFT | 55.066 | CANDIDATE |

## Source failures
- SB.PRD: ValueError: EMPTY_PROVIDER_RESPONSE
- MET.PRA: ValueError: EMPTY_PROVIDER_RESPONSE
- WKEY: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ACVA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- CBZ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- MIMI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- BZH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- NATH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WALD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- LRHC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WFC.PRL: ValueError: EMPTY_PROVIDER_RESPONSE
- INDV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- MAMK: ValueError: EMPTY_PROVIDER_RESPONSE
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
- KVUE: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ADIL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- CCXI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- GNTA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ALDF: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- MGPI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ITGR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- VSME: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- IBO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- KAZR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- KNRX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- LXFR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SSTI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
