# OFTS saved-evidence report card

Audit UTC: 2026-11-10T04:24:05.155686+00:00
Market as-of: 2026-11-09; qualified cohorts: 22; cohort rows: 2918; attempts retained: 140.
Outcome counts: {'MATURE': 3611, 'PENDING': 9279, 'MISSING_SESSIONS': 2, 'INELIGIBLE_DATA': 1680, 'CORPORATE_ACTION_REVIEW': 18}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 124, 'selected': 146}.
Cycle ledger: {'complete_signal_cohorts': 22, 'pending_entries': 6, 'open_positions': 28, 'closed_trades': 20, 'benchmark_pairs': 20, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 1980 | 595 | 336 | 7 | 2026-10-16 |
| 10 | 1401 | 1172 | 336 | 9 | 2026-10-23 |
| 20 | 230 | 2348 | 336 | 4 | 2026-11-06 |
| 30 | 0 | 2582 | 336 | 0 | 2026-11-20 |
| 60 | 0 | 2582 | 336 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-11-10T04:24:01.200431+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 32.23694167025438, 'observed_max': 68.29728282833231, 'scored_rows': 101, 'distribution': {'BELOW_40': 14, '40_TO_49_999': 41, '50_TO_59_999': 39, '60_TO_69_999': 7, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| MWH | 68.297 | CANDIDATE |
| AKAM | 66.283 | CANDIDATE |
| SCYX | 63.745 | CANDIDATE |
| MESO | 62.172 | CANDIDATE |
| SPGI | 62.070 | CANDIDATE |
| EPM | 61.064 | CANDIDATE |
| LBTYB | 60.242 | CANDIDATE |
| ASO | 59.758 | CANDIDATE |
| OBE | 59.096 | CANDIDATE |
| METCB | 59.065 | CANDIDATE |
| PPHC | 59.018 | CANDIDATE |
| TBI | 58.923 | CANDIDATE |
| CRNC | 58.704 | CANDIDATE |
| HLIT | 58.610 | CANDIDATE |
| SBGI | 58.547 | CANDIDATE |
| DXC | 58.219 | CANDIDATE |
| TT | 58.052 | CANDIDATE |
| XPRO | 57.916 | CANDIDATE |
| OLLI | 57.412 | CANDIDATE |
| ATGL | 57.386 | CANDIDATE |
| IMTX | 57.328 | CANDIDATE |
| SLNG | 56.873 | CANDIDATE |
| HELP | 56.533 | CANDIDATE |
| DUOT | 56.241 | CANDIDATE |
| CCK | 55.788 | CANDIDATE |

## Source failures
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
- CCXI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- AAC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- CLBR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- FTRA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- RDIB: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SAGU: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TCBI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
