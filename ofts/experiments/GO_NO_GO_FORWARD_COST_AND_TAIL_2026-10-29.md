# OFTS forward model-separated cost and tail audit — 2026-10-29

**Research only.** No production-scoring changes, no brokerage orders, no retrospective refit. Source is immutable v2.3 scored fixed-horizon summaries saved on `ofts-daily-state` (`validation_summary.json`, blob `db? verify source blob from this report's commit metadata`), market as-of **2026-10-28**; durable audit recorded **2026-10-29T17:07:52Z**. Model hash `a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b`. This is a **fresh arithmetic diagnostic of overlapping, already-matured observations**, not a new chronological out-of-sample test and not an executable strategy.

## Reproducible arithmetic
For each horizon and model version, weight each saved score-band mean by its `observations` count. Saved `average_net_pct` already deducts assumed 0.20 percentage-point round-trip costs. Saved `average_excess_pct` is *gross* excess versus same-date SPY, so `net_excess = weighted_gross_excess - 0.20`; `matched_SPY = weighted_net + 0.20 - weighted_gross_excess`. For total assumed costs `c`, adjusted net = saved net - (c - 0.20). Do not pool different model hashes or claim observations are independent trades.

| v2.3 horizon | Mature scored observations | Net @0.20% | Matched SPY price | Net excess vs SPY | Net @0.50% | Net @1.00% | Gross-cost break-even |
|---|---:|---:|---:|---:|---:|---:|---:|
| 5 sessions | 762 | +0.443% | -0.369% | +0.812 pp | +0.143% | -0.357% | 0.643% |
| 10 sessions | 298 | +1.069% | -0.466% | +1.536 pp | +0.769% | +0.269% | 1.269% |

| v2.3 score band | N, 5 sessions | Net 5 sessions | N, 10 sessions | Net 10 sessions |
|---|---:|---:|---:|---:|
| 0–40 | 105 | -2.233% | 41 | +0.760% |
| 40–60 | 578 | +1.080% | 221 | +1.084% |
| 60–80 | 79 | -0.666% | 36 | +1.332% |

The five-session higher-scoring 60–80 band underperforms the 40–60 band by **1.746 percentage points**, so the score is not monotonic as a return-ranking signal over that horizon. The ten-session ordering reverses. No single score threshold is validated. Some worst **adverse excursions** within scored observations are below **-86%** (five sessions) and **-88%** (ten sessions); these are observation-level path extremes, **not** verified executable portfolio drawdowns.

## Separate hypothetical cycle-trade ledger (do not merge with overlapping outcomes)
Two *completed* hypothetical trades: YDES net -39.144% (9 holding sessions, earlier model), matched SPY -2.424%; MF net -23.840% (8 holding sessions, v2.3), matched SPY -0.234%. Both lost; equal-weight mean net -31.492%. This tiny trade sample neither proves a future loss rate nor supports live trading. Ledger at this snapshot: 31 open, 2 pending entries, 2 closed.

## LYEL missed-rebound case, not hindsight optimization
Frozen October 26/27/28 research scores 48.797 / 51.556 / 51.585, all NO_TRADE for `NO_NEW_CONFIRMED_TURN`. October 28 viability WATCH, cycle confidence MEDIUM, cycle-timing gate false, recent UP-leg repeatability 2 of 3. This documents a missed observed move but **does not** establish that an earlier entry was knowably profitable at decision time. Test any relaxed-confirmation rule across all contemporaneous candidates on an untouched future cohort, not LYEL alone.

## GO/NO-GO interpretation
**RESEARCH_ONLY_NO_GO**. Favorable recent overlapping v2.3 fixed-horizon averages vs SPY are **not** completed BUY-to-SELL trading performance, cannot establish live fillability, and lack matched-stock passive/alternative-entry and matched IWM benchmarks. Two completed trades are both severe losses. Previously saved 15-trade training-selected same-stock delayed-entry diagnostic favored delaying one session by 0.286 pp; it is *not* an independent holdout. Required next: frozen chronological holdout, same-stock/date/horizon comparisons, IWM, liquidity/spread/slippage, independent trades, drawdown and tail control. Preserve all frozen cohorts.
