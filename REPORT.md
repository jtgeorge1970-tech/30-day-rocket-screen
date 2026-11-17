# OFTS daily research

Market session: 2026-11-16
Selected: 155; refreshed: 126; refresh errors: 38
Qualified prediction cohorts saved: 27; current coverage: 126/155
Outcome counts: {'CORPORATE_ACTION_REVIEW': 34, 'INELIGIBLE_DATA': 2460, 'MATURE': 5359, 'MISSING_SESSIONS': 4, 'PENDING': 10503}
Cycle fingerprints saved: 129/190
Signal states: BUY=0, SELL=11, NO_TRADE=179
Cycle ledger: pending entries=0; open positions=38; closed trades=24; SPY pairs=24
Cycle-speed report card: READY; closed forward trades=24; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 10.812020991246296-68.39422789876026; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 23, '40_TO_49_999': 49, '50_TO_59_999': 43, '60_TO_69_999': 14, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=127
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=105; REVIEW=24; INSUFFICIENT=85
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| MWH | 68.394 | CANDIDATE | NO_TRADE | INSUFFICIENT | 11.152554385226521 | [11.38, 13.52, 15.21] | [18.33, 5.95, 9.76] | 1.385666278611575 | 3 | STABLE_3_OF_3 | [11, 17, 3] | [8, 17, 9] | [19, 5, 4] | [19, 5, 12] | 0.8194444444444445 | STABLE_OR_MIXED | False | 15.212715679159539 | 11.431672904891617 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 47.5 | 35.23344052246027 | HIGH |
| LBTYB | 64.358 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.909092989834864 | [4.07, 5.65, 6.91] | [4.67, 5.37, 3.68] | 1.2089660041389128 | 2 | WATCH_2_OF_3 | [2, 4, 22] | [3, 7, 16] | [2, 21, 5] | [6, 18, 2] | 0.7023809523809523 | STABLE_OR_MIXED | False | 6.909092989834864 | 9.227690725673797 | WATCH | NO_TRADE | MIXED | MIXED | 26 | 14.742978057208127 | MEDIUM |
| MUR | 63.814 | CANDIDATE | NO_TRADE | IRREGULAR | 22.079388547218926 | [5.65, 23.34, 6.57] | [10.73, 8.87, 10.87] | 0.6122143089647392 | 3 | STABLE_3_OF_3 | [7, 21, 15] | [7, 9, 8] | [11, 5, 29] | [6, 7, 8] | 1.7232142857142856 | DISSIPATING | False | 6.570189603155541 | 9.025646968385692 | CYCLE_TIMING | NO_TRADE | RISING | RISING | 23 | 15.80403296501915 | MEDIUM |
| AKAM | 63.190 | CANDIDATE | NO_TRADE | IRREGULAR | 18.41982001904674 | [13.36, 6.0, 14.14] | [13.34, 5.28, 5.39] | 2.4808292663919276 | 3 | STABLE_3_OF_3 | [10, 12, 12] | [7, 10, 8] | [16, 7, 13] | [11, 7, 9] | 1.4722222222222223 | STABLE_OR_MIXED | False | 14.143262278384672 | 12.625845993401144 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 29.5 | 17.4508464841565 | HIGH |
| WRBY | 63.024 | CANDIDATE | NO_TRADE | INSUFFICIENT | 17.830949282487975 | [6.29, 11.01, 41.9] | [10.39, 18.71, 12.65] | 0.8703031911300206 | 3 | STABLE_3_OF_3 | [9, 8, 11] | [17, 9, 3] | [8, 6, 13] | [17, 10, 6] | 0.9 | STABLE_OR_MIXED | False | 41.89759410691114 | 13.735333179368437 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | FALLING | 33 | 27.759537725403796 | HIGH |
| OBE | 62.606 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.994571511853363 | [4.06, 4.99, 7.38] | [7.27, 13.97, 18.18] | 0.357473074980304 | 1 | UNSTABLE | [4, 10, 5] | [5, 10, 26] | [17, 9, 4] | [14, 3, 21] | 0.5714285714285714 | DISSIPATING | False | 7.383282327462348 | 12.933036572311671 | TOO_SMALL | NO_TRADE | MIXED | MIXED | 26 | 20.579126911603737 | MEDIUM |
| DXC | 62.425 | CANDIDATE | NO_TRADE | STABLE_RANGE | 15.46012038061787 | [12.68, 46.85, 11.1] | [4.87, 12.32, 10.68] | 1.1868595755041154 | 3 | STABLE_3_OF_3 | [13, 17, 11] | [11, 15, 6] | [14, 3, 22] | [21, 3, 16] | 1.0284090909090908 | STABLE_OR_MIXED | False | 11.10305309356936 | 10.583942175967174 | CYCLE_TIMING | NO_TRADE | RISING | MIXED | 31 | 15.51175056999825 | HIGH |
| CACC | 61.451 | CANDIDATE | NO_TRADE | DOWNTREND | 15.289628474476945 | [9.17, 7.15, 15.29] | [3.85, 7.2, 6.53] | 1.4054024701331038 | 3 | STABLE_3_OF_3 | [35, 5, 7] | [9, 13, 20] | [31, 17, 4] | [21, 8, 16] | 0.8004807692307692 | STABLE_OR_MIXED | False | 15.289628474476945 | 9.42626034498389 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 42 | 16.10968422328472 | HIGH |
| S | 60.802 | CANDIDATE | NO_TRADE | IRREGULAR | 16.686111088855004 | [17.38, 19.14, 11.02] | [11.82, 20.84, 7.06] | 1.4709178542010226 | 3 | STABLE_3_OF_3 | [12, 14, 9] | [10, 12, 6] | [5, 15, 14] | [23, 9, 8] | 1.3777777777777778 | STABLE_OR_MIXED | False | 11.017743239709121 | 11.447871138581554 | CYCLE_TIMING | NO_TRADE | MIXED | RISING | 45 | 19.60443311050927 | HIGH |
| TDY | 60.792 | CANDIDATE | NO_TRADE | INSUFFICIENT | 12.134402813224042 | [4.53, 12.13, 10.04] | [8.94, 5.18, 9.5] | 1.1228368303155556 | 2 | WATCH_2_OF_3 | [41, 17, 9] | [9, 17, 10] | [29, 20, 21] | [9, 13, 11] | 1.8045454545454547 | DISSIPATING | False | 10.038536360954486 | 7.245056130560562 | WATCH | NO_TRADE | INSUFFICIENT | FALLING | 58 | 13.900054013498732 | MEDIUM |
| SKY | 60.771 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.459516171185919 | [5.32, 28.04, 5.46] | [20.98, 8.67, 3.09] | 0.6295002503869188 | 3 | STABLE_3_OF_3 | [9, 14, 3] | [12, 27, 8] | [15, 3, 14] | [6, 28, 9] | 1.1527777777777777 | DISSIPATING | False | 5.459516171185919 | 9.227890222701015 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | MIXED | 39 | 20.609552618625955 | MEDIUM |
| SPGI | 60.665 | CANDIDATE | NO_TRADE | INSUFFICIENT | 14.272715050622754 | [7.88, 4.37, 24.7] | [6.24, 4.72, 4.3] | 1.6695164333270074 | 2 | WATCH_2_OF_3 | [11, 4, 43] | [8, 7, 13] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 24.70293218258719 | 7.608237653408694 | WATCH | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 34.5 | 12.047373424014074 | MEDIUM |
| SGML | 60.232 | CANDIDATE | NO_TRADE | DOWNTREND | 7.869478779465289 | [12.97, 7.87, 11.21] | [19.14, 18.3, 3.53] | 0.6129616139871417 | 3 | STABLE_3_OF_3 | [8, 6, 3] | [13, 11, 6] | [6, 7, 3] | [19, 10, 9] | 0.5727272727272728 | DISSIPATING | False | 11.214951688373453 | 16.233279881291654 | FADING | NO_TRADE | FALLING | FALLING | 24 | 25.88678330185843 | MEDIUM |
| TT | 60.032 | CANDIDATE | NO_TRADE | STABLE_RANGE | 8.258798834697112 | [3.07, 3.63, 8.26] | [9.92, 2.73, 13.36] | 0.3663484686261195 | 1 | UNSTABLE | [6, 4, 11] | [11, 11, 33] | [21, 6, 9] | [8, 15, 18] | 0.5727272727272728 | DISSIPATING | False | 8.258798834697112 | 6.927709676529757 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | FALLING | 45.0 | 13.358475163215644 | HIGH |
| MESO | 59.838 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.364017811603918 | [5.0, 7.36, 27.61] | [9.25, 4.97, 10.48] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [13, 8, 6] | [5, 6, 11] | [14, 9, 4] | [6, 6, 10] | 1.4166666666666665 | DISSIPATING | False | 27.60586658826034 | 11.58064295250315 | WATCH | NO_TRADE | FALLING | MIXED | 16.0 | 19.704195329980422 | MEDIUM |
| ESNT | 59.508 | CANDIDATE | NO_TRADE | INSUFFICIENT | 8.309903114311389 | [9.81, 6.74, 8.31] | [5.74, 6.23, 3.06] | 1.4468196786663896 | 3 | STABLE_3_OF_3 | [24, 8, 11] | [8, 20, 6] | [8, 7, 12] | [10, 17, 21] | 0.9227941176470589 | STABLE_OR_MIXED | False | 8.309903114311389 | 7.668946271433978 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 53 | 12.641914967787642 | HIGH |
| SCI | 59.440 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.257798466890627 | [10.21, 3.31, 2.77] | [11.65, 3.67, 3.16] | 0.9033699635757841 | 1 | UNSTABLE | [29, 7, 2] | [11, 18, 11] | [18, 3, 4] | [20, 15, 18] | 0.4292929292929293 | STABLE_OR_MIXED | False | 2.7685370785236696 | 7.215071929780312 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 51 | 10.816676294127237 | HIGH |
| METCB | 59.297 | CANDIDATE | NO_TRADE | INSUFFICIENT | 17.857141716747872 | [6.24, 18.52, 11.68] | [7.19, 4.68, 6.15] | 1.90102632967061 | 3 | STABLE_3_OF_3 | [6, 13, 12] | [4, 11, 6] | [3, 13, 11] | [8, 11, 6] | 1.6875 | DISSIPATING | False | 11.684784210781718 | 11.531564597478907 | CYCLE_TIMING | NO_TRADE | FALLING | INSUFFICIENT | 53 | 41.58882283911626 | HIGH |
| HLIT | 58.513 | CANDIDATE | NO_TRADE | STABLE_RANGE | 9.296026534869107 | [6.82, 10.69, 7.46] | [3.58, 3.36, 3.29] | 2.2215823222141275 | 3 | STABLE_3_OF_3 | [16, 9, 7] | [8, 11, 2] | [11, 7, 9] | [8, 6, 11] | 1.125 | STABLE_OR_MIXED | False | 7.462686425532894 | 10.422283846651746 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 46 | 18.52179327708091 | HIGH |
| ATGL | 58.395 | CANDIDATE | NO_TRADE | STABLE_RANGE | 14.583338714307992 | [145.59, 6.08, 18.17] | [4.02, 6.46, 11.36] | 2.8133257639351634 | 3 | STABLE_3_OF_3 | [9, 4, 4] | [4, 9, 3] | [11, 4, 4] | [9, 3, 2] | 1.1666666666666665 | STABLE_OR_MIXED | False | 18.17072933873267 | 21.47650795379392 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 21 | 32.06849916938487 | MEDIUM |
| ECG | 57.956 | CANDIDATE | NO_TRADE | DOWNTREND | 23.012144681288472 | [13.86, 9.84, 23.01] | [6.42, 3.64, 21.53] | 2.156937540949749 | 3 | STABLE_3_OF_3 | [17, 3, 6] | [15, 3, 17] | [28, 5, 4] | [17, 5, 3] | 0.7 | STABLE_OR_MIXED | False | 23.012144681288472 | 10.678637332284598 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 33 | 25.592558307926748 | MEDIUM |
| WTTR | 57.695 | CANDIDATE | NO_TRADE | INSUFFICIENT | 6.860325027289937 | [3.72, 13.63, 4.79] | [9.65, 3.64, 4.61] | 1.0387891392598312 | 1 | UNSTABLE | [5, 18, 6] | [15, 8, 6] | [17, 10, 2] | [13, 7, 4] | 1.0892857142857144 | STABLE_OR_MIXED | False | 4.792750938495227 | 10.08192257740611 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | INSUFFICIENT | 60 | 20.239811263803087 | MEDIUM |
| TLN | 57.604 | CANDIDATE | NO_TRADE | STABLE_RANGE | 11.490985450081748 | [6.39, 7.29, 22.28] | [10.91, 34.08, 6.38] | 0.6687327628073135 | 3 | STABLE_3_OF_3 | [12, 3, 7] | [18, 21, 4] | [11, 6, 3] | [19, 9, 17] | 0.3709150326797386 | DISSIPATING | False | 22.280017459847024 | 11.524454149433504 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 32.0 | 23.460024521868796 | MEDIUM |
| NYAX | 57.255 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.842953829227538 | [18.54, 3.19, 14.84] | [16.98, 5.29, 16.75] | 0.8862085258938412 | 2 | WATCH_2_OF_3 | [16, 6, 5] | [5, 5, 22] | [14, 13, 4] | [4, 4, 17] | 2.225 | DISSIPATING | False | 14.842899778193752 | 10.159913159516131 | WATCH | NO_TRADE | MIXED | RISING | 28.0 | 16.922769870358156 | MEDIUM |
| BFAM | 56.977 | CANDIDATE | NO_TRADE | INSUFFICIENT | 10.05678951147475 | [11.66, 10.06, 5.6] | [6.43, 6.86, 5.1] | 1.5639209490413801 | 3 | STABLE_3_OF_3 | [17, 6, 7] | [22, 12, 5] | [7, 15, 9] | [18, 17, 7] | 0.5563725490196079 | STABLE_OR_MIXED | False | 5.597294230442529 | 9.640542319296094 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 65.5 | 18.3680156066923 | MEDIUM |

## Experimental recent-swing review shortlist (NOT BUY signals)
Count: 0 of 107 scored CANDIDATE names
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
    "observations": 246,
    "positive_net_pct": 42.68292682926829,
    "average_net_pct": -1.5054502729663786,
    "average_positive_pct": 4.034497233911707,
    "average_nonpositive_pct": -5.630943097237297,
    "benchmark_pairs": 246,
    "average_excess_pct": -0.7123250749790538,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 1572,
    "positive_net_pct": 50.25445292620865,
    "average_net_pct": 0.029195962503293618,
    "average_positive_pct": 6.410471447642856,
    "average_nonpositive_pct": -6.417361113277066,
    "benchmark_pairs": 1572,
    "average_excess_pct": 0.8169544879590721,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 173,
    "positive_net_pct": 48.554913294797686,
    "average_net_pct": -0.5707849718183643,
    "average_positive_pct": 5.092548809313373,
    "average_nonpositive_pct": -5.915953933785397,
    "benchmark_pairs": 173,
    "average_excess_pct": 0.1878920975381807,
    "worst_adverse_excursion_pct": -25.57142802647182
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 191,
    "positive_net_pct": 48.69109947643979,
    "average_net_pct": -1.792351161277526,
    "average_positive_pct": 6.212460509264757,
    "average_nonpositive_pct": -9.388754073118667,
    "benchmark_pairs": 191,
    "average_excess_pct": -0.28193947582533574,
    "worst_adverse_excursion_pct": -95.51242232978043
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 1170,
    "positive_net_pct": 49.914529914529915,
    "average_net_pct": 0.5704082651341182,
    "average_positive_pct": 10.811967268881942,
    "average_nonpositive_pct": -9.636196612321044,
    "benchmark_pairs": 1170,
    "average_excess_pct": 2.234264123648674,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 139,
    "positive_net_pct": 53.9568345323741,
    "average_net_pct": 0.8308102583818071,
    "average_positive_pct": 8.10127984497034,
    "average_nonpositive_pct": -7.689271288401634,
    "benchmark_pairs": 139,
    "average_excess_pct": 2.3245829051363556,
    "worst_adverse_excursion_pct": -30.81636301420778
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "0-40",
    "observations": 72,
    "positive_net_pct": 56.94444444444444,
    "average_net_pct": -0.9255820586010013,
    "average_positive_pct": 7.093006869076836,
    "average_nonpositive_pct": -11.530812575852336,
    "benchmark_pairs": 72,
    "average_excess_pct": 1.6129926377180477,
    "worst_adverse_excursion_pct": -69.10112242914782
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "40-60",
    "observations": 435,
    "positive_net_pct": 47.12643678160919,
    "average_net_pct": 0.8754228320563748,
    "average_positive_pct": 17.41210925862396,
    "average_nonpositive_pct": -13.863797678579937,
    "benchmark_pairs": 435,
    "average_excess_pct": 3.4586207735065786,
    "worst_adverse_excursion_pct": -89.14473627454025
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "60-80",
    "observations": 65,
    "positive_net_pct": 44.61538461538461,
    "average_net_pct": -1.817771618713318,
    "average_positive_pct": 11.276614132768072,
    "average_nonpositive_pct": -12.366026807406666,
    "benchmark_pairs": 65,
    "average_excess_pct": 0.7725775084233738,
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
- INM: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- ALDF: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- BFS: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- EMBJ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SPLIT_REQUIRES_DAILY_ACTION_AUDIT
- KNRX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- MGPI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- MHNC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- RDIB: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TCBI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- TGL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
