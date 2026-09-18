# ENGINE 4 SSOT v5.6 — Triple Wake and Human Failsafe Addendum

Effective: 2026-09-18  
Repository: `jtgeorge1970-tech/30-day-rocket-screen`

This addendum governs Engine 4 startup reliability. It does not change scoring,
eligibility, catalyst, price-cap, or trade-safety rules.

## Required wake layers

1. **Early controller — 08:20 ET**
   - Runs code/tests/provider preflight.
   - Sends both phones an `EARLY PROTECTION ACTIVE` SMS.
   - At 08:35 ET, verifies an actual production run ID.
   - Dispatches production if no active or successful production run exists.

2. **Primary production retries — 08:35, 08:40, 08:45, 08:50 ET**
   - Uses explicit UTC schedules for both EDT and EST.
   - The Eastern-time guard rejects the wrong seasonal duplicate.
   - Duplicate protection permits no more than one valid daily cycle.

3. **Recovery watchdog — 08:42, 08:47, 08:52 ET**
   - Verifies actual production state or an active morning manual-failsafe run.
   - Dispatches a recovery wake if production is absent.
   - Sends both phones a distinct watchdog-intervention SMS only when it acts.
   - The Eastern-time guard rejects the wrong seasonal duplicate.

4. **Independent ChatGPT manual wake — 08:50 ET**
   - Checks actual GitHub Actions state rather than schedule configuration.
   - If no valid production or live-manual run exists, updates the manual trigger
     for `live_today` and monitors the run through terminal completion.
   - The manual workflow preserves the required 08:55, 09:05, 09:18, and 09:45
     ET stage checkpoints when started early.

## Notification proof

The following notification kinds are independent and cannot deduplicate one
another: `preflight`, `launch`, `watchdog`, `start`, `final`,
`recovery`, `complete`, and `failure`.

A successful wake claim requires an actual GitHub Actions run ID. A configured
cron expression is not proof that Engine 4 started.

## Correct completion

A day is operationally successful when the correct Eastern market date is
locked, every required stage executes in order, dated artifacts are preserved,
both-phone notifications are API-accepted, and the run reaches a valid terminal
result. Zero qualifying stocks is a valid `NO_TRADE` result. Missing, stale,
out-of-order, or fabricated data is a pipeline failure.
