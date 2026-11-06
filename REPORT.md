# OFTS daily research

Market session: 2026-11-05
Selected: 140; refreshed: 121; refresh errors: 21
Qualified prediction cohorts saved: 20; current coverage: 121/140
Outcome counts: {'CORPORATE_ACTION_REVIEW': 14, 'INELIGIBLE_DATA': 1435, 'MATURE': 2916, 'MISSING_SESSIONS': 1, 'PENDING': 8764}
Cycle fingerprints saved: 131/173
Signal states: BUY=0, SELL=17, NO_TRADE=156
Cycle ledger: pending entries=0; open positions=33; closed trades=14; SPY pairs=14
Cycle-speed report card: READY; closed forward trades=14; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 10.10326084401892-68.04345761267534; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 14, '40_TO_49_999': 54, '50_TO_59_999': 53, '60_TO_69_999': 10, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=131
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=110; REVIEW=21; INSUFFICIENT=90
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| MWH | 68.043 | CANDIDATE | NO_TRADE | INSUFFICIENT | 13.517312490359545 | [11.38, 13.52, 15.21] | [18.33, 5.95, 9.76] | 1.385666278611575 | 3 | STABLE_3_OF_3 | [11, 17, 3] | [8, 17, 9] | [12, 19, 5] | [6, 19, 5] | 1.6111111111111112 | DISSIPATING | False | 15.212715679159539 | 11.438164033255923 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 47.5 | 35.23344052246027 | HIGH |
| AKAM | 67.541 | CANDIDATE | NO_TRADE | IRREGULAR | 14.143262278384672 | [13.36, 6.0, 14.14] | [13.34, 5.28, 5.39] | 2.4808292663919276 | 3 | STABLE_3_OF_3 | [10, 12, 12] | [7, 10, 8] | [9, 16, 7] | [7, 11, 7] | 1.3928571428571428 | STABLE_OR_MIXED | False | 14.143262278384672 | 12.491096330455223 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 28 | 16.858607095784766 | HIGH |
| ASO | 62.800 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.082550099856398 | [29.86, 2.51, 29.11] | [2.66, 5.36, 3.23] | 9.007066123750718 | 2 | WATCH_2_OF_3 | [16, 7, 22] | [5, 4, 7] | [15, 9, 19] | [4, 7, 8] | 2.6714285714285717 | DISSIPATING | False | 29.111809298613878 | 8.130347772559263 | TOO_SMALL | NO_TRADE | INSUFFICIENT | MIXED | 31.0 | 15.450212978444922 | HIGH |
| TBI | 62.540 | CANDIDATE | NO_TRADE | STABLE_RANGE | 11.026203555747681 | [3.04, 2.92, 21.1] | [9.15, 8.46, 11.19] | 0.33244085473662105 | 1 | UNSTABLE | [7, 5, 17] | [3, 17, 6] | [3, 10, 11] | [18, 5, 8] | 1.2083333333333335 | DISSIPATING | False | 21.104298742764648 | 13.743229600719665 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 23 | 17.688890954168752 | MEDIUM |
| SCYX | 62.471 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.556963660361335 | [22.32, 7.92, 4.51] | [51.26, 17.88, 18.25] | 0.4342075970797313 | 2 | UNSTABLE | [7, 19, 4] | [10, 16, 18] | [7, 16, 9] | [5, 12, 24] | 0.59375 | DISSIPATING | False | 4.509285866154467 | 14.264716103033118 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 25 | 27.6617157809988 | MEDIUM |
| SPGI | 61.660 | CANDIDATE | NO_TRADE | INSUFFICIENT | 4.370988740285164 | [4.3, 7.88, 4.37] | [19.63, 6.24, 4.72] | 0.7000410382722665 | 1 | UNSTABLE | [13, 11, 4] | [12, 8, 7] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 4.370988740285164 | 6.861549721499744 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | FALLING | 35 | 11.723543952355413 | MEDIUM |
| TARS | 60.375 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.890997729114678 | [5.82, 5.89, 9.75] | [6.67, 30.56, 28.49] | 0.20675561616394783 | 3 | STABLE_3_OF_3 | [17, 16, 6] | [8, 23, 12] | [19, 17, 5] | [8, 4, 27] | 1.7291666666666665 | DISSIPATING | False | 9.75073581150696 | 11.390005764188949 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 34.0 | 24.901612451689736 | HIGH |
| NYAX | 60.012 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.5308166126839 | [16.75, 18.54, 3.19] | [16.98, 5.29, 2.94] | 3.1667565986879476 | 2 | UNSTABLE | [10, 16, 6] | [5, 5, 12] | [5, 14, 13] | [4, 4, 12] | 2.625 | DISSIPATING | False | 3.186841590260814 | 8.994193477231317 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 22 | 16.312324542859397 | MEDIUM |
| XPRO | 59.597 | CANDIDATE | NO_TRADE | STABLE_RANGE | 12.452112272923799 | [6.88, 12.45, 3.9] | [5.13, 6.34, 5.53] | 1.2446100317773452 | 2 | UNSTABLE | [6, 5, 5] | [10, 22, 6] | [6, 5, 8] | [20, 24, 5] | 0.4 | STABLE_OR_MIXED | False | 3.8980472124543253 | 9.705812859435934 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | RISING | 21.0 | 14.691943189164292 | MEDIUM |
| EPM | 59.576 | CANDIDATE | NO_TRADE | IRREGULAR | 5.7377058257448095 | [6.34, 2.81, 15.65] | [9.43, 6.29, 12.28] | 0.6720088429954724 | 2 | WATCH_2_OF_3 | [6, 2, 25] | [19, 2, 14] | [14, 3, 5] | [18, 10, 5] | 0.4642857142857143 | DISSIPATING | False | 15.652172590999713 | 8.906958041485016 | WATCH | NO_TRADE | RISING | MIXED | 26.5 | 13.172043165811598 | MEDIUM |
| GEV | 59.349 | CANDIDATE | SELL | DOWNTREND | 7.032536099086029 | [4.0, 9.83, 7.03] | [8.1, 3.61, 17.66] | 0.8682258343971804 | 2 | WATCH_2_OF_3 | [11, 4, 5] | [15, 3, 17] | [26, 3, 5] | [23, 7, 2] | 0.5238095238095238 | STABLE_OR_MIXED | False | 7.032536099086029 | 10.171265053070048 | WATCH | NO_TRADE | FALLING | FALLING | 34.0 | 20.982622115166482 | MEDIUM |
| MESO | 59.264 | CANDIDATE | SELL | STABLE_RANGE | 7.364017811603918 | [5.0, 7.36, 27.61] | [9.25, 4.97, 10.48] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [13, 8, 6] | [5, 6, 11] | [14, 9, 4] | [6, 6, 10] | 1.4166666666666665 | DISSIPATING | False | 27.60586658826034 | 11.46470076812834 | WATCH | NO_TRADE | FALLING | MIXED | 17.0 | 20.139586356352645 | LOW |
| METCB | 58.967 | CANDIDATE | SELL | INSUFFICIENT | 17.82608587484953 | [6.15, 6.24, 18.52] | [15.95, 7.19, 4.68] | 0.8675568786153617 | 3 | STABLE_3_OF_3 | [6, 6, 13] | [6, 4, 11] | [6, 3, 13] | [2, 8, 11] | 0.875 | STABLE_OR_MIXED | False | 18.518519920156272 | 11.439208895140018 | CYCLE_TIMING | NO_TRADE | FALLING | INSUFFICIENT | 53 | 41.58882283911626 | HIGH |
| ASIC | 58.568 | CANDIDATE | NO_TRADE | INSUFFICIENT | 7.564650726993549 | [4.7, 5.73, 7.56] | [6.42, 13.74, 8.03] | 0.7139734239697425 | 2 | WATCH_2_OF_3 | [12, 5, 9] | [7, 21, 6] | [5, 4, 11] | [12, 15, 16] | 0.8095238095238095 | STABLE_OR_MIXED | False | 7.564650726993549 | 7.912201908834161 | WATCH | NO_TRADE | MIXED | INSUFFICIENT | 26 | 12.1034236732233 | MEDIUM |
| EME | 58.528 | CANDIDATE | NO_TRADE | STABLE_RANGE | 13.062557728380074 | [4.32, 13.06, 9.23] | [28.26, 4.75, 5.3] | 1.7419553683835496 | 2 | WATCH_2_OF_3 | [3, 17, 20] | [17, 8, 7] | [5, 5, 26] | [7, 19, 6] | 1.4196428571428572 | STABLE_OR_MIXED | False | 9.228611001086495 | 9.866019808479864 | WATCH | NO_TRADE | FALLING | MIXED | 39.0 | 17.698546150662253 | MEDIUM |
| CRD.B | 58.367 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.3927024582229626 | [3.49, 3.3, 3.39] | [4.47, 16.03, 4.89] | 0.6931643226306808 | 0 | UNSTABLE | [9, 12, 8] | [7, 6, 3] | [13, 9, 2] | [6, 3, 7] | 1.5 | DISSIPATING | False | 3.3927024582229626 | 6.535756989160789 | TOO_SMALL_UPSIDE | NO_TRADE | RISING | INSUFFICIENT | 35 | 14.391010603698984 | HIGH |
| TT | 57.981 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.634527680280586 | [13.36, 3.07, 3.63] | [3.24, 9.92, 2.73] | 1.120909955921715 | 1 | UNSTABLE | [33, 6, 4] | [18, 11, 11] | [18, 21, 6] | [15, 8, 15] | 0.8727272727272727 | STABLE_OR_MIXED | False | 3.634527680280586 | 6.779315218997924 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | INSUFFICIENT | 42.5 | 12.549158572299103 | HIGH |
| CRNC | 57.837 | CANDIDATE | NO_TRADE | IRREGULAR | 12.322792857572228 | [6.47, 19.56, 9.02] | [12.68, 4.55, 3.82] | 1.9838325962779013 | 3 | STABLE_3_OF_3 | [3, 17, 14] | [15, 4, 4] | [2, 7, 24] | [9, 12, 4] | 2.138888888888889 | DISSIPATING | False | 9.017417722756193 | 11.710855708142569 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 17 | 20.135473477171224 | MEDIUM |
| ATGL | 57.817 | CANDIDATE | NO_TRADE | STABLE_RANGE | 18.834076229970485 | [11.36, 145.59, 6.08] | [32.71, 4.02, 6.46] | 1.75940159940304 | 3 | STABLE_3_OF_3 | [3, 9, 4] | [5, 4, 9] | [3, 2, 11] | [3, 7, 9] | 0.6142857142857143 | STABLE_OR_MIXED | False | 6.0773500457816265 | 22.25333550449673 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 23.0 | 32.103798759905985 | MEDIUM |
| LOMA | 57.059 | CANDIDATE | NO_TRADE | DOWNTREND | 6.719370680489034 | [12.91, 12.07, 3.6] | [4.22, 8.36, 3.95] | 2.8636212011930535 | 2 | UNSTABLE | [24, 26, 10] | [3, 5, 6] | [17, 31, 15] | [2, 4, 5] | 4.525 | DISSIPATING | True | 3.6016966917501225 | 7.791908422594611 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 25.0 | 14.025245216681359 | MEDIUM |
| GLW | 56.004 | CANDIDATE | NO_TRADE | IRREGULAR | 11.465139720745743 | [11.23, 11.47, 6.07] | [9.25, 4.98, 16.88] | 1.2134154140163043 | 3 | STABLE_3_OF_3 | [9, 10, 16] | [3, 8, 8] | [8, 9, 19] | [3, 7, 7] | 1.2678571428571428 | STABLE_OR_MIXED | False | 6.071626128711194 | 13.448849733552443 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 20.5 | 17.6917131717661 | MEDIUM |
| CCK | 55.803 | CANDIDATE | NO_TRADE | INSUFFICIENT | 12.471972602345737 | [3.64, 3.6, 13.14] | [23.09, 8.0, 5.86] | 0.45502779164561385 | 1 | UNSTABLE | [6, 14, 41] | [26, 12, 5] | [11, 31, 20] | [20, 11, 6] | 1.4924242424242424 | DISSIPATING | False | 13.139168952613932 | 6.278077902902429 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 76.5 | 15.407802338822385 | HIGH |
| DUOT | 55.786 | CANDIDATE | SELL | STABLE_RANGE | 10.427352879635944 | [4.41, 16.48, 10.43] | [3.67, 5.11, 17.9] | 2.0404408123277755 | 2 | WATCH_2_OF_3 | [8, 11, 6] | [7, 7, 12] | [14, 12, 5] | [11, 4, 6] | 1.5714285714285714 | DISSIPATING | False | 10.427352879635944 | 13.404310740003705 | WATCH | NO_TRADE | FALLING | MIXED | 25 | 29.75700752799146 | MEDIUM |
| NU | 55.760 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.987596318438696 | [3.74, 31.81, 4.48] | [12.32, 6.76, 9.65] | 0.46419729279774347 | 1 | UNSTABLE | [12, 13, 10] | [11, 8, 6] | [6, 15, 9] | [6, 6, 14] | 1.5 | DISSIPATING | False | 4.479666493984369 | 9.10266759249963 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 47 | 20.913023034561995 | MEDIUM |
| SAIL | 55.441 | CANDIDATE | NO_TRADE | STABLE_UPTREND | 15.18534931315002 | [6.08, 19.41, 3.84] | [15.05, 5.9, 28.31] | 0.40374484018418394 | 2 | UNSTABLE | [11, 12, 6] | [12, 3, 14] | [18, 7, 12] | [9, 6, 6] | 1.4583333333333333 | DISSIPATING | False | 3.8441261244593683 | 14.750873925230195 | TOO_SMALL_UPSIDE | NO_TRADE | RISING | RISING | 23.5 | 20.30904098999389 | MEDIUM |

## Experimental recent-swing review shortlist (NOT BUY signals)
Count: 0 of 109 scored CANDIDATE names
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
    "observations": 170,
    "positive_net_pct": 43.529411764705884,
    "average_net_pct": -1.9499296484980808,
    "average_positive_pct": 3.5039273284194246,
    "average_nonpositive_pct": -6.153944401538662,
    "benchmark_pairs": 170,
    "average_excess_pct": -1.0180191614120713,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 1021,
    "positive_net_pct": 52.59549461312439,
    "average_net_pct": 0.7737545533879383,
    "average_positive_pct": 6.94974541810678,
    "average_nonpositive_pct": -6.078532831641027,
    "benchmark_pairs": 1021,
    "average_excess_pct": 1.7185010238159082,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 125,
    "positive_net_pct": 49.6,
    "average_net_pct": -0.7347386421806933,
    "average_positive_pct": 4.64653857382267,
    "average_nonpositive_pct": -6.030598759517336,
    "benchmark_pairs": 125,
    "average_excess_pct": 0.18302503461720004,
    "worst_adverse_excursion_pct": -25.57142802647182
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 115,
    "positive_net_pct": 48.69565217391305,
    "average_net_pct": -1.7607449925947185,
    "average_positive_pct": 5.8696552322948765,
    "average_nonpositive_pct": -9.00315876537128,
    "benchmark_pairs": 115,
    "average_excess_pct": -0.48297562309483033,
    "worst_adverse_excursion_pct": -95.51242232978043
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 657,
    "positive_net_pct": 53.272450532724505,
    "average_net_pct": 1.9529971416622787,
    "average_positive_pct": 11.530598261902368,
    "average_nonpositive_pct": -8.966092083367124,
    "benchmark_pairs": 657,
    "average_excess_pct": 3.3878340704544407,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 86,
    "positive_net_pct": 54.651162790697676,
    "average_net_pct": 1.6274984556190033,
    "average_positive_pct": 8.222045170619001,
    "average_nonpositive_pct": -6.319775790663046,
    "benchmark_pairs": 86,
    "average_excess_pct": 2.8608798482584588,
    "worst_adverse_excursion_pct": -30.81636301420778
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
- INDV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- VSME: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- MAMK: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
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
- LNAI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- KVUE: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- ADIL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- CCXI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
