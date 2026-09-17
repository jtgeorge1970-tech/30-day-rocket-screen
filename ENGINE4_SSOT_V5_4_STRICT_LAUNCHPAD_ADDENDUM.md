# Engine 4 SSOT v5.4 — Strict B-or-Better Launchpad

Locked: 2026-09-17

This addendum is binding and supersedes every earlier Engine 4 provision that
allowed a sub-80 score or a premarket evidence-gate failure into the official
09:45 launchpad or post-open recovery queue.

## 1. Honest 80-point floor

- The existing 100-point model and component weights remain unchanged.
- Scores must not be inflated, curved, normalized, or recalibrated to create
  candidates or fill a capacity.
- A raw score of at least 80.00 is required for launchpad eligibility.
- Conventional grades are B = 80.00–89.99, A = 90.00–94.99, and A+ =
  95.00–100.00.
- Any score below 80 is REJECT for trading purposes and remains audit-only.

## 2. Every premarket evidence gate remains mandatory

The numerical floor never overrides missing evidence. An eligible candidate must
also have all of the following:

- verified positive catalyst tied to the exact ticker and company identity;
- qualifying true premarket RVOL or Nasdaq premarket-volume intensity;
- ATR of at least 1.5% of price;
- positive room to resistance;
- authoritative real-time-capable bid/ask spread no greater than 0.60%.

A provider failure degrades only the affected evidence gate and does not abort the
full engine, but an unverified candidate cannot enter the official launchpad.

## 3. Capacities are never quotas

- Top-25, Top-10, Top-5, and Top-3 are maximum capacities.
- The engine must never pad any list with a weaker candidate.
- A valid daily launchpad may contain 25, 10, 5, 3, 1, or zero stocks.
- Zero eligible stocks is a successful completed run whose result is:
  `NO TRADE — no B-or-better premarket candidates. DO NOT BUY.`

## 4. No post-open promotion of rejects

- Sub-80 and evidence-gate-failing names receive no 09:45 live analysis and no
  recovery-watch slot.
- A brief opening move cannot transform a rejected premarket candidate into an
  official Engine 4 trade.
- The final stage must revalidate the frozen eligibility fields before analyzing
  opening structure or issuing BUY/ARM instructions.

## 5. Audit preservation

The complete deep ranking, including rejected names, scores, component points, and
failure reasons, remains preserved for measurement and future review. Audit
visibility never grants trading eligibility.
