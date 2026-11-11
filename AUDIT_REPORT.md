# OFTS saved-evidence report card

Audit UTC: 2026-11-11T08:25:05.777943+00:00
Market as-of: 2026-11-10; qualified cohorts: 23; cohort rows: 3065; attempts retained: 144.
Outcome counts: {'MATURE': 3971, 'PENDING': 9525, 'MISSING_SESSIONS': 2, 'INELIGIBLE_DATA': 1805, 'CORPORATE_ACTION_REVIEW': 22}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 123, 'selected': 147}.
Cycle ledger: {'complete_signal_cohorts': 23, 'pending_entries': 3, 'open_positions': 34, 'closed_trades': 20, 'benchmark_pairs': 20, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 2099 | 598 | 361 | 7 | 2026-10-16 |
| 10 | 1513 | 1180 | 361 | 11 | 2026-10-23 |
| 20 | 359 | 2339 | 361 | 6 | 2026-11-06 |
| 30 | 0 | 2704 | 361 | 0 | 2026-11-20 |
| 60 | 0 | 2704 | 361 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-11-11T08:25:00.995819+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 11.194940444955614, 'observed_max': 68.3761930201991, 'scored_rows': 98, 'distribution': {'BELOW_40': 17, '40_TO_49_999': 39, '50_TO_59_999': 33, '60_TO_69_999': 9, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| MWH | 68.376 | CANDIDATE |
| DXC | 64.650 | CANDIDATE |
| SCYX | 63.790 | CANDIDATE |
| LBTYB | 63.635 | CANDIDATE |
| EPM | 63.618 | CANDIDATE |
| MESO | 62.143 | CANDIDATE |
| SPGI | 62.036 | CANDIDATE |
| CRNC | 60.217 | CANDIDATE |
| CTSO | 60.025 | CANDIDATE |
| ASO | 59.747 | CANDIDATE |
| OBE | 59.397 | CANDIDATE |
| ATGL | 59.092 | CANDIDATE |
| METCB | 59.034 | CANDIDATE |
| AKAM | 59.020 | CANDIDATE |
| TT | 58.029 | CANDIDATE |
| TLN | 57.832 | CANDIDATE |
| DUOT | 57.446 | CANDIDATE |
| IMTX | 57.287 | CANDIDATE |
| CNXN | 56.698 | CANDIDATE |
| LINE | 56.612 | CANDIDATE |
| HELP | 56.527 | CANDIDATE |
| HLIT | 56.117 | CANDIDATE |
| MTG | 55.984 | CANDIDATE |
| CCK | 55.768 | CANDIDATE |
| TBI | 55.641 | CANDIDATE |

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
- CCXI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- RDIB: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TCBI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
