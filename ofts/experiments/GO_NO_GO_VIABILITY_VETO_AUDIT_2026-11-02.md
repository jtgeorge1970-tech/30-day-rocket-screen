# OFTS point-in-time BUY / viability-veto audit — 2026-11-02

**Frozen source:** `ofts-daily-state` commit `eb05038a4e793e5ecb844b8fcd321e3ccb8e9db9`, latest qualified market session 2026-10-30. **Research-only.** This report does not incorporate any later cohort or rewrite frozen data.

## Test and controls

Read the 16 uniquely dated saved `signals/YYYY-MM-DD.json` files (2026-10-09 through 2026-10-30, excluding `-qualified` duplicates). For every original, point-in-time BUY event, read the *already-frozen* experimental `recent_viability.proposed_entry` and `state`. Reconcile each signal date and symbol with `cycle_ledger.json`. No thresholds were tuned, no future returns were used to classify signals, and no brokerage orders were placed. The experimental viability filter is **not** production-approved.

## Results

- **39 BUY events** across 16 signal cohorts; **38 distinct ledger entries** (33 open, two pending, three closed). The extra event is DNTH's October 28 repeated BUY while the original position was already open; the ledger correctly prevented a duplicate entry.
- Of 39 BUY events, **38 had an experimental viability assessment, and all 38 proposed NO_TRADE**. **Zero** were approved by that filter. The first YDES BUY on October 9 lacked a recorded experimental viability assessment; this is missing, **not** a pass or veto.
- Experimental states among the 38 vetoes: **TOO_SMALL_UPSIDE 16; CYCLE_TIMING 10; FADING 6; WATCH 5; STALE_UPSIDE 1**. WATCH is still a proposed NO_TRADE, not a BUY.
- Original BUY confidence: LOW 19; MEDIUM 19; HIGH 1. The proposed veto would suppress all assessed confidence levels, not merely LOW confidence.
- **LYEL** generated an original BUY on **October 19**, score **44.513**, LOW confidence, and entered the hypothetical ledger October 20 at $8.74. Its point-in-time experimental viability state was **TOO_SMALL_UPSIDE / NO_TRADE**. LYEL remained open at the source snapshot; its later favorable price movement is *not* a realized profit.
- The three closed hypothetical trades were **YDES -39.144%, MF -23.840%, CCS -4.367%** after the original 0.20% cost assumption. MF and CCS were vetoed by the experimental filter; first YDES had no experimental classification. **It would be invalid to claim the filter improves profitability by removing these losses:** the same filter also rejects LYEL and all other assessed BUYs, most of which are still open.

## Implication

The experimental viability filter has **zero positive coverage of original BUY opportunities** in this 16-cohort sample. As currently defined, applying it as a hard gate would result in **no assessed trades** and therefore no demonstrated return edge. This is a **validation failure of the filter's trade-selection usefulness**, not evidence that the original detector is profitable.

Do **not** deploy this veto or relax it by tuning on LYEL. A fair next experiment needs frozen, pre-specified thresholds and a genuinely later chronological cohort, including both selected and rejected stocks, executable next-open prices, liquidity/cost controls, matched same-stock passive/alternative entries, SPY/IWM, exits, and independent closed trades.

## Separate saved forward research context (not independent trade results)

From the same saved `validation_summary.json`, model v2.3's scored fixed-horizon observations (correlated, including research controls) are:

| Horizon | N | OFTS net with assumed 0.20% costs | Matched SPY price-only | Net excess |
|---|---:|---:|---:|---:|
| 5 sessions | 950 | +0.610% | -0.249% | +0.859 percentage points |
| 10 sessions | 491 | +2.238% | -0.684% | +2.922 percentage points |

At 1.00% assumed total costs, the five-session OFTS average would be **-0.190%** (mechanical +0.80-point adjustment). The 40-60 score band has a 5-session mean +1.165% (N=731), whereas the higher 60-80 band averages -0.238% (N=94). The saved worst adverse excursion among 40-60 observations is **-86.842%** at five sessions and **-88.158%** at ten sessions. These are *observed intrahorizon adverse excursions*, not closed-trade returns. There are no matured 20/30/60-session results at this snapshot.

The score-band reversal and tail exposures make the positive mean insufficient to establish a live-trading edge. No independent confidence interval is claimed because observations overlap.

## Reproduction

Run `python ofts/experiments/viability_veto_audit_20261102.py /path/to/ofts-daily-state` from a checkout of this research branch. It reads the existing JSON evidence only and prints counts, per-event veto states, and ledger reconciliation.

**Verdict: RESEARCH_ONLY_NO_GO.** The existing evidence does not meet executable profitability, matched-stock superiority, tolerable drawdown, or independent-sample requirements.
