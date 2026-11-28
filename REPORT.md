# OFTS daily research

Market session: 2026-11-27
Selected: 177; refreshed: 123; refresh errors: 60
Qualified prediction cohorts saved: 35; current coverage: 123/177
Outcome counts: {'CORPORATE_ACTION_REVIEW': 69, 'INELIGIBLE_DATA': 4370, 'MATURE': 8738, 'MISSING_SESSIONS': 23, 'PENDING': 11880}
Cycle fingerprints saved: 122/203
Signal states: BUY=10, SELL=0, NO_TRADE=193
Cycle ledger: pending entries=9; open positions=29; closed trades=45; SPY pairs=45
Cycle-speed report card: READY; closed forward trades=45; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 11.688651812478852-67.91193702808391; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 19, '40_TO_49_999': 52, '50_TO_59_999': 44, '60_TO_69_999': 7, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=122
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=101; REVIEW=21; INSUFFICIENT=82
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| MWH | 67.912 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.842042335413549 | [15.21, 17.93, 9.84] | [9.76, 11.38, 13.52] | 1.3365853122913098 | 3 | STABLE_3_OF_3 | [3, 9, 5] | [9, 11, 17] | [4, 11, 2] | [12, 19, 5] | 0.3939393939393939 | STABLE_OR_MIXED | False | 9.842042335413549 | 11.421858318531408 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 47.5 | 35.23344052246027 | HIGH |
| WRBY | 63.416 | CANDIDATE | NO_TRADE | IRREGULAR | 14.200592976461513 | [11.01, 41.9, 8.87] | [18.71, 12.65, 6.29] | 0.8703031911300206 | 3 | STABLE_3_OF_3 | [8, 11, 7] | [9, 3, 9] | [6, 13, 9] | [10, 6, 8] | 1.0069444444444444 | STABLE_OR_MIXED | False | 8.873453820565746 | 13.52327415134402 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 33.0 | 27.91928135796663 | HIGH |
| TRNS | 63.339 | CANDIDATE | BUY | STABLE_RANGE | 9.145248611633328 | [9.97, 25.28, 9.15] | [13.37, 5.38, 7.42] | 1.3442016749303707 | 3 | STABLE_3_OF_3 | [6, 4, 3] | [17, 9, 12] | [6, 4, 11] | [9, 14, 4] | 0.5 | STABLE_OR_MIXED | False | 9.145248611633328 | 8.703646615928049 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 34 | 17.870775968554845 | MEDIUM |
| ASAN | 62.035 | CANDIDATE | BUY | IRREGULAR | 7.98668886511491 | [26.61, 21.91, 5.24] | [16.19, 22.3, 4.3] | 1.352700286712471 | 3 | STABLE_3_OF_3 | [16, 6, 8] | [12, 12, 4] | [13, 11, 14] | [16, 9, 5] | 1.0555555555555556 | STABLE_OR_MIXED | False | 5.244122076861135 | 15.000283902146172 | FADING | NO_TRADE | MIXED | MIXED | 33 | 26.84147887311239 | MEDIUM |
| CLSK | 61.628 | CANDIDATE | NO_TRADE | IRREGULAR | 13.087941938589797 | [21.65, 5.18, 13.09] | [4.17, 10.42, 13.99] | 1.2554730345319052 | 3 | STABLE_3_OF_3 | [4, 2, 8] | [21, 5, 4] | [3, 3, 8] | [23, 6, 5] | 0.65 | STABLE_OR_MIXED | False | 13.087941938589797 | 12.457254952383144 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 27 | 29.073334378324457 | MEDIUM |
| YARW | 61.116 | CANDIDATE | NO_TRADE | DOWNTREND | 34.284257921351355 | [10.38, 4.41, 44.34] | [4.8, 6.09, 7.53] | 1.7048948678909543 | 2 | WATCH_2_OF_3 | [3, 5, 12] | [10, 5, 5] | [5, 9, 11] | [4, 5, 3] | 1.625 | DISSIPATING | False | 44.33822507470566 | 14.903910187398981 | WATCH | NO_TRADE | FALLING | FALLING | 36.5 | 44.85373798163754 | MEDIUM |
| SMPL | 60.924 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.430826946479496 | [3.84, 36.31, 4.98] | [12.54, 3.66, 18.66] | 0.39717293579457325 | 1 | UNSTABLE | [4, 9, 6] | [11, 8, 22] | [4, 8, 12] | [12, 7, 19] | 0.606060606060606 | DISSIPATING | False | 4.979248284632765 | 9.88924246739229 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 37 | 18.296229912909233 | MEDIUM |
| GLXY | 59.101 | CANDIDATE | NO_TRADE | DOWNTREND | 23.035445533438992 | [15.35, 23.04, 11.85] | [22.0, 7.7, 30.04] | 0.6977773326720461 | 3 | STABLE_3_OF_3 | [4, 6, 8] | [10, 21, 5] | [6, 3, 11] | [10, 23, 4] | 0.6 | DISSIPATING | False | 11.853831479972454 | 14.789359209428106 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 28 | 31.02357961284737 | MEDIUM |
| SPGI | 59.055 | CANDIDATE | NO_TRADE | INSUFFICIENT | 14.272715050622754 | [7.88, 4.37, 24.7] | [6.24, 4.72, 4.3] | 1.6695164333270074 | 2 | WATCH_2_OF_3 | [11, 4, 43] | [8, 7, 13] | [12, 21, 35] | [9, 10, 7] | 1.8541666666666667 | DISSIPATING | False | 24.70293218258719 | 7.628868970437515 | WATCH | NO_TRADE | RISING | INSUFFICIENT | 35 | 12.362397606590037 | MEDIUM |
| LEGN | 58.993 | CANDIDATE | NO_TRADE | STABLE_RANGE | 15.118485670071902 | [11.24, 21.92, 15.12] | [11.49, 10.11, 17.0] | 1.3152434398607804 | 3 | STABLE_3_OF_3 | [11, 9, 8] | [6, 10, 19] | [4, 11, 14] | [11, 12, 18] | 0.9083333333333333 | STABLE_OR_MIXED | False | 15.118485670071902 | 14.934835332052627 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 43.5 | 24.778762331620573 | MEDIUM |
| AKAM | 58.528 | CANDIDATE | NO_TRADE | DOWNTREND | 17.818606627850574 | [6.0, 14.14, 17.82] | [5.28, 5.39, 13.36] | 2.6259972073716815 | 3 | STABLE_3_OF_3 | [12, 12, 17] | [10, 8, 10] | [7, 13, 11] | [7, 9, 16] | 1.2111111111111112 | STABLE_OR_MIXED | False | 17.818606627850574 | 12.772893303530779 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 27 | 17.260784530300764 | MEDIUM |
| ESNT | 58.379 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.7060436752457626 | [6.74, 8.31, 3.71] | [6.23, 3.06, 9.81] | 1.082920604364391 | 2 | UNSTABLE | [8, 11, 3] | [20, 6, 24] | [7, 12, 9] | [17, 21, 8] | 0.4647058823529412 | STABLE_OR_MIXED | False | 3.7060436752457626 | 7.271589781454671 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 53 | 12.641914967787642 | HIGH |
| TT | 58.060 | CANDIDATE | NO_TRADE | DOWNTREND | 9.07400153593555 | [3.07, 3.63, 8.26] | [9.92, 2.73, 13.36] | 0.3663484686261195 | 1 | UNSTABLE | [6, 4, 11] | [11, 11, 33] | [6, 9, 11] | [15, 18, 21] | 0.5227272727272727 | DISSIPATING | False | 8.258798834697112 | 7.098494077273868 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 41 | 12.708995341084723 | MEDIUM |
| SW | 57.987 | CANDIDATE | NO_TRADE | DOWNTREND | 12.050574200351338 | [10.17, 4.39, 12.05] | [5.55, 6.58, 4.78] | 1.8326494076968836 | 2 | WATCH_2_OF_3 | [19, 24, 6] | [5, 7, 9] | [25, 10, 17] | [4, 8, 15] | 2.419642857142857 | DISSIPATING | False | 12.050574200351338 | 10.26724368614649 | WATCH | NO_TRADE | FALLING | FALLING | 40 | 15.666353683374574 | MEDIUM |
| SITM | 57.857 | CANDIDATE | NO_TRADE | IRREGULAR | 21.47603232950741 | [6.46, 33.12, 21.48] | [16.78, 7.85, 8.9] | 2.413013107129545 | 3 | STABLE_3_OF_3 | [4, 6, 8] | [11, 11, 5] | [3, 11, 2] | [17, 5, 6] | 0.5227272727272727 | STABLE_OR_MIXED | False | 21.47603232950741 | 14.977920422718327 | CYCLE_TIMING | NO_TRADE | FALLING | MIXED | 32 | 27.82944861320112 | MEDIUM |
| CACC | 57.726 | CANDIDATE | BUY | IRREGULAR | 15.289628474476945 | [4.62, 7.15, 15.29] | [6.53, 7.07, 3.3] | 1.0950717066105202 | 2 | WATCH_2_OF_3 | [5, 5, 7] | [13, 27, 3] | [5, 4, 15] | [31, 9, 3] | 0.4700854700854701 | STABLE_OR_MIXED | False | 15.289628474476945 | 7.254804814247848 | WATCH | NO_TRADE | FALLING | FALLING | 29.0 | 14.342854817708329 | MEDIUM |
| SMP | 57.579 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.083103898942907 | [2.91, 26.84, 2.73] | [7.53, 3.64, 12.21] | 0.38627950173654124 | 1 | UNSTABLE | [15, 27, 10] | [4, 3, 20] | [18, 24, 3] | [4, 16, 14] | 2.517857142857143 | DISSIPATING | False | 2.7312339569521393 | 7.518781088805409 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | FALLING | 34.5 | 10.74892724482146 | HIGH |
| ECG | 57.467 | CANDIDATE | NO_TRADE | DOWNTREND | 14.050055197740107 | [9.84, 23.01, 9.82] | [3.64, 21.53, 13.86] | 0.7102868229830571 | 3 | STABLE_3_OF_3 | [3, 6, 8] | [3, 17, 17] | [5, 4, 11] | [5, 3, 28] | 0.6764705882352942 | STABLE_OR_MIXED | False | 9.818520214160964 | 10.495417442166536 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 33 | 24.58437900733869 | MEDIUM |
| TLN | 57.420 | CANDIDATE | NO_TRADE | STABLE_RANGE | 13.902963759783372 | [7.29, 22.28, 9.58] | [34.08, 6.38, 6.39] | 1.5009439453767632 | 3 | STABLE_3_OF_3 | [3, 7, 7] | [21, 4, 12] | [6, 3, 11] | [9, 17, 11] | 0.5643939393939394 | STABLE_OR_MIXED | False | 9.584876804487408 | 11.761330637123255 | CYCLE_TIMING | NO_TRADE | RISING | MIXED | 32 | 23.203330155509867 | MEDIUM |
| SGI | 57.314 | CANDIDATE | BUY | DOWNTREND | 7.41393276469402 | [6.85, 12.36, 7.39] | [5.9, 6.67, 11.83] | 1.1080127767232346 | 3 | STABLE_3_OF_3 | [33, 9, 10] | [7, 6, 23] | [13, 16, 3] | [6, 19, 28] | 1.056390977443609 | STABLE_OR_MIXED | False | 7.394667453528592 | 9.23610396670457 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 44 | 20.52416090953542 | MEDIUM |
| SGML | 57.184 | CANDIDATE | NO_TRADE | DOWNTREND | 14.36313617215552 | [7.87, 11.21, 14.36] | [18.3, 3.53, 12.97] | 0.8648232679139778 | 3 | STABLE_3_OF_3 | [6, 3, 10] | [11, 6, 8] | [3, 11, 2] | [9, 6, 7] | 0.5892857142857143 | STABLE_OR_MIXED | False | 14.36313617215552 | 15.523478670868316 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 24 | 25.388311193241208 | MEDIUM |
| CD | 56.799 | CANDIDATE | NO_TRADE | DOWNTREND | 5.472637553583393 | [5.83, 9.84, 54.74] | [29.71, 32.16, 17.83] | 0.3310798357896869 | 3 | STABLE_3_OF_3 | [3, 7, 4] | [8, 5, 6] | [7, 3, 3] | [5, 9, 3] | 0.6333333333333333 | DISSIPATING | False | 54.73684705855779 | 19.809311654049683 | FADING | NO_TRADE | FALLING | FALLING | 15 | 34.63362346555654 | MEDIUM |
| GAP | 56.319 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.557896664268096 | [5.48, 8.0, 3.49] | [16.71, 5.69, 3.84] | 0.9643884665975666 | 2 | UNSTABLE | [8, 4, 3] | [21, 5, 9] | [5, 3, 9] | [12, 8, 9] | 0.5 | STABLE_OR_MIXED | False | 3.491620186142308 | 9.517023241242113 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | MIXED | 37.0 | 20.598169570933965 | MEDIUM |
| MGY | 55.639 | CANDIDATE | NO_TRADE | DOWNTREND | 9.127960859404316 | [3.0, 13.2, 8.25] | [18.97, 5.41, 6.53] | 1.2632433271433978 | 2 | WATCH_2_OF_3 | [7, 24, 12] | [14, 8, 9] | [6, 28, 10] | [17, 5, 11] | 1.121212121212121 | STABLE_OR_MIXED | False | 8.24879061729189 | 8.069178542565018 | WATCH | NO_TRADE | FALLING | FALLING | 29 | 13.001615135593191 | MEDIUM |
| USAU | 55.231 | CANDIDATE | NO_TRADE | INSUFFICIENT | 8.323137072530374 | [12.24, 13.14, 5.69] | [8.86, 8.17, 8.81] | 1.3896971586006994 | 3 | STABLE_3_OF_3 | [5, 3, 10] | [10, 12, 26] | [2, 11, 2] | [9, 29, 6] | 0.3194444444444444 | STABLE_OR_MIXED | False | 5.692109393722844 | 12.599765007779517 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 37 | 28.34518755461911 | MEDIUM |

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
    "observations": 367,
    "positive_net_pct": 36.78474114441417,
    "average_net_pct": -1.8865445871937432,
    "average_positive_pct": 4.324279132484111,
    "average_nonpositive_pct": -5.500601493040772,
    "benchmark_pairs": 367,
    "average_excess_pct": -0.27767502644147946,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 2150,
    "positive_net_pct": 44.23255813953488,
    "average_net_pct": -1.0154146174411054,
    "average_positive_pct": 6.361865145535217,
    "average_nonpositive_pct": -6.8667849715615965,
    "benchmark_pairs": 2150,
    "average_excess_pct": 0.46279606151427544,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 248,
    "positive_net_pct": 41.53225806451613,
    "average_net_pct": -2.2367881753308065,
    "average_positive_pct": 4.915108774077636,
    "average_nonpositive_pct": -7.317101180772673,
    "benchmark_pairs": 248,
    "average_excess_pct": -0.6498895253577557,
    "worst_adverse_excursion_pct": -40.22770195885972
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 295,
    "positive_net_pct": 40.33898305084746,
    "average_net_pct": -3.098924585444279,
    "average_positive_pct": 5.694886778818205,
    "average_nonpositive_pct": -9.044740223780842,
    "benchmark_pairs": 295,
    "average_excess_pct": -0.4632573894809871,
    "worst_adverse_excursion_pct": -95.51242232978043
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 1793,
    "positive_net_pct": 40.15616285554936,
    "average_net_pct": -2.1026078305596045,
    "average_positive_pct": 9.904735539477965,
    "average_nonpositive_pct": -10.159725469354616,
    "benchmark_pairs": 1793,
    "average_excess_pct": 0.6081431004618187,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 197,
    "positive_net_pct": 45.68527918781726,
    "average_net_pct": -1.5978480284245786,
    "average_positive_pct": 8.105336508219144,
    "average_nonpositive_pct": -9.759405115321172,
    "benchmark_pairs": 197,
    "average_excess_pct": 0.8211912656705647,
    "worst_adverse_excursion_pct": -54.17457361302592
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "0-40",
    "observations": 168,
    "positive_net_pct": 46.42857142857143,
    "average_net_pct": -5.450471507166101,
    "average_positive_pct": 6.473217598964384,
    "average_nonpositive_pct": -15.78433539914585,
    "benchmark_pairs": 168,
    "average_excess_pct": -0.9182667255090972,
    "worst_adverse_excursion_pct": -98.15217388688697
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "40-60",
    "observations": 1018,
    "positive_net_pct": 40.86444007858546,
    "average_net_pct": -2.9814376481981135,
    "average_positive_pct": 15.48925409229253,
    "average_nonpositive_pct": -15.745237920696631,
    "benchmark_pairs": 1018,
    "average_excess_pct": 1.7463074764560924,
    "worst_adverse_excursion_pct": -93.04037981042042
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "60-80",
    "observations": 125,
    "positive_net_pct": 39.2,
    "average_net_pct": -4.089467976064968,
    "average_positive_pct": 11.425302109770277,
    "average_nonpositive_pct": -14.092411847195589,
    "benchmark_pairs": 125,
    "average_excess_pct": 0.31327906590519694,
    "worst_adverse_excursion_pct": -47.09677302750536
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 30,
    "score_band": "0-40",
    "observations": 49,
    "positive_net_pct": 53.06122448979592,
    "average_net_pct": -8.016366873738486,
    "average_positive_pct": 3.970598153681323,
    "average_nonpositive_pct": -21.56684907864784,
    "benchmark_pairs": 49,
    "average_excess_pct": -1.1043111808709116,
    "worst_adverse_excursion_pct": -91.17210610065763
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 30,
    "score_band": "40-60",
    "observations": 291,
    "positive_net_pct": 34.707903780068726,
    "average_net_pct": -5.306703370282399,
    "average_positive_pct": 18.607349733191455,
    "average_nonpositive_pct": -18.018910546339548,
    "benchmark_pairs": 291,
    "average_excess_pct": 1.5636621319066437,
    "worst_adverse_excursion_pct": -92.76315784314002
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 30,
    "score_band": "60-80",
    "observations": 47,
    "positive_net_pct": 34.04255319148936,
    "average_net_pct": -12.684417872466417,
    "average_positive_pct": 13.010142707269143,
    "average_nonpositive_pct": -25.946126558781547,
    "benchmark_pairs": 47,
    "average_excess_pct": -5.8124710078732615,
    "worst_adverse_excursion_pct": -59.81042943637307
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
- WPRT: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- DYNC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
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
- LXFR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SSTI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ARI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- CLGN: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- PTLE: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- UTZ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- VABK: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- ACH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- IPFX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- ASA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- CLBR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- FTRA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- KTN: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- MPV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- RDIB: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
