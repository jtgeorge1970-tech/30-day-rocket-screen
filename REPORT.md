# OFTS daily research

Market session: 2026-10-23
Selected: 130; refreshed: 121; refresh errors: 47
Qualified prediction cohorts saved: 11; current coverage: 121/130
Outcome counts: {'CORPORATE_ACTION_REVIEW': 2, 'INELIGIBLE_DATA': 580, 'MATURE': 827, 'MISSING_SESSIONS': 7, 'PENDING': 5634}
Cycle fingerprints saved: 106/147
Signal states: BUY=1, SELL=1, NO_TRADE=145
Cycle ledger: pending entries=1; open positions=22; closed trades=1; SPY pairs=1
Cycle-speed report card: READY; closed forward trades=1; groups=['MEDIUM_11_TO_25']
Score scale: theoretical 0-100; observed 13.729695932252008-68.87575634703964; validated BUY threshold=NONE
Score distribution: {'BELOW_40': 11, '40_TO_49_999': 51, '50_TO_59_999': 36, '60_TO_69_999': 8, '70_TO_79_999': 0, '80_TO_89_999': 0, '90_TO_100': 0}
System actionability gate: RESEARCH_ONLY_NO_GO; OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED
Production approval: NO. These are quality scores, not BUY signals.
Experimental recent viability v0.5: last three minor swings, last three UP legs, old-outlier dominance, peak/trough spacing 10-40 sessions, adjacent 3-vs-3 amplitude/cadence, and hypothetical capture after costs; NOT validated.
Experimental viable REVIEW=0; viability NO_TRADE=105
Experimental swing-health v0.1: last-four-leg stability and lower-high/lower-low deterioration (NOT validated for trading).
Experimental swing-health NO_TRADE=75; REVIEW=31; INSUFFICIENT=56
Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.
Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.

| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | Prior 3 UP % | UP ratio | >=5% count | Repeatability | Peak gaps | Prior peak gaps | Trough gaps | Prior trough gaps | Cadence ratio | Comparison | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |
|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|
| SCYX | 68.876 | CANDIDATE | NO_TRADE | STABLE_RANGE | 22.323463527984643 | [17.88, 18.25, 22.32] | [12.56, 3.98, 51.26] | 1.4532190612379912 | 3 | STABLE_3_OF_3 | [16, 18, 7] | [6, 5, 10] | [24, 7, 16] | [6, 5, 12] | 2.6666666666666665 | DISSIPATING | False | 22.323463527984643 | 15.16496066569145 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 25 | 27.6617157809988 | MEDIUM |
| AKAM | 65.013 | CANDIDATE | NO_TRADE | DOWNTREND | 14.809186553508058 | [5.39, 13.36, 6.0] | [14.84, 13.34, 5.28] | 0.4493567985845546 | 3 | STABLE_3_OF_3 | [8, 10, 12] | [10, 7, 10] | [9, 16, 7] | [7, 11, 7] | 1.1428571428571428 | DISSIPATING | False | 5.996031051408424 | 12.31875251089575 | CYCLE_TIMING | NO_TRADE | FALLING | FALLING | 28 | 16.858607095784766 | HIGH |
| ASO | 62.946 | CANDIDATE | NO_TRADE | STABLE_RANGE | 3.3333364159169876 | [3.23, 29.86, 2.51] | [8.24, 2.66, 5.36] | 0.6025206595314702 | 1 | UNSTABLE | [7, 16, 7] | [4, 5, 4] | [8, 15, 9] | [5, 4, 7] | 1.775 | DISSIPATING | False | 2.5056928174204796 | 7.643326882512502 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 31.0 | 15.465077423248275 | HIGH |
| SPGI | 61.938 | CANDIDATE | NO_TRADE | INSUFFICIENT | 4.370988740285164 | [4.3, 7.88, 4.37] | [19.63, 6.24, 4.72] | 0.7000410382722665 | 1 | UNSTABLE | [13, 11, 4] | [12, 8, 7] | [7, 12, 21] | [10, 9, 10] | 1.2875 | STABLE_OR_MIXED | False | 4.370988740285164 | 6.798198120405242 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | MIXED | 35 | 11.723543952355413 | HIGH |
| Q | 61.631 | CANDIDATE | NO_TRADE | STABLE_RANGE | 13.664597372606302 | [9.45, 16.62, 4.16] | [14.81, 6.91, 5.93] | 1.3664938446855541 | 2 | UNSTABLE | [15, 17, 11] | [10, 7, 5] | [9, 9, 23] | [7, 6, 9] | 1.7142857142857144 | DISSIPATING | False | 4.16052293325051 | 10.017170057116969 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | FALLING | 24 | 15.558687260850146 | MEDIUM |
| FUBO | 61.064 | CANDIDATE | NO_TRADE | IRREGULAR | 8.468683359655271 | [10.83, 4.04, 8.47] | [24.1, 21.8, 14.75] | 0.38843602032248625 | 2 | WATCH_2_OF_3 | [6, 5, 13] | [6, 14, 7] | [8, 6, 12] | [4, 5, 15] | 1.2285714285714286 | DISSIPATING | False | 8.468683359655271 | 14.685663461095555 | WATCH | NO_TRADE | RISING | RISING | 21.0 | 24.122807873668826 | HIGH |
| RERE | 60.792 | CANDIDATE | NO_TRADE | IRREGULAR | 9.67742145409768 | [6.85, 3.07, 9.89] | [13.95, 11.11, 3.15] | 0.6167511454734013 | 2 | WATCH_2_OF_3 | [10, 13, 20] | [5, 12, 4] | [5, 14, 13] | [3, 8, 10] | 2.1125 | DISSIPATING | False | 9.890106723095894 | 8.536226476930292 | WATCH | NO_TRADE | MIXED | MIXED | 13.0 | 12.351543378023134 | MEDIUM |
| NYAX | 60.621 | CANDIDATE | NO_TRADE | STABLE_RANGE | 11.995180160324592 | [5.29, 2.94, 16.75] | [7.24, 3.44, 16.98] | 0.7307811318654659 | 2 | WATCH_2_OF_3 | [5, 12, 10] | [4, 4, 5] | [12, 5, 14] | [4, 4, 4] | 2.75 | DISSIPATING | False | 16.748766621516097 | 8.819942040929368 | WATCH | NO_TRADE | MIXED | MIXED | 22 | 15.198181980197784 | MEDIUM |
| TT | 59.611 | CANDIDATE | SELL | DOWNTREND | 4.319998324760499 | [2.73, 13.36, 3.07] | [2.78, 3.24, 9.92] | 0.9480926253012288 | 1 | UNSTABLE | [11, 33, 6] | [3, 18, 11] | [15, 18, 21] | [3, 15, 8] | 1.625 | DISSIPATING | False | 3.0741710089404073 | 7.006748662368222 | TOO_SMALL_UPSIDE | NO_TRADE | FALLING | FALLING | 41 | 12.708995341084723 | MEDIUM |
| ATGL | 59.523 | CANDIDATE | NO_TRADE | IRREGULAR | 7.9497928402005975 | [4.02, 6.46, 11.36] | [10.12, 7.23, 32.71] | 0.6382818393478004 | 2 | WATCH_2_OF_3 | [4, 9, 3] | [7, 13, 5] | [9, 3, 2] | [16, 3, 7] | 0.5 | DISSIPATING | False | 11.363636117336174 | 20.128696054993185 | FADING | NO_TRADE | FALLING | FALLING | 21 | 32.06849916938487 | MEDIUM |
| ACDC | 58.984 | CANDIDATE | NO_TRADE | DECAYING | 18.375247042226196 | [9.82, 6.82, 15.52] | [24.31, 8.78, 13.85] | 0.7088552038191496 | 3 | STABLE_3_OF_3 | [8, 7, 12] | [7, 5, 4] | [12, 9, 17] | [9, 4, 2] | 2.3 | DISSIPATING | False | 15.521332757663542 | 13.131208480798506 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 22.5 | 23.767799004313883 | MEDIUM |
| CHPT | 58.750 | CANDIDATE | NO_TRADE | IRREGULAR | 8.721803238921733 | [4.68, 16.7, 8.72] | [12.21, 90.56, 17.01] | 0.5128420127040436 | 2 | WATCH_2_OF_3 | [2, 7, 10] | [7, 10, 9] | [5, 12, 2] | [11, 8, 4] | 0.7013888888888888 | DISSIPATING | False | 8.721803238921733 | 17.062166110777145 | FADING | NO_TRADE | MIXED | MIXED | 26 | 24.28571729521672 | MEDIUM |
| LFCR | 58.698 | CANDIDATE | NO_TRADE | IRREGULAR | 8.695655679332305 | [3.91, 8.7, 56.9] | [3.65, 6.16, 7.97] | 1.4106287244879654 | 2 | WATCH_2_OF_3 | [7, 6, 5] | [2, 11, 5] | [5, 4, 8] | [8, 6, 10] | 0.9125 | STABLE_OR_MIXED | False | 56.904772663333205 | 11.036121615140166 | WATCH | NO_TRADE | FALLING | MIXED | 12 | 11.617739999739435 | LOW |
| XPRO | 58.521 | CANDIDATE | NO_TRADE | INSUFFICIENT | 6.618965891784978 | [6.34, 5.53, 6.88] | [19.33, 29.6, 5.13] | 0.32805539003287426 | 3 | STABLE_3_OF_3 | [22, 6, 6] | [11, 24, 10] | [5, 6, 5] | [17, 20, 24] | 0.3977272727272727 | DISSIPATING | False | 6.883370976826919 | 9.664145545244601 | CYCLE_TIMING | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 20 | 14.95875149963658 | MEDIUM |
| GLW | 58.510 | CANDIDATE | NO_TRADE | IRREGULAR | 11.227968443843794 | [16.88, 11.23, 11.47] | [6.14, 9.25, 4.98] | 1.8685319181458309 | 3 | STABLE_3_OF_3 | [8, 9, 10] | [3, 3, 8] | [7, 8, 9] | [8, 3, 7] | 2.071428571428571 | DISSIPATING | False | 11.465139720745743 | 13.067640246400046 | CYCLE_TIMING | NO_TRADE | MIXED | MIXED | 20.5 | 17.6917131717661 | MEDIUM |
| KTB | 57.717 | CANDIDATE | NO_TRADE | INSUFFICIENT | 4.153874291641935 | [5.37, 3.34, 3.49] | [4.14, 5.63, 13.26] | 0.6212021491906816 | 1 | UNSTABLE | [6, 16, 4] | [4, 4, 13] | [14, 5, 9] | [3, 13, 7] | 1.3928571428571428 | DISSIPATING | False | 3.494584096117559 | 9.427640193368852 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | FALLING | 32 | 15.945346795151156 | MEDIUM |
| EPM | 57.644 | CANDIDATE | NO_TRADE | IRREGULAR | 5.7377058257448095 | [12.28, 6.34, 2.81] | [10.19, 9.43, 6.29] | 0.6720088429954724 | 2 | UNSTABLE | [14, 6, 2] | [10, 19, 2] | [14, 3, 5] | [18, 10, 5] | 0.55 | DISSIPATING | False | 2.8089928274849907 | 8.661247242968178 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 26 | 12.982888675563604 | LOW |
| VIRC | 57.467 | CANDIDATE | NO_TRADE | STABLE_RANGE | 4.461537874661969 | [9.51, 4.46, 3.19] | [3.06, 10.32, 2.95] | 1.4599118296170084 | 1 | UNSTABLE | [9, 9, 9] | [9, 7, 2] | [4, 9, 14] | [7, 6, 6] | 1.3928571428571428 | STABLE_OR_MIXED | False | 3.1897896311569474 | 6.935189494334906 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 20.0 | 11.659188733927506 | MEDIUM |
| DJT | 57.178 | CANDIDATE | NO_TRADE | STABLE_RANGE | 9.707601230295616 | [5.08, 9.71, 3.58] | [21.26, 4.87, 21.22] | 0.23931426913880552 | 2 | UNSTABLE | [5, 12, 21] | [7, 3, 17] | [10, 10, 23] | [13, 5, 12] | 1.2738095238095237 | DISSIPATING | False | 3.576983284817814 | 13.334175888910826 | TOO_SMALL_UPSIDE | NO_TRADE | MIXED | MIXED | 22.0 | 21.876944837676216 | LOW |
| FERG | 57.085 | CANDIDATE | NO_TRADE | INSUFFICIENT | 6.08606780511507 | [16.61, 4.34, 6.09] | [4.85, 5.97, 3.36] | 1.2544730128010313 | 2 | WATCH_2_OF_3 | [10, 19, 15] | [7, 12, 9] | [24, 11, 14] | [13, 9, 6] | 1.6111111111111112 | DISSIPATING | True | 6.08606780511507 | 7.144947741452169 | WATCH | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 43 | 15.39008433659906 | MEDIUM |
| MESO | 57.080 | CANDIDATE | NO_TRADE | STABLE_RANGE | 7.364017811603918 | [10.48, 5.0, 7.36] | [11.73, 9.25, 4.97] | 0.795695967807193 | 2 | WATCH_2_OF_3 | [11, 13, 8] | [7, 5, 6] | [10, 14, 9] | [12, 6, 6] | 1.75 | DISSIPATING | True | 7.364017811603918 | 11.12626176304761 | WATCH | NO_TRADE | FALLING | RISING | 16 | 17.007813091629323 | MEDIUM |
| CHTR | 56.936 | CANDIDATE | NO_TRADE | INSUFFICIENT | 15.776562646077686 | [3.57, 8.74, 8.87] | [27.88, 4.2, 7.66] | 1.141059599388954 | 2 | WATCH_2_OF_3 | [3, 3, 6] | [18, 2, 8] | [3, 5, 23] | [13, 3, 8] | 0.5 | STABLE_OR_MIXED | False | 8.872959098490352 | 11.117203878380282 | WATCH | NO_TRADE | INSUFFICIENT | INSUFFICIENT | 46.5 | 16.433007091739114 | HIGH |
| DKNG | 56.932 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.885425907149978 | [6.02, 3.62, 6.89] | [20.13, 8.86, 4.29] | 0.67891670684082 | 2 | WATCH_2_OF_3 | [10, 9, 9] | [13, 5, 5] | [15, 7, 8] | [9, 7, 3] | 1.4714285714285715 | DISSIPATING | False | 6.885425907149978 | 10.527785699037553 | WATCH | NO_TRADE | MIXED | FALLING | 42 | 22.446182935711857 | MEDIUM |
| CCS | 56.799 | CANDIDATE | NO_TRADE | INSUFFICIENT | 3.672368935275061 | [4.17, 7.24, 3.08] | [11.68, 6.09, 3.48] | 0.6840910734443489 | 1 | UNSTABLE | [4, 27, 17] | [8, 6, 2] | [22, 24, 3] | [8, 4, 2] | 4.166666666666667 | DISSIPATING | False | 3.0803486105271283 | 9.309555080988341 | TOO_SMALL_UPSIDE | NO_TRADE | INSUFFICIENT | MIXED | 34.5 | 17.292267882239752 | MEDIUM |
| CRNC | 56.601 | CANDIDATE | NO_TRADE | STABLE_RANGE | 6.804368129894389 | [3.82, 6.47, 19.56] | [6.64, 12.68, 4.55] | 0.9737109920041425 | 2 | WATCH_2_OF_3 | [4, 3, 17] | [8, 15, 4] | [4, 2, 7] | [9, 9, 12] | 0.4722222222222222 | STABLE_OR_MIXED | False | 19.556714277436903 | 11.976244956347891 | WATCH | NO_TRADE | FALLING | MIXED | 17 | 19.601070079276095 | MEDIUM |

## Experimental recent-swing review shortlist (NOT BUY signals)
Count: 0 of 94 scored CANDIDATE names
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
    "observations": 75,
    "positive_net_pct": 42.666666666666664,
    "average_net_pct": -2.5490401648617818,
    "average_positive_pct": 10.438619186741068,
    "average_nonpositive_pct": -12.214275031170878,
    "benchmark_pairs": 75,
    "average_excess_pct": 0.06628353196346297,
    "worst_adverse_excursion_pct": -41.60583899263223
  },
  {
    "model_hash": "2efb29d640e0ca751d9f8d30781f9021b2e38310114999e253e7b21b7283c3c6",
    "horizon": 10,
    "score_band": "60-80",
    "observations": 11,
    "positive_net_pct": 45.45454545454545,
    "average_net_pct": -5.258105020180599,
    "average_positive_pct": 4.888988754479735,
    "average_nonpositive_pct": -13.71401649906421,
    "benchmark_pairs": 11,
    "average_excess_pct": -2.6427813233553548,
    "worst_adverse_excursion_pct": -24.34210416242579
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "0-40",
    "observations": 63,
    "positive_net_pct": 47.61904761904762,
    "average_net_pct": -1.7000516744343006,
    "average_positive_pct": 3.1024183684986895,
    "average_nonpositive_pct": -6.06593353164611,
    "benchmark_pairs": 63,
    "average_excess_pct": -0.8873378802700889,
    "worst_adverse_excursion_pct": -55.257270184399786
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "40-60",
    "observations": 371,
    "positive_net_pct": 48.24797843665768,
    "average_net_pct": -0.07050049771173172,
    "average_positive_pct": 6.752274317051719,
    "average_nonpositive_pct": -6.43131660105891,
    "benchmark_pairs": 371,
    "average_excess_pct": 0.8162707675805635,
    "worst_adverse_excursion_pct": -86.84210490198016
  },
  {
    "model_hash": "a6ecf528ef92f072a3b6060380e01465574677be19e3fa4c75e4bcc7ae79519b",
    "horizon": 5,
    "score_band": "60-80",
    "observations": 56,
    "positive_net_pct": 46.42857142857143,
    "average_net_pct": -1.4325177231967547,
    "average_positive_pct": 4.478686467894362,
    "average_nonpositive_pct": -6.5555613554757235,
    "benchmark_pairs": 56,
    "average_excess_pct": -0.5857091821139421,
    "worst_adverse_excursion_pct": -25.57142802647182
  }
]
```

## Identity-boundary exclusions (current processing; prior snapshots immutable)

## Refresh failures
- LPBB: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BARK: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- CAQ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- YCY: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- GS.PRA: ValueError: EMPTY_PROVIDER_RESPONSE
- NVNI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SB.PRC: ValueError: EMPTY_PROVIDER_RESPONSE
- SLP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- WBD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- AMAN: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- ARCL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- AXIL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BREZ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BRKH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BRT: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- BRTM: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- CATX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- CPBI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- CQP: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- FOIL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- GJS: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- GSIW: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- GWH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- HVMC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- INAC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- INTJ: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- IPVV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- KCHV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- LESL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- LOCL: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- LWAC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- MCAH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- NCO: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- OCLT: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- ONCH: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- PAAC: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- POAS: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- QNCX: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- SDST: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SOS: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SPRU: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- SSEA: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TAP.A: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
- TDWD: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TONT: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- TVIV: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_SESSION_INCOMPLETE
- UCFI: ValueError: LATEST_SESSION_MISSING | 15m: ValueError: INTRADAY_EMPTY
