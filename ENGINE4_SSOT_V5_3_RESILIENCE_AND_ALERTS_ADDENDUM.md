# Engine 4 SSOT v5.3 — Provider Resilience and Immediate Alerts

This addendum is binding and extends the existing Engine 4 SSOT without weakening
any catalyst-identity, price, entry, risk/reward, or no-chase gate.

## 1. Provider failures do not erase the queue

- A failure by one news or quote provider must not terminate the full Engine 4 run.
- A candidate with missing required evidence fails only the affected gate and cannot
  receive an official BUY or ARM instruction until that evidence is verified.
- Other candidates with valid evidence continue through ranking and live review.
- If all providers for a required live field are unavailable, Engine 4 completes in
  a degraded state, preserves its ranked/recovery queues, and authorizes no order.

## 2. Verified news chain

The ordered catalyst sources are Google News RSS, Bing News RSS, then Nasdaq company
news. Every source is discovery evidence only. Catalyst credit still requires the
exact ticker plus verified company identity and must pass freshness, negative-news,
and promotional-content filters. If no source yields a verified catalyst, catalyst
quality is zero; the stock may remain an alternate but cannot be graded as an
official catalyst-backed setup.

## 3. Live quote chain

The three-shot quote chain is Nasdaq real-time quote, Yahoo quote fallback, then Cboe
delayed quote fallback. Cboe is independent but explicitly delayed: it may preserve
and rank an alternate, never satisfy the order-authoritative spread gate. If neither
real-time-capable path returns a valid bid, ask, and spread, only that ticker's live
order gate fails. The engine continues evaluating alternates and keeps the recovery
queue intact. A future authenticated broker quote may replace Cboe as the third,
order-authoritative path without changing this safety rule.

## 4. Event-driven notifications

The production workflow must send an immediate, deduplicated real SMS through the
user's existing OpenPhone/Quo account for the final result, recovery result, and
pipeline failure. GitHub Issues remains the independent audit trail and fallback
notification channel. OpenPhone credentials and both phone numbers must exist only
as encrypted GitHub Actions secrets; they must never be committed to the repository.
The alert contains the Engine 4 instruction and workflow link. Fixed-time ChatGPT
reports remain secondary summaries; they are not the immediate delivery mechanism.

No alert creates authority to trade. An official BUY or ARM still requires every
locked Engine 4 gate and a confirmed live broker quote.
