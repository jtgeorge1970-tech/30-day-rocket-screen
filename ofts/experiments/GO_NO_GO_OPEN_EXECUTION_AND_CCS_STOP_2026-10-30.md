# OFTS execution and stop-loss sensitivity — 2026-10-30

**Status: RESEARCH_ONLY_NO_GO.** Independent, point-in-time-referenced diagnostic for the October 29 frozen BUY/SELL events. Not a complete strategy backtest, not an executable fill, not an untouched multi-trade holdout. No production scoring or frozen-cohort changes; no orders.

## Source and event provenance
- Frozen October 29 BUY MIRM score 32.219545, LOW confidence, intended next-session open October 30.
- Frozen October 29 SELL CCS score 54.905424, MEDIUM confidence; ledger shows entry signal October 22, entry October 23 at $56.630001, intended next-session exit October 30.
- `ofts-daily-state/signals/2026-10-29.json` and `cycle_ledger.json` (state inspected October 30).
- Independent Alpaca **SIP** daily OHLCV bars October 22–30 and consolidated Level-1 quotes October 30 09:30–09:35 America/New_York, queried October 30 after close. SIP quotes are indicative and do **not** prove fills, size beyond displayed depth, or auction participation.
- Matched benchmark daily opening bars: SPY Oct23 $759.896, Oct30 $761.38; IWM Oct23 $274.85, Oct30 $281.97. Same opening-date endpoints as CCS, **price-only**, no dividends.
- Hypothetical baseline cost: subtract 0.20 percentage points from stock round-trip return, not a verified execution-cost model.

## New MIRM BUY entry executability
| Measure | Value |
|---|---:|
| Oct30 daily SIP open | $85.21 |
| Oct30 close | $85.00 |
| Opening 09:30:00.882 bid / ask | $83.01 / $87.29 (100 ask shares displayed) |
| Opening sampled spread / midpoint | **5.026%** |
| First 09:35:00.019 bid / ask | $86.04 / $88.25 (100 ask shares displayed) |
| 09:35 sampled spread / midpoint | **2.536%** |
| First ask vs daily open | **+2.441%** |
| 09:35 ask vs daily open | **+3.568%** |
| Open-to-close, minus 0.20pp | **−0.446%** |
| 09:35 ask-to-close, minus 0.20pp | **−3.883%** |
| Same-day SPY open-to-close, price-only | −0.743% |
| Same-day IWM open-to-close, price-only | −0.936% |

The 09:35 ask is a **different entry time** from the opening auction, so this is a diagnostic, not a controlled equal-horizon matched-stock performance claim. The opening price itself is not guaranteed to be achievable. An ask quote for 100 shares does not establish liquidity for a larger order.

## New CCS SELL exit and stop sensitivity
| Measure | Value |
|---|---:|
| Oct23 recorded entry open (SIP corroborated) | $56.63 |
| Oct30 SIP open (planned exit) | $54.27 |
| Oct30 first 09:30:00.995 bid / ask | $52.77 / $55.60 (100 shares each displayed) |
| 09:30:01.427 bid / ask | $53.60 / $54.75 |
| Oct30 close | $52.59 |
| Hypothetical entry to exit at daily open, minus 0.20pp | **−4.367%** |
| Entry to first observed bid, minus 0.20pp | **−7.016%** |
| Entry to 09:30:01.427 bid, minus 0.20pp | **−5.551%** |
| Matched Oct23-to-Oct30 SPY open-to-open | +0.195% |
| Matched Oct23-to-Oct30 IWM open-to-open | +2.591% |
| CCS underperformance vs SPY, using hypothetical open exit | **−4.563 percentage points** |
| CCS underperformance vs IWM, using hypothetical open exit | **−6.958 percentage points** |
| Holding from Oct30 open to close (same stock) | −3.096% |

### Predeclared-style simple stops, sensitivity only (retrospective)
- Entry Oct23 $56.63; 5% stop trigger $53.7985. On Oct29 the stock **gapped below** this trigger (open $52.76); an optimistic immediate opening sale at $52.76 yields **−7.034% net**, worse than the planned Oct30 open exit. Actual stop-market fill is not guaranteed.
- 10% stop trigger $50.967. Oct29 low was $50.45, so it was touched. A hypothetical fill at exactly the stop trigger yields **−10.20% net**, also worse. Intraday order sequencing and fill are not established by daily bars.
- This single case does not demonstrate that stops are generally harmful or beneficial; it shows gap and execution assumptions can reverse an apparent protection benefit.

## Interpretation and limitations
1. MIRM and CCS demonstrate material opening-market quote spreads relative to the 0.20% round-trip cost assumption. Bid/ask spreads are **not** realized trading costs and quote timestamps differ from auction execution.
2. CCS is a third potential completed hypothetical trade only after the durable ledger confirms its exit. Do not count it as closed before persistence.
3. The CCS same-stock hold-to-close comparison is one session, **not** a matched five-/ten-session BUY-entry benchmark. The MIRM next-session outcomes have not matured.
4. SPY/IWM comparisons here are matched **dates and open-to-open horizon** for CCS, but not matched fees, dividends or trading frictions.
5. No survivorship-adjusted universe-wide holdout, portfolio drawdown or sufficient independent trades yet. Do not infer GO.

**Verdict: RESEARCH_ONLY_NO_GO.** Continue untouched chronological cohort evaluation and actual bid/ask/liquidity verification.