# Engine 4 SSOT v5.5 — Manual On-Demand Control

This addendum locks the permanent manual control implemented by
`.github/workflows/engine4-manual-on-demand.yml`.

## Locked modes

1. `live_today`
   - Runs the complete current-date guarded Engine 4 cycle.
   - May start only from 08:55 through 10:30 Eastern on a weekday.
   - Uses the current Eastern market date for every stage.
   - Requires provider health, all code/unit/self-tests, date verification,
     terminal-state verification, and required SMS delivery.
   - Manual outputs are uploaded under the unique GitHub run ID and never
     overwrite committed production artifacts.

2. `acceptance_replay`
   - Runs the full prescreen, deep analysis, refresh/freeze, and final stages
     against an explicitly locked historical Eastern market date.
   - May run at any time.
   - Sends no trade-like SMS notifications.
   - Never commits or overwrites production artifacts.
   - Must verify the date on every output, every required timeline stage,
     funnel integrity, and a valid terminal status.

3. `preflight_only`
   - Compiles Engine 4, runs the complete unit/self-test suite, and verifies
     provider health.
   - Does not run the market funnel or send trade-like SMS notifications.

## Safety rules

- A manual request never bypasses market-time integrity.
- Midday or overnight data must never be described as a valid premarket live
  production cycle.
- Historical acceptance output must remain isolated from production output.
- Automatic production and manual operation share one concurrency lock so they
  cannot execute simultaneously.
- A failed live manual cycle sends the required pipeline-failure notification;
  an acceptance replay does not impersonate a production alert.
- The manual workflow is an independent recovery and verification control. It
  does not disable or replace the automatic 08:35 Eastern production schedule
  or its watchdog.
