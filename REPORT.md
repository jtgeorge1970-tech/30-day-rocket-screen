# OFTS daily research

Market session: 2026-11-13
Selected: 154; refreshed: 125; refresh errors: 33
Qualified prediction cohorts saved: 26; current coverage: 125/154
Outcome counts: {'CORPORATE_ACTION_REVIEW': 31, 'INELIGIBLE_DATA': 2280, 'MATURE': 5010, 'MISSING_SESSIONS': 4, 'PENDING': 10260}
Cycle fingerprints saved: 129/188
Signal states: BUY=1, SELL=4, NO_TRADE=183
Cycle ledger: pending entries=1; open positions=38; closed trades=23; SPY pairs=23
Cycle-speed report card: READY; closed forward trades=23; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 12.697831935764821-68.34102062980467; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 20, '40_TO_49_999': 50, '50_TO_59_999': 47, '60_TO_69_999': 12, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=128
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=106; REVIEW=23; INSUFFICIENT=87
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| MWH | 68.341 | CANDIDATE | NO_TRADE | INSUFFICIENT | 11.152554385226521 | [11.38, 13.52, 15.21] | [18.33, 5.95, 9.76] | 1.385666278611575 | 3 | STABLE_3_OF_3 | [11, 17, 3] | [8, 17, 9] | [19, 5, 4] | [19, 5, 12] | 0.8194444444444445 | STABLE_OR_MIXED | False | 15.212715679159539 | 11.431672904891617 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 47.5 | 35.23344052246027 | HIGH |
| MUR | 64.793 | CANDIDATE | NO_TRADE | IRREGULAR | 19.033557456611796 | [5.65, 6.79, 19.03] | [10.73, 8.87, 10.87] | 0.6324355165797887 | 3 | STABLE_3_OF_3 | [7, 7, 14] | [7, 9, 8] | [5, 6, 23] | [7, 8, 11] | 0.8125 | DISSIPATING | False | 19.033557456611796 | 8.336943948801956 | CYCLE_TIMING | NO_TRADE | RISING | RISING | 23 | 15.80403296501915 | MEDIUM |
| AKAM | 63.680 | CANDIDATE | NO_TRADE | IRREGULAR | 18.41982001904674 | [13.36, 6.0, 14.14] | [13.34, 5.28, 5.39] | 2.4808292663919276 | 3 | STABLE_3_OF_3 | [10, 12, 12] | [7, 10, 8] | [16, 7, 13] | [11, 7, 9] | 1.4722222222222223 | STABLE_OR_MIXED | False | 14.143262278384672 | 12.625845993401144 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 29.5 | 17.4508464841565 | HIGH |
| LBTYB | 63.253 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.909092989834864 | [4.07, 5.65, 6.91] | [4.67, 5.37, 3.68] | 1.2089660041389128 | 2 | WATCH_2_OF_3 | [2, 4, 22] | [3, 7, 16] | [2, 21, 5] | [6, 18, 2] | 0.7023809523809523 | STABLE_OR_MIXED | False | 6.909092989834864 | 9.267142068144333 | WATCH | NO_TRADE | MIXED | MIXED | 26 | 14.742978057208127 | MEDIUM |
| SCYX | 63.190 | CANDIDATE | NO_TRADE | INSUFFICIENT | 6.666667629974077 | [7.92, 4.51, 6.67] | [17.88, 18.25, 22.32] | 0.365333397990528 | 2 | WATCH_2_OF_3 | [19, 4, 5] | [16, 18, 7] | [16, 9, 4] | [12, 24, 7] | 0.53125 | DISSIPATING | False | 6.666667629974077 | 14.266437085736067 | FADING | NO_TRADE | MIXED | INSUFFICIENT | 27.5 | 28.630135062488527 | HIGH |
| MESO | 63.173 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.364017811603918 | [5.0, 7.36, 27.61] | [9.25, 4.97, 10.48] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [13, 8, 6] | [5, 6, 11] | [14, 9, 4] | [6, 6, 10] | 1.4166666666666665 | DISSIPATING | False | 27.60586658826034 | 11.58064295250315 | WATCH | NO_TRADE | FALLING | MIXED | 16 | 19.497767288923384 | MEDIUM |
| DXC | 62.572 | CANDIDATE | NO_TRADE | STABLE_RANGE | 15.46012038061787 | [12.68, 46.85, 11.1] | [4.87, 12.32, 10.68] | 1.1868595755041154 | 3 | STABLE_3_OF_3 | [13, 17, 11] | [11, 15, 6] | [14, 3, 22] | [21, 3, 16] | 1.0284090909090908 | STABLE_OR_MIXED | False | 11.10305309356936 | 10.636881532478355 | CYCLE_TIMING | NO_TRADE | RISING | MIXED | 30.5 | 15.46012038061787 | HIGH |
| WRBY | 62.166 | CANDIDATE | NO_TRADE | IRREGULAR | 17.830949282487975 | [6.29, 11.01, 41.9] | [10.39, 18.71, 12.65] | 0.8703031911300206 | 3 | STABLE_3_OF_3 | [9, 8, 11] | [17, 9, 3] | [8, 6, 13] | [17, 10, 6] | 0.9 | STABLE_OR_MIXED | False | 41.89759410691114 | 13.582607032642033 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 33 | 27.759537725403796 | HIGH |
| SPGI | 61.931 | CANDIDATE | NO_TRADE | INSUFFICIENT | 14.272715050622754 | [7.88, 4.37, 24.7] | [6.24, 4.72, 4.3] | 1.6695164333270074 | 2 | WATCH_2_OF_3 | [11, 4, 43] | [8, 7, 13] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 24.70293218258719 | 7.474272944170579 | WATCH | NO_TRADE | INSUFFICIENT | FALLING | 34.5 | 12.047373424014074 | MEDIUM |
| SKY | 60.785 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.459516171185919 | [5.32, 28.04, 5.46] | [20.98, 8.67, 3.09] | 0.6295002503869188 | 3 | STABLE_3_OF_3 | [9, 14, 3] | [12, 27, 8] | [15, 3, 14] | [6, 28, 9] | 1.1527777777777777 | DISSIPATING | False | 5.459516171185919 | 9.227890222701015 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | MIXED | 39 | 20.609552618625955 | MEDIUM |
| SGML | 60.324 | CANDIDATE | NO_TRADE | DOWNTREND | 7.869478779465289 | [12.97, 7.87, 11.21] | [19.14, 18.3, 3.53] | 0.6129616139871417 | 3 | STABLE_3_OF_3 | [8, 6, 3] | [13, 11, 6] | [6, 7, 3] | [19, 10, 9] | 0.5727272727272728 | DISSIPATING | False | 11.214951688373453 | 16.296788374760958 | FADING | NO_TRADE | FALLING | FALLING | 24 | 25.88678330185843 | MEDIUM |
| TT | 60.117 | CANDIDATE | NO_TRADE | STABLE_RANGE | 5.625560811137554 | [13.36, 3.07, 3.63] | [3.24, 9.92, 2.73] | 1.120909955921715 | 1 | UNSTABLE | [33, 6, 4] | [18, 11, 11] | [21, 6, 9] | [8, 15, 18] | 0.5727272727272728 | STABLE_OR_MIXED | False | 3.634527680280586 | 6.891734293876586 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | FALLING | 45.0 | 13.358475163215644 | HIGH |
| OBE | 59.882 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.994571511853363 | [18.18, 4.06, 4.99] | [33.37, 7.27, 13.97] | 0.357473074980304 | 1 | UNSTABLE | [26, 4, 10] | [14, 5, 10] | [17, 9, 4] | [14, 3, 21] | 0.8214285714285714 | DISSIPATING | False | 4.994571511853363 | 13.056364444419435 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 26 | 20.579126911603737 | MEDIUM |
| ESNT | 59.550 | CANDIDATE | NO_TRADE | INSUFFICIENT | 8.309903114311389 | [9.81, 6.74, 8.31] | [5.74, 6.23, 3.06] | 1.4468196786663896 | 3 | STABLE_3_OF_3 | [24, 8, 11] | [8, 20, 6] | [8, 7, 12] | [10, 17, 21] | 0.9227941176470589 | STABLE_OR_MIXED | False | 8.309903114311389 | 7.668946271433978 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 53 | 12.641914967787642 | HIGH |
| SCI | 59.459 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.257798466890627 | [10.21, 3.31, 2.77] | [11.65, 3.67, 3.16] | 0.9033699635757841 | 1 | UNSTABLE | [29, 7, 2] | [11, 18, 11] | [18, 3, 4] | [20, 15, 18] | 0.4292929292929293 | STABLE_OR_MIXED | False | 2.7685370785236696 | 7.215071929780312 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 51 | 10.816676294127237 | HIGH |
| EPOW | 59.148 | CANDIDATE | NO_TRADE | IRREGULAR | 37.50000240341308 | [18.05, 75.27, 8.87] | [12.76, 16.09, 6.79] | 1.414459581942611 | 3 | STABLE_3_OF_3 | [7, 5, 11] | [16, 7, 7] | [5, 6, 14] | [18, 6, 6] | 1.0 | STABLE_OR_MIXED | False | 8.870971091208023 | 17.175320233745158 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 28 | 30.18182482727739 | MEDIUM |
| FORTY | 58.993 | CANDIDATE | SELL | STABLE_RANGE | 15.446710910926864 | [4.1, 16.5, 15.45] | [7.31, 4.07, 23.72] | 2.11184666776608 | 2 | WATCH_2_OF_3 | [21, 15, 11] | [4, 7, 22] | [36, 7, 18] | [5, 8, 6] | 2.571428571428571 | DISSIPATING | False | 15.446710910926864 | 10.170618032023935 | WATCH | NO_TRADE | MIXED | MIXED | 25.5 | 14.303135627186482 | MEDIUM |
| METCB | 58.881 | CANDIDATE | NO_TRADE | INSUFFICIENT | 17.857141716747872 | [6.24, 18.52, 11.68] | [7.19, 4.68, 6.15] | 1.90102632967061 | 3 | STABLE_3_OF_3 | [6, 13, 12] | [4, 11, 6] | [3, 13, 11] | [8, 11, 6] | 1.6875 | DISSIPATING | False | 11.684784210781718 | 11.534077315677237 | CYCLE_TIMING | NO_TRADE | FALLING | INSUFFICIENT | 53 | 41.58882283911626 | HIGH |
| NYAX | 58.653 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.842953829227538 | [18.54, 3.19, 14.84] | [5.29, 2.94, 16.75] | 2.8064066971878407 | 2 | WATCH_2_OF_3 | [16, 6, 5] | [5, 12, 10] | [14, 13, 4] | [4, 12, 5] | 1.6 | DISSIPATING | False | 14.842899778193752 | 9.616382893600244 | WATCH | NO_TRADE | MIXED | RISING | 24 | 16.651655201817416 | MEDIUM |
| COOK | 58.455 | CANDIDATE | NO_TRADE | STABLE_RANGE | 20.104380920592835 | [19.93, 20.1, 45.35] | [6.15, 4.55, 3.62] | 4.422055989466411 | 3 | STABLE_3_OF_3 | [12, 19, 6] | [10, 10, 6] | [10, 14, 12] | [10, 10, 7] | 1.2 | STABLE_OR_MIXED | False | 45.34672876099246 | 14.37046129050408 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 22.5 | 22.828281286991004 | MEDIUM |
| ATGL | 58.389 | CANDIDATE | NO_TRADE | STABLE_RANGE | 14.583338714307992 | [145.59, 6.08, 18.17] | [4.02, 6.46, 11.36] | 2.8133257639351634 | 3 | STABLE_3_OF_3 | [9, 4, 4] | [4, 9, 3] | [2, 11, 4] | [7, 9, 3] | 0.7857142857142857 | STABLE_OR_MIXED | False | 18.17072933873267 | 21.88135714940693 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 21 | 32.06849916938487 | MEDIUM |
| HLIT | 58.332 | CANDIDATE | NO_TRADE | DOWNTREND | 9.296026534869107 | [6.82, 10.69, 7.46] | [3.58, 3.36, 3.29] | 2.2215823222141275 | 3 | STABLE_3_OF_3 | [16, 9, 7] | [8, 11, 2] | [11, 7, 9] | [8, 6, 11] | 1.125 | STABLE_OR_MIXED | False | 7.462686425532894 | 10.432113298587037 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 46 | 18.52179327708091 | HIGH |
| CNXN | 58.077 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.862198238801012 | [14.11, 24.13, 2.56] | [14.93, 5.33, 13.28] | 1.0624938734190283 | 2 | UNSTABLE | [16, 49, 16] | [16, 6, 21] | [28, 47, 6] | [14, 12, 16] | 1.5 | STABLE_OR_MIXED | False | 2.5578074535849593 | 8.56666484348327 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 40.0 | 11.614243259273094 | MEDIUM |
| ASO | 57.770 | CANDIDATE | NO_TRADE | INSUFFICIENT | 21.384722111271024 | [29.86, 29.11, 21.38] | [8.24, 5.36, 3.23] | 5.426943421325845 | 3 | STABLE_3_OF_3 | [16, 29, 12] | [4, 9, 7] | [8, 24, 19] | [12, 9, 7] | 2.1984126984126986 | DISSIPATING | True | 21.384722111271024 | 9.912657410948654 | DISSIPATING | NO_TRADE | INSUFFICIENT | MIXED | 36 | 18.155691497181934 | MEDIUM |
| TLN | 57.693 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.294516128795747 | [6.38, 6.39, 7.29] | [10.68, 10.91, 34.08] | 0.5854343137150776 | 3 | STABLE_3_OF_3 | [4, 12, 3] | [7, 18, 21] | [11, 6, 3] | [19, 9, 17] | 0.2875816993464052 | DISSIPATING | False | 7.294516128795747 | 11.358460982509582 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 32.0 | 23.460024521868796 | MEDIUM |

## Experimental recent-swing review shortlist (NOT BUY signals)
Count: 0 of 110 scored CANDIDATE names
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
    "observations": 232,
    "positive_net_pct": 44.39655172413793,
    "average_net_pct": -1.4008831464156533,
    "average_positive_pct": 4.084670820919169,
    "average_nonpositive_pct": -5.780821585450437,
    "benchmark_pairs": 232,
    "average_excess_pct": -0.6364302502094917,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 1492,
    "positive_net_pct": 51.0053619302949,
    "average_net_pct": 0.20274392546630055,
    "average_positive_pct": 6.507169883431778,
    "average_nonpositive_pct": -6.360413603961495,
    "benchmark_pairs": 1492,
    "average_excess_pct": 0.9647379644085918,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 166,
    "positive_net_pct": 48.19277108433735,
    "average_net_pct": -0.48339324496540587,
    "average_positive_pct": 5.0754501898788025,
    "average_nonpositive_pct": -5.6544103936576935,
    "benchmark_pairs": 166,
    "average_excess_pct": 0.25379512615601646,
    "worst_adverse_excursion_pct": -25.57142802647182
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 181,
    "positive_net_pct": 48.61878453038674,
    "average_net_pct": -1.9919774955548384,
    "average_positive_pct": 6.110539660059957,
    "average_nonpositive_pct": -9.658875449254856,
    "benchmark_pairs": 181,
    "average_excess_pct": -0.5029693503022813,
    "worst_adverse_excursion_pct": -95.51242232978043
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 1099,
    "positive_net_pct": 51.137397634212924,
    "average_net_pct": 0.9045055849544441,
    "average_positive_pct": 10.948377972065696,
    "average_nonpositive_pct": -9.606958626510211,
    "benchmark_pairs": 1099,
    "average_excess_pct": 2.553246654366977,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 133,
    "positive_net_pct": 54.13533834586466,
    "average_net_pct": 0.9018946122463671,
    "average_positive_pct": 8.108890946225427,
    "average_nonpositive_pct": -7.604724011466625,
    "benchmark_pairs": 133,
    "average_excess_pct": 2.377439749994404,
    "worst_adverse_excursion_pct": -30.81636301420778
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "0-40",
    "observations": 64,
    "positive_net_pct": 59.375,
    "average_net_pct": -0.6186187134550195,
    "average_positive_pct": 7.594188417476893,
    "average_nonpositive_pct": -12.621952212509353,
    "benchmark_pairs": 64,
    "average_excess_pct": 1.7893876434991887,
    "worst_adverse_excursion_pct": -69.10112242914782
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "40-60",
    "observations": 371,
    "positive_net_pct": 46.63072776280323,
    "average_net_pct": 1.211078150648151,
    "average_positive_pct": 17.840821668243677,
    "average_nonpositive_pct": -13.318950276341868,
    "benchmark_pairs": 371,
    "average_excess_pct": 3.621782555531223,
    "worst_adverse_excursion_pct": -89.14473627454025
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "60-80",
    "observations": 56,
    "positive_net_pct": 44.642857142857146,
    "average_net_pct": -1.5735703066350726,
    "average_positive_pct": 11.641899599521816,
    "average_nonpositive_pct": -12.231207327729344,
    "benchmark_pairs": 56,
    "average_excess_pct": 0.8572261319853742,
    "worst_adverse_excursion_pct": -47.09677302750536
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
- CBZ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- MIMI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- BZH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- NATH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WALD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- LRHC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WFC.PRL: ValueError: EMPTY_PROVIDER_RESPONSE
- INDV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
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
- KVUE: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ADIL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- CCXI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- GNTA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ALDF: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- INM: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- KAZR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TCBI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
