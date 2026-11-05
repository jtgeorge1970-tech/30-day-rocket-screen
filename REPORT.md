# OFTS daily research

Market session: 2026-11-04
Selected: 139; refreshed: 123; refresh errors: 20
Qualified prediction cohorts saved: 19; current coverage: 123/139
Outcome counts: {'CORPORATE_ACTION_REVIEW': 11, 'INELIGIBLE_DATA': 1310, 'MATURE': 2690, 'MISSING_SESSIONS': 1, 'PENDING': 8418}
Cycle fingerprints saved: 123/170
Signal states: BUY=5, SELL=5, NO_TRADE=160
Cycle ledger: pending entries=5; open positions=32; closed trades=10; SPY pairs=10
Cycle-speed report card: READY; closed forward trades=10; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 10.40137643498515-67.73065868382596; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 18, '40_TO_49_999': 57, '50_TO_59_999': 42, '60_TO_69_999': 6, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=122
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=95; REVIEW=28; INSUFFICIENT=76
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| AKAM | 67.731 | CANDIDATE | NO_TRADE | IRREGULAR | 14.143262278384672 | [13.36, 6.0, 14.14] | [13.34, 5.28, 5.39] | 2.4808292663919276 | 3 | STABLE_3_OF_3 | [10, 12, 12] | [7, 10, 8] | [9, 16, 7] | [7, 11, 7] | 1.3928571428571428 | STABLE_OR_MIXED | False | 14.143262278384672 | 12.531616810430005 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 28 | 16.858607095784766 | HIGH |
| EEFT | 64.855 | CANDIDATE | NO_TRADE | IRREGULAR | 12.004174664675238 | [3.77, 8.32, 7.26] | [8.25, 7.81, 5.34] | 0.9299372980162708 | 2 | WATCH_2_OF_3 | [8, 8, 33] | [9, 4, 7] | [9, 25, 14] | [6, 7, 6] | 1.7380952380952381 | DISSIPATING | False | 7.261671573238626 | 7.801420935426914 | WATCH | NO_TRADE | FALLING | FALLING | 29.0 | 12.877679514179475 | HIGH |
| SCYX | 64.089 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.92349603967859 | [18.25, 22.32, 7.92] | [3.98, 51.26, 17.88] | 1.0206244779698799 | 3 | STABLE_3_OF_3 | [18, 7, 19] | [5, 10, 16] | [7, 16, 9] | [5, 12, 24] | 1.275 | STABLE_OR_MIXED | False | 7.92349603967859 | 14.463806516030642 | FADING | NO_TRADE | MIXED | MIXED | 25 | 27.6617157809988 | MEDIUM |
| TBI | 63.432 | CANDIDATE | NO_TRADE | STABLE_RANGE | 11.026203555747681 | [3.04, 2.92, 21.1] | [9.15, 8.46, 11.19] | 0.33244085473662105 | 1 | UNSTABLE | [7, 5, 17] | [3, 17, 6] | [8, 3, 10] | [3, 18, 5] | 1.3833333333333333 | DISSIPATING | False | 21.104298742764648 | 14.123538621876273 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 23 | 17.688890954168752 | MEDIUM |
| ASO | 62.784 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.082550099856398 | [29.86, 2.51, 29.11] | [2.66, 5.36, 3.23] | 9.007066123750718 | 2 | WATCH_2_OF_3 | [16, 7, 22] | [5, 4, 7] | [15, 9, 19] | [4, 7, 8] | 2.6714285714285717 | DISSIPATING | False | 29.111809298613878 | 8.02929205969693 | TOO_SMALL | NO_TRADE | INSUFFICIENT | MIXED | 31.0 | 15.450212978444922 | HIGH |
| SPGI | 60.419 | CANDIDATE | NO_TRADE | INSUFFICIENT | 4.370988740285164 | [4.3, 7.88, 4.37] | [19.63, 6.24, 4.72] | 0.7000410382722665 | 1 | UNSTABLE | [13, 11, 4] | [12, 8, 7] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 4.370988740285164 | 6.861549721499744 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | MIXED | 35 | 11.723543952355413 | MEDIUM |
| XPRO | 59.632 | CANDIDATE | NO_TRADE | STABLE_RANGE | 12.452112272923799 | [5.53, 6.88, 12.45] | [29.6, 5.13, 6.34] | 1.085507634555178 | 3 | STABLE_3_OF_3 | [6, 6, 5] | [24, 10, 22] | [6, 5, 8] | [20, 24, 5] | 0.2863636363636364 | STABLE_OR_MIXED | False | 12.452112272923799 | 9.819690617219887 | CYCLE_TIMING | NO_TRADE | MIXED | RISING | 21.0 | 14.691943189164292 | MEDIUM |
| TT | 59.304 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.634527680280586 | [13.36, 3.07, 3.63] | [3.24, 9.92, 2.73] | 1.120909955921715 | 1 | UNSTABLE | [33, 6, 4] | [18, 11, 11] | [18, 21, 6] | [15, 8, 15] | 0.8727272727272727 | STABLE_OR_MIXED | False | 3.634527680280586 | 6.779315218997924 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | INSUFFICIENT | 42.5 | 12.549158572299103 | HIGH |
| NYAX | 58.898 | CANDIDATE | NO_TRADE | STABLE_RANGE | 11.995180160324592 | [2.94, 16.75, 18.54] | [3.44, 16.98, 5.29] | 3.1667565986879476 | 2 | WATCH_2_OF_3 | [12, 10, 16] | [4, 5, 5] | [5, 14, 13] | [4, 4, 12] | 2.825 | DISSIPATING | False | 18.53881066969101 | 9.092623170230818 | WATCH | NO_TRADE | MIXED | MIXED | 22 | 16.312324542859397 | MEDIUM |
| EPM | 58.707 | CANDIDATE | NO_TRADE | IRREGULAR | 5.7377058257448095 | [6.34, 2.81, 15.65] | [9.43, 6.29, 12.28] | 0.6720088429954724 | 2 | WATCH_2_OF_3 | [6, 2, 25] | [19, 2, 14] | [14, 3, 5] | [18, 10, 5] | 0.4642857142857143 | DISSIPATING | False | 15.652172590999713 | 8.906958041485016 | WATCH | NO_TRADE | RISING | MIXED | 26.5 | 13.172043165811598 | MEDIUM |
| TARS | 58.408 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.890997729114678 | [5.82, 5.89, 9.75] | [6.67, 30.56, 28.49] | 0.20675561616394783 | 3 | STABLE_3_OF_3 | [17, 16, 6] | [8, 23, 12] | [19, 17, 5] | [8, 4, 27] | 1.7291666666666665 | DISSIPATING | False | 9.75073581150696 | 11.21577497805403 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 32.0 | 22.88800424885913 | HIGH |
| METCB | 58.155 | CANDIDATE | NO_TRADE | INSUFFICIENT | 17.82608587484953 | [6.15, 6.24, 18.52] | [15.95, 7.19, 4.68] | 0.8675568786153617 | 3 | STABLE_3_OF_3 | [6, 6, 13] | [6, 4, 11] | [6, 3, 13] | [2, 8, 11] | 0.875 | STABLE_OR_MIXED | False | 18.518519920156272 | 11.578336026537247 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 54.5 | 41.968602167990475 | HIGH |
| ATGL | 57.958 | CANDIDATE | NO_TRADE | STABLE_RANGE | 18.834076229970485 | [6.46, 11.36, 145.59] | [7.23, 32.71, 4.02] | 1.5708548121969454 | 3 | STABLE_3_OF_3 | [9, 3, 9] | [13, 5, 4] | [3, 2, 11] | [3, 7, 9] | 1.1142857142857143 | STABLE_OR_MIXED | False | 145.5947073175599 | 22.577569118666595 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 23.0 | 32.103798759905985 | MEDIUM |
| CRNC | 57.599 | CANDIDATE | NO_TRADE | IRREGULAR | 12.322792857572228 | [3.82, 6.47, 19.56] | [6.64, 12.68, 4.55] | 0.9737109920041425 | 2 | WATCH_2_OF_3 | [4, 3, 17] | [8, 15, 4] | [2, 7, 24] | [9, 12, 4] | 0.6388888888888888 | STABLE_OR_MIXED | False | 19.556714277436903 | 11.752293215610052 | WATCH | NO_TRADE | FALLING | FALLING | 17.0 | 19.819817420347153 | MEDIUM |
| LOMA | 57.089 | CANDIDATE | NO_TRADE | DOWNTREND | 6.719370680489034 | [12.91, 12.07, 3.6] | [4.22, 8.36, 3.95] | 2.8636212011930535 | 2 | UNSTABLE | [24, 26, 10] | [3, 5, 6] | [17, 31, 15] | [2, 4, 5] | 4.525 | DISSIPATING | True | 3.6016966917501225 | 7.418555926773681 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 25.0 | 14.025245216681359 | MEDIUM |
| ROOT | 56.741 | CANDIDATE | NO_TRADE | IRREGULAR | 3.722315311817248 | [4.32, 17.06, 3.67] | [4.3, 2.52, 3.13] | 1.378217385117116 | 1 | UNSTABLE | [5, 28, 5] | [4, 2, 5] | [14, 19, 5] | [4, 4, 4] | 2.375 | DISSIPATING | False | 3.6658260545212373 | 9.030673609061202 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 14 | 15.030799707594273 | LOW |
| VST | 56.604 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.63755695645518 | [4.3, 4.64, 3.7] | [11.84, 20.86, 3.98] | 0.3633880069835668 | 0 | UNSTABLE | [6, 4, 5] | [16, 21, 4] | [7, 4, 6] | [13, 22, 10] | 0.3870192307692308 | DISSIPATING | False | 3.6995733637609884 | 8.221623461363562 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 23.0 | 20.238881878143445 | MEDIUM |
| MESO | 56.398 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.364017811603918 | [5.0, 7.36, 27.61] | [9.25, 4.97, 10.48] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [13, 8, 6] | [5, 6, 11] | [14, 9, 4] | [6, 6, 10] | 1.4166666666666665 | DISSIPATING | False | 27.60586658826034 | 11.470499344617043 | WATCH | NO_TRADE | FALLING | MIXED | 17 | 20.101265180857112 | MEDIUM |
| CRD.B | 56.174 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.3927024582229626 | [3.49, 3.3, 3.39] | [4.47, 16.03, 4.89] | 0.6931643226306808 | 0 | UNSTABLE | [9, 12, 8] | [7, 6, 3] | [13, 9, 2] | [6, 3, 7] | 1.5 | DISSIPATING | False | 3.3927024582229626 | 6.541064184951839 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 35 | 14.391010603698984 | HIGH |
| CCK | 55.660 | CANDIDATE | NO_TRADE | INSUFFICIENT | 12.471972602345737 | [3.64, 3.6, 13.14] | [23.09, 8.0, 5.86] | 0.45502779164561385 | 1 | UNSTABLE | [6, 14, 41] | [26, 12, 5] | [11, 31, 20] | [20, 11, 6] | 1.4924242424242424 | DISSIPATING | False | 13.139168952613932 | 6.278077902902429 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 76.5 | 15.407802338822385 | HIGH |
| SAIL | 55.407 | CANDIDATE | NO_TRADE | STABLE_UPTREND | 15.18534931315002 | [28.31, 6.08, 19.41] | [6.73, 15.05, 5.9] | 2.885806328775393 | 3 | STABLE_3_OF_3 | [14, 11, 12] | [3, 12, 3] | [18, 7, 12] | [9, 6, 6] | 3.0 | DISSIPATING | False | 19.413330078125 | 15.00451922292254 | CYCLE_TIMING | NO_TRADE | RISING | RISING | 23.5 | 20.30904098999389 | MEDIUM |
| OABI | 55.287 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.010985279670747 | [10.11, 9.01, 14.53] | [15.07, 24.56, 8.24] | 0.6712646425592168 | 3 | STABLE_3_OF_3 | [6, 7, 6] | [5, 13, 7] | [7, 6, 8] | [23, 7, 11] | 0.7467532467532467 | DISSIPATING | False | 14.533623793697693 | 15.47706841703262 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 56.5 | 27.22772066879009 | HIGH |
| SLDE | 55.188 | CANDIDATE | NO_TRADE | IRREGULAR | 5.265391979999645 | [28.42, 2.57, 30.35] | [6.59, 12.33, 6.81] | 4.172994265752101 | 2 | WATCH_2_OF_3 | [27, 7, 22] | [5, 7, 6] | [7, 30, 5] | [5, 6, 6] | 2.4166666666666665 | DISSIPATING | False | 30.345139488230387 | 9.429460139525492 | TOO_SMALL | NO_TRADE | RISING | RISING | 27.0 | 16.265977094254247 | MEDIUM |
| IDYA | 55.167 | CANDIDATE | NO_TRADE | IRREGULAR | 7.744402920108151 | [4.72, 9.95, 3.28] | [5.06, 20.0, 6.03] | 0.7813435060923797 | 1 | UNSTABLE | [6, 16, 4] | [14, 21, 19] | [15, 6, 6] | [8, 27, 11] | 0.43062200956937796 | STABLE_OR_MIXED | False | 3.2846653931672964 | 8.938556315596403 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | FALLING | 37 | 16.851088405566358 | MEDIUM |
| GLW | 55.156 | CANDIDATE | NO_TRADE | IRREGULAR | 11.465139720745743 | [11.23, 11.47, 6.07] | [9.25, 4.98, 16.88] | 1.2134154140163043 | 3 | STABLE_3_OF_3 | [9, 10, 16] | [3, 8, 8] | [8, 9, 19] | [3, 7, 7] | 1.2678571428571428 | STABLE_OR_MIXED | False | 6.071626128711194 | 13.454638413001303 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 21.0 | 17.21659014301915 | MEDIUM |

## Experimental recent-swing review shortlist (NOT BUY signals)
Count: 0 of 105 scored CANDIDATE names
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
    "observations": 156,
    "positive_net_pct": 44.87179487179487,
    "average_net_pct": -1.6622670956164463,
    "average_positive_pct": 3.425515226628621,
    "average_nonpositive_pct": -5.803485264885688,
    "benchmark_pairs": 156,
    "average_excess_pct": -0.9991864398549851,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 954,
    "positive_net_pct": 53.56394129979036,
    "average_net_pct": 0.8651817902029062,
    "average_positive_pct": 6.778611175536691,
    "average_nonpositive_pct": -5.955952331480083,
    "benchmark_pairs": 954,
    "average_excess_pct": 1.600451677475034,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 117,
    "positive_net_pct": 50.427350427350426,
    "average_net_pct": -0.402318739258715,
    "average_positive_pct": 4.65489997735877,
    "average_nonpositive_pct": -5.546730882024777,
    "benchmark_pairs": 117,
    "average_excess_pct": 0.3096549056433869,
    "worst_adverse_excursion_pct": -25.57142802647182
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 104,
    "positive_net_pct": 50.0,
    "average_net_pct": -1.345651418882307,
    "average_positive_pct": 5.804187150620743,
    "average_nonpositive_pct": -8.495489988385355,
    "benchmark_pairs": 104,
    "average_excess_pct": -0.29371424883969455,
    "worst_adverse_excursion_pct": -95.51242232978043
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 577,
    "positive_net_pct": 54.939341421143844,
    "average_net_pct": 2.750647496859813,
    "average_positive_pct": 12.008018578224773,
    "average_nonpositive_pct": -8.536224167727465,
    "benchmark_pairs": 577,
    "average_excess_pct": 3.865885723954204,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 79,
    "positive_net_pct": 55.69620253164557,
    "average_net_pct": 1.9238688297000286,
    "average_positive_pct": 8.178869234667369,
    "average_nonpositive_pct": -5.939560250830342,
    "benchmark_pairs": 79,
    "average_excess_pct": 2.935149865313726,
    "worst_adverse_excursion_pct": -30.81636301420778
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
- MS.PRF: ValueError: EMPTY_PROVIDER_RESPONSE
- PSKY: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ALL.PRI: ValueError: EMPTY_PROVIDER_RESPONSE
- USB.PRH: ValueError: EMPTY_PROVIDER_RESPONSE
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
- LNAI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- KVUE: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- FNWD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- LEO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- PEBK: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- WHG: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
