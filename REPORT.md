# OFTS daily research

Market session: 2026-11-03
Selected: 138; refreshed: 124; refresh errors: 14
Qualified prediction cohorts saved: 18; current coverage: 124/138
Outcome counts: {'CORPORATE_ACTION_REVIEW': 10, 'INELIGIBLE_DATA': 1205, 'MATURE': 2461, 'PENDING': 8059}
Cycle fingerprints saved: 126/166
Signal states: BUY=2, SELL=5, NO_TRADE=159
Cycle ledger: pending entries=2; open positions=34; closed trades=6; SPY pairs=6
Cycle-speed report card: READY; closed forward trades=6; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 11.629396185079681-67.78646095688094; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 9, '40_TO_49_999': 62, '50_TO_59_999': 50, '60_TO_69_999': 5, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=126
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=96; REVIEW=30; INSUFFICIENT=76
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| AKAM | 67.786 | CANDIDATE | NO_TRADE | IRREGULAR | 14.143262278384672 | [13.36, 6.0, 14.14] | [13.34, 5.28, 5.39] | 2.4808292663919276 | 3 | STABLE_3_OF_3 | [10, 12, 12] | [7, 10, 8] | [9, 16, 7] | [7, 11, 7] | 1.3928571428571428 | STABLE_OR_MIXED | False | 14.143262278384672 | 12.531616810430005 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 28 | 16.858607095784766 | HIGH |
| SCYX | 66.032 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.92349603967859 | [18.25, 22.32, 7.92] | [3.98, 51.26, 17.88] | 1.0206244779698799 | 3 | STABLE_3_OF_3 | [18, 7, 19] | [5, 10, 16] | [7, 16, 9] | [5, 12, 24] | 1.275 | STABLE_OR_MIXED | False | 7.92349603967859 | 14.487170151011188 | FADING | NO_TRADE | MIXED | MIXED | 25 | 27.6617157809988 | MEDIUM |
| EEFT | 64.482 | CANDIDATE | NO_TRADE | IRREGULAR | 12.004174664675238 | [3.77, 8.32, 7.26] | [8.25, 7.81, 5.34] | 0.9299372980162708 | 2 | WATCH_2_OF_3 | [8, 8, 33] | [9, 4, 7] | [9, 25, 14] | [6, 7, 6] | 1.7380952380952381 | DISSIPATING | False | 7.261671573238626 | 7.827879339922485 | WATCH | NO_TRADE | FALLING | FALLING | 29.0 | 12.877679514179475 | HIGH |
| ASO | 63.347 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.082550099856398 | [29.86, 2.51, 29.11] | [2.66, 5.36, 3.23] | 9.007066123750718 | 2 | WATCH_2_OF_3 | [16, 7, 22] | [5, 4, 7] | [15, 9, 19] | [4, 7, 8] | 2.6714285714285717 | DISSIPATING | False | 29.111809298613878 | 8.02929205969693 | TOO_SMALL | NO_TRADE | INSUFFICIENT | MIXED | 31.0 | 15.450212978444922 | HIGH |
| SPGI | 60.654 | CANDIDATE | NO_TRADE | INSUFFICIENT | 4.370988740285164 | [4.3, 7.88, 4.37] | [19.63, 6.24, 4.72] | 0.7000410382722665 | 1 | UNSTABLE | [13, 11, 4] | [12, 8, 7] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 4.370988740285164 | 6.861549721499744 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | MIXED | 35 | 11.723543952355413 | MEDIUM |
| XPRO | 59.687 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.883370976826919 | [5.53, 6.88, 12.45] | [29.6, 5.13, 6.34] | 1.085507634555178 | 3 | STABLE_3_OF_3 | [6, 6, 5] | [24, 10, 22] | [5, 6, 5] | [17, 20, 24] | 0.26136363636363635 | STABLE_OR_MIXED | False | 12.452112272923799 | 9.550997280259715 | CYCLE_TIMING | NO_TRADE | MIXED | RISING | 21.0 | 14.691943189164292 | MEDIUM |
| TT | 59.402 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.634527680280586 | [13.36, 3.07, 3.63] | [3.24, 9.92, 2.73] | 1.120909955921715 | 1 | UNSTABLE | [33, 6, 4] | [18, 11, 11] | [18, 21, 6] | [15, 8, 15] | 0.8727272727272727 | STABLE_OR_MIXED | False | 3.634527680280586 | 6.837258883170663 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | INSUFFICIENT | 42.5 | 12.549158572299103 | HIGH |
| EPM | 58.843 | CANDIDATE | NO_TRADE | IRREGULAR | 5.7377058257448095 | [6.34, 2.81, 15.65] | [9.43, 6.29, 12.28] | 0.6720088429954724 | 2 | WATCH_2_OF_3 | [6, 2, 25] | [19, 2, 14] | [14, 3, 5] | [18, 10, 5] | 0.4642857142857143 | DISSIPATING | False | 15.652172590999713 | 8.906958041485016 | WATCH | NO_TRADE | RISING | MIXED | 26.5 | 13.172043165811598 | MEDIUM |
| TARS | 58.257 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.890997729114678 | [28.49, 5.82, 5.89] | [15.86, 6.67, 30.56] | 0.37132785936427515 | 3 | STABLE_3_OF_3 | [12, 17, 16] | [8, 8, 23] | [19, 17, 5] | [8, 4, 27] | 2.0625 | DISSIPATING | False | 5.890997729114678 | 11.255370631203952 | FADING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 32.0 | 22.88800424885913 | HIGH |
| PRCT | 58.088 | CANDIDATE | NO_TRADE | STABLE_RANGE | 10.526313224660921 | [5.93, 14.98, 15.93] | [4.58, 10.49, 4.73] | 3.1652199537400043 | 3 | STABLE_3_OF_3 | [11, 9, 13] | [2, 10, 5] | [4, 9, 12] | [5, 9, 11] | 1.6 | DISSIPATING | False | 15.933746269042025 | 11.001848306089123 | CYCLE_TIMING | NO_TRADE | FALLING | MIXED | 24.5 | 15.76067129433103 | MEDIUM |
| METCB | 57.955 | CANDIDATE | NO_TRADE | INSUFFICIENT | 17.82608587484953 | [6.15, 6.24, 18.52] | [15.95, 7.19, 4.68] | 0.8675568786153617 | 3 | STABLE_3_OF_3 | [6, 6, 13] | [6, 4, 11] | [6, 3, 13] | [2, 8, 11] | 0.875 | STABLE_OR_MIXED | False | 18.518519920156272 | 11.578336026537247 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 54.5 | 41.968602167990475 | HIGH |
| ATGL | 57.953 | CANDIDATE | SELL | STABLE_RANGE | 11.363636117336174 | [6.46, 11.36, 145.59] | [7.23, 32.71, 4.02] | 1.5708548121969454 | 3 | STABLE_3_OF_3 | [9, 3, 9] | [13, 5, 4] | [9, 3, 2] | [16, 3, 7] | 1.1142857142857143 | STABLE_OR_MIXED | False | 145.5947073175599 | 22.66995575536634 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 23.0 | 32.103798759905985 | MEDIUM |
| CRNC | 57.634 | CANDIDATE | NO_TRADE | IRREGULAR | 6.804368129894389 | [3.82, 6.47, 19.56] | [6.64, 12.68, 4.55] | 0.9737109920041425 | 2 | WATCH_2_OF_3 | [4, 3, 17] | [8, 15, 4] | [4, 2, 7] | [9, 9, 12] | 0.4722222222222222 | STABLE_OR_MIXED | False | 19.556714277436903 | 11.91872729819917 | WATCH | NO_TRADE | FALLING | FALLING | 17.0 | 19.819817420347153 | MEDIUM |
| LOMA | 57.056 | CANDIDATE | NO_TRADE | DOWNTREND | 6.719370680489034 | [12.91, 12.07, 3.6] | [4.22, 8.36, 3.95] | 2.8636212011930535 | 2 | UNSTABLE | [24, 26, 10] | [3, 5, 6] | [17, 31, 15] | [2, 4, 5] | 4.525 | DISSIPATING | True | 3.6016966917501225 | 7.759677020726251 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 25.0 | 14.025245216681359 | MEDIUM |
| VST | 56.778 | CANDIDATE | NO_TRADE | STABLE_RANGE | 8.216284433975519 | [3.98, 4.3, 4.64] | [5.37, 11.84, 20.86] | 0.3633880069835668 | 0 | UNSTABLE | [4, 6, 4] | [9, 16, 21] | [7, 4, 6] | [13, 22, 10] | 0.3557692307692308 | DISSIPATING | False | 4.63755695645518 | 8.232134828695818 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 23.0 | 20.238881878143445 | MEDIUM |
| ROOT | 56.672 | CANDIDATE | NO_TRADE | IRREGULAR | 3.722315311817248 | [4.32, 17.06, 3.67] | [4.3, 2.52, 3.13] | 1.378217385117116 | 1 | UNSTABLE | [5, 28, 5] | [4, 2, 5] | [14, 19, 5] | [4, 4, 4] | 2.375 | DISSIPATING | False | 3.6658260545212373 | 9.030673609061202 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 14 | 15.030799707594273 | LOW |
| MESO | 56.367 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.364017811603918 | [5.0, 7.36, 27.61] | [9.25, 4.97, 10.48] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [13, 8, 6] | [5, 6, 11] | [14, 9, 4] | [6, 6, 10] | 1.4166666666666665 | DISSIPATING | False | 27.60586658826034 | 11.528670663677737 | WATCH | NO_TRADE | FALLING | MIXED | 17 | 20.101265180857112 | MEDIUM |
| CCK | 55.866 | CANDIDATE | NO_TRADE | INSUFFICIENT | 12.471972602345737 | [3.64, 3.6, 13.14] | [23.09, 8.0, 5.86] | 0.45502779164561385 | 1 | UNSTABLE | [6, 14, 41] | [26, 12, 5] | [11, 31, 20] | [20, 11, 6] | 1.4924242424242424 | DISSIPATING | False | 13.139168952613932 | 6.278077902902429 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 76.5 | 15.407802338822385 | HIGH |
| SAIL | 55.672 | CANDIDATE | NO_TRADE | STABLE_UPTREND | 9.725567709405658 | [28.31, 6.08, 19.41] | [6.73, 15.05, 5.9] | 2.885806328775393 | 3 | STABLE_3_OF_3 | [14, 11, 12] | [3, 12, 3] | [6, 18, 7] | [14, 9, 6] | 2.388888888888889 | DISSIPATING | False | 19.413330078125 | 15.122633491840139 | CYCLE_TIMING | NO_TRADE | RISING | RISING | 23.5 | 20.30904098999389 | MEDIUM |
| GDEV | 55.629 | CANDIDATE | NO_TRADE | STABLE_RANGE | 5.015679323064615 | [4.05, 5.02, 4.67] | [10.19, 8.97, 6.21] | 0.5201389534329883 | 1 | UNSTABLE | [4, 7, 4] | [4, 13, 5] | [5, 6, 4] | [5, 11, 8] | 0.7125 | DISSIPATING | False | 4.666667514377165 | 10.675567042731183 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | MIXED | 18.0 | 19.954987716703343 | LOW |
| DLTH | 55.589 | CANDIDATE | NO_TRADE | STABLE_RANGE | 5.12820011216677 | [28.45, 3.38, 5.13] | [7.44, 5.48, 4.24] | 0.9364538133404328 | 2 | WATCH_2_OF_3 | [27, 5, 11] | [12, 3, 10] | [9, 10, 7] | [6, 7, 25] | 1.192857142857143 | STABLE_OR_MIXED | False | 5.12820011216677 | 10.029780675872301 | TOO_SMALL | NO_TRADE | MIXED | MIXED | 17.5 | 15.96009551012061 | MEDIUM |
| BRCB | 55.268 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.652171899931369 | [5.62, 5.65, 53.4] | [7.98, 19.1, 21.31] | 0.2958826969370916 | 3 | STABLE_3_OF_3 | [9, 10, 30] | [6, 5, 8] | [7, 13, 13] | [11, 6, 5] | 1.9166666666666665 | DISSIPATING | False | 53.39594875847315 | 13.60956373423241 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 27.5 | 27.974946238849828 | HIGH |
| IDYA | 55.202 | CANDIDATE | NO_TRADE | IRREGULAR | 8.970094018772068 | [4.72, 9.95, 3.28] | [5.06, 20.0, 6.03] | 0.7813435060923797 | 1 | UNSTABLE | [6, 16, 4] | [14, 21, 19] | [11, 15, 6] | [28, 8, 27] | 0.3615984405458089 | STABLE_OR_MIXED | False | 3.2846653931672964 | 8.892086671087913 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | FALLING | 37 | 16.851088405566358 | MEDIUM |
| GLW | 55.197 | CANDIDATE | NO_TRADE | IRREGULAR | 11.465139720745743 | [11.23, 11.47, 6.07] | [9.25, 4.98, 16.88] | 1.2134154140163043 | 3 | STABLE_3_OF_3 | [9, 10, 16] | [3, 8, 8] | [8, 9, 19] | [3, 7, 7] | 1.2678571428571428 | STABLE_OR_MIXED | False | 6.071626128711194 | 13.454638413001303 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 21.0 | 17.21659014301915 | MEDIUM |
| EE | 55.153 | CANDIDATE | NO_TRADE | STABLE_RANGE | 11.286232646508864 | [4.3, 4.9, 10.65] | [3.52, 5.39, 13.71] | 0.9075272236691071 | 1 | UNSTABLE | [6, 9, 18] | [11, 6, 17] | [11, 12, 15] | [14, 7, 15] | 0.8376623376623377 | STABLE_OR_MIXED | False | 10.650881669067246 | 8.342085727372215 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | FALLING | 35 | 13.007619608228389 | MEDIUM |

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
    "observations": 146,
    "positive_net_pct": 44.52054794520548,
    "average_net_pct": -1.9402343407094353,
    "average_positive_pct": 3.099702146350241,
    "average_nonpositive_pct": -5.984627817979544,
    "benchmark_pairs": 146,
    "average_excess_pct": -1.2630759031562961,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 879,
    "positive_net_pct": 53.69738339021615,
    "average_net_pct": 0.888772956548527,
    "average_positive_pct": 6.708040290715833,
    "average_nonpositive_pct": -5.859861396588986,
    "benchmark_pairs": 879,
    "average_excess_pct": 1.6477395030074435,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 107,
    "positive_net_pct": 51.401869158878505,
    "average_net_pct": -0.4180298328816701,
    "average_positive_pct": 4.4431272091993055,
    "average_nonpositive_pct": -5.5596382427750095,
    "benchmark_pairs": 107,
    "average_excess_pct": 0.31772218616053755,
    "worst_adverse_excursion_pct": -25.57142802647182
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 88,
    "positive_net_pct": 52.27272727272727,
    "average_net_pct": -0.3927249661078249,
    "average_positive_pct": 5.486067663048247,
    "average_nonpositive_pct": -6.831402607564472,
    "benchmark_pairs": 88,
    "average_excess_pct": 0.8245487511820886,
    "worst_adverse_excursion_pct": -55.257270184399786
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 507,
    "positive_net_pct": 53.25443786982248,
    "average_net_pct": 2.34359252150083,
    "average_positive_pct": 11.900561547754823,
    "average_nonpositive_pct": -8.54409371094043,
    "benchmark_pairs": 507,
    "average_excess_pct": 3.5931219609893725,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 71,
    "positive_net_pct": 53.521126760563384,
    "average_net_pct": 1.7297464844254256,
    "average_positive_pct": 8.381347731037248,
    "average_nonpositive_pct": -5.929673132885157,
    "benchmark_pairs": 71,
    "average_excess_pct": 2.83890863276377,
    "worst_adverse_excursion_pct": -30.81636301420778
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
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
