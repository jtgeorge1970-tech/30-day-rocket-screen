# Extreme-Winner Continuation Engine — Locked SSOT

## Golden Rules

1. Never guess or assume.
2. No shortcuts or skipped stages.
3. Follow the SSOT: verify first, then act.

## Objective

Find rare, liquid U.S.-listed stocks whose extreme upward move is supported by
real demand and a credible catalyst, and whose structure leaves a realistic
path to at least another 10% over approximately 30 sessions. The engine studies
continuation; it never assumes that a large gain will continue.

One fully qualified opportunity in a month is sufficient. Zero candidates on
any day, week, or month is valid. Thresholds may not be loosened to create a
trade.

## Separation

This is Engine #3. It is separate from the original three-lens Rocket Engine
and the Quality-Loser Reversal Engine. It may not overwrite, replace, or
silently change either engine. Only measured out-of-sample expectancy and alpha
may determine which engine is best.

## Universe and investability

1. Process the complete Nasdaq Trader U.S.-listed security universe.
2. Retain common stocks and ADRs; exclude ETFs, test issues, warrants, rights,
   units, preferreds, acquisition shells, SPAC-like structures, and other
   obvious non-common securities.
3. Require event-date price >= $3.
4. Require trailing 20-session average dollar volume >= $2 million.
5. Require current market capitalization >= $200 million for the live screen.

## Extreme-winner event

An event requires at least one of:

- one-session close-to-close return >= +20%; or
- five-session close-to-close return >= +30%.

The engine examines every event in the latest 30 completed trading sessions.
The current screen uses the most recent event per ticker and requires the move
to retain a valid continuation structure at the present close. The cohort study
applies a ten-session same-ticker cooldown so a single run is not counted
repeatedly.

## Automated continuation gates

Every live candidate must pass all of these gates before ranking:

- event close in the upper 70% of the daily range;
- event volume at least 3.0 times the prior 20-session average;
- current price retains at least half of the event-day range;
- current price remains above its 10-session moving average;
- current extension above the 20-session average is no greater than 35%;
- 14-session ATR is no greater than 5% of price, so the locked approximately
  -10% disaster stop is not obviously inside ordinary two-ATR noise;
- event occurred within the latest 30 completed trading sessions;
- core price, volume, liquidity, and market-cap data are present.

Passing these rules creates a quantitative research candidate, not a buy.

## Ranking funnel

Process the full universe and preserve an auditable funnel of up to:

**50 → 25 → 10 → 5 → 3**

Never fill a stage with stocks that failed a gate merely to reach its nominal
size. Rank only gate-passing stocks using observable evidence:

- event strength and five-session acceleration;
- abnormal volume;
- event close location and gap retention;
- SPY-relative strength;
- post-event hold quality;
- liquidity;
- volatility and extension risk;
- available business-quality evidence.

Ranking is a tie-breaker. It cannot override a failed gate.

## Current verification — all mandatory

Each Top 3 stock must receive a sourced review no more than 24 hours old:

- a specific, credible catalyst capable of supporting continuation;
- confirmation that the news is new and not recycled;
- operating/business quality remains acceptable;
- no unacceptable ATM, shelf, warrant, convertible, lockup, or other supply
  risk;
- float and ownership do not create unacceptable manipulation risk;
- current spread and liquidity are executable;
- premarket/opening-range/VWAP/higher-low structure confirms the entry;
- sector and broad-market regime permit a new long position;
- a roughly -10% disaster stop is below meaningful support and outside normal
  noise;
- at least 10% practical upside remains before material resistance.

One failed or unresolved manual gate is a veto. `ENTRY_READY` is allowed only
when every gate is `PASS` and `final_status` is `APPROVED`.

## Standardized finalist visual packet — mandatory

Every Top 3-5 finalist must receive a current multi-timeframe visual review
before promotion to `WATCH` or `ENTRY_READY`. This is a confirmation layer and
does not replace the automated gates or sourced current verification.

Review, when available:

- 1-day, 5-day, 1-month, 1-year and 5-year charts;
- current last price, bid, ask, spread and volume, with regular-session and
  extended-hours data clearly separated;
- candlestick/OHLC, volume and VWAP views, preferred over line charts for
  opening-range, reclaim, retest and higher-low confirmation;
- current earnings history, key financial statistics, ownership and analyst
  consensus as supporting evidence only.

Record support/resistance, gap retention, higher highs/lows, reclaim or failed
reclaim, close location, volume confirmation, extension, volatility,
liquidity/spread and remaining practical upside. Analyst ratings and attractive
charts cannot override a failed catalyst, business, supply/dilution, liquidity,
volatility, market-regime, downside or entry-geometry gate. If required visual
or intraday evidence is unavailable, the gate is `UNRESOLVED`, never assumed
to pass.

Retrieve the packet automatically when reliable data is available. Request
standardized screenshots only for the small finalist group when necessary;
never request them for the full universe. Preserve the reviewed packet or its
extracted observations in the audit record.

## Entry and exit research

- Historical measurement entry is the next session's open after the event.
- Primary outcome: +10% touched before -10% within 30 subsequent sessions.
- Same-bar target/stop touches are `AMBIGUOUS`; never assume the favorable path.
- Record +10%, +20%, and +30% target timing; 5/10/20/30-session returns;
  maximum favorable/adverse excursion; and 7%/10% trailing-stop variants after
  +10% activation.
- An unresolved event with fewer than 30 forward sessions is `OPEN`, never a
  win or loss.
- Live orders require a refreshed premarket/current check and a Fidelity limit
  order plan. The engine never places an order automatically.

## Historical-study limitations

The initial implementation uses the current listed universe and adjusted Yahoo
daily history. It excludes securities delisted before the run, lacks a fully
point-in-time security master/fundamental database, and cannot reconstruct
historical intraday VWAP or opening-range paths. Results are exploratory.

Promotion to a proven rule requires point-in-time data including delisted
issues, realistic spread/slippage estimates, purged walk-forward validation,
an untouched final test period, and sufficient observations across market
regimes. No in-sample fingerprint may be called an edge.

## Audit rule

Save the starting universe, price failures, all detected events, investable
events, every ranking stage, current-verification template, `ENTRY_READY` file
(even when empty), historical event ledger, outcome partitions, fingerprint
summary, exit-policy comparison, and audit JSON files. Validators must fail
closed if counts, subsets, labels, thresholds, or entry-ready invariants break.
