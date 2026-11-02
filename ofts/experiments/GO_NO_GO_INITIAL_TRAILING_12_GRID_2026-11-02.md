# OFTS 12-combination initial-stop + activated trailing-stop test — November 2, 2026

**Read-only research, no production scoring change and no orders.**

Sources: `ofts-daily-state/cycle_ledger.json` read 2026-11-02; `ofts/experiments/SIP_DAILY_BARS_2026-10-09_TO_2026-10-30.csv` (independent Alpaca SIP daily bars, cutoff October 30). All 36 executed ledger entries with available entry date/price and OHLC bars, including multiple distinct trade entries for the same symbol. Three completed exits by cutoff and 33 censored open entries. November 2 MH exit not included due to price cutoff.

**Rule:** fixed initial stop 3/4/5/6% below entry; if highest observed high reaches 10% above entry, switch to max(initial stop, peak*(1-trailing)) using trailing distances 5/8/10%. Stop threshold checked at the next daily open first (fill at worse open if gap), then against daily low (optimistic stop-level fill). The trailing reference peak is updated *after* each day's stop check to avoid same-bar high-before-low assumptions. Entry-day lows can trigger stops after an opening entry. On no stop, use actual recorded hypothetical SELL open if completed by Oct 30, otherwise Oct 30 close. No reentry, no redeployment of capital, subtract 0.20 percentage points per trade. All outcomes are retrospective, largely censored, non-independent, and have optimistic execution assumptions. Daily OHLC cannot prove attainable intraday stop execution.

| Initial stop | Trail 5% | Trail 8% | Trail 10% |
|---|---:|---:|---:|
| 3% | -0.179% | -0.169% | -0.306% |
| 4% | -0.281% | -0.051% | -0.188% |
| 5% | +0.289% | +0.344% | +0.078% |
| 6% | +0.441% | **+0.496%** | +0.186% |

Each cell is equal-weight average of 36 entry returns net of assumed 0.20% costs, NOT a portfolio CAGR or realized P&L. No-stop October 30 baseline from saved prior matched-stock audit +3.877% (median -0.283%, worst -39.144%). Best tested 6%/8% has median -0.578%, worst -8.424%, 16 positive of 36, 18 stopped, 5 stopped after activation. **No tested rule improves the mean relative to no-stop.**

Important entry-timing counterexamples under 6%/8%: BETR and ATGL each hit initial -6% before major later gains; modeled exit about -6.2% net, while their no-stop October 30 marks were +94.931% and +46.430%. LYEL is modeled to stop with +6.33% instead of +26.116% open mark. This is evidence the entry/re-entry/stop combination must be reconsidered rather than declaring a tight stop profitable.

Caveats: OHLC stop fills are optimistic; gaps can exceed stops, and thin stocks may be worse. Historical selection overfits, 33 entries still open, positions overlap, no benchmark-adjusted matched-stock results for each stop variant, no adequate independent holdout. **Decision remains RESEARCH_ONLY_NO_GO.** Next experiment should test delayed/confirmed entries and volatility-adjusted stops, frozen chronologically and compared to matched same-stock and SPY/IWM controls.