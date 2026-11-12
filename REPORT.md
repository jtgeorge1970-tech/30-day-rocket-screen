# OFTS daily research

Market session: 2026-11-11
Selected: 149; refreshed: 125; refresh errors: 25
Qualified prediction cohorts saved: 24; current coverage: 125/149
Outcome counts: {'CORPORATE_ACTION_REVIEW': 25, 'INELIGIBLE_DATA': 1950, 'MATURE': 4316, 'MISSING_SESSIONS': 4, 'PENDING': 9775}
Cycle fingerprints saved: 134/181
Signal states: BUY=5, SELL=2, NO_TRADE=174
Cycle ledger: pending entries=2; open positions=37; closed trades=20; SPY pairs=20
Cycle-speed report card: READY; closed forward trades=20; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 12.711807464839426-68.3899852324604; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 24, '40_TO_49_999': 57, '50_TO_59_999': 46, '60_TO_69_999': 7, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=131
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=112; REVIEW=22; INSUFFICIENT=101
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| MWH | 68.390 | CANDIDATE | NO_TRADE | INSUFFICIENT | 11.152554385226521 | [11.38, 13.52, 15.21] | [18.33, 5.95, 9.76] | 1.385666278611575 | 3 | STABLE_3_OF_3 | [11, 17, 3] | [8, 17, 9] | [19, 5, 4] | [19, 5, 12] | 0.8194444444444445 | STABLE_OR_MIXED | False | 15.212715679159539 | 11.431672904891617 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 47.5 | 35.23344052246027 | HIGH |
| MESO | 62.375 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.364017811603918 | [5.0, 7.36, 27.61] | [9.25, 4.97, 10.48] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [13, 8, 6] | [5, 6, 11] | [14, 9, 4] | [6, 6, 10] | 1.4166666666666665 | DISSIPATING | False | 27.60586658826034 | 11.654384747299156 | WATCH | NO_TRADE | FALLING | MIXED | 16.0 | 19.704195329980422 | MEDIUM |
| SPGI | 61.960 | CANDIDATE | NO_TRADE | INSUFFICIENT | 14.272715050622754 | [7.88, 4.37, 24.7] | [6.24, 4.72, 4.3] | 1.6695164333270074 | 2 | WATCH_2_OF_3 | [11, 4, 43] | [8, 7, 13] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 24.70293218258719 | 7.474272944170579 | WATCH | NO_TRADE | INSUFFICIENT | FALLING | 34.5 | 12.047373424014074 | MEDIUM |
| BFAM | 61.209 | CANDIDATE | NO_TRADE | INSUFFICIENT | 10.05678951147475 | [11.66, 10.06, 5.6] | [6.43, 6.86, 5.1] | 1.5639209490413801 | 3 | STABLE_3_OF_3 | [17, 6, 7] | [22, 12, 5] | [7, 15, 9] | [18, 17, 7] | 0.5563725490196079 | STABLE_OR_MIXED | False | 5.597294230442529 | 10.06680558673672 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 67.5 | 19.296013785096644 | HIGH |
| DUOT | 61.144 | CANDIDATE | BUY | DOWNTREND | 10.427352879635944 | [4.41, 16.48, 10.43] | [3.67, 5.11, 17.9] | 2.0404408123277755 | 2 | WATCH_2_OF_3 | [8, 11, 6] | [7, 7, 12] | [12, 5, 9] | [4, 6, 14] | 1.3214285714285714 | STABLE_OR_MIXED | False | 10.427352879635944 | 13.48728896541379 | WATCH | NO_TRADE | FALLING | FALLING | 21.0 | 29.401851767193875 | MEDIUM |
| CRNC | 60.257 | CANDIDATE | NO_TRADE | IRREGULAR | 9.017417722756193 | [6.47, 19.56, 9.02] | [12.68, 4.55, 3.82] | 1.9838325962779013 | 3 | STABLE_3_OF_3 | [3, 17, 14] | [15, 4, 4] | [7, 24, 3] | [12, 4, 2] | 2.625 | DISSIPATING | False | 9.017417722756193 | 11.844600527859972 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 17 | 20.135473477171224 | MEDIUM |
| OBE | 60.135 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.994571511853363 | [18.18, 4.06, 4.99] | [33.37, 7.27, 13.97] | 0.357473074980304 | 1 | UNSTABLE | [26, 4, 10] | [14, 5, 10] | [21, 17, 9] | [6, 14, 3] | 1.9166666666666667 | DISSIPATING | False | 4.994571511853363 | 13.255222517268619 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 26 | 21.37633118736948 | HIGH |
| ASO | 59.766 | CANDIDATE | NO_TRADE | INSUFFICIENT | 13.565755154320215 | [3.23, 29.86, 29.11] | [9.9, 8.24, 5.36] | 3.5313266240759957 | 2 | WATCH_2_OF_3 | [7, 16, 29] | [19, 4, 9] | [8, 24, 19] | [12, 9, 7] | 1.9444444444444444 | DISSIPATING | False | 29.111809298613878 | 9.329632020806041 | WATCH | NO_TRADE | INSUFFICIENT | MIXED | 35.5 | 17.894552642278793 | HIGH |
| SCYX | 59.696 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.556963660361335 | [22.32, 7.92, 4.51] | [51.26, 17.88, 18.25] | 0.4342075970797313 | 2 | UNSTABLE | [7, 19, 4] | [10, 16, 18] | [16, 9, 4] | [12, 24, 7] | 0.59375 | DISSIPATING | False | 4.509285866154467 | 14.214018946486583 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 25 | 27.926120670386638 | MEDIUM |
| TARS | 59.557 | CANDIDATE | BUY | INSUFFICIENT | 9.75073581150696 | [5.82, 5.89, 9.75] | [6.67, 30.56, 28.49] | 0.20675561616394783 | 3 | STABLE_3_OF_3 | [17, 16, 6] | [8, 23, 12] | [17, 5, 9] | [4, 27, 19] | 0.9035087719298245 | DISSIPATING | False | 9.75073581150696 | 11.354996337388563 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 36 | 25.059167034037465 | HIGH |
| ESNT | 59.523 | CANDIDATE | NO_TRADE | INSUFFICIENT | 8.309903114311389 | [9.81, 6.74, 8.31] | [5.74, 6.23, 3.06] | 1.4468196786663896 | 3 | STABLE_3_OF_3 | [24, 8, 11] | [8, 20, 6] | [8, 7, 12] | [10, 17, 21] | 0.9227941176470589 | STABLE_OR_MIXED | False | 8.309903114311389 | 7.497705483335897 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 53 | 12.641914967787642 | HIGH |
| SCI | 59.236 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.257798466890627 | [10.21, 3.31, 2.77] | [11.65, 3.67, 3.16] | 0.9033699635757841 | 1 | UNSTABLE | [29, 7, 2] | [11, 18, 11] | [18, 3, 4] | [20, 15, 18] | 0.4292929292929293 | STABLE_OR_MIXED | False | 2.7685370785236696 | 7.250381153445083 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 51 | 10.816676294127237 | HIGH |
| METCB | 59.026 | CANDIDATE | NO_TRADE | INSUFFICIENT | 17.857141716747872 | [6.15, 6.24, 18.52] | [15.95, 7.19, 4.68] | 0.8675568786153617 | 3 | STABLE_3_OF_3 | [6, 6, 13] | [6, 4, 11] | [3, 13, 11] | [8, 11, 6] | 1.1875 | STABLE_OR_MIXED | False | 18.518519920156272 | 11.475315459512194 | CYCLE_TIMING | NO_TRADE | FALLING | INSUFFICIENT | 53 | 41.58882283911626 | HIGH |
| ATGL | 58.831 | CANDIDATE | NO_TRADE | STABLE_RANGE | 14.583338714307992 | [145.59, 6.08, 18.17] | [4.02, 6.46, 11.36] | 2.8133257639351634 | 3 | STABLE_3_OF_3 | [9, 4, 4] | [4, 9, 3] | [2, 11, 4] | [7, 9, 3] | 0.7857142857142857 | STABLE_OR_MIXED | False | 18.17072933873267 | 22.0029523430569 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 21 | 32.06849916938487 | MEDIUM |
| TT | 58.248 | CANDIDATE | NO_TRADE | STABLE_RANGE | 5.625560811137554 | [13.36, 3.07, 3.63] | [3.24, 9.92, 2.73] | 1.120909955921715 | 1 | UNSTABLE | [33, 6, 4] | [18, 11, 11] | [21, 6, 9] | [8, 15, 18] | 0.5727272727272728 | STABLE_OR_MIXED | False | 3.634527680280586 | 6.9137442829677545 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | FALLING | 42.5 | 12.868832109870343 | HIGH |
| NYAX | 58.145 | CANDIDATE | BUY | STABLE_RANGE | 6.842953829227538 | [16.75, 18.54, 3.19] | [16.98, 5.29, 2.94] | 3.1667565986879476 | 2 | UNSTABLE | [10, 16, 6] | [5, 5, 12] | [14, 13, 4] | [4, 12, 5] | 2.3 | DISSIPATING | False | 3.186841590260814 | 9.218835401299751 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | RISING | 23.0 | 16.554543782118735 | MEDIUM |
| IMTX | 57.863 | CANDIDATE | NO_TRADE | DOWNTREND | 14.264487896377975 | [5.4, 4.54, 14.26] | [12.82, 3.5, 11.81] | 0.4573113544487047 | 2 | WATCH_2_OF_3 | [17, 11, 4] | [4, 4, 18] | [13, 3, 14] | [4, 10, 24] | 2.025 | DISSIPATING | False | 14.264487896377975 | 9.695312475976822 | WATCH | NO_TRADE | FALLING | FALLING | 32 | 23.73424207174944 | MEDIUM |
| TLN | 57.707 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.294516128795747 | [6.38, 6.39, 7.29] | [10.68, 10.91, 34.08] | 0.5854343137150776 | 3 | STABLE_3_OF_3 | [4, 12, 3] | [7, 18, 21] | [11, 6, 3] | [19, 9, 17] | 0.2875816993464052 | DISSIPATING | False | 7.294516128795747 | 11.24665100095067 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 32.0 | 23.460024521868796 | MEDIUM |
| DXC | 57.365 | CANDIDATE | NO_TRADE | STABLE_RANGE | 15.46012038061787 | [10.68, 12.68, 46.85] | [28.49, 4.87, 12.32] | 1.0293825439823863 | 3 | STABLE_3_OF_3 | [6, 13, 17] | [12, 11, 15] | [14, 3, 22] | [21, 3, 16] | 0.9791666666666666 | STABLE_OR_MIXED | False | 46.84683492688584 | 10.682395098587056 | CYCLE_TIMING | NO_TRADE | RISING | MIXED | 29.0 | 15.364983182423341 | MEDIUM |
| AKAM | 57.198 | CANDIDATE | NO_TRADE | IRREGULAR | 18.41982001904674 | [13.36, 6.0, 14.14] | [13.34, 5.28, 5.39] | 2.4808292663919276 | 3 | STABLE_3_OF_3 | [10, 12, 12] | [7, 10, 8] | [16, 7, 13] | [11, 7, 9] | 1.4722222222222223 | STABLE_OR_MIXED | False | 14.143262278384672 | 12.437195038121656 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 34.0 | 18.77617445503659 | MEDIUM |
| CNXN | 57.027 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.862198238801012 | [14.11, 24.13, 2.56] | [14.93, 5.33, 13.28] | 1.0624938734190283 | 2 | UNSTABLE | [16, 49, 16] | [16, 6, 21] | [28, 47, 6] | [14, 12, 16] | 1.5 | STABLE_OR_MIXED | False | 2.5578074535849593 | 8.573800059642204 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 40.0 | 11.614243259273094 | MEDIUM |
| CTSO | 56.796 | CANDIDATE | NO_TRADE | STABLE_RANGE | 21.374044551152437 | [96.41, 17.23, 41.5] | [18.97, 14.29, 7.31] | 2.905339745182618 | 3 | STABLE_3_OF_3 | [15, 4, 8] | [5, 8, 20] | [11, 7, 5] | [9, 6, 22] | 0.8888888888888888 | STABLE_OR_MIXED | False | 41.50485644770659 | 16.11243440600704 | CYCLE_TIMING | NO_TRADE | FALLING | MIXED | 36.5 | 29.666670163472496 | MEDIUM |
| MMYT | 56.758 | CANDIDATE | NO_TRADE | INSUFFICIENT | 11.928170504414215 | [6.14, 28.52, 7.86] | [4.17, 14.16, 50.28] | 0.5553361330180799 | 3 | STABLE_3_OF_3 | [10, 10, 51] | [7, 7, 26] | [3, 52, 14] | [4, 15, 26] | 1.180952380952381 | DISSIPATING | False | 7.862577660579895 | 14.390041637393708 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 36 | 23.595014950111683 | HIGH |
| LINE | 56.707 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.031441808362825 | [3.53, 2.97, 19.39] | [3.41, 8.28, 5.88] | 0.6003081996433184 | 1 | UNSTABLE | [21, 15, 25] | [13, 8, 11] | [24, 15, 12] | [13, 9, 10] | 1.7045454545454546 | DISSIPATING | True | 19.385907254860356 | 7.802350431610048 | TOO_SMALL | NO_TRADE | FALLING | INSUFFICIENT | 25 | 11.653946580632502 | MEDIUM |
| HELP | 56.510 | CANDIDATE | NO_TRADE | INSUFFICIENT | 7.065753647476858 | [6.45, 3.7, 7.07] | [6.86, 10.83, 12.27] | 0.5958574060297749 | 2 | WATCH_2_OF_3 | [4, 3, 6] | [3, 3, 13] | [2, 5, 9] | [3, 13, 5] | 1.1666666666666665 | DISSIPATING | False | 7.065753647476858 | 14.347703499422485 | FADING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 40 | 27.760661644802614 | HIGH |

## Experimental recent-swing review shortlist (NOT BUY signals)
Count: 0 of 104 scored CANDIDATE names
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
    "observations": 211,
    "positive_net_pct": 42.654028436018955,
    "average_net_pct": -1.692504449720275,
    "average_positive_pct": 4.053785417655451,
    "average_nonpositive_pct": -5.966604351074125,
    "benchmark_pairs": 211,
    "average_excess_pct": -0.6343289643540395,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 1330,
    "positive_net_pct": 50.225563909774436,
    "average_net_pct": 0.14083958019251602,
    "average_positive_pct": 6.710607571476195,
    "average_nonpositive_pct": -6.488473136087683,
    "benchmark_pairs": 1330,
    "average_excess_pct": 1.2549892482485605,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 150,
    "positive_net_pct": 47.333333333333336,
    "average_net_pct": -0.7639311621790976,
    "average_positive_pct": 4.969777386154542,
    "average_nonpositive_pct": -5.9170109967574325,
    "benchmark_pairs": 150,
    "average_excess_pct": 0.2907609718642302,
    "worst_adverse_excursion_pct": -25.57142802647182
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 156,
    "positive_net_pct": 46.794871794871796,
    "average_net_pct": -2.1047443474977965,
    "average_positive_pct": 6.023781481297815,
    "average_nonpositive_pct": -9.25392971499273,
    "benchmark_pairs": 156,
    "average_excess_pct": -0.5065435125311366,
    "worst_adverse_excursion_pct": -95.51242232978043
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 952,
    "positive_net_pct": 51.99579831932773,
    "average_net_pct": 1.06680999869611,
    "average_positive_pct": 11.02906870871161,
    "average_nonpositive_pct": -9.723820332721107,
    "benchmark_pairs": 952,
    "average_excess_pct": 2.8436656350657463,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 117,
    "positive_net_pct": 52.99145299145299,
    "average_net_pct": 0.9654808046112348,
    "average_positive_pct": 8.241723008186034,
    "average_nonpositive_pct": -7.23682858850945,
    "benchmark_pairs": 117,
    "average_excess_pct": 2.531465003244621,
    "worst_adverse_excursion_pct": -30.81636301420778
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "0-40",
    "observations": 41,
    "positive_net_pct": 53.65853658536585,
    "average_net_pct": -1.1136106512639181,
    "average_positive_pct": 7.044184637861738,
    "average_nonpositive_pct": -10.559478880777833,
    "benchmark_pairs": 41,
    "average_excess_pct": 1.483131826664957,
    "worst_adverse_excursion_pct": -69.10112242914782
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "40-60",
    "observations": 221,
    "positive_net_pct": 46.15384615384615,
    "average_net_pct": 0.6263694652856006,
    "average_positive_pct": 17.785230227169077,
    "average_nonpositive_pct": -14.081225473471655,
    "benchmark_pairs": 221,
    "average_excess_pct": 3.268626339229598,
    "worst_adverse_excursion_pct": -89.14473627454025
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "60-80",
    "observations": 36,
    "positive_net_pct": 44.44444444444444,
    "average_net_pct": -1.8002749965421272,
    "average_positive_pct": 11.730664033815307,
    "average_nonpositive_pct": -12.625026220828076,
    "benchmark_pairs": 36,
    "average_excess_pct": 0.8138113586537536,
    "worst_adverse_excursion_pct": -47.09677302750536
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
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
