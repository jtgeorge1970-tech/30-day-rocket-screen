# OFTS v0.4 — quantified recent peak/trough timing audit

**Verified:** [full-universe CI run 38047336873](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/actions/runs/38047336873) on 2026-10-10. Restored historical OHLC cache, **not live quotes**. 22 tests passed in prior equivalent run 38047328236; current run 38047336873 passed all stages.

- Universe: **5,502**; numeric research scores: **3,977**; research-only shortlist after candidate, stability, three rising swings >=5%, economic, and recent cycle timing gates: **16**. Previous no-timing research shortlist **237**; difference **221**, but **842** scored names have primary `CYCLE_TIMING` state across the whole scored population.
- v0.4 rule: at least 4 confirmed peaks and 4 confirmed troughs; last 3 **peak-to-peak** and last 3 **trough-to-trough** intervals each have median **10–40 trading sessions**, all individual intervals **8–45**, relative median absolute deviation <=0.35. Both pass.
- The original historical quality scores are **unchanged**. This filter is **not predictive validation**, a BUY trigger or a 100-point score.

## Complete experimental REVIEW shortlist (not BUY)

| Rank | Symbol | v2.3 score | Last 3 UP swings % | Last 3 peak gaps (sessions) | Last 3 trough gaps (sessions) | Classification |
|---:|---|---:|---|---|---|---|
| 1 | XPRO | 60.623 | 29.6 / 5.1 / 6.3 | 24 / 10 / 22 | 17 / 20 / 24 | REVIEW |
| 2 | CLW | 59.538 | 5.5 / 11.3 / 5.1 | 12 / 19 / 9 | 11 / 17 / 14 | REVIEW |
| 3 | CSPI | 58.550 | 7.3 / 11.7 / 5.4 | 23 / 13 / 26 | 15 / 20 / 25 | REVIEW |
| 4 | EVI | 53.994 | 8.9 / 17.2 / 56.0 | 9 / 12 / 29 | 11 / 8 / 21 | REVIEW |
| 5 | PAHC | 53.529 | 12.4 / 7.5 / 13.1 | 12 / 14 / 8 | 17 / 8 / 22 | REVIEW |
| 6 | HRI | 52.777 | 6.2 / 6.5 / 10.9 | 16 / 10 / 8 | 25 / 11 / 8 | REVIEW |
| 7 | PATH | 52.001 | 63.5 / 19.8 / 8.0 | 18 / 12 / 9 | 18 / 15 / 13 | REVIEW |
| 8 | BXC | 51.316 | 9.4 / 11.2 / 5.2 | 12 / 11 / 10 | 10 / 12 / 8 | REVIEW |
| 9 | VSAT | 50.288 | 17.3 / 8.2 / 7.7 | 18 / 8 / 12 | 17 / 9 / 10 | REVIEW |
| 10 | ATEX | 49.185 | 11.0 / 12.2 / 9.1 | 17 / 17 / 9 | 16 / 17 / 11 | REVIEW |
| 11 | AVIR | 47.892 | 11.4 / 9.0 / 9.5 | 8 / 12 / 11 | 9 / 15 / 11 | REVIEW |
| 12 | HYLN | 47.876 | 27.0 / 17.9 / 14.4 | 17 / 10 / 8 | 11 / 14 / 10 | REVIEW |
| 13 | INTS | 46.930 | 5.9 / 23.6 / 7.9 | 10 / 11 / 17 | 11 / 21 / 12 | REVIEW |
| 14 | CAT | 46.299 | 5.3 / 5.6 / 10.3 | 9 / 15 / 20 | 8 / 16 / 10 | REVIEW |
| 15 | WRD | 45.611 | 12.8 / 7.4 / 7.6 | 8 / 11 / 10 | 13 / 14 / 12 | REVIEW |
| 16 | CTOS | 42.774 | 6.4 / 9.3 / 9.3 | 18 / 10 / 10 | 17 / 8 / 12 | REVIEW |

## Primary recent-viability classification counts, all 3,977 scored

- CYCLE_TIMING: **842**
- FADING: **106**
- FOOLS_GOLD: **10**
- INSUFFICIENT: **143**
- REVIEW: **106**
- STALE_SWINGS: **22**
- STALE_UPSIDE: **28**
- TOO_SMALL: **278**
- TOO_SMALL_UPSIDE: **1825**
- WATCH: **617**

## Next validation

- Compare 10–20, 10–30, 10–40, 10–50 session cycle bands and 5/6/7/8% minimum upward swing amplitudes on chronologically embargoed holdouts.
- Track avoided losing trades and rejected winners, realistic next-session entry, slippage, drawdown, SPY excess return and 5/10/20/30/60-session outcomes.
- Confirm corporate identity boundaries and fresh market data before treating these historical patterns as actionable.
- Do not overwrite previous frozen cohorts or present any REVIEW as BUY.
