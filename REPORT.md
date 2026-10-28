# OFTS daily research

Market session: 2026-10-27
Selected: 130; refreshed: 123; refresh errors: 8
Qualified prediction cohorts saved: 13; current coverage: 123/130
Outcome counts: {'CORPORATE_ACTION_REVIEW': 5, 'INELIGIBLE_DATA': 730, 'MATURE': 1306, 'MISSING_SESSIONS': 1, 'PENDING': 6308}
Cycle fingerprints saved: 109/150
Signal states: BUY=6, SELL=2, NO_TRADE=142
Cycle ledger: pending entries=6; open positions=26; closed trades=1; SPY pairs=1
Cycle-speed report card: READY; closed forward trades=1; groups=['MEDIUM_11_TO_25']
Score scale: theoretical 0-100; observed 13.932595241509777-68.3978448348677; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 9, '40_TO_49_999': 54, '50_TO_59_999': 39, '60_TO_69_999': 7, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=109
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=85; REVIEW=24; INSUFFICIENT=65
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| SCYX | 68.398 | CANDIDATE | NO_TRADE | STABLE_RANGE | 22.323463527984643 | [17.88, 18.25, 22.32] | [12.56, 3.98, 51.26] | 1.4532190612379912 | 3 | STABLE_3_OF_3 | [16, 18, 7] | [6, 5, 10] | [24, 7, 16] | [6, 5, 12] | 2.6666666666666665 | DISSIPATING | False | 22.323463527984643 | 15.128965832346518 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 25 | 27.6617157809988 | MEDIUM |
| ASO | 64.213 | CANDIDATE | NO_TRADE | STABLE_RANGE | 3.3333364159169876 | [29.86, 2.51, 29.11] | [2.66, 5.36, 3.23] | 9.007066123750718 | 2 | WATCH_2_OF_3 | [16, 7, 22] | [5, 4, 7] | [8, 15, 9] | [5, 4, 7] | 2.5 | DISSIPATING | False | 29.111809298613878 | 8.087706665405447 | TOO_SMALL | NO_TRADE | MIXED | MIXED | 31.0 | 15.450212978444922 | HIGH |
| SPGI | 62.022 | CANDIDATE | NO_TRADE | INSUFFICIENT | 4.370988740285164 | [4.3, 7.88, 4.37] | [19.63, 6.24, 4.72] | 0.7000410382722665 | 1 | UNSTABLE | [13, 11, 4] | [12, 8, 7] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 4.370988740285164 | 6.903881291687142 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | MIXED | 35 | 11.723543952355413 | HIGH |
| MESO | 61.211 | CANDIDATE | BUY | STABLE_RANGE | 7.364017811603918 | [10.48, 5.0, 7.36] | [11.73, 9.25, 4.97] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [11, 13, 8] | [7, 5, 6] | [14, 9, 4] | [6, 6, 10] | 1.6666666666666665 | DISSIPATING | False | 7.364017811603918 | 10.961563776598672 | FADING | NO_TRADE | FALLING | MIXED | 16.0 | 17.21854608824742 | MEDIUM |
| TT | 60.873 | CANDIDATE | NO_TRADE | INSUFFICIENT | 4.319998324760499 | [2.73, 13.36, 3.07] | [2.78, 3.24, 9.92] | 0.9480926253012288 | 1 | UNSTABLE | [11, 33, 6] | [3, 18, 11] | [18, 21, 6] | [15, 8, 15] | 1.1 | STABLE_OR_MIXED | False | 3.0741710089404073 | 6.894507949070816 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | INSUFFICIENT | 42.5 | 12.868832109870343 | HIGH |
| AKAM | 60.756 | CANDIDATE | NO_TRADE | DOWNTREND | 14.809186553508058 | [5.39, 13.36, 6.0] | [14.84, 13.34, 5.28] | 0.4493567985845546 | 3 | STABLE_3_OF_3 | [8, 10, 12] | [10, 7, 10] | [9, 16, 7] | [7, 11, 7] | 1.1428571428571428 | DISSIPATING | False | 5.996031051408424 | 12.31875251089575 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 29.5 | 17.906599335249563 | MEDIUM |
| WOR | 60.225 | CANDIDATE | NO_TRADE | INSUFFICIENT | 8.469851028030305 | [10.26, 8.47, 10.08] | [6.43, 3.09, 10.82] | 1.5681252779753838 | 3 | STABLE_3_OF_3 | [8, 6, 18] | [5, 8, 15] | [17, 3, 9] | [7, 10, 6] | 1.1428571428571428 | STABLE_OR_MIXED | False | 10.077780091279243 | 7.353104572302474 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 37 | 12.475830150764388 | HIGH |
| ATGL | 59.731 | CANDIDATE | NO_TRADE | IRREGULAR | 7.9497928402005975 | [4.02, 6.46, 11.36] | [10.12, 7.23, 32.71] | 0.6382818393478004 | 2 | WATCH_2_OF_3 | [4, 9, 3] | [7, 13, 5] | [9, 3, 2] | [16, 3, 7] | 0.5 | DISSIPATING | False | 11.363636117336174 | 20.128696054993185 | FADING | NO_TRADE | FALLING | FALLING | 21.5 | 32.03319957886376 | MEDIUM |
| FUBO | 59.446 | CANDIDATE | NO_TRADE | IRREGULAR | 8.468683359655271 | [10.83, 4.04, 8.47] | [24.1, 21.8, 14.75] | 0.38843602032248625 | 2 | WATCH_2_OF_3 | [6, 5, 13] | [6, 14, 7] | [8, 6, 12] | [4, 5, 15] | 1.2285714285714286 | DISSIPATING | False | 8.468683359655271 | 14.685663461095555 | WATCH | NO_TRADE | RISING | RISING | 21 | 24.901278854720466 | HIGH |
| NYAX | 59.260 | CANDIDATE | NO_TRADE | STABLE_RANGE | 11.995180160324592 | [5.29, 2.94, 16.75] | [7.24, 3.44, 16.98] | 0.7307811318654659 | 2 | WATCH_2_OF_3 | [5, 12, 10] | [4, 4, 5] | [12, 5, 14] | [4, 4, 4] | 2.75 | DISSIPATING | False | 16.748766621516097 | 8.778055688211552 | WATCH | NO_TRADE | MIXED | MIXED | 22.0 | 16.07010530360006 | MEDIUM |
| GLW | 59.221 | CANDIDATE | NO_TRADE | IRREGULAR | 11.227968443843794 | [16.88, 11.23, 11.47] | [6.14, 9.25, 4.98] | 1.8685319181458309 | 3 | STABLE_3_OF_3 | [8, 9, 10] | [3, 3, 8] | [7, 8, 9] | [8, 3, 7] | 2.071428571428571 | DISSIPATING | False | 11.465139720745743 | 13.055043292827767 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 20.5 | 17.6917131717661 | MEDIUM |
| XPRO | 59.080 | CANDIDATE | BUY | INSUFFICIENT | 6.618965891784978 | [6.34, 5.53, 6.88] | [19.33, 29.6, 5.13] | 0.32805539003287426 | 3 | STABLE_3_OF_3 | [22, 6, 6] | [11, 24, 10] | [5, 6, 5] | [17, 20, 24] | 0.3977272727272727 | DISSIPATING | False | 6.883370976826919 | 9.262520874636781 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | RISING | 21 | 14.95875149963658 | MEDIUM |
| LFCR | 58.705 | CANDIDATE | NO_TRADE | IRREGULAR | 8.695655679332305 | [3.91, 8.7, 56.9] | [3.65, 6.16, 7.97] | 1.4106287244879654 | 2 | WATCH_2_OF_3 | [7, 6, 5] | [2, 11, 5] | [5, 4, 8] | [8, 6, 10] | 0.9125 | STABLE_OR_MIXED | False | 56.904772663333205 | 11.036121615140166 | WATCH | NO_TRADE | FALLING | MIXED | 12 | 11.617739999739435 | LOW |
| EEFT | 58.570 | CANDIDATE | SELL | DOWNTREND | 8.321100997553987 | [3.77, 8.32, 7.26] | [8.25, 7.81, 5.34] | 0.9299372980162708 | 2 | WATCH_2_OF_3 | [8, 8, 33] | [9, 4, 7] | [6, 9, 25] | [11, 6, 7] | 1.2142857142857144 | STABLE_OR_MIXED | False | 7.261671573238626 | 7.900787776507285 | WATCH | NO_TRADE | FALLING | FALLING | 27.0 | 12.736936852846249 | MEDIUM |
| CHPT | 58.519 | CANDIDATE | NO_TRADE | IRREGULAR | 8.721803238921733 | [4.68, 16.7, 8.72] | [12.21, 90.56, 17.01] | 0.5128420127040436 | 2 | WATCH_2_OF_3 | [2, 7, 10] | [7, 10, 9] | [5, 12, 2] | [11, 8, 4] | 0.7013888888888888 | DISSIPATING | False | 8.721803238921733 | 17.062166110777145 | FADING | NO_TRADE | MIXED | MIXED | 26 | 24.28571729521672 | MEDIUM |
| CCS | 57.980 | CANDIDATE | NO_TRADE | DOWNTREND | 3.672368935275061 | [4.17, 7.24, 3.08] | [11.68, 6.09, 3.48] | 0.6840910734443489 | 1 | UNSTABLE | [4, 27, 17] | [8, 6, 2] | [22, 24, 3] | [8, 4, 2] | 4.166666666666667 | DISSIPATING | False | 3.0803486105271283 | 9.263526996345199 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 30.5 | 13.42962727806235 | MEDIUM |
| KTB | 57.822 | CANDIDATE | NO_TRADE | INSUFFICIENT | 7.062814711119647 | [3.34, 3.49, 23.4] | [5.63, 13.26, 5.37] | 0.6212021491906816 | 1 | UNSTABLE | [16, 4, 22] | [4, 13, 6] | [14, 5, 9] | [3, 13, 7] | 1.9761904761904763 | DISSIPATING | False | 23.40155526838572 | 9.431529748222447 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | FALLING | 29 | 15.945346795151156 | MEDIUM |
| CRNC | 57.641 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.804368129894389 | [3.82, 6.47, 19.56] | [6.64, 12.68, 4.55] | 0.9737109920041425 | 2 | WATCH_2_OF_3 | [4, 3, 17] | [8, 15, 4] | [4, 2, 7] | [9, 9, 12] | 0.4722222222222222 | STABLE_OR_MIXED | False | 19.556714277436903 | 11.965370435068952 | WATCH | NO_TRADE | FALLING | MIXED | 16 | 19.229020363714117 | MEDIUM |
| EPM | 57.552 | CANDIDATE | NO_TRADE | IRREGULAR | 5.7377058257448095 | [12.28, 6.34, 2.81] | [10.19, 9.43, 6.29] | 0.6720088429954724 | 2 | UNSTABLE | [14, 6, 2] | [10, 19, 2] | [14, 3, 5] | [18, 10, 5] | 0.55 | DISSIPATING | False | 2.8089928274849907 | 8.633041857154323 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 26 | 12.982888675563604 | LOW |
| DKNG | 57.535 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.885425907149978 | [6.02, 3.62, 6.89] | [20.13, 8.86, 4.29] | 0.67891670684082 | 2 | WATCH_2_OF_3 | [10, 9, 9] | [13, 5, 5] | [15, 7, 8] | [9, 7, 3] | 1.4714285714285715 | DISSIPATING | False | 6.885425907149978 | 10.437410233147245 | WATCH | NO_TRADE | MIXED | FALLING | 47 | 25.0024339747031 | MEDIUM |
| VIRC | 57.441 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.461537874661969 | [9.51, 4.46, 3.19] | [3.06, 10.32, 2.95] | 1.4599118296170084 | 1 | UNSTABLE | [9, 9, 9] | [9, 7, 2] | [4, 9, 14] | [7, 6, 6] | 1.3928571428571428 | STABLE_OR_MIXED | False | 3.1897896311569474 | 6.917197182068815 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 20.0 | 11.659188733927506 | MEDIUM |
| LTRX | 57.084 | CANDIDATE | BUY | STABLE_UPTREND | 5.525845550833175 | [3.56, 45.15, 5.53] | [22.24, 16.06, 6.54] | 0.34416404875986895 | 2 | WATCH_2_OF_3 | [10, 17, 11] | [10, 9, 8] | [3, 24, 4] | [8, 12, 9] | 0.8333333333333334 | DISSIPATING | False | 5.525845550833175 | 13.429411112096231 | FADING | NO_TRADE | RISING | RISING | 26.5 | 23.465208841666907 | LOW |
| FERG | 57.067 | CANDIDATE | NO_TRADE | INSUFFICIENT | 6.08606780511507 | [16.61, 4.34, 6.09] | [4.85, 5.97, 3.36] | 1.2544730128010313 | 2 | WATCH_2_OF_3 | [10, 19, 15] | [7, 12, 9] | [24, 11, 14] | [13, 9, 6] | 1.6111111111111112 | DISSIPATING | True | 6.08606780511507 | 7.144947741452169 | WATCH | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 43 | 15.39008433659906 | MEDIUM |
| DJT | 56.810 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.807807700304547 | [5.08, 9.71, 3.58] | [21.26, 4.87, 21.22] | 0.23931426913880552 | 2 | UNSTABLE | [5, 12, 21] | [7, 3, 17] | [10, 23, 5] | [5, 12, 10] | 1.3571428571428572 | DISSIPATING | False | 3.576983284817814 | 13.221392864653556 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 23 | 21.56931123663407 | MEDIUM |
| CCEL | 56.050 | CANDIDATE | NO_TRADE | IRREGULAR | 18.888886769612633 | [3.7, 21.29, 30.14] | [3.53, 17.85, 6.27] | 3.398493616168822 | 2 | WATCH_2_OF_3 | [3, 8, 6] | [2, 2, 3] | [4, 8, 6] | [2, 2, 4] | 3.0 | DISSIPATING | False | 30.136982901142506 | 10.217642007947585 | WATCH | NO_TRADE | MIXED | RISING | 54 | 26.011617268804855 | MEDIUM |

## Experimental recent-swing review shortlist (NOT BUY signals)
Count: 0 of 91 scored CANDIDATE names
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
    "observations": 87,
    "positive_net_pct": 43.67816091954023,
    "average_net_pct": -1.6787421760582086,
    "average_positive_pct": 3.12218785157421,
    "average_nonpositive_pct": -5.401912401569064,
    "benchmark_pairs": 87,
    "average_excess_pct": -0.9845332231692424,
    "worst_adverse_excursion_pct": -55.257270184399786
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 508,
    "positive_net_pct": 52.16535433070866,
    "average_net_pct": 0.6437642727482458,
    "average_positive_pct": 6.8243658503529385,
    "average_nonpositive_pct": -6.096397941512012,
    "benchmark_pairs": 508,
    "average_excess_pct": 1.3829989457082528,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 71,
    "positive_net_pct": 50.70422535211268,
    "average_net_pct": -0.7979541385930692,
    "average_positive_pct": 4.405116912193532,
    "average_nonpositive_pct": -6.149684362259287,
    "benchmark_pairs": 71,
    "average_excess_pct": -0.06313813929758183,
    "worst_adverse_excursion_pct": -25.57142802647182
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 27,
    "positive_net_pct": 40.74074074074074,
    "average_net_pct": 0.11971755448610884,
    "average_positive_pct": 6.178207379905422,
    "average_nonpositive_pct": -4.04549420048967,
    "benchmark_pairs": 27,
    "average_excess_pct": 1.3493129109639783,
    "worst_adverse_excursion_pct": -39.606737923462546
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 150,
    "positive_net_pct": 44.666666666666664,
    "average_net_pct": -0.4083933361047655,
    "average_positive_pct": 10.658007213798857,
    "average_nonpositive_pct": -9.341511852292028,
    "benchmark_pairs": 150,
    "average_excess_pct": 0.8722295601973328,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 24,
    "positive_net_pct": 41.666666666666664,
    "average_net_pct": -0.044351991854340585,
    "average_positive_pct": 10.715879269155037,
    "average_nonpositive_pct": -7.730231464003895,
    "benchmark_pairs": 24,
    "average_excess_pct": 1.229095156659975,
    "worst_adverse_excursion_pct": -30.81636301420778
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
- GAM.PRB: ValueError: EMPTY_PROVIDER_RESPONSE
- SPG.PRJ: ValueError: EMPTY_PROVIDER_RESPONSE
- GS.PRA: ValueError: EMPTY_PROVIDER_RESPONSE
- NVNI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SB.PRC: ValueError: EMPTY_PROVIDER_RESPONSE
- SLP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- NMI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
