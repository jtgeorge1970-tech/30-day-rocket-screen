# OFTS STAGED ACCOUNTABILITY — authoritative execution checklist

Updated: 2026-10-10 (America/Bahia_Banderas)
Owner: automated GitHub Actions for recurring daily runs; assistant for development, verification, and reporting during active sessions.
Rules: no stage is marked complete without saved evidence; do not rewrite historical predictions; research scores are not production BUY signals.

| Stage | Status | Acceptance gate | Evidence / next work |
|---|---|---|---|
| 1. SSOT and research foundation | COMPLETE | 5,502 universe and 3,978 research scores; PR #38 merged | PR #38 merged into main; independent research worker results |
| 2. Daily market-data reliability | PROVISIONALLY PASSED | At least 100/125 fresh, target 125; repeat on next market session | Run 38013760788: 124/125 fresh; AKO.A failed. Verify a second independent session before full closure |
| 3. Durable daily selections | COMPLETE | All 125 classifications saved; dated Top 10–25 ranked eligible selections; restart and remote-save verified | Run 38032700274: 124/125 fresh, all 125 classified, Top 25 saved, qualified cohort immutable, durable remote save verified at 5e2afc4 |
| 4. Stock-specific cycle fingerprints | COMPLETE | Per-symbol cycle duration, amplitude, consistency, and confidence without future leakage | Run 38032700274: 97/125 eligible rows saved with point-in-time cadence/amplitude/consistency/confidence; remaining 28 explicitly unscorable/ineligible; tests passed |
| 5. BUY/SELL signals and trade simulation | NOT VERIFIED | Point-in-time entries/exits, risk, costs, no-lookahead and no-trade classification | Implement and test; no production trading approval |
| 6. Forward fixed-horizon and cycle audits | PARTIAL | Immutable 5/10/20/30/60-session audits plus cycle BUY-to-SELL audits for every cohort | Fixed horizon framework exists; zero mature outcomes yet |
| 7. Report card | PARTIAL | Win/loss, avg gains/losses, downside, SPY, score-band predictive power, sample sizes, missing data, missed opportunities | REPORT.md exists; no mature results |
| 8. Out-of-sample predictive validation | NOT VERIFIED | Demonstrated results across independent dates and cycle classes, net of costs | Requires matured cohorts |
| 9. Unattended operations | PARTIAL | Scheduled runs, persistence, alerts on failures, automatic recovery and verified reports | GitHub schedule exists; demonstrate repeated independent sessions |

Automatic progress rule: daily workflow runs on trading weekdays, stores immutable predictions, and matures prior outcomes. Research stages 4–8 require code changes and evidence; do not falsely mark them complete just because a scheduled job passed.

Current blocker: Stage 5 has no independently verified point-in-time BUY/SELL state machine or executable trade simulation. Stage 6 fixed-horizon outcomes are pending future sessions; first 5-session maturity for the 2026-10-09 qualified cohort is after the 2026-10-16 close/data delay. Cycle-based BUY-to-SELL audits still require Stage 5 signals. AKO.A remains the sole 2026-10-09 provider failure and stays in retry.
