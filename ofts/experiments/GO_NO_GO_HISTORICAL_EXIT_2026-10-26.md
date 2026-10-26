# OFTS GO/NO-GO: Historical exit sensitivity — 2026-10-26

**Research only. NOT production approved. No brokerage orders.**

## Provenance and controls

Source: `ofts/validation/cycle_execution_trades.csv` and `ofts/validation/cycle_execution_summary.txt` on this research branch; these files were produced by the v2.3 research validation workflow, including [run 40251991735](https://github.com/jtgeorge1970-tech/30-day-rocket-screen/actions/runs/40251991735). The data represent **24 nonoverlapping historical cycle trades on six training-selected stocks** (AEHR, AXTI, HOOD, PLTR, ROCK, STX), not an untouched independent test population. Original entries are next-session open after confirmed BUY; original exits are next-session open after later confirmed SELL. Fixed and trailing stop scenarios are the **already-saved hypothetical stop-return fields**, not newly executed trades. Original net return includes 0.20 percentage-point assumed round-trip cost. For like-for-like sensitivity, subtract the same 0.20 percentage points from the saved fixed/trailing stop returns. These assumptions do not prove fillability or cost realism.

| Same 24 historical trades | Original exit | Fixed 12% stop | Trailing 12% stop |
|---|---:|---:|---:|
| Average net return | +13.252% | +13.169% | +3.380% |
| Median net return | -0.825% | -12.200% | -5.761% |
| Positive net trades | 12/24 | 8/24 | 8/24 |
| Worst net trade | -66.227% | -14.547% | -12.200% |
| Average net excluding top 3 winners in each scenario | -1.045% | -1.139% | -3.647% |
| Trades with net loss below -20% | 4 | 0 | 0 |

Paired mean change vs original exits: fixed stop **-0.082 percentage points** (improved 8/24 trades); trailing stop **-9.872 percentage points** (improved 11/24 trades). This is descriptive, not a significance test. Historical stops may gap through trigger levels, so do not assume a hard loss cap. The stop scenarios are based on existing simulation columns; their execution logic has **not** been independently re-audited.

## Outlier dependence and stock concentration

Three largest original net winners: STX +137.112%, STX +108.870%, AXTI +94.001%. Removing these three turns the mean original cycle return **negative (-1.045%)**. The original median is negative (-0.825%) and 12 of 24 trades lost money.

Original leave-one-symbol-out means (percent): omit AEHR +19.711, AXTI +11.381, HOOD +14.381, PLTR +17.568, ROCK +14.532, STX +2.733. The positive mean is concentrated in a few unusually large winners. These are not independent estimates of generalization.

### Six-symbol cluster sensitivity (new)

To avoid treating repeated trades from the same symbol as independent, enumerate all **46,656** possible six-draw bootstrap samples with replacement from the six historical symbol clusters (including all trades from each sampled symbol). For the original exit rule, the resulting distribution of sample mean returns has 2.5th percentile **-3.500%**, median **+12.227%**, and 97.5th percentile **+37.544%**; **8.779%** of these cluster-resampled means are nonpositive. The range includes zero despite the +13.252% raw trade-weighted mean. This is only a *sensitivity diagnostic*: six training-selected symbols are far too few to claim a population confidence interval or infer future profitability.

## GO/NO-GO interpretation

This historical comparison is **new robustness analysis of existing evidence**, not a new unseen chronological holdout. The 12% fixed stop dramatically reduced the simulated worst loss but **did not improve mean returns** and reduced the fraction of winners. The 12% trailing stop reduced severe losses but also removed much of the upside. Neither rule is approved. No parameter tuning or production rule changes were performed.

Required before GO: fresh qualified cohorts, materially more independent completed trades, verified realistic next-open fills and spread/slippage, a chronological untouched test of stop/cooldown/entry challengers against unchanged baseline, same-stock passive/alternative-entry controls, matched-date SPY and IWM, portfolio drawdown/tail risk, and explicit corporate-action integrity checks.

**Current verdict: RESEARCH_ONLY_NO_GO.**

Reproduce with `python ofts/experiments/historical_exit_sensitivity_20261026.py` from this branch.
