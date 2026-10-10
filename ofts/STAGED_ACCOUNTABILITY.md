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
| 5. BUY/SELL signals and trade simulation | COMPLETE | Point-in-time entries/exits, risk, costs, no-lookahead and no-trade classification | Runs 38037741448 and 38037848973 passed: 125 immutable daily states (1 research BUY, 0 SELL, 124 NO_TRADE); 24 chronological nonoverlapping BUY-to-SELL simulations with costs, fixed/trailing risk rules and no-lookahead tests. Production approval remains NO |
| 6. Forward fixed-horizon and cycle audits | PARTIAL | Immutable 5/10/20/30/60-session audits plus cycle BUY-to-SELL audits for every cohort | Run 38038483917 verified restart-safe next-open cycle ledger and durable save 7a21896: 1 pending YDES entry for 2026-10-12, 0 open, 0 closed, 0 SPY pairs. Historical audit: 24 trades, +13.252% mean but -0.825% median and outlier dependence. Forward cohort still has zero mature outcomes |
| 7. Report card | PARTIAL | Win/loss, avg gains/losses, downside, SPY, score-band predictive power, sample sizes, missing data, missed opportunities | Run 38043991571 passed 18 tests and durably saved cycle-speed accounting: FAST 1–10, MEDIUM 11–25, SLOW >25, raw net return plus capital-time efficiency per 20 sessions, captured/missed swing and SPY excess. Status honestly remains AWAITING_CLOSED_FORWARD_TRADES |
| 8. Out-of-sample predictive validation | NOT VERIFIED | Demonstrated results across independent dates and cycle classes, net of costs | Requires matured cohorts |
| 9. Unattended operations | PARTIAL | Scheduled runs, persistence, alerts on failures, automatic recovery and verified reports | GitHub schedule exists; demonstrate repeated independent sessions |

Automatic progress rule: daily workflow runs on trading weekdays, stores immutable predictions, and matures prior outcomes. Research stages 4–8 require code changes and evidence; do not falsely mark them complete just because a scheduled job passed.

Current blocker: forward evidence, not ledger or cycle-speed report-card machinery. The 2026-10-09 YDES research BUY is correctly pending for hypothetical execution at the 2026-10-12 open; no future opening price is filled early. The historical cycle audit remains mixed and not production-ready: only 24 trades across 6 training-selected symbols, 50% wins, positive mean driven by outliers, negative median, and no historical SPY pair. First 5-session fixed-horizon maturity is after the 2026-10-16 close/data delay. AKO.A remains in retry.
