I WILL NOW RUN THE FULL SCREEN AND FULL ANALYSIS AND NEVER TAKE A SHORTCUT.

# 30-Day Rocket Screen — Single Source of Truth (SSOT)

## Absolute governing rule — no shortcuts
This rule overrides speed, convenience, partial results, provisional rankings, and any temptation to infer completion from incomplete work.

Every official Rocket Screen run must execute the entire locked process from the beginning through the final verified ranking. No stage may be skipped, abbreviated, sampled, substituted, assumed, or declared complete without evidence that it was actually completed.

The assistant has no authority to shorten or bypass this process unless the user explicitly changes the SSOT. A quantitative shortlist is never permission to jump directly to a FINAL ranking. If any required stage is incomplete, the status must be stated as incomplete and no official #1/#2/#3 may be declared.

## Objective
Identify the U.S.-listed stock(s) with the strongest probability-weighted setup for a gain of roughly +10% over the next ~30 days, without pretending that unavailable or unverified data has been checked.

## Non-negotiable quality rule
No stock may be labeled the official FINAL #1/#2/#3 unless the broad eligible universe has been systematically processed through the quantitative funnel and the surviving candidates have then been verified with fresh/current company-specific information.

A market-wide quantitative score is not a FINAL recommendation.

## Funnel
1. Build the broad U.S.-listed common-stock/ADR universe.
2. Remove ETFs, test issues, warrants, rights, units, preferreds, obvious SPAC/acquisition shells and other non-common-stock structures.
3. Obtain market-wide price/volume history and calculate investability metrics.
4. Require basic investability: price >= $3, average dollar volume >= $2M/day, market cap >= $200M.
5. Score every sufficiently supported eligible stock under three independent quantitative lenses.
6. Apply a data-quality/confidence gate. Missing secondary information reduces confidence; it must not be silently converted into favorable evidence.
7. Narrow to approximately 100 semifinalists and then approximately 20-30 quantitative candidates.
8. Perform deeper current research only on the narrowed candidate set: latest earnings, guidance, estimate revisions, beat/raise execution, identified catalysts, financing/dilution, binary/regulatory risk, downside, valuation/runway, and current technical condition.
9. Narrow to a small finalist group and compare directly.
10. Only after current verification may #1/#2/#3 be labeled FINAL.

## Three quantitative lenses
### 1. Leadership / Momentum
Looks for sustained relative leadership, healthy intermediate momentum, sector/industry strength, growth quality, liquidity and reasonable valuation/runway.

### 2. Beaten-Down / Reversal
Looks for meaningful drawdown combined with improving short-term trend, volume confirmation, fundamental support and adequate liquidity. A falling stock is not rewarded merely for being down.

### 3. Acceleration / Emerging Momentum
This replaces the old misleading market-wide label `fresh_catalyst_acceleration`. At scale the engine is detecting the *fingerprints* of an emerging move: acceleration in returns, abnormal volume, improving growth/earnings characteristics, sector/industry confirmation and relative strength. It does NOT claim a catalyst has been found.

A real catalyst is researched only after the universe has been narrowed.

## Market-wide data that may be used
Use only information that can be collected consistently enough across thousands of securities:
- price and volume history
- dollar liquidity
- market cap
- revenue growth
- earnings growth / quarterly earnings growth where available
- valuation where available
- analyst target information where available
- sector and industry classification
- sector/industry relative performance
- SPY-relative performance
- drawdown, reversal, moving-average position and volatility

Earnings dates may be used when reliably obtainable, but their absence must not eliminate an otherwise well-supported stock.

## Missing-data rule
Core investability data is mandatory. Secondary fields are optional.

Do not fill missing secondary factors with arbitrary low/medium scores and then treat them as actual evidence. Scores must be calculated from available factors with weight re-normalization, and each stock must receive an explicit `data_confidence` score.

A stock with insufficient factor coverage cannot advance, even if the few available factors look strong.

## Catalyst rule
No catalyst found does NOT automatically eliminate a stock.

- Confirmed positive catalyst: positive evidence in finalist verification.
- No identifiable catalyst but exceptional quantitative/fundamental evidence: may remain eligible, with no catalyst bonus.
- Catalyst information unavailable/ambiguous: uncertainty penalty, not automatic rejection.
- Negative catalyst: may eliminate the stock.
- Thesis depends on a binary clinical/regulatory event: normally eliminate under the risk rules.

## Risk rules
Automatically flag obvious high-risk categories where possible, but do not pretend automated labels are exhaustive. Finalist verification must explicitly test:
- predominantly binary clinical/regulatory dependence
- financing/dilution risk
- shell/SPAC-like characteristics
- extreme crypto-proxy/speculative dependence
- deteriorating guidance/fundamentals
- whether negative price action is fundamentally justified
- excessive extension/volatility
- downside relative to the expected ~30-day opportunity

## Freshness rule
A new full run must not silently reuse stale fundamentals. Cached/checkpoint fundamentals need retrieval timestamps and a defined expiration. Stale rows must be refreshed.

## Relative-strength rule
Use both SPY-relative strength and peer context. Sector-only comparison is insufficient; industry strength should be used when enough peers exist.

## Final research requirements
For EACH quantitative candidate considered for FINAL ranking, complete the full checklist below with fresh/current evidence before comparing finalists. Do not perform a lighter review on some candidates than others.
- latest earnings and reported operating trends
- latest guidance and any change in guidance
- earnings/estimate revisions when available
- beat/raise execution history
- credible catalyst relevant to the next ~30 days, if one exists
- current price/technical condition and whether extended
- sector/industry strength
- valuation/runway
- downside/risk
- financing/dilution or special-situation risk
- whether recent negative price action is fundamentally justified

Every surviving candidate must have its verification status recorded. A candidate with an unfinished checklist cannot be used to justify a FINAL ranking.

## Auditability
Every full run must save:
- starting universe
- price metrics
- investable universe
- fully scored universe
- semifinalists
- quantitative candidates requiring current verification
- audit JSON containing row counts, lens names, data-confidence thresholds and freshness settings

The audit must explicitly state `FINAL_LABEL_ALLOWED: false` until the separate current-verification stage has been completed for the full candidate set and the final comparison has been documented.