# OFTS daily operation and persistence SSOT

Locked by Joseph's instructions on 2026-10-09: make OFTS functional, score
stocks each market day, save and reuse the data, and validate predictions
across many stocks. Joseph independently chose his HLIT purchase; it is not
an assistant-executed order and is not the sole system validation sample.

## Authority and scope

This addendum locks operational controls. It does not change the existing
v2.3 research formula or represent it as locked v2.2 production scoring.
`research/v23_replacement.py` and `research/candidate_components.py` remain
the scoring implementation. Save their combined SHA-256 with each cohort.
Research quality scores are not executable BUY or SELL signals. No brokerage
actions are authorized by this process.

## Required daily cycle

1. Restore the durable `ofts-daily-state` branch. A read failure is a failure,
   not permission to silently reset the ledger. Confirm prior predictions are
   present before continuing. An initial empty state is allowed only when the
   remote branch genuinely does not exist.
2. Determine the latest completed NYSE session using its holiday/early-close
   calendar and a 30-minute data availability delay. Refresh the existing top
   25 watchlist plus 100 rotating universe positions in stride-137 order.
   Also refresh retry symbols and symbols with pending forward observations.
   The 100-symbol batch is an implementation setting, not a scoring rule.
3. Save valid historical rows atomically, keyed by symbol and date. Refresh
   recent history even for previously downloaded symbols. Retry empty/failed
   responses. Count only verified current-session data as fresh. Exclude stale
   data from current scoring. Preserve prior history on a provider error.
4. Run the unchanged research scorer. Record actual symbols, data dates,
   scores, classifications, model hash and UTC recording time. Freeze the first dated cohort, including failure classifications; subsequent
   price movement must not rewrite it. Repeated attempts go into a separate
   immutable attempt audit; failed observations are not backfilled as predictions.
5. Evaluate earlier cohorts at 5, 10, 20, 30 and 60 trading sessions. These
   horizons are research measurements, not newly validated exit rules.
   Use next-session open as hypothetical entry; a cohort recorded after that
   open is NOT prospective. No filling future outcomes before they exist.
   Report missing sessions and corporate actions explicitly.
6. Save history, cursor, retries, predictions, outcomes, and readable report to
   the durable branch. Push successfully and verify remote HEAD equals the
   saved commit before reporting a completed cycle. Cache/artifacts are backup
   conveniences, not the authoritative permanent record.
7. Report counts, symbols, scores, data date, matured/pending results and exact
   failures. A configured schedule, successful download attempt, or green
   scoring step is not evidence that persistence and reuse succeeded.

## Validation accounting

Forward measurements are hypothetical long price returns excluding dividends;
the initial explicit cost assumption is 0.20% round trip. Do not call them
realized user profits, a stop/target strategy backtest, or validated trade
recommendations. Compare same-period SPY price returns when available.
Keep score groups, horizon, and model version separate. Overlapping cohorts
are correlated; do not treat them as independent trades or claim portfolio
drawdown from per-observation adverse excursion. Current historical holdout
reports remain separate and retain their limitations, including that an
independent untouched dataset has not been established.

## Acceptance gate

Tests must cover restart/reload, adding a new session, deduplication, failed
download recovery, immutable predictions, no premature outcomes, entry timing,
and corporate-action/missing-session exclusions. Production operation is not
verified until an actual run saves state remotely and a subsequent run restores
that state and preserves prior predictions. Record that evidence; do not claim
the gate passed solely because this document or a schedule exists.

## Ownership

Continue routine refresh, recovery, persistence and reporting without waiting
for Joseph to remind the assistant. If access or data prevents a required step,
report the precise blocker and preserve all prior evidence. Never silently
substitute stale data, invent scores, mix versions, or reset progress.


## LOCKED — ASSISTANT-OWNED AUTOMATION CAPACITY AND PROACTIVE REPORTING (2026-10-09)

- The assistant owns the task/automation slots used to supervise OFTS and other assistant-operated projects. Never ask the user to choose which task to pause, remove, or replace when task capacity is full.
- Reuse, consolidate, or reconfigure an existing assistant-owned automation where possible. Handle task-slot housekeeping without user intervention; do not disable unrelated essential tasks merely to create a duplicate.
- Proactively deliver verified OFTS progress and material blockers without waiting for the user to chase results. Include stage checklist, dated selection and scores, counts, post-audit results, precise failures, corrective actions and direct evidence links. Deduplicate unchanged reports.
- A GitHub green check is not evidence of trading profitability or complete validation. Keep immutable forward predictions and score/cycle-based audits as acceptance gates.
- If a task-capacity error occurs, do not ask the user to manage slots; inspect existing tasks and update a relevant one.

## LOCKED — POINT-IN-TIME SIGNALS AND CYCLE AUDITS (2026-10-10)

- Save one explicit research state for every selected symbol after the completed-session close: BUY, SELL, or NO_TRADE with a reason. Missing labels fail the completeness gate.
- A BUY or SELL state may be created only when the latest pivot becomes confirmed using bars available by that close. Hypothetical execution is the next session open; never use the eventual pivot date as an executable price.
- Preserve partial or failed signal snapshots. A repaired same-session snapshot must use a separate immutable qualified file rather than overwrite history.
- Cycle profitability is measured from next-open BUY execution to next-open execution after a later confirmed SELL state. Record holding sessions, gross return, 0.20% assumed round-trip cost, adverse/risk-rule outcomes, and captured percentage of the available pivot swing.
- Keep fixed 5/10/20/30/60-session audits and cycle BUY-to-SELL audits separate. Neither may replace the other.
- Compare fixed forward outcomes with same-period SPY. If benchmark history is unavailable for an older research cohort, disclose the missing comparison instead of estimating it.
- Historical simulation, a positive mean, or a green workflow does not authorize a production trade. Report sample size, median, outlier dependence, losses, and confidence alongside any average gain.
- Rebuild the permanent cycle ledger deterministically from immutable signal snapshots on every run. A signal is not filled until its next-session opening bar exists; restarts must not duplicate positions or trades.
- Keep pending and open-position symbols in the refresh queue until a later frozen SELL can be executed. Record SPY open-to-open return, excess return, adverse excursion, observed ordered swing, captured swing, and missed swing for each completed trade.
- Compare fast (1–10 sessions), medium (11–25), and slow (>25) entry-cycle classes separately. Alongside raw net return, report capital-time efficiency as total net percentage return divided by total holding sessions and scaled to 20 sessions; label it descriptive, not annualized or a portfolio return.

## LOCKED — CHART-CHALLENGE / RANKING ROBUSTNESS AUDIT (2026-10-10)

Trigger: manual review of 2026-10-09 #1 research-quality symbol AKAM (62.584, 32-session estimated cycle, 18.11% median pivot swing, MEDIUM confidence, NO_TRADE). User-supplied 1Y/1M/intraday charts show an irregular large price jump, extended decline and one-day rebound; chart observation is not an independently computed historical test.

- Never equate the top **quality** rank with a current BUY. Keep separate fields: historical oscillation quality, recent repeatability/regime stability, and point-in-time entry readiness.
- Current v2.3 research formula blends 75% full-history quality and 25% last-90-bar quality; this can reward stale or discontinuous historical patterns. Treat this as a hypothesis to test, not a proven AKAM-specific cause.
- Add an independent, **non-retroactive** ranking robustness audit for each top-25 name: count recent complete peak-to-peak and trough-to-trough cycles, compare recent vs older cadence/amplitude, quantify largest-event/outlier dependence, distinguish abrupt one-off repricing from repeated turns, measure confirmed-entry lag and missed swing, and flag regime breaks. Mark insufficient evidence rather than inventing cycles.
- Audit ranking stability and outcomes on frozen future cohorts, with separate fast/medium/slow groups and missed-opportunity controls. Record failures and rejected candidates. No cherry-picking of only visually attractive winners.
- Any new score weights or hard gates must be versioned as an experimental challenger, backtested chronologically against untouched holdouts, and never silently overwrite frozen v2.3 scores. Do not present any challenger as production approved until it demonstrates forward net performance.
- For AKAM as of 2026-10-09, current saved signal is NO_TRADE; no automatic purchase recommendation is authorized.

## LOCKED — YDES CHART CHALLENGE AND ENTRY-CHASE AUDIT (2026-10-10)

Trigger: user-supplied YDES brokerage charts as of 2026-10-09 showing +16.23% one day, -17.02% five days, +58.35% one month and -60.55% one year; 5-minute chart shows a rapid intraday rebound. These are user-supplied chart readings, NOT independently verified market-data bars. The existing frozen research BUY state is score 44.611, estimated cycle 12 sessions, 32.36% median historical swing, LOW confidence, hypothetical next-open entry only.

- Keep the original 2026-10-09 BUY research observation immutable and include its hypothetical future result even if the setup proves bad. Do not rewrite the signal as NO_TRADE or remove it from the denominator after seeing price action.
- A newly confirmed low reversal is not sufficient evidence for an attractive entry. Independently report point-in-time latest-session return, trailing 5-session return, distance above the most recent confirmed low, and confidence. Flag abrupt rebound/chase risk and low-confidence cycles as *research warnings*; never silently change locked v2.3 scores.
- Audit next-session opening gaps, next-open fill price, slippage sensitivity, maximum adverse excursion, and whether entry occurred after most of the rebound. Include failures, missed entries and stopped-out outcomes.
- Test any candidate BUY rejection thresholds prospectively and on chronological untouched holdouts before adoption. A hard-coded retrospective filter chosen after seeing YDES is prohibited.
- Research BUY is NOT a production recommendation or brokerage authorization. Current forward cycle ledger must remain intact.


## LOCKED — SCORE INTERPRETATION AND ACTIONABILITY GATE (2026-10-10)

- The v2.3 research quality score has a mathematical 0–100 scale because each component is clamped to 0–100 and the component weights sum to 1. A theoretical ceiling is not evidence that 80, 60, 40, or any other cutoff predicts profit.
- There is currently no validated numeric BUY threshold. A quality score measures historical oscillation structure; BUY/SELL/NO_TRADE is a separate point-in-time reversal state.
- The daily report must show the actual observed score range and distribution, state that the validated BUY threshold is NONE, and keep the system actionability gate at RESEARCH_ONLY_NO_GO until Stage 8 out-of-sample predictive validation passes.
- Never convert a research score or research BUY state into a production recommendation merely because it is the highest available result. If the evidence gate fails, say plainly that OFTS is not ready to select production winners.

## LOCKED — VERIFIED IQMX SPAC/SECURITY IDENTITY BREAK (2026-10-10)

Evidence: Nasdaq announced IQM Quantum Computers ADS began trading under IQMX on **2026-07-02** after the RAAQ business combination:
https://www.nasdaq.com/press-release/iqm-quantum-computers-and-real-asset-acquisition-corp-complete-combination-trading
The full-universe worker run 38008125845 reported **IQMX 340 bars, 77.597 score, rank #1**. It is impossible for 340 daily IQMX post-combination bars to exist between July 2 and the Oct 9 scoring date. Historical bars must be treated as spanning different security regimes until audited. Do not claim they all belong to the current operating-company ADS.

**Effective immediately:** IQMX historical oscillation scores blending pre-2026-07-02 and post-2026-07-02 bars are INVALID for current ranking. Do not present 77.597 as a valid candidate score or production BUY. Source of the old result remains preserved for audit. The existing October 9 immutable snapshots are NOT rewritten.

- New code: `ofts/research/security_regimes.py` records verified event boundaries and excludes predecessor bars from both full-universe research and future daily candidate scoring.
- Apply the same >=180 usable daily bars gate **after** identity-boundary filtering. If too few, mark `INSUFFICIENT_POST_REGIME_HISTORY`, numeric score null, NO_TRADE; retain raw count, post-event count, effective date and source. Do not fabricate older operating-company history.
- All new candidate rankings must include a security-identity/merger/corporate-action integrity audit, not just a symbol match. The current dated boundary registry is **not comprehensive**; other SPAC, IPO, ADR, ticker-reuse and major structural-event histories may remain contaminated. Broaden verified coverage systematically.
- Version new model snapshots with identity-gate source; do not retrospectively reclassify frozen observations, and compare old/new cohort results separately.
- Full-universe identity-gated rescore was VERIFIED in run **38046200050** against the original saved history: **5,502** symbols, **3,977** numeric research scores; IQMX **340 raw/68 post-event bars**, status **INSUFFICIENT_POST_REGIME_HISTORY**, score withheld. Provisional new research #1 **SCYX 67.197**, with **zero scores >=80**. Saved Top 25: `ofts/validation/full_universe_identity_rescore_2026-10-10.md`. Because the identity registry is not comprehensive and forward performance is unvalidated, **NO VALIDATED OVERALL BUY LEADER**.

## LOCKED — LAST FOUR SWINGS AND LOWER-HIGH/LOWER-LOW STRUCTURAL RISK (2026-10-10)

User-directed correction: A good long-history oscillation score alone does NOT warrant an entry. OFTS must read the latest price swings for **continued regularity, shrinking/dissipating amplitude, and deterioration of both highs and lows**.

Two independent research dimensions are now implemented in `ofts/research/swing_health.py`, **experimental v0.1**:

1. **Recent stability / decaying oscillation:** On the last 90 daily closes, identify only **confirmed** alternating pivots using the existing adaptive percentage-reversal threshold; show the **last four completed legs** with direction, start/end bar, amplitude percent and duration. Require at least 3 confirmed highs, 3 confirmed lows, 4 completed legs. Compare last-four amplitude and duration median absolute deviations; if relative MAD amplitude >35% or duration >45%, flag `IRREGULAR`; if last-four median amplitude <70% of the preceding four legs, flag `DECAYING`. When insufficient recent cycles, mark `INSUFFICIENT`, **not** `STABLE`. These are provisional screening hypotheses, NOT empirically calibrated cutoffs.
2. **High/low structural deterioration:** Compare the last **three confirmed highs** and last **three confirmed lows** separately. Two successive lower highs **AND** two successive lower lows = `DOWNTREND` risk; mixed structure is not a confirmed breakdown. A lower-high/lower-low series does **not** automatically prohibit a profitable swing. Add stronger caution for an abnormally weak confirmed rebound relative to preceding rising legs. Always distinguish weakness risk from swing tradability.
3. **Experimental proposed entry:** `DECAYING`, `IRREGULAR`, `INSUFFICIENT` and `DOWNTREND_WEAK_BOUNCE` => `NO_TRADE`; other recent patterns => `REVIEW` (NOT BUY). Report high and low progression and the precise reason. No positive production entry state is issued by this diagnostic.
4. **Audit safeguards:** Keep locked v2.3 scores, original research BUY/SELL state and historical frozen cohorts **unchanged**. Record `swing_health` independently on NEW daily frozen cohorts; add swing fields to full-universe worker output. Include this new module in the daily model hash, add deterministic tests, and retain all original losers, rejected candidates and no-trades in subsequent forward report cards.
5. **Validation before promotion:** Evaluate new v0.1 gates against the same chronologically held-out future cohorts and original unfiltered baseline, reporting trade count, average and median net returns, worst adverse excursion, avoided failures **and missed winners**, SPY comparisons and sensitivity to gate cutoffs. Do not promote experimental gate to the official BUY/SELL execution ledger until proven.

Current standing: implemented as **research challenger**, not verified predictive edge, and not a production BUY engine. No score threshold, including 80, is validated as profitable.

## LOCKED — FOOL'S-GOLD RECENT-SWING ECONOMICS (2026-10-10)

**User-detected failure mode:** Two or three huge historical swings inflate the arithmetic average and volatility score, while the **last several completed swings are tiny**. Such symbols waste review time despite attractive old average returns. Historical amplitude and volatility are NOT evidence that recent swings are economically worth trading.

Implement independent **experimental recent-viability v0.2** without silently changing the v2.3 quality score, original frozen research BUY/SELL states, or the v0.1 major-pivot structural trend diagnostic:

- Reconstruct point-in-time, **confirmed** alternating minor pivots over up to 252 daily closes, using a 2.5%–3.5% minor diagnostic threshold **separate** from the major 6%–16% v2.3 pivot threshold. This prevents the major detector from simply hiding recent 3%–5% swings. Apply the same minor threshold to both older and recent swings.
- Save every recent leg's **direction, amplitude and duration**. Explicitly display **last-three completed swing median**, **last-two UP-leg median**, prior-swing median, historical **mean** and median, top-two historical swing share, recent/older ratio, age of most recent confirmed pivot, and hypothetical captured upside after costs.
- Do **not** substitute large DOWN legs for BUY-side upside. Experimental economic hurdle: assume only 50% of the last-two UP-leg median can be captured, less 0.20% round-trip cost; require at least 2.50% modeled net opportunity (equivalent to **5.4%** gross recent UP swing). These are **provisional hypotheses**, not validated capture estimates or promised returns.
- Flag `FOOLS_GOLD` when old top-two outliers represent at least 45% of observed swing movement **and** the median of the last three legs is below 60% of the earlier median. Flag `TOO_SMALL` when last-three median is under 5.4% gross; `FADING` when recent/older median is below 60% or recent legs shrink consistently; `TOO_SMALL_UPSIDE` when last-two UP legs fail the provisional modeled net hurdle; `STALE_SWINGS` when recent pivots are old; `INSUFFICIENT` when recent/prior legs are too few. All issue **experimental NO_TRADE**, never a production SELL or advice.
- `REVIEW` requires v2.3 `CANDIDATE` gate, v0.1 swing-health `REVIEW`, **and** v0.2 recent-viability `REVIEW`. This is a **research-only current-swing shortlist**, not an official BUY, and is saved separately from the full universe and original ranking. Do not throw away the rejected names; retain reasons and future results to measure both avoided losses and **missed winners**.
- Backtest on chronological, embargoed holdouts and forward snapshots with the original unfiltered baseline, including frequency of candidates, capture assumptions, spread/slippage sensitivity, missed winners, outlier influence, false rejections, 5/10/20/30/60-session returns and SPY. Tune thresholds only on training data, freeze before untouched evaluation, and promote nothing without verified out-of-sample improvement.

Code: `ofts/research/recent_viability.py`, `ofts/test_recent_viability.py`, full-universe `ofts/worker.py` and prospective daily `ofts/daily.py`. Research challenger, not proven profitability.

## LOCKED — REPEATED MINIMUM CURRENT UP SWING, EXPERIMENTAL v0.3 (2026-10-10)

User correction to v0.2: **A current average is insufficient.** Report actual percentages for the **three latest separately confirmed UP swings** and require repeated economic amplitude. A 15%, 12%, 4% sequence fails even if its average is high.

- Starting research-only floor: **5.0% gross for EACH of the latest three completed UP legs**. All **3 of 3** must reach 5% for v0.3 `REVIEW`; **2 of 3** is `WATCH` with proposed `NO_TRADE`; **0–1 of 3** is `TOO_SMALL_UPSIDE` / `NO_TRADE`. The **most recent** UP leg below 5% is independently `NO_TRADE` regardless of mean.
- Require three fully confirmed UP legs. If fewer, `INSUFFICIENT_UPSIDE`; if latest completed UP leg is older than 45 sessions, `STALE_UPSIDE`. Keep earlier v0.2 last-three-all-legs median, historical outlier, shrinkage and net-capture hurdles, which may reject an otherwise 3/3 passing pattern.
- Save exact `last_three_up_pct` (chronological oldest→newest), `last_up_pct`, `repeated_up_pass_count`, `up_progression` (shrinking/growing/mixed), and hypothetical net capture. Never infer buyability from large DOWN legs or historical averages.
- **No untested numeric gate is permanent:** compare floors 5/6/7/8% and 2-of-3 versus 3-of-3 repetitions on training then embargoed holdout / forward cohorts, with rejects, missed winners, SPY, costs, drawdown, trade frequency and cycle duration. Version all challenger changes; do not revise frozen cohorts or the original v2.3 score/BUY ledger. All states remain **RESEARCH ONLY**, no production trade recommendations.

### Experimental v0.3 — three repeatable recent UP swings, not generic HIGH/LOW (2026-10-10)

Require actual amplitudes of the **last THREE completed and confirmed UP legs** (not any three alternating UP/DOWN legs) to appear in the full-universe and daily outputs. Provisional minimum **5.00% gross per UP leg**; do not assume this is optimal. Independently show the count passing 5%, latest UP leg %, UP-leg progression and a named repeatability classification:

- `STABLE_3_OF_3`: all three most recent completed UP legs >=5%; eligible only for additional structural/recency/economic gates and `REVIEW`, **never** an automatic BUY.
- `WATCH_2_OF_3`: exactly two pass and the latest is >=5%; **NO_TRADE** pending stronger repeatability. Another blocker (e.g. most recent alternating swing median too small) may yield the more severe primary `state`, but the independent repeatability field must still say `WATCH_2_OF_3`.
- `UNSTABLE`: 0–1 of three pass, or latest UP leg <5%; **NO_TRADE** regardless of old average. `INSUFFICIENT`: fewer than three confirmed UP legs; **NO_TRADE**.
- Keep existing 5.4% median economic opportunity and 2.5% assumed net capture hurdles; passing 5% repetition alone does not override these or downtrend/dissipation risk. Confirmed pivot lag means this is a retrospective current-cycle quality filter, not a prediction of the next UP leg.
- Compare training-only candidates for 5/6/7/8% gross UP floors and repeatability 2-of-3 vs 3-of-3, using embargoed untouched chronological validation, missed winners, avoided losses, execution costs, SPY and all 5/10/20/30/60-session outcomes. **Do not promote or calibrate a score=80 BUY rule** without measured forward evidence.

### Experimental v0.4 — recent oscillation cycle clock is mandatory (2026-10-10)

User-identified issue: Three qualifying 5% upward swings six months apart are **not** a useful active oscillator. OFTS previously measured peak/trough timing as a **historical weighted component** and the daily cycle fingerprint, but did **not** require recent same-side pivot spacing as a current trade-readiness hard gate.

**New research-only timing gate:** Using the same confirmed minor pivots as recent UP swing amplitude, record the **last THREE peak-to-peak trading-session intervals** and the **last THREE trough-to-trough trading-session intervals**, requiring at least four recent confirmed peaks and four recent confirmed troughs. Each series must have median **10–40 trading sessions** (roughly 2–8 calendar weeks), every individual interval **8–45 sessions**, and relative median absolute deviation / median <=**0.35**. Both peak and trough checks must pass to issue research `REVIEW`. Otherwise issue `CYCLE_TIMING / NO_TRADE`, preserving actual intervals and reason. Existing v0.3 3-of-3 UP >=5%, freshness, economic viability, v0.1 stability and structural checks remain mandatory. **Do not substitute up-leg duration for full peak-to-peak cycle length.**

Cutoffs are experimental: test 10–20, 10–30, 10–40, and 10–50 session cycle ranges, stability cutoffs, forward capture, rejected winners and avoided losers on chronologically held-out cohorts before promoting. All original scores and frozen prior cohorts remain unchanged. No research `REVIEW` is an authorized BUY.

Implementation: `ofts/research/recent_viability.py` v0.4, regression tests, full-universe `ofts/worker.py` output, prospective `ofts/daily.py` snapshots and reports.

### Experimental v0.5 — adjacent three cycles versus preceding three (2026-10-10)

Chart challenge XPRO: one-year chart has many pronounced oscillations, but the most recent ones appear smaller and/or farther apart. Historical v2.3 quality (XPRO 60.623) and v0.4 passing three 5% rising legs + absolute 10–40-session cadence do NOT prove the oscillator remains as strong now.

Compare **three latest completed UP legs** with the **immediately preceding three UP legs**, using median amplitude ratio `recent/prior`. Compare last three **peak-to-peak** intervals with preceding three and last three **trough-to-trough** intervals with preceding three; median the two spacing ratios. Use only confirmed point-in-time pivots; retain actual six UP amplitudes and six peak/trough intervals in full-universe and daily reports. **Never use full-history average as the sole comparator.**

Provisional independent `NO_TRADE` dissipation veto if recent median UP amplitude is <**70%** of preceding-three median, OR recent combined peak/trough cadence >**150%** of preceding-three, OR UP amplitude <**85%** AND cadence >**130%** simultaneously. If any preceding group has <3 confirmed observations, `INSUFFICIENT_COMPARISON / NO_TRADE`; never silently pass missing history. Keep all existing 5% 3-of-3, cycle 10–40, fading, swing-health, freshness and net-capture gates; never rewrite original frozen scores/signals. This is an **experimental challenger**, not a verified predictive threshold or production BUY.

Audit XPRO against **actual underlying cached OHLC**, not screenshots alone. Save its six UP amplitudes and six peak/trough intervals, actual pass/fail reasons, chart observations vs calculated facts, and impact on 5,502-universe research shortlist. Test 0.6/0.7/0.8 amplitude and 1.25/1.5/1.75 cadence alternatives on untouched chronological holdouts with missed winners, avoided losses, costs, SPY and full 5/10/20/30/60-day outcomes before threshold promotion.


## LOCKED — ELIGIBILITY-ADJUSTED TRADING RANKING (2026-10-10)

Owner decision: do not publish a top-six trading list containing a stock with a known eligibility problem merely accompanied by an "eligibility risk" footnote. Eligibility and tradability must affect the actual ranking and top-N membership, and replacements must be selected from the next eligible scored candidates, not invented or hand-picked.

- Preserve original v2.3 research quality score unchanged. Introduce separate, versioned, experimental opportunity score (0–100) and eligibility/tradability score (0–100). Do not label hand-ranked watchlists as computed scores.
- Proposed opportunity components: recent UP-leg repeatability 25; upward swing magnitude 20; peak/trough timing consistency 15; health/deterioration 20; current entry position/readiness 15; execution/liquidity 5. Implement and validate every component before publishing a complete numerical score. The overlap with eligibility liquidity must be measured and reviewed before final weights are locked.
- Proposed adjusted ranking: opportunity_score * eligibility_score / 100, **only** when both inputs have been calculated from dated, sourced data. Unknown cap, dollar volume, spread, float, or data history must produce UNVERIFIED eligibility and must not silently receive a perfect score.
- Honor previously locked security type, $3 minimum price, and $200M minimum market capitalization as noncompensable hard gates until the owner explicitly changes them. A failed hard gate means INELIGIBLE, not merely a low but selectable score. If required market cap cannot be verified, status is PENDING_ELIGIBILITY, not PASS.
- For passing stocks, eligibility score should penalize thin dollar volume, poor spreads, unstable fills, or weak source/data reliability. Numerical scoring cutoffs are experimental and must be specified, tested, and documented before use.
- For the six v0.5 research survivors, INTS was flagged for possible small capitalization/illiquidity. Do **not** claim it is definitively ineligible without dated market-cap and trading-data verification; keep it off any *verified eligible* top six until checked. The replacement sixth ticker must be found through a full-universe eligibility-aware run. The original six were a research shortlist, not a verified trading top six.
- Preserve original frozen cohorts and audit both admitted and rejected names (false-negative opportunity cost), using dated as-of market-cap/liquidity snapshots, next-session entry, costs, SPY benchmark and untouched chronological holdouts. No production BUY authorization from a rank alone.


## LOCKED — PRIMARY v0.6 RESEARCH RANKING; v2.3 BENCHMARK ONLY (2026-10-10)

Owner approved changing the active OFTS *research review ranking* to prioritize current repeatable, economically worthwhile, healthy oscillations. Historical v2.3 quality score is retained in every output **only as a benchmark and immutable historical comparison**, not as the primary ordering of the current trading-watch research shortlist.

- Implementation: `ofts/research/opportunity_v06.py` and `ofts/worker.py`. On each full-universe worker run, evaluate the original v2.3 score and independent swing health and v0.5 viability first, then calculate the v0.6 80-point measured opportunity score using the last three confirmed UP legs and peak/trough intervals. Sort `ofts-output/v06_opportunity_research_ranked.csv` by v0.6 score descending; use this as the **primary research watchlist**. Preserve `v23_research_ranked.csv` unchanged in meaning for benchmarking.
- 80 measured points: repeatability 25, upside magnitude 20, timing 15, health/deterioration 20. The other 20 points (entry 15, execution/liquidity 5) and separate 0–100 eligibility/tradability multiplier **are not yet implemented**; they must remain null, not assumed perfect. Report scores explicitly **out of 80**, not out of 100. This is a partial research ordering, not an approved trading selection.
- **No junk in the qualified trading top-N:** market capitalization below $200M, price below $3, disallowed security types and other locked hard gates are excluded once verified. Missing as-of cap, security type, liquidity or other required evidence means `PENDING_ELIGIBILITY`; never label these verified keepers or invent a sixth stock. A source-backed INTS sub-$200M capitalization is a known exclusion for trading eligibility, even if it remains in the full diagnostic research table for audit.
- **Workflow verification:** `.github/workflows/ofts-full-universe-identity-rescore.yml` must run `ofts.test_opportunity_v06` alongside swing-health and recent-viability regressions; verify descending v0.6 ranks, original score preservation, no eligibility false passes, and upload `v06_opportunity_research_ranked.csv` with the same run's v2.3 benchmark and underlying diagnostics.
- Do not modify `ofts/daily.py` frozen prospective signal/return cohorts retroactively. Future live daily ranking integration must be separately implemented and verified with immutable cohort comparisons; the full-universe research worker being updated does not prove daily signal logic changed.
- Before promoting v0.6 to a complete eligible top-N or production BUY process, acquire dated security type, market cap, OHLCV and execution metrics; implement entry and liquidity components; run full eligible-universe scoring and chronological forward outcome tests including excluded winners, fees, SPY and trade execution lag. Never equate score magnitude with win probability.

### Verified eligibility exclusions in the active v0.6 worker (2026-10-10)

The research worker now calls `eligibility_status(symbol, asof_date, close)` and **removes known INELIGIBLE names from the primary v0.6 watch ranking**. The underlying all-symbol diagnostic ledger still records each exclusion and evidence. Dated verified evidence: INTS market capitalization **$10.55M as of 2026-10-09** per https://ycharts.com/companies/INTS/market_cap; this fails the locked $200M hard gate and cannot be rescued by a high opportunity score. Earlier historical as-of dates must not inherit future eligibility evidence. Unknown eligibility remains `PENDING_ELIGIBILITY`, not `PASS`; thus the resulting five-name list is **provisional research**, not five verified trade-eligible BUYs. The workflow tests the INTS exclusion, retains the v2.3 benchmark, and uploads the new ranking artifact. Add complete dated market-cap and security-type coverage before publishing an eligible universe-wide top-N.

### CTOS chart challenge — ranking is not entry readiness (2026-10-10)

Owner supplied dated October 9 brokerage screenshots for CTOS: last $9.25, session -1.28%, 5D -5.42%, 1M -2.01%, 1Y +47.29%. The 15-minute intraday chart shows a late selloff into the session low with elevated final-bar volume. The displayed bid $8.70 / ask $12.18 is unusually wide and MUST NOT be treated as a reliable executable spread without regular-session NBBO and timestamp verification. The one-month chart has visible rallies but no confirmed present-time upward reversal. **Human chart challenge: NO CONFIRMED ENTRY**. Screenshot observations are separate from programmatically computed OHLCV, and must not be retroactively applied to earlier historical snapshots.

The experimental v0.6 65.8489/80 CTOS rank is a **partial historical swing-quality research score**, not a verified BUY or an entry score. Its missing 15-point entry-readiness and 5-point execution fields must remain null; unknown dated cap/type/spread = PENDING_ELIGIBILITY. Do not promote CTOS merely because it ranks #1 on the partial score.

Required next model version: add as-of **entry-state** diagnostics that distinguish (1) descending into a possible trough, (2) unconfirmed bottom, (3) confirmed rebound, (4) chasing near prior peak, and (5) fresh breakdown; use trend, swing-pivot age, close relative to recent support, candle/volume confirmation, intraday selloff and reversal evidence where genuinely available, and stale/abnormal spreads. The screenshot is a challenge case, **not** permission to invent or backfill intraday observations from daily data. For a qualified trade candidate, require confirmed entry, verified liquidity/execution and all eligibility gates; otherwise explicit WAIT/NO_TRADE. Preserve a full-universe watchlist of candidates for future confirmation, rather than dropping potentially useful oscillators because they are currently falling. Benchmark prospective performance of confirmed vs unconfirmed entries, missed winners, and failed breakdowns; no claim of predictive improvement until validated.

### v0.7 — CRITICAL DATA/CURRENT-ENTRY CORRECTION (2026-10-10)

Owner challenged CTOS (#1 partial quality rank, 65.8489/80) with 2026-10-09 screenshots: close/last $9.25, 5D -5.42%, 1M -2.01%, 1Y +47.29%, late-day selling, quote $8.70 bid / $12.18 ask (potential after-hours/nonfirm, requires NBBO verification). **Never represent historical confirmed UP swings (6.43%, 9.31%, 9.33%) as the latest current movement or as a forecast.** The last completed UP leg was followed by an unfinished or completed new decline; the v0.6 score omitted that developing decline. Previous v0.6 scores also had no as-of date or live-data freshness flag in primary output. The full-universe worker consumes a RESTORED CACHED OHLCV file and must not imply those bars include the latest brokerage session.

Implemented separate `ofts/research/entry_diagnostic_v07.py` (experimental, research only) and attached it to `ofts/worker.py` outputs: last bar date, calendar-age freshness, close, last 5- and 20-session return, prior 20-close range, location within range, support break, short recovery confirmation, and states `STALE_DATA`, `BREAKDOWN_NO_TRADE`, `FALLING_WAIT`, `UNCONFIRMED_TROUGH_WAIT`, `CHASE_RISK_WAIT`, `REVERSAL_REVIEW`, `MID_CYCLE_WAIT`, `INSUFFICIENT_DATA`. Strictly no trade if stale, breaking down, or unconfirmed; even REVERSAL_REVIEW is NOT a BUY and must still pass liquidity/eligibility, spread and holdout validation. Screenshots are challenge evidence only, never substituted for raw point-in-time OHLCV in backtests.

**Separate columns/outputs**: historical quality rank (v2.3 benchmark), current swing quality (v0.6 partial out of 80), current entry state (v0.7), as-of date/freshness, eligibility, and approved actionable signal (NONE until fully validated). A top historical oscillator must not appear as an actionable buy just because its quality score is high. Never retrofit past BUY/SELL cohorts. The new v0.7 rules are provisional; validate no-lookahead, missed rebounds and false positives on chronological forward data before treating them as reliable predictions.

Operational next step: replace/refresh cached historical bars with verified current data, compare the same as-of date and adjusted close basis to brokerage chart, and calculate missing entry/execution points. Without this, **do not claim the CTOS chart discrepancy is fully fixed or that v0.7's classification reflects Oct 9 prices**.

### VERIFIED CTOS DATE MISMATCH — ROOT CAUSE (2026-10-10)

Actual successful run `38050372559` scored CTOS using cached **2026-10-07** daily OHLCV: **$9.43999958** last close, **+3.622%** trailing 5 sessions, entry diagnostic `MID_CYCLE_WAIT`. Owner's brokerage screenshot dated **2026-10-09** showed **$9.25** last and **-5.42%** trailing 5 days, a **9.042 percentage-point reversal** in the 5-day change. These are different as-of dates. It was WRONG to present Oct 7 partial historical rank as if describing Oct 9 current market conditions. The source cache needs refreshing; no score revision can compensate for stale prices.

Fix in `entry_diagnostic_v07.py`: date-aware `trading_session_lag` based on weekdays (temporary approximation pending actual exchange calendar); stale if >1 elapsed weekday, or future-dated. On Sat Oct 10, Wed Oct 7 is **2 elapsed weekdays, STALE_DATA**; Fri Oct 9 is **0**. Regression test pins this failure mode. Full-universe worker emits `v07_current_verified_trading_candidates.csv` separately, fail-closed to empty unless entry `REVERSAL_REVIEW`, verified eligibility `PASS`, and complete opportunity score. Historical v0.6 ranks remain research-only and should never be represented as a current trading top-N. A complete up-to-date feed, actual exchange calendar, intraday data where used, and executable bid/ask spread verification remain outstanding.

Mandatory QA: compare timestamp and last adjusted/unadjusted price basis to brokerage as-of before scoring, then last 5/20 session returns, swing pivots and incomplete latest leg. Never treat chart images as source of exact OHLCV or claim a system is spot-on/predictive without held-out forward testing.

### v0.8 independently refreshed chart-shape audit and fresh research keepers (2026-10-10)

Confirmed via successful GitHub Actions `38050736200`: independent Yahoo Finance/yfinance download through **2026-10-09**, **16/16** symbols refreshed, **0** errors; CTOS **$9.25** exactly matches the owner's screenshot. CTOS 30 sessions high **$10.27**, low **$8.714**, total high/low range **17.856%**, **3** completed UP legs (6.426%,9.308%,9.33%). CTOS 60 sessions high **$12.23**, low **$8.714**, range **40.349%**, **6** completed UP legs; 126 sessions high $12.23 low $7.10 range 72.254%, 12 UP legs; 252 sessions high $12.23 low $5.18 range 136.1%, 23 UP legs. **High/low range is NOT a swing profit or realizable trade.** Updated as-of v2.3 quality score **43.5034**, partial v0.6 quality **67.7239/80**; crucially current viability **DISSIPATING**, entry **FALLING_WAIT**. This disproves the suggestion that a two-session cache lag fully explained the chart disagreement. The core problem was ranking *historical oscillation magnitude* without applying current health as a noncompensable eligibility gate.

Automated workflow `.github/workflows/ofts-fresh-chart-audit.yml` now independently downloads latest two years of OHLCV for every research shortlisted name plus failed controls, verifies latest completed NYSE session, measures 30/60/126/252-session OHLC highs/lows, gross range %, return, completed UP legs and pivot spacing; stores dated JSON and CSV. `ofts/research/fresh_audit.py` writes a **separate current research keeper ranking** only if current health is not rejected; a high old v0.6 score can never override a DISSIPATING health veto. Current falling entries are watch only; eligibility remains separately PENDING until verified cap/type/liquidity evidence. Fresh keeper ranking is still **NOT** a production BUY ranking. Source and window labels are required on all published statistics.

Known limitations: present workflow refreshes the 6 shortlist candidates and 10 failed controls, NOT the entire 5,502 universe. Full-universe worker still uses a historical cache; daily worker refreshes a rotating subset. Before claiming full-universe current top rankings, refresh and re-score **all eligible universe names** to a common as-of date and verify completeness; do not represent 16-name current audit as complete universe refresh. The v0.8 keeper list is research-only and cannot prove future win rates; score calibration and forward controls remain outstanding.

### EVI screenshot challenge and regression: do not confuse one surge with repeatable oscillation (2026-10-10)
The user's Oct 9 brokerage charts showed EVI **5Y -34.07%, 1Y -34.18%, 1M +31.77%, 5D -0.88%**. Independent v0.8 OHLCV audit (workflow 38050866248, artifact 11669735025) confirmed EVI $19.12 and **30-session 1 completed UP leg (+56.025%)**, 60-session 3 UP legs (+8.889%, +17.239%, +56.025%), 126-session return -15.098%, 252-session return -35.903%. The independent swing health itself marked EVI **DOWNTREND**, yet the keeper code ignored it, promoting EVI #1 because v0.5 viability=REVIEW and entry=MID_CYCLE_WAIT. **This was a demonstrated ranking bug, not a data freshness issue.**

New v0.8 keeper gate: require last 30 sessions >=2 completed UP legs, last 60 >=3 completed UP legs and >=2 completed peak intervals and trough intervals; veto current viability != REVIEW, fail-closed missing windows, and keep DOWNTREND, weak-bounce, DECAYING, IRREGULAR, INSUFFICIENT out of current keeper rank (watch separately). All of these rules are provisional and require forward tests for false-negative costs. An isolated large jump does NOT satisfy repeatable 30-60 day oscillation criteria. Regression tests pin the EVI case. Old v2.3 and v0.6 scores are retained as benchmark only, not allowed to override hard current health and repeatability gates.

### v0.9 three CLEAR 5% peak-valley cycles, with cliff veto (experimental, 2026-10-10)

Owner clarified that OFTS must show the **last three CLEAR peak/valley oscillations each >=5%** rather than count noise or historic big rebounds. The separate `ofts/research/three_clear_cycles_v09.py` uses **daily closing prices** and a fixed **5% reversal-confirmed ZigZag** over the latest **126 trading sessions** (about six months). Each full cycle must be **LOW → HIGH → LOW**, with both the low-to-high rise **>=5%** and the high-to-next-low pullback **>=5%**; the last three cycles must each take **8–45 sessions**, and the latest completed trough must be <=40 sessions old. This avoids mistaking three minor micro-bounces or one giant recovery spike for three healthy completed cycles. Raw high/low price, swing percentages, session durations, and each of three cycles are exported in dated JSON; no image/screenshot input needed.

A **big-loss veto** prevents a high historical score from hiding a cliff: worst daily close-to-close drop <= -12%, or maximum close-to-close drawdown in 126 sessions >25%, or any of the last three confirmed peak-to-valley down legs >20% => `REJECT_BIG_LOSS`. These thresholds are *provisional research choices*, not validated profit/loss optimization. Typical 5-10% oscillatory declines do not automatically fail. Missing three full cycles => `REJECT_TOO_FEW_CYCLES`; timing or sub-5% leg => `REJECT_NOISY_OR_IRREGULAR`; stale cycle => `REJECT_STALE_CYCLES`. A clean three-cycle pass is necessary but NOT sufficient: retain prior viability, downtrend, entry-readiness and eligibility checks. A top historical score cannot override a veto. Preserve old scores as benchmark. Run holdout checks for missed good candidates and overrestriction before declaring model predictive.

Full-universe **5,502-name** refresh/re-score is not yet done; the fresh 16-name audit is only a challenge/control cohort. The independent workflow `ofts-fresh-chart-audit.yml` must pass its tests and complete before publishing new keeper counts. Never claim that three cycles guarantee future swings or that a historical peak/trough is tradeable at the exact turning point (pivot confirmation lag).

**v0.9 calibration correction (same date):** First verified independent 16-name run `38051483626` (11 tests, 16/16 data, 0 errors) showed 15/16 `REJECT_BIG_LOSS`, 1/16 `THREE_CLEAR_CYCLES` (BXC, but entry breakdown). This exposed an **overbroad 126-session drawdown veto** that incorrectly treated older history as a current loss event. Corrected loss veto to the **most recent 60 sessions** for worst day and max drawdown, while retaining the last 3 completed cycle down legs for the 20% peak-to-valley cap. Added **one-off giant rally veto** if the largest of the last three rises is >3x their median, so BXC's +70.99% rise cannot dominate +9.42%, +11.22% cycles. This addresses user's requirement to ignore irrelevant old noise without letting actual recent cliffs pass. Rerun and report new counts before claiming success. This is provisional research and must be calibrated against forward outcomes, not hand-tuned to individual chart aesthetics.

**v0.9b intra-swing choppiness (2026-10-10):** Three confirmed >=5% valley→peak→valley cycles alone do not establish tradability. The six legs of the latest three cycles now carry `rise_path_efficiency` and `fall_path_efficiency` = abs(net price change) / sum(abs(daily close-to-close changes)) from the underlying **unfiltered** daily closes. A straight move scores 1.0; whipsaw/noisy paths score closer to 0.0. `REJECT_CHOPPY_SWINGS` if **any of six** efficiency <0.40 OR the **median of six** <0.60. This test examines noise deliberately hidden by the 5% macro-pivot detector, including around peak/trough turning zones, and is a non-compensable keeper gate. Export all six leg values plus median and worst for visual audit. Thresholds are provisional, and path smoothness alone does not ensure the exact turning point can be predicted or entered without confirmation lag. Test on chronological holdouts for missed good swings and false positives before production promotion.

### Full universe reset and independent clean-cycle ranking (v0.10 experimental, 2026-10-10)

The old 16-name v0.6 shortlist is NOT the new discovery population. All 5,502 names are independently assessed with v0.9b `three_clear_cycles` using the original cached multi-year OHLC history, including post-identity-regime boundaries. First verified full-universe run `38051865638`: 5,502 total; 3,977 scoreable; 335 pass THREE_CLEAR_CYCLES, 368 REJECT_CHOPPY_SWINGS, 1,591 REJECT_BIG_LOSS, 214 REJECT_ONE_OFF_SPIKE, 475 REJECT_NOISY_OR_IRREGULAR, 910 REJECT_TOO_FEW_CYCLES, 84 REJECT_STALE_CYCLES; others missing/price/identity. Old combined rules left only CTOS; user chart shows CTOS is not a convincing entry, so do NOT present CTOS as best BUY.

**v0.10 independent research ranking** uses `ofts/research/clear_cycle_rank_v10.py` applied to the 335 passing clear-cycle stocks, not old v0.6 ordering. Score out of 100: amplitude consistency 25 (both up and down), cycle timing consistency 20, median intra-leg path smoothness 25, worst of six legs smoothness 10, typical median upside 15, recency 5. Missing verified cap/security eligibility costs 8 points; known INELIGIBLE is excluded from any keeper shortlist. Historical v2.3/v0.6 scores, viability state, trend, and entry diagnostic are retained as benchmark/warnings, not automatic score boosters or invisible legacy ranking gates. Scores are experimental *research quality*, not success probabilities or production BUYs. Preserve unfiltered 5,502-row `v09_full_universe_cycle_audit.csv`, `v09_full_universe_clear_cycle_pass.csv`, `v09_full_universe_keepers.csv`, and `v09_full_universe_report.json` as Actions artifacts. Do not claim current-price validity from the cached historical OHLC. An independent fresh provider audit now refreshes top 40 of the NEW ranked cohort plus prior false-positive controls using completed NYSE sessions; report data errors and never infer fresh prices from old cache. Require forward chronological holdout before promotion.
