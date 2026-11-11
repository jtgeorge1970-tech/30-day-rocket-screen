# OFTS daily research

Market session: 2026-11-10
Selected: 147; refreshed: 123; refresh errors: 26
Qualified prediction cohorts saved: 23; current coverage: 123/147
Outcome counts: {'CORPORATE_ACTION_REVIEW': 22, 'INELIGIBLE_DATA': 1805, 'MATURE': 3971, 'MISSING_SESSIONS': 2, 'PENDING': 9525}
Cycle fingerprints saved: 130/179
Signal states: BUY=3, SELL=4, NO_TRADE=172
Cycle ledger: pending entries=3; open positions=34; closed trades=20; SPY pairs=20
Cycle-speed report card: READY; closed forward trades=20; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 11.194940444955614-68.3761930201991; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 20, '40_TO_49_999': 60, '50_TO_59_999': 41, '60_TO_69_999': 9, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=129
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=108; REVIEW=22; INSUFFICIENT=95
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| MWH | 68.376 | CANDIDATE | NO_TRADE | INSUFFICIENT | 11.152554385226521 | [11.38, 13.52, 15.21] | [18.33, 5.95, 9.76] | 1.385666278611575 | 3 | STABLE_3_OF_3 | [11, 17, 3] | [8, 17, 9] | [19, 5, 4] | [19, 5, 12] | 0.8194444444444445 | STABLE_OR_MIXED | False | 15.212715679159539 | 11.431672904891617 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 47.5 | 35.23344052246027 | HIGH |
| DXC | 64.650 | CANDIDATE | BUY | STABLE_RANGE | 15.46012038061787 | [10.68, 12.68, 46.85] | [28.49, 4.87, 12.32] | 1.0293825439823863 | 3 | STABLE_3_OF_3 | [6, 13, 17] | [12, 11, 15] | [14, 3, 22] | [21, 3, 16] | 0.9791666666666666 | STABLE_OR_MIXED | False | 46.84683492688584 | 10.682395098587056 | CYCLE_TIMING | NO_TRADE | RISING | MIXED | 33.5 | 15.563380759378632 | HIGH |
| SCYX | 63.790 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.556963660361335 | [22.32, 7.92, 4.51] | [51.26, 17.88, 18.25] | 0.4342075970797313 | 2 | UNSTABLE | [7, 19, 4] | [10, 16, 18] | [16, 9, 4] | [12, 24, 7] | 0.59375 | DISSIPATING | False | 4.509285866154467 | 14.214018946486583 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 25 | 27.6617157809988 | MEDIUM |
| LBTYB | 63.635 | CANDIDATE | BUY | STABLE_RANGE | 6.909092989834864 | [4.07, 5.65, 6.91] | [4.67, 5.37, 3.68] | 1.2089660041389128 | 2 | WATCH_2_OF_3 | [2, 4, 22] | [3, 7, 16] | [2, 21, 5] | [6, 18, 2] | 0.7023809523809523 | STABLE_OR_MIXED | False | 6.909092989834864 | 9.267142068144333 | WATCH | NO_TRADE | MIXED | MIXED | 25.5 | 14.757276465457124 | MEDIUM |
| EPM | 63.618 | CANDIDATE | NO_TRADE | IRREGULAR | 13.283207271252762 | [6.34, 2.81, 15.65] | [9.43, 6.29, 12.28] | 0.6720088429954724 | 2 | WATCH_2_OF_3 | [6, 2, 25] | [19, 2, 14] | [3, 5, 28] | [10, 5, 14] | 0.4642857142857143 | DISSIPATING | False | 15.652172590999713 | 8.955807929783713 | WATCH | NO_TRADE | RISING | MIXED | 32.0 | 14.754093715305938 | MEDIUM |
| MESO | 62.143 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.364017811603918 | [5.0, 7.36, 27.61] | [9.25, 4.97, 10.48] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [13, 8, 6] | [5, 6, 11] | [14, 9, 4] | [6, 6, 10] | 1.4166666666666665 | DISSIPATING | False | 27.60586658826034 | 11.489035306119467 | WATCH | NO_TRADE | FALLING | MIXED | 16.0 | 19.704195329980422 | MEDIUM |
| SPGI | 62.036 | CANDIDATE | NO_TRADE | INSUFFICIENT | 14.272715050622754 | [7.88, 4.37, 24.7] | [6.24, 4.72, 4.3] | 1.6695164333270074 | 2 | WATCH_2_OF_3 | [11, 4, 43] | [8, 7, 13] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 24.70293218258719 | 7.474272944170579 | WATCH | NO_TRADE | INSUFFICIENT | FALLING | 34.5 | 12.047373424014074 | MEDIUM |
| CRNC | 60.217 | CANDIDATE | NO_TRADE | IRREGULAR | 9.017417722756193 | [6.47, 19.56, 9.02] | [12.68, 4.55, 3.82] | 1.9838325962779013 | 3 | STABLE_3_OF_3 | [3, 17, 14] | [15, 4, 4] | [7, 24, 3] | [12, 4, 2] | 2.625 | DISSIPATING | False | 9.017417722756193 | 11.871152514095101 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 17 | 20.135473477171224 | MEDIUM |
| CTSO | 60.025 | CANDIDATE | NO_TRADE | STABLE_RANGE | 21.374044551152437 | [7.31, 96.41, 17.23] | [11.11, 18.97, 14.29] | 1.2058164959760302 | 3 | STABLE_3_OF_3 | [20, 15, 4] | [6, 5, 8] | [11, 7, 5] | [9, 6, 22] | 1.6388888888888888 | DISSIPATING | False | 17.225951164832164 | 15.73363267524421 | CYCLE_TIMING | NO_TRADE | FALLING | MIXED | 36.5 | 29.666670163472496 | MEDIUM |
| ASO | 59.747 | CANDIDATE | NO_TRADE | INSUFFICIENT | 13.565755154320215 | [3.23, 29.86, 29.11] | [9.9, 8.24, 5.36] | 3.5313266240759957 | 2 | WATCH_2_OF_3 | [7, 16, 29] | [21, 4, 9] | [8, 24, 19] | [12, 9, 7] | 1.9444444444444444 | DISSIPATING | False | 29.111809298613878 | 9.978998514611185 | WATCH | NO_TRADE | INSUFFICIENT | MIXED | 35.5 | 17.894552642278793 | HIGH |
| OBE | 59.397 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.994571511853363 | [18.18, 4.06, 4.99] | [33.37, 7.27, 13.97] | 0.357473074980304 | 1 | UNSTABLE | [26, 4, 10] | [14, 5, 10] | [21, 17, 9] | [6, 14, 3] | 1.9166666666666667 | DISSIPATING | False | 4.994571511853363 | 13.04486484045032 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 26 | 21.37633118736948 | HIGH |
| ATGL | 59.092 | CANDIDATE | BUY | STABLE_RANGE | 14.583338714307992 | [11.36, 145.59, 6.08] | [32.71, 4.02, 6.46] | 1.75940159940304 | 3 | STABLE_3_OF_3 | [3, 9, 4] | [5, 4, 9] | [2, 11, 4] | [7, 9, 3] | 0.6857142857142857 | STABLE_OR_MIXED | False | 6.0773500457816265 | 22.074596180542123 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 21 | 32.06849916938487 | MEDIUM |
| METCB | 59.034 | CANDIDATE | NO_TRADE | INSUFFICIENT | 17.857141716747872 | [6.15, 6.24, 18.52] | [15.95, 7.19, 4.68] | 0.8675568786153617 | 3 | STABLE_3_OF_3 | [6, 6, 13] | [6, 4, 11] | [3, 13, 11] | [8, 11, 6] | 1.1875 | STABLE_OR_MIXED | False | 18.518519920156272 | 11.483925374313214 | CYCLE_TIMING | NO_TRADE | FALLING | INSUFFICIENT | 53 | 41.58882283911626 | HIGH |
| AKAM | 59.020 | CANDIDATE | NO_TRADE | IRREGULAR | 18.41982001904674 | [13.36, 6.0, 14.14] | [13.34, 5.28, 5.39] | 2.4808292663919276 | 3 | STABLE_3_OF_3 | [10, 12, 12] | [7, 10, 8] | [16, 7, 13] | [11, 7, 9] | 1.4722222222222223 | STABLE_OR_MIXED | False | 14.143262278384672 | 12.245576200899507 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 34.0 | 18.77617445503659 | MEDIUM |
| TT | 58.029 | CANDIDATE | NO_TRADE | INSUFFICIENT | 5.625560811137554 | [13.36, 3.07, 3.63] | [6.14, 3.24, 9.92] | 0.592033700423493 | 1 | UNSTABLE | [44, 6, 4] | [3, 21, 11] | [21, 6, 9] | [18, 8, 33] | 0.5227272727272727 | DISSIPATING | False | 3.634527680280586 | 8.16102153991272 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | INSUFFICIENT | 54 | 13.381161832283905 | MEDIUM |
| TLN | 57.832 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.294516128795747 | [6.38, 6.39, 7.29] | [10.68, 10.91, 34.08] | 0.5854343137150776 | 3 | STABLE_3_OF_3 | [4, 12, 3] | [7, 18, 21] | [11, 6, 3] | [19, 9, 17] | 0.2875816993464052 | DISSIPATING | False | 7.294516128795747 | 11.330191176271354 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 32.0 | 23.460024521868796 | MEDIUM |
| DUOT | 57.446 | CANDIDATE | NO_TRADE | STABLE_RANGE | 10.427352879635944 | [4.41, 16.48, 10.43] | [3.67, 5.11, 17.9] | 2.0404408123277755 | 2 | WATCH_2_OF_3 | [8, 11, 6] | [7, 7, 12] | [12, 5, 9] | [4, 6, 14] | 1.3214285714285714 | STABLE_OR_MIXED | False | 10.427352879635944 | 13.53140165446076 | WATCH | NO_TRADE | FALLING | MIXED | 21 | 29.75700752799146 | MEDIUM |
| IMTX | 57.287 | CANDIDATE | NO_TRADE | DOWNTREND | 14.264487896377975 | [5.4, 4.54, 14.26] | [12.82, 3.5, 11.81] | 0.4573113544487047 | 2 | WATCH_2_OF_3 | [17, 11, 4] | [4, 4, 18] | [13, 3, 14] | [4, 10, 24] | 2.025 | DISSIPATING | False | 14.264487896377975 | 9.733409144763202 | WATCH | NO_TRADE | FALLING | FALLING | 32 | 23.73424207174944 | MEDIUM |
| NYAX | 57.187 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.842953829227538 | [16.75, 18.54, 3.19] | [16.98, 5.29, 2.94] | 3.1667565986879476 | 2 | UNSTABLE | [10, 16, 6] | [5, 5, 12] | [14, 13, 4] | [4, 12, 5] | 2.3 | DISSIPATING | False | 3.186841590260814 | 8.997027166484536 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 24 | 16.651655201817416 | MEDIUM |
| CNXN | 56.698 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.862198238801012 | [14.11, 24.13, 2.56] | [14.93, 5.33, 13.28] | 1.0624938734190283 | 2 | UNSTABLE | [16, 49, 16] | [16, 6, 21] | [28, 47, 6] | [14, 12, 16] | 1.5 | STABLE_OR_MIXED | False | 2.5578074535849593 | 8.573800059642204 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 40.0 | 11.614243259273094 | MEDIUM |
| LINE | 56.612 | CANDIDATE | SELL | INSUFFICIENT | 5.031441808362825 | [3.53, 2.97, 19.39] | [3.41, 8.28, 5.88] | 0.6003081996433184 | 1 | UNSTABLE | [21, 15, 25] | [13, 8, 11] | [24, 15, 12] | [13, 9, 10] | 1.7045454545454546 | DISSIPATING | True | 19.385907254860356 | 7.802350431610048 | TOO_SMALL | NO_TRADE | FALLING | INSUFFICIENT | 25 | 11.653946580632502 | MEDIUM |
| HELP | 56.527 | CANDIDATE | NO_TRADE | INSUFFICIENT | 7.065753647476858 | [6.45, 3.7, 7.07] | [6.86, 10.83, 12.27] | 0.5958574060297749 | 2 | WATCH_2_OF_3 | [4, 3, 6] | [3, 3, 13] | [2, 5, 9] | [3, 13, 5] | 1.1666666666666665 | DISSIPATING | False | 7.065753647476858 | 14.347703499422485 | FADING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 40 | 27.760661644802614 | HIGH |
| HLIT | 56.117 | CANDIDATE | NO_TRADE | DOWNTREND | 9.296026534869107 | [6.82, 10.69, 7.46] | [3.58, 3.36, 3.29] | 2.2215823222141275 | 3 | STABLE_3_OF_3 | [16, 9, 7] | [8, 11, 2] | [11, 7, 9] | [8, 6, 11] | 1.125 | STABLE_OR_MIXED | False | 7.462686425532894 | 10.551179968059344 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 45 | 17.917578566909686 | MEDIUM |
| MTG | 55.984 | CANDIDATE | NO_TRADE | INSUFFICIENT | 4.217533705841414 | [7.86, 4.22, 7.47] | [5.16, 13.52, 26.59] | 0.5523774378614623 | 2 | WATCH_2_OF_3 | [24, 8, 12] | [11, 41, 88] | [82, 8, 7] | [9, 19, 51] | 0.35686777920410784 | DISSIPATING | False | 7.469794783670269 | 7.634594825317911 | TOO_SMALL | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 51 | 13.159246197205187 | HIGH |
| TARS | 55.788 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.75073581150696 | [5.82, 5.89, 9.75] | [6.67, 30.56, 28.49] | 0.20675561616394783 | 3 | STABLE_3_OF_3 | [17, 16, 6] | [8, 23, 12] | [17, 5, 9] | [4, 27, 19] | 0.9035087719298245 | DISSIPATING | False | 9.75073581150696 | 11.159216719175015 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 34.0 | 24.901612451689736 | HIGH |

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
    "observations": 198,
    "positive_net_pct": 42.92929292929293,
    "average_net_pct": -1.8270062282654984,
    "average_positive_pct": 3.8370545542437564,
    "average_nonpositive_pct": -6.087582923073348,
    "benchmark_pairs": 198,
    "average_excess_pct": -0.7610331088010832,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 1258,
    "positive_net_pct": 50.55643879173291,
    "average_net_pct": 0.20271003567432577,
    "average_positive_pct": 6.704585901771403,
    "average_nonpositive_pct": -6.445510303293102,
    "benchmark_pairs": 1258,
    "average_excess_pct": 1.326860615232223,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 144,
    "positive_net_pct": 47.916666666666664,
    "average_net_pct": -0.7002278191061874,
    "average_positive_pct": 5.043925346460971,
    "average_nonpositive_pct": -5.984848731427975,
    "benchmark_pairs": 144,
    "average_excess_pct": 0.35926767386099195,
    "worst_adverse_excursion_pct": -25.57142802647182
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 146,
    "positive_net_pct": 47.26027397260274,
    "average_net_pct": -2.349036888808238,
    "average_positive_pct": 5.482980291419314,
    "average_nonpositive_pct": -9.367337998362794,
    "benchmark_pairs": 146,
    "average_excess_pct": -0.7350734484724322,
    "worst_adverse_excursion_pct": -95.51242232978043
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 877,
    "positive_net_pct": 52.451539338654506,
    "average_net_pct": 1.0432947336030847,
    "average_positive_pct": 10.954674861344472,
    "average_nonpositive_pct": -9.890122193881405,
    "benchmark_pairs": 877,
    "average_excess_pct": 2.8551095067850776,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 107,
    "positive_net_pct": 53.271028037383175,
    "average_net_pct": 1.1656630767623462,
    "average_positive_pct": 8.315359073098191,
    "average_nonpositive_pct": -6.984990359060523,
    "benchmark_pairs": 107,
    "average_excess_pct": 2.7501442288589337,
    "worst_adverse_excursion_pct": -30.81636301420778
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "0-40",
    "observations": 27,
    "positive_net_pct": 48.148148148148145,
    "average_net_pct": -3.1542765728869275,
    "average_positive_pct": 5.59966596985431,
    "average_nonpositive_pct": -11.282937505432361,
    "benchmark_pairs": 27,
    "average_excess_pct": 0.24942869950817914,
    "worst_adverse_excursion_pct": -69.10112242914782
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "40-60",
    "observations": 150,
    "positive_net_pct": 45.333333333333336,
    "average_net_pct": -0.14291772525254806,
    "average_positive_pct": 17.152925910465783,
    "average_nonpositive_pct": -14.485812447555551,
    "benchmark_pairs": 150,
    "average_excess_pct": 3.2575243804203997,
    "worst_adverse_excursion_pct": -89.14473627454025
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 20,
    "score_band": "60-80",
    "observations": 24,
    "positive_net_pct": 41.666666666666664,
    "average_net_pct": -3.4646047650380987,
    "average_positive_pct": 9.990844416623268,
    "average_nonpositive_pct": -13.07563989479622,
    "benchmark_pairs": 24,
    "average_excess_pct": -0.06370377654484856,
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
- CCXI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- RDIB: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TCBI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
