# OFTS saved-evidence report card

Audit UTC: 2026-11-28T09:30:19.044459+00:00
Market as-of: 2026-11-27; qualified cohorts: 35; cohort rows: 5016; attempts retained: 183.
Outcome counts: {'MATURE': 8738, 'PENDING': 11880, 'CORPORATE_ACTION_REVIEW': 69, 'MISSING_SESSIONS': 23, 'INELIGIBLE_DATA': 4370}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 123, 'selected': 177}.
Cycle ledger: {'complete_signal_cohorts': 35, 'pending_entries': 9, 'open_positions': 29, 'closed_trades': 45, 'benchmark_pairs': 45, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 3526 | 603 | 874 | 13 | 2026-10-16 |
| 10 | 2914 | 1201 | 874 | 27 | 2026-10-23 |
| 20 | 1718 | 2389 | 874 | 35 | 2026-11-06 |
| 30 | 580 | 3545 | 874 | 17 | 2026-11-20 |
| 60 | 0 | 4142 | 874 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-11-28T04:28:00.166653+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 11.688651812478852, 'observed_max': 67.91193702808391, 'scored_rows': 98, 'distribution': {'BELOW_40': 12, '40_TO_49_999': 41, '50_TO_59_999': 38, '60_TO_69_999': 7, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| MWH | 67.912 | CANDIDATE |
| WRBY | 63.416 | CANDIDATE |
| TRNS | 63.339 | CANDIDATE |
| ASAN | 62.035 | CANDIDATE |
| CLSK | 61.628 | CANDIDATE |
| YARW | 61.116 | CANDIDATE |
| SMPL | 60.924 | CANDIDATE |
| GLXY | 59.101 | CANDIDATE |
| SPGI | 59.055 | CANDIDATE |
| LEGN | 58.993 | CANDIDATE |
| ESNT | 58.379 | CANDIDATE |
| TT | 58.060 | CANDIDATE |
| SW | 57.987 | CANDIDATE |
| SITM | 57.857 | CANDIDATE |
| CACC | 57.726 | CANDIDATE |
| SMP | 57.579 | CANDIDATE |
| ECG | 57.467 | CANDIDATE |
| TLN | 57.420 | CANDIDATE |
| SGI | 57.314 | CANDIDATE |
| SGML | 57.184 | CANDIDATE |
| CD | 56.799 | CANDIDATE |
| GAP | 56.319 | CANDIDATE |
| MGY | 55.639 | CANDIDATE |
| USAU | 55.231 | CANDIDATE |
| STRZ | 55.006 | CANDIDATE |

## Source failures
- WPRT: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- DYNC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- BKH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- BIPC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- GSL.PRB: ValueError: EMPTY_PROVIDER_RESPONSE
- BWMN: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
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
- ITGR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- VSME: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- IBO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- KAZR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- KNRX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- LXFR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SSTI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ARI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- CLGN: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- PTLE: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- UTZ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- VABK: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- ACH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- IPFX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
