# OFTS saved-evidence report card

Audit UTC: 2026-11-19T04:00:36.828132+00:00
Market as-of: 2026-11-18; qualified cohorts: 29; cohort rows: 3987; attempts retained: 161.
Outcome counts: {'MATURE': 6067, 'PENDING': 10984, 'MISSING_SESSIONS': 7, 'INELIGIBLE_DATA': 2840, 'CORPORATE_ACTION_REVIEW': 37}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 125, 'selected': 158}.
Cycle ledger: {'complete_signal_cohorts': 29, 'pending_entries': 2, 'open_positions': 28, 'closed_trades': 34, 'benchmark_pairs': 34, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 2813 | 595 | 568 | 11 | 2026-10-16 |
| 10 | 2205 | 1195 | 568 | 19 | 2026-10-23 |
| 20 | 1049 | 2356 | 568 | 14 | 2026-11-06 |
| 30 | 0 | 3419 | 568 | 0 | 2026-11-20 |
| 60 | 0 | 3419 | 568 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-11-19T04:00:30.789982+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 9.280062252891744, 'observed_max': 68.2503810873324, 'scored_rows': 92, 'distribution': {'BELOW_40': 14, '40_TO_49_999': 36, '50_TO_59_999': 32, '60_TO_69_999': 10, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| MWH | 68.250 | CANDIDATE |
| CACC | 65.847 | CANDIDATE |
| S | 63.205 | CANDIDATE |
| WRBY | 62.920 | CANDIDATE |
| OBE | 62.718 | CANDIDATE |
| PLAB | 61.872 | CANDIDATE |
| SPGI | 60.926 | CANDIDATE |
| TDY | 60.711 | CANDIDATE |
| MIR | 60.646 | CANDIDATE |
| SGML | 60.189 | CANDIDATE |
| ESNT | 59.517 | CANDIDATE |
| MESO | 59.288 | CANDIDATE |
| METCB | 59.221 | CANDIDATE |
| ATGL | 58.323 | CANDIDATE |
| TT | 58.102 | CANDIDATE |
| ECG | 57.910 | CANDIDATE |
| XYL | 57.763 | CANDIDATE |
| CRDO | 57.464 | CANDIDATE |
| STRZ | 57.382 | CANDIDATE |
| CLSK | 57.338 | CANDIDATE |
| AKAM | 57.197 | CANDIDATE |
| TLN | 57.164 | CANDIDATE |
| HLIT | 57.015 | CANDIDATE |
| BFAM | 56.948 | CANDIDATE |
| CD | 56.773 | CANDIDATE |

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
- GNS: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- IBO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- INM: ValueError: EMPTY_PROVIDER_RESPONSE
- MKDW: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- MTAL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- RDIB: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SPWR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SPLIT_REQUIRES_DAILY_ACTION_AUDIT
- TCBI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
