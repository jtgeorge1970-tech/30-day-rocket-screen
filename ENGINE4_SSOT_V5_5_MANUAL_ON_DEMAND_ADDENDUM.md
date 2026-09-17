# Engine 4 SSOT v5.5 — Manual On-Demand Control

This addendum locks the permanent manual control implemented by
`.github/workflows/engine4-manual-on-demand.yml`.

The workflow can be started from GitHub's **Run workflow** button or by an
authorized Engine 4 operator updating `.github/engine4-manual-trigger.txt`.
The trigger file exists so Joseph can request an on-demand run in ChatGPT
without operating GitHub himself.

## Locked modes

1. `live_today`
   - Runs the complete current-date guarded Engine 4 cycle.
   - May start from 08:55 through 15:30 Eastern on a weekday while the regular market is open.
   - A start after the original morning stages replays those stages from the same
     current Eastern market date, then performs final confirmation with the live
     quote available at execution time. It is identified as an on-demand recovery
     run, never mislabeled as the original scheduled morning run.
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
- A midday current-date recovery run must never be described as the original
  scheduled premarket production cycle; an overnight request must be refused.
- The locked $100 maximum tradable price is a mandatory launchpad gate. Names
  above the cap remain in audit rankings but cannot occupy a frozen slot.
- Historical acceptance output must remain isolated from production output.
- Automatic production and manual operation share one concurrency lock so they
  cannot execute simultaneously.
- A failed live manual cycle sends the required pipeline-failure notification;
  an acceptance replay does not impersonate a production alert.
- The manual workflow is an independent recovery and verification control. It
  does not disable or replace the automatic 08:35 Eastern production schedule
  or its watchdog.
