# OFTS daily research

Market session: 2026-11-20
Selected: 166; refreshed: 124; refresh errors: 47
Qualified prediction cohorts saved: 31; current coverage: 124/166
Outcome counts: {'CORPORATE_ACTION_REVIEW': 43, 'INELIGIBLE_DATA': 3265, 'MATURE': 6880, 'MISSING_SESSIONS': 12, 'PENDING': 11360}
Cycle fingerprints saved: 112/193
Signal states: BUY=0, SELL=13, NO_TRADE=180
Cycle ledger: pending entries=0; open positions=27; closed trades=38; SPY pairs=38
Cycle-speed report card: READY; closed forward trades=38; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 10.474052168680252-67.93392659658588; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 18, '40_TO_49_999': 37, '50_TO_59_999': 45, '60_TO_69_999': 12, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=108
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=86; REVIEW=26; INSUFFICIENT=73
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| MWH | 67.934 | CANDIDATE | NO_TRADE | INSUFFICIENT | 15.212715679159539 | [13.52, 15.21, 17.93] | [5.95, 9.76, 11.38] | 1.5594628841902478 | 3 | STABLE_3_OF_3 | [17, 3, 9] | [17, 9, 11] | [19, 5, 4] | [19, 5, 12] | 0.6174242424242424 | STABLE_OR_MIXED | False | 17.926114661922043 | 11.575993832825626 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 47.5 | 35.23344052246027 | HIGH |
| CACC | 67.013 | CANDIDATE | NO_TRADE | IRREGULAR | 15.289628474476945 | [5.0, 7.15, 15.29] | [7.2, 6.53, 7.07] | 1.0114146772919794 | 2 | WATCH_2_OF_3 | [8, 5, 7] | [13, 20, 27] | [9, 8, 4] | [8, 16, 31] | 0.425 | STABLE_OR_MIXED | False | 15.289628474476945 | 7.98313696866579 | WATCH | NO_TRADE | FALLING | FALLING | 41.0 | 15.528029835742508 | HIGH |
| JBS | 63.624 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.128208067290285 | [9.27, 5.13, 3.19] | [4.56, 7.91, 19.98] | 0.6482455212975712 | 2 | UNSTABLE | [13, 3, 5] | [6, 12, 37] | [19, 7, 4] | [18, 5, 36] | 0.4027777777777778 | DISSIPATING | False | 3.193278374977382 | 10.400954459348334 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 57.5 | 22.97762566772592 | HIGH |
| WRBY | 63.254 | CANDIDATE | NO_TRADE | IRREGULAR | 14.200592976461513 | [11.01, 41.9, 8.87] | [18.71, 12.65, 6.29] | 0.8703031911300206 | 3 | STABLE_3_OF_3 | [8, 11, 7] | [9, 3, 9] | [6, 13, 9] | [10, 6, 8] | 1.0069444444444444 | STABLE_OR_MIXED | False | 8.873453820565746 | 13.602505290606286 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 33.0 | 27.91928135796663 | HIGH |
| HLIT | 62.289 | CANDIDATE | SELL | DOWNTREND | 13.79629393336872 | [10.69, 7.46, 15.36] | [21.57, 3.58, 6.82] | 1.566279906172395 | 3 | STABLE_3_OF_3 | [9, 7, 14] | [8, 8, 29] | [11, 7, 9] | [9, 9, 25] | 1.0625 | STABLE_OR_MIXED | False | 15.359820483878561 | 11.599491465226908 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 45.5 | 17.93938839074336 | HIGH |
| CLSK | 61.622 | CANDIDATE | SELL | IRREGULAR | 5.175032981235916 | [13.99, 21.65, 5.18] | [19.97, 4.17, 10.42] | 1.3416207754739036 | 3 | STABLE_3_OF_3 | [4, 4, 2] | [7, 21, 5] | [5, 3, 3] | [3, 23, 6] | 0.5357142857142857 | STABLE_OR_MIXED | False | 5.175032981235916 | 12.757443827047748 | TOO_SMALL | NO_TRADE | MIXED | FALLING | 30.0 | 28.9776092510905 | MEDIUM |
| EEFT | 61.602 | CANDIDATE | NO_TRADE | STABLE_RANGE | 12.004174664675238 | [8.32, 7.26, 20.57] | [7.81, 5.34, 3.77] | 1.5595416603754826 | 3 | STABLE_3_OF_3 | [8, 33, 10] | [4, 7, 8] | [9, 25, 14] | [6, 7, 6] | 1.880952380952381 | DISSIPATING | False | 20.572790289193634 | 8.10235939732078 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 28 | 13.308085891713855 | HIGH |
| TLN | 61.511 | CANDIDATE | SELL | STABLE_RANGE | 11.490985450081748 | [6.39, 7.29, 22.28] | [10.91, 34.08, 6.38] | 0.6687327628073135 | 3 | STABLE_3_OF_3 | [12, 3, 7] | [18, 21, 4] | [11, 6, 3] | [19, 9, 17] | 0.3709150326797386 | DISSIPATING | False | 22.280017459847024 | 11.686034556152578 | CYCLE_TIMING | NO_TRADE | RISING | MIXED | 32.0 | 23.460024521868796 | HIGH |
| PWR | 61.354 | CANDIDATE | NO_TRADE | IRREGULAR | 20.23498138943196 | [17.32, 20.23, 19.42] | [23.5, 9.3, 7.94] | 2.0889449301000873 | 3 | STABLE_3_OF_3 | [17, 20, 6] | [8, 9, 18] | [11, 28, 9] | [8, 8, 14] | 1.6319444444444444 | DISSIPATING | False | 19.424037511694525 | 11.535072502193337 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 35 | 19.81219643427886 | HIGH |
| OBE | 60.588 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.994571511853363 | [4.06, 4.99, 7.38] | [7.27, 13.97, 18.18] | 0.357473074980304 | 1 | UNSTABLE | [4, 10, 5] | [5, 10, 26] | [17, 9, 4] | [14, 3, 21] | 0.5714285714285714 | DISSIPATING | False | 7.383282327462348 | 12.916508941597959 | TOO_SMALL | NO_TRADE | MIXED | MIXED | 25 | 19.84161399857889 | MEDIUM |
| SPGI | 60.317 | CANDIDATE | NO_TRADE | INSUFFICIENT | 14.272715050622754 | [7.88, 4.37, 24.7] | [6.24, 4.72, 4.3] | 1.6695164333270074 | 2 | WATCH_2_OF_3 | [11, 4, 43] | [8, 7, 13] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 24.70293218258719 | 7.606401588235964 | WATCH | NO_TRADE | MIXED | INSUFFICIENT | 35 | 12.362397606590037 | MEDIUM |
| TT | 60.015 | CANDIDATE | SELL | DOWNTREND | 8.258798834697112 | [3.07, 3.63, 8.26] | [9.92, 2.73, 13.36] | 0.3663484686261195 | 1 | UNSTABLE | [6, 4, 11] | [11, 11, 33] | [21, 6, 9] | [8, 15, 18] | 0.5727272727272728 | DISSIPATING | False | 8.258798834697112 | 6.997958907642477 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 44 | 13.113653636542994 | HIGH |
| TRNS | 59.502 | CANDIDATE | NO_TRADE | STABLE_RANGE | 9.145248611633328 | [9.97, 25.28, 9.15] | [13.37, 5.38, 7.42] | 1.3442016749303707 | 3 | STABLE_3_OF_3 | [6, 4, 3] | [17, 9, 12] | [4, 6, 4] | [15, 9, 14] | 0.30952380952380953 | STABLE_OR_MIXED | False | 9.145248611633328 | 8.536640204051357 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 34 | 17.870775968554845 | MEDIUM |
| ESNT | 59.409 | CANDIDATE | NO_TRADE | INSUFFICIENT | 8.309903114311389 | [6.74, 8.31, 3.71] | [6.23, 3.06, 9.81] | 1.082920604364391 | 2 | UNSTABLE | [8, 11, 3] | [20, 6, 24] | [8, 7, 12] | [10, 17, 21] | 0.43529411764705883 | STABLE_OR_MIXED | False | 3.7060436752457626 | 7.429954445529278 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 53 | 12.641914967787642 | HIGH |
| MESO | 58.890 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.364017811603918 | [5.0, 7.36, 27.61] | [9.25, 4.97, 10.48] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [13, 8, 6] | [5, 6, 11] | [14, 9, 4] | [6, 6, 10] | 1.4166666666666665 | DISSIPATING | False | 27.60586658826034 | 11.712845461470458 | WATCH | NO_TRADE | FALLING | MIXED | 16.0 | 19.704195329980422 | MEDIUM |
| LI | 58.463 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.544011309154186 | [9.92, 5.95, 13.6] | [4.71, 4.46, 3.23] | 2.221521569027974 | 3 | STABLE_3_OF_3 | [17, 5, 13] | [11, 4, 4] | [13, 8, 12] | [10, 6, 3] | 2.625 | DISSIPATING | False | 13.599275034578252 | 7.72053949442203 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 27.5 | 13.731341432933164 | MEDIUM |
| DXC | 58.013 | CANDIDATE | NO_TRADE | STABLE_RANGE | 15.46012038061787 | [12.68, 46.85, 11.1] | [4.81, 10.62, 10.68] | 1.1945535015094293 | 3 | STABLE_3_OF_3 | [13, 17, 11] | [8, 7, 6] | [14, 3, 22] | [3, 7, 9] | 1.9285714285714286 | DISSIPATING | False | 11.10305309356936 | 9.849532708585711 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 29 | 15.278696465763314 | MEDIUM |
| ECG | 57.778 | CANDIDATE | NO_TRADE | DOWNTREND | 23.012144681288472 | [13.86, 9.84, 23.01] | [6.42, 3.64, 21.53] | 2.156937540949749 | 3 | STABLE_3_OF_3 | [17, 3, 6] | [15, 3, 17] | [28, 5, 4] | [17, 5, 3] | 0.7 | STABLE_OR_MIXED | False | 23.012144681288472 | 10.676349017257728 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 33 | 25.592558307926748 | MEDIUM |
| PLAB | 57.671 | CANDIDATE | SELL | DOWNTREND | 13.087935012328856 | [5.12, 5.27, 13.45] | [20.26, 7.43, 15.94] | 0.3308430566166697 | 3 | STABLE_3_OF_3 | [13, 5, 10] | [19, 15, 18] | [24, 6, 8] | [12, 24, 8] | 0.6111111111111112 | DISSIPATING | False | 13.450981588924638 | 12.998387035976561 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 35.0 | 19.166663449907915 | MEDIUM |
| SMP | 57.652 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.241409028719824 | [2.91, 26.84, 2.73] | [7.53, 3.64, 12.21] | 0.38627950173654124 | 1 | UNSTABLE | [15, 27, 10] | [4, 3, 20] | [14, 18, 24] | [9, 4, 16] | 2.875 | DISSIPATING | True | 2.7312339569521393 | 7.621679573407872 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | FALLING | 34.5 | 12.212917219004149 | MEDIUM |
| NYAX | 57.540 | CANDIDATE | SELL | STABLE_UPTREND | 7.679244707215505 | [18.54, 14.84, 4.03] | [16.98, 5.29, 16.75] | 0.8862085258938412 | 2 | UNSTABLE | [16, 11, 5] | [5, 5, 22] | [14, 17, 8] | [4, 4, 17] | 2.85 | DISSIPATING | False | 4.026162289834967 | 10.429110638430732 | TOO_SMALL_UPSIDE | NO_TRADE | RISING | RISING | 27 | 16.835768245937125 | LOW |
| KRUS | 57.489 | CANDIDATE | NO_TRADE | DOWNTREND | 22.456254595313286 | [20.31, 22.46, 11.47] | [26.43, 8.67, 15.35] | 1.323262287697805 | 3 | STABLE_3_OF_3 | [35, 23, 3] | [8, 20, 12] | [33, 27, 9] | [13, 22, 5] | 1.9967948717948718 | DISSIPATING | False | 11.468230070278619 | 14.371299038664649 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 32 | 27.619397282714765 | HIGH |
| STRZ | 57.385 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.868419607920643 | [7.46, 21.38, 9.87] | [11.7, 7.03, 23.4] | 0.8434828543681092 | 3 | STABLE_3_OF_3 | [6, 10, 5] | [13, 5, 16] | [16, 5, 8] | [16, 7, 5] | 0.8021978021978022 | STABLE_OR_MIXED | False | 9.868419607920643 | 14.24961893825109 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | FALLING | 55 | 27.400937576802434 | MEDIUM |
| BBY | 57.365 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.4946674795365205 | [9.59, 3.54, 13.22] | [11.48, 18.32, 11.33] | 0.835089937173392 | 2 | WATCH_2_OF_3 | [6, 4, 7] | [15, 17, 23] | [8, 7, 4] | [10, 17, 26] | 0.38235294117647056 | STABLE_OR_MIXED | False | 13.220406593805833 | 8.99643927494022 | WATCH | NO_TRADE | MIXED | RISING | 30.5 | 11.484632375578263 | MEDIUM |
| CD | 57.097 | CANDIDATE | NO_TRADE | STABLE_RANGE | 9.836062476870634 | [17.83, 5.83, 9.84] | [84.29, 29.71, 32.16] | 0.3058556342515651 | 3 | STABLE_3_OF_3 | [6, 3, 7] | [8, 8, 5] | [9, 3, 7] | [4, 11, 5] | 1.075 | DISSIPATING | False | 9.836062476870634 | 19.774288242641784 | CYCLE_TIMING | NO_TRADE | FALLING | MIXED | 15.0 | 34.267245653870674 | MEDIUM |

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
    "observations": 309,
    "positive_net_pct": 37.86407766990291,
    "average_net_pct": -2.219334333931323,
    "average_positive_pct": 3.799932687224502,
    "average_nonpositive_pct": -5.887325174948156,
    "benchmark_pairs": 309,
    "average_excess_pct": -0.5697480040613411,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 1867,
    "positive_net_pct": 44.29566148901982,
    "average_net_pct": -1.042317240560729,
    "average_positive_pct": 6.3014623664275495,
    "average_nonpositive_pct": -6.88203429342543,
    "benchmark_pairs": 1867,
    "average_excess_pct": 0.4456841040355577,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 208,
    "positive_net_pct": 40.86538461538461,
    "average_net_pct": -2.3480171781999832,
    "average_positive_pct": 5.1010112288521805,
    "average_nonpositive_pct": -7.495719735918961,
    "benchmark_pairs": 208,
    "average_excess_pct": -0.7920567806817812,
    "worst_adverse_excursion_pct": -40.22770195885972
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 232,
    "positive_net_pct": 43.96551724137931,
    "average_net_pct": -2.624358991208217,
    "average_positive_pct": 5.963281721917654,
    "average_nonpositive_pct": -9.362354012276205,
    "benchmark_pairs": 232,
    "average_excess_pct": -0.5413529771184377,
    "worst_adverse_excursion_pct": -95.51242232978043
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 1489,
    "positive_net_pct": 43.38482202820685,
    "average_net_pct": -1.2014801340694197,
    "average_positive_pct": 10.374942007479323,
    "average_nonpositive_pct": -10.072617386074734,
    "benchmark_pairs": 1489,
    "average_excess_pct": 1.1296351797616986,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 166,
    "positive_net_pct": 50.602409638554214,
    "average_net_pct": 0.12181893596911617,
    "average_positive_pct": 8.287462024906155,
    "average_nonpositive_pct": -8.242986179527366,
    "benchmark_pairs": 166,
    "average_excess_pct": 2.128456453343614,
    "worst_adverse_excursion_pct": -32.33082603432881
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "0-40",
    "observations": 125,
    "positive_net_pct": 48.8,
    "average_net_pct": -4.968662866665674,
    "average_positive_pct": 6.401250751829763,
    "average_nonpositive_pct": -15.805611784294134,
    "benchmark_pairs": 125,
    "average_excess_pct": -0.9131146473452867,
    "worst_adverse_excursion_pct": -98.15217388688697
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "40-60",
    "observations": 728,
    "positive_net_pct": 42.582417582417584,
    "average_net_pct": -2.132727411940763,
    "average_positive_pct": 14.964132034026587,
    "average_nonpositive_pct": -14.812216474739504,
    "benchmark_pairs": 728,
    "average_excess_pct": 2.0104819313506073,
    "worst_adverse_excursion_pct": -93.04037981042042
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "60-80",
    "observations": 94,
    "positive_net_pct": 43.61702127659574,
    "average_net_pct": -2.7087138883837936,
    "average_positive_pct": 11.24270980667965,
    "average_nonpositive_pct": -13.501324671357404,
    "benchmark_pairs": 94,
    "average_excess_pct": 1.1067135182921624,
    "worst_adverse_excursion_pct": -47.09677302750536
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
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
- ITGR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
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
