# OFTS GO/NO-GO: same-stock entry-delay and price-source robustness — 2026-10-27

**Decision: RESEARCH_ONLY_NO_GO.** This is a newly computed **exploratory matched-stock alternative-entry comparison**, not an untouched prospective holdout, a same-stock passive benchmark, or a profitable portfolio simulation. No brokerage trades. No change to production scoring or the permanent `ofts-daily-state` branch.

## Sources and scope
- Existing historical simulated BUY-to-SELL trades: `ofts/validation/cycle_execution_trades.csv` (24 trades, six training-selected symbols).
- Frozen historical OHLCV files: `ofts/research/historical_control_bars_2025-10_to_2026-09.csv` and `ofts/research/historical_controls_206bars_asof_2026-10-02.csv`.
- 1,020 overlapping bar rows between the two source files had **zero opening-price discrepancies greater than 0.1%**.
- Only **15 of 24** original trades (four symbols: AEHR 7, AXTI 5, PLTR 2, ROCK 1) had entry date, next session, and exit date in these saved bars. **Nine trades are excluded for missing coverage**, not assigned zero returns. This is a nonrandom subset.
- Exact same stock and same original exit date for each pair. Baseline buys at the original recorded next-open entry date; control delays purchase by one additional completed trading session. Both exit at the original frozen SELL exit date's open. Both assume 0.20 percentage points round-trip costs; same-source OHLCV prices used for both legs to prevent source-mixing. Delayed control is actionable after the original signal but may omit an adverse first session; it is not a no-signal passive buy-and-hold comparison.
- Each trade is given equal weight; no compounding, capital overlap, dividends, spreads, fill guarantees, portfolio drawdown or borrow constraints. The six original symbols were training-selected and the delay experiment was chosen after viewing historical results. Therefore this is **not an independent out-of-sample GO test**.

## Paired results (15 trades)
| Metric | Original next-open entry | One-session-delayed entry |
|---|---:|---:|
| Average net return | **+4.623%** | **+4.909%** |
| Winning trades | 8/15 | 7/15 |
| Worst net trade | **−66.221%** | **−63.888%** |

The original entry timing underperformed the one-session-delay control by **0.286 percentage points on average**; the median paired baseline-minus-delay difference was **−1.874 percentage points**. Original entry beat the delay in **5/15** pairs. Neither variant solves the tail-loss problem.

By stock (baseline vs delayed average): AEHR −2.709% vs −2.455% (7 pairs); AXTI +20.122% vs +21.820% (5); PLTR −6.854% vs −8.852% (2); ROCK +1.409% vs −0.569% (1). Results are concentrated in AXTI, so the aggregate average cannot establish an edge.

## New data-integrity concern
When the same saved OHLCV bar opens were compared with the original historical trade ledger opens, **5/15 entries and 5/15 exits differed by more than 0.5%**. Mean absolute entry discrepancy was **0.428 percentage points**. Examples: AEHR Jan 6 +1.275% entry discrepancy, AEHR Feb 10 −1.270% entry discrepancy, AEHR Mar 23 exit −3.034%. Causes not established (provider, adjustments, auction conventions or replay data lineage). The 0.20% total trading-cost assumption is smaller than several observed price-source discrepancies. **Do not call the historical returns fill-validated.**

## Interpretation and next validation
- The first actual same-stock alternative-entry diagnostic **does not demonstrate an advantage for immediate OFTS entry**. A one-session delay had slightly higher mean net return in the 15 available historical pairs, despite a slightly lower win count. This is descriptive and post-hoc, not a forecast.
- The earlier October 27 SIP quote audit separately found large opening spreads for some prospective names, especially YDES and DNTH; do not extrapolate 0.20% cost to all symbols.
- Required before GO: independent matched same-stock passive baseline and IWM/SPY on identical dates; prespecified chronological untouched test with more independent completed trades; reconciled cross-provider open/exit prices; actual fill/slippage and minimum-liquidity gates; stop/cooldown loss containment. Longer 20/30/60-session prospective horizons remain immature.
- Keep this research branch isolated. Do not change frozen cohorts or production logic.

Reproduce: `python ofts/experiments/matched_stock_delay_20261027.py`.
