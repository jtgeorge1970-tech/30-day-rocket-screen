# OFTS daily research

Market session: 2026-10-28
Selected: 132; refreshed: 121; refresh errors: 26
Qualified prediction cohorts saved: 14; current coverage: 121/132
Outcome counts: {'CORPORATE_ACTION_REVIEW': 7, 'INELIGIBLE_DATA': 815, 'MATURE': 1536, 'MISSING_SESSIONS': 2, 'PENDING': 6650}
Cycle fingerprints saved: 118/155
Signal states: BUY=3, SELL=3, NO_TRADE=149
Cycle ledger: pending entries=2; open positions=31; closed trades=2; SPY pairs=2
Cycle-speed report card: READY; closed forward trades=2; groups=['MEDIUM_11_TO_25']
Score scale: theoretical 0-100; observed 10.745352243166598-67.47318717243705; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 12, '40_TO_49_999': 52, '50_TO_59_999': 44, '60_TO_69_999': 10, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=117
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=84; REVIEW=34; INSUFFICIENT=61
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| SCYX | 67.473 | CANDIDATE | NO_TRADE | STABLE_RANGE | 22.323463527984643 | [17.88, 18.25, 22.32] | [12.56, 3.98, 51.26] | 1.4532190612379912 | 3 | STABLE_3_OF_3 | [16, 18, 7] | [6, 5, 10] | [24, 7, 16] | [6, 5, 12] | 2.6666666666666665 | DISSIPATING | False | 22.323463527984643 | 15.042317323410682 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 25 | 27.6617157809988 | MEDIUM |
| ASO | 64.477 | CANDIDATE | NO_TRADE | STABLE_RANGE | 3.3333364159169876 | [29.86, 2.51, 29.11] | [2.66, 5.36, 3.23] | 9.007066123750718 | 2 | WATCH_2_OF_3 | [16, 7, 22] | [5, 4, 7] | [8, 15, 9] | [5, 4, 7] | 2.5 | DISSIPATING | False | 29.111809298613878 | 8.087706665405447 | TOO_SMALL | NO_TRADE | MIXED | MIXED | 31.0 | 15.450212978444922 | HIGH |
| MESO | 64.299 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.364017811603918 | [10.48, 5.0, 7.36] | [11.73, 9.25, 4.97] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [11, 13, 8] | [7, 5, 6] | [14, 9, 4] | [6, 6, 10] | 1.6666666666666665 | DISSIPATING | False | 7.364017811603918 | 10.363820865374347 | FADING | NO_TRADE | MIXED | FALLING | 15.5 | 16.79708009501123 | MEDIUM |
| AKAM | 62.402 | CANDIDATE | NO_TRADE | DOWNTREND | 14.809186553508058 | [5.39, 13.36, 6.0] | [14.84, 13.34, 5.28] | 0.4493567985845546 | 3 | STABLE_3_OF_3 | [8, 10, 12] | [10, 7, 10] | [9, 16, 7] | [7, 11, 7] | 1.1428571428571428 | DISSIPATING | False | 5.996031051408424 | 12.31875251089575 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 28.0 | 17.07072257644503 | MEDIUM |
| SPGI | 61.989 | CANDIDATE | NO_TRADE | INSUFFICIENT | 4.370988740285164 | [4.3, 7.88, 4.37] | [19.63, 6.24, 4.72] | 0.7000410382722665 | 1 | UNSTABLE | [13, 11, 4] | [12, 8, 7] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 4.370988740285164 | 6.888446144998326 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | MIXED | 35 | 11.723543952355413 | HIGH |
| TT | 60.950 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.634527680280586 | [13.36, 3.07, 3.63] | [3.24, 9.92, 2.73] | 1.120909955921715 | 1 | UNSTABLE | [33, 6, 4] | [18, 11, 11] | [18, 21, 6] | [15, 8, 15] | 0.8727272727272727 | STABLE_OR_MIXED | False | 3.634527680280586 | 6.806400374238647 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | INSUFFICIENT | 42.5 | 12.868832109870343 | HIGH |
| WOR | 60.595 | CANDIDATE | NO_TRADE | INSUFFICIENT | 8.469851028030305 | [10.26, 8.47, 10.08] | [6.43, 3.09, 10.82] | 1.5681252779753838 | 3 | STABLE_3_OF_3 | [8, 6, 18] | [5, 8, 15] | [17, 3, 9] | [7, 10, 6] | 1.1428571428571428 | STABLE_OR_MIXED | False | 10.077780091279243 | 7.347106273853511 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 37 | 12.475830150764388 | HIGH |
| LOMA | 60.402 | CANDIDATE | NO_TRADE | DOWNTREND | 6.719370680489034 | [12.91, 12.07, 3.6] | [4.22, 8.36, 3.95] | 2.8636212011930535 | 2 | UNSTABLE | [24, 26, 10] | [3, 5, 6] | [17, 31, 15] | [2, 4, 5] | 4.525 | DISSIPATING | True | 3.6016966917501225 | 7.286310504322341 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 23.0 | 14.025245216681359 | MEDIUM |
| TARS | 60.198 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.890997729114678 | [28.49, 5.82, 5.89] | [15.86, 6.67, 30.56] | 0.37132785936427515 | 3 | STABLE_3_OF_3 | [12, 17, 16] | [8, 8, 23] | [19, 17, 5] | [8, 4, 27] | 2.0625 | DISSIPATING | False | 5.890997729114678 | 11.114296536379065 | FADING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 34.0 | 24.901612451689736 | HIGH |
| ATGL | 59.787 | CANDIDATE | NO_TRADE | IRREGULAR | 7.9497928402005975 | [4.02, 6.46, 11.36] | [10.12, 7.23, 32.71] | 0.6382818393478004 | 2 | WATCH_2_OF_3 | [4, 9, 3] | [7, 13, 5] | [9, 3, 2] | [16, 3, 7] | 0.5 | DISSIPATING | False | 11.363636117336174 | 20.018171749821228 | FADING | NO_TRADE | FALLING | FALLING | 21.5 | 32.03319957886376 | MEDIUM |
| NYAX | 59.689 | CANDIDATE | NO_TRADE | STABLE_RANGE | 16.748766621516097 | [2.94, 16.75, 18.54] | [3.44, 16.98, 5.29] | 3.1667565986879476 | 2 | WATCH_2_OF_3 | [12, 10, 16] | [4, 5, 5] | [12, 5, 14] | [4, 4, 4] | 2.7 | DISSIPATING | False | 18.53881066969101 | 9.033147867477107 | WATCH | NO_TRADE | FALLING | MIXED | 25.0 | 16.554543782118735 | MEDIUM |
| GLW | 59.333 | CANDIDATE | NO_TRADE | IRREGULAR | 11.465139720745743 | [16.88, 11.23, 11.47] | [6.14, 9.25, 4.98] | 1.8685319181458309 | 3 | STABLE_3_OF_3 | [8, 9, 10] | [3, 3, 8] | [8, 9, 19] | [3, 7, 7] | 2.142857142857143 | DISSIPATING | False | 11.465139720745743 | 13.29198488213546 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 20.5 | 17.6917131717661 | MEDIUM |
| XPRO | 59.004 | CANDIDATE | NO_TRADE | INSUFFICIENT | 6.618965891784978 | [6.34, 5.53, 6.88] | [19.33, 29.6, 5.13] | 0.32805539003287426 | 3 | STABLE_3_OF_3 | [22, 6, 6] | [11, 24, 10] | [5, 6, 5] | [17, 20, 24] | 0.3977272727272727 | DISSIPATING | False | 6.883370976826919 | 9.262520874636781 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | RISING | 21 | 14.95875149963658 | MEDIUM |
| EEFT | 58.842 | CANDIDATE | NO_TRADE | DOWNTREND | 12.004174664675238 | [3.77, 8.32, 7.26] | [8.25, 7.81, 5.34] | 0.9299372980162708 | 2 | WATCH_2_OF_3 | [8, 8, 33] | [9, 4, 7] | [9, 25, 14] | [6, 7, 6] | 1.7380952380952381 | DISSIPATING | False | 7.261671573238626 | 7.963418121075431 | WATCH | NO_TRADE | FALLING | FALLING | 27.0 | 12.736936852846249 | MEDIUM |
| LFCR | 58.721 | CANDIDATE | NO_TRADE | IRREGULAR | 8.695655679332305 | [3.91, 8.7, 56.9] | [3.65, 6.16, 7.97] | 1.4106287244879654 | 2 | WATCH_2_OF_3 | [7, 6, 5] | [2, 11, 5] | [5, 4, 8] | [8, 6, 10] | 0.9125 | STABLE_OR_MIXED | False | 56.904772663333205 | 10.984510449013637 | WATCH | NO_TRADE | FALLING | MIXED | 12 | 11.617739999739435 | LOW |
| FUBO | 58.515 | CANDIDATE | NO_TRADE | IRREGULAR | 8.468683359655271 | [10.83, 4.04, 8.47] | [24.1, 21.8, 14.75] | 0.38843602032248625 | 2 | WATCH_2_OF_3 | [6, 5, 13] | [6, 14, 7] | [8, 6, 12] | [4, 5, 15] | 1.2285714285714286 | DISSIPATING | False | 8.468683359655271 | 14.64863279446273 | WATCH | NO_TRADE | RISING | RISING | 23 | 25.859568709143034 | HIGH |
| OMC | 57.817 | CANDIDATE | NO_TRADE | IRREGULAR | 9.177257270769722 | [3.63, 3.54, 12.29] | [10.68, 12.27, 4.07] | 0.3401182137005038 | 1 | UNSTABLE | [8, 6, 29] | [8, 12, 7] | [12, 4, 15] | [11, 6, 11] | 1.0454545454545454 | DISSIPATING | False | 12.29119026123242 | 6.985866237718975 | TOO_SMALL_UPSIDE | NO_TRADE | RISING | MIXED | 30.5 | 9.39219121783279 | MEDIUM |
| DKNG | 57.811 | CANDIDATE | NO_TRADE | INSUFFICIENT | 6.885425907149978 | [3.62, 6.89, 12.28] | [8.86, 4.29, 6.02] | 1.1446411660045923 | 2 | WATCH_2_OF_3 | [9, 9, 12] | [5, 5, 10] | [15, 7, 8] | [9, 7, 3] | 1.4714285714285715 | STABLE_OR_MIXED | False | 12.275130908201737 | 10.373752035744312 | WATCH | NO_TRADE | INSUFFICIENT | FALLING | 47 | 25.0024339747031 | MEDIUM |
| CRNC | 57.763 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.804368129894389 | [3.82, 6.47, 19.56] | [6.64, 12.68, 4.55] | 0.9737109920041425 | 2 | WATCH_2_OF_3 | [4, 3, 17] | [8, 15, 4] | [4, 2, 7] | [9, 9, 12] | 0.4722222222222222 | STABLE_OR_MIXED | False | 19.556714277436903 | 11.965370435068952 | WATCH | NO_TRADE | FALLING | MIXED | 16 | 19.229020363714117 | MEDIUM |
| CCS | 57.616 | CANDIDATE | NO_TRADE | DOWNTREND | 3.672368935275061 | [7.24, 3.08, 9.03] | [6.09, 3.48, 4.17] | 1.7369855022054526 | 2 | WATCH_2_OF_3 | [27, 17, 5] | [6, 2, 4] | [22, 24, 3] | [8, 4, 2] | 4.875 | DISSIPATING | False | 9.026353919938401 | 9.257880018335513 | TOO_SMALL | NO_TRADE | FALLING | FALLING | 30.5 | 13.42962727806235 | MEDIUM |
| EPM | 57.583 | CANDIDATE | NO_TRADE | IRREGULAR | 5.7377058257448095 | [6.34, 2.81, 15.65] | [9.43, 6.29, 12.28] | 0.6720088429954724 | 2 | WATCH_2_OF_3 | [6, 2, 25] | [19, 2, 14] | [14, 3, 5] | [18, 10, 5] | 0.4642857142857143 | DISSIPATING | False | 15.652172590999713 | 8.906958041485016 | WATCH | NO_TRADE | MIXED | MIXED | 26 | 12.982888675563604 | LOW |
| SRAD | 57.319 | CANDIDATE | NO_TRADE | IRREGULAR | 4.385212586959231 | [12.21, 9.6, 4.39] | [3.89, 6.5, 4.8] | 1.999118045730454 | 2 | UNSTABLE | [5, 14, 3] | [6, 8, 7] | [7, 11, 5] | [8, 6, 6] | 0.9404761904761905 | STABLE_OR_MIXED | False | 4.385212586959231 | 10.465342365509766 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 27 | 15.038462844909056 | LOW |
| FERG | 57.133 | CANDIDATE | NO_TRADE | INSUFFICIENT | 6.08606780511507 | [16.61, 4.34, 6.09] | [4.85, 5.97, 3.36] | 1.2544730128010313 | 2 | WATCH_2_OF_3 | [10, 19, 15] | [7, 12, 9] | [24, 11, 14] | [13, 9, 6] | 1.6111111111111112 | DISSIPATING | True | 6.08606780511507 | 7.144947741452169 | WATCH | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 43 | 15.39008433659906 | MEDIUM |
| METCB | 56.797 | CANDIDATE | NO_TRADE | INSUFFICIENT | 6.23556548923494 | [4.68, 6.15, 6.24] | [7.92, 15.95, 7.19] | 0.7756966492326193 | 2 | WATCH_2_OF_3 | [11, 6, 6] | [2, 6, 4] | [6, 3, 13] | [2, 8, 11] | 1.125 | STABLE_OR_MIXED | False | 6.23556548923494 | 11.67318312790953 | WATCH | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 54.5 | 41.968602167990475 | HIGH |
| FISV | 56.472 | CANDIDATE | NO_TRADE | DOWNTREND | 13.997675386580132 | [2.57, 6.02, 14.56] | [3.41, 7.64, 3.76] | 1.6033249049045082 | 2 | WATCH_2_OF_3 | [4, 4, 29] | [4, 7, 12] | [8, 5, 17] | [6, 8, 6] | 0.9523809523809523 | STABLE_OR_MIXED | False | 14.562666807008995 | 8.795352557297182 | WATCH | NO_TRADE | FALLING | FALLING | 21.5 | 12.342339593010976 | MEDIUM |

## Experimental recent-swing review shortlist (NOT BUY signals)
Count: 0 of 101 scored CANDIDATE names
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
    "model_hash": "2efb29d640e0ca751d9f8d30781f9021b2e38310114999e253e7b21b7283c3c6",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 9,
    "positive_net_pct": 44.44444444444444,
    "average_net_pct": -3.0424148117701404,
    "average_positive_pct": 1.3552946041324676,
    "average_nonpositive_pct": -6.560582344492227,
    "benchmark_pairs": 9,
    "average_excess_pct": -0.42709111494489593,
    "worst_adverse_excursion_pct": -15.498938708303832
  },
  {
    "model_hash": "2efb29d640e0ca751d9f8d30781f9021b2e38310114999e253e7b21b7283c3c6",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 77,
    "positive_net_pct": 41.55844155844156,
    "average_net_pct": -2.5891565191497574,
    "average_positive_pct": 10.442966882624233,
    "average_nonpositive_pct": -11.856444271522372,
    "benchmark_pairs": 77,
    "average_excess_pct": 0.026167177675487083,
    "worst_adverse_excursion_pct": -41.60583899263223
  },
  {
    "model_hash": "2efb29d640e0ca751d9f8d30781f9021b2e38310114999e253e7b21b7283c3c6",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 11,
    "positive_net_pct": 45.45454545454545,
    "average_net_pct": -5.263696113069489,
    "average_positive_pct": 4.8766883501241765,
    "average_nonpositive_pct": -13.71401649906421,
    "benchmark_pairs": 11,
    "average_excess_pct": -2.6483724162442455,
    "worst_adverse_excursion_pct": -24.34210416242579
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "0-40",
    "observations": 103,
    "positive_net_pct": 41.74757281553398,
    "average_net_pct": -2.2963883924202557,
    "average_positive_pct": 3.469574031279319,
    "average_nonpositive_pct": -6.428661462738281,
    "benchmark_pairs": 103,
    "average_excess_pct": -1.7899248612307261,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 578,
    "positive_net_pct": 54.49826989619377,
    "average_net_pct": 1.0804121125704709,
    "average_positive_pct": 6.940343973081702,
    "average_nonpositive_pct": -5.938137454201531,
    "benchmark_pairs": 578,
    "average_excess_pct": 1.660473382436789,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 79,
    "positive_net_pct": 50.63291139240506,
    "average_net_pct": -0.6656511002635334,
    "average_positive_pct": 4.277236359342019,
    "average_nonpositive_pct": -5.7352792639615355,
    "benchmark_pairs": 79,
    "average_excess_pct": -0.06348308625793508,
    "worst_adverse_excursion_pct": -25.57142802647182
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 41,
    "positive_net_pct": 51.21951219512195,
    "average_net_pct": 0.7602017585800842,
    "average_positive_pct": 5.020722235516258,
    "average_nonpositive_pct": -3.7133447422028985,
    "benchmark_pairs": 41,
    "average_excess_pct": 1.36817675079909,
    "worst_adverse_excursion_pct": -39.606737923462546
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 221,
    "positive_net_pct": 47.51131221719457,
    "average_net_pct": 1.0839919215553138,
    "average_positive_pct": 11.528992322991078,
    "average_nonpositive_pct": -8.370534303882238,
    "benchmark_pairs": 221,
    "average_excess_pct": 1.7633678059172584,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 36,
    "positive_net_pct": 44.44444444444444,
    "average_net_pct": 1.3324531061941407,
    "average_positive_pct": 11.036217283109716,
    "average_nonpositive_pct": -6.430558235338319,
    "benchmark_pairs": 36,
    "average_excess_pct": 1.9844631113007505,
    "worst_adverse_excursion_pct": -30.81636301420778
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
- ACA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- QRVO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- PERF: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- CET: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- GAM.PRB: ValueError: EMPTY_PROVIDER_RESPONSE
- SPG.PRJ: ValueError: EMPTY_PROVIDER_RESPONSE
- GS.PRA: ValueError: EMPTY_PROVIDER_RESPONSE
- NVNI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SB.PRC: ValueError: EMPTY_PROVIDER_RESPONSE
- SLP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ACGC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BHAV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BREZ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BRKH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BRTM: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- CAQ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- CLBR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- LEO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- LTGR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- MHNC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- NMI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- PAAC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- QSEA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TDWD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- UCFI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
