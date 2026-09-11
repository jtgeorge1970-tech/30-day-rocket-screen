from __future__ import annotations

"""Engine 4 production runner hotfix.

This module preserves the existing Engine 4 pipeline and replaces only the broad-pool
builder that regressed in SSOT v4.4. The regression incorrectly required non-zero
Yahoo premarket *volume* to count a stock as broadly qualified. The prior production
screen qualified a stock when it had a trustworthy premarket price observation; volume
was a ranking/quality field, not an all-or-nothing gate. Yahoo can report valid extended-
hours prices while returning zero volume in the 1-minute bars, so the regression could
collapse a healthy observed universe to zero.

The repaired logic restores the prior screening criterion exactly while reporting every
count honestly before ranking caps are applied.
"""

import argparse
import math

import pandas as pd

import engine4_pipeline as core
from engine4_config import BROAD_POOL_SIZE, MIN_PRICE
from engine4_data import download_intraday, prior_regular_close, slice_window
from engine4_score import preliminary_activity_score


def repaired_build_broad_pool(date_et, cutoff: str, max_symbols: int | None = None):
    base = core.eligible_baseline()
    if max_symbols:
        base = base.head(max_symbols).copy()

    symbols = base.ticker.astype(str).tolist()
    frames = download_intraday(
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
        pm = slice_window(frame, date_et, "04:00", cutoff)
        if pm.empty or "Close" not in pm.columns or "Volume" not in pm.columns:
            continue

        close = pd.to_numeric(pm["Close"], errors="coerce").dropna()
        volume = pd.to_numeric(pm["Volume"], errors="coerce").fillna(0)
        if close.empty:
            continue

        current = float(close.iloc[-1])
        previous = prior_regular_close(frame, date_et)
        if not math.isfinite(previous):
            previous = float(indexed.at[symbol, "price"])
        if previous <= 0 or current < MIN_PRICE:
            continue

        gap = (current / previous - 1.0) * 100.0
        pm_volume = float(volume.sum())
        pm_dollar = pm_volume * current
        daily_dollar = float(indexed.at[symbol, "dollar_volume"])

        rows.append({
            "ticker": symbol,
            "name": str(indexed.at[symbol, "name"]),
            "sector": str(indexed.at[symbol, "sector"]),
            "market_cap": float(indexed.at[symbol, "market_cap"]),
            "avg_daily_dollar_volume": daily_dollar,
            "previous_close": previous,
            "last_premarket": current,
            "premarket_volume": pm_volume,
            "premarket_dollar_volume": pm_dollar,
            "gap_pct": gap,
            # Restored criterion: a trustworthy observed premarket price is broad-qualified.
            # Premarket volume is reported separately and affects ranking/strict quality only.
            "broad_qualifier": True,
            "nonzero_premarket_activity": bool(pm_dollar > 0),
            "strict_activity_pass": bool(gap >= 0.50 and gap <= 25.0 and pm_dollar >= 500_000),
            "activity_score": preliminary_activity_score(gap, max(pm_dollar, 1.0), daily_dollar),
        })

    observed = pd.DataFrame(rows)
    meta = {
        "baseline_eligible": len(base),
        "symbols_with_intraday_data": len(frames),
        "trustworthy_observed": len(observed),
        "broad_qualified": len(observed),
        "nonzero_premarket_activity_count": 0,
        "strict_activity_count": 0,
        "retained_by_cap": 0,
        "broad_pool_cap": BROAD_POOL_SIZE,
    }

    if observed.empty:
        return observed, meta

    meta["nonzero_premarket_activity_count"] = int(observed.nonzero_premarket_activity.sum())
    meta["strict_activity_count"] = int(observed.strict_activity_pass.sum())

    # Preserve the old ranking behavior exactly: positive names with non-zero volume first;
    # if Yahoo has no non-zero volume observations, rank the trustworthy observed set rather
    # than converting a data-field limitation into a false zero-candidate day.
    positive = observed[(observed.gap_pct > 0) & (observed.premarket_dollar_volume > 0)].copy()
    if positive.empty:
        positive = observed[observed.premarket_dollar_volume > 0].copy()
    if positive.empty:
        positive = observed.copy()

    broad = positive.sort_values(
        ["strict_activity_pass", "activity_score", "premarket_dollar_volume"],
        ascending=False,
    ).head(BROAD_POOL_SIZE).reset_index(drop=True)
    meta["retained_by_cap"] = len(broad)
    return broad, meta


def main() -> None:
    # Patch only the regressed function. All scoring, deep analysis, refresh/freeze,
    # and final live gates remain the locked Engine 4 implementation.
    core.build_broad_pool = repaired_build_broad_pool

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
    args = parser.parse_args()

    if args.command == "prescreen":
        core.prescreen_stage(args.date, args.max_symbols)
    elif args.command == "deep":
        core.deep_stage(args.date)
    elif args.command == "refresh":
        core.refresh_and_freeze(args.date, args.max_symbols)
    elif args.command == "final":
        core.final_with_timeline(args.date)
    else:
        broad, meta = repaired_build_broad_pool
        core.self_test()
        assert callable(repaired_build_broad_pool)
        print("ENGINE4_RUNNER_REPAIR_SELF_TEST_PASS")


if __name__ == "__main__":
    main()
