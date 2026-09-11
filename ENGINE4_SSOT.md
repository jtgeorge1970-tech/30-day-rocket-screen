# Engine 4 — Intraday Perfect Setup SSOT

## Golden Rules
1. Never guess or assume.
2. No shortcuts or skipped steps.
3. Follow the SSOT exactly.
4. Verify before reporting completion.

## Objective
Engine 4 is a separate intraday/day-trading engine. Engines 1–3 remain unchanged. Engine 4 does not force trades. Zero trades for multiple days is acceptable.

## Operating schedule (Eastern Time)
- 8:55 AM: start premarket stage.
- 8:55–9:05: broad objective elimination pass.
- 9:05–9:18: deep score survivors.
- 9:18–9:25: refresh, rerank, freeze Top 25.
- 9:30: market open.
- 9:30–9:45: allow opening structure to form.
- 9:45: final live scan on frozen Top 25 only.
- Target final alert by 9:48.

## Eligible universe
- NYSE/Nasdaq U.S. common stocks and ADRs.
- Price >= $5.
- Market cap >= approximately $300M.
- Adequate liquidity.
- Exclude OTC, ETFs, CEFs, BDCs, preferreds, warrants, units, and obvious thin/microcap/pump-type names.

## Premarket hard disqualifiers
Reject before final ranking when data shows:
- poor liquidity,
- excessively wide spread,
- negligible premarket participation,
- insufficient intraday range,
- bizarre/parabolic gap with no clean setup potential,
- major nearby resistance destroying reward/risk,
- promotional/pump risk.

## Premarket 100-point score
- Catalyst quality: 25
- Relative premarket volume: 20
- Premarket price behavior / gap quality: 15
- Liquidity / dollar volume: 15
- Room to resistance: 10
- Volatility / ATR suitability: 5
- Sector + market relative strength: 5
- Execution quality / spread: 5

The Top 25 must be the highest-scoring serious candidates, not random names, not first-returned names, and not a simple top-gainers list. A minimum-quality floor applies. No single flashy metric may compensate for broad weakness.

## Final 9:45 A+ gates
A trade must pass all mandatory gates:
- clear relative strength versus SPY/QQQ and preferably sector,
- holding/reclaiming VWAP,
- no lower-low deterioration,
- clean higher-low or tight consolidation,
- attack on opening-range high or obvious breakout level,
- pullback volume contraction,
- breakout volume expansion,
- liquid execution / acceptable spread,
- obvious technical stop,
- no immediate resistance problem,
- at least 2:1 potential reward/risk before entry,
- not extended too far from VWAP,
- no giant first candle followed by collapsing volume,
- no promotional-looking move,
- reject if broad market reverses sharply against setup.

Premarket rank only gets a stock into the arena. Live structure decides the winner. A lower-ranked premarket stock may become the trade.

## Final output
Exactly one of:

NO TRADE — no A+ setup.

or

BUY [TICKER] NOW
Entry/trigger: exact level
Initial stop: exact level
First management level: exact level
Trailing stop: activation rule if runner
Reason: one short sentence

If the entry is already missed/extended: NO TRADE — entry missed.

Do not list rejected tickers or near-misses in the user-facing alert. Do not chase. Do not convert the day trade to an overnight hold.

## Runner / trailing-stop rule
Use the defined initial stop first. Only transition to a trailing stop after continued strength confirms a runner. Trail under a fresh intraday higher-low/VWAP support structure rather than using an arbitrary tight percentage.

## Data-source rule
Use the existing free Rocket data stack first. Reuse Yahoo/yfinance and Alpaca-free capabilities where appropriate. Do not introduce a paid data source unless a specific required field is proven unavailable/reliably inadequate from the free stack.

## Fail-safe rule
Missing, stale, late, or untrustworthy data must fail closed to NO TRADE. Never fabricate a candidate or send a stale BUY alert.
