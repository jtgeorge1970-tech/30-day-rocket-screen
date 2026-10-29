# OFTS v2.3 score-band and cost-fragility audit — October 28, 2026

Research only. No production scoring changes, no trades. This is a **new arithmetic sensitivity test** of the already saved, correlated v2.3 research observations, not a new untouched chronological holdout. Data source: `ofts-daily-state/validation_summary.json` blob `6d15fb20bf3372d5c797de8f5a156b96a0976912`, market as-of **2026-10-27**. Latest qualified daily state commit `db625dfe698bee64f2dafcdeab4081656b25367d`.

Method: select model hash `a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b`. Weight each score-band mean by its matured observation count, never merge the earlier model. Saved net returns deduct 0.20 percentage points in assumed round-trip cost. Saved `average_excess_pct` is **gross** excess versus matched SPY, so **net excess = saved gross excess - 0.20 pp**. Matched SPY mean = saved net + 0.20 - saved gross excess. For alternative total costs c, adjusted net = saved net - (c - 0.20).

| Horizon | Score band | N | Net @ 0.20% | Net @ 0.50% | Net @ 1.00% | Matched SPY | Net excess @ 0.20% |
|---|---|---:|---:|---:|---:|---:|---:|
| 5 | 0-40 | 88 | -1.667% | -1.967% | -2.467% | -0.691% | -1.176 pp |
| 5 | 40-60 | 508 | +0.644% | +0.344% | -0.156% | -0.739% | +1.183 pp |
| 5 | 60-80 | 71 | -0.798% | -1.098% | -1.598% | -0.735% | -0.263 pp |
| 5 | **All scored** | **667** | **+0.185%** | **-0.115%** | **-0.615%** | **-0.532%** | **+0.718 pp** |
| 10 | 0-40 | 27 | +0.120% | -0.180% | -0.680% | -1.230% | +1.149 pp |
| 10 | 40-60 | 150 | -0.408% | -0.708% | -1.208% | -1.281% | +0.672 pp |
| 10 | 60-80 | 24 | -0.044% | -0.344% | -0.844% | -1.273% | +1.029 pp |
| 10 | **All scored** | **201** | **-0.294%** | **-0.594%** | **-1.094%** | **-1.073%** | **+0.779 pp** |

The five-session 40-60 band looks strongest in this retrospective subset, but the same band loses money over ten sessions. The higher 60-80 band loses at five sessions. Therefore score ranking is not monotonically predictive, and cherry-picking 40-60 after viewing results would introduce selection bias. At 0.50% assumed total costs, the **entire** five-session v2.3 scored sample becomes negative in absolute return; at 1.00%, both five- and ten-session samples are negative and the ten-session sample slightly trails SPY (net excess approximately -0.021 pp). This does not measure actual fill costs.

Execution integrity remains unresolved: sampled Oct 28 09:35 bid/ask spreads averaged 2.097% across six new BUYs, and earlier matched-price audit found 5/15 entry and 5/15 exit discrepancies above 0.5% versus historical ledger. Quotes are not fills. Same-stock passive and matched IWM benchmarks are incomplete. Only one trade is officially closed in the latest durable ledger; MF's October 28 SELL exit is provisional. No 20/30/60-session outcomes have matured.

Operational note: the latest accessible daily workflow run `40729515105` finished at 2026-10-28T16:53Z, before the October 28 NYSE close, and reloaded October 27 saved state without downloading new market data. As of this audit no qualified October 28 cohort was verified. Do not backdate or overwrite frozen predictions. A post-close run is needed to record the new session.

**Decision: RESEARCH_ONLY_NO_GO.** Further GO consideration requires chronological unseen samples, executable entry/exit cost verification, same-stock matched controls and risk limits. Sources: [saved summary](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/blob/ofts-daily-state/validation_summary.json), [audit](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/blob/ofts-daily-state/AUDIT_REPORT.md), [daily run](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/actions/runs/40729515105), [Oct 28 quote diagnostic](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/blob/ofts-go-no-go-20261025/ofts/experiments/GO_NO_GO_NEXT_OPEN_EXECUTION_2026-10-28.md).
