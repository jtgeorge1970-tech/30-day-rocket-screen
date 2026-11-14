# OFTS saved-evidence report card

Audit UTC: 2026-11-14T10:58:11.228198+00:00
Market as-of: 2026-11-13; qualified cohorts: 26; cohort rows: 3517; attempts retained: 154.
Outcome counts: {'MATURE': 5010, 'PENDING': 10260, 'MISSING_SESSIONS': 4, 'INELIGIBLE_DATA': 2280, 'CORPORATE_ACTION_REVIEW': 31}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 125, 'selected': 154}.
Cycle ledger: {'complete_signal_cohorts': 26, 'pending_entries': 1, 'open_positions': 38, 'closed_trades': 23, 'benchmark_pairs': 23, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 2449 | 602 | 456 | 10 | 2026-10-16 |
| 10 | 1855 | 1190 | 456 | 16 | 2026-10-23 |
| 20 | 706 | 2346 | 456 | 9 | 2026-11-06 |
| 30 | 0 | 3061 | 456 | 0 | 2026-11-20 |
| 60 | 0 | 3061 | 456 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-11-14T02:48:57.839918+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 12.697831935764821, 'observed_max': 68.34102062980467, 'scored_rows': 95, 'distribution': {'BELOW_40': 14, '40_TO_49_999': 33, '50_TO_59_999': 37, '60_TO_69_999': 11, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| MWH | 68.341 | CANDIDATE |
| MUR | 64.793 | CANDIDATE |
| AKAM | 63.680 | CANDIDATE |
| SCYX | 63.190 | CANDIDATE |
| MESO | 63.173 | CANDIDATE |
| DXC | 62.572 | CANDIDATE |
| WRBY | 62.166 | CANDIDATE |
| SPGI | 61.931 | CANDIDATE |
| SKY | 60.785 | CANDIDATE |
| SGML | 60.324 | CANDIDATE |
| TT | 60.117 | CANDIDATE |
| OBE | 59.882 | CANDIDATE |
| ESNT | 59.550 | CANDIDATE |
| SCI | 59.459 | CANDIDATE |
| EPOW | 59.148 | CANDIDATE |
| FORTY | 58.993 | CANDIDATE |
| METCB | 58.881 | CANDIDATE |
| COOK | 58.455 | CANDIDATE |
| ATGL | 58.389 | CANDIDATE |
| HLIT | 58.332 | CANDIDATE |
| CNXN | 58.077 | CANDIDATE |
| ASO | 57.770 | CANDIDATE |
| TLN | 57.693 | CANDIDATE |
| ECG | 57.291 | CANDIDATE |
| BFAM | 57.028 | CANDIDATE |

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
- INM: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
