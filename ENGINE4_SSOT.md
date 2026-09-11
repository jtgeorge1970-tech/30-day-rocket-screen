# Engine 4 — Intraday Perfect Setup SSOT v4.5
Locked for live trial: 2026-09-14

## Golden Rules
1. Never guess or assume.
2. No shortcuts or skipped steps.
3. Follow this SSOT exactly.
4. Verify before reporting completion.

## Non-negotiable reporting integrity rule
Engine 4 must never describe a configured ranking cap as though it were a naturally occurring survivor count.

The following quantities must always be labeled separately:
- NATURAL QUALIFICATION COUNT = how many names actually met the defined criteria before a cap was applied.
- NONZERO PREMARKET ACTIVITY COUNT = how many naturally qualified names also had non-zero premarket dollar volume reported by the data source.
- RETAINED BY CAP = how many names were deliberately kept because the engine is configured to carry only the strongest N forward.
- SELECTED FOR DEEP ANALYSIS = how many names were deliberately chosen for the 100-point analysis because of the configured deep-analysis cap.
- ACTUALLY ANALYZED = how many selected names had enough trustworthy data to complete scoring.
- SCORE >=70 COUNT = how many actually reached the 70-point reference threshold.
- STRICT A-GRADE COUNT = how many met every strict premarket A-grade gate.
- FROZEN FINAL-SCAN COUNT = how many ranked names were frozen for the 09:45 live scan.

Rounded values such as 100, 60 or 25 are expected when they are configured caps. They must be explicitly labeled as caps and never presented as organic pass/fail results.

## Purpose
Engine 4 is a separate long-only intraday/day-trading engine. Engines 1–3 remain untouched. Engine 4 must search broadly enough to surface real opportunities, then become progressively stricter. The early pre-screen is NOT allowed to behave like the final A+ trade gate.

A valid day may end in NO TRADE, but a healthy engine should normally produce a broad naturally-qualified population and then rank the strongest names forward. Zero naturally-qualified names with otherwise healthy price data must be investigated and cannot be casually reported as a normal trading conclusion.

## Free-data rule
Use the existing Rocket free-data stack first. Production code uses Yahoo Finance/yfinance and the existing Rocket baseline outputs. Alpaca free may be used as an independent live cross-check in ChatGPT, but Engine 4 must not require a paid data subscription. No paid source may be added without explicit user approval after a documented gap is proven.

## Ordered daily schedule — Eastern Time
The production workflow wakes early, then executes these stages in order. It may never run the final stage before the earlier stages complete.

- 08:55 ET — BROAD PRE-SCREEN starts.
- Target by ~09:05 ET — PRE-SCREEN completes and publishes true qualification counts plus the retained candidate pool.
- 09:05 ET — DEEP 100-POINT ANALYSIS starts on the highest-ranked retained candidates.
- 09:18 ET — mandatory fresh full-universe REFRESH + RERANK starts.
- Target by ~09:25 ET — TOP-25 FREEZE completes and publishes the ranked frozen shortlist internally.
- 09:30 ET — market opens.
- 09:30–09:45 ET — opening structure forms.
- 09:45 ET — FINAL LIVE CONFIRMATION starts on the frozen shortlist only.
- Target by ~09:48 ET — BUY NOW or NO TRADE result completes.

Every stage must record its actual Eastern start/completion timestamp. Displayed times are actual execution times, not invented schedule labels.

## Starting universe
Reuse the prior Rocket daily investable universe and fundamentals cache. Baseline investability gates remain:
- price >= $5
- market cap >= $300M
- average daily dollar volume >= $20M
- existing Rocket common-stock/ADR investability exclusions remain in force

Engine 4 must not rebuild or alter Engines 1–3.

## Stage 1 — Broad pre-screen
The broad pre-screen exists to FIND candidates, not eliminate the day before analysis begins.

For every baseline-eligible stock with trustworthy current premarket observations, calculate premarket gap, premarket volume, premarket dollar volume and activity score.

### Locked natural broad-qualification rule
Natural broad qualification is deliberately permissive and restores the same broad criterion used before the reporting-integrity repair:
- baseline investability already passed
- trustworthy current premarket price observation exists
- price is valid and >= $5
- valid prior-close reference exists

A stock does NOT need non-zero Yahoo-reported premarket volume to count as naturally broad-qualified. Yahoo can return valid extended-hours prices while reporting zero volume in the 1-minute bars. Treating zero reported volume as an automatic disqualifier is a data-source regression and is prohibited.

The NATURAL BROAD QUALIFICATION COUNT is measured and reported before any cap is applied.

Separately report:
- NONZERO PREMARKET ACTIVITY COUNT = naturally qualified names with premarket dollar volume > 0
- STRICT ACTIVITY COUNT = gap >= 0.50%, gap <= 25%, and premarket dollar volume >= $500,000

Those volume/activity measures are quality and ranking signals. They are not all-or-nothing early kill switches.

### Locked ranking behavior
Preserve the prior broad ranking behavior:
1. Prefer positive movers with non-zero premarket volume.
2. If none exist, prefer names with any non-zero premarket volume.
3. If the data source reports zero premarket volume across the observed set, rank the trustworthy observed set rather than manufacturing a false zero-candidate day.
4. Sort by strict-activity flag, activity score, then premarket dollar volume.
5. Retain no more than the configured Top-100 candidate cap.

Required output after completion:
- actual start/completion times ET
- baseline-eligible stock count
- number with trustworthy observations
- NATURAL broad-qualified count
- NONZERO premarket activity count
- strict-activity count
- RETAINED BY TOP-100 CAP count
- retained ticker list

Never use the word “survived” for a Top-100 cap as though exactly 100 independently passed a threshold.

## Stage 2 — Deep 100-point analysis
Select up to the highest-ranked 60 retained candidates for the locked 100-point model. The number 60 is a configured workload/ranking cap, not an organic survivor count.

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

Reference A-grade premarket gates remain visible and auditable:
- identifiable positive catalyst/reason from recent news
- premarket relative volume >= 1.5x recent premarket baseline
- ATR >= 1.5% of price
- live bid/ask spread <= 0.60%
- positive room to resistance
- score >= 70/100

These gates classify/rank quality; they do not automatically erase every near-miss before the 09:45 opening test. Promotional-looking moves remain rejected by catalyst logic. Missing/stale data must be marked, never fabricated.

Required output after completion:
- SELECTED FOR DEEP ANALYSIS count, explicitly labeled as cap-driven
- ACTUALLY ANALYZED count
- SCORE >=70 count
- B-grade count
- STRICT A-GRADE count
- ranked leaders and scores
- each ticker’s failures retained in audit output

## Stage 3 — 09:18 refresh, rerank, Top-25 freeze
At 09:18 ET, refresh the broad universe with the latest premarket data and repeat the honest funnel accounting:
- naturally broad-qualified count
- nonzero premarket activity count
- retained-by-Top-100-cap count
- selected-for-deep count
- actually analyzed count
- score >=70 count
- strict A-grade count

Then freeze up to the best 25 trustworthy ranked names. Top-25 is a configured final-scan arena cap, not a claim that exactly 25 stocks passed an independent threshold.

Sort by:
1. strict premarket A-grade status
2. total 100-point score
3. count of quality gates passed
4. relative premarket volume
5. premarket dollar volume

Do not insert random names. Do not silently convert a ranking limit into a “survivor” count.

Internal/audit output must retain the complete frozen Top-25 with score and grade per name. User-facing reports show only the ranked Top 10 finalists to prove the final-scan arena formed without redundant clutter. The full Top-25 remains preserved in the production artifact.

Required user-facing output:
- actual refresh start/freeze completion times ET
- honest funnel counts listed above
- frozen count explicitly labeled as cap-driven ranking output
- ranked Top 10 finalists only
- score/grade for each displayed finalist

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
- entry is not more than 0.50% beyond breakout trigger
- obvious technical stop from VWAP/recent higher-low structure
- at least 2.0:1 reward/risk before known resistance / management level
- reject if SPY and QQQ both suffer a hard adverse opening reversal <= -0.60% with negative recent momentum

The 09:45 live gate is intentionally the strictest stage. Premarket near-misses may enter the arena because a stock can improve materially after the opening bell; it still receives no BUY unless the live setup fully qualifies.

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
The daily result must be understandable without opening code and must clearly distinguish natural counts from configured caps. Example format only:

`08:55:02 ET — PRE-SCREEN STARTED`
`09:03:41 ET — PRE-SCREEN COMPLETED`
`Baseline eligible: 1,870`
`Trustworthy observations: 1,842`
`Naturally broad-qualified: 1,842`
`Nonzero premarket activity: 74`
`Strict-activity names: 18`
`Retained by Top-100 cap: 100`
`09:05:00 ET — DEEP 100-POINT ANALYSIS STARTED`
`Selected for deep analysis by Top-60 cap: 60`
`Actually analyzed: 57`
`Score >=70: 9`
`Strict A-grade: 3`
`09:18:00 ET — REFRESH + RANKING STARTED`
`09:23:47 ET — TOP-25 FROZEN`
`Final-scan Top 10: 1. TICKER score/grade ... through 10. TICKER score/grade`
`09:45:00 ET — FINAL LIVE CONFIRMATION STARTED`
`09:47:26 ET — FINAL LIVE CONFIRMATION COMPLETED`
`RESULT: BUY ...` or `RESULT: NO TRADE — no A+ setup.`

All numbers and times above are illustrative only. Production must display actual measured values.

## Regression note — 2026-09-11
During the reporting-integrity repair, the code was accidentally tightened from “trustworthy premarket price observation” to “trustworthy price plus non-zero Yahoo-reported premarket dollar volume.” That was NOT the same criterion and caused a false zero-candidate failure in a same-day test. This regression is prohibited going forward. The restored rule above is authoritative.

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
- Any report that conflates a configured cap with a natural pass count is considered a reporting failure and must be corrected before the result is accepted.
- Any code change that alters a screening criterion must be explicitly identified and approved in the SSOT; reporting-only fixes may not silently tighten or loosen trading criteria.
