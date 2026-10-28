# OFTS October 28 next-open SIP execution diagnostic

Research only. Six v2.3 BUY signals were frozen after the October 27 close; the experimental viability filter rejected all six. Alpaca SIP daily bars and Level-1 quote samples retrieved October 28 after the close. These are NOT executed trades, executable fill guarantees, completed BUY-to-SELL trades, or a new qualified October 28 OFTS cohort.

Open-to-close net assumes a buy at the consolidated daily open and sale at daily close minus 0.20 percentage points in costs. The alternative ask-to-close net uses the first sampled quote at or after 09:35 ET (ATEX 09:37), buys at its ask and sells at daily close, also minus 0.20 pp. It does NOT account for selling at the bid or full market impact; both calculations are optimistic diagnostics. The first 09:30 quote may be transient or unfillable.

| Symbol | Open | Close | Volume | Open-close net % | First 09:30 bid/ask | 09:30 spread % | Later bid/ask (ET) | Later spread % | Ask-close net % |
|---|---:|---:|---:|---:|---|---:|---|---:|---:|
| MESO | 13.24 | 13.39 | 171034 | 0.933 | 13/13.75 | 5.607 | 13.17/13.66 (09:35:04) | 3.653 | -2.177 |
| XPRO | 17.51 | 17.61 | 742023 | 0.371 | 14.19/17.7 | 22.013 | 16.97/17.68 (09:35:03) | 4.098 | -0.596 |
| LTRX | 6.3 | 6.3 | 469261 | -0.200 | 6.19/6.51 | 5.039 | 6.21/6.27 (09:35:00) | 0.962 | 0.278 |
| ACDC | 4.61 | 4.99 | 1919952 | 8.043 | 4.54/4.67 | 2.823 | 4.67/4.69 (09:35:04) | 0.427 | 6.197 |
| AOMR | 7.35 | 7.23 | 95269 | -1.833 | 7.3/7.59 | 3.895 | 7.33/7.44 (09:35:03) | 1.490 | -3.023 |
| ATEX | 86.33 | 87.95 | 219713 | 1.677 | 82.4/89.39 | 8.138 | 85.62/87.31 (09:37:05) | 1.955 | 0.533 |

Equal-weight six-name open-to-close mean net: 1.498%; SPY same-day gross 0.114%; IWM same-day gross 0.335%. These are one-day diagnostics, not fair matched-horizon strategy benchmarks.
Ask-to-close mean net: 0.202%; excluding ACDC: -0.997%. Opening sampled spreads mean 7.919%; later sampled spreads mean 2.097%. Quotes are not fills.

## MF next-open SELL reconstruction
MF entry October 16 at $10.66 in frozen ledger; SELL signal October 27, planned exit October 28. SIP October 28 open $8.14 gives provisional gross -23.640% and net -23.840% after 0.20 pp cost. The saved ledger at latest qualified October 27 state still says OPEN_PENDING_EXIT. Do not count this as officially closed until durable cycle ledger is updated and independently verified. A holding-period-matched SPY comparison remains outstanding.

## v2.3 cost stress (from saved 2026-10-28 audit, market as-of October 27)
667 matured five-session scored observations: +0.1853% net at 0.20% assumed total costs, matched SPY -0.5324%, net excess +0.7177 pp. If total costs 0.50%, net -0.1147%; at 1.00%, net -0.6147%.
201 matured ten-session scored observations: -0.2940% net at 0.20% assumed costs, matched SPY -1.0729%, net excess +0.7789 pp. If total costs 0.50%, net -0.5940%; at 1.00%, net -1.0940%. This is deterministic stress of correlated observations, not new out-of-sample validation.

## Integrity / status
Latest qualified durable cohort is October 27, 13 cohorts, 1,670 frozen prediction rows, 945 matured 5-session and 362 matured 10-session observations across models/controls, zero matured 20/30/60. Latest daily run 40729515105 restored October 27 state and passed, without new October 28 cohort. Latest independent chart audit 40675367028 verified 50/50 charts for October 27. No production scoring changes, no brokerage trades.

Sources: [daily run](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/actions/runs/40729515105), [saved state commit](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/commit/db625dfe698bee64f2dafcdeab4081656b25367d), [signals](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/blob/ofts-daily-state/signals/2026-10-27.json), [cycle ledger](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/blob/ofts-daily-state/cycle_ledger.json), [independent chart audit](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/actions/runs/40675367028). SIP price/quote evidence retrieved via connected Alpaca historical bars/quotes with exact sampled values above.