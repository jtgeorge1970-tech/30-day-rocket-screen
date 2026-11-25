# OFTS daily research

Market session: 2026-11-24
Selected: 176; refreshed: 126; refresh errors: 54
Qualified prediction cohorts saved: 33; current coverage: 126/176
Outcome counts: {'CORPORATE_ACTION_REVIEW': 56, 'INELIGIBLE_DATA': 3805, 'MATURE': 7826, 'MISSING_SESSIONS': 14, 'PENDING': 11599}
Cycle fingerprints saved: 117/199
Signal states: BUY=4, SELL=1, NO_TRADE=194
Cycle ledger: pending entries=4; open positions=26; closed trades=44; SPY pairs=44
Cycle-speed report card: READY; closed forward trades=44; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 12.253230691540354-67.861463950846; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 25, '40_TO_49_999': 41, '50_TO_59_999': 40, '60_TO_69_999': 11, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=116
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=95; REVIEW=22; INSUFFICIENT=80
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| MWH | 67.861 | CANDIDATE | NO_TRADE | INSUFFICIENT | 12.10395016041691 | [15.21, 17.93, 9.84] | [9.76, 11.38, 13.52] | 1.3365853122913098 | 3 | STABLE_3_OF_3 | [3, 9, 5] | [9, 11, 17] | [5, 4, 11] | [5, 12, 19] | 0.4356060606060606 | STABLE_OR_MIXED | False | 9.842042335413549 | 11.550334361127312 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 47.5 | 35.23344052246027 | HIGH |
| CACC | 66.813 | CANDIDATE | NO_TRADE | IRREGULAR | 15.289628474476945 | [4.62, 7.15, 15.29] | [6.53, 7.07, 3.3] | 1.0950717066105202 | 2 | WATCH_2_OF_3 | [5, 5, 7] | [13, 27, 3] | [5, 4, 15] | [31, 9, 3] | 0.4700854700854701 | STABLE_OR_MIXED | False | 15.289628474476945 | 7.307305555010348 | WATCH | NO_TRADE | FALLING | FALLING | 42 | 15.646931501854873 | HIGH |
| WRBY | 63.359 | CANDIDATE | NO_TRADE | IRREGULAR | 14.200592976461513 | [11.01, 41.9, 8.87] | [18.71, 12.65, 6.29] | 0.8703031911300206 | 3 | STABLE_3_OF_3 | [8, 11, 7] | [9, 3, 9] | [6, 13, 9] | [10, 6, 8] | 1.0069444444444444 | STABLE_OR_MIXED | False | 8.873453820565746 | 13.421859820436337 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 33.0 | 27.91928135796663 | HIGH |
| JBS | 63.316 | CANDIDATE | NO_TRADE | INSUFFICIENT | 4.1530886506307985 | [9.27, 5.13, 3.19] | [4.56, 7.91, 19.98] | 0.6482455212975712 | 2 | UNSTABLE | [13, 3, 5] | [6, 12, 37] | [7, 4, 7] | [5, 36, 19] | 0.3925438596491228 | DISSIPATING | False | 3.193278374977382 | 10.044898013260841 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 57.5 | 22.97762566772592 | HIGH |
| CLSK | 61.542 | CANDIDATE | NO_TRADE | IRREGULAR | 13.087941938589797 | [21.65, 5.18, 13.09] | [4.17, 10.42, 13.99] | 1.2554730345319052 | 3 | STABLE_3_OF_3 | [4, 2, 8] | [21, 5, 4] | [3, 3, 8] | [23, 6, 5] | 0.65 | STABLE_OR_MIXED | False | 13.087941938589797 | 12.678696874132893 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 27 | 29.073334378324457 | MEDIUM |
| SMPL | 61.484 | CANDIDATE | NO_TRADE | STABLE_RANGE | 9.330321856112867 | [3.84, 36.31, 4.98] | [12.54, 3.66, 18.66] | 0.39717293579457325 | 1 | UNSTABLE | [4, 9, 6] | [11, 8, 22] | [19, 4, 8] | [8, 12, 7] | 0.7727272727272727 | DISSIPATING | False | 4.979248284632765 | 9.962139730343692 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 37 | 18.296229912909233 | MEDIUM |
| PWR | 61.208 | CANDIDATE | NO_TRADE | IRREGULAR | 19.424037511694525 | [17.32, 20.23, 19.42] | [23.5, 9.3, 7.94] | 2.0889449301000873 | 3 | STABLE_3_OF_3 | [17, 20, 6] | [8, 9, 18] | [28, 9, 11] | [8, 14, 11] | 1.4444444444444444 | STABLE_OR_MIXED | False | 19.424037511694525 | 11.360173245560635 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 35 | 19.81219643427886 | HIGH |
| YARW | 61.041 | CANDIDATE | BUY | DOWNTREND | 34.284257921351355 | [10.38, 4.41, 44.34] | [4.8, 6.09, 7.53] | 1.7048948678909543 | 2 | WATCH_2_OF_3 | [3, 5, 12] | [10, 5, 5] | [5, 9, 11] | [4, 5, 3] | 1.625 | DISSIPATING | False | 44.33822507470566 | 14.699030662777147 | WATCH | NO_TRADE | FALLING | FALLING | 36.5 | 44.85373798163754 | MEDIUM |
| TLN | 60.766 | CANDIDATE | NO_TRADE | STABLE_RANGE | 13.902963759783372 | [7.29, 22.28, 9.58] | [34.08, 6.38, 6.39] | 1.5009439453767632 | 3 | STABLE_3_OF_3 | [3, 7, 7] | [21, 4, 12] | [6, 3, 11] | [9, 17, 11] | 0.5643939393939394 | STABLE_OR_MIXED | False | 9.584876804487408 | 11.62079314244909 | CYCLE_TIMING | NO_TRADE | RISING | MIXED | 31 | 23.366879645868412 | HIGH |
| GAP | 60.299 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.557896664268096 | [5.48, 8.0, 3.49] | [16.71, 5.69, 3.84] | 0.9643884665975666 | 2 | UNSTABLE | [8, 4, 3] | [21, 5, 9] | [5, 3, 9] | [12, 8, 9] | 0.5 | STABLE_OR_MIXED | False | 3.491620186142308 | 9.556007395001348 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | MIXED | 45.0 | 21.01723332316722 | HIGH |
| TT | 60.116 | CANDIDATE | NO_TRADE | DOWNTREND | 9.07400153593555 | [3.07, 3.63, 8.26] | [9.92, 2.73, 13.36] | 0.3663484686261195 | 1 | UNSTABLE | [6, 4, 11] | [11, 11, 33] | [6, 9, 11] | [15, 18, 21] | 0.5227272727272727 | DISSIPATING | False | 8.258798834697112 | 6.985771816608114 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 44 | 13.113653636542994 | HIGH |
| ESNT | 59.589 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.7060436752457626 | [6.74, 8.31, 3.71] | [6.23, 3.06, 9.81] | 1.082920604364391 | 2 | UNSTABLE | [8, 11, 3] | [20, 6, 24] | [7, 12, 9] | [17, 21, 8] | 0.4647058823529412 | STABLE_OR_MIXED | False | 3.7060436752457626 | 7.271589781454671 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 53 | 12.641914967787642 | HIGH |
| TRNS | 59.411 | CANDIDATE | NO_TRADE | STABLE_RANGE | 9.145248611633328 | [9.97, 25.28, 9.15] | [13.37, 5.38, 7.42] | 1.3442016749303707 | 3 | STABLE_3_OF_3 | [6, 4, 3] | [17, 9, 12] | [6, 4, 11] | [9, 14, 4] | 0.5 | STABLE_OR_MIXED | False | 9.145248611633328 | 8.650532351009394 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 34 | 17.870775968554845 | MEDIUM |
| SPGI | 59.162 | CANDIDATE | NO_TRADE | INSUFFICIENT | 14.272715050622754 | [7.88, 4.37, 24.7] | [6.24, 4.72, 4.3] | 1.6695164333270074 | 2 | WATCH_2_OF_3 | [11, 4, 43] | [8, 7, 13] | [12, 21, 35] | [9, 10, 7] | 1.8541666666666667 | DISSIPATING | False | 24.70293218258719 | 7.63800743370442 | WATCH | NO_TRADE | RISING | INSUFFICIENT | 35 | 12.362397606590037 | MEDIUM |
| AKAM | 58.582 | CANDIDATE | NO_TRADE | DOWNTREND | 17.818606627850574 | [6.0, 14.14, 17.82] | [5.28, 5.39, 13.36] | 2.6259972073716815 | 3 | STABLE_3_OF_3 | [12, 12, 17] | [10, 8, 10] | [7, 13, 11] | [7, 9, 16] | 1.2111111111111112 | STABLE_OR_MIXED | False | 17.818606627850574 | 12.801346995584812 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 32 | 19.64519470497008 | MEDIUM |
| GLXY | 58.511 | CANDIDATE | NO_TRADE | DOWNTREND | 23.035445533438992 | [15.35, 23.04, 11.85] | [22.0, 7.7, 30.04] | 0.6977773326720461 | 3 | STABLE_3_OF_3 | [4, 6, 8] | [10, 21, 5] | [6, 3, 11] | [10, 23, 4] | 0.6 | DISSIPATING | False | 11.853831479972454 | 14.689558090444605 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 28 | 31.02357961284737 | MEDIUM |
| SITM | 58.129 | CANDIDATE | NO_TRADE | IRREGULAR | 23.556798692089032 | [6.46, 33.12, 21.48] | [16.78, 7.85, 8.9] | 2.413013107129545 | 3 | STABLE_3_OF_3 | [4, 6, 8] | [11, 11, 5] | [6, 3, 11] | [5, 17, 5] | 0.8727272727272727 | STABLE_OR_MIXED | False | 21.47603232950741 | 14.868605877453223 | CYCLE_TIMING | NO_TRADE | FALLING | MIXED | 32 | 27.82944861320112 | MEDIUM |
| CD | 57.916 | CANDIDATE | NO_TRADE | DOWNTREND | 9.836062476870634 | [17.83, 5.83, 9.84] | [84.29, 29.71, 32.16] | 0.3058556342515651 | 3 | STABLE_3_OF_3 | [6, 3, 7] | [8, 8, 5] | [3, 7, 3] | [11, 5, 9] | 0.5416666666666666 | DISSIPATING | False | 9.836062476870634 | 19.529273325517874 | FADING | NO_TRADE | FALLING | FALLING | 15 | 33.4228210858649 | MEDIUM |
| ATGL | 57.818 | CANDIDATE | NO_TRADE | IRREGULAR | 11.35190377120634 | [6.08, 18.17, 3.61] | [6.46, 11.36, 145.59] | 0.5348068156204089 | 2 | UNSTABLE | [4, 4, 4] | [9, 3, 9] | [11, 4, 4] | [9, 3, 2] | 0.8888888888888888 | DISSIPATING | False | 3.6088412157826433 | 19.31822536675701 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 21 | 31.890384715763037 | MEDIUM |
| SMP | 57.633 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.083103898942907 | [2.91, 26.84, 2.73] | [7.53, 3.64, 12.21] | 0.38627950173654124 | 1 | UNSTABLE | [15, 27, 10] | [4, 3, 20] | [18, 24, 3] | [4, 16, 14] | 2.517857142857143 | DISSIPATING | False | 2.7312339569521393 | 7.538478715179516 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | FALLING | 34.5 | 10.74892724482146 | HIGH |
| ECG | 57.482 | CANDIDATE | NO_TRADE | DOWNTREND | 14.050055197740107 | [9.84, 23.01, 9.82] | [3.64, 21.53, 13.86] | 0.7102868229830571 | 3 | STABLE_3_OF_3 | [3, 6, 8] | [3, 17, 17] | [5, 4, 11] | [5, 3, 28] | 0.6764705882352942 | STABLE_OR_MIXED | False | 9.818520214160964 | 10.580003685294654 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 33 | 24.58437900733869 | MEDIUM |
| STRZ | 57.362 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.868419607920643 | [7.46, 21.38, 9.87] | [11.7, 7.03, 23.4] | 0.8434828543681092 | 3 | STABLE_3_OF_3 | [6, 10, 5] | [13, 5, 16] | [16, 5, 8] | [16, 7, 5] | 0.8021978021978022 | STABLE_OR_MIXED | False | 9.868419607920643 | 14.452659077132765 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | FALLING | 55 | 27.400937576802434 | MEDIUM |
| BFAM | 57.116 | CANDIDATE | NO_TRADE | INSUFFICIENT | 11.472786593544626 | [11.66, 10.06, 5.6] | [6.43, 6.86, 5.1] | 1.5639209490413801 | 3 | STABLE_3_OF_3 | [17, 6, 7] | [22, 12, 5] | [15, 9, 12] | [17, 7, 7] | 1.1488095238095237 | STABLE_OR_MIXED | False | 5.597294230442529 | 9.785371777259604 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 67 | 18.832014695894472 | MEDIUM |
| SGML | 57.079 | CANDIDATE | NO_TRADE | DOWNTREND | 14.36313617215552 | [7.87, 11.21, 14.36] | [18.3, 3.53, 12.97] | 0.8648232679139778 | 3 | STABLE_3_OF_3 | [6, 3, 10] | [11, 6, 8] | [7, 3, 11] | [10, 9, 6] | 0.7638888888888888 | STABLE_OR_MIXED | False | 14.36313617215552 | 15.7747116325804 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 24 | 25.388311193241208 | MEDIUM |
| FN | 56.485 | CANDIDATE | NO_TRADE | DECAYING | 15.499575972268653 | [24.91, 5.88, 15.5] | [32.83, 16.63, 15.45] | 0.9322837777305417 | 3 | STABLE_3_OF_3 | [4, 2, 8] | [20, 15, 4] | [3, 3, 8] | [7, 28, 6] | 0.3476190476190476 | STABLE_OR_MIXED | False | 15.499575972268653 | 14.019547947259346 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 27.5 | 25.062328495303454 | LOW |

## Experimental recent-swing review shortlist (NOT BUY signals)
Count: 0 of 93 scored CANDIDATE names
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
    "model_hash": "2efb29d640e0ca751d9f8d30781f9021b2e38310114999e253e7b21b7283c3c6",
    "horizon": 20,
    "score_band": "0-40",
    "observations": 9,
    "positive_net_pct": 33.333333333333336,
    "average_net_pct": -6.584737508786917,
    "average_positive_pct": 2.8321757461285664,
    "average_nonpositive_pct": -11.293194136244658,
    "benchmark_pairs": 9,
    "average_excess_pct": -0.8003555737755099,
    "worst_adverse_excursion_pct": -31.422505458317453
  },
  {
    "model_hash": "2efb29d640e0ca751d9f8d30781f9021b2e38310114999e253e7b21b7283c3c6",
    "horizon": 20,
    "score_band": "40-60",
    "observations": 76,
    "positive_net_pct": 39.473684210526315,
    "average_net_pct": -6.370612734615107,
    "average_positive_pct": 13.220480505917298,
    "average_nonpositive_pct": -19.14741267409276,
    "benchmark_pairs": 76,
    "average_excess_pct": -0.5862307996037003,
    "worst_adverse_excursion_pct": -66.20208824777455
  },
  {
    "model_hash": "2efb29d640e0ca751d9f8d30781f9021b2e38310114999e253e7b21b7283c3c6",
    "horizon": 20,
    "score_band": "60-80",
    "observations": 11,
    "positive_net_pct": 27.272727272727273,
    "average_net_pct": -7.709895828528918,
    "average_positive_pct": 9.604041197653755,
    "average_nonpositive_pct": -14.20262221334742,
    "benchmark_pairs": 11,
    "average_excess_pct": -1.925513893517512,
    "worst_adverse_excursion_pct": -30.48245601804731
  },
  {
    "model_hash": "2efb29d640e0ca751d9f8d30781f9021b2e38310114999e253e7b21b7283c3c6",
    "horizon": 30,
    "score_band": "0-40",
    "observations": 9,
    "positive_net_pct": 33.333333333333336,
    "average_net_pct": -10.218361391121903,
    "average_positive_pct": 2.0275411297380272,
    "average_nonpositive_pct": -16.341312651551867,
    "benchmark_pairs": 9,
    "average_excess_pct": 1.4059212549814195,
    "worst_adverse_excursion_pct": -35.39192389633718
  },
  {
    "model_hash": "2efb29d640e0ca751d9f8d30781f9021b2e38310114999e253e7b21b7283c3c6",
    "horizon": 30,
    "score_band": "40-60",
    "observations": 76,
    "positive_net_pct": 21.05263157894737,
    "average_net_pct": -15.281089589747912,
    "average_positive_pct": 12.852476577733565,
    "average_nonpositive_pct": -22.783373901076313,
    "benchmark_pairs": 76,
    "average_excess_pct": -3.656806943644589,
    "worst_adverse_excursion_pct": -74.2160265141408
  },
  {
    "model_hash": "2efb29d640e0ca751d9f8d30781f9021b2e38310114999e253e7b21b7283c3c6",
    "horizon": 30,
    "score_band": "60-80",
    "observations": 11,
    "positive_net_pct": 18.181818181818183,
    "average_net_pct": -18.6451848104542,
    "average_positive_pct": 15.295519477028343,
    "average_nonpositive_pct": -26.187563541005876,
    "benchmark_pairs": 11,
    "average_excess_pct": -7.0209021643508756,
    "worst_adverse_excursion_pct": -48.88093107299715
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "0-40",
    "observations": 338,
    "positive_net_pct": 36.3905325443787,
    "average_net_pct": -2.182889189127413,
    "average_positive_pct": 4.120346278831494,
    "average_nonpositive_pct": -5.788926224285304,
    "benchmark_pairs": 338,
    "average_excess_pct": -0.47794331655955846,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 2011,
    "positive_net_pct": 43.11287916459473,
    "average_net_pct": -1.1687409337336045,
    "average_positive_pct": 6.3630193070898935,
    "average_nonpositive_pct": -6.876814472889163,
    "benchmark_pairs": 2011,
    "average_excess_pct": 0.37566083994750055,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 231,
    "positive_net_pct": 41.125541125541126,
    "average_net_pct": -2.290907375097576,
    "average_positive_pct": 5.048552303731988,
    "average_nonpositive_pct": -7.417735827221172,
    "benchmark_pairs": 231,
    "average_excess_pct": -0.6611251489335379,
    "worst_adverse_excursion_pct": -40.22770195885972
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 263,
    "positive_net_pct": 40.68441064638783,
    "average_net_pct": -3.1049208396020145,
    "average_positive_pct": 5.875844544035734,
    "average_nonpositive_pct": -9.264804788635596,
    "benchmark_pairs": 263,
    "average_excess_pct": -0.7365803239897639,
    "worst_adverse_excursion_pct": -95.51242232978043
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 1641,
    "positive_net_pct": 40.95063985374772,
    "average_net_pct": -1.8714426419651766,
    "average_positive_pct": 10.238662994059453,
    "average_nonpositive_pct": -10.269782154254699,
    "benchmark_pairs": 1641,
    "average_excess_pct": 0.649883747343018,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 182,
    "positive_net_pct": 48.35164835164835,
    "average_net_pct": -0.7743746875747317,
    "average_positive_pct": 8.255365514938704,
    "average_nonpositive_pct": -9.227748494183057,
    "benchmark_pairs": 182,
    "average_excess_pct": 1.4537670570890247,
    "worst_adverse_excursion_pct": -39.22651609852351
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "0-40",
    "observations": 145,
    "positive_net_pct": 44.827586206896555,
    "average_net_pct": -5.689381592230983,
    "average_positive_pct": 6.143970573024969,
    "average_nonpositive_pct": -15.30398022650144,
    "benchmark_pairs": 145,
    "average_excess_pct": -1.3097913443741878,
    "worst_adverse_excursion_pct": -98.15217388688697
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "40-60",
    "observations": 876,
    "positive_net_pct": 40.52511415525114,
    "average_net_pct": -3.496374840846556,
    "average_positive_pct": 14.19266314445808,
    "average_nonpositive_pct": -15.549366174403449,
    "benchmark_pairs": 876,
    "average_excess_pct": 1.0531165417553243,
    "worst_adverse_excursion_pct": -93.04037981042042
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "60-80",
    "observations": 107,
    "positive_net_pct": 41.12149532710281,
    "average_net_pct": -3.6697860484890428,
    "average_positive_pct": 11.338162005828117,
    "average_nonpositive_pct": -14.1515275467423,
    "benchmark_pairs": 107,
    "average_excess_pct": 0.48208943200163756,
    "worst_adverse_excursion_pct": -47.09677302750536
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 30,
    "score_band": "0-40",
    "observations": 26,
    "positive_net_pct": 42.30769230769231,
    "average_net_pct": -8.212541400123621,
    "average_positive_pct": 3.776383337460351,
    "average_nonpositive_pct": -17.004419541018535,
    "benchmark_pairs": 26,
    "average_excess_pct": -0.8305298606339417,
    "worst_adverse_excursion_pct": -70.50561884289033
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 30,
    "score_band": "40-60",
    "observations": 150,
    "positive_net_pct": 30.666666666666668,
    "average_net_pct": -7.364140921609146,
    "average_positive_pct": 18.16006961621672,
    "average_nonpositive_pct": -18.65369558257058,
    "benchmark_pairs": 150,
    "average_excess_pct": 0.0045156453707307816,
    "worst_adverse_excursion_pct": -92.76315784314002
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 30,
    "score_band": "60-80",
    "observations": 24,
    "positive_net_pct": 33.333333333333336,
    "average_net_pct": -15.784847920291801,
    "average_positive_pct": 11.378462453630164,
    "average_nonpositive_pct": -29.366503107252786,
    "benchmark_pairs": 24,
    "average_excess_pct": -8.414834988916398,
    "worst_adverse_excursion_pct": -57.419351836769096
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
- BKH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- BIPC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- GSL.PRB: ValueError: EMPTY_PROVIDER_RESPONSE
- BWMN: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SB.PRD: ValueError: EMPTY_PROVIDER_RESPONSE
- MET.PRA: ValueError: EMPTY_PROVIDER_RESPONSE
- WKEY: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ACVA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- CBZ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- MIMI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- BZH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- NATH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WALD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- LRHC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WFC.PRL: ValueError: EMPTY_PROVIDER_RESPONSE
- INDV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- MAMK: ValueError: EMPTY_PROVIDER_RESPONSE
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
- KVUE: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ADIL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- CCXI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- GNTA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ALDF: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- MGPI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ITGR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- VSME: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- IBO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- KAZR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- KNRX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- LXFR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SSTI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ARI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- CLGN: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- PTLE: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- UTZ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- VABK: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- ACH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- IPFX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- PASG: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- INM: ValueError: EMPTY_PROVIDER_RESPONSE
