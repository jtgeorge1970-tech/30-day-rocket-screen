# OFTS 3-trade fixed-stop sensitivity — 2026-10-30

**RESEARCH_ONLY_NO_GO.** Post-hoc diagnostic on all two officially completed hypothetical trades plus the October 29 SELL / October 30 scheduled exit CCS, whose official closure was **not yet verified** when this experiment ran. No production changes or orders.

## Sources and deterministic method
- Permanent `ofts-daily-state/cycle_ledger.json` as inspected October 30 before the post-close rerun: YDES Oct12 $7.01 to Oct23 $4.28, MF Oct16 $10.66 to Oct28 $8.14, CCS Oct23 $56.63 with SELL signal Oct29 and planned Oct30 open exit.
- Independently fetched Alpaca SIP daily OHLCV bars, October 12–30, for all three symbols; recorded entry and exit opening prices matched the SIP daily opens to displayed precision.
- Entry at recorded next-session open. For a fixed stop of 5%, 10%, or 12% below entry, examine daily lows from entry date through the day **before** the scheduled original next-open exit. First low <= stop triggers hypothetical exit at stop price, **unless that day's opening price is already below the stop**, in which case exit at the opening price (gap-aware). No intraday bar sequencing, spread, partial fills, halts, stop-market slippage or liquidity model. If stop never triggers, exit at original scheduled open. Subtract 0.20 percentage points assumed round-trip cost for each hypothetical trade.
- The stop thresholds were selected **after** observing the losing trades. This is not a chronological untouched holdout, a reliable stop model, or proof of improvement.

| Symbol | Baseline net | 5% stop net (trigger date) | 10% stop net (trigger date) | 12% stop net (trigger date) |
|---|---:|---:|---:|---:|
| YDES | -39.144% | -5.200% (Oct12) | -10.200% (Oct12) | -12.200% (Oct12) |
| MF | -23.840% | -5.200% (Oct20) | -10.200% (Oct22) | -12.200% (Oct23) |
| CCS* | -4.367% | -7.034% (Oct29 gap) | -10.200% (Oct29) | -4.367% (not triggered) |
| Equal-weight mean of three selected losers | **-22.451%** | **-5.811%** | **-10.200%** | **-9.589%** |

*CCS is a provisional planned-exit reconstruction, not an officially completed trade until durable ledger confirmation.*

## Interpretation
- This is a **loser-selected** sample of three; the substantial apparent improvement for 5% stops is subject to severe selection bias. A full universe test must include all still-open positions, winners, stop-triggered exits, reentries and opportunity cost, on an untouched chronological holdout.
- A 5% stop **worsened** CCS (−7.034% vs −4.367%) because its October 29 open ($52.76) gapped below the stop ($53.7985). Actual stop-market execution can be worse.
- The YDES 5% stop is touched **on the entry day**, demonstrating how a simple tight stop may exit a position almost immediately. Intraday sequencing is not modeled.
- MF intraday lows show stop touch but not achievable fill at the trigger; quoted spreads can be material. Daily OHLC stop-touch arithmetic is optimistic.
- These three negative baseline trades cannot be used to estimate a portfolio drawdown or win rate. Overlapping positions and capital allocation remain unmodeled.

**Conclusion: NO-GO remains.** Only prospective, precommitted stop rules with realistic execution and adequate independent completed trades can inform a live-trading decision.