# OFTS daily research

Market session: 2026-10-19
Selected: 126; refreshed: 123; refresh errors: 3
Qualified prediction cohorts saved: 7; current coverage: 123/126
Outcome counts: {'CORPORATE_ACTION_REVIEW': 1, 'INELIGIBLE_DATA': 315, 'MATURE': 233, 'PENDING': 3906}
Cycle fingerprints saved: 88/133
Signal states: BUY=1, SELL=0, NO_TRADE=132
Cycle ledger: pending entries=1; open positions=10; closed trades=0; SPY pairs=0
Cycle-speed report card: AWAITING_CLOSED_FORWARD_TRADES; closed forward trades=0; groups=[]
Score scale: theoretical 0-100; observed 10.85272562264587-63.9462796150476; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 10, '40_TO_49_999': 33, '50_TO_59_999': 36, '60_TO_69_999': 9, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=88
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=63; REVIEW=25; INSUFFICIENT=43
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| SCYX | 63.946 | CANDIDATE | NO_TRADE | STABLE_RANGE | 18.248174589685128 | [17.88, 18.25, 22.32] | [12.56, 3.98, 51.26] | 1.4532190612379912 | 3 | STABLE_3_OF_3 | [16, 18, 7] | [6, 5, 10] | [12, 24, 7] | [13, 6, 5] | 2.333333333333333 | DISSIPATING | False | 22.323463527984643 | 14.823267044769459 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 27 | 28.4176344838303 | HIGH |
| SB | 63.892 | CANDIDATE | NO_TRADE | STABLE_RANGE | 5.480982037106042 | [9.94, 9.83, 4.38] | [16.57, 18.69, 10.75] | 0.593159145672681 | 2 | UNSTABLE | [9, 9, 5] | [11, 18, 8] | [12, 9, 8] | [12, 17, 11] | 0.7840909090909092 | DISSIPATING | False | 4.378696969358398 | 8.140418542886913 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 51 | 14.646983328731938 | MEDIUM |
| RERE | 63.344 | CANDIDATE | NO_TRADE | IRREGULAR | 7.125889539144248 | [3.15, 6.85, 3.07] | [3.68, 13.95, 11.11] | 0.2831467413002345 | 1 | UNSTABLE | [4, 10, 13] | [3, 5, 12] | [5, 14, 13] | [3, 8, 10] | 1.8125 | DISSIPATING | False | 3.06905681185341 | 8.598130689455795 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 13.0 | 12.351543378023134 | MEDIUM |
| AKAM | 62.306 | CANDIDATE | NO_TRADE | DOWNTREND | 13.361407576511365 | [5.39, 13.36, 6.0] | [14.84, 13.34, 5.28] | 0.4493567985845546 | 3 | STABLE_3_OF_3 | [8, 10, 12] | [10, 7, 10] | [7, 9, 16] | [9, 7, 11] | 1.0 | DISSIPATING | False | 5.996031051408424 | 12.005786686082951 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 32 | 18.113510469596545 | MEDIUM |
| Q | 62.149 | CANDIDATE | NO_TRADE | STABLE_RANGE | 13.664597372606302 | [5.93, 9.45, 16.62] | [3.12, 14.81, 6.91] | 1.3664938446855541 | 3 | STABLE_3_OF_3 | [5, 15, 17] | [11, 10, 7] | [9, 9, 23] | [7, 6, 9] | 1.3928571428571428 | STABLE_OR_MIXED | False | 16.61576852553408 | 9.85712158373966 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 24 | 15.558687260850146 | MEDIUM |
| MESO | 60.880 | CANDIDATE | NO_TRADE | DECAYING | 4.996328599039779 | [10.48, 2.55, 5.0] | [11.73, 9.25, 4.97] | 0.5398626974844074 | 1 | UNSTABLE | [11, 5, 8] | [7, 5, 6] | [10, 8, 6] | [10, 6, 6] | 1.3333333333333333 | DISSIPATING | False | 4.996328599039779 | 10.23786984277521 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 15 | 14.95519576098916 | MEDIUM |
| CHTR | 60.584 | CANDIDATE | NO_TRADE | INSUFFICIENT | 15.776562646077686 | [3.57, 8.74, 8.87] | [4.2, 5.81, 4.99] | 1.750303479370837 | 2 | WATCH_2_OF_3 | [3, 3, 6] | [2, 4, 4] | [3, 5, 23] | [3, 3, 5] | 1.2083333333333335 | STABLE_OR_MIXED | False | 8.872959098490352 | 10.074590696229741 | WATCH | NO_TRADE | RISING | INSUFFICIENT | 41.5 | 15.790322759136277 | HIGH |
| MH | 60.191 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.879997253417967 | [9.99, 6.92, 4.88] | [25.42, 7.83, 3.58] | 0.8837717803312876 | 2 | UNSTABLE | [7, 5, 5] | [11, 7, 9] | [6, 6, 5] | [12, 12, 5] | 0.5277777777777778 | STABLE_OR_MIXED | False | 4.879997253417967 | 9.673241986917564 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | RISING | 26.5 | 15.40984546306361 | MEDIUM |
| XPRO | 60.035 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.530544348093702 | [5.13, 6.34, 5.53] | [12.83, 19.33, 29.6] | 0.2861190423872202 | 3 | STABLE_3_OF_3 | [10, 22, 6] | [15, 11, 24] | [24, 5, 6] | [7, 17, 20] | 0.5098039215686274 | DISSIPATING | False | 5.530544348093702 | 9.989441695807335 | FADING | NO_TRADE | RISING | INSUFFICIENT | 20 | 14.95875149963658 | MEDIUM |
| FUBO | 59.853 | CANDIDATE | NO_TRADE | IRREGULAR | 8.468683359655271 | [10.83, 4.04, 8.47] | [24.1, 21.8, 14.75] | 0.38843602032248625 | 2 | WATCH_2_OF_3 | [6, 5, 13] | [6, 14, 7] | [8, 6, 12] | [4, 5, 15] | 1.2285714285714286 | DISSIPATING | False | 8.468683359655271 | 14.552183626050171 | WATCH | NO_TRADE | RISING | RISING | 22.5 | 25.679749835772103 | HIGH |
| NYAX | 59.715 | CANDIDATE | NO_TRADE | DOWNTREND | 11.995180160324592 | [5.29, 2.94, 16.75] | [7.24, 3.44, 16.98] | 0.7307811318654659 | 2 | WATCH_2_OF_3 | [5, 12, 10] | [4, 4, 5] | [12, 5, 14] | [4, 4, 4] | 2.75 | DISSIPATING | False | 16.748766621516097 | 8.920449275592457 | WATCH | NO_TRADE | FALLING | FALLING | 25.5 | 16.554543782118735 | MEDIUM |
| SPGI | 59.563 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.370988740285164 | [4.3, 7.88, 4.37] | [19.63, 6.24, 4.72] | 0.7000410382722665 | 1 | UNSTABLE | [13, 11, 4] | [12, 8, 7] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 4.370988740285164 | 6.852614011775887 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 34.5 | 11.399714480696755 | MEDIUM |
| ATGL | 58.437 | CANDIDATE | NO_TRADE | DOWNTREND | 7.9497928402005975 | [4.02, 6.46, 11.36] | [10.12, 7.23, 32.71] | 0.6382818393478004 | 2 | WATCH_2_OF_3 | [4, 9, 3] | [7, 13, 5] | [7, 9, 3] | [3, 16, 3] | 1.4523809523809526 | DISSIPATING | False | 11.363636117336174 | 19.782781577819243 | FADING | NO_TRADE | FALLING | FALLING | 20.5 | 32.103798759905985 | MEDIUM |
| CHPT | 58.136 | CANDIDATE | NO_TRADE | IRREGULAR | 16.70480636591809 | [4.68, 16.7, 8.72] | [12.21, 90.56, 17.01] | 0.5128420127040436 | 2 | WATCH_2_OF_3 | [2, 7, 10] | [7, 10, 9] | [4, 5, 12] | [14, 11, 8] | 0.6161616161616161 | DISSIPATING | False | 8.721803238921733 | 17.336886868662866 | WATCH | NO_TRADE | MIXED | RISING | 26.0 | 23.571429933820454 | MEDIUM |
| SFM | 58.038 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.764149138352236 | [4.0, 6.18, 4.76] | [20.85, 10.78, 3.35] | 0.44190981548954067 | 1 | UNSTABLE | [5, 12, 11] | [11, 17, 7] | [5, 11, 12] | [6, 20, 9] | 1.1111111111111112 | DISSIPATING | False | 4.764149138352236 | 8.562929263659466 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | MIXED | 23.5 | 14.357597616056061 | MEDIUM |
| SRAD | 58.010 | CANDIDATE | NO_TRADE | IRREGULAR | 9.602072806101592 | [8.12, 12.21, 9.6] | [4.69, 11.99, 3.89] | 2.046531067064293 | 3 | STABLE_3_OF_3 | [15, 5, 14] | [7, 12, 6] | [12, 7, 11] | [8, 13, 8] | 1.6875 | DISSIPATING | False | 9.602072806101592 | 11.057795950944065 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 26 | 16.53954916634129 | LOW |
| CCS | 57.700 | CANDIDATE | NO_TRADE | INSUFFICIENT | 7.236396002714862 | [4.17, 7.24, 3.08] | [11.68, 6.09, 3.48] | 0.6840910734443489 | 1 | UNSTABLE | [4, 27, 17] | [8, 6, 2] | [2, 22, 24] | [9, 8, 4] | 2.791666666666667 | DISSIPATING | False | 3.0803486105271283 | 9.431790859526767 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 34 | 16.172723350139588 | HIGH |
| LFCR | 57.677 | CANDIDATE | NO_TRADE | IRREGULAR | 8.695655679332305 | [3.91, 8.7, 56.9] | [3.65, 6.16, 7.97] | 1.4106287244879654 | 2 | WATCH_2_OF_3 | [7, 6, 5] | [2, 11, 5] | [5, 4, 8] | [8, 6, 10] | 0.9125 | STABLE_OR_MIXED | False | 56.904772663333205 | 11.113587531250976 | WATCH | NO_TRADE | FALLING | MIXED | 12 | 11.617739999739435 | LOW |
| ACDC | 57.617 | CANDIDATE | NO_TRADE | DECAYING | 15.521332757663542 | [9.82, 6.82, 15.52] | [24.31, 8.78, 13.85] | 0.7088552038191496 | 3 | STABLE_3_OF_3 | [8, 7, 12] | [7, 5, 4] | [2, 12, 9] | [7, 9, 4] | 1.442857142857143 | DISSIPATING | False | 15.521332757663542 | 13.053566294269592 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 22.5 | 23.767799004313883 | MEDIUM |
| VIRC | 57.231 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.461537874661969 | [2.95, 9.51, 4.46] | [5.46, 3.06, 10.32] | 0.817019921083376 | 1 | UNSTABLE | [2, 9, 9] | [8, 9, 7] | [4, 9, 14] | [7, 6, 6] | 1.3125 | DISSIPATING | False | 4.461537874661969 | 7.014878853125926 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 20.0 | 11.659188733927506 | MEDIUM |
| EPM | 56.875 | CANDIDATE | NO_TRADE | IRREGULAR | 5.7377058257448095 | [12.28, 6.34, 2.81] | [10.19, 9.43, 6.29] | 0.6720088429954724 | 2 | UNSTABLE | [14, 6, 2] | [10, 19, 2] | [14, 3, 5] | [18, 10, 5] | 0.55 | DISSIPATING | False | 2.8089928274849907 | 8.661247242968178 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 26 | 12.982888675563604 | LOW |
| CRNC | 56.838 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.468299119393417 | [4.55, 3.82, 6.47] | [18.11, 6.64, 12.68] | 0.3584280762422222 | 1 | UNSTABLE | [4, 4, 3] | [9, 8, 15] | [4, 2, 7] | [9, 9, 12] | 0.4444444444444444 | DISSIPATING | False | 6.468299119393417 | 11.571756148414037 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | MIXED | 14 | 19.601070079276095 | MEDIUM |
| DKNG | 56.630 | CANDIDATE | NO_TRADE | INSUFFICIENT | 6.885425907149978 | [6.02, 3.62, 6.89] | [20.13, 8.86, 4.29] | 0.67891670684082 | 2 | WATCH_2_OF_3 | [10, 9, 9] | [13, 5, 5] | [15, 7, 8] | [9, 7, 3] | 1.4714285714285715 | DISSIPATING | False | 6.885425907149978 | 10.376661340400165 | WATCH | NO_TRADE | FALLING | INSUFFICIENT | 44.5 | 21.84106683486984 | MEDIUM |
| SGRY | 56.491 | CANDIDATE | NO_TRADE | DOWNTREND | 9.93873437611683 | [3.01, 19.25, 3.45] | [6.9, 6.76, 6.65] | 0.5101038434633243 | 1 | UNSTABLE | [7, 7, 4] | [5, 9, 7] | [8, 4, 5] | [9, 7, 6] | 0.8571428571428572 | DISSIPATING | False | 3.4507026598581403 | 8.460999700010124 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 39.5 | 18.51484965277759 | MEDIUM |
| WULF | 56.393 | CANDIDATE | NO_TRADE | DOWNTREND | 9.358751536188347 | [20.43, 4.66, 9.36] | [6.52, 21.91, 3.72] | 1.4343904620347199 | 2 | WATCH_2_OF_3 | [6, 9, 9] | [5, 7, 3] | [3, 11, 10] | [3, 6, 6] | 1.7333333333333334 | DISSIPATING | False | 9.358751536188347 | 13.476728432085284 | WATCH | NO_TRADE | FALLING | FALLING | 17.0 | 23.59208026482824 | LOW |

## Experimental recent-swing review shortlist (NOT BUY signals)
Count: 0 of 68 scored CANDIDATE names
| Symbol | Quality score | Last 3 swings % | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Historical avg % |
|---|---:|---:|---|---|---:|---:|---|---|---|---|---:|---:|

## Mature outcomes by score and horizon
```json
[
  {
    "model_hash": "2efb29d640e0ca751d9f8d30781f9021b2e38310114999e253e7b21b7283c3c6",
    "horizon": 5,
    "score_band": "0-40",
    "observations": 9,
    "positive_net_pct": 22.22222222222222,
    "average_net_pct": -2.4042649451013145,
    "average_positive_pct": 3.535550998543635,
    "average_nonpositive_pct": -4.101355214714158,
    "benchmark_pairs": 9,
    "average_excess_pct": -0.21011657038036496,
    "worst_adverse_excursion_pct": -13.595710342333245
  },
  {
    "model_hash": "2efb29d640e0ca751d9f8d30781f9021b2e38310114999e253e7b21b7283c3c6",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 77,
    "positive_net_pct": 38.96103896103896,
    "average_net_pct": -3.572760627165922,
    "average_positive_pct": 4.412636113262518,
    "average_nonpositive_pct": -8.669822376375567,
    "benchmark_pairs": 77,
    "average_excess_pct": -1.3786122524449742,
    "worst_adverse_excursion_pct": -40.99756998687247
  },
  {
    "model_hash": "2efb29d640e0ca751d9f8d30781f9021b2e38310114999e253e7b21b7283c3c6",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 11,
    "positive_net_pct": 18.181818181818183,
    "average_net_pct": -6.120536161300652,
    "average_positive_pct": 5.132624031052579,
    "average_nonpositive_pct": -8.621238426268038,
    "benchmark_pairs": 11,
    "average_excess_pct": -3.9263877865797028,
    "worst_adverse_excursion_pct": -24.34210416242579
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "0-40",
    "observations": 11,
    "positive_net_pct": 9.090909090909092,
    "average_net_pct": -2.695605351908024,
    "average_positive_pct": 1.6669421639563755,
    "average_nonpositive_pct": -3.1318601034944638,
    "benchmark_pairs": 11,
    "average_excess_pct": -1.0985273665313637,
    "worst_adverse_excursion_pct": -11.560105423793154
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 70,
    "positive_net_pct": 32.857142857142854,
    "average_net_pct": -3.886807210623226,
    "average_positive_pct": 2.8616595324521166,
    "average_nonpositive_pct": -7.189248382766479,
    "benchmark_pairs": 70,
    "average_excess_pct": -2.289729225246567,
    "worst_adverse_excursion_pct": -41.84652498923972
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 11,
    "positive_net_pct": 27.272727272727273,
    "average_net_pct": -6.327300851535608,
    "average_positive_pct": 3.9279201253455596,
    "average_nonpositive_pct": -10.173008717866047,
    "benchmark_pairs": 11,
    "average_excess_pct": -4.7302228661589485,
    "worst_adverse_excursion_pct": -25.57142802647182
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
- SB.PRC: ValueError: EMPTY_PROVIDER_RESPONSE
- SLP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
