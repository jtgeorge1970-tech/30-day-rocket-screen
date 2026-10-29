# OFTS October 29, 2026 post-close validation — model-separated forward arithmetic and LYEL signal audit

**Research only. NO-GO for real-money trading.** Source state commit `db85bcc4d941063fbbdf77f264ceda7feb81cd15`, market as-of **2026-10-29**, successful recovery workflow **40729515105 attempt 3**, immutable v2.3 validation source blob `f7e09945c40db22d67a40d5577e4b0f08bbc0ef6`, model hash `a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b`. No scoring changes or trades.

## Reproducible model-separated arithmetic
Weight score-band means by matured observations, separately for each model and horizon. Saved `average_net_pct` deducts assumed 0.20 percentage points round-trip. Saved `average_excess_pct` is gross versus matched SPY: net excess = weighted gross excess - 0.20; matched SPY = weighted net - net excess. Cost sensitivity: adjusted net = saved net - (new cost - 0.20).

| Horizon | v2.3 matured scored N | OFTS net at 0.20% | Matched SPY price | Net excess vs SPY | OFTS net at 0.50% | OFTS net at 1.00% |
|---|---:|---:|---:|---:|---:|---:|
| 5 sessions | 857 | +0.604% | -0.190% | +0.795 pp | +0.304% | -0.196% |
| 10 sessions | 391 | +1.845% | -0.475% | +2.320 pp | +1.545% | +1.045% |

| v2.3 score band | N five | Five-session net | N ten | Ten-session net |
|---|---:|---:|---:|---:|
| 0–40 | 114 | -2.185% | 52 | -0.154% |
| 40–60 | 657 | +1.197% | 292 | +2.213% |
| 60–80 | 86 | -0.223% | 47 | +1.771% |

Five-session 40–60 band exceeds 60–80 by **1.420 pp**. Ten-session 40–60 also exceeds 60–80 by **0.442 pp**. These are **overlapping fixed-horizon candidate/control observations**, not independent completed BUY-to-SELL trades or a portfolio; outlier dependence and true maximum drawdown are not established. All-model maturity counts: five **1,171**, ten **593**, 20/30/60 **zero**. No full same-stock passive control or matched IWM test.

## Signal and frozen cohort
Latest frozen Oct29 162 monitored: **1 BUY (MIRM 32.220, LOW confidence), 3 SELL (CRNC 62.004, CCS 54.905, VNCE 40.819), 158 NO_TRADE**. BUY entry planned next session, not filled as of Oct29 close. 136 selected; 118 fresh, gate PASS, zero required stale, 73 broader provider errors; 15 qualified cohorts, 1,938 frozen rows. Latest October 28 qualified snapshot remains unchanged at Git blob `d573e2fbb5e9b89c72e5a98df4efd641ed5d9f68`. The separate independent chart audit is still market as-of Oct28, 50/50 fresh, zero errors.

## Critical LYEL correction
LYEL **did receive a BUY on October 19** (score 44.513, LOW cycle confidence), and durable hypothetical ledger recorded **next-session open $8.74 on October 20**. October 28 actual close **$10.93**, hence **+25.057% gross unrealized price mark**, or illustrative **+24.857% after the assumed 0.20% round-trip cost**, not realized or fill-verified. Subsequent NO_TRADE states only meant no *new* BUY. Earlier user-facing reports saying LYEL was missed were incorrect because they ignored the existing position. This is a reporting/alerting failure; the model did identify a potentially valuable entry, but user was not informed. Do not refit to this single winner.

## Hypothetical completed trades and GO/NO-GO
Two closed hypothetical trades: YDES -39.144% net vs SPY -2.424%; MF -23.840% net vs SPY -0.234%. Both negative, equal-weight net -31.492%; 33 other open positions, one pending entry. The completed trade sample is tiny and unrepresentative. A previous retrospective matched-stock delayed-entry comparison (15 trades) did not favor immediate OFTS entry (0.286 pp worse); it was training-selected, not holdout. Realistic liquidity/spreads, slippage, risk stops, independent trade sample, chronological untouched holdout, same-stock alternative entry/passive and IWM benchmarks remain unresolved.

**Verdict RESEARCH_ONLY_NO_GO.** Favorable recent overlapping forward means versus SPY are research progress, not proof of executable profitability. No production changes or brokerage orders.
