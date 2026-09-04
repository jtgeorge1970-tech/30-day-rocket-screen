# Quality Loser Reversal Engine V2 — Locked SSOT

## Golden Rules

1. Never guess or assume.
2. No shortcuts or skipped stages.
3. Follow the SSOT: verify first, then act.

## Objective

Find an intact, liquid U.S.-listed business after a material selloff, near a
defensible bottom, with at least 15% chart headroom and a credible positive
catalyst expected in the next 5–30 days. The target is to capture the move from
support rather than buy after most of the move has occurred.

The biggest-loser list is a discovery pool, never a buy list.

## Complete funnel

1. Process the full U.S.-listed common-stock/ADR universe.
2. Exclude non-common structures and require price >= $3, average dollar volume
   >= $2M/day, and market cap >= $200M.
3. Require both a recent shock and a meaningful drawdown: a daily loss of at
   least 6% in the last 20 sessions or a five-session loss of at least 12% in
   the last 30 sessions, plus a current drawdown of at least 15% from the
   52-week high. A slow chronic decliner does not qualify merely for being down.
4. Require price to remain within 12% of its 60-session low. A rebound that has
   already traveled too far is late, even if momentum is strong.
5. Apply automated business triage and require at least 60% coverage of the
   locked balance-sheet/growth fields. Missing fields receive no invented score
   and never constitute proof that the business is intact.
6. Require bottom confirmation: the 60-session low is at least two sessions old,
   a higher five-session low, a reclaim of the prior high or 10-day average, and
   at least four of five confirmation signals (higher low, reclaim, fading sell
   volume, strong close location, no fresh low).
7. Require entry geometry: nearest meaningful resistance >= 15% overhead;
   support <= 8% below entry; a 10% disaster stop below support; and that stop
   at least 2.25 ATR from entry so ordinary noise does not trigger it.
8. Require stability: the complete technical setup passed in at least two of the
   last three completed sessions.
9. Research no more than the top 25 survivors, applying the same current manual
   verification to every stock.
10. A stock reaches `ENTRY_READY` only when every current manual gate is PASS.
    If none passes, the decision is cash/no new purchase.

## Current manual gates — all mandatory

- Selloff cause is known and is not a thesis-breaking event.
- Operating business remains intact.
- Balance sheet/liquidity can support the next 30 days.
- No material financing, dilution, accounting, regulatory, or binary-event risk.
- A specific, credible, positive catalyst lies 5–30 days ahead. A past earnings
  event, an old announcement, or “momentum” is not a future catalyst.
- Daily, weekly, and intraday charts all support the same entry thesis.
- Current market regime permits a new long position.
- Evidence is timestamped, sourced, and no more than 24 hours old.

One failed or unresolved manual gate is a veto. Scores cannot compensate.

## Ranking

Ranking occurs only among stocks that pass the same preceding gates. It is a
tie-breaker, not permission to bypass a gate:

- bottom/entry quality: 50%
- automated business quality: 30%
- loss-event severity: 20%

The engine must display every gate and raw metric beside the score.

## Active positions

Every active holding is audited on every run even if it is outside the candidate
pool. Candidate rank changes do not create an automatic sell signal. Existing
positions remain governed by their individual entry, stop, thesis-break, +10%
trigger, and 30-day clock in `POSITION_TRACKER_SSOT.md`.

## Audit rule

Save every funnel stage, all failures, all gate values, the current-verification
worksheet, the entry-ready file (even when empty), and the active-position audit.
No final recommendation may be stated unless the `ENTRY_READY` file contains a
freshly verified survivor.
