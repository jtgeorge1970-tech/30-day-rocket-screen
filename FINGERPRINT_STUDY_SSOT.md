# 30-Session Loser Cohort & Fingerprint Study — Locked SSOT

## Purpose

Measure what happened after every qualifying major-loss event in the latest 30
completed trading sessions and identify observable fingerprints associated with
recovery or continued failure. This is a research study, not a daily pick list.

## Scarcity rule

The study is never required to produce a stock on any day, week, or month. Zero
strict candidates is a valid result. Thresholds may not be loosened because the
current candidate file is empty.

## Event cohort

1. Start with the complete current U.S.-listed common-stock/ADR universe and
   retain the engine's structure exclusions.
2. Examine the latest 30 completed trading sessions for each security.
3. A loss event requires a one-session close decline of at least 6% or a
   five-session close decline of at least 12%, plus a drawdown of at least 15%
   from the trailing 52-week closing high as known on that event date.
4. Require event-date price of at least $3 and trailing 20-session average
   dollar volume of at least $2 million.
5. Apply a ten-session same-ticker cooldown after an accepted event so one
   collapse is not counted repeatedly.

## Anti-hindsight outcome rules

- The hypothetical measurement entry is the next session's open. The event
  close is not treated as an executable foreknown entry.
- Primary outcome is whether +10% was touched before -10% within 30 subsequent
  sessions, using daily highs and lows.
- If both levels are touched on the same daily bar before either was previously
  resolved, label the path `AMBIGUOUS`; never assume the favorable order.
- If neither level is touched and 30 subsequent sessions have not elapsed,
  label the event `OPEN`. It is not a winner or failure.
- Also record 5/10/20/30-session close returns, maximum favorable excursion,
  maximum adverse excursion, and time to each barrier when observable.

## Fingerprints

Record only values known at the event timestamp for event-level comparisons:
loss type and severity, preceding 20-session trend, trailing drawdown, relation
to the prior 52-week low, volume expansion, volatility, and event-bar close
location. Post-event bottom/reclaim signals may be used only when the modeled
entry occurs after those signals; they cannot be smuggled into an event-date
prediction.

## Current opportunities

A current opportunity must be both part of the open 30-session loss cohort and
pass every quantitative gate in `QUALITY_LOSER_SSOT.md`. It remains
`RESEARCH_ONLY_NOT_BUY` until all fresh manual gates pass. The cohort study alone
can never create `ENTRY_READY` status.

## Data limitation

The initial implementation uses the current listed universe and adjusted Yahoo
daily history. It therefore excludes securities that delisted before the run
and lacks fully point-in-time fundamentals and historical shares outstanding.
Results are exploratory and may not be called statistically proven. Promotion
to a validated V2.1 rule requires point-in-time data including delisted issues,
larger historical cohorts, walk-forward testing, costs, and an untouched final
test period.
