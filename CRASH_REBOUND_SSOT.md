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

1. 🟡 Finish Stage 1 classification on the existing September sample
   - Classification buckets: Probable Overreaction / Uncertain / Justified
   - Current issue: the complete September working dataset must be recovered/rebuilt and verified before this step can be completed.

2. 🔴 Finish the outcome fields for every classified crash
   - Crash %
   - Catalyst
   - Close position in day range
   - Relative volume
   - Next-day rebound
   - 3-day rebound
   - 5-day rebound
   - Maximum additional downside

3. 🔴 Run the first real separation test
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
- Steps 2–7: 🔴 Not complete / not started.

- Step 2: 🟡 Working — observable outcomes through 2026-09-30 populated. 75/100 rows have full 5-session outcome windows; 25/100 are pending future market sessions. Day-1 available for 93/100; Day-3 for 81/100; Day-5 for 75/100; max 5-day additional downside for 93/100.
