# OFTS daily research

Market session: 2026-11-18
Selected: 158; refreshed: 125; refresh errors: 34
Qualified prediction cohorts saved: 29; current coverage: 125/158
Outcome counts: {'CORPORATE_ACTION_REVIEW': 37, 'INELIGIBLE_DATA': 2840, 'MATURE': 6067, 'MISSING_SESSIONS': 7, 'PENDING': 10984}
Cycle fingerprints saved: 121/187
Signal states: BUY=2, SELL=2, NO_TRADE=183
Cycle ledger: pending entries=2; open positions=28; closed trades=34; SPY pairs=34
Cycle-speed report card: READY; closed forward trades=34; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 9.280062252891744-68.2503810873324; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 18, '40_TO_49_999': 50, '50_TO_59_999': 41, '60_TO_69_999': 12, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=118
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=98; REVIEW=23; INSUFFICIENT=88
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| MWH | 68.250 | CANDIDATE | NO_TRADE | INSUFFICIENT | 11.152554385226521 | [11.38, 13.52, 15.21] | [18.33, 5.95, 9.76] | 1.385666278611575 | 3 | STABLE_3_OF_3 | [11, 17, 3] | [8, 17, 9] | [19, 5, 4] | [19, 5, 12] | 0.8194444444444445 | STABLE_OR_MIXED | False | 15.212715679159539 | 11.431672904891617 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 47.5 | 35.23344052246027 | HIGH |
| CACC | 65.847 | CANDIDATE | NO_TRADE | DOWNTREND | 15.289628474476945 | [9.17, 7.15, 15.29] | [3.85, 7.2, 6.53] | 1.4054024701331038 | 3 | STABLE_3_OF_3 | [35, 5, 7] | [9, 13, 20] | [31, 17, 4] | [21, 8, 16] | 0.8004807692307692 | STABLE_OR_MIXED | False | 15.289628474476945 | 8.650515681118401 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 42 | 16.02883648649655 | HIGH |
| LBTYB | 64.092 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.909092989834864 | [4.07, 5.65, 6.91] | [4.67, 5.37, 3.68] | 1.2089660041389128 | 2 | WATCH_2_OF_3 | [2, 4, 22] | [3, 7, 16] | [2, 21, 5] | [6, 18, 2] | 0.7023809523809523 | STABLE_OR_MIXED | False | 6.909092989834864 | 9.227690725673797 | WATCH | NO_TRADE | MIXED | MIXED | 26 | 14.742978057208127 | MEDIUM |
| S | 63.205 | CANDIDATE | NO_TRADE | IRREGULAR | 11.059718217721514 | [17.38, 19.14, 11.02] | [11.82, 20.84, 7.06] | 1.4709178542010226 | 3 | STABLE_3_OF_3 | [12, 14, 9] | [10, 12, 6] | [15, 14, 8] | [9, 8, 5] | 1.475 | STABLE_OR_MIXED | True | 11.017743239709121 | 11.367431776987782 | REVIEW | NO_TRADE | MIXED | RISING | 47 | 20.6446881325586 | HIGH |
| WRBY | 62.920 | CANDIDATE | NO_TRADE | INSUFFICIENT | 17.830949282487975 | [6.29, 11.01, 41.9] | [10.39, 18.71, 12.65] | 0.8703031911300206 | 3 | STABLE_3_OF_3 | [9, 8, 11] | [17, 9, 3] | [6, 13, 9] | [10, 6, 8] | 1.0625 | STABLE_OR_MIXED | False | 41.89759410691114 | 13.681322815106963 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | FALLING | 33 | 27.759537725403796 | HIGH |
| OBE | 62.718 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.994571511853363 | [4.06, 4.99, 7.38] | [7.27, 13.97, 18.18] | 0.357473074980304 | 1 | UNSTABLE | [4, 10, 5] | [5, 10, 26] | [17, 9, 4] | [14, 3, 21] | 0.5714285714285714 | DISSIPATING | False | 7.383282327462348 | 12.933036572311671 | TOO_SMALL | NO_TRADE | MIXED | MIXED | 26 | 21.37633118736948 | HIGH |
| PLAB | 61.872 | CANDIDATE | NO_TRADE | STABLE_RANGE | 13.087935012328856 | [5.12, 5.27, 13.45] | [20.26, 7.43, 15.94] | 0.3308430566166697 | 3 | STABLE_3_OF_3 | [13, 5, 10] | [19, 15, 18] | [24, 6, 8] | [12, 24, 8] | 0.6111111111111112 | DISSIPATING | False | 13.450981588924638 | 12.998387035976561 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | FALLING | 32 | 19.139999184949197 | HIGH |
| SPGI | 60.926 | CANDIDATE | NO_TRADE | INSUFFICIENT | 14.272715050622754 | [7.88, 4.37, 24.7] | [6.24, 4.72, 4.3] | 1.6695164333270074 | 2 | WATCH_2_OF_3 | [11, 4, 43] | [8, 7, 13] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 24.70293218258719 | 7.606401588235964 | WATCH | NO_TRADE | MIXED | INSUFFICIENT | 35 | 12.362397606590037 | MEDIUM |
| TDY | 60.711 | CANDIDATE | NO_TRADE | INSUFFICIENT | 12.134402813224042 | [4.53, 12.13, 10.04] | [8.94, 5.18, 9.5] | 1.1228368303155556 | 2 | WATCH_2_OF_3 | [41, 17, 9] | [9, 17, 10] | [29, 20, 21] | [9, 13, 11] | 1.8045454545454547 | DISSIPATING | False | 10.038536360954486 | 7.245056130560562 | WATCH | NO_TRADE | INSUFFICIENT | FALLING | 58 | 13.900054013498732 | MEDIUM |
| MIR | 60.646 | CANDIDATE | NO_TRADE | INSUFFICIENT | 13.718625199071877 | [17.71, 28.63, 13.72] | [5.44, 17.57, 7.22] | 2.453234001852276 | 3 | STABLE_3_OF_3 | [13, 17, 4] | [5, 15, 11] | [17, 9, 8] | [14, 10, 12] | 0.9659090909090909 | STABLE_OR_MIXED | False | 13.718625199071877 | 10.016863265553726 | CYCLE_TIMING | NO_TRADE | RISING | INSUFFICIENT | 29.0 | 17.569449678247494 | MEDIUM |
| SGML | 60.189 | CANDIDATE | NO_TRADE | DOWNTREND | 7.869478779465289 | [12.97, 7.87, 11.21] | [19.14, 18.3, 3.53] | 0.6129616139871417 | 3 | STABLE_3_OF_3 | [8, 6, 3] | [13, 11, 6] | [6, 7, 3] | [19, 10, 9] | 0.5727272727272728 | DISSIPATING | False | 11.214951688373453 | 15.717885875588312 | FADING | NO_TRADE | FALLING | FALLING | 24 | 25.88678330185843 | MEDIUM |
| ESNT | 59.517 | CANDIDATE | NO_TRADE | INSUFFICIENT | 8.309903114311389 | [9.81, 6.74, 8.31] | [5.74, 6.23, 3.06] | 1.4468196786663896 | 3 | STABLE_3_OF_3 | [24, 8, 11] | [8, 20, 6] | [8, 7, 12] | [10, 17, 21] | 0.9227941176470589 | STABLE_OR_MIXED | False | 8.309903114311389 | 7.617054651392599 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 53 | 12.641914967787642 | HIGH |
| MESO | 59.288 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.364017811603918 | [5.0, 7.36, 27.61] | [9.25, 4.97, 10.48] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [13, 8, 6] | [5, 6, 11] | [14, 9, 4] | [6, 6, 10] | 1.4166666666666665 | DISSIPATING | False | 27.60586658826034 | 11.555150088219005 | WATCH | NO_TRADE | FALLING | MIXED | 16.0 | 19.704195329980422 | MEDIUM |
| METCB | 59.221 | CANDIDATE | NO_TRADE | INSUFFICIENT | 17.857141716747872 | [6.24, 18.52, 11.68] | [7.19, 4.68, 6.15] | 1.90102632967061 | 3 | STABLE_3_OF_3 | [6, 13, 12] | [4, 11, 6] | [3, 13, 11] | [8, 11, 6] | 1.6875 | DISSIPATING | False | 11.684784210781718 | 11.423941066297132 | CYCLE_TIMING | NO_TRADE | FALLING | INSUFFICIENT | 53 | 41.58882283911626 | HIGH |
| ATGL | 58.323 | CANDIDATE | NO_TRADE | STABLE_RANGE | 11.35190377120634 | [6.08, 18.17, 3.61] | [6.46, 11.36, 145.59] | 0.5348068156204089 | 2 | UNSTABLE | [4, 4, 4] | [9, 3, 9] | [11, 4, 4] | [9, 3, 2] | 0.8888888888888888 | DISSIPATING | False | 3.6088412157826433 | 19.096268728078698 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 21 | 32.06849916938487 | MEDIUM |
| TT | 58.102 | CANDIDATE | NO_TRADE | STABLE_RANGE | 8.258798834697112 | [3.07, 3.63, 8.26] | [9.92, 2.73, 13.36] | 0.3663484686261195 | 1 | UNSTABLE | [6, 4, 11] | [11, 11, 33] | [21, 6, 9] | [8, 15, 18] | 0.5727272727272728 | DISSIPATING | False | 8.258798834697112 | 6.997958907642477 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | FALLING | 42.5 | 12.868832109870343 | HIGH |
| ECG | 57.910 | CANDIDATE | NO_TRADE | DOWNTREND | 23.012144681288472 | [13.86, 9.84, 23.01] | [6.42, 3.64, 21.53] | 2.156937540949749 | 3 | STABLE_3_OF_3 | [17, 3, 6] | [15, 3, 17] | [28, 5, 4] | [17, 5, 3] | 0.7 | STABLE_OR_MIXED | False | 23.012144681288472 | 10.603226357182294 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 33 | 25.592558307926748 | MEDIUM |
| XYL | 57.763 | CANDIDATE | NO_TRADE | IRREGULAR | 14.530204246917044 | [3.66, 7.31, 14.53] | [7.6, 5.44, 2.95] | 1.3421468304075173 | 2 | WATCH_2_OF_3 | [20, 12, 9] | [8, 10, 19] | [18, 4, 15] | [28, 6, 26] | 0.8884615384615384 | STABLE_OR_MIXED | False | 14.530204246917044 | 7.317661165296027 | WATCH | NO_TRADE | FALLING | FALLING | 54 | 15.167223318689327 | MEDIUM |
| CRDO | 57.464 | CANDIDATE | NO_TRADE | IRREGULAR | 25.564906828467194 | [17.92, 7.78, 25.89] | [40.56, 14.81, 7.41] | 1.2105510805826645 | 3 | STABLE_3_OF_3 | [5, 4, 6] | [14, 7, 11] | [5, 6, 3] | [6, 11, 13] | 0.45454545454545453 | STABLE_OR_MIXED | False | 25.888009754323036 | 17.44688959867088 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 27 | 33.70009678324473 | MEDIUM |
| STRZ | 57.382 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.868419607920643 | [7.46, 21.38, 9.87] | [11.7, 7.03, 23.4] | 0.8434828543681092 | 3 | STABLE_3_OF_3 | [6, 10, 5] | [13, 5, 16] | [16, 5, 8] | [16, 7, 5] | 0.8021978021978022 | STABLE_OR_MIXED | False | 9.868419607920643 | 14.093598584836856 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | FALLING | 55 | 27.400937576802434 | MEDIUM |
| CLSK | 57.338 | CANDIDATE | NO_TRADE | IRREGULAR | 5.175032981235916 | [13.99, 21.65, 5.18] | [19.97, 4.17, 10.42] | 1.3416207754739036 | 3 | STABLE_3_OF_3 | [4, 4, 2] | [7, 21, 5] | [5, 3, 3] | [3, 23, 6] | 0.5357142857142857 | STABLE_OR_MIXED | False | 5.175032981235916 | 12.725273050393232 | TOO_SMALL | NO_TRADE | MIXED | FALLING | 27 | 29.073334378324457 | MEDIUM |
| AKAM | 57.197 | CANDIDATE | BUY | DOWNTREND | 18.41982001904674 | [13.36, 6.0, 14.14] | [13.34, 5.28, 5.39] | 2.4808292663919276 | 3 | STABLE_3_OF_3 | [10, 12, 12] | [7, 10, 8] | [16, 7, 13] | [11, 7, 9] | 1.4722222222222223 | STABLE_OR_MIXED | False | 14.143262278384672 | 12.625845993401144 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 34 | 20.307858690410125 | MEDIUM |
| NYAX | 57.190 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.679244707215505 | [18.54, 3.19, 14.84] | [16.98, 5.29, 16.75] | 0.8862085258938412 | 2 | WATCH_2_OF_3 | [16, 6, 5] | [5, 5, 22] | [13, 4, 8] | [4, 17, 14] | 0.8857142857142857 | STABLE_OR_MIXED | False | 14.842899778193752 | 10.230204558244079 | WATCH | NO_TRADE | MIXED | RISING | 28.0 | 16.922769870358156 | MEDIUM |
| TLN | 57.164 | CANDIDATE | NO_TRADE | STABLE_RANGE | 11.490985450081748 | [6.39, 7.29, 22.28] | [10.91, 34.08, 6.38] | 0.6687327628073135 | 3 | STABLE_3_OF_3 | [12, 3, 7] | [18, 21, 4] | [11, 6, 3] | [19, 9, 17] | 0.3709150326797386 | DISSIPATING | False | 22.280017459847024 | 11.451601120608707 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 33 | 23.56044601857301 | MEDIUM |
| HLIT | 57.015 | CANDIDATE | NO_TRADE | STABLE_RANGE | 9.296026534869107 | [6.82, 10.69, 7.46] | [21.57, 3.58, 3.36] | 2.084348856940502 | 3 | STABLE_3_OF_3 | [18, 9, 7] | [8, 8, 11] | [11, 7, 9] | [9, 8, 17] | 1.0625 | STABLE_OR_MIXED | False | 7.462686425532894 | 10.999411954817631 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 46 | 18.52179327708091 | HIGH |

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
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "0-40",
    "observations": 282,
    "positive_net_pct": 40.0709219858156,
    "average_net_pct": -1.8412598404421423,
    "average_positive_pct": 3.92369372399251,
    "average_nonpositive_pct": -5.6959329338215285,
    "benchmark_pairs": 282,
    "average_excess_pct": -0.71731222397877,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 1719,
    "positive_net_pct": 47.294938917975564,
    "average_net_pct": -0.4341984286375879,
    "average_positive_pct": 6.376316764142072,
    "average_nonpositive_pct": -6.5456210022908445,
    "benchmark_pairs": 1719,
    "average_excess_pct": 0.5757232988894018,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 189,
    "positive_net_pct": 44.973544973544975,
    "average_net_pct": -1.4334933422078722,
    "average_positive_pct": 5.1010112288521805,
    "average_nonpositive_pct": -6.774194193555032,
    "benchmark_pairs": 189,
    "average_excess_pct": -0.45202275782823,
    "worst_adverse_excursion_pct": -40.22770195885972
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 211,
    "positive_net_pct": 46.91943127962085,
    "average_net_pct": -2.210670386551279,
    "average_positive_pct": 6.047503538343746,
    "average_nonpositive_pct": -9.510306266592414,
    "benchmark_pairs": 211,
    "average_excess_pct": -0.4077528979717326,
    "worst_adverse_excursion_pct": -95.51242232978043
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 1328,
    "positive_net_pct": 46.31024096385542,
    "average_net_pct": -0.3894854863207377,
    "average_positive_pct": 10.602789624268597,
    "average_nonpositive_pct": -9.870900904290487,
    "benchmark_pairs": 1328,
    "average_excess_pct": 1.6093116650198194,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 150,
    "positive_net_pct": 52.0,
    "average_net_pct": 0.37107607099556666,
    "average_positive_pct": 8.117868555851743,
    "average_nonpositive_pct": -8.021282454265293,
    "benchmark_pairs": 150,
    "average_excess_pct": 2.087743007175631,
    "worst_adverse_excursion_pct": -32.33082603432881
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "0-40",
    "observations": 105,
    "positive_net_pct": 51.42857142857143,
    "average_net_pct": -3.677250228025665,
    "average_positive_pct": 6.774640791664125,
    "average_nonpositive_pct": -14.743958366520735,
    "benchmark_pairs": 105,
    "average_excess_pct": -0.34422912757121416,
    "worst_adverse_excursion_pct": -98.15217388688697
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "40-60",
    "observations": 577,
    "positive_net_pct": 47.14038128249567,
    "average_net_pct": 0.013138103455687078,
    "average_positive_pct": 15.763134089075466,
    "average_nonpositive_pct": -14.032759955851116,
    "benchmark_pairs": 577,
    "average_excess_pct": 3.2090958966455956,
    "worst_adverse_excursion_pct": -89.14473627454025
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "60-80",
    "observations": 79,
    "positive_net_pct": 44.30379746835443,
    "average_net_pct": -1.9262457345305908,
    "average_positive_pct": 11.879309555528023,
    "average_nonpositive_pct": -12.907937442531763,
    "benchmark_pairs": 79,
    "average_excess_pct": 1.0998721622804073,
    "worst_adverse_excursion_pct": -47.09677302750536
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
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
