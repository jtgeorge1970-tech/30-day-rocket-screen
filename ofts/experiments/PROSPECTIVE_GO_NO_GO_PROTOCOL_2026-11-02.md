# OFTS prospective GO / NO-GO holdout protocol — frozen 2026-11-02

**Pre-registration date:** 2026-11-02, after NYSE close. **First eligible untouched cohort:** 2026-11-03. **Last in-sample reference:** durable state commit `6593b68b8f474142d5cf239e59ff0b1642b8f016`. **Original v2.3 model hash:** `a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b`.

This is a research-only, prospective protocol. No changes to production scoring, no retrospective reclassification, no brokerage orders. Any modifications to this protocol must create a *new* version and reset its prospective holdout clock; do not backfill revised rules into earlier cohorts.

## Universe and provenance

- Every original daily frozen `signals/YYYY-MM-DD.json` and `predictions/YYYY-MM-DD.json` cohort, including rejected candidates and data-ineligible rows, is immutable once qualified. Keep all signal states, exact scores, model hashes, universe membership, exclusions, and data provider failures. Preserve delisted/merged names; flag unavailable prices rather than silently dropping them.
- Independent 50-chart audit is a *separate* model and is not a substitute for daily v2.3 signals.
- A cohort counts only if the date, NYSE session, minimum selected freshness, required-symbol freshness, saved artifact, remote SHA and recomputed audit are verified.
- For any missing or stale price, record `NO_EXECUTABLE_DATA`; never fill with stale bars or claim zero return.

## Primary unit: executable completed trade

- A BUY signal is known only after that session's close. Primary entry is the **next NYSE session's open**, but only count it as executable if independent consolidated trades/quotes establish an attainable size-aware entry (not simply an auction print). Primary exit follows the original next-open SELL, subject to a separately frozen stop rule.
- Keep a no-stop baseline; separately test 5%, 10%, 12% fixed stops, each gap-aware, and 7/14-calendar-day reentry cooldowns. Never choose a winner after seeing holdout results.
- For each signal record LOW/MEDIUM/HIGH confidence, original score band (<40, 40-60, 60-80, >=80), cycle timing, liquidity, spread, and expected holding window *as of signal time*. No future data for classification.
- Compute equal-dollar, no-leverage, capital-constrained portfolio returns as well as equal-trade returns. Account for concurrent open positions, available cash, trading calendar, turnover, gap fills, dividends/corporate actions, and realistic transaction costs.

## Matched controls and costs

- Compare the same stock on the same signal dates using (a) next-session opening execution, (b) first independently observed executable ask after 9:35 AM ET, (c) one-session-delayed opening entry. For same holding-period comparisons, shift the exit by the same elapsed number of trading sessions; additionally report the common-exit comparison separately, labeled shorter exposure.
- Compare the same stock to pre-specified non-signal entry dates (all eligible weekdays within the preceding 20 sessions) at *identical 5/10/20/30/60-session horizons*, with calendar-date effects and multiple comparisons disclosed. Same-stock buy-and-hold on the *identical entry and exit* is an identity check, not independent evidence of timing skill.
- For each signal, compute SPY and IWM price and total-return comparators using matched entry/exit timestamps and cash exposure; clearly distinguish price-only from dividend-adjusted returns.
- Base execution cost must use observed spread, fees and slippage at a pre-specified order size. Separately stress **0.20%, 0.50%, 1.00%, 2.00%** round-trip costs; mark unavailable executable quotes as missing, never as free fills.
- Report 5/10/20/30/60-session fixed horizons separately from completed BUY-to-SELL trade returns. Account for overlapping observations via date- or symbol-block resampling, not naive independent-sample standard errors.

## Decision gates

No GO decision until at least **100 non-overlapping completed prospective trades**, **60 NYSE trading sessions of forward observation**, and all five horizon families have some matured observations. These are conservative research minima, not guarantees of statistical power. Additional sample is required if concentration, clustering or confidence intervals remain unresolved.

GO requires **all**: (1) positive after measured executable costs, with 1% cost stress nonnegative; (2) advantage over same-stock pre-specified timing controls and matched SPY and IWM after costs, with uncertainty assessed by blocked resampling; (3) capital-constrained maximum drawdown **at most 20%** and no unexplained loss beyond **20% per position**; (4) no dominance by one or two extreme winners; (5) reproducible frozen signals, eligible quotes and immutable ledger; (6) enough truly independent trades for stable inference. The risk thresholds are provisional conservative research gates; changing them prospectively requires a new protocol version.

NO-GO / move on if, after sufficient prospective observations, the strategy has nonpositive net returns after realistic costs, fails matched-stock/market benchmarks, exhibits unacceptable tail loss or drawdown, or cannot achieve reliable executable fills. If 100 independent completed trades cannot be accumulated after six months, report that the sample remains inadequate and recommend against deployment rather than extending indefinitely without a decision.

**Current status at protocol freeze: RESEARCH_ONLY_NO_GO.** Four completed hypothetical trades have all lost money. Earlier favorable scored averages are overlapping observations, not executable profitability.
