# OFTS point-in-time signal-to-ledger reconciliation and confidence-veto feasibility — 2026-10-29

**Research-only diagnostic. Not a strategy backtest or a live-trading recommendation.** Permanent frozen state: `ofts-daily-state` commit `db85bcc4d941063fbbdf77f264ceda7feb81cd15`; market as-of **2026-10-29**. No scoring, signal, position, or frozen cohort was changed. No brokerage orders.

## Method

Read exactly 15 dated frozen signal files `signals/YYYY-MM-DD.json` for NYSE sessions Oct 9, 12–16, 19–23, 26–29, 2026. Count each row's `signal.state`, retaining rows with absent signals as ineligible rather than inventing NO_TRADE. Join each BUY on `(symbol, signal_date)` to `cycle_ledger.json` entry records (open, pending, and closed) using `entry_signal_date`. Check unmatched BUYs against ledger exceptions; join each SELL to a closed or pending exit or a `NO_OPEN_POSITION` exception. Classify entry-time confidence using `cycle` for positions and `entry_cycle` for closed trades. Do not evaluate current-day prices or refit thresholds. This is an **event reconciliation and censoring audit**, not a causal out-of-sample test.

## Reconciled event accounting

- **2,091** signal-file rows across 15 dated sessions: **37 BUY**, **18 SELL**, **2,032 NO_TRADE**, **4 without a signal** (Oct 9 ARCL, CATL, EROC insufficient history; AKO.A stale). These four are not silently counted as NO_TRADE.
- **37 BUY events** produce **36 distinct ledger entry opportunities**: **33 open or pending-exit positions**, **2 closed trades**, **1 pending entry**. The remaining event is **DNTH BUY on Oct 28**, correctly recorded as `POSITION_ALREADY_EXISTS`: DNTH was already hypothetically entered Oct 27 from an Oct 26 BUY. It is **not** a missing trade or a second independent position.
- **18 SELL events** reconcile as **15 `NO_OPEN_POSITION` exceptions**, **two completed exits** (YDES, MF), and **one `OPEN_PENDING_EXIT`** (CCS, scheduled next-session Oct 30). No unmatched SELL event remains.
- Entry-time confidence across **36** unique opportunities: **18 LOW**, **17 MEDIUM**, **1 HIGH**. Outcomes are **33 open, 2 closed, 1 pending**. LOW includes **15 open, 2 closed, 1 pending**; MEDIUM includes **17 open**, HIGH includes **one open**. Note that `OPEN_PENDING_EXIT` is included in open.
- Entry score bands across 36: **3 below 40**, **27 from 40 to under 60**, **6 at least 60**. Model versions: **35 v2.3** and **one earlier model** (YDES's first trade). Do not pool their realized results as proof of a model-version edge.
- Only two closed trades: **YDES -39.144%** net (earlier model, LOW confidence), **MF -23.840%** net (v2.3, LOW confidence); equal-weight completed net **-31.492%**. Their matched SPY price returns are **-2.424%** and **-0.234%** respectively.

## Controlled confidence-veto feasibility check (NOT validated performance)

A hypothetical predeclared **exclude-LOW** rule would reject **18 of 36** entry opportunities (50%). It would exclude **both** observed closed losers, but also **LYEL**, a LOW-confidence Oct 19 BUY that the ledger entered hypothetically Oct 20 at $8.74 and that was still open after its reported Oct 28 rise. Crucially, **all 18 retained MEDIUM/HIGH opportunities are still open**; there are **zero closed trades** with which to estimate their net performance. The apparent 2-for-2 loser removal is pure **outcome censoring / hindsight selection**, not evidence that the filter works. A score >=60 veto similarly cannot be validated from completed trades. Neither rule should be deployed based on these data.

## New operational/reporting conclusion

The frozen BUY and position ledger are internally reconcilable; however, a daily-only BUY/SELL/NO_TRADE report can falsely suggest an earlier successful BUY was missed, because a later NO_TRADE means **no new turn**, not **no active position**. Daily user reports should explicitly show **new signals AND carried open positions**, including LYEL, with entry date, score, confidence, and status. Do not report unrealized marks as completed returns. This visibility issue is distinct from trading profitability.

## Limits and decision

No matched-stock alternative-entry or passive price series, IWM paired horizon, quote-based fills, portfolio drawdown, or independent holdout trade sample was established by this event audit. Forward 5/10-session averages in `validation_summary.json` are overlapping candidate/control observations and must not be equated with the two completed BUY-to-SELL trades. Current gate remains **RESEARCH_ONLY_NO_GO**. Future confidence and stop/cooldown experiments must be predeclared and assessed on later **chronological, independent completed trades** with realistic costs.

Source paths at snapshot: `signals/2026-10-09.json` through `signals/2026-10-29.json` on the 15 listed sessions, `cycle_ledger.json`, `latest_audit.json`, `validation_summary.json`, `AUDIT_REPORT.md` on `ofts-daily-state`. Workflow https://github.com/jtgeorge1970-tech/30-day-rocket-screen/actions/runs/40729515105 (attempt 3), artifact 12940681367.
