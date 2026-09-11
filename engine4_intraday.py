from __future__ import annotations

import argparse
import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from engine4_config import (
    BROAD_POOL_SIZE,
    DEEP_POOL_SIZE,
    ET,
    MAX_GAP_PCT,
    MAX_SPREAD_PCT,
    MIN_ATR_PCT,
    MIN_DOLLAR_VOLUME,
    MIN_GAP_PCT,
    MIN_MARKET_CAP,
    MIN_PREMARKET_DOLLAR_VOLUME,
    MIN_PREMARKET_RVOL,
    MIN_PRICE,
    MIN_SCORE,
    SECTOR_ETF,
    TOP_N,
    WEIGHTS,
)
from engine4_data import (
    catalyst_for,
    data_smoke,
    download_daily_metrics,
    download_intraday,
    historical_premarket_baseline,
    load_baseline,
    now_et,
    prior_regular_close,
    quote_spread,
    slice_window,
)
from engine4_live import live_quality, market_context, opening_structure
from engine4_score import preliminary_activity_score, score_candidate

OUT = Path("output/engine4")
OUT.mkdir(parents=True, exist_ok=True)


def serializable(value):
    if isinstance(value, (np.floating,)):
        value = float(value)
    if isinstance(value, (np.integer,)):
        value = int(value)
    if isinstance(value, float) and not math.isfinite(value):
        return None
    return value


def records_json(frame: pd.DataFrame) -> list[dict]:
    return [{k: serializable(v) for k, v in row.items()} for row in frame.to_dict("records")]


def eligible_baseline() -> pd.DataFrame:
    base = load_baseline()
    base = base[
        (base.price >= MIN_PRICE)
        & (base.market_cap >= MIN_MARKET_CAP)
        & (base.dollar_volume >= MIN_DOLLAR_VOLUME)
    ].copy()
    if base.empty:
        raise RuntimeError("No eligible baseline universe after locked gates")
    return base


def premarket_stage(date_override: str | None = None, max_symbols: int | None = None) -> pd.DataFrame:
    started = time.monotonic()
    reference = now_et() if date_override is None else datetime.fromisoformat(date_override + "T09:25:00").replace(tzinfo=ET)
    date_et = reference.date()

    base = eligible_baseline()
    if max_symbols:
        base = base.head(max_symbols).copy()
    symbols = base.ticker.astype(str).tolist()

    frames = download_intraday(symbols, period="1d", interval="1m", prepost=True, date_et=date_et, lookback_days=1)
    indexed = base.set_index("ticker")
    rows = []
    for symbol in symbols:
        frame = frames.get(symbol)
        if frame is None or frame.empty:
            continue
        pm = slice_window(frame, date_et, "04:00", "09:18")
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
        if gap < MIN_GAP_PCT or gap > MAX_GAP_PCT:
            continue
        if pm_dollar < MIN_PREMARKET_DOLLAR_VOLUME:
            continue
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
            "activity_score": preliminary_activity_score(gap, pm_dollar, daily_dollar),
        })

    broad = pd.DataFrame(rows)
    if broad.empty:
        return write_empty_premarket("No names survived broad premarket gates", started, date_et)
    broad = broad.sort_values(["activity_score", "premarket_dollar_volume"], ascending=False).head(BROAD_POOL_SIZE).reset_index(drop=True)

    deep_symbols = broad.ticker.tolist()
    history = download_intraday(deep_symbols, period="7d", interval="1m", prepost=True, date_et=date_et, lookback_days=7)
    daily = download_daily_metrics(deep_symbols, asof_date=date_et)

    benchmark_symbols = ["SPY", "QQQ"] + sorted({SECTOR_ETF[s] for s in broad.sector if s in SECTOR_ETF})
    benchmarks = download_intraday(benchmark_symbols, period="1d", interval="1m", prepost=True, date_et=date_et, lookback_days=1)
    benchmark_returns = {}
    for symbol, frame in benchmarks.items():
        pm = slice_window(frame, date_et, "04:00", "09:18")
        prev = prior_regular_close(frame, date_et)
        if pm.empty or not math.isfinite(prev) or prev <= 0:
            continue
        close = pd.to_numeric(pm["Close"], errors="coerce").dropna()
        if close.empty:
            continue
        benchmark_returns[symbol] = (float(close.iloc[-1]) / prev - 1.0) * 100.0
    market_return = np.nanmean([benchmark_returns.get("SPY", np.nan), benchmark_returns.get("QQQ", np.nan)])
    if not math.isfinite(market_return):
        market_return = 0.0

    enriched = []
    for row in broad.to_dict("records"):
        symbol = row["ticker"]
        hist = history.get(symbol)
        if hist is None or hist.empty:
            continue
        baseline_volume = historical_premarket_baseline(hist, date_et, "09:18")
        rvol = row["premarket_volume"] / baseline_volume if math.isfinite(baseline_volume) and baseline_volume > 0 else np.nan
        dm = daily.get(symbol, {})
        atr = dm.get("atr", np.nan)
        atr_pct = atr / row["last_premarket"] * 100.0 if atr and math.isfinite(atr) else np.nan
        levels = [dm.get(k, np.nan) for k in ("high_5", "high_20", "high_60")]
        overhead = [x for x in levels if x and math.isfinite(x) and x > row["last_premarket"]]
        resistance = min(overhead) if overhead else np.nan
        room = (resistance / row["last_premarket"] - 1.0) * 100.0 if math.isfinite(resistance) else 10.0
        sector_etf = SECTOR_ETF.get(row["sector"])
        sector_return = benchmark_returns.get(sector_etf, market_return)
        row.update({
            "premarket_rvol": float(rvol),
            "atr_pct": float(atr_pct),
            "resistance_price": float(resistance) if math.isfinite(resistance) else np.nan,
            "resistance_room_pct": float(room),
            "market_relative_strength_pct": float(row["gap_pct"] - market_return),
            "sector_relative_strength_pct": float(row["gap_pct"] - sector_return),
        })
        enriched.append(row)

    deep = pd.DataFrame(enriched)
    if deep.empty:
        return write_empty_premarket("No names had trustworthy deep premarket data", started, date_et)

    deep["deep_prelim"] = (
        deep.gap_pct.clip(0, 15) * 2.0
        + deep.premarket_rvol.fillna(0).clip(0, 6) * 4.0
        + np.log10(deep.premarket_dollar_volume.clip(lower=1)) * 2.0
        + deep.resistance_room_pct.clip(0, 10)
    )
    deep = deep.sort_values("deep_prelim", ascending=False).head(DEEP_POOL_SIZE).copy()

    final_rows = []
    for row in deep.to_dict("records"):
        symbol = row["ticker"]
        catalyst, headline, age_hours = catalyst_for(symbol, reference)
        bid, ask, spread = quote_spread(symbol)
        row.update({
            "catalyst_quality": catalyst,
            "catalyst_headline": headline,
            "catalyst_age_hours": age_hours,
            "bid": bid,
            "ask": ask,
            "spread_pct": spread,
        })

        if catalyst <= 0:
            continue
        if not math.isfinite(row["premarket_rvol"]) or row["premarket_rvol"] < MIN_PREMARKET_RVOL:
            continue
        if not math.isfinite(row["atr_pct"]) or row["atr_pct"] < MIN_ATR_PCT:
            continue
        if row["resistance_room_pct"] <= 0:
            continue
        if not math.isfinite(spread) or spread > MAX_SPREAD_PCT:
            continue

        score, components = score_candidate(row)
        row["score"] = score
        for key, value in components.items():
            row[f"pts_{key}"] = value
        if score >= MIN_SCORE:
            final_rows.append(row)

    if not final_rows:
        return write_empty_premarket("No stock cleared all A-grade premarket gates and 70/100 floor", started, date_et)

    ranked = pd.DataFrame(final_rows).sort_values(
        ["score", "premarket_rvol", "premarket_dollar_volume"], ascending=False
    ).head(TOP_N).reset_index(drop=True)
    ranked.insert(0, "rank", np.arange(1, len(ranked) + 1))
    ranked["frozen_at_et"] = reference.isoformat()
    ranked["runtime_seconds"] = round(time.monotonic() - started, 3)
    ranked.to_csv(OUT / "top25_frozen.csv", index=False)
    (OUT / "top25_frozen.json").write_text(json.dumps({
        "target_date_et": str(date_et),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "requested_top_n": TOP_N,
        "actual_count": len(ranked),
        "runtime_seconds": round(time.monotonic() - started, 3),
        "candidates": records_json(ranked),
    }, indent=2), encoding="utf-8")
    (OUT / "premarket_status.txt").write_text(
        f"TOP25 READY — {len(ranked)} A-grade candidates frozen. Runtime {time.monotonic()-started:.1f}s\n",
        encoding="utf-8",
    )
    return ranked


def write_empty_premarket(reason: str, started: float, date_et) -> pd.DataFrame:
    empty = pd.DataFrame()
    empty.to_csv(OUT / "top25_frozen.csv", index=False)
    payload = {
        "target_date_et": str(date_et),
        "status": "NO_TOP25",
        "reason": reason,
        "runtime_seconds": round(time.monotonic() - started, 3),
        "candidates": [],
    }
    (OUT / "top25_frozen.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    (OUT / "premarket_status.txt").write_text(f"PREMARKET SCREEN — {reason}\n", encoding="utf-8")
    return empty


def final_stage(date_override: str | None = None) -> dict:
    started = time.monotonic()
    reference = now_et() if date_override is None else datetime.fromisoformat(date_override + "T09:45:00").replace(tzinfo=ET)
    date_et = reference.date()
    frozen_path = OUT / "top25_frozen.csv"
    if not frozen_path.exists() or frozen_path.stat().st_size < 5:
        return write_final({
            "status": "NO_TRADE",
            "reason": "missing_top25",
            "message": "NO TRADE — premarket Top 25 unavailable.",
            "runtime_seconds": round(time.monotonic() - started, 3),
        })
    try:
        top = pd.read_csv(frozen_path)
    except Exception:
        top = pd.DataFrame()
    if top.empty or "ticker" not in top.columns:
        return write_final({
            "status": "NO_TRADE",
            "reason": "empty_top25",
            "message": "NO TRADE — no A+ setup.",
            "runtime_seconds": round(time.monotonic() - started, 3),
        })

    symbols = top.ticker.astype(str).tolist()
    candidate_frames = download_intraday(symbols, period="1d", interval="1m", prepost=False, date_et=date_et, lookback_days=0)
    benchmark_symbols = ["SPY", "QQQ"] + sorted({SECTOR_ETF[s] for s in top.sector if s in SECTOR_ETF})
    benchmark_frames = download_intraday(benchmark_symbols, period="1d", interval="1m", prepost=False, date_et=date_et, lookback_days=0)
    market = market_context(benchmark_frames, date_et)

    audit = []
    passes = []
    otherwise_valid_but_missed = False
    for _, row in top.iterrows():
        symbol = str(row.ticker)
        frame = candidate_frames.get(symbol)
        if frame is None or frame.empty:
            audit.append({"ticker": symbol, "pass": False, "failures": ["missing_live_data"]})
            continue
        metrics = opening_structure(symbol, frame, row, market, date_et)
        audit.append(metrics)
        failures = metrics.get("failures", [])
        if metrics.get("pass"):
            quality = live_quality(float(row.get("score", 0)), metrics)
            passes.append((quality, row, metrics))
        elif failures == ["entry_missed"]:
            otherwise_valid_but_missed = True

    (OUT / "final_live_audit.json").write_text(json.dumps({
        "target_date_et": str(date_et),
        "market": {k: serializable(v) for k, v in market.items()},
        "candidates": [{k: serializable(v) for k, v in item.items()} for item in audit],
    }, indent=2), encoding="utf-8")

    if not passes:
        message = "NO TRADE — entry missed." if otherwise_valid_but_missed else "NO TRADE — no A+ setup."
        return write_final({
            "status": "NO_TRADE",
            "reason": "entry_missed" if otherwise_valid_but_missed else "no_a_plus",
            "message": message,
            "runtime_seconds": round(time.monotonic() - started, 3),
        })

    passes.sort(key=lambda item: item[0], reverse=True)
    _, row, metrics = passes[0]
    symbol = str(row.ticker)
    message = (
        f"BUY {symbol} NOW\n"
        f"Entry/trigger: ${metrics['entry_trigger']:.2f}\n"
        f"Initial stop: ${metrics['initial_stop']:.2f}\n"
        f"First management level: ${metrics['first_target']:.2f}\n"
        "Trailing stop: activate only after +1R and a confirmed higher low forms above entry; then trail just below the newest confirmed higher-low/VWAP support and never loosen the stop.\n"
        f"Reason: full A+ gates passed; R:R {metrics['reward_risk']:.2f}:1."
    )
    return write_final({
        "status": "BUY",
        "ticker": symbol,
        "message": message,
        "entry_trigger": metrics["entry_trigger"],
        "initial_stop": metrics["initial_stop"],
        "first_target": metrics["first_target"],
        "reward_risk": metrics["reward_risk"],
        "runtime_seconds": round(time.monotonic() - started, 3),
    })


def write_final(payload: dict) -> dict:
    payload["generated_at_utc"] = datetime.now(timezone.utc).isoformat()
    (OUT / "final_signal.json").write_text(json.dumps({k: serializable(v) for k, v in payload.items()}, indent=2), encoding="utf-8")
    (OUT / "final_alert.txt").write_text(payload["message"] + "\n", encoding="utf-8")
    print(payload["message"], flush=True)
    return payload


def self_test() -> None:
    assert TOP_N == 25
    assert sum(WEIGHTS.values()) == 100.0
    assert MIN_SCORE == 70.0
    print("ENGINE4_SELF_TEST_PASS")


def smoke() -> dict:
    base = eligible_baseline()
    sample = base.ticker.astype(str).head(25).tolist()
    result = data_smoke(sample)
    (OUT / "data_smoke.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["intraday_returned"] < max(10, int(len(sample) * 0.5)):
        raise RuntimeError("Free-data smoke test failed: insufficient intraday coverage")
    return result


def scheduled() -> None:
    et = now_et()
    minutes = et.hour * 60 + et.minute
    if et.weekday() >= 5:
        print("Weekend — Engine 4 does not run")
        return
    if 8 * 60 + 50 <= minutes <= 9 * 60 + 7:
        premarket_stage()
    elif 9 * 60 + 43 <= minutes <= 9 * 60 + 53:
        final_stage()
    else:
        print(f"Ignored schedule wake-up at {et.isoformat()}")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    pre = sub.add_parser("premarket")
    pre.add_argument("--date")
    pre.add_argument("--max-symbols", type=int)
    final = sub.add_parser("final")
    final.add_argument("--date")
    sub.add_parser("smoke")
    sub.add_parser("self-test")
    sub.add_parser("scheduled")
    args = parser.parse_args()

    if args.command == "premarket":
        premarket_stage(args.date, args.max_symbols)
    elif args.command == "final":
        final_stage(args.date)
    elif args.command == "smoke":
        smoke()
    elif args.command == "scheduled":
        scheduled()
    else:
        self_test()


if __name__ == "__main__":
    main()
