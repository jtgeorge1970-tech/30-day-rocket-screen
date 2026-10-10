# OFTS STAGED ACCOUNTABILITY — authoritative execution checklist

Updated: 2026-10-10 (America/Bahia_Banderas)
Owner: automated GitHub Actions for recurring daily runs; assistant for development, verification, and reporting during active sessions.
Rules: no stage is marked complete without saved evidence; do not rewrite historical predictions; research scores are not production BUY signals.

| Stage | Status | Acceptance gate | Evidence / next work |
|---|---|---|---|
| 1. SSOT and research foundation | COMPLETE (infrastructure only) | 5,502 universe and 3,977 identity-gated research scores; PR #38 merged | Run 38046200050 verified IQMX 340 raw/68 post-event bars and excluded it; new provisional #1 SCYX 67.197. Other identities not audited; no production BUY. |
| 2. Daily market-data reliability | PARTIAL — IDENTITY INTEGRITY | >=100/125 fresh on repeat sessions AND verified identity-regime integrity | 124/125 fresh Oct 9, AKO.A failed; Oct 10 IQMX identity break exposed. Identity-aware full-universe rescore verified run 38046200050; daily integration and no-go reporting passed 24 tests in run 38046226818 with durable save 7e32ff1; broader SPAC/IPO/ticker-change audit and next-session coverage remain. |
| 3. Durable daily selections | COMPLETE | All 125 classifications saved; dated Top 10–25 ranked eligible selections; restart and remote-save verified | Run 38032700274: 124/125 fresh, all 125 classified, Top 25 saved, qualified cohort immutable, durable remote save verified at 5e2afc4 |
| 4. Stock-specific cycle fingerprints | COMPLETE | Per-symbol cycle duration, amplitude, consistency, and confidence without future leakage | Run 38032700274: 97/125 eligible rows saved with point-in-time cadence/amplitude/consistency/confidence; remaining 28 explicitly unscorable/ineligible; tests passed |
| 5. BUY/SELL signals and trade simulation | COMPLETE | Point-in-time entries/exits, risk, costs, no-lookahead and no-trade classification | Runs 38037741448 and 38037848973 passed: 125 immutable daily states (1 research BUY, 0 SELL, 124 NO_TRADE); 24 chronological nonoverlapping BUY-to-SELL simulations with costs, fixed/trailing risk rules and no-lookahead tests. Production approval remains NO |
| 6. Forward fixed-horizon and cycle audits | PARTIAL | Immutable 5/10/20/30/60-session audits plus cycle BUY-to-SELL audits for every cohort | Run 38038483917 verified restart-safe next-open cycle ledger and durable save 7a21896: 1 pending YDES entry for 2026-10-12, 0 open, 0 closed, 0 SPY pairs. Historical audit: 24 trades, +13.252% mean but -0.825% median and outlier dependence. Forward cohort still has zero mature outcomes |
| 7. Report card | PARTIAL | Win/loss, avg gains/losses, downside, SPY, score-band predictive power, sample sizes, missing data, missed opportunities | Run 38043991571 passed 18 tests and durably saved cycle-speed accounting: FAST 1–10, MEDIUM 11–25, SLOW >25, raw net return plus capital-time efficiency per 20 sessions, captured/missed swing and SPY excess. Status honestly remains AWAITING_CLOSED_FORWARD_TRADES |
| 8. Out-of-sample predictive validation | NOT VERIFIED — RESEARCH_ONLY_NO_GO | Demonstrated results across independent dates and cycle classes, net of costs | Run 38046226818 passed 24 tests and durably reports observed daily score range 10.884–62.584, validated BUY threshold NONE, and system actionability RESEARCH_ONLY_NO_GO. Requires matured cohorts before any numeric BUY cutoff |
| 9. Unattended operations | PARTIAL | Scheduled runs, persistence, alerts on failures, automatic recovery and verified reports | GitHub schedule exists; demonstrate repeated independent sessions |

Automatic progress rule: daily workflow runs on trading weekdays, stores immutable predictions, and matures prior outcomes. Research stages 4–8 require code changes and evidence; do not falsely mark them complete just because a scheduled job passed.

Current blockers: (1) DATA INTEGRITY: IQMX full-universe rank #1 / 77.597 used 340 historical bars despite its ADS beginning July 2, 2026; old rank must not be represented as authoritative. Code now excludes pre-identity bars and requires >=180 post-event bars; full-universe rescore verified run 38046200050; daily persistence verification and broader security-identity audit remain. (2) FORWARD EVIDENCE: no matured forward cycle trades or fixed-horizon observations yet. The 2026-10-09 YDES research BUY is correctly pending for hypothetical execution at the 2026-10-12 open; no future opening price is filled early. The historical cycle audit remains mixed and not production-ready: only 24 trades across 6 training-selected symbols, 50% wins, positive mean driven by outliers, negative median, and no historical SPY pair. First 5-session fixed-horizon maturity is after the 2026-10-16 close/data delay. AKO.A remains in retry.


## IQMX identity-break repair (2026-10-10)

- Source: Nasdaq July 1, 2026 post-RAAQ combination announcement; IQMX ADS began trading July 2.
- Worker evidence: GitHub Actions run 38008125845 reported IQMX **340 bars**, score **77.597**, rank **1**. This necessarily spans pre-July 2 prices and invalidates a continuous-operating-company oscillation claim.
- Repairs committed: `ofts/research/security_regimes.py` verified boundary; `ofts/worker.py` full-universe post-identity history gate; `ofts/daily.py` future-cohort post-identity history gate, model hash, and diagnostic; `ofts/test_regime.py` integration tests; workflow runs new tests.
- Frozen 2026-10-09 predictions remain immutable. No revised full-universe rank is yet certified; 77.597 must not be reused as valid.
- Verified full-universe rescore: run 38046200050, 5,502 symbols, 3,977 numeric research scores; IQMX excluded (68 of 340 raw bars after July 2), provisional new #1 SCYX 67.197. Full Top 25: `ofts/validation/full_universe_identity_rescore_2026-10-10.md`.
- Next: verify daily persistence, extend identity registry to other corporate-action/ticker-change cases, then test predictive power against untouched holdouts.

## Recent-swing decay / lower-high-and-low structural-risk challenger (2026-10-10)

- User required a separate test for **last several completed swing amplitudes and cadence** to detect fading oscillation, and for **two successive lower highs and lower lows** to flag downside structural weakness without automatically discarding profitable downward swings.
- Code committed: `ofts/research/swing_health.py`, worker and daily integration, `ofts/test_swing_health.py`, daily and universe CI checks. SSOT locked under last-four-swings section.
- Verified 5,502-universe run 38046622126, **3,977** scored, all scored symbols assigned experimental swing health. Counts: **2,291 INSUFFICIENT**, **637 IRREGULAR**, **109 DECAYING**, **103 DOWNTREND**, **15 DOWNTREND_WEAK_BOUNCE**, **725 STABLE_RANGE**, **97 STABLE_UPTREND**. Saved Top 25 and high/low flags: `ofts/validation/swing_health_v01_2026-10-10.md`.
- Examples: SCYX #1 67.197 **STABLE_RANGE / REVIEW**; HNRG #2 65.889 **DOWNTREND / REVIEW** (lower highs and lower lows); MIR #3 64.881 **IRREGULAR / experimental NO_TRADE**; CHTR #5 63.990 **IRREGULAR / experimental NO_TRADE**; HLIT #21 61.809 **STABLE_RANGE / REVIEW**.
- All new swing-health classifications are **experimental**, NOT an official BUY/SELL decision, not proof of profitability. Unchanged v2.3 research scores, immutable prior cohorts and original cycle ledger preserved.
- Next: verify daily workflow test/persistence, then prospectively audit avoided losing entries and **missed profitable swings** with benchmark and fixed-horizon outcomes before any production promotion.
