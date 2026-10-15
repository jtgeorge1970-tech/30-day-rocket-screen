# OFTS saved-evidence report card

Audit UTC: 2026-10-15T21:12:52.402665+00:00
Market as-of: 2026-10-15; qualified cohorts: 5; cohort rows: 639; attempts retained: 65.
Outcome counts: {'PENDING': 2985, 'INELIGIBLE_DATA': 210}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 120, 'selected': 126}.
Cycle ledger: {'complete_signal_cohorts': 5, 'pending_entries': 4, 'open_positions': 6, 'closed_trades': 0, 'benchmark_pairs': 0, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 0 | 597 | 42 | 0 | 2026-10-16 |
| 10 | 0 | 597 | 42 | 0 | 2026-10-23 |
| 20 | 0 | 597 | 42 | 0 | 2026-11-06 |
| 30 | 0 | 597 | 42 | 0 | 2026-11-20 |
| 60 | 0 | 597 | 42 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-10-15T21:12:51.095059+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 11.93401150485412, 'observed_max': 64.09252239149635, 'scored_rows': 93, 'distribution': {'BELOW_40': 11, '40_TO_49_999': 33, '50_TO_59_999': 38, '60_TO_69_999': 11, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| SCYX | 64.093 | CANDIDATE |
| RERE | 63.291 | CANDIDATE |
| WULF | 62.149 | CANDIDATE |
| AKAM | 62.026 | CANDIDATE |
| XPRO | 61.754 | CANDIDATE |
| NYAX | 61.700 | CANDIDATE |
| SPGI | 61.155 | CANDIDATE |
| MESO | 60.968 | CANDIDATE |
| MH | 60.885 | CANDIDATE |
| CSIQ | 60.675 | CANDIDATE |
| CHTR | 60.548 | CANDIDATE |
| FUBO | 59.962 | CANDIDATE |
| ATGL | 59.451 | CANDIDATE |
| INTJ | 58.952 | CANDIDATE |
| Q | 58.790 | CANDIDATE |
| CHPT | 58.458 | CANDIDATE |
| SFM | 58.220 | CANDIDATE |
| SGRY | 57.915 | CANDIDATE |
| JACK | 57.633 | CANDIDATE |
| ACDC | 57.628 | CANDIDATE |
| LFCR | 57.555 | CANDIDATE |
| CSPI | 57.120 | CANDIDATE |
| DKNG | 56.715 | CANDIDATE |
| EPM | 56.703 | CANDIDATE |
| CRNC | 55.950 | CANDIDATE |

## Source failures
- AFJK: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SAGU: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TAP.A: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- NBR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BRT: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- AKO.A: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- AKO.B: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- BREZ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BWIV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- CODX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- GIX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- GTN.A: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- GWH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- HDL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- KCHV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- LESL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- NTHI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- QNCX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- QSEA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SIMA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TPVG: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- UCFI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- YHNA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
