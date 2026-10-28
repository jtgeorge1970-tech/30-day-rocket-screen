# OFTS saved-evidence report card

Audit UTC: 2026-10-28T16:53:06.994439+00:00
Market as-of: 2026-10-27; qualified cohorts: 13; cohort rows: 1670; attempts retained: 108.
Outcome counts: {'MATURE': 1307, 'PENDING': 6308, 'INELIGIBLE_DATA': 730, 'CORPORATE_ACTION_REVIEW': 5}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 123, 'selected': 130}.
Cycle ledger: {'complete_signal_cohorts': 13, 'pending_entries': 6, 'open_positions': 26, 'closed_trades': 1, 'benchmark_pairs': 1, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 945 | 577 | 146 | 2 | 2026-10-16 |
| 10 | 362 | 1159 | 146 | 3 | 2026-10-23 |
| 20 | 0 | 1524 | 146 | 0 | 2026-11-06 |
| 30 | 0 | 1524 | 146 | 0 | 2026-11-20 |
| 60 | 0 | 1524 | 146 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-10-27T23:20:45.495002+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 13.932595241509777, 'observed_max': 68.3978448348677, 'scored_rows': 89, 'distribution': {'BELOW_40': 8, '40_TO_49_999': 43, '50_TO_59_999': 31, '60_TO_69_999': 7, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| SCYX | 68.398 | CANDIDATE |
| ASO | 64.213 | CANDIDATE |
| SPGI | 62.022 | CANDIDATE |
| MESO | 61.211 | CANDIDATE |
| TT | 60.873 | CANDIDATE |
| AKAM | 60.756 | CANDIDATE |
| WOR | 60.225 | CANDIDATE |
| ATGL | 59.731 | CANDIDATE |
| FUBO | 59.446 | CANDIDATE |
| NYAX | 59.260 | CANDIDATE |
| GLW | 59.221 | CANDIDATE |
| XPRO | 59.080 | CANDIDATE |
| LFCR | 58.705 | CANDIDATE |
| EEFT | 58.570 | CANDIDATE |
| CHPT | 58.519 | CANDIDATE |
| CCS | 57.980 | CANDIDATE |
| KTB | 57.822 | CANDIDATE |
| CRNC | 57.641 | CANDIDATE |
| EPM | 57.552 | CANDIDATE |
| DKNG | 57.535 | CANDIDATE |
| VIRC | 57.441 | CANDIDATE |
| LTRX | 57.084 | CANDIDATE |
| FERG | 57.067 | CANDIDATE |
| DJT | 56.810 | CANDIDATE |
| CCEL | 56.050 | CANDIDATE |

## Source failures
- GAM.PRB: ValueError: EMPTY_PROVIDER_RESPONSE
- SPG.PRJ: ValueError: EMPTY_PROVIDER_RESPONSE
- GS.PRA: ValueError: EMPTY_PROVIDER_RESPONSE
- NVNI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SB.PRC: ValueError: EMPTY_PROVIDER_RESPONSE
- SLP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
