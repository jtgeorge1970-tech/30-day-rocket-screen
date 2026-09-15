# Engine 4 — SSOT v5.0 Addendum
Locked: 2026-09-15

This addendum is part of the Engine 4 SSOT and supersedes any conflicting wording in `ENGINE4_SSOT.md` v4.9. All non-conflicting v4.9 rules remain locked and unchanged.

## Golden Rules
1. Never guess or assume.
2. No shortcuts or skipped steps.
3. Follow the SSOT exactly.
4. Verify before reporting completion.

## Why v5.0 exists
Live dry runs proved the selection engine can identify real movers, but two execution-layer gaps were exposed:

1. A high-priced stock can be an excellent Engine 4 research candidate yet be untradeable for the current roughly $200-$300 position size because Fidelity protective stop orders require whole-share execution in this workflow. A $350 stock therefore cannot be the official trade candidate.
2. A top-ranked stock can fail the initial 09:45 continuation/breakout setup, flush hard, form a new base, reclaim, and become an excellent second-chance trade later in the morning. The primary setup failure must not automatically throw away a strong candidate for the rest of the morning.

The v5.0 repair changes the execution/tradeability layer. It does NOT weaken or rebuild the successful premarket selection engine.

## Locked official trade-price cap
- Official live Engine 4 trades must have a fresh live share price <= $100.00.
- The existing minimum price remains $5.00.
- The reason is account-size/executability: current allocations are roughly $200-$300 per trade and the workflow requires multiple whole shares so the entire position can be protected by normal whole-share stop orders.
- Stocks above $100 may remain in the broad universe, scoring, Top-25, audit, and shadow validation so Engine 4's selection edge can still be measured.
- A stock above $100 can NEVER become the official BUY, ARM, or recovery trade while this cap is locked.
- If the best setup is above $100, label it SHADOW ONLY / ABOVE TRADE CAP and continue looking for an eligible <=$100 official candidate.
- The cap may be raised only when position sizing materially increases and the SSOT is explicitly revised.

## Locked primary entry instructions
The user explicitly requested broker instructions that are clear enough to execute without interpretation. This supersedes the prior v4.9 prohibition on using stop-limit terminology in the actionable instruction.

If a valid primary setup has not yet reached its trigger, the correct action is:

`PLACE BUY STOP-LIMIT NOW — [TICKER]`
`STOP PRICE: $X.XX`
`LIMIT PRICE: $Y.YY`
`TIME IN FORCE: DAY`
`CURRENT PRICE: $C.CC`
`IF FILLED, ENTER GTC SELL STOP AT $S.SS`
`IF PRICE THEN RISES TO $T.TT, MOVE SELL STOP TO $P.PP`
`DO NOT CHASE ABOVE $Y.YY`

Meaning:
- below the stop/trigger, nothing happens;
- when the stop price is reached, the order becomes eligible to execute;
- Fidelity may fill only up to the stated limit price;
- if price gaps above the limit, do not chase.

`BUY NOW` remains reserved for a fresh price already inside the valid buy band.

## Stage 5 — Post-open Hook-Set / Recovery Watch
After the 09:45 final confirmation, Engine 4 must not permanently discard every top candidate that failed the primary continuation setup.

The engine must create a small RECOVERY WATCH consisting only of strong, already-ranked candidates that:
- came from the frozen Top-25;
- failed the primary 09:45 setup rather than failing the entire premarket selection thesis;
- have fresh price <= $100;
- do not have a hard broad-market reversal invalidation;
- remain technically capable of forming a second setup.

Carry no more than the strongest 5 recovery candidates. This is a configured cap and must be labeled as such.

### Recovery watch schedule
- Starts immediately after the 09:45 primary final stage.
- Rechecks only the small recovery list, not the full universe.
- Default polling interval: every 5 minutes.
- Recovery window closes at 11:30 ET unless a valid order is armed/buy signal is generated earlier.
- If an official <=$100 primary BUY/ARM is already active, the recovery module stays on standby and must not create a competing official order.

### Locked recovery pattern
The recovery module exists specifically to detect a VERA-style sequence:

`hard opening flush -> selling exhaustion/base -> higher low -> improving demand -> reclaim trigger`

A recovery setup must satisfy all of the following before it can be armed:
- opening/session flush from high to low >= 3.0%;
- the session low must be at least 8 one-minute bars old;
- a confirmed higher low must form at least 0.20% above the session low;
- recent base range <= 3.0% of current price;
- at least 2 of the latest 4 bars are green;
- recent demand volume is improving: latest four-bar average volume >= 1.05x the preceding comparison baseline;
- refreshed live spread <= 0.60%;
- fresh live price <= $100;
- no new structural low invalidation.

These thresholds are intentionally deterministic for dry-run validation and must be measured before any later tuning.

### Recovery trigger and order
Once the recovery base is valid:
- RECOVERY ENTRY TRIGGER = recent base high + 0.05% confirmation buffer.
- MAXIMUM BUY PRICE = recovery trigger + 0.50% chase band.
- INITIAL STOP = just below the confirmed recent higher-low support using the locked 0.20% stop buffer.
- FIRST MANAGEMENT LEVEL = 2.5R unless a future explicit SSOT revision adds a nearer verified resistance rule.
- PRECALCULATED PROFIT STOP = trigger + 0.50R, same deterministic profit-lock architecture as the primary setup.

If current price is below the recovery trigger:

`PLACE RECOVERY BUY STOP-LIMIT NOW — [TICKER]`
`STOP PRICE: $X.XX`
`LIMIT PRICE: $Y.YY`
`TIME IN FORCE: DAY`
`CURRENT PRICE: $C.CC`
`IF FILLED, ENTER GTC SELL STOP AT $S.SS`
`IF PRICE THEN RISES TO $T.TT, MOVE SELL STOP TO $P.PP`
`DO NOT CHASE ABOVE $Y.YY`

If current price is already inside the valid recovery buy band:

`RECOVERY BUY [TICKER] NOW`
`BUY BETWEEN $X.XX AND $Y.YY`
`AFTER PURCHASE, ENTER GTC SELL STOP AT $S.SS`
`IF PRICE RISES TO $T.TT, MOVE SELL STOP TO $P.PP`
`DO NOT BUY ABOVE $Y.YY`

If price has already run beyond the chase band, the engine must not chase. It continues observing for a new valid base until 11:30 ET.

## State transition repair
`ABORT MISSION` is no longer an acceptable automatic outcome merely because the first 09:45 setup failed.

The correct states are:
- PRIMARY BUY / PRIMARY ARM — first setup is actionable.
- PRIMARY FAILED — KEEP ON HOOK — strong candidate failed the first setup but remains recovery-eligible.
- RECOVERY WATCH — monitor for exhaustion/base/higher-low/reclaim.
- RECOVERY ARM — valid second-chance base exists; stage the buy stop-limit.
- RECOVERY BUY — trigger is confirmed and fresh price is inside the buy band.
- TRUE ABORT — recovery window expired, structural invalidation persists, data failed, or another locked fail-safe applies.

## Dry-run validation rule
Engine 4 remains in proof/validation mode while these changes are evaluated. For each dry run preserve:
- primary top candidate(s);
- official tradability status;
- shadow-only high-priced candidates;
- recovery-watch list;
- every recovery scan's measured state where available;
- whether a recovery ARM/BUY would have triggered;
- subsequent observed price behavior.

Do not call the new recovery thresholds optimized or proven from one VERA example. VERA is the motivating live example, not sufficient statistical validation.

## Reporting artifacts
Production must preserve:
- `final_live_audit.json` — primary 09:45 audit including official tradeability and shadow-only status;
- `recovery_watch.json` — up to the 5 strongest failed but recovery-eligible candidates;
- `recovery_audit.json` — latest measured recovery conditions and failure reasons;
- `recovery_signal.json` — current recovery state/action;
- `recovery_alert.txt` — plain-English recovery instruction.

## Non-negotiable separation of success/failure
A correct report must distinguish:
- SELECTION SUCCESS: Engine 4 found/ranked the mover;
- PRIMARY ENTRY SUCCESS/FAILURE: whether the first setup was captured;
- RECOVERY SUCCESS/FAILURE: whether the second-chance hook-set module captured a later valid setup;
- EXECUTION SUCCESS/FAILURE: whether the user/broker order was actually placed and filled.

Do not label a selection-engine success as an engine failure merely because the execution layer missed the move, and do not label a selection success as a completed trading success unless the entry was actually executable.
