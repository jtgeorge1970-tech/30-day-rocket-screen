# OFTS Active Incident Recovery

## Current incident

- Latest completed NYSE session: **2026-10-13**.
- Required 2026-10-13 qualified fresh cohort: **missing**.
- Latest attempt: [GitHub Actions run 38495326066](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/actions/runs/38495326066), started 2026-10-14 01:22:03 UTC and completed 2026-10-14 01:25:15 UTC.
- Attempt result: **138 selected, 2 refreshed/scored, 319 refresh errors**.
- Required freshness failures: all 25 required watchlist symbols plus SPY remained stale; provider histories generally ended at 2026-10-12.
- The only scored symbols were SAC (13.986) and QSEA (11.829). Both were `REJECT_CANDIDATE_GATE` and `NO_TRADE`. There is no valid dated Top 10–25 ranking for 2026-10-13.
- Precise external blocker: the market-data provider did not yet return the 2026-10-13 closing bar for the required universe and SPY. This is not repaired by accepting a future bar, backdating predictions, or weakening freshness.

## Repair completed

- Main commit [87f6c6087932a30f1c1d4d3dfd84257a2b5d4169](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/commit/87f6c6087932a30f1c1d4d3dfd84257a2b5d4169) repaired failed-attempt accounting and fail-closed cohort admission.
- The saved freshness audit now records the attempted session's failed snapshot instead of implicitly reusing a prior successful cohort.
- A failed operational gate now prevents cohort qualification even when aggregate bulk coverage is otherwise sufficient.
- Fingerprints and signals are saved only after the full required-watchlist-plus-SPY gate passes.
- Unit tests, durable-state restore, audit, persistence, remote save, and artifact upload passed in run 38495326066.
- Research formulas, freshness requirements, frozen evidence, and immutable prior predictions were not changed.

## Verified durable state

- Qualified cohorts remain **2**; no 2026-10-13 cohort was admitted.
- Predictions: **4 immutable files**, 54 attempts, 250 cohort rows.
- Outcomes: **1,170 PENDING** and **80 INELIGIBLE_DATA**.
- Cycle ledger: **2 pending, 1 open, 0 closed, 0 SPY comparison pairs**.
- The 5/10/20/30/60-session and cycle report cards remain awaiting mature closed forward trades.
- Research quality rankings are not production BUY signals.

## Cooldown and next-check procedure

- Do not retry before **2026-10-14 02:25:15 UTC** (one hour after the last attempt completed).
- At or after that time:
  1. Check for an active OFTS daily workflow and do not create a duplicate.
  2. If no run is active, rerun the failed jobs from run 38495326066.
  3. Require the actual 2026-10-13 close for all required watchlist names and SPY, with at least 100 fresh symbols.
  4. Verify a qualified 2026-10-13 cohort, immutable prediction file, fingerprints/signals, freshness audit, durable remote save, and reload proof.
  5. Recheck dated rankings, losers, 5/10/20/30/60-session outcomes, cycle report cards, and benchmark comparisons.
  6. If the provider still lacks the bars, preserve the failed evidence and extend the cooldown; do not hammer the provider.

No brokerage actions are authorized or performed.
