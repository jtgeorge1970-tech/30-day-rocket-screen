# OFTS daily research

Market session: 2026-10-29
Selected: 136; refreshed: 118; refresh errors: 73
Qualified prediction cohorts saved: 15; current coverage: 118/136
Outcome counts: {'CORPORATE_ACTION_REVIEW': 8, 'INELIGIBLE_DATA': 925, 'MATURE': 1764, 'MISSING_SESSIONS': 3, 'PENDING': 6990}
Cycle fingerprints saved: 115/162
Signal states: BUY=1, SELL=3, NO_TRADE=158
Cycle ledger: pending entries=1; open positions=33; closed trades=2; SPY pairs=2
Cycle-speed report card: READY; closed forward trades=2; groups=['MEDIUM_11_TO_25']
Score scale: theoretical 0-100; observed 11.744188253821582-67.49615153894838; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 16, '40_TO_49_999': 51, '50_TO_59_999': 40, '60_TO_69_999': 8, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=115
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=92; REVIEW=23; INSUFFICIENT=70
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| SCYX | 67.496 | CANDIDATE | NO_TRADE | STABLE_RANGE | 22.323463527984643 | [17.88, 18.25, 22.32] | [12.56, 3.98, 51.26] | 1.4532190612379912 | 3 | STABLE_3_OF_3 | [16, 18, 7] | [6, 5, 10] | [24, 7, 16] | [6, 5, 12] | 2.6666666666666665 | DISSIPATING | False | 22.323463527984643 | 14.972337440654174 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 25 | 27.6617157809988 | MEDIUM |
| ASO | 64.407 | CANDIDATE | NO_TRADE | STABLE_RANGE | 5.082550099856398 | [29.86, 2.51, 29.11] | [2.66, 5.36, 3.23] | 9.007066123750718 | 2 | WATCH_2_OF_3 | [16, 7, 22] | [5, 4, 7] | [15, 9, 19] | [4, 7, 8] | 2.6714285714285717 | DISSIPATING | False | 29.111809298613878 | 7.988658286346364 | TOO_SMALL | NO_TRADE | MIXED | MIXED | 31.0 | 15.450212978444922 | HIGH |
| MESO | 62.900 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.364017811603918 | [10.48, 5.0, 7.36] | [11.73, 9.25, 4.97] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [11, 13, 8] | [7, 5, 6] | [14, 9, 4] | [6, 6, 10] | 1.6666666666666665 | DISSIPATING | False | 7.364017811603918 | 10.35738361243058 | FADING | NO_TRADE | MIXED | FALLING | 15.5 | 16.79708009501123 | MEDIUM |
| AKAM | 62.427 | CANDIDATE | NO_TRADE | DOWNTREND | 14.809186553508058 | [5.39, 13.36, 6.0] | [14.84, 13.34, 5.28] | 0.4493567985845546 | 3 | STABLE_3_OF_3 | [8, 10, 12] | [10, 7, 10] | [9, 16, 7] | [7, 11, 7] | 1.1428571428571428 | DISSIPATING | False | 5.996031051408424 | 12.299628681298188 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 28.0 | 17.07072257644503 | MEDIUM |
| CRNC | 62.004 | CANDIDATE | SELL | IRREGULAR | 6.804368129894389 | [3.82, 6.47, 19.56] | [6.64, 12.68, 4.55] | 0.9737109920041425 | 2 | WATCH_2_OF_3 | [4, 3, 17] | [8, 15, 4] | [4, 2, 7] | [9, 9, 12] | 0.4722222222222222 | STABLE_OR_MIXED | False | 19.556714277436903 | 11.935038454381385 | WATCH | NO_TRADE | FALLING | FALLING | 17.0 | 19.819817420347153 | MEDIUM |
| SPGI | 61.931 | CANDIDATE | NO_TRADE | INSUFFICIENT | 4.370988740285164 | [4.3, 7.88, 4.37] | [19.63, 6.24, 4.72] | 0.7000410382722665 | 1 | UNSTABLE | [13, 11, 4] | [12, 8, 7] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 4.370988740285164 | 6.963713623391614 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | MIXED | 35 | 11.723543952355413 | HIGH |
| TT | 60.786 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.634527680280586 | [13.36, 3.07, 3.63] | [3.24, 9.92, 2.73] | 1.120909955921715 | 1 | UNSTABLE | [33, 6, 4] | [18, 11, 11] | [18, 21, 6] | [15, 8, 15] | 0.8727272727272727 | STABLE_OR_MIXED | False | 3.634527680280586 | 6.79894890943597 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | INSUFFICIENT | 42.5 | 12.868832109870343 | HIGH |
| TARS | 60.106 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.890997729114678 | [28.49, 5.82, 5.89] | [15.86, 6.67, 30.56] | 0.37132785936427515 | 3 | STABLE_3_OF_3 | [12, 17, 16] | [8, 8, 23] | [19, 17, 5] | [8, 4, 27] | 2.0625 | DISSIPATING | False | 5.890997729114678 | 11.114296536379065 | FADING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 34.0 | 24.901612451689736 | HIGH |
| LFCR | 59.773 | CANDIDATE | NO_TRADE | IRREGULAR | 8.695655679332305 | [3.91, 8.7, 56.9] | [3.65, 6.16, 7.97] | 1.4106287244879654 | 2 | WATCH_2_OF_3 | [7, 6, 5] | [2, 11, 5] | [5, 4, 8] | [8, 6, 10] | 0.9125 | STABLE_OR_MIXED | False | 56.904772663333205 | 11.120142699198306 | WATCH | NO_TRADE | FALLING | MIXED | 12 | 11.617739999739435 | MEDIUM |
| NYAX | 59.678 | CANDIDATE | NO_TRADE | STABLE_RANGE | 16.748766621516097 | [2.94, 16.75, 18.54] | [3.44, 16.98, 5.29] | 3.1667565986879476 | 2 | WATCH_2_OF_3 | [12, 10, 16] | [4, 5, 5] | [12, 5, 14] | [4, 4, 4] | 2.7 | DISSIPATING | False | 18.53881066969101 | 9.033147867477107 | WATCH | NO_TRADE | FALLING | MIXED | 25.0 | 16.554543782118735 | MEDIUM |
| FUBO | 59.475 | CANDIDATE | NO_TRADE | IRREGULAR | 8.468683359655271 | [10.83, 4.04, 8.47] | [24.1, 21.8, 14.75] | 0.38843602032248625 | 2 | WATCH_2_OF_3 | [6, 5, 13] | [6, 14, 7] | [8, 6, 12] | [4, 5, 15] | 1.2285714285714286 | DISSIPATING | False | 8.468683359655271 | 14.883469278734859 | WATCH | NO_TRADE | RISING | RISING | 21 | 24.901278854720466 | HIGH |
| EEFT | 59.357 | CANDIDATE | NO_TRADE | DOWNTREND | 12.004174664675238 | [3.77, 8.32, 7.26] | [8.25, 7.81, 5.34] | 0.9299372980162708 | 2 | WATCH_2_OF_3 | [8, 8, 33] | [9, 4, 7] | [9, 25, 14] | [6, 7, 6] | 1.7380952380952381 | DISSIPATING | False | 7.261671573238626 | 7.917927762027626 | WATCH | NO_TRADE | FALLING | FALLING | 27.0 | 12.736936852846249 | MEDIUM |
| PLBL | 59.049 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.375234900937721 | [17.31, 10.84, 6.38] | [6.55, 7.41, 5.59] | 1.6532587220073007 | 3 | STABLE_3_OF_3 | [6, 6, 5] | [3, 4, 12] | [8, 7, 4] | [7, 4, 8] | 1.25 | STABLE_OR_MIXED | False | 6.375234900937721 | 13.05308214753947 | FADING | NO_TRADE | MIXED | FALLING | 15.0 | 18.62197432609234 | MEDIUM |
| XPRO | 59.008 | CANDIDATE | NO_TRADE | INSUFFICIENT | 6.618965891784978 | [6.34, 5.53, 6.88] | [19.33, 29.6, 5.13] | 0.32805539003287426 | 3 | STABLE_3_OF_3 | [22, 6, 6] | [11, 24, 10] | [5, 6, 5] | [17, 20, 24] | 0.3977272727272727 | DISSIPATING | False | 6.883370976826919 | 9.262520874636781 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | RISING | 21 | 14.95875149963658 | MEDIUM |
| ATGL | 58.886 | CANDIDATE | NO_TRADE | IRREGULAR | 7.9497928402005975 | [4.02, 6.46, 11.36] | [10.12, 7.23, 32.71] | 0.6382818393478004 | 2 | WATCH_2_OF_3 | [4, 9, 3] | [7, 13, 5] | [9, 3, 2] | [16, 3, 7] | 0.5 | DISSIPATING | False | 11.363636117336174 | 19.913481705977798 | FADING | NO_TRADE | FALLING | FALLING | 22 | 32.06849916938487 | MEDIUM |
| GLW | 58.550 | CANDIDATE | NO_TRADE | IRREGULAR | 11.465139720745743 | [16.88, 11.23, 11.47] | [6.14, 9.25, 4.98] | 1.8685319181458309 | 3 | STABLE_3_OF_3 | [8, 9, 10] | [3, 3, 8] | [8, 9, 19] | [3, 7, 7] | 2.142857142857143 | DISSIPATING | False | 11.465139720745743 | 13.446825975260357 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 21.0 | 17.21659014301915 | MEDIUM |
| BRCB | 58.448 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.652171899931369 | [21.31, 5.62, 5.65] | [7.42, 7.98, 19.1] | 0.707866566368476 | 3 | STABLE_3_OF_3 | [8, 9, 10] | [11, 6, 5] | [7, 13, 13] | [11, 6, 5] | 1.8333333333333333 | DISSIPATING | False | 5.652171899931369 | 12.812493106788954 | FADING | NO_TRADE | INSUFFICIENT | FALLING | 27.5 | 27.974946238849828 | HIGH |
| RYAN | 57.742 | CANDIDATE | NO_TRADE | IRREGULAR | 3.7567551071579386 | [5.39, 3.76, 20.21] | [3.16, 7.52, 5.69] | 0.9470633785572741 | 2 | WATCH_2_OF_3 | [8, 3, 15] | [5, 13, 16] | [8, 5, 7] | [8, 11, 17] | 0.6258741258741258 | STABLE_OR_MIXED | False | 20.210763837245494 | 7.587706531652655 | TOO_SMALL | NO_TRADE | MIXED | MIXED | 29 | 14.403424060313986 | MEDIUM |
| EPM | 57.533 | CANDIDATE | NO_TRADE | IRREGULAR | 5.7377058257448095 | [6.34, 2.81, 15.65] | [9.43, 6.29, 12.28] | 0.6720088429954724 | 2 | WATCH_2_OF_3 | [6, 2, 25] | [19, 2, 14] | [14, 3, 5] | [18, 10, 5] | 0.4642857142857143 | DISSIPATING | False | 15.652172590999713 | 8.906958041485016 | WATCH | NO_TRADE | MIXED | MIXED | 26 | 12.982888675563604 | LOW |
| SRAD | 57.285 | CANDIDATE | NO_TRADE | IRREGULAR | 4.385212586959231 | [12.21, 9.6, 4.39] | [3.89, 6.5, 4.8] | 1.999118045730454 | 2 | UNSTABLE | [5, 14, 3] | [6, 8, 7] | [7, 11, 5] | [8, 6, 6] | 0.9404761904761905 | STABLE_OR_MIXED | False | 4.385212586959231 | 10.431659738756977 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 27 | 15.038462844909056 | LOW |
| LOMA | 57.183 | CANDIDATE | NO_TRADE | DOWNTREND | 6.719370680489034 | [12.91, 12.07, 3.6] | [4.22, 8.36, 3.95] | 2.8636212011930535 | 2 | UNSTABLE | [24, 26, 10] | [3, 5, 6] | [17, 31, 15] | [2, 4, 5] | 4.525 | DISSIPATING | True | 3.6016966917501225 | 7.286310504322341 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 23.0 | 14.025245216681359 | MEDIUM |
| FERG | 56.970 | CANDIDATE | NO_TRADE | INSUFFICIENT | 6.08606780511507 | [16.61, 4.34, 6.09] | [4.85, 5.97, 3.36] | 1.2544730128010313 | 2 | WATCH_2_OF_3 | [10, 19, 15] | [7, 12, 9] | [24, 11, 14] | [13, 9, 6] | 1.6111111111111112 | DISSIPATING | True | 6.08606780511507 | 7.144947741452169 | WATCH | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 43 | 15.39008433659906 | MEDIUM |
| WOR | 56.862 | CANDIDATE | NO_TRADE | INSUFFICIENT | 8.469851028030305 | [10.26, 8.47, 10.08] | [6.43, 3.09, 10.82] | 1.5681252779753838 | 3 | STABLE_3_OF_3 | [8, 6, 18] | [5, 8, 15] | [17, 3, 9] | [7, 10, 6] | 1.1428571428571428 | STABLE_OR_MIXED | False | 10.077780091279243 | 7.347106273853511 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 37 | 12.475830150764388 | HIGH |
| METCB | 56.860 | CANDIDATE | NO_TRADE | INSUFFICIENT | 17.82608587484953 | [6.15, 6.24, 18.52] | [15.95, 7.19, 4.68] | 0.8675568786153617 | 3 | STABLE_3_OF_3 | [6, 6, 13] | [6, 4, 11] | [6, 3, 13] | [2, 8, 11] | 0.875 | STABLE_OR_MIXED | False | 18.518519920156272 | 11.775352333763957 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 54.5 | 41.968602167990475 | HIGH |
| VIRC | 56.857 | CANDIDATE | NO_TRADE | INSUFFICIENT | 4.461537874661969 | [9.51, 4.46, 3.19] | [3.06, 10.32, 2.95] | 1.4599118296170084 | 1 | UNSTABLE | [9, 9, 9] | [9, 7, 2] | [4, 9, 14] | [7, 6, 6] | 1.3928571428571428 | STABLE_OR_MIXED | False | 3.1897896311569474 | 6.896213103462215 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | INSUFFICIENT | 20.0 | 11.659188733927506 | MEDIUM |

## Experimental recent-swing review shortlist (NOT BUY signals)
Count: 0 of 96 scored CANDIDATE names
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
    "observations": 114,
    "positive_net_pct": 43.85964912280702,
    "average_net_pct": -2.185158211804318,
    "average_positive_pct": 3.236662887806862,
    "average_nonpositive_pct": -6.4209559458755505,
    "benchmark_pairs": 114,
    "average_excess_pct": -1.8201448887997824,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 657,
    "positive_net_pct": 55.70776255707762,
    "average_net_pct": 1.196728248662033,
    "average_positive_pct": 6.822370357686893,
    "average_nonpositive_pct": -5.878821620420775,
    "benchmark_pairs": 657,
    "average_excess_pct": 1.5813989827554042,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 86,
    "positive_net_pct": 52.325581395348834,
    "average_net_pct": -0.22288864812210363,
    "average_positive_pct": 4.614505884745269,
    "average_nonpositive_pct": -5.532224111025318,
    "benchmark_pairs": 86,
    "average_excess_pct": 0.24521605950598413,
    "worst_adverse_excursion_pct": -25.57142802647182
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 52,
    "positive_net_pct": 51.92307692307692,
    "average_net_pct": -0.15386691296697153,
    "average_positive_pct": 5.336292836559109,
    "average_nonpositive_pct": -6.083239442455139,
    "benchmark_pairs": 52,
    "average_excess_pct": 0.473952575044435,
    "worst_adverse_excursion_pct": -55.257270184399786
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 292,
    "positive_net_pct": 50.68493150684932,
    "average_net_pct": 2.2129338084838244,
    "average_positive_pct": 12.743590148635025,
    "average_nonpositive_pct": -8.61024076333825,
    "benchmark_pairs": 292,
    "average_excess_pct": 2.897758566351966,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 47,
    "positive_net_pct": 48.93617021276596,
    "average_net_pct": 1.7709673390082128,
    "average_positive_pct": 9.979412169144334,
    "average_nonpositive_pct": -6.095458956538903,
    "benchmark_pairs": 47,
    "average_excess_pct": 2.4346268896348473,
    "worst_adverse_excursion_pct": -30.81636301420778
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
- FUSB: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- AESP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- COPL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- RDIB: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- WSO.B: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- GJP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- DCO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- FPH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- ACA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- QRVO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- PERF: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- GAM.PRB: ValueError: EMPTY_PROVIDER_RESPONSE
- SPG.PRJ: ValueError: EMPTY_PROVIDER_RESPONSE
- GS.PRA: ValueError: EMPTY_PROVIDER_RESPONSE
- NVNI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SB.PRC: ValueError: EMPTY_PROVIDER_RESPONSE
- SLP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ADIL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- ALDF: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ATNM: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- AUNA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- AUST: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BGSF: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BHAV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BRKH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- CCAQ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- DRDB: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- EURK: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- GJS: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- GWH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- HCMA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- HDL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- HRTG: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- IACQ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- INAC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- IPVV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- JONE: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- KRSP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- LESL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- LTGR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- MPTI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- MSGS: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- NCO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- NGL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- NINE: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- NTIP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- OCLT: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- ODC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- PAAC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- PBHC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- PONO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- PRSU: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- QNCX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- QSEA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SAAQ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SAC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SAGU: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SENEB: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SIMA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SMHI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SMJF: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SSEA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SVCC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TAP.A: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- TCI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TRGS: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TULP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TVIV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- UCFI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- UI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- WLII: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- YCY: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
