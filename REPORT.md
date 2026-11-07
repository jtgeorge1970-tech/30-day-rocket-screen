# OFTS daily research

Market session: 2026-11-06
Selected: 146; refreshed: 125; refresh errors: 21
Qualified prediction cohorts saved: 21; current coverage: 125/146
Outcome counts: {'CORPORATE_ACTION_REVIEW': 15, 'INELIGIBLE_DATA': 1565, 'MATURE': 3269, 'MISSING_SESSIONS': 2, 'PENDING': 9009}
Cycle fingerprints saved: 127/172
Signal states: BUY=2, SELL=3, NO_TRADE=167
Cycle ledger: pending entries=1; open positions=28; closed trades=19; SPY pairs=19
Cycle-speed report card: READY; closed forward trades=19; groups=['MEDIUM_11_TO_25', 'SLOW_OVER_25']
Score scale: theoretical 0-100; observed 13.32078622571862-68.21900290616671; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 14, '40_TO_49_999': 53, '50_TO_59_999': 53, '60_TO_69_999': 7, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=127
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=102; REVIEW=25; INSUFFICIENT=85
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| MWH | 68.219 | CANDIDATE | NO_TRADE | INSUFFICIENT | 11.152554385226521 | [11.38, 13.52, 15.21] | [18.33, 5.95, 9.76] | 1.385666278611575 | 3 | STABLE_3_OF_3 | [11, 17, 3] | [8, 17, 9] | [19, 5, 4] | [19, 5, 12] | 0.8194444444444445 | STABLE_OR_MIXED | False | 15.212715679159539 | 11.431672904891617 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 47.5 | 35.23344052246027 | HIGH |
| AKAM | 67.588 | CANDIDATE | NO_TRADE | IRREGULAR | 18.41982001904674 | [13.36, 6.0, 14.14] | [13.34, 5.28, 5.39] | 2.4808292663919276 | 3 | STABLE_3_OF_3 | [10, 12, 12] | [7, 10, 8] | [16, 7, 13] | [11, 7, 9] | 1.4722222222222223 | STABLE_OR_MIXED | False | 14.143262278384672 | 12.702788071512776 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 28 | 16.858607095784766 | HIGH |
| PPHC | 65.732 | CANDIDATE | SELL | STABLE_RANGE | 13.656787440563512 | [23.1, 9.01, 31.32] | [9.15, 9.69, 7.52] | 2.5232700232596494 | 3 | STABLE_3_OF_3 | [11, 15, 18] | [6, 3, 7] | [7, 17, 15] | [5, 3, 4] | 3.125 | DISSIPATING | False | 31.321543563119892 | 12.348426052933233 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 33.5 | 25.462008218832032 | HIGH |
| TBI | 63.540 | CANDIDATE | NO_TRADE | STABLE_RANGE | 11.026203555747681 | [3.04, 2.92, 21.1] | [9.15, 8.46, 11.19] | 0.33244085473662105 | 1 | UNSTABLE | [7, 5, 17] | [3, 17, 6] | [3, 10, 11] | [18, 5, 8] | 1.2083333333333335 | DISSIPATING | False | 21.104298742764648 | 13.735466001925433 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 23.0 | 18.032783467976866 | HIGH |
| SPGI | 61.194 | CANDIDATE | NO_TRADE | INSUFFICIENT | 14.272715050622754 | [7.88, 4.37, 24.7] | [6.24, 4.72, 4.3] | 1.6695164333270074 | 2 | WATCH_2_OF_3 | [11, 4, 43] | [8, 7, 13] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 24.70293218258719 | 7.343749247475079 | WATCH | NO_TRADE | INSUFFICIENT | FALLING | 35 | 11.723543952355413 | MEDIUM |
| EPM | 60.372 | CANDIDATE | NO_TRADE | IRREGULAR | 5.7377058257448095 | [6.34, 2.81, 15.65] | [9.43, 6.29, 12.28] | 0.6720088429954724 | 2 | WATCH_2_OF_3 | [6, 2, 25] | [19, 2, 14] | [14, 3, 5] | [18, 10, 5] | 0.4642857142857143 | DISSIPATING | False | 15.652172590999713 | 8.906958041485016 | WATCH | NO_TRADE | RISING | MIXED | 26.5 | 12.793734185315609 | MEDIUM |
| LBTYB | 60.109 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.909092989834864 | [4.07, 5.65, 6.91] | [4.67, 5.37, 3.68] | 1.2089660041389128 | 2 | WATCH_2_OF_3 | [2, 4, 22] | [3, 7, 16] | [2, 2, 21] | [5, 6, 18] | 0.45238095238095233 | STABLE_OR_MIXED | False | 6.909092989834864 | 9.303102477694548 | WATCH | NO_TRADE | MIXED | MIXED | 24.5 | 13.250001271565747 | MEDIUM |
| SCYX | 59.714 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.556963660361335 | [22.32, 7.92, 4.51] | [51.26, 17.88, 18.25] | 0.4342075970797313 | 2 | UNSTABLE | [7, 19, 4] | [10, 16, 18] | [16, 9, 4] | [12, 24, 7] | 0.59375 | DISSIPATING | False | 4.509285866154467 | 14.214018946486583 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 25 | 27.926120670386638 | MEDIUM |
| MESO | 59.451 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.364017811603918 | [5.0, 7.36, 27.61] | [9.25, 4.97, 10.48] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [13, 8, 6] | [5, 6, 11] | [14, 9, 4] | [6, 6, 10] | 1.4166666666666665 | DISSIPATING | False | 27.60586658826034 | 11.572154548619979 | WATCH | NO_TRADE | FALLING | MIXED | 17.0 | 20.062944005361583 | MEDIUM |
| ASO | 59.091 | CANDIDATE | NO_TRADE | INSUFFICIENT | 13.565755154320215 | [3.23, 29.86, 29.11] | [8.24, 2.66, 5.36] | 5.426943421325845 | 2 | WATCH_2_OF_3 | [7, 16, 29] | [4, 5, 4] | [8, 24, 19] | [5, 4, 7] | 3.9 | DISSIPATING | False | 29.111809298613878 | 8.305518891736162 | WATCH | NO_TRADE | INSUFFICIENT | MIXED | 33.0 | 16.886489455764362 | HIGH |
| METCB | 59.009 | CANDIDATE | NO_TRADE | INSUFFICIENT | 17.857141716747872 | [6.15, 6.24, 18.52] | [15.95, 7.19, 4.68] | 0.8675568786153617 | 3 | STABLE_3_OF_3 | [6, 6, 13] | [6, 4, 11] | [3, 13, 11] | [8, 11, 6] | 1.1875 | STABLE_OR_MIXED | False | 18.518519920156272 | 11.533590260163662 | CYCLE_TIMING | NO_TRADE | FALLING | INSUFFICIENT | 53 | 41.58882283911626 | HIGH |
| CRNC | 58.695 | CANDIDATE | NO_TRADE | IRREGULAR | 12.322792857572228 | [6.47, 19.56, 9.02] | [12.68, 4.55, 3.82] | 1.9838325962779013 | 3 | STABLE_3_OF_3 | [3, 17, 14] | [15, 4, 4] | [2, 7, 24] | [9, 12, 4] | 2.138888888888889 | DISSIPATING | False | 9.017417722756193 | 11.808887271823533 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 17 | 20.135473477171224 | MEDIUM |
| OBE | 58.670 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.301079000833297 | [13.97, 18.18, 4.06] | [13.92, 33.37, 7.27] | 1.0036287212204067 | 2 | UNSTABLE | [10, 26, 4] | [6, 14, 5] | [21, 17, 9] | [6, 14, 3] | 2.25 | DISSIPATING | False | 4.062232320015191 | 13.39869650257444 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 26 | 21.37633118736948 | MEDIUM |
| XPRO | 58.579 | CANDIDATE | NO_TRADE | STABLE_RANGE | 12.452112272923799 | [6.88, 12.45, 3.9] | [5.13, 6.34, 5.53] | 1.2446100317773452 | 2 | UNSTABLE | [6, 5, 5] | [10, 22, 6] | [6, 5, 8] | [20, 24, 5] | 0.4 | STABLE_OR_MIXED | False | 3.8980472124543253 | 10.02983010296741 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | RISING | 21 | 14.95875149963658 | MEDIUM |
| ASIC | 58.449 | CANDIDATE | NO_TRADE | INSUFFICIENT | 7.564650726993549 | [4.7, 5.73, 7.56] | [6.42, 13.74, 8.03] | 0.7139734239697425 | 2 | WATCH_2_OF_3 | [12, 5, 9] | [7, 21, 6] | [5, 4, 11] | [12, 15, 16] | 0.8095238095238095 | STABLE_OR_MIXED | False | 7.564650726993549 | 7.962983405471117 | WATCH | NO_TRADE | MIXED | INSUFFICIENT | 26 | 12.1034236732233 | MEDIUM |
| HLIT | 58.378 | CANDIDATE | NO_TRADE | INSUFFICIENT | 9.296026534869107 | [6.82, 10.69, 7.46] | [3.58, 3.36, 3.29] | 2.2215823222141275 | 3 | STABLE_3_OF_3 | [16, 9, 7] | [8, 11, 2] | [11, 11, 7] | [9, 8, 6] | 1.25 | STABLE_OR_MIXED | False | 7.462686425532894 | 10.4835734271154 | CYCLE_TIMING | NO_TRADE | FALLING | INSUFFICIENT | 45.5 | 17.93938839074336 | MEDIUM |
| TT | 58.347 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.634527680280586 | [13.36, 3.07, 3.63] | [3.24, 9.92, 2.73] | 1.120909955921715 | 1 | UNSTABLE | [33, 6, 4] | [18, 11, 11] | [18, 21, 6] | [15, 8, 15] | 0.8727272727272727 | STABLE_OR_MIXED | False | 3.634527680280586 | 6.776039738289942 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | INSUFFICIENT | 44 | 12.708995341084723 | MEDIUM |
| CRD.B | 58.305 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.3927024582229626 | [3.49, 3.3, 3.39] | [4.47, 16.03, 4.89] | 0.6931643226306808 | 0 | UNSTABLE | [9, 12, 8] | [7, 6, 3] | [13, 9, 2] | [6, 3, 7] | 1.5 | DISSIPATING | False | 3.3927024582229626 | 6.535756989160789 | TOO_SMALL_UPSIDE | NO_TRADE | RISING | INSUFFICIENT | 35 | 14.391010603698984 | HIGH |
| DXC | 58.277 | CANDIDATE | NO_TRADE | STABLE_RANGE | 15.46012038061787 | [10.68, 12.68, 46.85] | [28.49, 4.87, 12.32] | 1.0293825439823863 | 3 | STABLE_3_OF_3 | [6, 13, 17] | [12, 11, 15] | [14, 3, 22] | [21, 3, 16] | 0.9791666666666666 | STABLE_OR_MIXED | False | 46.84683492688584 | 10.440823251347487 | CYCLE_TIMING | NO_TRADE | RISING | MIXED | 34 | 15.810026215807765 | HIGH |
| ATGL | 57.564 | CANDIDATE | NO_TRADE | STABLE_RANGE | 18.834076229970485 | [11.36, 145.59, 6.08] | [32.71, 4.02, 6.46] | 1.75940159940304 | 3 | STABLE_3_OF_3 | [3, 9, 4] | [5, 4, 9] | [3, 2, 11] | [3, 7, 9] | 0.6142857142857143 | STABLE_OR_MIXED | False | 6.0773500457816265 | 22.25333550449673 | CYCLE_TIMING | NO_TRADE | MIXED | FALLING | 21.5 | 32.103798759905985 | MEDIUM |
| NYAX | 57.534 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.842953829227538 | [16.75, 18.54, 3.19] | [16.98, 5.29, 2.94] | 3.1667565986879476 | 2 | UNSTABLE | [10, 16, 6] | [5, 5, 12] | [14, 13, 4] | [4, 12, 5] | 2.3 | DISSIPATING | False | 3.186841590260814 | 9.218835401299751 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 24 | 16.651655201817416 | MEDIUM |
| LOMA | 56.918 | CANDIDATE | NO_TRADE | DOWNTREND | 6.719370680489034 | [12.91, 12.07, 3.6] | [4.22, 8.36, 3.95] | 2.8636212011930535 | 2 | UNSTABLE | [24, 26, 10] | [3, 5, 6] | [17, 31, 15] | [2, 4, 5] | 4.525 | DISSIPATING | True | 3.6016966917501225 | 7.869140952798156 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 25.0 | 14.025245216681359 | MEDIUM |
| SLNG | 56.406 | CANDIDATE | NO_TRADE | DOWNTREND | 4.377881348855817 | [12.63, 3.99, 4.38] | [7.18, 14.61, 13.59] | 0.32213360956211406 | 1 | UNSTABLE | [15, 2, 10] | [7, 5, 12] | [11, 7, 8] | [22, 6, 12] | 1.0476190476190477 | DISSIPATING | False | 4.377881348855817 | 14.3315436355003 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 21.5 | 24.4060493846741 | MEDIUM |
| GLW | 56.113 | CANDIDATE | NO_TRADE | IRREGULAR | 11.465139720745743 | [11.23, 11.47, 6.07] | [9.25, 4.98, 16.88] | 1.2134154140163043 | 3 | STABLE_3_OF_3 | [9, 10, 16] | [3, 8, 8] | [8, 9, 19] | [3, 7, 7] | 1.2678571428571428 | STABLE_OR_MIXED | False | 6.071626128711194 | 13.448849733552443 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 20.5 | 17.6917131717661 | MEDIUM |
| CCK | 55.887 | CANDIDATE | NO_TRADE | INSUFFICIENT | 7.337633358534945 | [3.6, 13.14, 7.34] | [8.0, 5.86, 3.64] | 1.2519906738702835 | 2 | WATCH_2_OF_3 | [14, 41, 9] | [12, 5, 6] | [11, 31, 20] | [20, 11, 6] | 2.0757575757575757 | DISSIPATING | False | 7.337633358534945 | 6.40568680463789 | WATCH | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 76.5 | 15.407802338822385 | HIGH |

## Experimental recent-swing review shortlist (NOT BUY signals)
Count: 0 of 109 scored CANDIDATE names
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
    "observations": 181,
    "positive_net_pct": 43.646408839779006,
    "average_net_pct": -1.7643102872467775,
    "average_positive_pct": 3.7497816688118157,
    "average_nonpositive_pct": -6.0350285669392205,
    "benchmark_pairs": 181,
    "average_excess_pct": -0.6835446672342157,
    "worst_adverse_excursion_pct": -81.83229896445631
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 1101,
    "positive_net_pct": 51.58946412352407,
    "average_net_pct": 0.44051993574433446,
    "average_positive_pct": 6.898582023656376,
    "average_nonpositive_pct": -6.441617523794203,
    "benchmark_pairs": 1101,
    "average_excess_pct": 1.5623060114431802,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 133,
    "positive_net_pct": 48.87218045112782,
    "average_net_pct": -0.7405022635418794,
    "average_positive_pct": 4.81872940381158,
    "average_nonpositive_pct": -6.054473710276804,
    "benchmark_pairs": 133,
    "average_excess_pct": 0.32544128460461424,
    "worst_adverse_excursion_pct": -25.57142802647182
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "0-40",
    "observations": 125,
    "positive_net_pct": 48.8,
    "average_net_pct": -2.0642293706215575,
    "average_positive_pct": 5.645963658401102,
    "average_nonpositive_pct": -9.413007101408775,
    "benchmark_pairs": 125,
    "average_excess_pct": -0.5897295326019614,
    "worst_adverse_excursion_pct": -95.51242232978043
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "40-60",
    "observations": 729,
    "positive_net_pct": 52.81207133058985,
    "average_net_pct": 1.5752388418043788,
    "average_positive_pct": 11.281197543754862,
    "average_nonpositive_pct": -9.2875347054367,
    "benchmark_pairs": 729,
    "average_excess_pct": 3.2374400468636084,
    "worst_adverse_excursion_pct": -88.15789411768027
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 94,
    "positive_net_pct": 54.255319148936174,
    "average_net_pct": 1.5642601839871904,
    "average_positive_pct": 8.30172035506545,
    "average_nonpositive_pct": -6.426680949152145,
    "benchmark_pairs": 94,
    "average_excess_pct": 3.010707009252754,
    "worst_adverse_excursion_pct": -30.81636301420778
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
- INDV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
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
