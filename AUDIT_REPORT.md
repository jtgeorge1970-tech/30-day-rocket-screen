# OFTS saved-evidence report card

Audit UTC: 2026-11-17T04:52:58.847929+00:00
Market as-of: 2026-11-16; qualified cohorts: 27; cohort rows: 3672; attempts retained: 155.
Outcome counts: {'MATURE': 5359, 'PENDING': 10503, 'MISSING_SESSIONS': 4, 'INELIGIBLE_DATA': 2460, 'CORPORATE_ACTION_REVIEW': 34}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 126, 'selected': 155}.
Cycle ledger: {'complete_signal_cohorts': 27, 'pending_entries': 0, 'open_positions': 38, 'closed_trades': 24, 'benchmark_pairs': 24, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 2572 | 598 | 492 | 10 | 2026-10-16 |
| 10 | 1971 | 1193 | 492 | 16 | 2026-10-23 |
| 20 | 816 | 2352 | 492 | 12 | 2026-11-06 |
| 30 | 0 | 3180 | 492 | 0 | 2026-11-20 |
| 60 | 0 | 3180 | 492 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-11-17T04:52:53.213760+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 10.812020991246296, 'observed_max': 68.39422789876026, 'scored_rows': 94, 'distribution': {'BELOW_40': 16, '40_TO_49_999': 32, '50_TO_59_999': 33, '60_TO_69_999': 13, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| MWH | 68.394 | CANDIDATE |
| MUR | 63.814 | CANDIDATE |
| AKAM | 63.190 | CANDIDATE |
| WRBY | 63.024 | CANDIDATE |
| OBE | 62.606 | CANDIDATE |
| DXC | 62.425 | CANDIDATE |
| CACC | 61.451 | CANDIDATE |
| S | 60.802 | CANDIDATE |
| TDY | 60.792 | CANDIDATE |
| SKY | 60.771 | CANDIDATE |
| SPGI | 60.665 | CANDIDATE |
| SGML | 60.232 | CANDIDATE |
| TT | 60.032 | CANDIDATE |
| MESO | 59.838 | CANDIDATE |
| ESNT | 59.508 | CANDIDATE |
| SCI | 59.440 | CANDIDATE |
| METCB | 59.297 | CANDIDATE |
| HLIT | 58.513 | CANDIDATE |
| ATGL | 58.395 | CANDIDATE |
| ECG | 57.956 | CANDIDATE |
| WTTR | 57.695 | CANDIDATE |
| TLN | 57.604 | CANDIDATE |
| BFAM | 56.977 | CANDIDATE |
| CCOI | 56.604 | CANDIDATE |
| ASO | 56.499 | CANDIDATE |

## Source failures
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
- INM: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ALDF: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- BFS: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- EMBJ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SPLIT_REQUIRES_DAILY_ACTION_AUDIT
- KNRX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- MGPI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- MHNC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- RDIB: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TCBI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- TGL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
