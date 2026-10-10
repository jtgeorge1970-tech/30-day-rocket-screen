# OFTS experimental v0.6: preliminary measured trading-opportunity ranking — 2026-10-10

**Status: research only; not a BUY/SELL signal, not validated, not the official v2.3 score.** Based on v0.5 successful workflow 38048039690, artifact 11667788223, file `v23_research_recent_viability_shortlist.csv`. The following scores use only **80 of the proposed 100 opportunity points**. The remaining 15 for current entry position and 5 for execution liquidity are **not calculated**; they must not be filled with guesses. Full-universe v0.6 scoring and replacement sixth candidate remain outstanding.

## Provisional ranking after market-cap hard gate

|rank|ticker|original v2.3 historical score|recent swing repeatability /25|upward magnitude /20|timing /15|health /20|measured total /80|eligibility|
|---:|---|---:|---:|---:|---:|---:|---:|---|
|1|CTOS|42.774|24.94|12.41|12.50|16|65.85|Market cap >$200M supported; complete liquidity verification pending|
|2|BXC|51.316|20.22|12.55|12.82|16|61.59|Market cap >$200M supported; complete liquidity verification pending|
|3|HYLN|47.876|20.06|20.00|12.82|1|53.87|Market cap >$200M supported; complete liquidity verification pending|
|4|EVI|53.994|12.89|20.00|11.08|9|52.97|Market cap and complete liquidity verification pending|
|5|PATH|52.001|10.13|20.00|12.12|4|46.25|Market cap >$200M supported; complete liquidity verification pending|
|—|INTS|46.930|18.81|10.50|13.69|20|63.01|**INELIGIBLE: Oct 9, 2026 market cap ~$10.55M, below locked $200M minimum. Excluded from top-N.**|

INTS independent market-cap source: https://ycharts.com/companies/INTS/market_cap (Oct 9, 2026); contemporaneous thin daily volume https://www.financecharts.com/stocks/INTS/summary/volume-current-vs-avg. Other supporting dated caps: CTOS https://stockanalysis.com/stocks/ctos/statistics/; BXC https://www.financecharts.com/stocks/BXC/summary/market-cap; HYLN https://ycharts.com/companies/HYLN/market_cap; PATH https://stockanalysis.com/stocks/path/market-cap/.

## Exact v0.6 exploratory partial-score definitions

Inputs are last three **completed UP** percentages `u` in chronological order, last three peak-to-peak intervals `p`, last three trough-to-trough intervals `t`, `swing_state` and `cadence_ratio` from the above artifact. Define `M(x)=median(x)`, `R(x)=min(1,max(0,x))`.

- **Repeatability /25**: `25 * R(1 - median(abs(u_i - M(u))) / M(u))`.
- **Upward magnitude /20**: `20 * R(M(u)/15)`; experimental 15% full-points cap.
- **Timing /15**: `7.5 * [R(1 - median(abs(p_i - M(p)))/M(p)) + R(1 - median(abs(t_i - M(t)))/M(t))]`.
- **Health /20**: Start at 20 and subtract 8 if three successive UP legs strictly shrink, 7 if swing state is DOWNTREND or DOWNTREND_WEAK_BOUNCE, 4 if recent-to-prior cadence ratio >=1.4, 4 if latest UP <70% of median of last three, and 4 if largest UP >3x median. Floor at zero.
- **Entry /15**: **UNSCORED** until point-in-time current price relative to confirmed swing band and lag/chase metrics are available.
- **Execution /5**: **UNSCORED** until point-in-time volume, spread, and fills are available.
- **Eligibility adjustment**: Hard gates first, including $200M minimum market cap, $3 price minimum, eligible security type, valid post-regime history. For passing stocks, proposed separate 0–100 eligibility/tradability multiplier is **NOT IMPLEMENTED OR CALCULATED**. Do not label these partial values as eligibility-adjusted scores or assign an arbitrary 100 multiplier.

Numbers are reproducible from the source artifact and the formulas above, rounded to 2 decimals. These weights/penalties are *hypotheses*, not optimized or chronologically validated. Only 5 of 6 existing survivors remain after verified INTS market-cap exclusion; no replacement sixth has been computed, and no eligible top six can yet be claimed. In particular, HYLN scores strongly on upside magnitude but is heavily penalized for declining recent rebounds, downtrend, and slowing cadence. CTOS has high repeatability but also a cadence-slowdown penalty. Future runs must rescore the entire eligible universe and audit false negatives.
