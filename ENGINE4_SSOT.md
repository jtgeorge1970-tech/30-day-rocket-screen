# Engine 4 — Intraday Perfect Setup SSOT v4.9
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
- NONZERO PREMARKET ACTIVITY COUNT = how many enriched names had actual non-zero Nasdaq premarket share volume.
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

## Locked free-data architecture
No paid source is required for Engine 4. Production uses the following verified no-cost sources:

- Yahoo Finance / yfinance: batched broad price bars, historical bars, daily ATR/resistance inputs, SPY/QQQ/sector price context.
- Nasdaq public quote endpoint: current bid/ask spread.
- Nasdaq public extended-trading endpoint: actual current premarket consolidated price and premarket share volume.
- Google News RSS: recent catalyst headlines.
- Existing Rocket baseline outputs: investability, market cap, sector, average daily dollar volume.

Alpaca free IEX may still be used as an independent ChatGPT cross-check, but Engine 4 production must not depend on a paid service.

### Prohibited Yahoo dependencies
Yahoo Ticker.info and Yahoo Ticker.news are prohibited in the production Engine 4 decision path because live testing produced repeated HTTP 401/429 failures. Yahoo extended-hours 1-minute volume is also prohibited as the source of premarket share volume because live testing showed valid prices with zero extended-hours volume.

## Provider health rule
Before the pre-screen, 09:18 refresh, and 09:45 final stage, Engine 4 must verify:
- Nasdaq premarket endpoint returns a valid premarket price and share volume for a liquid reference symbol.
- Nasdaq quote endpoint returns a valid bid/ask spread.
- Google News RSS is reachable.

A systemic provider outage is DATA/PIPELINE FAILURE, not a normal NO TRADE day. During deep analysis, if valid Nasdaq spreads are available for fewer than half of analyzed names, fail closed as a provider-health failure.

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
- Target by ~09:48 ET — BUY NOW, WAIT, or NO TRADE result completes.

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

### Locked natural broad-qualification rule
Natural broad qualification is deliberately permissive:
- baseline investability already passed
- trustworthy current premarket price observation exists
- price is valid and >= $5
- valid prior-close reference exists

A stock does NOT need non-zero Yahoo-reported premarket volume to count as naturally broad-qualified. Yahoo is not used as the authoritative premarket-volume source.

The NATURAL BROAD QUALIFICATION COUNT is measured and reported before any cap is applied.

### Nasdaq premarket-volume enrichment
After the broad price universe is formed, rank a generous preliminary enrichment pool using positive gap and liquidity. Enrich up to 400 names with Nasdaq's public extended-trading endpoint. For each successfully enriched name, capture:
- consolidated premarket price
- actual premarket share volume
- premarket dollar volume
- premarket high/low when available

Then compute:

`PREMARKET VOLUME INTENSITY % = Nasdaq premarket shares / estimated average daily shares × 100`

where estimated average daily shares = average daily dollar volume / current premarket price.

This is an auditable current-session activity measure. It is NOT mislabeled as historical RVOL.

Separately report:
- NASDAQ PREMARKET ENRICHED count
- NONZERO PREMARKET ACTIVITY COUNT
- STRICT ACTIVITY COUNT = gap >= 0.50%, gap <= 25%, and premarket dollar volume >= $500,000

Those activity measures are ranking/quality signals, not all-or-nothing natural-qualification gates.

### Locked broad ranking behavior
Within the Nasdaq-enriched pool, sort by:
1. strict-activity flag
2. premarket-volume intensity
3. objective activity score
4. premarket dollar volume
5. positive price gap

Retain no more than the configured Top-100 candidate cap.

Required output after completion:
- actual start/completion times ET
- baseline-eligible stock count
- number with trustworthy price observations
- NATURAL broad-qualified count
- Nasdaq premarket enriched count
- NONZERO premarket activity count
- strict-activity count
- RETAINED BY TOP-100 CAP count
- retained ticker list

Never use the word “survived” for a Top-100 cap as though exactly 100 independently passed a threshold.

## Stage 2 — Deep 100-point analysis
Select up to the highest-ranked 60 retained candidates for the locked 100-point model. The number 60 is a configured workload/ranking cap, not an organic survivor count.

Locked weights:
- Catalyst quality: 25
- Relative premarket volume/activity: 20
- Premarket price/gap quality: 15
- Liquidity/dollar volume: 15
- Room to resistance: 10
- ATR/volatility suitability: 5
- Sector + market relative strength: 5
- Execution/spread quality: 5

Total: 100 points.

### Premarket-volume scoring hierarchy
Preferred metric, when a trustworthy historical premarket-volume baseline exists:
- true premarket RVOL = current premarket shares / median recent comparable premarket shares

Fallback metric, when historical premarket RVOL is unavailable:
- Nasdaq premarket-volume intensity % defined above

The audit output must identify which metric was used for every candidate. The fallback may never be labeled “RVOL.”

For the 20-point activity component:
- if true RVOL exists, retain the locked RVOL scoring curve
- otherwise use premarket-volume intensity, with 10% of estimated ADV receiving the full 20 points and lower values scaling proportionally

Reference strict premarket A-grade volume gate:
- true RVOL >= 1.5x when a trustworthy historical premarket baseline exists, OR
- Nasdaq premarket-volume intensity >= 2.0% of estimated ADV when historical premarket RVOL is unavailable

Other reference A-grade gates:
- identifiable positive catalyst/reason from recent Google News RSS headlines
- ATR >= 1.5% of price
- Nasdaq live bid/ask spread <= 0.60%
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
- each ticker's failure reasons
- premarket-volume metric source
- catalyst source
- spread source

## Stage 3 — 09:18 refresh, rerank, Top-25 freeze
At 09:18 ET, refresh the broad universe with the latest price data and repeat the Nasdaq premarket-volume enrichment and honest funnel accounting.

Report:
- naturally broad-qualified count
- Nasdaq premarket enriched count
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
4. premarket-volume intensity / true RVOL strength
5. premarket dollar volume

Do not insert random names. Do not silently convert a ranking limit into a “survivor” count.

Internal/audit output must retain the complete frozen Top-25 with score and grade per name. User-facing reports show only the ranked Top 10 finalists to prove the final-scan arena formed without redundant clutter. The full Top-25 remains preserved in the production artifact.

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
- refreshed Nasdaq live spread <= 0.60%
- not extended more than 1.50% above VWAP
- obvious technical stop from VWAP/recent higher-low structure
- at least 2.0:1 reward/risk before known resistance / management level
- reject if SPY and QQQ both suffer a hard adverse opening reversal <= -0.60% with negative recent momentum

The 09:45 live gate is intentionally the strictest stage. Premarket near-misses may enter the arena because a stock can improve materially after the opening bell; it still receives no BUY unless the live setup fully qualifies.

## Locked plain-English buy-signal state machine
The user-facing signal must use plain English. Do not lead with broker order-type jargon such as STOP-LIMIT or LIMIT. Engine 4 may use technical order logic internally, but the user should see only whether to BUY NOW, WAIT, or NOT BUY, plus the exact valid price range and exact downside/profit-protection instructions.

The words BUY NOW are reserved for an immediately actionable live entry. A qualifying setup and an actionable entry are not the same thing.

Every finalist must be placed into exactly one of these live states at the moment the alert is generated:

1. **BUY NOW**
   - every final A+ gate passes
   - a fresh current price/quote is available at alert time
   - current price is at or above the breakout trigger
   - current price is no more than 0.50% above the breakout trigger
   - the breakout remains structurally valid and has not failed back below the trigger
   - reward/risk remains >= 2.0:1 using the actual live entry price

   Mandatory user-facing format:
   `BUY [TICKER] NOW`
   `BUY BETWEEN $X.XX AND $Y.YY`
   `AFTER PURCHASE, ENTER SELL STOP AT $S.SS`
   `IF PRICE RISES TO $T.TT, MOVE SELL STOP TO $P.PP`
   `DO NOT BUY ABOVE $Y.YY`
   `Current price: $...`

2. **WAIT — breakout trigger not reached**
   - setup quality is otherwise acceptable
   - current live price remains below the breakout trigger
   - the stock has not already broken out and failed

   Mandatory user-facing format:
   `WAIT — DO NOT BUY [TICKER] YET`
   `BUY ONLY IF PRICE REACHES $X.XX`
   `VALID BUY RANGE: $X.XX TO $Y.YY`
   `IF BOUGHT, ENTER SELL STOP AT $S.SS`
   `IF PRICE THEN RISES TO $T.TT, MOVE SELL STOP TO $P.PP`
   `Current price: $...`
   `DO NOT BUY BELOW $X.XX`
   `DO NOT BUY ABOVE $Y.YY`

   WAIT is not a buy recommendation and must never be shortened to BUY NOW. Do not show STOP-LIMIT or LIMIT jargon in the main signal.

3. **NO TRADE — entry missed / breakout failed**
   - the breakout trigger was reached earlier, but current live price has fallen back below it, OR
   - price is already more than 0.50% beyond the allowed chase band, OR
   - the live structure/R:R no longer satisfies the A+ entry rules

   Mandatory user-facing output:
   `NO TRADE — entry missed / breakout failed. DO NOT BUY.`

4. **NO TRADE — no A+ setup**
   - no finalist passes the complete live A+ setup requirements.

   Mandatory user-facing output:
   `NO TRADE — no A+ setup. DO NOT BUY.`

### Mandatory live-price validation
Immediately before any `BUY [TICKER] NOW` alert is written, Engine 4 must fetch a fresh current price/quote and record its timestamp in the audit artifact. Historical opening bars, an earlier intraday high, or the fact that the trigger was touched at some earlier time may never substitute for this final live-price check.

A lower price than the breakout trigger is NOT automatically a better entry. Engine 4 is a breakout/momentum setup: the trigger is evidence of confirmed strength. If current price is below an already-triggered breakout level, the original setup may have failed and must not be relabeled as a bargain entry.

## Entry / stop / management
- Entry trigger: opening-range high + 0.05% confirmation buffer.
- BUY NOW is valid only when the fresh current price is at/above the trigger and no more than 0.50% beyond it.
- If current price is below an untriggered level: WAIT only.
- If current price is below a trigger that was already reached and then lost: NO TRADE — entry missed / breakout failed.
- Initial sell stop: just below strongest nearby VWAP/recent higher-low support.
- First management level: no lower than 2R; target logic may use the nearer of a 2.5R objective and identified overhead resistance only when at least 2R remains available.
- Do not chase beyond the allowed 0.50% breakout band.

### Locked deterministic profit-protection stop
The second stop must be fully calculable before purchase so the complete trade plan can be shown in the original signal.

Definitions:
- `REFERENCE ENTRY = breakout trigger`
- `R = REFERENCE ENTRY - INITIAL SELL STOP`
- `PRECALCULATED PROFIT STOP = REFERENCE ENTRY + 0.50 × R`

When price reaches the first management level shown in the signal, the instruction is:
`MOVE SELL STOP TO $P.PP`
where `$P.PP` is the precalculated profit stop above.

This rule intentionally replaces the prior subjective requirement to wait for a later confirmed higher low before moving the stop. The user must not be required to interpret chart structure after entry in order to know the next stop price.

The profit stop may only move upward; it may never be loosened below a previously active stop.

## Required user-facing timeline
The daily result must be understandable without opening code and must clearly distinguish natural counts from configured caps. Example format only:

`08:55:02 ET — PRE-SCREEN STARTED`
`09:03:41 ET — PRE-SCREEN COMPLETED`
`Baseline eligible: 1,870`
`Trustworthy price observations: 1,842`
`Naturally broad-qualified: 1,842`
`Nasdaq premarket enriched: 392`
`Nonzero premarket activity: 387`
`Strict-activity names: 74`
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
`RESULT: BUY ...`, `RESULT: WAIT ...`, or `RESULT: NO TRADE ...`

All numbers and times above are illustrative only. Production must display actual measured values.

## Regression notes — 2026-09-11
1. A reporting-integrity repair accidentally tightened natural qualification from “trustworthy premarket price observation” to “trustworthy price plus non-zero Yahoo premarket volume,” causing a false zero-candidate failure. That change was reverted.
2. Same-day diagnostics proved Yahoo extended-hours bars could return valid premarket prices while volume remained zero. Nasdaq's public extended-trading endpoint returned real premarket share volume for CRCL, NVDA and ORCL and is now the locked premarket-volume source.
3. Same-day diagnostics proved Yahoo Ticker.info / Ticker.news generated repeated 401/429 errors. Nasdaq quote data returned valid real-time bid/ask and Google News RSS returned current headlines. Those are now the locked production sources for spread and catalyst data.
4. A same-day test generated `BUY AAOI NOW` with a breakout trigger of $108.48 even though an independent live cross-check showed AAOI trading near $105.75–$106 at alert time. The failure was caused by treating an earlier qualifying breakout condition as though it were still an actionable live entry. SSOT v4.7 locked the live-price guard.
5. SSOT v4.8 locked simplified user-facing wording. The signal must communicate the action in plain English: `BUY NOW`, `WAIT — DO NOT BUY YET`, or `NO TRADE — DO NOT BUY`, with exact valid buy range boundaries. Broker order-type jargon must not be the headline instruction.
6. SSOT v4.9 locks the complete pre-calculated risk-management plan. Every BUY/WAIT signal must include the initial sell stop, first management level, and the exact profit-protection stop calculated at +0.50R from the breakout trigger once that management level is reached.

## Final output
If no ticker passes every final live mandatory gate:
`NO TRADE — no A+ setup. DO NOT BUY.`

If a setup is valid but the breakout trigger has not yet been reached:
`WAIT — DO NOT BUY [TICKER] YET`
`BUY ONLY IF PRICE REACHES $X.XX`
`VALID BUY RANGE: $X.XX TO $Y.YY`
`IF BOUGHT, ENTER SELL STOP AT $S.SS`
`IF PRICE THEN RISES TO $T.TT, MOVE SELL STOP TO $P.PP`
`Current price: $...`
`DO NOT BUY BELOW $X.XX`
`DO NOT BUY ABOVE $Y.YY`

If the trigger was reached earlier but the live price has fallen back below it, or the entry is otherwise stale/failed:
`NO TRADE — entry missed / breakout failed. DO NOT BUY.`

If one or more names pass every final gate AND the fresh live-price validation, rank the full-pass names and send only the strongest one:

`BUY [TICKER] NOW`
`BUY BETWEEN $X.XX AND $Y.YY`
`AFTER PURCHASE, ENTER SELL STOP AT $S.SS`
`IF PRICE RISES TO $T.TT, MOVE SELL STOP TO $P.PP`
`DO NOT BUY ABOVE $Y.YY`
`Current price: $...`

## Fail-safe rules
- Missing or stale required data => DATA FAILURE or NO TRADE as appropriate; never fabricated values.
- Missing frozen Top-25 => final stage must not pretend a normal full-cycle NO TRADE occurred.
- BUY NOW requires a fresh current-price/quote timestamp recorded immediately before alert generation.
- An earlier touch of the breakout trigger does not authorize a later BUY NOW if current price has fallen below the trigger.
- Below-trigger price before any valid breakout => WAIT, not BUY.
- Failed/reversed breakout or stale/extended entry => NO TRADE.
- Production stages must execute in order.
- Engine 4 is intraday only and must not silently become an overnight hold.
- Production alert is generated from Engine 4 output artifacts; ChatGPT relays it.
- Any report that conflates a configured cap with a natural pass count is considered a reporting failure and must be corrected before the result is accepted.
- Any code change that alters a screening criterion must be explicitly identified and approved in the SSOT; reporting-only fixes may not silently tighten or loosen trading criteria.
- A systemic free-provider outage must never be disguised as weak market conditions.
