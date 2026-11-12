# OFTS saved-evidence report card

Audit UTC: 2026-11-12T08:56:28.238177+00:00
Market as-of: 2026-11-11; qualified cohorts: 24; cohort rows: 3214; attempts retained: 147.
Outcome counts: {'MATURE': 4316, 'PENDING': 9775, 'MISSING_SESSIONS': 4, 'INELIGIBLE_DATA': 1950, 'CORPORATE_ACTION_REVIEW': 25}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 125, 'selected': 149}.
Cycle ledger: {'complete_signal_cohorts': 24, 'pending_entries': 2, 'open_positions': 37, 'closed_trades': 20, 'benchmark_pairs': 20, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 2215 | 600 | 390 | 9 | 2026-10-16 |
| 10 | 1627 | 1185 | 390 | 12 | 2026-10-23 |
| 20 | 474 | 2342 | 390 | 8 | 2026-11-06 |
| 30 | 0 | 2824 | 390 | 0 | 2026-11-20 |
| 60 | 0 | 2824 | 390 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-11-12T03:25:19.645545+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 12.711807464839426, 'observed_max': 68.3899852324604, 'scored_rows': 102, 'distribution': {'BELOW_40': 20, '40_TO_49_999': 38, '50_TO_59_999': 37, '60_TO_69_999': 7, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| MWH | 68.390 | CANDIDATE |
| MESO | 62.375 | CANDIDATE |
| SPGI | 61.960 | CANDIDATE |
| BFAM | 61.209 | CANDIDATE |
| DUOT | 61.144 | CANDIDATE |
| CRNC | 60.257 | CANDIDATE |
| OBE | 60.135 | CANDIDATE |
| ASO | 59.766 | CANDIDATE |
| SCYX | 59.696 | CANDIDATE |
| ESNT | 59.523 | CANDIDATE |
| SCI | 59.236 | CANDIDATE |
| METCB | 59.026 | CANDIDATE |
| ATGL | 58.831 | CANDIDATE |
| TT | 58.248 | CANDIDATE |
| IMTX | 57.863 | CANDIDATE |
| TLN | 57.707 | CANDIDATE |
| DXC | 57.365 | CANDIDATE |
| AKAM | 57.198 | CANDIDATE |
| CNXN | 57.027 | CANDIDATE |
| CTSO | 56.796 | CANDIDATE |
| MMYT | 56.758 | CANDIDATE |
| LINE | 56.707 | CANDIDATE |
| HELP | 56.510 | CANDIDATE |
| HLIT | 56.142 | CANDIDATE |
| MTG | 55.965 | CANDIDATE |

## Source failures
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

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
