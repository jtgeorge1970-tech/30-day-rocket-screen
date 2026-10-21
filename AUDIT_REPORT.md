# OFTS saved-evidence report card

Audit UTC: 2026-10-21T23:08:51.159208+00:00
Market as-of: 2026-10-21; qualified cohorts: 8; cohort rows: 1020; attempts retained: 85.
Outcome counts: {'MATURE': 478, 'PENDING': 4253, 'INELIGIBLE_DATA': 365, 'CORPORATE_ACTION_REVIEW': 2, 'MISSING_SESSIONS': 2}.
Saved-data freshness gate: {'passed': False, 'required_stale': ['CCS'], 'fresh': 120, 'selected': 129}.
Cycle ledger: {'complete_signal_cohorts': 8, 'pending_entries': 0, 'open_positions': 15, 'closed_trades': 0, 'benchmark_pairs': 0, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 478 | 465 | 73 | 4 | 2026-10-16 |
| 10 | 0 | 947 | 73 | 0 | 2026-10-23 |
| 20 | 0 | 947 | 73 | 0 | 2026-11-06 |
| 30 | 0 | 947 | 73 | 0 | 2026-11-20 |
| 60 | 0 | 947 | 73 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-10-21T06:33:39.977822+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 11.788948608821608, 'observed_max': 63.975759674336935, 'scored_rows': 94, 'distribution': {'BELOW_40': 16, '40_TO_49_999': 33, '50_TO_59_999': 39, '60_TO_69_999': 6, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| SCYX | 63.976 | CANDIDATE |
| Q | 62.338 | CANDIDATE |
| RERE | 62.136 | CANDIDATE |
| CHTR | 60.545 | CANDIDATE |
| NYAX | 60.476 | CANDIDATE |
| XPRO | 60.028 | CANDIDATE |
| ATGL | 59.956 | CANDIDATE |
| AKAM | 59.861 | CANDIDATE |
| SPGI | 59.544 | CANDIDATE |
| FUBO | 59.426 | CANDIDATE |
| CHPT | 59.162 | CANDIDATE |
| CRNC | 58.702 | CANDIDATE |
| DKNG | 58.556 | CANDIDATE |
| CCS | 57.800 | CANDIDATE |
| LFCR | 57.680 | CANDIDATE |
| ACDC | 57.516 | CANDIDATE |
| VIRC | 57.365 | CANDIDATE |
| TT | 57.236 | CANDIDATE |
| FERG | 57.042 | CANDIDATE |
| MESO | 57.000 | CANDIDATE |
| MH | 56.993 | CANDIDATE |
| EPM | 56.923 | CANDIDATE |
| SGRY | 56.516 | CANDIDATE |
| FFBC | 56.261 | CANDIDATE |
| SFM | 54.859 | CANDIDATE |

## Source failures
- CCS: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- NCO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ARCI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- GS.PRA: ValueError: EMPTY_PROVIDER_RESPONSE
- TRGS: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- NVNI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SB.PRC: ValueError: EMPTY_PROVIDER_RESPONSE
- SLP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ACGC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- AEON: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- AFJK: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- AKO.A: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- APWC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- ARCL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BRKH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BRT: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BWIV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- CEPV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- CQP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- DYOR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- ELTK: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- FEBO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- FTRA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- GIX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- GROV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- GWH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- IBTA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- JACS: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- KCHV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- KOP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- KWR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- LESL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- LIVE: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- MPTI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- PONO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- QNCX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- RMCO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SAC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SENEB: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SIMA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SOS: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SSEA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SVCC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TAP.A: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- UCFI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WFG: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- YHNA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
