# Crash Rebound — Single Source of Truth (SSOT)

## Locked purpose
Build and validate a crash-rebound trading framework without hindsight, shortcuts, moving goalposts, or unsupported claims.

## Locked reporting rule
Progress is reported only against the seven original processing steps below.
Do not add, split, rename, or substitute extra milestones to make progress appear greater.
A step is marked complete only when that exact step is finished and verified against source data.

Status symbols:
- ✅ Complete
- 🟡 Working
- 🔴 Not started / not complete

## Original seven processing steps

1. ✅ Finish Stage 1 classification on the existing September sample
   - Classification buckets: Probable Overreaction / Uncertain / Justified
   - September source reconstruction and pre-rebound classification are complete at 100/100.

2. 🟡 Finish the outcome fields for every classified crash
   - Crash %
   - Catalyst
   - Close position in day range
   - Relative volume
   - Next-day rebound
   - 3-day rebound
   - 5-day rebound
   - Maximum additional downside

3. 🟡 Run the first real separation test
   - Compare Probable Overreaction vs Justified
   - Rebound frequency
   - Median rebound
   - Rebound speed
   - Additional downside before recovery

4. 🔴 Define the usable Crash Rebound trigger
   - Only after Step 3 shows real separation
   - Candidate ingredients may include crash size, catalyst type, range behavior, volume, and next-session confirmation

5. 🔴 Stress-test the trigger
   - Crash thresholds
   - Rebound definitions
   - 1/3/5-day holding windows
   - Maximum adverse excursion
   - False positives
   - Early vs delayed entry

6. 🔴 Out-of-sample validation
   - Freeze rules before test
   - No rule changes after seeing validation results

7. 🔴 Final go/no-go evidence package
   - Sample size
   - Win rate
   - Median gain
   - Average gain
   - Worst drawdown
   - P/L distribution
   - Failure types
   - Exact entry/exit rules

## Hard acceptance gates
- No guessing or gap-filling.
- No hindsight classification.
- No changing the seven-step progress framework.
- No support activity reported as milestone completion.
- No green check without source verification.
- Fewer verified results are preferred over more borderline results.
- If a required source is missing, mark the step blocked/working rather than infer completion.

## Current verified project status
- Step 1: ✅ COMPLETE — September source dataset reconstruction is 100/100 and pre-rebound classification is 100/100. Consistency check passed: 100 rows, 100 unique ranks, no missing ranks, no duplicates.
- Step 2: 🟡 Working — observable outcomes through 2026-09-30 populated. 75/100 rows have full 5-session outcome windows; 25/100 are pending future market sessions. Day-1 available for 93/100; Day-3 for 81/100; Day-5 for 75/100; max 5-day additional downside for 93/100.

- Step 3: 🟡 Working — first regime-separation pass completed on the frozen 400-event development set. The simple classification and simple regime flag are not sufficient alone. The strongest current candidate intersection is Probable Overreaction + crash <= -30% + relative volume >= 5x (N=12): Day-5 median +12.47%, Day-10 median +12.78%, 75% positive at both horizons, median Day-10 excess vs SPY +8.12%, median max additional downside through Day 10 -5.75%. However March reverses after Day 3 while April/August drive the pooled strength, so this is not yet a universal trigger. Full details are locked in crash_rebound/stage3_regime_separation.md and crash_rebound/stage3_regime_separation.csv.
- Development stress-test note: the strongest non-month-confounded candidate zone currently is Probable Overreaction + crash >=30% + relative volume >=5x + RSP prior-5 > -1%. In the frozen development sample this produced N=8 across March/April/August, Day-10 win rate 87.5%, median Day-10 +15.61%, and median max additional downside through Day 10 -1.99%. Nearby crash/volume thresholds remained directionally positive, supporting a zone rather than a single knife-edge cutoff. This is not yet a frozen Step-4 trigger or Step-5 completion.

## Additional development cohort — August 2026
- Purpose: compensate for the 25 late-September crashes whose full five-session outcomes do not yet exist, without deleting or changing any September case.
- August source cohort: 100/100 ranked events reconstructed; integrity check passed (100 rows, 100 unique ranks, no missing ranks, no duplicates).
- August mature outcomes: 100/100 have Day-1, Day-3, Day-5, and five-session maximum additional downside from Alpaca IEX daily bars.
- Close position in crash-day range: 100/100 available.
- Relative volume vs prior-20-session median (IEX): 99/100 available; XTNT lacks enough usable prior IEX volume history for this derived field and remains blank rather than guessed.
- August pre-rebound classification is COMPLETE at 100/100 using a conservative acceptance gate: 11 Probable Overreaction, 6 Justified, 83 Uncertain. Only clearly supported cases were forced into directional buckets; ambiguous earnings/clinical/other events remained Uncertain.
- August remains DEVELOPMENT data only. It is not the frozen out-of-sample validation set for Step 6.

## Extended rebound horizons — Day 10 / 20 / 30
- Added to both August and September outcome tables: Day 10, Day 20, Day 30 return from crash close, plus maximum additional downside through Day 10, Day 20, and Day 30.
- August availability as of 2026-09-30: Day 10 = 99/100, Day 20 = 99/100, Day 30 = 85/100. The missing late-horizon cells are future-dependent or lack usable market bars and remain blank rather than guessed.
- September availability as of 2026-09-30: Day 10 = 58/100, Day 20 = 7/100, Day 30 = 0/100. These are preserved as pending future observations.
- Existing Day 1 / 3 / 5 fields remain unchanged.
- Preliminary August high-confidence separation remains strongest through Day 10; longer-horizon medians weaken materially by Day 20/30, so the current signal looks more like an early-rebound effect than a persistent 30-day drift. This is exploratory development evidence, not a final trigger.

## March 2026 risk-off development cohort
- Purpose: test whether the crash-classification effect survives materially different market conditions from August/September.
- Source cohort: 100/100 StockTitan March 2026 ranked losers reconstructed; integrity gate passed.
- Outcomes: Day 1/3/5 complete for 100/100; Day 10/20/30 complete for 99/100; one later-history gap remains blank rather than guessed.
- Market context attached per crash: SPY, IWM, RSP and QQQ crash-day and prior-5-day returns; forward SPY/IWM/RSP returns and stock excess returns through Day 30.
- Regime mix using prior-5-day SPY/IWM/RSP average: 82 mild risk-off, 11 broad risk-off, 7 mild risk-on.
- Conservative pre-rebound classification: 15 Probable Overreaction, 13 Justified, 72 Uncertain. Classification used only contemporaneous announcement/catalyst information and did not use post-crash outcomes.
- Preliminary result: unlike August, March does NOT show the same early long-vs-short separation. Probable Overreaction median raw returns were -0.17% Day 1, -3.77% Day 5, -6.84% Day 10; median excess vs SPY was -0.26%, -5.04%, -7.06%. This suggests market regime and/or classification refinement materially matters. Do not define the final trigger from August alone.

## April 2026 strong risk-on development cohort
- Purpose: complete the intended development-regime spectrum before freezing the framework.
- Source cohort: 100/100 StockTitan April 2026 ranked losers reconstructed.
- Outcomes: crash-date bars 100/100; Day 1/3/5/10/20/30 available for 99/100; missing cells remain blank rather than guessed.
- Market context attached per crash: SPY, IWM, RSP and QQQ crash-day and prior-5-day returns, plus forward SPY/IWM/RSP returns and stock excess returns through Day 30.
- Regime mix using prior-5-day SPY/IWM/RSP average: 29 broad risk-on, 40 mild risk-on, 31 mild risk-off.
- Conservative pre-rebound classification: 11 Probable Overreaction, 21 Justified, 68 Uncertain.
- April Probable Overreaction medians: Day 1 +3.64%, Day 3 +1.06%, Day 5 +1.01%, Day 10 -1.45%, Day 20 -3.64%, Day 30 -4.23%.
- April Justified medians: Day 1 0.00%, Day 3 +4.41%, Day 5 -0.10%, Day 10 +5.49%, Day 20 +2.20%, Day 30 +6.59%.

## Development framework freeze after April cohort
- Development months now include March, April, August, and September 2026. Do not add or remove development months merely because their results are favorable or unfavorable.
- Do not change the pre-rebound classification labels after reviewing post-crash outcomes. Any future rule refinement must be documented as a new candidate rule before out-of-sample validation.
- Current pooled classified sample across four months: 400 crash events = 70 Probable Overreaction, 65 Justified, 265 Uncertain.
- Pooled available raw medians (unequal horizon maturity must be respected): Probable Overreaction Day 1 +0.68%, Day 3 -0.69%, Day 5 -2.74%, Day 10 -4.18%; Justified Day 1 -1.09%, Day 3 -0.95%, Day 5 -0.72%, Day 10 -1.03%; Uncertain Day 1 -0.64%, Day 3 -1.27%, Day 5 -0.71%, Day 10 -2.78%.
- Interpretation: the simple three-way headline classification alone is not sufficient as a universal standalone long/short trigger. Market regime appears material and must be tested explicitly in Step 3 rather than tuned retrospectively.
- Targeted expansion falsification: five untouched 2026 months (Jan/Feb/May/Jun/Jul) were screened with the frozen numeric criteria crash >=30%, relative volume >=5x, RSP prior-5 > -1%. From 500 source events, 111 passed numerically; 20 were conservatively classified as clear Probable Overreaction before outcome review. Their Day-10 result was only 40.0% positive with median -3.01% and median max additional downside -17.58%. This materially fails to reproduce the earlier 8-case development result. The current candidate must NOT be frozen as a Step-4 trigger. Outcome source for this expansion pass was Yahoo Finance via yfinance because the Alpaca connector repeatedly failed; reconcile source consistency before final evidence package.
- Targeted expansion check (Jan/Feb/May/Jun/Jul 2026): the frozen candidate did NOT replicate. Of 500 source events, 111 passed crash>=30%, RV>=5x, RSP prior-5>-1%; 17 were frozen pre-outcome as Probable Overreaction. Those 17 had Day-10 win rate 35.3%, median -2.53%, median excess vs SPY -0.75%, and median max additional downside -17.45%. The prior 8-case development pocket must therefore be treated as non-validated / likely sample-specific. Do not promote it to Step 4 trigger without a different, pre-specified hypothesis.
- Make-or-break technical test: news/opinion classification was removed from the decision layer and the 111 mechanically selected untouched-month crashes were tested using only Day-1 tape behavior. Strongest broad executable candidate: crash>=30%, RV>=5x, RSP prior-5>-1%, Day1 holds crash low, Day1 closes above crash-day midpoint, Day1 gap>-5%, entry at Day1 close. N=22; Day10 win rate 63.6%; median post-entry return +8.07%; mean +5.74%; 25th percentile -5.12%; worst -19.85%. Nearby natural refinements did not materially improve the result. Simple fixed stops reduced expectancy. Candidate is not validated and must be frozen before any untouched validation test.
