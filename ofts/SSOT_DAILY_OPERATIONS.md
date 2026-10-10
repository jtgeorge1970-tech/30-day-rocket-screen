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
