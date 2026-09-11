# Engine 4 — Intraday Perfect Setup SSOT
Locked for trial: 2026-09-11

## Golden Rules
1. Never guess or assume.
2. No shortcuts or skipped steps.
3. Follow this SSOT exactly.
4. Verify before reporting completion.

## Purpose
Engine 4 is a separate long-only intraday/day-trading engine. Engines 1–3 remain untouched. Engine 4 trades only A+ setups and may produce NO TRADE for multiple consecutive days.

## Free-data rule
Use the existing Rocket free-data stack first. Production code uses Yahoo Finance/yfinance and the existing Rocket baseline outputs. Alpaca free may be used as an independent live cross-check in ChatGPT, but Engine 4 must not require a paid data subscription. No paid source may be added without explicit user approval after a documented gap is proven.

## Exact daily schedule — Eastern Time
- 08:55 ET: premarket job starts.
- 08:55–09:05 ET target: fast broad-universe elimination.
- 09:05–09:18 ET target: deep candidate enrichment/scoring.
- 09:18–09:25 ET target: refresh/rerank and freeze final candidate list.
- 09:25 ET: Top 25 frozen. If fewer than 25 clear the quality floor, do not insert weak names to fill the list.
- 09:30 ET: market opens.
- 09:30–09:45 ET: opening structure forms.
- 09:45 ET: final live job starts on the frozen shortlist only.
- 09:48 ET target: actionable ChatGPT signal delivered.

## Starting universe
Reuse the prior Rocket daily investable universe and fundamentals cache, sourced from the official listed-symbol universe and Yahoo Finance. Apply:
- price >= $5
- market cap >= $300M
- average daily dollar volume >= $20M
- existing Rocket common-stock/ADR investability exclusions remain in force

Engine 4 must not rebuild or alter Engines 1–3.

## Broad premarket elimination
This stage is computationally fast but high quality. It only narrows the universe; it does not pick the trade.

Hard filters:
- current premarket dollar volume >= $500,000
- positive premarket gap >= 0.50%
- gap <= 25%
- price remains >= $5
- existing market-cap/liquidity gates remain satisfied

Rank objective premarket activity and keep at most 100 names for deep analysis. No random selection and no simple top-gainers list.

## Deep premarket 100-point score
Locked weights:
- Catalyst quality: 25
- Relative premarket volume: 20
- Premarket price/gap quality: 15
- Liquidity/dollar volume: 15
- Room to resistance: 10
- ATR/volatility suitability: 5
- Sector + market relative strength: 5
- Execution/spread quality: 5

Total: 100 points.

A-grade hard gates before the Top 25:
- identifiable positive catalyst/reason from recent news; promotional-looking moves rejected
- premarket relative volume >= 1.5x recent premarket baseline
- ATR >= 1.5% of price
- live bid/ask spread <= 0.60%
- positive room to resistance
- minimum premarket score = 70/100

The engine may return fewer than 25 if fewer than 25 names clear every gate. It must never fill the list with weaker names just to reach 25.

## Top 25 freeze
Sort survivors by total premarket score, then relative premarket volume, then premarket dollar volume. Premarket rank gets a stock into the arena only; it does not create a buy signal.

## 09:45 ET final A+ gates
Analyze only the frozen shortlist. Every BUY must pass every mandatory gate:
- relative strength > SPY/QQQ composite
- relative strength > relevant sector ETF where mapped
- price at/above VWAP
- no lower-low deterioration
- clean higher-low or tight-base structure
- price attacking the opening-range high / breakout level
- pullback volume contracts
- breakout volume expands by at least 1.20x versus the immediate pullback baseline
- refreshed live spread <= 0.60%
- not extended more than 1.50% above VWAP
- entry is not more than 0.50% beyond the breakout trigger
- obvious technical stop from VWAP/recent higher-low structure
- at least 2.0:1 reward/risk before known resistance / management level
- reject if SPY and QQQ both suffer a hard adverse opening reversal <= -0.60% with negative recent momentum

If any mandatory gate fails, that ticker is not a BUY.

## Entry / stop / management
- Entry trigger: opening-range high + 0.05% confirmation buffer.
- Initial stop: just below strongest nearby VWAP/recent higher-low support.
- First management level: no lower than 2R; target logic may use the nearer of a 2.5R objective and identified overhead resistance only when at least 2R remains available.
- Do not chase beyond the allowed 0.50% breakout band.

## Runner / trailing stop
Start with the defined initial stop. A trailing stop may activate only after:
1. price reaches at least +1R, and
2. a confirmed higher low forms above entry.

Then trail just below the newest confirmed higher-low / VWAP support and never loosen the stop.

## Final output
If no ticker passes every mandatory gate:
`NO TRADE — no A+ setup.`

If the only otherwise-valid opportunity has already run beyond a safe entry:
`NO TRADE — entry missed.`

If one or more names pass, rank the full-pass names and send only the strongest one:

`BUY [TICKER] NOW`
`Entry/trigger: $...`
`Initial stop: $...`
`First management level: $...`
`Trailing stop: ...`
`Reason: ...`

Do not show rejected tickers or near-misses in the user alert.

## Fail-safe rules
- Missing or stale required data => NO TRADE, never fabricated values.
- Missing frozen Top 25 => NO TRADE.
- Stale/extended entry => NO TRADE.
- Engine 4 is intraday only and must not silently become an overnight hold.
- Production alert is generated from the Engine 4 output artifact; ChatGPT relays it.
