# OFTS fixed and trailing stop grid — 2026-11-02 (retrospective, NOT validated optimum)

Source: ofts-daily-state/cycle_ledger.json read 2026-11-02, and research-branch ofts/experiments/SIP_DAILY_BARS_2026-10-09_TO_2026-10-30.csv. 36 distinct executed entries with October 30 or earlier entry and available daily SIP bars. Four completed trades in the November 2 ledger, but MH's November 2 exit is **not** included: MH is censored at October 30. 33 open or pending positions and three completed exits as of October 30. Two pending Nov 3 entries and any entries after Oct 30 excluded.

Simulation: equal weight per entry; fixed stop at entry*(1-p); trailing stop at highest observed high of prior bars or entry*(1-p); at session open if below stop, fill at that worse open; otherwise if session low breaches stop, optimistic fill at stop level; stop checks begin on entry session after opening entry. No reentry. Otherwise saved exit open if dated by Oct 30, else Oct 30 close. Subtract 0.20 percentage points total costs. No real execution, slippage, order-book impact, or cash-reinvestment accounting. Trailing rule uses prior-bar highs only, avoiding same-bar high/low lookahead, but same-day entry-stop and intraday trigger fills remain optimistic.

| Rule | N | Mean net % | Median % | Worst % | Positive | Stops triggered |
|---|---:|---:|---:|---:|---:|---:|
| No stop (saved audit baseline) | 36 | 3.877 | -0.283 | -39.144 | 17 | 0 |
| Fixed 3% | 36 | 0.361 | -3.200 | -7.034 | 11 | 23 |
| Fixed 4% | 36 | 0.479 | -4.200 | -7.034 | 12 | 20 |
| Fixed 5% | 36 | 0.803 | -2.663 | -8.424 | 13 | 16 |
| Fixed 6% | 36 | 1.024 | -0.819 | -8.424 | 15 | 14 |
| Fixed 7% | 36 | 0.813 | -0.819 | -8.424 | 15 | 12 |
| Fixed 8% | 36 | 0.759 | -0.819 | -8.424 | 15 | 10 |
| Fixed 9% | 36 | 3.528 | -0.578 | -9.200 | 16 | 6 |
| Fixed 10% | 36 | 3.361 | -0.578 | -10.200 | 16 | 6 |
| Fixed 12% | 36 | 3.415 | -0.578 | -12.200 | 16 | 4 |
| Fixed 15% | 36 | 4.794 | -0.283 | -15.200 | 17 | 3 |
| Fixed 20% | 36 | 4.504 | -0.283 | -20.200 | 17 | 2 |
| Trailing 3% | 36 | 0.041 | -1.937 | -6.314 | 13 | 32 |
| Trailing 4% | 36 | -0.491 | -2.355 | -6.314 | 13 | 31 |
| Trailing 5% | 36 | -0.596 | -1.037 | -6.314 | 13 | 30 |
| Trailing 6% | 36 | -0.862 | -1.345 | -8.424 | 14 | 26 |
| Trailing 7% | 36 | -0.100 | -1.278 | -8.424 | 15 | 23 |
| Trailing 8% | 36 | 0.034 | -0.984 | -8.424 | 14 | 18 |
| Trailing 9% | 36 | 1.197 | -0.819 | -9.200 | 15 | 17 |
| Trailing 10% | 36 | 1.148 | -0.819 | -10.200 | 15 | 13 |
| Trailing 12% | 36 | 3.258 | -0.283 | -12.200 | 17 | 8 |
| Trailing 15% | 36 | 5.278 | -0.283 | -13.907 | 17 | 3 |
| Trailing 20% | 36 | 4.926 | -0.283 | -18.831 | 17 | 2 |

The in-sample maximum average is trailing 15%, but this is NOT an optimal live stop: selected retrospectively from 23 candidates, 33 positions still open at cutoff, highly overlapping, thinly traded winners, and unrealistic stop execution. Median remains negative. Need untouched chronological holdout, bid/ask and gap/slippage sensitivity, per-stock matched SPY/IWM, independent completed trades, and drawdown. Production unchanged. No orders.
