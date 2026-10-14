# OFTS Incident Recovery Record

## Resolution

- Status: **RESOLVED and reload-verified**.
- Latest completed NYSE session: **2026-10-13**.
- Successful recovery: [GitHub Actions run 38499864000](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/actions/runs/38499864000), completed 2026-10-14 02:15:11 UTC.
- Durable remote commit: [db1cab38f643beacbaa8dd09e14dce76a5f3c2c4](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/commit/db1cab38f643beacbaa8dd09e14dce76a5f3c2c4).

## Verified October 13 result

- Selected: **138**.
- Refreshed/scored: **138**.
- Refresh errors: **0**.
- Required stale symbols: **0**; SPY refreshed through 2026-10-13.
- Freshness gate: **passed**, 138/138.
- Qualified prediction cohorts: **3**, including immutable `predictions/2026-10-13-qualified.json`.
- Immutable prediction files: **5**; cohort rows: **388**; attempts retained: **56**.
- Cycle fingerprints: **111/139**.
- Signal states: **3 research BUY states, 0 SELL, 136 NO_TRADE**. Production approval remains **NO** and the system gate remains `RESEARCH_ONLY_NO_GO`.
- Outcomes: **1,825 PENDING**, **115 INELIGIBLE_DATA**; recomputation matches saved evidence.
- Cycle ledger: **3 pending entries, 3 open positions, 0 closed trades, 0 SPY benchmark pairs**.
- 5/10/20/30/60-session report cards have **0 mature observations** and remain awaiting their scheduled exits. First 5-session exit is 2026-10-16.
- Remote durable-state save and reload proof passed.

## Incident history preserved

Earlier October 13 attempts failed closed because the daily provider returned histories ending on October 12 for nearly the entire universe and SPY. The last failed snapshot had 138 selected, 2 refreshed/scored and 319 refresh errors. No stale cohort was admitted, no prediction was backdated, and failures were retained.

## Repairs completed

1. [87f6c6087932a30f1c1d4d3dfd84257a2b5d4169](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/commit/87f6c6087932a30f1c1d4d3dfd84257a2b5d4169): fail-closed attempted-session audit and full freshness admission.
2. [df3fdd5e9ed793df7841001e8041d4ad85693aab](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/commit/df3fdd5e9ed793df7841001e8041d4ad85693aab): strict completed-session 15-minute fallback when the daily provider lags.
3. [d42b5ecf6b448a9380c299d9caeb1398fcf00a19](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/commit/d42b5ecf6b448a9380c299d9caeb1398fcf00a19): Yahoo aliases for class-share tickers while preserving canonical research symbols.
4. [2fa858389cfde3017c8f5543788ca20e0fb1ab63](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/commit/2fa858389cfde3017c8f5543788ca20e0fb1ab63): corrected the intraday provider argument and added bounded retries for transient durable-state push failures.

Tests, freshness verification, independent saved-evidence audit, persistence, remote save, and reload all passed. Research formulas, freshness requirements, frozen evidence, and prior immutable predictions were not weakened or rewritten.

## Next normal check

- Do not rerun October 13 again unless its durable qualified cohort, audit, remote commit, or reload proof disappears.
- On the next completed NYSE session, require the same full freshness, immutable prediction, audit, remote save, and reload gates.
- Continue preserving rejected candidates and losers for forward validation.
- No brokerage actions are authorized or performed.
