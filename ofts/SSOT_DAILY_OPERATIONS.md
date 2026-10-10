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
