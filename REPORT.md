# OFTS daily research

Market session: 2026-11-23
Selected: 172; refreshed: 124; refresh errors: 55
Qualified prediction cohorts saved: 32; current coverage: 124/172
Outcome counts: {'CORPORATE_ACTION_REVIEW': 48, 'INELIGIBLE_DATA': 3535, 'MATURE': 7343, 'MISSING_SESSIONS': 15, 'PENDING': 11479}
Cycle fingerprints saved: 120/196
Signal states: BUY=5, SELL=1, NO_TRADE=190
Cycle ledger: pending entries=5; open positions=21; closed trades=44; SPY pairs=44
Cycle-speed report card: READY; closed forward trades=44; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 12.124295853709103-68.11134170759169; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 22, '40_TO_49_999': 48, '50_TO_59_999': 39, '60_TO_69_999': 11, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=117
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=97; REVIEW=23; INSUFFICIENT=82
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| MWH | 68.111 | CANDIDATE | NO_TRADE | INSUFFICIENT | 12.10395016041691 | [13.52, 15.21, 17.93] | [5.95, 9.76, 11.38] | 1.5594628841902478 | 3 | STABLE_3_OF_3 | [17, 3, 9] | [17, 9, 11] | [5, 4, 11] | [5, 12, 19] | 0.6174242424242424 | STABLE_OR_MIXED | False | 17.926114661922043 | 11.587471144295003 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 47.5 | 35.23344052246027 | HIGH |
| CACC | 66.834 | CANDIDATE | NO_TRADE | IRREGULAR | 15.289628474476945 | [5.0, 7.15, 15.29] | [7.2, 6.53, 7.07] | 1.0114146772919794 | 2 | WATCH_2_OF_3 | [8, 5, 7] | [13, 20, 27] | [8, 4, 15] | [16, 31, 9] | 0.425 | STABLE_OR_MIXED | False | 15.289628474476945 | 7.999128413819159 | WATCH | NO_TRADE | FALLING | FALLING | 42 | 15.646931501854873 | HIGH |
| WRBY | 63.352 | CANDIDATE | NO_TRADE | IRREGULAR | 14.200592976461513 | [11.01, 41.9, 8.87] | [18.71, 12.65, 6.29] | 0.8703031911300206 | 3 | STABLE_3_OF_3 | [8, 11, 7] | [9, 3, 9] | [6, 13, 9] | [10, 6, 8] | 1.0069444444444444 | STABLE_OR_MIXED | False | 8.873453820565746 | 13.468659010867796 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 33.0 | 27.91928135796663 | HIGH |
| JBS | 63.326 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.128208067290285 | [9.27, 5.13, 3.19] | [4.56, 7.91, 19.98] | 0.6482455212975712 | 2 | UNSTABLE | [13, 3, 5] | [6, 12, 37] | [19, 7, 4] | [18, 5, 36] | 0.4027777777777778 | DISSIPATING | False | 3.193278374977382 | 10.37515020898423 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 57.5 | 22.97762566772592 | HIGH |
| CLSK | 61.659 | CANDIDATE | NO_TRADE | IRREGULAR | 5.175032981235916 | [13.99, 21.65, 5.18] | [19.97, 4.17, 10.42] | 1.3416207754739036 | 3 | STABLE_3_OF_3 | [4, 4, 2] | [7, 21, 5] | [3, 3, 8] | [23, 6, 5] | 0.5357142857142857 | STABLE_OR_MIXED | False | 5.175032981235916 | 12.949020015430532 | TOO_SMALL | NO_TRADE | MIXED | FALLING | 27 | 29.073334378324457 | MEDIUM |
| HLIT | 61.576 | CANDIDATE | NO_TRADE | DOWNTREND | 13.79629393336872 | [10.69, 7.46, 15.36] | [21.57, 3.58, 6.82] | 1.566279906172395 | 3 | STABLE_3_OF_3 | [9, 7, 14] | [8, 8, 29] | [7, 9, 11] | [9, 25, 11] | 0.9715909090909092 | STABLE_OR_MIXED | False | 15.359820483878561 | 11.6111110003264 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 45.5 | 17.93938839074336 | MEDIUM |
| TLN | 61.536 | CANDIDATE | NO_TRADE | STABLE_RANGE | 13.902963759783372 | [6.39, 7.29, 22.28] | [10.91, 34.08, 6.38] | 0.6687327628073135 | 3 | STABLE_3_OF_3 | [12, 3, 7] | [18, 21, 4] | [6, 3, 11] | [9, 17, 11] | 0.4671717171717171 | DISSIPATING | False | 22.280017459847024 | 11.727088800664259 | CYCLE_TIMING | NO_TRADE | RISING | MIXED | 32.0 | 23.460024521868796 | HIGH |
| PWR | 61.257 | CANDIDATE | NO_TRADE | IRREGULAR | 19.424037511694525 | [17.32, 20.23, 19.42] | [23.5, 9.3, 7.94] | 2.0889449301000873 | 3 | STABLE_3_OF_3 | [17, 20, 6] | [8, 9, 18] | [28, 9, 11] | [8, 14, 11] | 1.4444444444444444 | STABLE_OR_MIXED | False | 19.424037511694525 | 11.440774564690765 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 35 | 19.81219643427886 | HIGH |
| TT | 60.178 | CANDIDATE | NO_TRADE | DOWNTREND | 9.07400153593555 | [3.07, 3.63, 8.26] | [9.92, 2.73, 13.36] | 0.3663484686261195 | 1 | UNSTABLE | [6, 4, 11] | [11, 11, 33] | [6, 9, 11] | [15, 18, 21] | 0.5227272727272727 | DISSIPATING | False | 8.258798834697112 | 6.985771816608114 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 44 | 13.113653636542994 | HIGH |
| SPGI | 60.089 | CANDIDATE | NO_TRADE | INSUFFICIENT | 14.272715050622754 | [7.88, 4.37, 24.7] | [6.24, 4.72, 4.3] | 1.6695164333270074 | 2 | WATCH_2_OF_3 | [11, 4, 43] | [8, 7, 13] | [12, 21, 35] | [9, 10, 7] | 1.8541666666666667 | DISSIPATING | False | 24.70293218258719 | 7.63800743370442 | WATCH | NO_TRADE | RISING | INSUFFICIENT | 35 | 12.362397606590037 | MEDIUM |
| OBE | 59.684 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.994571511853363 | [4.06, 4.99, 7.38] | [7.27, 13.97, 18.18] | 0.357473074980304 | 1 | UNSTABLE | [4, 10, 5] | [5, 10, 26] | [17, 9, 4] | [14, 3, 21] | 0.5714285714285714 | DISSIPATING | False | 7.383282327462348 | 12.903094345740078 | TOO_SMALL | NO_TRADE | MIXED | MIXED | 25 | 19.84161399857889 | MEDIUM |
| ESNT | 59.556 | CANDIDATE | NO_TRADE | INSUFFICIENT | 8.309903114311389 | [6.74, 8.31, 3.71] | [6.23, 3.06, 9.81] | 1.082920604364391 | 2 | UNSTABLE | [8, 11, 3] | [20, 6, 24] | [8, 7, 12] | [10, 17, 21] | 0.43529411764705883 | STABLE_OR_MIXED | False | 3.7060436752457626 | 7.429954445529278 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 53 | 12.641914967787642 | HIGH |
| TRNS | 59.375 | CANDIDATE | NO_TRADE | STABLE_RANGE | 9.145248611633328 | [9.97, 25.28, 9.15] | [13.37, 5.38, 7.42] | 1.3442016749303707 | 3 | STABLE_3_OF_3 | [6, 4, 3] | [17, 9, 12] | [6, 4, 11] | [9, 14, 4] | 0.5 | STABLE_OR_MIXED | False | 9.145248611633328 | 8.650532351009394 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 34 | 17.870775968554845 | MEDIUM |
| GLXY | 58.650 | CANDIDATE | NO_TRADE | DOWNTREND | 23.035445533438992 | [30.04, 15.35, 23.04] | [15.45, 22.0, 7.7] | 1.4909410362652467 | 3 | STABLE_3_OF_3 | [5, 4, 6] | [5, 10, 21] | [6, 3, 11] | [10, 23, 4] | 0.55 | STABLE_OR_MIXED | False | 23.035445533438992 | 14.812083649924661 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 28 | 31.02357961284737 | MEDIUM |
| AKAM | 58.595 | CANDIDATE | NO_TRADE | DOWNTREND | 17.818606627850574 | [6.0, 14.14, 17.82] | [5.28, 5.39, 13.36] | 2.6259972073716815 | 3 | STABLE_3_OF_3 | [12, 12, 17] | [10, 8, 10] | [7, 13, 11] | [7, 9, 16] | 1.2111111111111112 | STABLE_OR_MIXED | False | 17.818606627850574 | 12.801346995584812 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 32 | 19.64519470497008 | MEDIUM |
| SITM | 58.246 | CANDIDATE | BUY | IRREGULAR | 23.556798692089032 | [8.9, 6.46, 33.12] | [16.29, 16.78, 7.85] | 0.5463274672163875 | 3 | STABLE_3_OF_3 | [5, 4, 6] | [6, 11, 11] | [6, 3, 11] | [5, 17, 5] | 0.8272727272727273 | DISSIPATING | False | 33.115492270026415 | 14.83919441235197 | CYCLE_TIMING | NO_TRADE | FALLING | MIXED | 32 | 27.82944861320112 | MEDIUM |
| SMPL | 58.171 | CANDIDATE | SELL | STABLE_RANGE | 9.330321856112867 | [3.84, 36.31, 4.98] | [12.54, 3.66, 18.66] | 0.39717293579457325 | 1 | UNSTABLE | [4, 9, 6] | [11, 8, 22] | [19, 4, 8] | [8, 12, 7] | 0.7727272727272727 | DISSIPATING | False | 4.979248284632765 | 10.269691175380087 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 44 | 18.79529330282167 | HIGH |
| CD | 58.072 | CANDIDATE | BUY | DOWNTREND | 9.836062476870634 | [17.83, 5.83, 9.84] | [84.29, 29.71, 32.16] | 0.3058556342515651 | 3 | STABLE_3_OF_3 | [6, 3, 7] | [8, 8, 5] | [3, 7, 3] | [11, 5, 9] | 0.5416666666666666 | DISSIPATING | False | 9.836062476870634 | 19.569944191865506 | FADING | NO_TRADE | FALLING | FALLING | 15 | 33.4228210858649 | MEDIUM |
| ATGL | 58.050 | CANDIDATE | NO_TRADE | IRREGULAR | 11.35190377120634 | [6.08, 18.17, 3.61] | [6.46, 11.36, 145.59] | 0.5348068156204089 | 2 | UNSTABLE | [4, 4, 4] | [9, 3, 9] | [11, 4, 4] | [9, 3, 2] | 0.8888888888888888 | DISSIPATING | False | 3.6088412157826433 | 19.49743516554152 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 21 | 31.890384715763037 | MEDIUM |
| PLAB | 57.705 | CANDIDATE | NO_TRADE | DOWNTREND | 13.450981588924638 | [5.12, 5.27, 13.45] | [20.26, 7.43, 15.94] | 0.3308430566166697 | 3 | STABLE_3_OF_3 | [13, 5, 10] | [19, 15, 18] | [6, 8, 11] | [24, 8, 24] | 0.4444444444444444 | DISSIPATING | False | 13.450981588924638 | 12.939354718959905 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 35.0 | 19.166663449907915 | MEDIUM |
| ECG | 57.571 | CANDIDATE | NO_TRADE | DOWNTREND | 23.012144681288472 | [13.86, 9.84, 23.01] | [6.42, 3.64, 21.53] | 2.156937540949749 | 3 | STABLE_3_OF_3 | [17, 3, 6] | [15, 3, 17] | [5, 4, 11] | [5, 3, 28] | 0.7 | STABLE_OR_MIXED | False | 23.012144681288472 | 10.67994988580606 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 33 | 24.58437900733869 | MEDIUM |
| KRUS | 57.565 | CANDIDATE | NO_TRADE | DOWNTREND | 26.965922079934902 | [20.31, 22.46, 11.47] | [26.43, 8.67, 15.35] | 1.323262287697805 | 3 | STABLE_3_OF_3 | [35, 23, 3] | [8, 20, 12] | [27, 9, 10] | [22, 5, 33] | 1.1856060606060606 | STABLE_OR_MIXED | False | 11.468230070278619 | 14.53817540689679 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 32 | 27.619397282714765 | HIGH |
| NYAX | 57.521 | CANDIDATE | NO_TRADE | STABLE_UPTREND | 7.6424422155821015 | [18.54, 14.84, 4.03] | [16.98, 5.29, 16.75] | 0.8862085258938412 | 2 | UNSTABLE | [16, 11, 5] | [5, 5, 22] | [17, 8, 3] | [4, 17, 14] | 1.3857142857142857 | STABLE_OR_MIXED | False | 4.026162289834967 | 10.951448303176404 | TOO_SMALL_UPSIDE | NO_TRADE | RISING | RISING | 27 | 16.835768245937125 | LOW |
| SMP | 57.492 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.083103898942907 | [2.91, 26.84, 2.73] | [7.53, 3.64, 12.21] | 0.38627950173654124 | 1 | UNSTABLE | [15, 27, 10] | [4, 3, 20] | [18, 24, 3] | [4, 16, 14] | 2.517857142857143 | DISSIPATING | False | 2.7312339569521393 | 7.538478715179516 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | FALLING | 34.5 | 12.212917219004149 | MEDIUM |
| STRZ | 57.349 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.868419607920643 | [7.46, 21.38, 9.87] | [11.7, 7.03, 23.4] | 0.8434828543681092 | 3 | STABLE_3_OF_3 | [6, 10, 5] | [13, 5, 16] | [16, 5, 8] | [16, 7, 5] | 0.8021978021978022 | STABLE_OR_MIXED | False | 9.868419607920643 | 14.452659077132765 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | FALLING | 55 | 27.400937576802434 | MEDIUM |

## Experimental recent-swing review shortlist (NOT BUY signals)
Count: 0 of 92 scored CANDIDATE names
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
    "observations": 325,
    "positive_net_pct": 36.61538461538461,
    "average_net_pct": -2.2656712109674326,
    "average_positive_pct": 3.8177950356540977,
    "average_nonpositive_pct": -5.779906567025505,
    "benchmark_pairs": 325,
    "average_excess_pct": -0.5801051568912114,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 1932,
    "positive_net_pct": 43.63354037267081,
    "average_net_pct": -1.14766359854893,
    "average_positive_pct": 6.256960787748757,
    "average_nonpositive_pct": -6.879618013286245,
    "benchmark_pairs": 1932,
    "average_excess_pct": 0.37036233386249157,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 221,
    "positive_net_pct": 40.27149321266968,
    "average_net_pct": -2.3619988762913158,
    "average_positive_pct": 5.115990249576852,
    "average_nonpositive_pct": -7.40397639297516,
    "benchmark_pairs": 221,
    "average_excess_pct": -0.7575405916971709,
    "worst_adverse_excursion_pct": -40.22770195885972
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 246,
    "positive_net_pct": 41.86991869918699,
    "average_net_pct": -2.911993456512757,
    "average_positive_pct": 5.9724932322123445,
    "average_nonpositive_pct": -9.31130904349657,
    "benchmark_pairs": 246,
    "average_excess_pct": -0.7409799873231354,
    "worst_adverse_excursion_pct": -95.51242232978043
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 1569,
    "positive_net_pct": 41.93753983428935,
    "average_net_pct": -1.5897996468686042,
    "average_positive_pct": 10.254344041827387,
    "average_nonpositive_pct": -10.144625714005766,
    "benchmark_pairs": 1569,
    "average_excess_pct": 0.8075136229242099,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 173,
    "positive_net_pct": 50.28901734104046,
    "average_net_pct": -0.11801743873389649,
    "average_positive_pct": 8.315569659103426,
    "average_nonpositive_pct": -8.649669502825144,
    "benchmark_pairs": 173,
    "average_excess_pct": 1.954281907856137,
    "worst_adverse_excursion_pct": -34.75783566737878
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "0-40",
    "observations": 138,
    "positive_net_pct": 45.65217391304348,
    "average_net_pct": -5.592801763703578,
    "average_positive_pct": 6.2995452368599265,
    "average_nonpositive_pct": -15.582373244176924,
    "benchmark_pairs": 138,
    "average_excess_pct": -1.3473980884289922,
    "worst_adverse_excursion_pct": -98.15217388688697
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "40-60",
    "observations": 802,
    "positive_net_pct": 41.5211970074813,
    "average_net_pct": -2.7866193532595758,
    "average_positive_pct": 14.510908503903657,
    "average_nonpositive_pct": -15.068232949070563,
    "benchmark_pairs": 802,
    "average_excess_pct": 1.5344601142351506,
    "worst_adverse_excursion_pct": -93.04037981042042
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "60-80",
    "observations": 100,
    "positive_net_pct": 42.0,
    "average_net_pct": -3.322524632618426,
    "average_positive_pct": 11.352796320717196,
    "average_nonpositive_pct": -13.94948118503388,
    "benchmark_pairs": 100,
    "average_excess_pct": 0.6282333439931785,
    "worst_adverse_excursion_pct": -47.09677302750536
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 30,
    "score_band": "0-40",
    "observations": 10,
    "positive_net_pct": 50.0,
    "average_net_pct": -6.100088774484737,
    "average_positive_pct": 3.0015188586896095,
    "average_nonpositive_pct": -15.201696407659085,
    "benchmark_pairs": 10,
    "average_excess_pct": 1.1817604711814007,
    "worst_adverse_excursion_pct": -32.879903750427175
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 30,
    "score_band": "40-60",
    "observations": 70,
    "positive_net_pct": 32.857142857142854,
    "average_net_pct": -5.960172819412953,
    "average_positive_pct": 17.0623060882589,
    "average_nonpositive_pct": -17.226492284869387,
    "benchmark_pairs": 70,
    "average_excess_pct": 1.3216764262531857,
    "worst_adverse_excursion_pct": -53.35731374420762
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 30,
    "score_band": "60-80",
    "observations": 11,
    "positive_net_pct": 27.272727272727273,
    "average_net_pct": -14.982898263539612,
    "average_positive_pct": 14.33361066890874,
    "average_nonpositive_pct": -25.976589113207748,
    "benchmark_pairs": 11,
    "average_excess_pct": -7.701049017873476,
    "worst_adverse_excursion_pct": -50.72463699259495
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
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
- IBO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- KAZR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- KNRX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- LXFR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SSTI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- ARI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- CLGN: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- PTLE: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- UTZ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- VABK: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- CODX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- INM: ValueError: EMPTY_PROVIDER_RESPONSE
- ISPC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- PARA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SPLIT_REQUIRES_DAILY_ACTION_AUDIT
- RDIB: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SCNI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SOS: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
