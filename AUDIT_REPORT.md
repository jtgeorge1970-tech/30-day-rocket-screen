# OFTS saved-evidence report card

Audit UTC: 2026-11-04T08:01:24.447062+00:00
Market as-of: 2026-11-03; qualified cohorts: 18; cohort rows: 2347; attempts retained: 129.
Outcome counts: {'MATURE': 2461, 'PENDING': 8059, 'INELIGIBLE_DATA': 1205, 'CORPORATE_ACTION_REVIEW': 10}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 124, 'selected': 138}.
Cycle ledger: {'complete_signal_cohorts': 18, 'pending_entries': 2, 'open_positions': 34, 'closed_trades': 6, 'benchmark_pairs': 6, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 1519 | 582 | 241 | 5 | 2026-10-16 |
| 10 | 942 | 1159 | 241 | 5 | 2026-10-23 |
| 20 | 0 | 2106 | 241 | 0 | 2026-11-06 |
| 30 | 0 | 2106 | 241 | 0 | 2026-11-20 |
| 60 | 0 | 2106 | 241 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-11-04T02:50:34.947709+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 11.629396185079681, 'observed_max': 67.78646095688094, 'scored_rows': 98, 'distribution': {'BELOW_40': 7, '40_TO_49_999': 45, '50_TO_59_999': 41, '60_TO_69_999': 5, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| AKAM | 67.786 | CANDIDATE |
| SCYX | 66.032 | CANDIDATE |
| EEFT | 64.482 | CANDIDATE |
| ASO | 63.347 | CANDIDATE |
| SPGI | 60.654 | CANDIDATE |
| XPRO | 59.687 | CANDIDATE |
| TT | 59.402 | CANDIDATE |
| EPM | 58.843 | CANDIDATE |
| TARS | 58.257 | CANDIDATE |
| PRCT | 58.088 | CANDIDATE |
| METCB | 57.955 | CANDIDATE |
| ATGL | 57.953 | CANDIDATE |
| CRNC | 57.634 | CANDIDATE |
| LOMA | 57.056 | CANDIDATE |
| VST | 56.778 | CANDIDATE |
| ROOT | 56.672 | CANDIDATE |
| MESO | 56.367 | CANDIDATE |
| CCK | 55.866 | CANDIDATE |
| SAIL | 55.672 | CANDIDATE |
| GDEV | 55.629 | CANDIDATE |
| DLTH | 55.589 | CANDIDATE |
| BRCB | 55.268 | CANDIDATE |
| IDYA | 55.202 | CANDIDATE |
| GLW | 55.197 | CANDIDATE |
| EE | 55.153 | CANDIDATE |

## Source failures
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
- LNAI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- KVUE: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
