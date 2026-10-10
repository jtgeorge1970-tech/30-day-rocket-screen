# OFTS — recent swing viability / fool's gold audit

**Research run date:** 2026-10-10. **Source:** original restored full-universe historical cache; no assertion of live price freshness. [Verified full-universe workflow](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/actions/runs/38046875287).

## Screening counts

- Population **5502**; numerical v2.3 research scores **3977**.
- Experimental last-three swing / last-two rising swing filter: **1922** REVIEW, **2055** provisional NO_TRADE.
- Combined research shortlist after original candidate status + v0.1 swing stability + v0.2 recent viability: **447** REVIEW. This is **not** 447 production BUY signals.
- FADING: **144**
- FOOLS_GOLD: **10**
- INSUFFICIENT: **143**
- STALE_SWINGS: **22**
- TOO_SMALL: **1350**
- TOO_SMALL_UPSIDE: **386**

## What changed in top original research-quality rankings

| Original rank | Symbol | Quality score | Swing health v0.1 | Recent viability v0.2 | Combined research entry |
|---:|---|---:|---|---|---|
| 1 | SCYX | 67.197 | STABLE_RANGE | REVIEW | REVIEW |
| 2 | HNRG | 65.889 | DOWNTREND | REVIEW | REVIEW |
| 3 | MIR | 64.881 | IRREGULAR | REVIEW | NO_TRADE |
| 4 | BHC | 64.346 | STABLE_RANGE | REVIEW | REVIEW |
| 5 | CHTR | 63.990 | IRREGULAR | REVIEW | NO_TRADE |
| 6 | GAME | 63.828 | STABLE_UPTREND | REVIEW | REVIEW |
| 7 | RNGR | 63.737 | STABLE_RANGE | REVIEW | NO_TRADE |
| 8 | NEWT | 63.718 | STABLE_RANGE | TOO_SMALL_UPSIDE | NO_TRADE |
| 9 | BBY | 63.652 | STABLE_RANGE | TOO_SMALL | NO_TRADE |
| 10 | SRI | 63.511 | IRREGULAR | REVIEW | NO_TRADE |
| 11 | NVDA | 63.495 | STABLE_UPTREND | REVIEW | NO_TRADE |
| 12 | FUBO | 63.276 | IRREGULAR | REVIEW | NO_TRADE |
| 13 | OLLI | 62.883 | IRREGULAR | REVIEW | NO_TRADE |
| 14 | S | 62.768 | STABLE_RANGE | REVIEW | REVIEW |
| 15 | MGY | 62.730 | STABLE_UPTREND | TOO_SMALL | NO_TRADE |
| 16 | COKE | 62.527 | IRREGULAR | TOO_SMALL | NO_TRADE |
| 17 | EPOW | 62.527 | IRREGULAR | REVIEW | NO_TRADE |
| 18 | WULF | 62.362 | DOWNTREND | REVIEW | REVIEW |
| 19 | IMKTA | 62.140 | IRREGULAR | TOO_SMALL | NO_TRADE |
| 20 | LND | 62.011 | STABLE_RANGE | REVIEW | NO_TRADE |
| 21 | HLIT | 61.809 | STABLE_RANGE | TOO_SMALL_UPSIDE | NO_TRADE |
| 22 | JACK | 61.780 | STABLE_RANGE | REVIEW | REVIEW |
| 23 | ANET | 61.747 | STABLE_RANGE | TOO_SMALL_UPSIDE | NO_TRADE |
| 24 | SCCO | 61.692 | STABLE_UPTREND | REVIEW | REVIEW |
| 25 | TGS | 61.692 | DOWNTREND | REVIEW | REVIEW |

## Top 25 after recent economic-swing and original candidate filters (research REVIEW only)

| Shortlist rank | Symbol | Original quality score | Last 3 completed legs median % | Last 2 UP legs median % |
|---:|---|---:|---:|---:|
| 1 | SCYX | 67.197 | 18.25 | 20.29 |
| 2 | HNRG | 65.889 | 9.79 | 7.82 |
| 3 | BHC | 64.346 | 8.41 | 6.46 |
| 4 | GAME | 63.828 | 21.92 | 22.22 |
| 5 | S | 62.768 | 7.06 | 13.95 |
| 6 | WULF | 62.362 | 15.19 | 12.55 |
| 7 | JACK | 61.780 | 6.46 | 5.68 |
| 8 | SCCO | 61.692 | 9.45 | 7.36 |
| 9 | TGS | 61.692 | 8.38 | 7.45 |
| 10 | IBKR | 61.371 | 7.46 | 6.75 |
| 11 | GEMI | 61.297 | 13.10 | 26.43 |
| 12 | GPGI | 61.224 | 7.86 | 7.28 |
| 13 | CSIQ | 60.904 | 11.47 | 8.14 |
| 14 | TLS | 60.623 | 8.61 | 9.27 |
| 15 | XPRO | 60.623 | 6.34 | 5.73 |
| 16 | FLR | 60.594 | 7.84 | 7.95 |
| 17 | TXN | 60.539 | 6.06 | 10.60 |
| 18 | DTIL | 60.451 | 26.55 | 19.53 |
| 19 | FWRG | 60.252 | 11.16 | 7.35 |
| 20 | ATGL | 59.850 | 18.05 | 18.37 |
| 21 | FIX | 59.629 | 6.91 | 10.89 |
| 22 | MNDY | 59.613 | 19.80 | 19.93 |
| 23 | CLW | 59.538 | 11.27 | 8.19 |
| 24 | VST | 59.490 | 9.08 | 8.60 |
| 25 | GSM | 59.469 | 7.66 | 12.45 |

## Interpretation / verification limits

- The old historical average is explicitly compared to the median of the latest three completed **minor** swings and the last two completed **UP** swings. Large DOWN swings are not counted as buyable upside.
- Micro-pivots (2.5%–3.5%) are detected separately because the old 6%–16% major threshold concealed tiny bounces. Both older and recent legs use the same micro threshold for fair comparison.
- Experimental capture assumption: 50% of the median of the last two UP legs, less 0.20% round trip, requiring at least 2.50% hypothetical net opportunity. These are not realized returns or calibrated win probabilities.
- The combined REVIEW list still includes downtrend risk names requiring separate analysis; **REVIEW is not BUY**.
- This run establishes screening behavior, NOT that the new gate improves profits. Audit rejected winners, avoided losers, transaction costs, forward 5/10/20/30/60-session outcomes, SPY and sensitivity before promoting.
- Preserve all 3,977 research rows, not just the 447 shortlisted, for prospective outcome auditing.

