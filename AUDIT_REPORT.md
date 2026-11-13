# OFTS saved-evidence report card

Audit UTC: 2026-11-13T03:03:45.226531+00:00
Market as-of: 2026-11-12; qualified cohorts: 25; cohort rows: 3363; attempts retained: 149.
Outcome counts: {'MATURE': 4654, 'PENDING': 10016, 'MISSING_SESSIONS': 5, 'INELIGIBLE_DATA': 2110, 'CORPORATE_ACTION_REVIEW': 30}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 120, 'selected': 149}.
Cycle ledger: {'complete_signal_cohorts': 25, 'pending_entries': 2, 'open_positions': 37, 'closed_trades': 22, 'benchmark_pairs': 22, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 2329 | 602 | 422 | 10 | 2026-10-16 |
| 10 | 1737 | 1188 | 422 | 16 | 2026-10-23 |
| 20 | 588 | 2344 | 422 | 9 | 2026-11-06 |
| 30 | 0 | 2941 | 422 | 0 | 2026-11-20 |
| 60 | 0 | 2941 | 422 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-11-13T03:03:41.707747+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 12.009358685782429, 'observed_max': 68.29485969280613, 'scored_rows': 100, 'distribution': {'BELOW_40': 14, '40_TO_49_999': 40, '50_TO_59_999': 38, '60_TO_69_999': 8, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| MWH | 68.295 | CANDIDATE |
| MESO | 62.929 | CANDIDATE |
| DXC | 62.547 | CANDIDATE |
| WRBY | 62.179 | CANDIDATE |
| SPGI | 61.998 | CANDIDATE |
| BFAM | 61.262 | CANDIDATE |
| SCYX | 60.350 | CANDIDATE |
| CRNC | 60.314 | CANDIDATE |
| DUOT | 59.984 | CANDIDATE |
| OBE | 59.929 | CANDIDATE |
| ESNT | 59.542 | CANDIDATE |
| SCI | 59.203 | CANDIDATE |
| METCB | 59.122 | CANDIDATE |
| EPOW | 59.060 | CANDIDATE |
| ASO | 58.944 | CANDIDATE |
| HLIT | 58.631 | CANDIDATE |
| ATGL | 58.593 | CANDIDATE |
| COOK | 58.456 | CANDIDATE |
| TT | 58.236 | CANDIDATE |
| CNXN | 58.029 | CANDIDATE |
| TLN | 57.732 | CANDIDATE |
| AKAM | 57.182 | CANDIDATE |
| CTSO | 56.859 | CANDIDATE |
| LINE | 56.628 | CANDIDATE |
| ECG | 56.509 | CANDIDATE |

## Source failures
- CBZ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- MIMI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- BZH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- NATH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WALD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- LRHC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WFC.PRL: ValueError: EMPTY_PROVIDER_RESPONSE
- INDV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
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
- KVUE: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ADIL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- CCXI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- GNTA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ALDF: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- CCU: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- CLBR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- KNRX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- RDIB: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SAGU: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- VECA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
