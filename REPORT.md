# OFTS daily research

Market session: 2026-11-19
Selected: 159; refreshed: 122; refresh errors: 41
Qualified prediction cohorts saved: 30; current coverage: 122/159
Outcome counts: {'CORPORATE_ACTION_REVIEW': 40, 'INELIGIBLE_DATA': 3035, 'MATURE': 6409, 'MISSING_SESSIONS': 9, 'PENDING': 11237}
Cycle fingerprints saved: 117/185
Signal states: BUY=1, SELL=12, NO_TRADE=172
Cycle ledger: pending entries=1; open positions=29; closed trades=35; SPY pairs=35
Cycle-speed report card: READY; closed forward trades=35; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 8.950692912157539-69.26211444649539; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 19, '40_TO_49_999': 43, '50_TO_59_999': 46, '60_TO_69_999': 9, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=114
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=85; REVIEW=32; INSUFFICIENT=76
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| CACC | 69.262 | CANDIDATE | SELL | IRREGULAR | 15.289628474476945 | [9.17, 7.15, 15.29] | [3.85, 7.2, 6.53] | 1.4054024701331038 | 3 | STABLE_3_OF_3 | [35, 5, 7] | [9, 13, 20] | [31, 17, 4] | [21, 8, 16] | 0.8004807692307692 | STABLE_OR_MIXED | False | 15.289628474476945 | 8.650515681118401 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 42.0 | 15.896230949151457 | HIGH |
| MWH | 68.323 | CANDIDATE | NO_TRADE | INSUFFICIENT | 11.152554385226521 | [11.38, 13.52, 15.21] | [18.33, 5.95, 9.76] | 1.385666278611575 | 3 | STABLE_3_OF_3 | [11, 17, 3] | [8, 17, 9] | [19, 5, 4] | [19, 5, 12] | 0.8194444444444445 | STABLE_OR_MIXED | False | 15.212715679159539 | 11.431672904891617 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 47.5 | 35.23344052246027 | HIGH |
| WRBY | 63.225 | CANDIDATE | SELL | IRREGULAR | 14.200592976461513 | [11.01, 41.9, 8.87] | [18.71, 12.65, 6.29] | 0.8703031911300206 | 3 | STABLE_3_OF_3 | [8, 11, 7] | [9, 3, 9] | [6, 13, 9] | [10, 6, 8] | 1.0069444444444444 | STABLE_OR_MIXED | False | 8.873453820565746 | 13.602505290606286 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 33.0 | 27.91928135796663 | HIGH |
| LBTYB | 63.092 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.909092989834864 | [4.07, 5.65, 6.91] | [4.67, 5.37, 3.68] | 1.2089660041389128 | 2 | WATCH_2_OF_3 | [2, 4, 22] | [3, 7, 16] | [2, 21, 5] | [6, 18, 2] | 0.7023809523809523 | STABLE_OR_MIXED | False | 6.909092989834864 | 9.485385965828954 | WATCH | NO_TRADE | MIXED | MIXED | 25 | 14.821865537105216 | MEDIUM |
| OBE | 62.746 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.994571511853363 | [4.06, 4.99, 7.38] | [7.27, 13.97, 18.18] | 0.357473074980304 | 1 | UNSTABLE | [4, 10, 5] | [5, 10, 26] | [17, 9, 4] | [14, 3, 21] | 0.5714285714285714 | DISSIPATING | False | 7.383282327462348 | 12.923151746336721 | TOO_SMALL | NO_TRADE | MIXED | MIXED | 26 | 21.37633118736948 | HIGH |
| PLAB | 61.886 | CANDIDATE | NO_TRADE | STABLE_RANGE | 13.087935012328856 | [5.12, 5.27, 13.45] | [20.26, 7.43, 15.94] | 0.3308430566166697 | 3 | STABLE_3_OF_3 | [13, 5, 10] | [19, 15, 18] | [24, 6, 8] | [12, 24, 8] | 0.6111111111111112 | DISSIPATING | False | 13.450981588924638 | 12.998387035976561 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | FALLING | 32 | 19.139999184949197 | HIGH |
| EEFT | 61.636 | CANDIDATE | SELL | STABLE_RANGE | 12.004174664675238 | [8.32, 7.26, 20.57] | [7.81, 5.34, 3.77] | 1.5595416603754826 | 3 | STABLE_3_OF_3 | [8, 33, 10] | [4, 7, 8] | [9, 25, 14] | [6, 7, 6] | 1.880952380952381 | DISSIPATING | False | 20.572790289193634 | 8.14792255070462 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 28 | 13.308085891713855 | HIGH |
| SPGI | 60.850 | CANDIDATE | NO_TRADE | INSUFFICIENT | 14.272715050622754 | [7.88, 4.37, 24.7] | [6.24, 4.72, 4.3] | 1.6695164333270074 | 2 | WATCH_2_OF_3 | [11, 4, 43] | [8, 7, 13] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 24.70293218258719 | 7.606401588235964 | WATCH | NO_TRADE | MIXED | INSUFFICIENT | 35 | 12.362397606590037 | MEDIUM |
| MIR | 60.657 | CANDIDATE | NO_TRADE | INSUFFICIENT | 13.718625199071877 | [17.71, 28.63, 13.72] | [5.44, 17.57, 7.22] | 2.453234001852276 | 3 | STABLE_3_OF_3 | [13, 17, 4] | [5, 15, 11] | [17, 9, 8] | [14, 10, 12] | 0.9659090909090909 | STABLE_OR_MIXED | False | 13.718625199071877 | 10.016863265553726 | CYCLE_TIMING | NO_TRADE | RISING | INSUFFICIENT | 29.0 | 17.569449678247494 | MEDIUM |
| DXC | 59.580 | CANDIDATE | SELL | STABLE_RANGE | 15.46012038061787 | [12.68, 46.85, 11.1] | [4.81, 10.62, 10.68] | 1.1945535015094293 | 3 | STABLE_3_OF_3 | [13, 17, 11] | [8, 7, 6] | [14, 3, 22] | [3, 7, 9] | 1.9285714285714286 | DISSIPATING | False | 11.10305309356936 | 9.885319325062806 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 29.0 | 15.364983182423341 | MEDIUM |
| ESNT | 59.433 | CANDIDATE | NO_TRADE | INSUFFICIENT | 8.309903114311389 | [6.74, 8.31, 3.71] | [6.23, 3.06, 9.81] | 1.082920604364391 | 2 | UNSTABLE | [8, 11, 3] | [20, 6, 24] | [8, 7, 12] | [10, 17, 21] | 0.43529411764705883 | STABLE_OR_MIXED | False | 3.7060436752457626 | 7.460230654516392 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 53 | 12.641914967787642 | HIGH |
| MESO | 59.294 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.364017811603918 | [5.0, 7.36, 27.61] | [9.25, 4.97, 10.48] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [13, 8, 6] | [5, 6, 11] | [14, 9, 4] | [6, 6, 10] | 1.4166666666666665 | DISSIPATING | False | 27.60586658826034 | 11.54996911426539 | WATCH | NO_TRADE | FALLING | MIXED | 16.0 | 19.704195329980422 | MEDIUM |
| METCB | 59.096 | CANDIDATE | NO_TRADE | INSUFFICIENT | 17.857141716747872 | [6.24, 18.52, 11.68] | [7.19, 4.68, 6.15] | 1.90102632967061 | 3 | STABLE_3_OF_3 | [6, 13, 12] | [4, 11, 6] | [3, 13, 11] | [8, 11, 6] | 1.6875 | DISSIPATING | False | 11.684784210781718 | 11.331022956850429 | CYCLE_TIMING | NO_TRADE | FALLING | INSUFFICIENT | 53 | 41.58882283911626 | HIGH |
| LI | 58.618 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.544011309154186 | [9.92, 5.95, 13.6] | [4.71, 4.46, 3.23] | 2.221521569027974 | 3 | STABLE_3_OF_3 | [17, 5, 13] | [11, 4, 4] | [13, 8, 12] | [10, 6, 3] | 2.625 | DISSIPATING | False | 13.599275034578252 | 7.72053949442203 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 27.5 | 13.731341432933164 | MEDIUM |
| ATGL | 58.470 | CANDIDATE | NO_TRADE | STABLE_RANGE | 11.35190377120634 | [6.08, 18.17, 3.61] | [6.46, 11.36, 145.59] | 0.5348068156204089 | 2 | UNSTABLE | [4, 4, 4] | [9, 3, 9] | [11, 4, 4] | [9, 3, 2] | 0.8888888888888888 | DISSIPATING | False | 3.6088412157826433 | 19.221629202064108 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 21 | 32.06849916938487 | MEDIUM |
| TT | 58.027 | CANDIDATE | NO_TRADE | STABLE_RANGE | 8.258798834697112 | [3.07, 3.63, 8.26] | [9.92, 2.73, 13.36] | 0.3663484686261195 | 1 | UNSTABLE | [6, 4, 11] | [11, 11, 33] | [21, 6, 9] | [8, 15, 18] | 0.5727272727272728 | DISSIPATING | False | 8.258798834697112 | 6.997958907642477 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | FALLING | 42.5 | 12.868832109870343 | HIGH |
| HLIT | 57.887 | CANDIDATE | NO_TRADE | STABLE_RANGE | 9.296026534869107 | [6.82, 10.69, 7.46] | [21.57, 3.58, 3.36] | 2.084348856940502 | 3 | STABLE_3_OF_3 | [18, 9, 7] | [8, 8, 11] | [11, 7, 9] | [9, 8, 17] | 1.0625 | STABLE_OR_MIXED | False | 7.462686425532894 | 10.980983684828491 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 46 | 18.52179327708091 | HIGH |
| TLN | 57.884 | CANDIDATE | NO_TRADE | STABLE_RANGE | 11.490985450081748 | [6.39, 7.29, 22.28] | [10.91, 34.08, 6.38] | 0.6687327628073135 | 3 | STABLE_3_OF_3 | [12, 3, 7] | [18, 21, 4] | [11, 6, 3] | [19, 9, 17] | 0.3709150326797386 | DISSIPATING | False | 22.280017459847024 | 11.58604605181013 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 33 | 23.56044601857301 | MEDIUM |
| ECG | 57.847 | CANDIDATE | NO_TRADE | DOWNTREND | 23.012144681288472 | [13.86, 9.84, 23.01] | [6.42, 3.64, 21.53] | 2.156937540949749 | 3 | STABLE_3_OF_3 | [17, 3, 6] | [15, 3, 17] | [28, 5, 4] | [17, 5, 3] | 0.7 | STABLE_OR_MIXED | False | 23.012144681288472 | 10.58725910100091 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 33 | 25.592558307926748 | MEDIUM |
| XYL | 57.684 | CANDIDATE | NO_TRADE | IRREGULAR | 14.530204246917044 | [3.66, 7.31, 14.53] | [7.6, 5.44, 2.95] | 1.3421468304075173 | 2 | WATCH_2_OF_3 | [20, 12, 9] | [8, 10, 19] | [18, 4, 15] | [28, 6, 26] | 0.8884615384615384 | STABLE_OR_MIXED | False | 14.530204246917044 | 7.317661165296027 | WATCH | NO_TRADE | FALLING | FALLING | 54 | 15.167223318689327 | MEDIUM |
| STRZ | 57.453 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.868419607920643 | [7.46, 21.38, 9.87] | [11.7, 7.03, 23.4] | 0.8434828543681092 | 3 | STABLE_3_OF_3 | [6, 10, 5] | [13, 5, 16] | [16, 5, 8] | [16, 7, 5] | 0.8021978021978022 | STABLE_OR_MIXED | False | 9.868419607920643 | 14.24961893825109 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | FALLING | 55 | 27.400937576802434 | MEDIUM |
| CLSK | 57.414 | CANDIDATE | NO_TRADE | IRREGULAR | 5.175032981235916 | [13.99, 21.65, 5.18] | [19.97, 4.17, 10.42] | 1.3416207754739036 | 3 | STABLE_3_OF_3 | [4, 4, 2] | [7, 21, 5] | [5, 3, 3] | [3, 23, 6] | 0.5357142857142857 | STABLE_OR_MIXED | False | 5.175032981235916 | 12.664851776902733 | TOO_SMALL | NO_TRADE | MIXED | FALLING | 27 | 29.073334378324457 | MEDIUM |
| NYAX | 57.270 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.679244707215505 | [3.19, 14.84, 4.03] | [5.29, 16.75, 18.54] | 0.24038559858269248 | 1 | UNSTABLE | [6, 5, 5] | [5, 22, 16] | [13, 4, 8] | [4, 17, 14] | 0.4419642857142857 | DISSIPATING | False | 4.026162289834967 | 9.923594238894578 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | RISING | 28.0 | 16.922769870358156 | MEDIUM |
| CD | 57.100 | CANDIDATE | NO_TRADE | STABLE_RANGE | 9.836062476870634 | [17.83, 5.83, 9.84] | [84.29, 29.71, 32.16] | 0.3058556342515651 | 3 | STABLE_3_OF_3 | [6, 3, 7] | [8, 8, 5] | [9, 3, 7] | [4, 11, 5] | 1.075 | DISSIPATING | False | 9.836062476870634 | 19.776690643202627 | CYCLE_TIMING | NO_TRADE | FALLING | MIXED | 15.0 | 34.267245653870674 | MEDIUM |
| BFAM | 56.791 | CANDIDATE | NO_TRADE | INSUFFICIENT | 10.05678951147475 | [11.66, 10.06, 5.6] | [6.43, 6.86, 5.1] | 1.5639209490413801 | 3 | STABLE_3_OF_3 | [17, 6, 7] | [22, 12, 5] | [7, 15, 9] | [18, 17, 7] | 0.5563725490196079 | STABLE_OR_MIXED | False | 5.597294230442529 | 9.778588055234788 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 65.5 | 18.3680156066923 | MEDIUM |

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
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "0-40",
    "observations": 295,
    "positive_net_pct": 39.32203389830509,
    "average_net_pct": -2.068931292322535,
    "average_positive_pct": 3.8310007344306656,
    "average_nonpositive_pct": -5.89235092977154,
    "benchmark_pairs": 295,
    "average_excess_pct": -0.7294345189351559,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 1797,
    "positive_net_pct": 45.85420144685587,
    "average_net_pct": -0.7253428450116326,
    "average_positive_pct": 6.321322700012056,
    "average_nonpositive_pct": -6.692919832780905,
    "benchmark_pairs": 1797,
    "average_excess_pct": 0.5018387751656246,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 197,
    "positive_net_pct": 43.14720812182741,
    "average_net_pct": -1.8339338674326704,
    "average_positive_pct": 5.1010112288521805,
    "average_nonpositive_pct": -7.097061842291711,
    "benchmark_pairs": 197,
    "average_excess_pct": -0.6480456252328936,
    "worst_adverse_excursion_pct": -40.22770195885972
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 222,
    "positive_net_pct": 45.04504504504504,
    "average_net_pct": -2.5458112921742853,
    "average_positive_pct": 6.049840909240611,
    "average_nonpositive_pct": -9.591427850711083,
    "benchmark_pairs": 222,
    "average_excess_pct": -0.6945360694739956,
    "worst_adverse_excursion_pct": -95.51242232978043
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 1406,
    "positive_net_pct": 45.59032716927454,
    "average_net_pct": -0.6033120631126253,
    "average_positive_pct": 10.427883805298194,
    "average_nonpositive_pct": -9.846444810369261,
    "benchmark_pairs": 1406,
    "average_excess_pct": 1.4387605164825445,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 159,
    "positive_net_pct": 51.57232704402516,
    "average_net_pct": 0.31351481757247224,
    "average_positive_pct": 8.216657240285944,
    "average_nonpositive_pct": -8.102818671550969,
    "benchmark_pairs": 159,
    "average_excess_pct": 2.09030614338135,
    "worst_adverse_excursion_pct": -32.33082603432881
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "0-40",
    "observations": 115,
    "positive_net_pct": 50.43478260869565,
    "average_net_pct": -4.647972992182633,
    "average_positive_pct": 6.57211934945574,
    "average_nonpositive_pct": -16.064909059112907,
    "benchmark_pairs": 115,
    "average_excess_pct": -1.0835461513856302,
    "worst_adverse_excursion_pct": -98.15217388688697
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "40-60",
    "observations": 656,
    "positive_net_pct": 44.207317073170735,
    "average_net_pct": -1.1223129763551098,
    "average_positive_pct": 15.24797933758678,
    "average_nonpositive_pct": -14.093309618549489,
    "benchmark_pairs": 656,
    "average_excess_pct": 2.4106267015529506,
    "worst_adverse_excursion_pct": -93.04037981042042
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "60-80",
    "observations": 86,
    "positive_net_pct": 45.348837209302324,
    "average_net_pct": -2.076666246592022,
    "average_positive_pct": 11.378728587888043,
    "average_nonpositive_pct": -13.241781109245697,
    "benchmark_pairs": 86,
    "average_excess_pct": 1.1910386795571124,
    "worst_adverse_excursion_pct": -47.09677302750536
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
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
