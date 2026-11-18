# OFTS daily research

Market session: 2026-11-17
Selected: 157; refreshed: 126; refresh errors: 33
Qualified prediction cohorts saved: 28; current coverage: 126/157
Outcome counts: {'CORPORATE_ACTION_REVIEW': 34, 'INELIGIBLE_DATA': 2630, 'MATURE': 5718, 'MISSING_SESSIONS': 5, 'PENDING': 10758}
Cycle fingerprints saved: 136/191
Signal states: BUY=0, SELL=13, NO_TRADE=178
Cycle ledger: pending entries=0; open positions=33; closed trades=29; SPY pairs=29
Cycle-speed report card: READY; closed forward trades=29; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 12.969752731266423-68.28982991323286; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 18, '40_TO_49_999': 55, '50_TO_59_999': 52, '60_TO_69_999': 11, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=1; viability NO_TRADE=132
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=104; REVIEW=32; INSUFFICIENT=91
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| MWH | 68.290 | CANDIDATE | NO_TRADE | INSUFFICIENT | 11.152554385226521 | [11.38, 13.52, 15.21] | [18.33, 5.95, 9.76] | 1.385666278611575 | 3 | STABLE_3_OF_3 | [11, 17, 3] | [8, 17, 9] | [19, 5, 4] | [19, 5, 12] | 0.8194444444444445 | STABLE_OR_MIXED | False | 15.212715679159539 | 11.431672904891617 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 47.5 | 35.23344052246027 | HIGH |
| LBTYB | 64.317 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.909092989834864 | [4.07, 5.65, 6.91] | [4.67, 5.37, 3.68] | 1.2089660041389128 | 2 | WATCH_2_OF_3 | [2, 4, 22] | [3, 7, 16] | [2, 21, 5] | [6, 18, 2] | 0.7023809523809523 | STABLE_OR_MIXED | False | 6.909092989834864 | 9.227690725673797 | WATCH | NO_TRADE | MIXED | MIXED | 26 | 14.742978057208127 | MEDIUM |
| S | 63.358 | CANDIDATE | NO_TRADE | IRREGULAR | 16.686111088855004 | [17.38, 19.14, 11.02] | [11.82, 20.84, 7.06] | 1.4709178542010226 | 3 | STABLE_3_OF_3 | [12, 14, 9] | [10, 12, 6] | [5, 15, 14] | [23, 9, 8] | 1.3777777777777778 | STABLE_OR_MIXED | False | 11.017743239709121 | 11.373842476139162 | CYCLE_TIMING | NO_TRADE | MIXED | RISING | 47 | 20.6446881325586 | HIGH |
| AKAM | 63.188 | CANDIDATE | NO_TRADE | IRREGULAR | 18.41982001904674 | [13.36, 6.0, 14.14] | [13.34, 5.28, 5.39] | 2.4808292663919276 | 3 | STABLE_3_OF_3 | [10, 12, 12] | [7, 10, 8] | [16, 7, 13] | [11, 7, 9] | 1.4722222222222223 | STABLE_OR_MIXED | False | 14.143262278384672 | 12.625845993401144 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 29.5 | 17.4508464841565 | HIGH |
| WRBY | 63.001 | CANDIDATE | NO_TRADE | INSUFFICIENT | 17.830949282487975 | [6.29, 11.01, 41.9] | [10.39, 18.71, 12.65] | 0.8703031911300206 | 3 | STABLE_3_OF_3 | [9, 8, 11] | [17, 9, 3] | [8, 6, 13] | [17, 10, 6] | 0.9 | STABLE_OR_MIXED | False | 41.89759410691114 | 13.735333179368437 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | FALLING | 33 | 27.759537725403796 | HIGH |
| DXC | 62.373 | CANDIDATE | NO_TRADE | STABLE_RANGE | 15.46012038061787 | [12.68, 46.85, 11.1] | [4.87, 12.32, 10.68] | 1.1868595755041154 | 3 | STABLE_3_OF_3 | [13, 17, 11] | [11, 15, 6] | [14, 3, 22] | [21, 3, 16] | 1.0284090909090908 | STABLE_OR_MIXED | False | 11.10305309356936 | 10.521827608711108 | CYCLE_TIMING | NO_TRADE | RISING | MIXED | 31 | 15.51175056999825 | HIGH |
| CACC | 61.494 | CANDIDATE | NO_TRADE | DOWNTREND | 15.289628474476945 | [9.17, 7.15, 15.29] | [3.85, 7.2, 6.53] | 1.4054024701331038 | 3 | STABLE_3_OF_3 | [35, 5, 7] | [9, 13, 20] | [31, 17, 4] | [21, 8, 16] | 0.8004807692307692 | STABLE_OR_MIXED | False | 15.289628474476945 | 9.504116450686253 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 42 | 16.10968422328472 | HIGH |
| SPGI | 60.878 | CANDIDATE | SELL | INSUFFICIENT | 14.272715050622754 | [7.88, 4.37, 24.7] | [6.24, 4.72, 4.3] | 1.6695164333270074 | 2 | WATCH_2_OF_3 | [11, 4, 43] | [8, 7, 13] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 24.70293218258719 | 7.608237653408694 | WATCH | NO_TRADE | MIXED | INSUFFICIENT | 35 | 12.362397606590037 | MEDIUM |
| SKY | 60.809 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.459516171185919 | [5.32, 28.04, 5.46] | [20.98, 8.67, 3.09] | 0.6295002503869188 | 3 | STABLE_3_OF_3 | [9, 14, 3] | [12, 27, 8] | [15, 3, 14] | [6, 28, 9] | 1.1527777777777777 | DISSIPATING | False | 5.459516171185919 | 9.313626647729087 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | MIXED | 39 | 20.609552618625955 | MEDIUM |
| TDY | 60.785 | CANDIDATE | NO_TRADE | INSUFFICIENT | 12.134402813224042 | [4.53, 12.13, 10.04] | [8.94, 5.18, 9.5] | 1.1228368303155556 | 2 | WATCH_2_OF_3 | [41, 17, 9] | [9, 17, 10] | [29, 20, 21] | [9, 13, 11] | 1.8045454545454547 | DISSIPATING | False | 10.038536360954486 | 7.245056130560562 | WATCH | NO_TRADE | INSUFFICIENT | FALLING | 58 | 13.900054013498732 | MEDIUM |
| SGML | 60.191 | CANDIDATE | NO_TRADE | DOWNTREND | 7.869478779465289 | [12.97, 7.87, 11.21] | [19.14, 18.3, 3.53] | 0.6129616139871417 | 3 | STABLE_3_OF_3 | [8, 6, 3] | [13, 11, 6] | [6, 7, 3] | [19, 10, 9] | 0.5727272727272728 | DISSIPATING | False | 11.214951688373453 | 15.717885875588312 | FADING | NO_TRADE | FALLING | FALLING | 24 | 25.88678330185843 | MEDIUM |
| TT | 59.984 | CANDIDATE | NO_TRADE | STABLE_RANGE | 8.258798834697112 | [3.07, 3.63, 8.26] | [9.92, 2.73, 13.36] | 0.3663484686261195 | 1 | UNSTABLE | [6, 4, 11] | [11, 11, 33] | [21, 6, 9] | [8, 15, 18] | 0.5727272727272728 | DISSIPATING | False | 8.258798834697112 | 6.901059251412342 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | FALLING | 45.0 | 13.358475163215644 | HIGH |
| ESNT | 59.494 | CANDIDATE | NO_TRADE | INSUFFICIENT | 8.309903114311389 | [9.81, 6.74, 8.31] | [5.74, 6.23, 3.06] | 1.4468196786663896 | 3 | STABLE_3_OF_3 | [24, 8, 11] | [8, 20, 6] | [8, 7, 12] | [10, 17, 21] | 0.9227941176470589 | STABLE_OR_MIXED | False | 8.309903114311389 | 7.668946271433978 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 53 | 12.641914967787642 | HIGH |
| METCB | 59.293 | CANDIDATE | NO_TRADE | INSUFFICIENT | 17.857141716747872 | [6.24, 18.52, 11.68] | [7.19, 4.68, 6.15] | 1.90102632967061 | 3 | STABLE_3_OF_3 | [6, 13, 12] | [4, 11, 6] | [3, 13, 11] | [8, 11, 6] | 1.6875 | DISSIPATING | False | 11.684784210781718 | 11.472091910667167 | CYCLE_TIMING | NO_TRADE | FALLING | INSUFFICIENT | 53 | 41.58882283911626 | HIGH |
| OBE | 59.083 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.994571511853363 | [4.06, 4.99, 7.38] | [7.27, 13.97, 18.18] | 0.357473074980304 | 1 | UNSTABLE | [4, 10, 5] | [5, 10, 26] | [17, 9, 4] | [14, 3, 21] | 0.5714285714285714 | DISSIPATING | False | 7.383282327462348 | 11.991142893803291 | TOO_SMALL | NO_TRADE | MIXED | MIXED | 25 | 19.84161399857889 | MEDIUM |
| NYAX | 58.748 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.842953829227538 | [18.54, 3.19, 14.84] | [5.29, 2.94, 16.75] | 2.8064066971878407 | 2 | WATCH_2_OF_3 | [16, 6, 5] | [5, 12, 10] | [14, 13, 4] | [4, 12, 5] | 1.6 | DISSIPATING | False | 14.842899778193752 | 9.703880559534518 | WATCH | NO_TRADE | MIXED | RISING | 24 | 16.651655201817416 | MEDIUM |
| HLIT | 58.528 | CANDIDATE | NO_TRADE | STABLE_RANGE | 9.296026534869107 | [6.82, 10.69, 7.46] | [3.58, 3.36, 3.29] | 2.2215823222141275 | 3 | STABLE_3_OF_3 | [16, 9, 7] | [8, 11, 2] | [11, 7, 9] | [8, 6, 11] | 1.125 | STABLE_OR_MIXED | False | 7.462686425532894 | 10.36946607545884 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 46 | 18.52179327708091 | HIGH |
| ATGL | 58.364 | CANDIDATE | NO_TRADE | STABLE_RANGE | 14.583338714307992 | [145.59, 6.08, 18.17] | [4.02, 6.46, 11.36] | 2.8133257639351634 | 3 | STABLE_3_OF_3 | [9, 4, 4] | [4, 9, 3] | [11, 4, 4] | [9, 3, 2] | 1.1666666666666665 | STABLE_OR_MIXED | False | 18.17072933873267 | 19.470268804307672 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 21 | 32.06849916938487 | MEDIUM |
| ECG | 57.911 | CANDIDATE | NO_TRADE | DOWNTREND | 23.012144681288472 | [13.86, 9.84, 23.01] | [6.42, 3.64, 21.53] | 2.156937540949749 | 3 | STABLE_3_OF_3 | [17, 3, 6] | [15, 3, 17] | [28, 5, 4] | [17, 5, 3] | 0.7 | STABLE_OR_MIXED | False | 23.012144681288472 | 10.628204235166523 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 33 | 25.592558307926748 | MEDIUM |
| CRDO | 57.416 | CANDIDATE | NO_TRADE | IRREGULAR | 25.564906828467194 | [17.92, 7.78, 25.89] | [40.56, 14.81, 7.41] | 1.2105510805826645 | 3 | STABLE_3_OF_3 | [5, 4, 6] | [14, 7, 11] | [5, 6, 3] | [6, 11, 13] | 0.45454545454545453 | STABLE_OR_MIXED | False | 25.888009754323036 | 17.483120844356392 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 27 | 33.70009678324473 | MEDIUM |
| STRZ | 57.411 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.868419607920643 | [7.46, 21.38, 9.87] | [11.7, 7.03, 23.4] | 0.8434828543681092 | 3 | STABLE_3_OF_3 | [6, 10, 5] | [13, 5, 16] | [16, 5, 8] | [16, 7, 5] | 0.8021978021978022 | STABLE_OR_MIXED | False | 9.868419607920643 | 14.041965922724431 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | FALLING | 55 | 27.400937576802434 | MEDIUM |
| MESO | 57.247 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.364017811603918 | [5.0, 7.36, 27.61] | [9.25, 4.97, 10.48] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [13, 8, 6] | [5, 6, 11] | [14, 9, 4] | [6, 6, 10] | 1.4166666666666665 | DISSIPATING | False | 27.60586658826034 | 11.58064295250315 | WATCH | NO_TRADE | FALLING | MIXED | 17.0 | 20.062944005361583 | MEDIUM |
| TLN | 57.179 | CANDIDATE | NO_TRADE | STABLE_RANGE | 11.490985450081748 | [6.39, 7.29, 22.28] | [10.91, 34.08, 6.38] | 0.6687327628073135 | 3 | STABLE_3_OF_3 | [12, 3, 7] | [18, 21, 4] | [11, 6, 3] | [19, 9, 17] | 0.3709150326797386 | DISSIPATING | False | 22.280017459847024 | 11.483204270179687 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 33 | 23.56044601857301 | MEDIUM |
| BFAM | 56.944 | CANDIDATE | NO_TRADE | INSUFFICIENT | 10.05678951147475 | [11.66, 10.06, 5.6] | [6.43, 6.86, 5.1] | 1.5639209490413801 | 3 | STABLE_3_OF_3 | [17, 6, 7] | [22, 12, 5] | [7, 15, 9] | [18, 17, 7] | 0.5563725490196079 | STABLE_OR_MIXED | False | 5.597294230442529 | 9.816052050618127 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 65.5 | 18.3680156066923 | MEDIUM |
| CD | 56.835 | CANDIDATE | NO_TRADE | STABLE_RANGE | 17.83216815279531 | [32.16, 17.83, 5.83] | [52.34, 84.29, 29.71] | 0.3407218358652037 | 3 | STABLE_3_OF_3 | [5, 6, 3] | [4, 8, 8] | [5, 9, 3] | [4, 4, 11] | 0.9375 | DISSIPATING | False | 5.825237055190802 | 19.576822649892573 | CYCLE_TIMING | NO_TRADE | FALLING | MIXED | 15.0 | 34.267245653870674 | MEDIUM |

## Experimental recent-swing review shortlist (NOT BUY signals)
Count: 1 of 118 scored CANDIDATE names
| Symbol | Quality score | Last 3 swings % | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Historical avg % |
|---|---:|---:|---|---|---:|---:|---|---|---|---|---:|---:|
| RBLX | 51.483 | 21.277767381768896 | [20.4, 14.58, 22.69] | [10.07, 36.55, 8.05] | 2.025012312234286 | 3 | [15, 11, 11] | [12, 13, 5] | [9, 11, 13] | [8, 10, 14] | 1.0083333333333333 | 13.796693468736086 |

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
    "observations": 263,
    "positive_net_pct": 41.82509505703422,
    "average_net_pct": -1.7670394596252537,
    "average_positive_pct": 3.930437504102034,
    "average_nonpositive_pct": -5.863264727664483,
    "benchmark_pairs": 263,
    "average_excess_pct": -0.8041929203369662,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 1644,
    "positive_net_pct": 48.661800486618006,
    "average_net_pct": -0.24657837004309657,
    "average_positive_pct": 6.398793846793626,
    "average_nonpositive_pct": -6.5455093812627245,
    "benchmark_pairs": 1644,
    "average_excess_pct": 0.6564088703852603,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 182,
    "positive_net_pct": 46.7032967032967,
    "average_net_pct": -1.0197783208035296,
    "average_positive_pct": 5.1010112288521805,
    "average_nonpositive_pct": -6.383356792151318,
    "benchmark_pairs": 182,
    "average_excess_pct": -0.1295560095142484,
    "worst_adverse_excursion_pct": -25.57142802647182
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 198,
    "positive_net_pct": 47.474747474747474,
    "average_net_pct": -2.105645858813948,
    "average_positive_pct": 6.150186069132456,
    "average_nonpositive_pct": -9.567647793688577,
    "benchmark_pairs": 198,
    "average_excess_pct": -0.5000069125784191,
    "worst_adverse_excursion_pct": -95.51242232978043
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 1256,
    "positive_net_pct": 48.00955414012739,
    "average_net_pct": 0.05399181197527975,
    "average_positive_pct": 10.64505289744845,
    "average_nonpositive_pct": -9.726115132190593,
    "benchmark_pairs": 1256,
    "average_excess_pct": 1.8917735581644401,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 144,
    "positive_net_pct": 52.77777777777778,
    "average_net_pct": 0.6163656606910352,
    "average_positive_pct": 8.117118905310756,
    "average_nonpositive_pct": -7.766829142119243,
    "benchmark_pairs": 144,
    "average_excess_pct": 2.204242825828443,
    "worst_adverse_excursion_pct": -32.33082603432881
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "0-40",
    "observations": 88,
    "positive_net_pct": 54.54545454545455,
    "average_net_pct": -1.1236177339635571,
    "average_positive_pct": 7.316641912039345,
    "average_nonpositive_pct": -11.251929309167041,
    "benchmark_pairs": 88,
    "average_excess_pct": 1.902895474708948,
    "worst_adverse_excursion_pct": -69.10112242914782
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "40-60",
    "observations": 507,
    "positive_net_pct": 46.74556213017752,
    "average_net_pct": 0.287410216026664,
    "average_positive_pct": 16.624278355635585,
    "average_nonpositive_pct": -14.052729595407818,
    "benchmark_pairs": 507,
    "average_excess_pct": 3.2453828660420054,
    "worst_adverse_excursion_pct": -89.14473627454025
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "60-80",
    "observations": 71,
    "positive_net_pct": 43.66197183098591,
    "average_net_pct": -2.0140530743278804,
    "average_positive_pct": 11.618741574108826,
    "average_nonpositive_pct": -12.579468926866333,
    "benchmark_pairs": 71,
    "average_excess_pct": 0.7987090714392082,
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
