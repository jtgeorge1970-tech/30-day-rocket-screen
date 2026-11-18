# OFTS saved-evidence report card

Audit UTC: 2026-11-18T12:18:28.252229+00:00
Market as-of: 2026-11-17; qualified cohorts: 28; cohort rows: 3829; attempts retained: 160.
Outcome counts: {'MATURE': 5718, 'PENDING': 10758, 'MISSING_SESSIONS': 5, 'INELIGIBLE_DATA': 2630, 'CORPORATE_ACTION_REVIEW': 34}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 126, 'selected': 157}.
Cycle ledger: {'complete_signal_cohorts': 28, 'pending_entries': 0, 'open_positions': 33, 'closed_trades': 29, 'benchmark_pairs': 29, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 2694 | 599 | 526 | 10 | 2026-10-16 |
| 10 | 2089 | 1197 | 526 | 17 | 2026-10-23 |
| 20 | 935 | 2356 | 526 | 12 | 2026-11-06 |
| 30 | 0 | 3303 | 526 | 0 | 2026-11-20 |
| 60 | 0 | 3303 | 526 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-11-18T03:59:56.278439+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 12.969752731266423, 'observed_max': 68.28982991323286, 'scored_rows': 102, 'distribution': {'BELOW_40': 13, '40_TO_49_999': 39, '50_TO_59_999': 40, '60_TO_69_999': 10, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| MWH | 68.290 | CANDIDATE |
| S | 63.358 | CANDIDATE |
| AKAM | 63.188 | CANDIDATE |
| WRBY | 63.001 | CANDIDATE |
| DXC | 62.373 | CANDIDATE |
| CACC | 61.494 | CANDIDATE |
| SPGI | 60.878 | CANDIDATE |
| SKY | 60.809 | CANDIDATE |
| TDY | 60.785 | CANDIDATE |
| SGML | 60.191 | CANDIDATE |
| TT | 59.984 | CANDIDATE |
| ESNT | 59.494 | CANDIDATE |
| METCB | 59.293 | CANDIDATE |
| OBE | 59.083 | CANDIDATE |
| HLIT | 58.528 | CANDIDATE |
| ATGL | 58.364 | CANDIDATE |
| ECG | 57.911 | CANDIDATE |
| CRDO | 57.416 | CANDIDATE |
| STRZ | 57.411 | CANDIDATE |
| MESO | 57.247 | CANDIDATE |
| TLN | 57.179 | CANDIDATE |
| BFAM | 56.944 | CANDIDATE |
| CD | 56.835 | CANDIDATE |
| CCOI | 56.599 | CANDIDATE |
| ASO | 56.547 | CANDIDATE |

## Source failures
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

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
