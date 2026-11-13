# OFTS daily research

Market session: 2026-11-12
Selected: 149; refreshed: 120; refresh errors: 36
Qualified prediction cohorts saved: 25; current coverage: 120/149
Outcome counts: {'CORPORATE_ACTION_REVIEW': 30, 'INELIGIBLE_DATA': 2110, 'MATURE': 4654, 'MISSING_SESSIONS': 5, 'PENDING': 10016}
Cycle fingerprints saved: 134/183
Signal states: BUY=2, SELL=3, NO_TRADE=178
Cycle ledger: pending entries=2; open positions=37; closed trades=22; SPY pairs=22
Cycle-speed report card: READY; closed forward trades=22; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 12.009358685782429-68.29485969280613; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 18, '40_TO_49_999': 61, '50_TO_59_999': 47, '60_TO_69_999': 8, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=133
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=116; REVIEW=18; INSUFFICIENT=101
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| MWH | 68.295 | CANDIDATE | NO_TRADE | INSUFFICIENT | 11.152554385226521 | [11.38, 13.52, 15.21] | [18.33, 5.95, 9.76] | 1.385666278611575 | 3 | STABLE_3_OF_3 | [11, 17, 3] | [8, 17, 9] | [19, 5, 4] | [19, 5, 12] | 0.8194444444444445 | STABLE_OR_MIXED | False | 15.212715679159539 | 11.431672904891617 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 47.5 | 35.23344052246027 | HIGH |
| MESO | 62.929 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.364017811603918 | [5.0, 7.36, 27.61] | [9.25, 4.97, 10.48] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [13, 8, 6] | [5, 6, 11] | [14, 9, 4] | [6, 6, 10] | 1.4166666666666665 | DISSIPATING | False | 27.60586658826034 | 11.654384747299156 | WATCH | NO_TRADE | FALLING | MIXED | 16.0 | 19.291339247866347 | MEDIUM |
| DXC | 62.547 | CANDIDATE | NO_TRADE | STABLE_RANGE | 15.46012038061787 | [10.68, 12.68, 46.85] | [28.49, 4.87, 12.32] | 1.0293825439823863 | 3 | STABLE_3_OF_3 | [6, 13, 17] | [12, 11, 15] | [14, 3, 22] | [21, 3, 16] | 0.9791666666666666 | STABLE_OR_MIXED | False | 46.84683492688584 | 10.682395098587056 | CYCLE_TIMING | NO_TRADE | RISING | MIXED | 30.5 | 15.46012038061787 | HIGH |
| WRBY | 62.179 | CANDIDATE | NO_TRADE | IRREGULAR | 17.830949282487975 | [6.29, 11.01, 41.9] | [10.39, 18.71, 12.65] | 0.8703031911300206 | 3 | STABLE_3_OF_3 | [9, 8, 11] | [17, 9, 3] | [8, 6, 13] | [17, 10, 6] | 0.9 | STABLE_OR_MIXED | False | 41.89759410691114 | 13.601703509082073 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 33 | 27.759537725403796 | HIGH |
| SPGI | 61.998 | CANDIDATE | NO_TRADE | INSUFFICIENT | 14.272715050622754 | [7.88, 4.37, 24.7] | [6.24, 4.72, 4.3] | 1.6695164333270074 | 2 | WATCH_2_OF_3 | [11, 4, 43] | [8, 7, 13] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 24.70293218258719 | 7.474272944170579 | WATCH | NO_TRADE | INSUFFICIENT | FALLING | 34.5 | 12.047373424014074 | MEDIUM |
| BFAM | 61.262 | CANDIDATE | NO_TRADE | INSUFFICIENT | 10.05678951147475 | [11.66, 10.06, 5.6] | [6.43, 6.86, 5.1] | 1.5639209490413801 | 3 | STABLE_3_OF_3 | [17, 6, 7] | [22, 12, 5] | [7, 15, 9] | [18, 17, 7] | 0.5563725490196079 | STABLE_OR_MIXED | False | 5.597294230442529 | 10.04827335318502 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 67.5 | 19.296013785096644 | HIGH |
| SCYX | 60.350 | CANDIDATE | NO_TRADE | INSUFFICIENT | 6.666667629974077 | [7.92, 4.51, 6.67] | [17.88, 18.25, 22.32] | 0.365333397990528 | 2 | WATCH_2_OF_3 | [19, 4, 5] | [16, 18, 7] | [16, 9, 4] | [12, 24, 7] | 0.53125 | DISSIPATING | False | 6.666667629974077 | 14.266437085736067 | FADING | NO_TRADE | MIXED | INSUFFICIENT | 25.5 | 28.115015507998507 | MEDIUM |
| CRNC | 60.314 | CANDIDATE | NO_TRADE | IRREGULAR | 8.38563127851435 | [19.56, 9.02, 8.34] | [4.55, 3.82, 6.47] | 1.9838325962779013 | 3 | STABLE_3_OF_3 | [17, 14, 5] | [4, 4, 3] | [7, 24, 3] | [12, 4, 2] | 2.625 | DISSIPATING | False | 8.343712311009476 | 11.748755577198116 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 17 | 20.135473477171224 | MEDIUM |
| DUOT | 59.984 | CANDIDATE | NO_TRADE | DOWNTREND | 15.856236722529871 | [16.48, 10.43, 15.86] | [5.11, 17.9, 4.41] | 3.102773341618217 | 3 | STABLE_3_OF_3 | [11, 6, 9] | [7, 12, 8] | [12, 5, 9] | [4, 6, 14] | 1.3125 | STABLE_OR_MIXED | False | 15.856236722529871 | 13.429468329214748 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 26.0 | 29.401851767193875 | MEDIUM |
| OBE | 59.929 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.994571511853363 | [18.18, 4.06, 4.99] | [33.37, 7.27, 13.97] | 0.357473074980304 | 1 | UNSTABLE | [26, 4, 10] | [14, 5, 10] | [17, 9, 4] | [14, 3, 21] | 0.8214285714285714 | DISSIPATING | False | 4.994571511853363 | 13.056364444419435 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 26 | 20.579126911603737 | MEDIUM |
| ESNT | 59.542 | CANDIDATE | NO_TRADE | INSUFFICIENT | 8.309903114311389 | [9.81, 6.74, 8.31] | [5.74, 6.23, 3.06] | 1.4468196786663896 | 3 | STABLE_3_OF_3 | [24, 8, 11] | [8, 20, 6] | [8, 7, 12] | [10, 17, 21] | 0.9227941176470589 | STABLE_OR_MIXED | False | 8.309903114311389 | 7.668946271433978 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 53 | 12.641914967787642 | HIGH |
| SCI | 59.203 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.257798466890627 | [10.21, 3.31, 2.77] | [11.65, 3.67, 3.16] | 0.9033699635757841 | 1 | UNSTABLE | [29, 7, 2] | [11, 18, 11] | [18, 3, 4] | [20, 15, 18] | 0.4292929292929293 | STABLE_OR_MIXED | False | 2.7685370785236696 | 7.22977562574648 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 51 | 10.816676294127237 | HIGH |
| METCB | 59.122 | CANDIDATE | NO_TRADE | INSUFFICIENT | 17.857141716747872 | [6.15, 6.24, 18.52] | [15.95, 7.19, 4.68] | 0.8675568786153617 | 3 | STABLE_3_OF_3 | [6, 6, 13] | [6, 4, 11] | [3, 13, 11] | [8, 11, 6] | 1.1875 | STABLE_OR_MIXED | False | 18.518519920156272 | 11.594349960298949 | CYCLE_TIMING | NO_TRADE | FALLING | INSUFFICIENT | 53 | 41.58882283911626 | HIGH |
| EPOW | 59.060 | CANDIDATE | NO_TRADE | IRREGULAR | 37.50000240341308 | [6.79, 18.05, 75.27] | [18.2, 12.76, 16.09] | 1.121500609105117 | 3 | STABLE_3_OF_3 | [7, 7, 5] | [12, 16, 7] | [5, 6, 14] | [18, 6, 6] | 0.7916666666666667 | STABLE_OR_MIXED | False | 75.26502374076233 | 17.102973443389956 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 28 | 30.18182482727739 | MEDIUM |
| ASO | 58.944 | CANDIDATE | NO_TRADE | INSUFFICIENT | 21.384722111271024 | [29.86, 29.11, 21.38] | [8.24, 5.36, 3.23] | 5.426943421325845 | 3 | STABLE_3_OF_3 | [16, 29, 12] | [4, 9, 7] | [8, 24, 19] | [12, 9, 7] | 2.1984126984126986 | DISSIPATING | True | 21.384722111271024 | 9.921063699309308 | DISSIPATING | NO_TRADE | INSUFFICIENT | MIXED | 35.5 | 17.894552642278793 | HIGH |
| HLIT | 58.631 | CANDIDATE | NO_TRADE | DOWNTREND | 9.296026534869107 | [6.82, 10.69, 7.46] | [3.58, 3.36, 3.29] | 2.2215823222141275 | 3 | STABLE_3_OF_3 | [16, 9, 7] | [8, 11, 2] | [11, 7, 9] | [8, 6, 11] | 1.125 | STABLE_OR_MIXED | False | 7.462686425532894 | 10.551179968059344 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 46 | 18.52179327708091 | HIGH |
| ATGL | 58.593 | CANDIDATE | NO_TRADE | STABLE_RANGE | 14.583338714307992 | [145.59, 6.08, 18.17] | [4.02, 6.46, 11.36] | 2.8133257639351634 | 3 | STABLE_3_OF_3 | [9, 4, 4] | [4, 9, 3] | [2, 11, 4] | [7, 9, 3] | 0.7857142857142857 | STABLE_OR_MIXED | False | 18.17072933873267 | 21.92543741223409 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 21 | 32.06849916938487 | MEDIUM |
| COOK | 58.456 | CANDIDATE | SELL | STABLE_RANGE | 20.104380920592835 | [19.93, 20.1, 45.35] | [6.15, 4.55, 3.62] | 4.422055989466411 | 3 | STABLE_3_OF_3 | [12, 19, 6] | [10, 10, 6] | [10, 14, 12] | [10, 10, 7] | 1.2 | STABLE_OR_MIXED | False | 45.34672876099246 | 14.388970871045828 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 22.5 | 22.828281286991004 | MEDIUM |
| TT | 58.236 | CANDIDATE | NO_TRADE | STABLE_RANGE | 5.625560811137554 | [13.36, 3.07, 3.63] | [3.24, 9.92, 2.73] | 1.120909955921715 | 1 | UNSTABLE | [33, 6, 4] | [18, 11, 11] | [21, 6, 9] | [8, 15, 18] | 0.5727272727272728 | STABLE_OR_MIXED | False | 3.634527680280586 | 6.9137442829677545 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | FALLING | 42.5 | 12.868832109870343 | HIGH |
| CNXN | 58.029 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.862198238801012 | [14.11, 24.13, 2.56] | [14.93, 5.33, 13.28] | 1.0624938734190283 | 2 | UNSTABLE | [16, 49, 16] | [16, 6, 21] | [28, 47, 6] | [14, 12, 16] | 1.5 | STABLE_OR_MIXED | False | 2.5578074535849593 | 8.573800059642204 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 40.0 | 11.614243259273094 | MEDIUM |
| NYAX | 58.022 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.842953829227538 | [16.75, 18.54, 3.19] | [3.44, 16.98, 5.29] | 3.1667565986879476 | 2 | UNSTABLE | [22, 16, 6] | [4, 5, 5] | [14, 13, 4] | [4, 4, 17] | 3.225 | DISSIPATING | False | 3.186841590260814 | 10.083382427656824 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | RISING | 27 | 16.835768245937125 | MEDIUM |
| TLN | 57.732 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.294516128795747 | [6.38, 6.39, 7.29] | [10.68, 10.91, 34.08] | 0.5854343137150776 | 3 | STABLE_3_OF_3 | [4, 12, 3] | [7, 18, 21] | [11, 6, 3] | [19, 9, 17] | 0.2875816993464052 | DISSIPATING | False | 7.294516128795747 | 11.358460982509582 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 32.0 | 23.460024521868796 | MEDIUM |
| TARS | 57.467 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.75073581150696 | [5.82, 5.89, 9.75] | [6.67, 30.56, 28.49] | 0.20675561616394783 | 3 | STABLE_3_OF_3 | [17, 16, 6] | [8, 23, 12] | [17, 5, 9] | [4, 27, 19] | 0.9035087719298245 | DISSIPATING | False | 9.75073581150696 | 11.556202290813927 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 36 | 25.059167034037465 | HIGH |
| AKAM | 57.182 | CANDIDATE | NO_TRADE | IRREGULAR | 18.41982001904674 | [13.36, 6.0, 14.14] | [13.34, 5.28, 5.39] | 2.4808292663919276 | 3 | STABLE_3_OF_3 | [10, 12, 12] | [7, 10, 8] | [16, 7, 13] | [11, 7, 9] | 1.4722222222222223 | STABLE_OR_MIXED | False | 14.143262278384672 | 12.424625505871242 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 34.0 | 18.77617445503659 | MEDIUM |
| CTSO | 56.859 | CANDIDATE | NO_TRADE | STABLE_RANGE | 21.374044551152437 | [96.41, 17.23, 41.5] | [18.97, 14.29, 7.31] | 2.905339745182618 | 3 | STABLE_3_OF_3 | [15, 4, 8] | [5, 8, 20] | [11, 7, 5] | [9, 6, 22] | 0.8888888888888888 | STABLE_OR_MIXED | False | 41.50485644770659 | 16.242260002278137 | CYCLE_TIMING | NO_TRADE | FALLING | MIXED | 36.5 | 29.666670163472496 | MEDIUM |

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
    "observations": 222,
    "positive_net_pct": 43.24324324324324,
    "average_net_pct": -1.608192630794662,
    "average_positive_pct": 4.018686397604059,
    "average_nonpositive_pct": -5.89533855719369,
    "benchmark_pairs": 222,
    "average_excess_pct": -0.7429101033379033,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 1408,
    "positive_net_pct": 51.06534090909091,
    "average_net_pct": 0.24081128785785283,
    "average_positive_pct": 6.619472916116481,
    "average_nonpositive_pct": -6.415585970078208,
    "benchmark_pairs": 1408,
    "average_excess_pct": 1.1362006054549376,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 159,
    "positive_net_pct": 47.79874213836478,
    "average_net_pct": -0.5765210907373384,
    "average_positive_pct": 5.01231865418195,
    "average_nonpositive_pct": -5.69401290536223,
    "benchmark_pairs": 159,
    "average_excess_pct": 0.2580136515837669,
    "worst_adverse_excursion_pct": -25.57142802647182
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 170,
    "positive_net_pct": 48.23529411764706,
    "average_net_pct": -2.0577756174490682,
    "average_positive_pct": 5.986719718291533,
    "average_nonpositive_pct": -9.553782634843715,
    "benchmark_pairs": 170,
    "average_excess_pct": -0.5286433042729471,
    "worst_adverse_excursion_pct": -95.51242232978043
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 1019,
    "positive_net_pct": 52.01177625122669,
    "average_net_pct": 1.1509903099009418,
    "average_positive_pct": 11.051475904042542,
    "average_nonpositive_pct": -9.579597348371136,
    "benchmark_pairs": 1019,
    "average_excess_pct": 2.860954829846195,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 125,
    "positive_net_pct": 53.6,
    "average_net_pct": 0.7317060495153287,
    "average_positive_pct": 7.86563520659365,
    "average_nonpositive_pct": -7.50921211469584,
    "benchmark_pairs": 125,
    "average_excess_pct": 2.2460760045111106,
    "worst_adverse_excursion_pct": -30.81636301420778
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "0-40",
    "observations": 52,
    "positive_net_pct": 55.76923076923077,
    "average_net_pct": -1.8357187726908823,
    "average_positive_pct": 6.288877106058543,
    "average_nonpositive_pct": -12.079774445896678,
    "benchmark_pairs": 52,
    "average_excess_pct": 0.6950218609225964,
    "worst_adverse_excursion_pct": -69.10112242914782
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "40-60",
    "observations": 292,
    "positive_net_pct": 45.89041095890411,
    "average_net_pct": 0.8225620641292326,
    "average_positive_pct": 18.44272478919751,
    "average_nonpositive_pct": -14.12112024700461,
    "benchmark_pairs": 292,
    "average_excess_pct": 3.3778869478801243,
    "worst_adverse_excursion_pct": -89.14473627454025
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "60-80",
    "observations": 47,
    "positive_net_pct": 42.5531914893617,
    "average_net_pct": -1.96932547765803,
    "average_positive_pct": 11.722052922989016,
    "average_nonpositive_pct": -12.111087255915104,
    "benchmark_pairs": 47,
    "average_excess_pct": 0.567678355105134,
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
- CCU: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- CLBR: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- KNRX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- RDIB: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SAGU: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- VECA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
