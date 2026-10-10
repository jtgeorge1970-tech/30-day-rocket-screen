# OFTS STAGED ACCOUNTABILITY — authoritative execution checklist

Updated: 2026-10-09 (America/Mexico_City)
Owner: automated GitHub Actions for recurring daily runs; assistant for development, verification, and reporting during active sessions.
Rules: no stage is marked complete without saved evidence; do not rewrite historical predictions; research scores are not production BUY signals.

| Stage | Status | Acceptance gate | Evidence / next work |
|---|---|---|---|
| 1. SSOT and research foundation | COMPLETE | 5,502 universe and 3,978 research scores; PR #38 merged | PR #38 merged into main; independent research worker results |
| 2. Daily market-data reliability | PROVISIONALLY PASSED | At least 100/125 fresh, target 125; repeat on next market session | Run 38013760788: 124/125 fresh; AKO.A failed. Verify a second independent session before full closure |
| 3. Durable daily selections | IN PROGRESS | All 125 classifications saved; dated Top 10–25 ranked eligible selections; restart and remote-save verified | State branch ofts-daily-state exists; 2026-10-09 cohort frozen. Only 1 scored candidate in latest report; diagnose why |
| 4. Stock-specific cycle fingerprints | NOT VERIFIED | Per-symbol cycle duration, amplitude, consistency, and confidence without future leakage | Implement and test |
| 5. BUY/SELL signals and trade simulation | NOT VERIFIED | Point-in-time entries/exits, risk, costs, no-lookahead and no-trade classification | Implement and test; no production trading approval |
| 6. Forward fixed-horizon and cycle audits | PARTIAL | Immutable 5/10/20/30/60-session audits plus cycle BUY-to-SELL audits for every cohort | Fixed horizon framework exists; zero mature outcomes yet |
| 7. Report card | PARTIAL | Win/loss, avg gains/losses, downside, SPY, score-band predictive power, sample sizes, missing data, missed opportunities | REPORT.md exists; no mature results |
| 8. Out-of-sample predictive validation | NOT VERIFIED | Demonstrated results across independent dates and cycle classes, net of costs | Requires matured cohorts |
| 9. Unattended operations | PARTIAL | Scheduled runs, persistence, alerts on failures, automatic recovery and verified reports | GitHub schedule exists; demonstrate repeated independent sessions |

Automatic progress rule: daily workflow runs on trading weekdays, stores immutable predictions, and matures prior outcomes. Research stages 4–8 require code changes and evidence; do not falsely mark them complete just because a scheduled job passed.

Current blocker: 2026-10-09 daily report shows 124/125 fresh but only FXNC scored as candidate. Determine why 123 refreshed names do not appear with valid scores; ensure all rows are retained and top ranking is meaningful.
