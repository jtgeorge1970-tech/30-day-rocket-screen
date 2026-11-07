# OFTS saved-evidence report card

Audit UTC: 2026-11-07T07:52:14.648508+00:00
Market as-of: 2026-11-06; qualified cohorts: 21; cohort rows: 2772; attempts retained: 138.
Outcome counts: {'MATURE': 3269, 'PENDING': 9009, 'MISSING_SESSIONS': 2, 'INELIGIBLE_DATA': 1565, 'CORPORATE_ACTION_REVIEW': 15}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 125, 'selected': 146}.
Cycle ledger: {'complete_signal_cohorts': 21, 'pending_entries': 1, 'open_positions': 28, 'closed_trades': 19, 'benchmark_pairs': 19, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 1864 | 588 | 313 | 7 | 2026-10-16 |
| 10 | 1285 | 1165 | 313 | 9 | 2026-10-23 |
| 20 | 120 | 2338 | 313 | 1 | 2026-11-06 |
| 30 | 0 | 2459 | 313 | 0 | 2026-11-20 |
| 60 | 0 | 2459 | 313 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-11-07T07:52:10.786007+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 13.32078622571862, 'observed_max': 68.21900290616671, 'scored_rows': 101, 'distribution': {'BELOW_40': 10, '40_TO_49_999': 39, '50_TO_59_999': 45, '60_TO_69_999': 7, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| MWH | 68.219 | CANDIDATE |
| AKAM | 67.588 | CANDIDATE |
| PPHC | 65.732 | CANDIDATE |
| TBI | 63.540 | CANDIDATE |
| SPGI | 61.194 | CANDIDATE |
| EPM | 60.372 | CANDIDATE |
| LBTYB | 60.109 | CANDIDATE |
| SCYX | 59.714 | CANDIDATE |
| MESO | 59.451 | CANDIDATE |
| ASO | 59.091 | CANDIDATE |
| METCB | 59.009 | CANDIDATE |
| CRNC | 58.695 | CANDIDATE |
| OBE | 58.670 | CANDIDATE |
| XPRO | 58.579 | CANDIDATE |
| ASIC | 58.449 | CANDIDATE |
| HLIT | 58.378 | CANDIDATE |
| TT | 58.347 | CANDIDATE |
| CRD.B | 58.305 | CANDIDATE |
| DXC | 58.277 | CANDIDATE |
| ATGL | 57.564 | CANDIDATE |
| LOMA | 56.918 | CANDIDATE |
| SLNG | 56.406 | CANDIDATE |
| GLW | 56.113 | CANDIDATE |
| CCK | 55.887 | CANDIDATE |
| DUOT | 55.875 | CANDIDATE |

## Source failures
- INDV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
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

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
