# ENGINE 4 SSOT v5.8 — Enforced Invocation, Launch Ownership, and Reporting Addendum

Effective: 2026-09-23  
Repository: `jtgeorge1970-tech/30-day-rocket-screen`

This addendum governs the ChatGPT invocation layer and morning launch accountability. It does not change Engine 4 scoring, eligibility, provider, stage, watchlist, risk, or trade-safety logic. Where startup language conflicts with an earlier addendum, this v5.8 addendum governs.

## Golden Rules

1. Never guess or assume.
2. No shortcuts or skipped steps.
3. Follow the SSOT exactly.
4. Verify before reporting.
5. A schedule, cron entry, commit, dispatch request, or run ID is not proof that Engine 4 successfully started.
6. Do not modify locked Engine 4 production logic without Joseph's explicit permission.

## Invocation responsibility

- The ChatGPT automation scheduler is responsible for invoking the saved early and launch-guard tasks.
- GitHub Actions does not invoke ChatGPT.
- The user is not required to send a morning message to activate the saved guards.
- ChatGPT cannot truthfully claim it will “wake itself.” It acts when the enabled automation scheduler invokes it.
- GitHub's independent production schedule, sentinel, and watchdog remain separate protections if a ChatGPT invocation is absent.

## Required 08:20 ET early preflight

An enabled exact-schedule ChatGPT automation must invoke at 08:20 Eastern on every U.S. market weekday.

It must perform a read-only preflight:
- lock and display the current Eastern market date;
- verify authenticated read access to the repository and GitHub Actions;
- verify deployed `main` and required Engine 4 workflow availability;
- verify the latest applicable acceptance result without substituting it for today's live run;
- verify the 08:36 launch-owner automation remains enabled;
- identify any permissions/platform blocker before the launch window.

This preflight must not redesign Engine 4, alter scoring, or create an early duplicate production cycle. It must produce a permanent on-screen status. A passing preflight is readiness evidence only, not proof of launch.

## Required 08:36 ET launch owner

A separate enabled exact-schedule ChatGPT automation must invoke at 08:36 Eastern on every U.S. market weekday.

It is the sole ChatGPT manual-launch owner and must:

1. Inspect current-day GitHub Actions state using the locked Eastern market date.
2. Accept only an actual current-day Engine 4 production run or a `live_today` manual run.
3. Reject acceptance, replay, preflight, stale-date, cancelled, skipped, and failed runs as launch proof.
4. Prevent duplicates by checking for a valid queued/in-progress run immediately before every write.
5. If no valid run exists, update `.github/engine4-manual-trigger.txt` with `mode=live_today`, the locked Eastern date, and a fresh unique `requested_at` value.
6. Recheck GitHub until the resulting run ID and job are visible.
7. Treat a trigger request or commit without a visible run as unproven and retry safely with a fresh unique trigger when no valid run exists.
8. Inspect job and step health after a run ID appears.
9. Treat any run that fails, is cancelled, or is skipped before verified Stage 1 execution as **ENGINE 4 NOT STARTED**.
10. For a pre–Stage 1 failure, report the exact failed step, confirm no valid run is active, and perform another authorized fresh `live_today` attempt without changing engine code.
11. Continue until one run reaches verified Stage 1 execution or a specific repository-permission/platform blocker makes further launch attempts impossible.

## Successful-start definition

Engine 4 is successfully started only when all of the following are verified:
- current Eastern market date matches;
- valid production or `live_today` workflow identity;
- actual GitHub run ID;
- job is running;
- required setup has not failed;
- Stage 1 / broad prescreen has visibly started.

A run ID by itself is never sufficient.

## Continuing ownership

After Stage 1 is verified, the launch owner remains responsible for monitoring the same verified run through:
- Stage 1 broad prescreen;
- Stage 2 deep analysis;
- Stage 3 refresh/rerank/freeze;
- Bench processing;
- Stage 4 primary live confirmation;
- Stage 5 recovery when applicable;
- artifact/date/order verification;
- required notification evidence;
- terminal GitHub conclusion.

A valid zero-eligible `NO_TRADE` is allowed only when the full required workflow completes correctly.

## Permanent on-screen reporting

Substantive reports must be standalone final messages, not temporary/collapsible work updates. Each report must carry forward verified facts and use actual Eastern timestamps.

When available, report:
- baseline eligible;
- trustworthy observations;
- NATURAL broad-qualified;
- Nasdaq premarket enriched;
- NONZERO premarket activity;
- strict activity;
- RETAINED BY TOP-100 CAP;
- SELECTED BY TOP-60 CAP;
- ACTUALLY ANALYZED;
- SCORE >=80;
- LAUNCHPAD ELIGIBLE;
- B-grade;
- STRICT A/A+;
- FROZEN FINAL-SCAN COUNT;
- no more than the ranked Top 10 eligible finalists with required evidence and failure reasons;
- selection, primary entry, recovery, and execution as separate results;
- Bench additions, removals, retained count, and tickers;
- provider health, locked ET date, artifacts, notifications, workflow run ID/link, and terminal conclusion.

Never call a configured cap a natural survivor count. Never infer a missing value. Mark unavailable fields explicitly.

## Permission boundary

This addendum is standing authorization only for the defined current-day launch verification, duplicate-safe `live_today` trigger, and necessary pre–Stage 1 retry loop. It is not authorization to:
- change Engine 4 code or SSOT trading logic;
- alter scoring, gates, timing, watchlist rules, providers, or notifications;
- create unrelated workflows;
- cancel a healthy run;
- start extra proof/replay/acceptance runs;
- continue running after a correct terminal result when no further stage is required.

## Proof standard

Reliability is demonstrated by three consecutive market-day cycles in which:
- the 08:20 preflight invokes;
- the 08:36 launch owner invokes;
- a healthy current-day run reaches Stage 1 without user prompting;
- the run is monitored through its correct terminal result;
- all reporting follows this SSOT;
- no unauthorized modification or duplicate occurs.

No promise or configured schedule substitutes for this measured proof.
