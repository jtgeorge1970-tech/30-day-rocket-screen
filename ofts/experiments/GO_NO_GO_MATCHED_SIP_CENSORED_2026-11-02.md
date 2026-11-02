# OFTS matched-stock / benchmark / stop diagnostic — 2026-11-02

**Source cutoff:** permanent `ofts-daily-state` commit `eb05038a4e793e5ecb844b8fcd321e3ccb8e9db9`, qualified NYSE session **2026-10-30**. Independent **Alpaca SIP 1Day OHLCV**, requested 2026-11-02 for 2026-10-09 through 2026-10-30, saved as a 592-bar CSV (37 symbols, including SPY and IWM). The latest November 2 session is **not** included in this test. Read-only research; no production changes or orders.

## Predefined comparison

Take every executed entry in the frozen `cycle_ledger.json`: **33 still-open positions + 3 completed trades = 36**. Exclude two pending entries with no October 30 fill. For the three completed trades, use the saved actual hypothetical next-open entry and exit dates and prices. For the 33 still-open positions, mark at the **October 30 closing price** (not a completed trade). Deduct **0.20 percentage points** for OFTS and same-stock delayed-entry returns; compare SPY and IWM price-only on the *identical entry and exit/censor dates* using their opening prices and, for open positions, the October 30 close. Delayed same-stock control buys the following session's open but exits at the **same calendar date and price** as OFTS; it therefore has a shorter holding period and is a timing diagnostic, not a same-horizon strategy comparison.

**Price-source validation:** all **36/36** frozen ledger entry prices matched SIP daily opens within 0.5%; all **3/3** completed exit prices matched. No invented fills were needed. SIP auction opening prices are still not a guarantee of executable individual fills.

## Censored mark-to-market results — NOT realized portfolio performance

| Comparison | N | Mean return | Median return | Positive |
|---|---:|---:|---:|---:|
| OFTS entries, 0.20% assumed costs | 36 | **+3.877%** | **-0.283%** | 17 |
| Matched SPY, price-only | 36 | **-1.612%** | -2.003% | 1 |
| Matched IWM, price-only | 36 | **+0.831%** | +0.892% | 26 |
| Same-stock one-day-delayed entry, same exit | 33 | **+3.524%** | -0.777% | 16 |

For the **33 paired delayed-entry comparisons**, the original OFTS entry was ahead by **+0.932 percentage points on average** and ahead in **19/33**. The unpaired three positions have no valid delayed entry before the original exit/censor. This is retrospective, with heavily overlapping holdings and right-censored open trades.

**Crucial concentration test:** the original OFTS average depends heavily on a few open winners:

| Largest winners excluded | Remaining N | OFTS mean | Matched SPY mean | Matched IWM mean |
|---|---:|---:|---:|---:|
| None | 36 | +3.877% | -1.612% | +0.831% |
| Top 1 | 35 | +1.275% | -1.594% | +0.815% |
| **Top 2** | **34** | **-0.053%** | -1.582% | **+0.813%** |
| **Top 3** | **33** | **-0.846%** | -1.589% | **+0.750%** |
| Top 5 | 31 | -2.122% | -1.600% | +0.733% |

Top three open marks: **BETR +94.931%, ATGL +46.430%, LYEL +26.116%**. The large gains are *unrealized* as of the October 30 cutoff. Removing the two largest open marks turns the OFTS mean negative and below matched IWM. This is a retrospective outlier-dependence stress test, not a claim those winners should be removed.

**Completed trades only (N=3):** YDES -39.144%, MF -23.840%, CCS -4.367%; equal-weight mean **-22.451%**, all losses. Matched SPY average **-0.821%** and matched IWM average **+1.015%**. Three trades are far too few for statistical inference.

## Fixed stop sensitivity, all 36 entries including open censored positions

For each trade/position, simulate fixed stops at 5%, 10%, and 12% below the original entry using *the saved daily SIP OHLC bars*. If a later session opens below the stop, use the worse opening price; otherwise assume an intraday fill at the stop threshold if the low touches it. For completed trades, the original SELL exits at the next-session open, so no stop test is applied after that exit. Do not reenter after a simulated stop. All stop results subtract 0.20% assumed round-trip costs.

| Rule | N | Mean marked/closed return | Median | Positive | Worst |
|---|---:|---:|---:|---:|---:|
| No fixed stop | 36 | +3.877% | -0.283% | 17 | -39.144% |
| 5% stop | 36 | **+0.803%** | -2.663% | 13 | -8.424% |
| 10% stop | 36 | +3.361% | -0.578% | 16 | -10.200% |
| 12% stop | 36 | +3.415% | -0.578% | 16 | -12.200% |

The 5% stop reduces the worst modeled loss but also cuts the average substantially and removes four positive marked outcomes. The 10%/12% rules also fail to improve the mean. This is *not* a deployable stop strategy: fills at intraday stop thresholds are optimistic, gap/spread/impact can worsen results, and many positions are still open. The same calendar sample was used for inspection, not an untouched holdout.

## Methodological limits and decision

1. **Open-position censoring:** 33 of 36 observations are open, not completed BUY-to-SELL trades. The mark-to-market mean is not realized profit or a capital-weighted portfolio result.
2. **Execution:** opening auction prints, SIP daily OHLC and 0.20% cost assumptions do not establish attainable fills, spreads, borrow constraints, order sizes, or capacity.
3. **Selection:** these are observed historical BUYs, not a randomly selected untouched holdout. There is no control for survivorship of the original candidate universe.
4. **Independence:** entries and holding periods overlap. No valid standard error, significance claim, or portfolio drawdown is calculated.
5. **Same-stock control:** one-day delayed entry shares the same exit but a shorter horizon. A true same-horizon and passive-control design remains necessary.
6. **Longer horizons:** no matured 20/30/60-session outcomes in the frozen October 30 saved audit.

**Verdict: RESEARCH_ONLY_NO_GO.** The aggregate favorable marked mean is dominated by a handful of still-open winners, and the only three completed trades lost. No realistic, independently replicated profitable edge is proven.

## Reproduction

- Frozen daily SIP bars: `ofts/experiments/SIP_DAILY_BARS_2026-10-09_TO_2026-10-30.csv`
- Read-only standard-library replay: `ofts/experiments/sip_matched_censor_audit_20261102.py`
- Frozen state: `ofts-daily-state` commit `eb05038a4e793e5ecb844b8fcd321e3ccb8e9db9`
- Run `python ofts/experiments/sip_matched_censor_audit_20261102.py /path/to/state ofts/experiments/SIP_DAILY_BARS_2026-10-09_TO_2026-10-30.csv`
