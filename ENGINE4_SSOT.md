# Engine 4 — Intraday Perfect Setup SSOT v4.3
Locked for live trial: 2026-09-14

## Golden Rules
1. Never guess or assume.
2. No shortcuts or skipped steps.
3. Follow this SSOT exactly.
4. Verify before reporting completion.

## Purpose
Engine 4 is a separate long-only intraday/day-trading engine. Engines 1–3 remain untouched. Engine 4 must search broadly enough to surface real opportunities, then become progressively stricter. The early pre-screen is NOT allowed to behave like the final A+ trade gate.

A valid day may end in NO TRADE, but a healthy engine should normally have stocks survive the broad pre-screen and advance into deeper analysis. Zero broad survivors is treated as a data/pipeline failure unless the underlying investable universe itself is unavailable.

## Free-data rule
Use the existing Rocket free-data stack first. Production code uses Yahoo Finance/yfinance and the existing Rocket baseline outputs. Alpaca free may be used as an independent live cross-check in ChatGPT, but Engine 4 must not require a paid data subscription. No paid source may be added without explicit user approval after a documented gap is proven.

## Ordered daily schedule — Eastern Time
The production workflow wakes early, then executes these stages in order. It may never run the final stage before the earlier stages complete.

- 08:55 ET — BROAD PRE-SCREEN starts.
- Target by ~09:05 ET — PRE-SCREEN completes and publishes the full survivor list.
- 09:05 ET — DEEP 100-POINT ANALYSIS starts on the strongest pre-screen survivors.
- 09:18 ET — mandatory fresh full-universe REFRESH + RERANK starts.
- Target by ~09:25 ET — TOP-25 FREEZE completes and publishes the ranked frozen shortlist internally.
- 09:30 ET — market opens.
- 09:30–09:45 ET — opening structure forms.
- 09:45 ET — FINAL LIVE CONFIRMATION starts on the frozen shortlist only.
- Target by ~09:48 ET — BUY NOW or NO TRADE result completes.

Every stage must record its actual Eastern start/completion timestamp. Displayed times are actual execution times, not invented schedule labels.

## Starting universe
Reuse the prior Rocket daily investable universe and fundamentals cache, sourced from the official listed-symbol universe and Yahoo Finance. Baseline investability gates remain:
- price >= $5
- market cap >= $300M
- average daily dollar volume >= $20M
- existing Rocket common-stock/ADR investability exclusions remain in force

Engine 4 must not rebuild or alter Engines 1–3.

## Stage 1 — Broad pre-screen
The broad pre-screen exists to FIND candidates, not eliminate the day before analysis begins.

For every baseline-eligible stock with trustworthy current premarket observations, calculate premarket gap, premarket volume, premarket dollar volume and activity score. The former activity thresholds — gap >= 0.50% and premarket dollar volume >= $500,000 — remain useful quality flags, but they are no longer all-or-nothing kill switches.

Rank objective premarket activity and retain up to 100 names. Positive premarket movers with real dollar volume rank first. If strict activity names are sparse, retain the strongest valid observed names rather than returning a false zero.

Required output after completion:
- actual start and completion times ET
- baseline-eligible stock count
- number with trustworthy premarket observations
- survivor count
- complete survivor ticker list
- number that met the former strict activity thresholds

## Stage 2 — Deep 100-point analysis
Analyze up to the strongest 60 pre-screen survivors with the locked 100-point model:
- Catalyst quality: 25
- Relative premarket volume: 20
- Premarket price/gap quality: 15
- Liquidity/dollar volume: 15
- Room to resistance: 10
- ATR/volatility suitability: 5
- Sector + market relative strength: 5
- Execution/spread quality: 5

Total: 100 points.

Reference A-grade premarket gates remain visible and auditable:
- identifiable positive catalyst/reason from recent news
- premarket relative volume >= 1.5x recent premarket baseline
- ATR >= 1.5% of price
- live bid/ask spread <= 0.60%
- positive room to resistance
- score >= 70/100

IMPORTANT: these premarket A-grade gates now classify/rank quality; they do not automatically erase every near-miss before the 09:45 opening test. Promotional-looking moves remain rejected by the catalyst logic. Missing/stale data must be marked, never fabricated.

Required output after completion:
- actual start/completion times ET
- number analyzed
- number meeting every strict premarket A-grade gate
- ranked leaders and scores
- each ticker’s grade/failures retained in audit output

## Stage 3 — 09:18 refresh, rerank, Top-25 freeze
At 09:18 ET, refresh the broad universe with the latest premarket data, rescore and rerank. Freeze up to the best 25 trustworthy ranked names. The Top-25 is an arena for the live opening test; it is not itself a BUY list.

Sort by:
1. strict premarket A-grade status
2. total 100-point score
3. count of quality gates passed
4. relative premarket volume
5. premarket dollar volume

Do not insert random names. Do not silently return zero because a soft ranking threshold was too restrictive. Zero frozen names is a data/pipeline failure if trustworthy scored names exist.

Internal/audit output must retain the complete frozen Top-25 with score and grade per name. User-facing reports do NOT need to repeat all 25 names. To prove the stage completed without redundant clutter, show only the ranked Top 10 finalists that advanced to the final-scan arena, including ticker, score/grade, and concise reason/strength. The full Top-25 remains preserved in the production artifact for verification when needed.

Required user-facing output:
- actual refresh start and freeze completion times ET
- count of frozen candidates
- ranked Top 10 finalists only
- score/grade for each displayed finalist
- count of strict premarket A-grade names

## Stage 4 — 09:45 final A+ live gates
Analyze only the frozen shortlist. Every BUY must pass the live mandatory setup logic:
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

The 09:45 live gate is intentionally the strictest stage. Premarket near-misses are allowed into the arena because a stock can improve materially after the opening bell; it still receives no BUY unless the live setup fully qualifies.

## Entry / stop / management
- Entry trigger: opening-range high + 0.05% confirmation buffer.
- Initial stop: just below strongest nearby VWAP/recent higher-low support.
- First management level: no lower than 2R; target logic may use the nearer of a 2.5R objective and identified overhead resistance only when at least 2R remains available.
- Do not chase beyond the allowed 0.50% breakout band.

## Runner / trailing stop
A trailing stop may activate only after:
1. price reaches at least +1R, and
2. a confirmed higher low forms above entry.

Then trail just below the newest confirmed higher-low / VWAP support and never loosen the stop.

## Required user-facing timeline
The daily result must be understandable without opening code. It must read in chronological order similar to:

`08:55:02 ET — PRE-SCREEN STARTED`
`09:03:41 ET — PRE-SCREEN COMPLETED — 100 survivors`
`Survivors: ...`
`09:05:00 ET — DEEP 100-POINT ANALYSIS STARTED`
`09:16:12 ET — DEEP ANALYSIS COMPLETED — 60 analyzed / X strict A-grade`
`09:18:00 ET — REFRESH + RANKING STARTED`
`09:23:47 ET — TOP-25 FROZEN`
`Final-scan Top 10: 1. TICKER score/grade ... through 10. TICKER score/grade`
`09:45:00 ET — FINAL LIVE CONFIRMATION STARTED`
`09:47:26 ET — FINAL LIVE CONFIRMATION COMPLETED`
`RESULT: BUY ...` or `RESULT: NO TRADE — no A+ setup.`

Times above are examples only; production must display actual ET timestamps.

## Final output
If no ticker passes every final live mandatory gate:
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

## Fail-safe rules
- Missing or stale required data => DATA FAILURE or NO TRADE as appropriate; never fabricated values.
- Missing frozen Top-25 => final stage must not pretend a normal full-cycle NO TRADE occurred.
- Stale/extended entry => NO TRADE.
- Production stages must execute in order.
- Engine 4 is intraday only and must not silently become an overnight hold.
- Production alert is generated from Engine 4 output artifacts; ChatGPT relays it.
