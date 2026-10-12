# OFTS saved-evidence report card

Audit UTC: 2026-10-12T23:30:19.022782+00:00
Market as-of: 2026-10-12; qualified cohorts: 2; cohort rows: 250; attempts retained: 50.
Outcome counts: {'PENDING': 1170, 'INELIGIBLE_DATA': 80}.
Saved-data freshness gate: {'passed': True, 'required_stale': [], 'fresh': 116, 'selected': 125}.
Cycle ledger: {'complete_signal_cohorts': 2, 'pending_entries': 2, 'open_positions': 1, 'closed_trades': 0, 'benchmark_pairs': 0, 'review_trades': 0}.
Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.
Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.
Rejected candidates are controls. Overlapping horizons are not independent trades.

| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |
|---|---:|---:|---:|---:|---|
| 5 | 0 | 234 | 16 | 0 | 2026-10-16 |
| 10 | 0 | 234 | 16 | 0 | 2026-10-23 |
| 20 | 0 | 234 | 16 | 0 | 2026-11-06 |
| 30 | 0 | 234 | 16 | 0 | 2026-11-20 |
| 60 | 0 | 234 | 16 | 0 | 2027-01-06 |

By model, horizon and score band: see latest_audit.json. Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.

## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)
Cohort recorded: 2026-10-12T23:30:18.246918+00:00; model: a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b.
Score distribution: {'theoretical_scale_min': 0, 'theoretical_scale_max': 100, 'observed_min': 12.679901321656114, 'observed_max': 72.9667877123091, 'scored_rows': 92, 'distribution': {'BELOW_40': 11, '40_TO_49_999': 36, '50_TO_59_999': 34, '60_TO_69_999': 10, '70_TO_79_999': 1, '80_TO_89_999': 0, '90_TO_100': 0}, 'validated_buy_threshold': None, 'system_actionability_gate': 'RESEARCH_ONLY_NO_GO', 'gate_reason': 'OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED'}.
| Symbol | Frozen score | Frozen classification |
|---|---:|---|
| SCYX | 72.967 | CANDIDATE |
| AKAM | 62.253 | CANDIDATE |
| WULF | 62.127 | CANDIDATE |
| FUBO | 61.624 | CANDIDATE |
| NYAX | 61.365 | CANDIDATE |
| SPGI | 61.195 | CANDIDATE |
| EPOW | 60.507 | CANDIDATE |
| CHTR | 60.480 | CANDIDATE |
| CSIQ | 60.463 | CANDIDATE |
| SFM | 60.233 | CANDIDATE |
| MESO | 60.228 | CANDIDATE |
| LE | 59.977 | CANDIDATE |
| JACK | 59.562 | CANDIDATE |
| TBLA | 59.491 | CANDIDATE |
| UPWK | 59.144 | CANDIDATE |
| ATGL | 58.917 | CANDIDATE |
| IDR | 58.813 | CANDIDATE |
| FMC | 58.430 | CANDIDATE |
| HNRG | 57.947 | CANDIDATE |
| NX | 57.906 | CANDIDATE |
| XPRO | 57.676 | CANDIDATE |
| CSPI | 57.551 | CANDIDATE |
| MBLY | 57.471 | CANDIDATE |
| CGNX | 57.050 | CANDIDATE |
| SRAD | 56.699 | CANDIDATE |

## Source failures
- THC: ValueError: LATEST_SESSION_MISSING
- AKO.B: ValueError: EMPTY_PROVIDER_RESPONSE
- GTN.A: ValueError: EMPTY_PROVIDER_RESPONSE
- EPM: ValueError: LATEST_SESSION_MISSING
- ASPN: ValueError: LATEST_SESSION_MISSING
- ONCH: ValueError: LATEST_SESSION_MISSING
- SAC: ValueError: LATEST_SESSION_MISSING
- SWX: ValueError: LATEST_SESSION_MISSING
- AKO.A: ValueError: EMPTY_PROVIDER_RESPONSE
- AXIL: ValueError: LATEST_SESSION_MISSING
- LESL: ValueError: LATEST_SESSION_MISSING
- ORA: ValueError: LATEST_SESSION_MISSING
- Q: ValueError: LATEST_SESSION_MISSING
- UCFI: ValueError: LATEST_SESSION_MISSING

Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.
