# OFTS October 30 post-close recovery and matched trade reconciliation

**Research-only, not live-trading approved.** Verified after the Friday October 30, 2026 NYSE close. No brokerage orders, no scoring changes, no rewrite of frozen cohorts.

## Recovered operational session
- Authorized rerun of existing GitHub Actions job 123785089671 on workflow run **40729515105**, yielding new job **124357276772**, completed successfully at ~23:05 UTC October 30.
- New immutable October 30 frozen signal/prediction cohort: selected 135, fresh 121 (**89.63%**), required stale 0, broader provider refresh errors 83, gate PASS; **16** qualified cohorts, **2,073** prediction rows.
- Signals: **TARS BUY 57.906385 MEDIUM**, **NIPG BUY 45.061939 LOW**, **MH SELL 59.717708 MEDIUM**, other **160 NO_TRADE**. Pending TARS/NIPG hypothetical entries and MH exit at next NYSE open **November 2**.
- Audit saved at 2026-10-30T23:05:22Z, recomputation matches, 119 attempts, outcome statuses MATURE 1995, PENDING 7346, INELIGIBLE_DATA 1010, CORPORATE_ACTION_REVIEW 9, MISSING_SESSIONS 5. Frozen older files retained; previous October 29 signal blob SHA 99b2d299f202acedcf5f12dcabf8c3cf87d3f8dd unchanged.
- Permanent state commit: **5da508edddbd6a73df5f9c8b14142e9c810054b5**. GitHub artifact **13019205927**.
- Independent chart audit last directly verified: October 28 target, 50/50 fresh, zero errors, workflow **40862981168**. Do not conflate it with October 30 daily cohort.

## Mature fixed-horizon outcomes, model-separated
The v2.3 model hash is a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b. From the newly saved `validation_summary.json`, weighted by observation count; hypothetical next-open and **0.20 percentage points** cost. SPY is matched price-only. `average_excess_pct` in the summary is gross excess, so subtract 0.20 pp for net excess.

| Model | Horizon | Mature N | OFTS mean net | Matched SPY mean | OFTS net excess |
|---|---:|---:|---:|---:|---:|
| v2.3 | 5 | 947 | +0.613% | -0.247% | +0.860 pp |
| v2.3 | 10 | 490 | +2.243% | -0.682% | +2.925 pp |
| Earlier | 5 | 97 | -3.753% | -1.994% | -1.759 pp |
| Earlier | 10 | 97 | -2.935% | -2.415% | -0.519 pp |

These are **overlapping scored candidate/control observations**, not independent executed trades or a portfolio P&L. Full saved outcomes across models and controls: 5-session 1286 matured, 10-session 709 matured, 20/30/60-session zero matured. V2.3 five-session score band 40–60 mean +1.166% (N=731), 60–80 mean -0.238% (N=94), so higher score is not monotonic. At 1.00% total round-trip costs (additional 0.80 pp), v2.3 five-session mean becomes -0.187%; the ten-session mean becomes +1.443% but still not fill-validated. IWM matched-horizon research-wide comparison remains incomplete.

## Officially completed hypothetical trades
| Symbol | Entry date / price | Exit date / price | Net with assumed costs | Matched SPY price return |
|---|---|---|---:|---:|
| YDES | Oct12 / $7.01 | Oct23 / $4.28 | -39.144% | -2.424% |
| MF | Oct16 / $10.66 | Oct28 / $8.14 | -23.840% | -0.234% |
| CCS | Oct23 / $56.63 | **Oct30 / $54.27** | **-4.367%** | +0.195% |

All **3/3 completed trades lost**; equal-weight net average approximately **-22.451%**. The new CCS official close independently agrees with Alpaca SIP Oct30 opening bar. CCS matched Oct23-to-Oct30 IWM open-to-open return was **+2.591%**, so CCS underperformed IWM by approximately **6.958 pp** net. CCS underperformed matched SPY by approximately **4.562 pp** net. No dividends/ETF transaction costs included. The three trades do not establish population win rate.

## New independent execution and stop diagnostics
See `GO_NO_GO_OPEN_EXECUTION_AND_CCS_STOP_2026-10-30.md` and `GO_NO_GO_FIXED_STOP_SIP_2026-10-30.md` in this folder. MIRM Oct30 first sampled 09:30 quote $83.01/$87.29, a **5.03%** quoted spread, versus SIP open $85.21. CCS Oct30 first 09:30 quote $52.77/$55.60, compared with recorded hypothetical exit at SIP open $54.27. Quotes do not prove auction fills or execution costs.

A three-loser-selected, gap-aware daily-OHLC fixed-stop test produced 5% stop net returns YDES -5.20%, MF -5.20%, CCS -7.03% versus baselines -39.14%, -23.84%, -4.37%. This is **severely biased, post-hoc, and not GO evidence**; tight stops can gap through thresholds, and still-open winners/losers are excluded.

## Verdict
**RESEARCH_ONLY_NO_GO**. The latest fixed-horizon scored averages versus SPY improved, but full same-stock passive/alternative-entry chronological controls, matched IWM universe-wide benchmarks, achievable bid/ask fills, survivorship, portfolio drawdowns, outlier sensitivity, and adequate independent completed trades remain unverified. Do not claim profitability or alter production scoring.