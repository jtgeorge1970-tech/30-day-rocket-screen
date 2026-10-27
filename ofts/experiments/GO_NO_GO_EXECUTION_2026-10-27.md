# OFTS execution feasibility audit — 2026-10-27 (research only)

**Finding: the fixed 0.20% round-trip cost assumption is not validated by observed opening-market quotes, particularly for DNTH and YDES. No brokerage trades were placed.**

## Independent market-data check
Retrieved on 2026-10-27 after the NYSE close from connected Alpaca historical **SIP** stock bars and level-1 bid/ask quotes. Source signal: immutable `signals/2026-10-26.json` on `ofts-daily-state`. The three frozen BUY signals are AKAM score 60.651, DNTH score 41.898, NET score 47.328. These were rejected by a separate unvalidated experimental viability filter. These are research signals, not production entries.

Full-session October 27 SIP open/close bars and *first observed 09:35 ET SIP quote*:

| Symbol | SIP open | SIP close | Open-to-close (not OFTS 5d result) | First 09:35 bid / ask | Ask premium over open | Median sampled 09:35+ quoted spread |
|---|---:|---:|---:|---|---:|---:|
| AKAM | $98.10 | $99.59 | +1.519% | $99.03 / $99.23 | +1.152% | 0.263% |
| DNTH | $79.55 | $79.52 | -0.038% | $77.51 / $80.28 | +0.918% | **2.510%** |
| NET | $331.95 | $327.80 | -1.250% | $332.00 / $333.87 | +0.578% | **0.539%** |

YDES, which lost 39.144% in its first completed hypothetical trade and then reentered on October 26, had only **47,166 SIP shares traded on October 27**. Its 09:35-09:40 SIP quote sample (12 observations) had median quoted spread **9.302%**; first quote was at 09:37:15 ET, $4.92 bid / $5.10 ask. This is a strong liquidity warning, not an executable fill guarantee.

SPY October 27 SIP open $767.34, close $769.66 (**+0.302%**); IWM open $277.96, close $280.18 (**+0.799%**). These are same-day reference returns, **not** matched five-session benchmark returns.


### One-day entry-price sensitivity (illustration only)

If all three October 26 research BUYs were marked at the October 27 close (rather than waiting for a SELL), then applying a flat 0.20 percentage-point cost gives an **equal-weight average -0.123%** using the SIP daily opening price, versus **-1.001%** using the first observed 09:35 ask for each symbol. By symbol, open-price vs 09:35-ask marks are AKAM +1.319% vs +0.163%, DNTH -0.238% vs -1.147%, NET -1.450% vs -2.018%. The 0.878 percentage-point difference is **not a pure slippage estimate**: it includes five minutes of price movement, an observed quote instead of a fill, and a closing-price mark rather than a sell-side executable quote. It demonstrates entry-timing sensitivity only; the OFTS strategy did not exit these positions at the close, and the experiment is not a completed trade or portfolio backtest.


### Closing-market spread check

Independently sampled 15:55-16:00 ET SIP quotes on October 27. Median sampled quoted spreads: AKAM **0.081%** (first 300 events), DNTH **0.176%** (first 300), NET **0.103%** (first 300), YDES **1.832%** (all 27 returned quotes). YDES's last 15:59:59 ET quote was **$5.95 bid (200 shares) / $6.05 ask (100 shares)** versus its official $6.04 daily close. The open YDES position in the saved ledger entered October 26 at **$4.96** (verified against the independent SIP open, $4.96). Marking that position at the October 27 close gives **+21.774% gross unrealized**, but using the last observed $5.95 bid instead gives **+19.960% gross** before commissions and market impact, for at most the displayed 200 shares. Neither is a realized trade, and no SELL signal is claimed. This shows why closing-price marks and executable exit prices must be distinguished.

## Method and limitations
The first 09:35 ask is a **quote**, not an executed trade. It is five minutes after the opening auction; the difference from the daily opening trade reflects both price movement and execution conditions, so it must not be labeled pure slippage. A market-on-open order submitted before 09:30 might receive the official opening-auction price, subject to broker/order constraints; the research ledger assumes that fill but has not demonstrated it. Quoted spread measures ask-minus-bid relative to midpoint, not actual round-trip realized trading cost. Quote medians were computed over returned 09:35-09:40 samples, capped at 300 quotes per symbol (AKAM 300, DNTH 64, NET 300, YDES 12); for high-activity names the cap covers only the earliest part of the window. Quote conditions and depth vary. No portfolio orders, order-book depth beyond level 1, fill simulator, or complete market-impact model were available. Daily open/close returns are not completed OFTS trades or predictive validation.


### Cross-provider opening-price audit after the qualified October 27 run

The recovered October 27 OFTS ledger now contains hypothetical entries at AKAM **$98.269997**, DNTH **$79.550003**, NET **$331.950012**. Independent Alpaca SIP official daily opens were AKAM **$98.10**, DNTH **$79.55**, NET **$331.95**. DNTH and NET agree to displayed precision, but AKAM differs by **+0.1733%** (OFTS ledger relative to SIP). This discrepancy alone is comparable to the model's entire 0.20% assumed round-trip cost. No cause has been verified: provider session-opening conventions, corporate-action adjustment, data errors, or differing eligible trade prints remain possibilities. Do not silently substitute one provider for the other or call either an executable fill. YDES's October 26 ledger entry of $4.96 matches the independent October 26 SIP open of $4.96.

The six new October 27 BUY signals are **pending next-open entries for October 28**, not October 27 fills. The October 27 three fills above belong to BUYs signaled October 26. This separation is essential to avoid look-ahead bias.

## Decision
**NO-GO remains.** The observed SIP quotes show the research assumption of universal 0.20% round-trip cost is unsafe without symbol-specific fill/slippage controls. Before GO: prespecify MOO vs delayed entry, minimum dollar volume and maximum spread, model fills conservatively using actual SIP quotes and trade prints, verify matched same-stock and SPY/IWM horizon controls, and test unseen signals without selecting thresholds based on these results. Preserve immutable daily state; do not change production scoring.

Captured source sample: `ofts/experiments/ofts_execution_quotes_2026-10-27.csv`.
