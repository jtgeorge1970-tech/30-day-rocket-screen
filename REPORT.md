# OFTS daily research

Market session: 2026-10-30
Selected: 135; refreshed: 124; refresh errors: 12
Qualified prediction cohorts saved: 16; current coverage: 124/135
Outcome counts: {'CORPORATE_ACTION_REVIEW': 9, 'INELIGIBLE_DATA': 1010, 'MATURE': 2000, 'PENDING': 7346}
Cycle fingerprints saved: 127/163
Signal states: BUY=2, SELL=1, NO_TRADE=160
Cycle ledger: pending entries=2; open positions=33; closed trades=3; SPY pairs=3
Cycle-speed report card: READY; closed forward trades=3; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 11.58497992944324-66.73869727478981; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 13, '40_TO_49_999': 59, '50_TO_59_999': 47, '60_TO_69_999': 8, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=127
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=99; REVIEW=28; INSUFFICIENT=78
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| SCYX | 66.739 | CANDIDATE | NO_TRADE | STABLE_RANGE | 22.323463527984643 | [18.25, 22.32, 7.92] | [3.98, 51.26, 17.88] | 1.0206244779698799 | 3 | STABLE_3_OF_3 | [18, 7, 19] | [5, 10, 16] | [24, 7, 16] | [6, 5, 12] | 2.2333333333333334 | DISSIPATING | False | 7.92349603967859 | 14.82548657813385 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 25 | 27.6617157809988 | MEDIUM |
| ASO | 63.005 | CANDIDATE | NO_TRADE | STABLE_RANGE | 5.082550099856398 | [29.86, 2.51, 29.11] | [2.66, 5.36, 3.23] | 9.007066123750718 | 2 | WATCH_2_OF_3 | [16, 7, 22] | [5, 4, 7] | [15, 9, 19] | [4, 7, 8] | 2.6714285714285717 | DISSIPATING | False | 29.111809298613878 | 7.9546806633031775 | TOO_SMALL | NO_TRADE | RISING | MIXED | 31.0 | 15.450212978444922 | HIGH |
| CRNC | 62.626 | CANDIDATE | NO_TRADE | IRREGULAR | 6.804368129894389 | [3.82, 6.47, 19.56] | [6.64, 12.68, 4.55] | 0.9737109920041425 | 2 | WATCH_2_OF_3 | [4, 3, 17] | [8, 15, 4] | [4, 2, 7] | [9, 9, 12] | 0.4722222222222222 | STABLE_OR_MIXED | False | 19.556714277436903 | 11.91872729819917 | WATCH | NO_TRADE | FALLING | FALLING | 16.5 | 19.819817420347153 | MEDIUM |
| AKAM | 62.339 | CANDIDATE | NO_TRADE | DOWNTREND | 14.143262278384672 | [13.36, 6.0, 14.14] | [13.34, 5.28, 5.39] | 2.4808292663919276 | 3 | STABLE_3_OF_3 | [10, 12, 12] | [7, 10, 8] | [9, 16, 7] | [7, 11, 7] | 1.3928571428571428 | STABLE_OR_MIXED | False | 14.143262278384672 | 12.341529444868335 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 28.0 | 17.07072257644503 | MEDIUM |
| EEFT | 62.063 | CANDIDATE | NO_TRADE | DOWNTREND | 12.004174664675238 | [3.77, 8.32, 7.26] | [8.25, 7.81, 5.34] | 0.9299372980162708 | 2 | WATCH_2_OF_3 | [8, 8, 33] | [9, 4, 7] | [9, 25, 14] | [6, 7, 6] | 1.7380952380952381 | DISSIPATING | False | 7.261671573238626 | 7.872956456943487 | WATCH | NO_TRADE | FALLING | FALLING | 30.5 | 12.877679514179475 | HIGH |
| SPGI | 61.808 | CANDIDATE | NO_TRADE | INSUFFICIENT | 4.370988740285164 | [4.3, 7.88, 4.37] | [19.63, 6.24, 4.72] | 0.7000410382722665 | 1 | UNSTABLE | [13, 11, 4] | [12, 8, 7] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 4.370988740285164 | 6.87787740888614 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | MIXED | 35 | 11.723543952355413 | HIGH |
| TT | 60.524 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.634527680280586 | [13.36, 3.07, 3.63] | [3.24, 9.92, 2.73] | 1.120909955921715 | 1 | UNSTABLE | [33, 6, 4] | [18, 11, 11] | [18, 21, 6] | [15, 8, 15] | 0.8727272727272727 | STABLE_OR_MIXED | False | 3.634527680280586 | 6.850245425140239 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | INSUFFICIENT | 42.5 | 12.868832109870343 | HIGH |
| ADXN | 60.410 | CANDIDATE | NO_TRADE | DOWNTREND | 8.609271261766393 | [16.63, 13.96, 10.51] | [5.4, 11.96, 4.98] | 2.586691461786436 | 3 | STABLE_3_OF_3 | [8, 4, 3] | [6, 15, 2] | [10, 2, 4] | [8, 9, 2] | 0.5833333333333333 | STABLE_OR_MIXED | False | 10.507245030981016 | 10.163268874166157 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 19 | 19.797282719189745 | MEDIUM |
| MESO | 59.975 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.364017811603918 | [5.0, 7.36, 27.61] | [9.25, 4.97, 10.48] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [13, 8, 6] | [5, 6, 11] | [14, 9, 4] | [6, 6, 10] | 1.4166666666666665 | DISSIPATING | False | 27.60586658826034 | 11.58624625396103 | WATCH | NO_TRADE | FALLING | MIXED | 16 | 19.497767288923384 | MEDIUM |
| NYAX | 59.813 | CANDIDATE | NO_TRADE | STABLE_RANGE | 16.748766621516097 | [2.94, 16.75, 18.54] | [3.44, 16.98, 5.29] | 3.1667565986879476 | 2 | WATCH_2_OF_3 | [12, 10, 16] | [4, 5, 5] | [12, 5, 14] | [4, 4, 4] | 2.7 | DISSIPATING | False | 18.53881066969101 | 9.366093637301285 | WATCH | NO_TRADE | FALLING | MIXED | 25.5 | 16.554543782118735 | MEDIUM |
| MH | 59.718 | CANDIDATE | SELL | STABLE_RANGE | 4.879997253417967 | [6.92, 4.88, 17.55] | [7.83, 3.58, 9.99] | 0.8837717803312876 | 2 | WATCH_2_OF_3 | [5, 5, 16] | [7, 9, 7] | [6, 6, 5] | [12, 12, 5] | 0.6071428571428572 | STABLE_OR_MIXED | False | 17.553614069597167 | 9.778120751441921 | TOO_SMALL | NO_TRADE | MIXED | RISING | 23 | 14.918626093934574 | MEDIUM |
| XPRO | 59.688 | CANDIDATE | NO_TRADE | INSUFFICIENT | 6.618965891784978 | [6.34, 5.53, 6.88] | [19.33, 29.6, 5.13] | 0.32805539003287426 | 3 | STABLE_3_OF_3 | [22, 6, 6] | [11, 24, 10] | [5, 6, 5] | [17, 20, 24] | 0.3977272727272727 | DISSIPATING | False | 6.883370976826919 | 9.372647302637372 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | RISING | 21 | 14.95875149963658 | MEDIUM |
| EE | 59.567 | CANDIDATE | NO_TRADE | STABLE_RANGE | 11.286232646508864 | [4.3, 4.9, 10.65] | [3.52, 5.39, 13.71] | 0.9075272236691071 | 1 | UNSTABLE | [6, 9, 18] | [11, 6, 17] | [11, 12, 15] | [14, 7, 15] | 0.8376623376623377 | STABLE_OR_MIXED | False | 10.650881669067246 | 8.342085727372215 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | FALLING | 29 | 12.565674412583611 | HIGH |
| GLW | 59.292 | CANDIDATE | NO_TRADE | IRREGULAR | 11.465139720745743 | [11.23, 11.47, 6.07] | [9.25, 4.98, 16.88] | 1.2134154140163043 | 3 | STABLE_3_OF_3 | [9, 10, 16] | [3, 8, 8] | [8, 9, 19] | [3, 7, 7] | 1.2678571428571428 | STABLE_OR_MIXED | False | 6.071626128711194 | 13.319487086937556 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 21.0 | 17.21659014301915 | MEDIUM |
| ATGL | 59.027 | CANDIDATE | NO_TRADE | IRREGULAR | 11.363636117336174 | [6.46, 11.36, 145.59] | [7.23, 32.71, 4.02] | 1.5708548121969454 | 3 | STABLE_3_OF_3 | [9, 3, 9] | [13, 5, 4] | [9, 3, 2] | [16, 3, 7] | 1.1142857142857143 | STABLE_OR_MIXED | False | 145.5947073175599 | 22.40447113990551 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 22 | 32.06849916938487 | MEDIUM |
| PLBL | 59.018 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.375234900937721 | [3.28, 10.84, 6.38] | [7.41, 5.59, 17.31] | 0.8606565668671475 | 2 | WATCH_2_OF_3 | [2, 4, 5] | [4, 12, 6] | [4, 3, 4] | [4, 8, 8] | 0.5833333333333333 | STABLE_OR_MIXED | False | 6.375234900937721 | 12.516555841344148 | WATCH | NO_TRADE | MIXED | FALLING | 15.0 | 18.62197432609234 | MEDIUM |
| FUBO | 58.549 | CANDIDATE | NO_TRADE | IRREGULAR | 8.468683359655271 | [10.83, 4.04, 8.47] | [24.1, 21.8, 14.75] | 0.38843602032248625 | 2 | WATCH_2_OF_3 | [6, 5, 13] | [6, 14, 7] | [8, 6, 12] | [4, 5, 15] | 1.2285714285714286 | DISSIPATING | False | 8.468683359655271 | 14.883469278734859 | WATCH | NO_TRADE | RISING | RISING | 23 | 25.859568709143034 | HIGH |
| BRCB | 58.409 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.652171899931369 | [21.31, 5.62, 5.65] | [7.42, 7.98, 19.1] | 0.707866566368476 | 3 | STABLE_3_OF_3 | [8, 9, 10] | [11, 6, 5] | [7, 13, 13] | [11, 6, 5] | 1.8333333333333333 | DISSIPATING | False | 5.652171899931369 | 12.812493106788954 | FADING | NO_TRADE | INSUFFICIENT | FALLING | 27.5 | 27.974946238849828 | HIGH |
| CCS | 58.140 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.672368935275061 | [7.24, 3.08, 9.03] | [6.09, 3.48, 4.17] | 1.7369855022054526 | 2 | WATCH_2_OF_3 | [27, 17, 5] | [6, 2, 4] | [22, 24, 3] | [8, 4, 2] | 4.875 | DISSIPATING | False | 9.026353919938401 | 9.13606263550888 | TOO_SMALL | NO_TRADE | FALLING | INSUFFICIENT | 35.0 | 17.292267882239752 | MEDIUM |
| EME | 58.130 | CANDIDATE | NO_TRADE | INSUFFICIENT | 13.062557728380074 | [5.3, 4.32, 13.06] | [3.37, 28.26, 4.75] | 1.1145064202784853 | 2 | WATCH_2_OF_3 | [7, 3, 17] | [16, 17, 8] | [5, 5, 26] | [7, 19, 6] | 0.5758928571428572 | STABLE_OR_MIXED | False | 13.062557728380074 | 9.383695582373424 | WATCH | NO_TRADE | FALLING | INSUFFICIENT | 41.5 | 18.085480819947296 | HIGH |
| TARS | 57.906 | CANDIDATE | BUY | INSUFFICIENT | 5.890997729114678 | [28.49, 5.82, 5.89] | [15.86, 6.67, 30.56] | 0.37132785936427515 | 3 | STABLE_3_OF_3 | [12, 17, 16] | [8, 8, 23] | [19, 17, 5] | [8, 4, 27] | 2.0625 | DISSIPATING | False | 5.890997729114678 | 11.06205348809888 | FADING | NO_TRADE | INSUFFICIENT | MIXED | 32 | 23.70560834640585 | MEDIUM |
| VST | 57.804 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.63755695645518 | [3.98, 4.3, 4.64] | [5.37, 11.84, 20.86] | 0.3633880069835668 | 0 | UNSTABLE | [4, 6, 4] | [9, 16, 21] | [10, 7, 4] | [5, 13, 22] | 0.3942307692307692 | DISSIPATING | False | 4.63755695645518 | 8.232390480223565 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 23.0 | 20.238881878143445 | MEDIUM |
| EPM | 57.494 | CANDIDATE | NO_TRADE | IRREGULAR | 5.7377058257448095 | [6.34, 2.81, 15.65] | [9.43, 6.29, 12.28] | 0.6720088429954724 | 2 | WATCH_2_OF_3 | [6, 2, 25] | [19, 2, 14] | [14, 3, 5] | [18, 10, 5] | 0.4642857142857143 | DISSIPATING | False | 15.652172590999713 | 8.906958041485016 | WATCH | NO_TRADE | MIXED | MIXED | 26 | 12.982888675563604 | LOW |
| BMBL | 57.354 | CANDIDATE | NO_TRADE | DOWNTREND | 4.942969915746687 | [9.62, 12.69, 3.95] | [7.89, 12.28, 4.21] | 1.2194054638810894 | 2 | UNSTABLE | [7, 15, 11] | [9, 5, 7] | [11, 18, 7] | [6, 8, 3] | 1.7023809523809523 | DISSIPATING | False | 3.952574868853298 | 10.348336975723969 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 20 | 16.065089686077847 | MEDIUM |
| SRAD | 57.300 | CANDIDATE | NO_TRADE | IRREGULAR | 4.385212586959231 | [9.6, 4.39, 7.33] | [6.5, 4.8, 12.21] | 1.1271952914054142 | 2 | WATCH_2_OF_3 | [14, 3, 7] | [8, 7, 5] | [7, 11, 5] | [8, 6, 6] | 1.0833333333333335 | STABLE_OR_MIXED | False | 7.3253886466613904 | 10.360767655867718 | TOO_SMALL | NO_TRADE | FALLING | FALLING | 27 | 15.038462844909056 | LOW |

## Experimental recent-swing review shortlist (NOT BUY signals)
Count: 0 of 108 scored CANDIDATE names
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
    "observations": 125,
    "positive_net_pct": 44.8,
    "average_net_pct": -1.997884482370004,
    "average_positive_pct": 3.0373630567880627,
    "average_nonpositive_pct": -6.084462195309882,
    "benchmark_pairs": 125,
    "average_excess_pct": -1.58881724247086,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 731,
    "positive_net_pct": 55.26675786593707,
    "average_net_pct": 1.1651515133607377,
    "average_positive_pct": 6.7758109007825835,
    "average_nonpositive_pct": -5.766672316970839,
    "benchmark_pairs": 731,
    "average_excess_pct": 1.612100499819087,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 94,
    "positive_net_pct": 51.06382978723404,
    "average_net_pct": -0.23769165842827164,
    "average_positive_pct": 4.535308206070623,
    "average_nonpositive_pct": -5.218213256166249,
    "benchmark_pairs": 94,
    "average_excess_pct": 0.2805044070971928,
    "worst_adverse_excursion_pct": -25.57142802647182
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 64,
    "positive_net_pct": 54.6875,
    "average_net_pct": 0.5770109861436212,
    "average_positive_pct": 6.228999452822132,
    "average_nonpositive_pct": -6.244354404675268,
    "benchmark_pairs": 64,
    "average_excess_pct": 1.4059024457467482,
    "worst_adverse_excursion_pct": -55.257270184399786
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 371,
    "positive_net_pct": 52.2911051212938,
    "average_net_pct": 2.5265373089078333,
    "average_positive_pct": 12.504571504324625,
    "average_nonpositive_pct": -8.409839153865374,
    "benchmark_pairs": 371,
    "average_excess_pct": 3.4275747560265497,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 56,
    "positive_net_pct": 55.357142857142854,
    "average_net_pct": 2.225331786817818,
    "average_positive_pct": 8.873202565141359,
    "average_nonpositive_pct": -6.018027978303371,
    "benchmark_pairs": 56,
    "average_excess_pct": 3.0555787316027656,
    "worst_adverse_excursion_pct": -30.81636301420778
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
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
