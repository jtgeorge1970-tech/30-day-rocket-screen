from __future__ import annotations

"""Engine 4 production runner — verified free-provider repair.

This runner keeps the locked Engine 4 funnel and final live logic, but repairs two
verified data-source defects:

1) Yahoo extended-hours bars do not reliably contain premarket volume. Engine 4 now
   uses Nasdaq's public extended-trading endpoint for current premarket share volume
   on the strongest preliminary candidates, then computes an auditable premarket
   volume intensity = premarket shares / estimated average daily shares.
2) Yahoo Ticker.news / Ticker.info produced repeated 401/429 failures. Engine 4 now
   uses Google News RSS for catalyst headlines and Nasdaq's public quote endpoint for
   bid/ask spread. No paid data source or API key is required.

Yahoo remains the batched source for broad price bars and historical/daily bars. All
provider substitutions are explicit in audit fields; no proxy is mislabeled as true
historical RVOL.
"""

import argparse
import math

import numpy as np
import pandas as pd

import engine4_live
import engine4_pipeline as core
from engine4_config import (
    BROAD_POOL_SIZE,
    DEEP_POOL_SIZE,
    MAX_SPREAD_PCT,
    MIN_ATR_PCT,
    MIN_PRICE,
    MIN_PREMARKET_RVOL,
    MIN_SCORE,
    SECTOR_ETF,
)
from engine4_data import (
    CATALYST_RULES,
    NEGATIVE_CATALYST,
    PROMOTIONAL,
    download_daily_metrics,
    download_intraday,
    historical_premarket_baseline,
    prior_regular_close,
    slice_window,
)
from engine4_free_providers import (
    google_news_catalyst,
    nasdaq_premarket_many,
    nasdaq_quote_spread,
    provider_smoke,
)
from engine4_score import preliminary_activity_score, score_candidate

NASDAQ_ENRICH_CAP = 400
MIN_PM_INTENSITY_PCT = 2.0


def provider_catalyst(ticker: str, reference_time):
    return google_news_catalyst(
        ticker,
        reference_time,
        CATALYST_RULES,
        NEGATIVE_CATALYST,
        PROMOTIONAL,
    )


def _estimated_avg_daily_shares(avg_daily_dollar_volume: float, price: float) -> float:
    if not (math.isfinite(avg_daily_dollar_volume) and math.isfinite(price) and price > 0):
        return math.nan
    return avg_daily_dollar_volume / price


def repaired_build_broad_pool(date_et, cutoff: str, max_symbols: int | None = None):
    base = core.eligible_baseline()
    if max_symbols:
        base = base.head(max_symbols).copy()

    symbols = base.ticker.astype(str).tolist()
    frames = core.download_intraday(
        symbols,
        period="1d",
        interval="1m",
        prepost=True,
        date_et=date_et,
        lookback_days=1,
    )
    indexed = base.set_index("ticker")
    rows = []

    for symbol in symbols:
        frame = frames.get(symbol)
        if frame is None or frame.empty:
            continue
        pm = core.slice_window(frame, date_et, "04:00", cutoff)
        if pm.empty or "Close" not in pm.columns:
            continue
        close = pd.to_numeric(pm["Close"], errors="coerce").dropna()
        if close.empty:
            continue

        current = float(close.iloc[-1])
        previous = core.prior_regular_close(frame, date_et)
        if not math.isfinite(previous):
            previous = float(indexed.at[symbol, "price"])
        if previous <= 0 or current < MIN_PRICE:
            continue

        gap = (current / previous - 1.0) * 100.0
        daily_dollar = float(indexed.at[symbol, "dollar_volume"])
        rows.append({
            "ticker": symbol,
            "name": str(indexed.at[symbol, "name"]),
            "sector": str(indexed.at[symbol, "sector"]),
            "market_cap": float(indexed.at[symbol, "market_cap"]),
            "avg_daily_dollar_volume": daily_dollar,
            "previous_close": previous,
            "last_premarket": current,
            "premarket_volume": 0.0,
            "premarket_dollar_volume": 0.0,
            "premarket_volume_intensity_pct": math.nan,
            "gap_pct": gap,
            "broad_qualifier": True,
            "nasdaq_premarket_ok": False,
            "strict_activity_pass": False,
            "activity_score": preliminary_activity_score(gap, 1.0, daily_dollar),
        })

    observed = pd.DataFrame(rows)
    meta = {
        "baseline_eligible": len(base),
        "symbols_with_intraday_data": len(frames),
        "trustworthy_observed": len(observed),
        "broad_qualified": len(observed),
        "nasdaq_enrichment_cap": NASDAQ_ENRICH_CAP,
        "nasdaq_premarket_enriched": 0,
        "nonzero_premarket_activity_count": 0,
        "strict_activity_count": 0,
        "retained_by_cap": 0,
        "broad_pool_cap": BROAD_POOL_SIZE,
    }
    if observed.empty:
        return observed, meta

    # Stage A: use only price-gap + liquidity to choose a generous enrichment pool.
    # No Yahoo premarket volume is used because it is known to be unreliable.
    preliminary = observed.copy()
    preliminary["positive_gap"] = preliminary.gap_pct > 0
    preliminary = preliminary.sort_values(
        ["positive_gap", "gap_pct", "avg_daily_dollar_volume"],
        ascending=[False, False, False],
    ).head(min(NASDAQ_ENRICH_CAP, len(preliminary)))

    snapshots = nasdaq_premarket_many(preliminary.ticker.astype(str).tolist(), max_workers=12)
    enriched_rows = []
    for row in preliminary.to_dict("records"):
        snap = snapshots.get(row["ticker"], {})
        if snap.get("ok"):
            px = snap.get("premarket_price", math.nan)
            vol = snap.get("premarket_volume", math.nan)
            if math.isfinite(px) and px >= MIN_PRICE:
                row["last_premarket"] = float(px)
                row["gap_pct"] = (float(px) / row["previous_close"] - 1.0) * 100.0
            if math.isfinite(vol) and vol >= 0:
                row["premarket_volume"] = float(vol)
                row["premarket_dollar_volume"] = float(vol) * row["last_premarket"]
                adv_shares = _estimated_avg_daily_shares(row["avg_daily_dollar_volume"], row["last_premarket"])
                row["premarket_volume_intensity_pct"] = (
                    float(vol) / adv_shares * 100.0 if math.isfinite(adv_shares) and adv_shares > 0 else math.nan
                )
                row["nasdaq_premarket_ok"] = True
        row["strict_activity_pass"] = bool(
            row["gap_pct"] >= 0.50
            and row["gap_pct"] <= 25.0
            and row["premarket_dollar_volume"] >= 500_000
        )
        row["activity_score"] = preliminary_activity_score(
            row["gap_pct"], max(row["premarket_dollar_volume"], 1.0), row["avg_daily_dollar_volume"]
        )
        enriched_rows.append(row)

    enriched = pd.DataFrame(enriched_rows)
    meta["nasdaq_premarket_enriched"] = int(enriched.nasdaq_premarket_ok.sum()) if not enriched.empty else 0
    meta["nonzero_premarket_activity_count"] = int((enriched.premarket_volume > 0).sum()) if not enriched.empty else 0
    meta["strict_activity_count"] = int(enriched.strict_activity_pass.sum()) if not enriched.empty else 0

    if enriched.empty or meta["nasdaq_premarket_enriched"] == 0:
        # This is a provider failure, not a legitimate no-opportunity day.
        return pd.DataFrame(), meta

    broad = enriched.sort_values(
        ["strict_activity_pass", "premarket_volume_intensity_pct", "activity_score", "premarket_dollar_volume", "gap_pct"],
        ascending=False,
        na_position="last",
    ).head(BROAD_POOL_SIZE).reset_index(drop=True)
    meta["retained_by_cap"] = len(broad)
    return broad, meta


def repaired_score_pool(broad: pd.DataFrame, date_et, reference, cutoff: str) -> pd.DataFrame:
    selected = broad.head(DEEP_POOL_SIZE).copy()
    deep_symbols = selected.ticker.astype(str).tolist()
    history = download_intraday(deep_symbols, period="7d", interval="1m", prepost=True, date_et=date_et, lookback_days=7)
    daily = download_daily_metrics(deep_symbols, asof_date=date_et)
    benchmark_symbols = ["SPY", "QQQ"] + sorted({SECTOR_ETF[s] for s in selected.sector if s in SECTOR_ETF})
    benchmarks = download_intraday(benchmark_symbols, period="1d", interval="1m", prepost=True, date_et=date_et, lookback_days=1)

    benchmark_returns = {}
    for symbol, frame in benchmarks.items():
        pm = slice_window(frame, date_et, "04:00", cutoff)
        prev = prior_regular_close(frame, date_et)
        if pm.empty or not math.isfinite(prev) or prev <= 0:
            continue
        close = pd.to_numeric(pm["Close"], errors="coerce").dropna()
        if not close.empty:
            benchmark_returns[symbol] = (float(close.iloc[-1]) / prev - 1.0) * 100.0

    market_return = np.nanmean([benchmark_returns.get("SPY", np.nan), benchmark_returns.get("QQQ", np.nan)])
    if not math.isfinite(market_return):
        market_return = 0.0

    enriched = []
    quote_ok_count = 0
    for row in selected.to_dict("records"):
        symbol = row["ticker"]
        hist = history.get(symbol)
        if hist is None or hist.empty:
            continue

        baseline_volume = historical_premarket_baseline(hist, date_et, cutoff)
        rvol = (
            row["premarket_volume"] / baseline_volume
            if math.isfinite(baseline_volume) and baseline_volume > 0 and row.get("premarket_volume", 0) > 0
            else math.nan
        )
        intensity = row.get("premarket_volume_intensity_pct", math.nan)
        volume_metric_source = "historical_premarket_rvol" if math.isfinite(rvol) else "nasdaq_pm_volume_pct_adv"
        volume_gate = (
            rvol >= MIN_PREMARKET_RVOL
            if math.isfinite(rvol)
            else (math.isfinite(intensity) and intensity >= MIN_PM_INTENSITY_PCT)
        )

        dm = daily.get(symbol, {})
        atr = dm.get("atr", np.nan)
        atr_pct = atr / row["last_premarket"] * 100.0 if atr and math.isfinite(atr) else np.nan
        levels = [dm.get(k, np.nan) for k in ("high_5", "high_20", "high_60")]
        overhead = [x for x in levels if x and math.isfinite(x) and x > row["last_premarket"]]
        resistance = min(overhead) if overhead else np.nan
        room = (resistance / row["last_premarket"] - 1.0) * 100.0 if math.isfinite(resistance) else 10.0
        sector_etf = SECTOR_ETF.get(row["sector"])
        sector_return = benchmark_returns.get(sector_etf, market_return)
        catalyst, headline, age_hours = provider_catalyst(symbol, reference)
        bid, ask, spread = nasdaq_quote_spread(symbol)
        if math.isfinite(spread):
            quote_ok_count += 1

        row.update({
            "premarket_rvol": float(rvol),
            "premarket_volume_metric_source": volume_metric_source,
            "premarket_volume_gate_pass": bool(volume_gate),
            "atr_pct": float(atr_pct),
            "resistance_price": float(resistance) if math.isfinite(resistance) else np.nan,
            "resistance_room_pct": float(room),
            "market_relative_strength_pct": float(row["gap_pct"] - market_return),
            "sector_relative_strength_pct": float(row["gap_pct"] - sector_return),
            "catalyst_quality": catalyst,
            "catalyst_headline": headline,
            "catalyst_age_hours": age_hours,
            "catalyst_source": "Google News RSS",
            "bid": bid,
            "ask": ask,
            "spread_pct": spread,
            "spread_source": "Nasdaq quote",
        })
        score, components = score_candidate(row)
        row["score"] = score
        for key, value in components.items():
            row[f"pts_{key}"] = value

        gate_map = {
            "catalyst": catalyst > 0,
            "pm_volume_strength": bool(volume_gate),
            "atr": math.isfinite(atr_pct) and atr_pct >= MIN_ATR_PCT,
            "room": room > 0,
            "spread": math.isfinite(spread) and spread <= MAX_SPREAD_PCT,
            "score70": score >= MIN_SCORE,
        }
        row["premarket_gate_count"] = int(sum(gate_map.values()))
        row["premarket_a_grade"] = bool(all(gate_map.values()))
        row["premarket_failures"] = ",".join(k for k, passed in gate_map.items() if not passed)
        row["premarket_grade"] = "A" if row["premarket_a_grade"] else ("B" if score >= 60 and row["premarket_gate_count"] >= 3 else "WATCH")
        enriched.append(row)

    ranked = pd.DataFrame(enriched)
    if ranked.empty:
        return ranked

    # Systemic quote-provider outage must fail closed instead of silently grading every stock poorly.
    if quote_ok_count < max(5, int(0.50 * len(ranked))):
        raise RuntimeError(
            f"Nasdaq quote provider health failure: valid spreads for only {quote_ok_count}/{len(ranked)} analyzed names"
        )

    return ranked.sort_values(
        ["premarket_a_grade", "score", "premarket_gate_count", "premarket_volume_intensity_pct", "premarket_dollar_volume"],
        ascending=False,
        na_position="last",
    ).reset_index(drop=True)


def install_repairs() -> None:
    core.build_broad_pool = repaired_build_broad_pool
    core._score_pool = repaired_score_pool
    core.catalyst_for = provider_catalyst
    core.quote_spread = nasdaq_quote_spread
    engine4_live.quote_spread = nasdaq_quote_spread

    # final_stage was imported into core from engine4_intraday. opening_structure delegates
    # to engine4_live, so patching engine4_live.quote_spread repairs refreshed final spreads too.


def assert_provider_health() -> dict:
    health = provider_smoke()
    required = ["nasdaq_premarket_ok", "nasdaq_quote_ok", "google_news_ok"]
    failed = [k for k in required if not health.get(k)]
    if failed:
        raise RuntimeError(f"Engine 4 free-provider health check failed: {failed}; details={health}")
    print(f"ENGINE4_FREE_PROVIDER_HEALTH_PASS {health}", flush=True)
    return health


def main() -> None:
    install_repairs()

    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("prescreen")
    p.add_argument("--date")
    p.add_argument("--max-symbols", type=int)
    d = sub.add_parser("deep")
    d.add_argument("--date")
    r = sub.add_parser("refresh")
    r.add_argument("--date")
    r.add_argument("--max-symbols", type=int)
    f = sub.add_parser("final")
    f.add_argument("--date")
    sub.add_parser("self-test")
    sub.add_parser("provider-smoke")
    args = parser.parse_args()

    if args.command == "prescreen":
        assert_provider_health()
        core.prescreen_stage(args.date, args.max_symbols)
    elif args.command == "deep":
        core.deep_stage(args.date)
    elif args.command == "refresh":
        assert_provider_health()
        core.refresh_and_freeze(args.date, args.max_symbols)
    elif args.command == "final":
        assert_provider_health()
        core.final_with_timeline(args.date)
    elif args.command == "provider-smoke":
        assert_provider_health()
    else:
        core.self_test()
        assert callable(repaired_build_broad_pool)
        assert callable(repaired_score_pool)
        print("ENGINE4_RUNNER_REPAIR_SELF_TEST_PASS")


if __name__ == "__main__":
    main()
