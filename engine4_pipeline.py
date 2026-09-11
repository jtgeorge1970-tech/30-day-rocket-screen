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
    MAX_SPREAD_PCT,
    MIN_ATR_PCT,
    MIN_DOLLAR_VOLUME,
    MIN_MARKET_CAP,
    MIN_PREMARKET_RVOL,
    MIN_PRICE,
    MIN_SCORE,
    SECTOR_ETF,
    TOP_N,
)
from engine4_data import (
    catalyst_for,
    download_daily_metrics,
    download_intraday,
    historical_premarket_baseline,
    load_baseline,
    now_et,
    prior_regular_close,
    quote_spread,
    slice_window,
)
from engine4_intraday import final_stage
from engine4_score import preliminary_activity_score, score_candidate

OUT = Path("output/engine4")
OUT.mkdir(parents=True, exist_ok=True)
TIMELINE = OUT / "timeline.json"


def _ser(v):
    if isinstance(v, (np.floating,)):
        v = float(v)
    if isinstance(v, (np.integer,)):
        v = int(v)
    if isinstance(v, float) and not math.isfinite(v):
        return None
    return v


def _records(df: pd.DataFrame) -> list[dict]:
    return [{k: _ser(v) for k, v in row.items()} for row in df.to_dict("records")]


def _now_iso() -> str:
    return now_et().isoformat()


def _load_timeline() -> dict:
    if TIMELINE.exists():
        try:
            return json.loads(TIMELINE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"market_date_et": str(now_et().date()), "events": []}


def log_event(stage: str, status: str, summary: str, tickers: list[str] | None = None, details: dict | None = None) -> None:
    payload = _load_timeline()
    event = {
        "time_et": _now_iso(),
        "stage": stage,
        "status": status,
        "summary": summary,
    }
    if tickers is not None:
        event["tickers"] = tickers
    if details:
        event["details"] = {k: _ser(v) for k, v in details.items()}
    payload["events"].append(event)
    payload["last_updated_et"] = event["time_et"]
    TIMELINE.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    _write_timeline_text(payload)
    print(f"{event['time_et']} | {stage} | {status} | {summary}", flush=True)


def _write_timeline_text(payload: dict) -> None:
    lines = [f"ENGINE 4 DAILY TIMELINE — {payload.get('market_date_et','')}"]
    for e in payload.get("events", []):
        try:
            stamp = datetime.fromisoformat(e["time_et"]).strftime("%I:%M:%S %p ET")
        except Exception:
            stamp = e.get("time_et", "")
        lines.append(f"{stamp} — {e.get('stage')} — {e.get('status')}")
        lines.append(f"  {e.get('summary','')}")
        if e.get("tickers"):
            lines.append("  Stocks: " + ", ".join(e["tickers"]))
    (OUT / "timeline.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def reset_timeline(date_et) -> None:
    TIMELINE.write_text(json.dumps({"market_date_et": str(date_et), "events": []}, indent=2), encoding="utf-8")
    _write_timeline_text({"market_date_et": str(date_et), "events": []})


def eligible_baseline() -> pd.DataFrame:
    base = load_baseline()
    base = base[
        (base.price >= MIN_PRICE)
        & (base.market_cap >= MIN_MARKET_CAP)
        & (base.dollar_volume >= MIN_DOLLAR_VOLUME)
    ].copy()
    if base.empty:
        raise RuntimeError("No eligible baseline universe after baseline investability gates")
    return base


def _reference(date_override: str | None, hhmm: str) -> datetime:
    if date_override is None:
        return now_et()
    return datetime.fromisoformat(f"{date_override}T{hhmm}:00").replace(tzinfo=ET)


def build_broad_pool(date_et, cutoff: str, max_symbols: int | None = None) -> tuple[pd.DataFrame, int, int]:
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
            "strict_activity_pass": bool(gap >= 0.50 and gap <= 25.0 and pm_dollar >= 500_000),
            "activity_score": preliminary_activity_score(gap, max(pm_dollar, 1.0), daily_dollar),
        })
    observed = pd.DataFrame(rows)
    if observed.empty:
        return observed, len(base), len(frames)

    # The pre-screen is intentionally broad. It ranks liquid, investable names with
    # trustworthy premarket observations instead of using the former hard gap/volume
    # gates as an all-or-nothing kill switch. Negative/flat names naturally rank lower.
    positive = observed[(observed.gap_pct > 0) & (observed.premarket_dollar_volume > 0)].copy()
    if positive.empty:
        positive = observed[observed.premarket_dollar_volume > 0].copy()
    if positive.empty:
        positive = observed.copy()
    broad = positive.sort_values(
        ["strict_activity_pass", "activity_score", "premarket_dollar_volume"],
        ascending=False,
    ).head(BROAD_POOL_SIZE).reset_index(drop=True)
    return broad, len(base), len(frames)


def prescreen_stage(date_override: str | None = None, max_symbols: int | None = None) -> pd.DataFrame:
    reference = _reference(date_override, "08:55")
    date_et = reference.date()
    if date_override is None:
        reset_timeline(date_et)
    log_event("PRE-SCREEN", "STARTED", "Broad liquid U.S. universe scan started.")
    started = time.monotonic()
    broad, baseline_count, data_count = build_broad_pool(date_et, "09:05", max_symbols)
    if broad.empty:
        log_event(
            "PRE-SCREEN",
            "DATA FAILURE",
            "No trustworthy premarket observations were returned; this is a data failure, not a valid zero-stock screen.",
            details={"baseline_eligible": baseline_count, "symbols_with_intraday_data": data_count},
        )
        raise RuntimeError("Engine 4 pre-screen data failure: zero trustworthy observations")
    broad.to_csv(OUT / "prescreen_survivors.csv", index=False)
    payload = {
        "target_date_et": str(date_et),
        "generated_at_et": _now_iso(),
        "baseline_eligible": baseline_count,
        "symbols_with_intraday_data": data_count,
        "survivor_count": len(broad),
        "runtime_seconds": round(time.monotonic() - started, 3),
        "survivors": _records(broad),
    }
    (OUT / "prescreen_survivors.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    log_event(
        "PRE-SCREEN",
        "COMPLETED",
        f"{len(broad)} stocks survived the broad pre-screen from {baseline_count} baseline-eligible stocks.",
        tickers=broad.ticker.astype(str).tolist(),
        details={"runtime_seconds": payload["runtime_seconds"], "strict_activity_names": int(broad.strict_activity_pass.sum())},
    )
    return broad


def _score_pool(broad: pd.DataFrame, date_et, reference: datetime, cutoff: str) -> pd.DataFrame:
    deep_symbols = broad.ticker.astype(str).head(DEEP_POOL_SIZE).tolist()
    history = download_intraday(deep_symbols, period="7d", interval="1m", prepost=True, date_et=date_et, lookback_days=7)
    daily = download_daily_metrics(deep_symbols, asof_date=date_et)
    benchmark_symbols = ["SPY", "QQQ"] + sorted({SECTOR_ETF[s] for s in broad.sector if s in SECTOR_ETF})
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
    for row in broad.head(DEEP_POOL_SIZE).to_dict("records"):
        symbol = row["ticker"]
        hist = history.get(symbol)
        if hist is None or hist.empty:
            continue
        baseline_volume = historical_premarket_baseline(hist, date_et, cutoff)
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
        catalyst, headline, age_hours = catalyst_for(symbol, reference)
        bid, ask, spread = quote_spread(symbol)
        row.update({
            "premarket_rvol": float(rvol),
            "atr_pct": float(atr_pct),
            "resistance_price": float(resistance) if math.isfinite(resistance) else np.nan,
            "resistance_room_pct": float(room),
            "market_relative_strength_pct": float(row["gap_pct"] - market_return),
            "sector_relative_strength_pct": float(row["gap_pct"] - sector_return),
            "catalyst_quality": catalyst,
            "catalyst_headline": headline,
            "catalyst_age_hours": age_hours,
            "bid": bid,
            "ask": ask,
            "spread_pct": spread,
        })
        score, components = score_candidate(row)
        row["score"] = score
        for key, value in components.items():
            row[f"pts_{key}"] = value
        gate_map = {
            "catalyst": catalyst > 0,
            "rvol": math.isfinite(rvol) and rvol >= MIN_PREMARKET_RVOL,
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
    ranked = ranked.sort_values(
        ["premarket_a_grade", "score", "premarket_gate_count", "premarket_rvol", "premarket_dollar_volume"],
        ascending=False,
        na_position="last",
    ).reset_index(drop=True)
    return ranked


def deep_stage(date_override: str | None = None) -> pd.DataFrame:
    reference = _reference(date_override, "09:05")
    date_et = reference.date()
    log_event("DEEP 100-POINT ANALYSIS", "STARTED", "Detailed catalyst, RVOL, ATR, liquidity, resistance, relative-strength and spread scoring started.")
    started = time.monotonic()
    path = OUT / "prescreen_survivors.csv"
    if not path.exists() or path.stat().st_size < 5:
        raise RuntimeError("Pre-screen survivors missing; refusing to skip stages")
    broad = pd.read_csv(path)
    ranked = _score_pool(broad, date_et, reference, "09:05")
    if ranked.empty:
        log_event("DEEP 100-POINT ANALYSIS", "DATA FAILURE", "No names had enough trustworthy deep-analysis data.")
        raise RuntimeError("Engine 4 deep-analysis data failure")
    ranked.to_csv(OUT / "deep_ranked.csv", index=False)
    (OUT / "deep_ranked.json").write_text(json.dumps({
        "target_date_et": str(date_et),
        "generated_at_et": _now_iso(),
        "analyzed_count": len(ranked),
        "runtime_seconds": round(time.monotonic() - started, 3),
        "ranked": _records(ranked),
    }, indent=2), encoding="utf-8")
    leaders = ranked.head(10).ticker.astype(str).tolist()
    log_event(
        "DEEP 100-POINT ANALYSIS",
        "COMPLETED",
        f"{len(ranked)} stocks completed the 100-point analysis; {int(ranked.premarket_a_grade.sum())} met every former A-grade premarket gate. Near-misses remain ranked for the 09:45 live test instead of being discarded early.",
        tickers=leaders,
        details={"runtime_seconds": round(time.monotonic() - started, 3)},
    )
    return ranked


def refresh_and_freeze(date_override: str | None = None, max_symbols: int | None = None) -> pd.DataFrame:
    reference = _reference(date_override, "09:18")
    date_et = reference.date()
    log_event("09:18 REFRESH + RANKING", "STARTED", "Mandatory fresh full-universe premarket refresh/rerank started.")
    started = time.monotonic()
    broad, baseline_count, data_count = build_broad_pool(date_et, "09:18", max_symbols)
    if broad.empty:
        log_event("09:18 REFRESH + RANKING", "DATA FAILURE", "Refresh returned zero trustworthy premarket observations; refusing to call this a valid zero-stock result.")
        raise RuntimeError("Engine 4 refresh data failure")
    ranked_all = _score_pool(broad, date_et, reference, "09:18")
    if ranked_all.empty:
        log_event("09:18 REFRESH + RANKING", "DATA FAILURE", "Refresh produced no trustworthy scored names.")
        raise RuntimeError("Engine 4 refresh scoring failure")

    top = ranked_all.head(TOP_N).copy().reset_index(drop=True)
    top.insert(0, "rank", np.arange(1, len(top) + 1))
    top["frozen_at_et"] = _now_iso()
    runtime = round(time.monotonic() - started, 3)
    top["runtime_seconds"] = runtime
    top.to_csv(OUT / "top25_frozen.csv", index=False)
    payload = {
        "target_date_et": str(date_et),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "generated_at_et": _now_iso(),
        "requested_top_n": TOP_N,
        "actual_count": len(top),
        "a_grade_count": int(top.premarket_a_grade.sum()),
        "baseline_eligible": baseline_count,
        "symbols_with_intraday_data": data_count,
        "runtime_seconds": runtime,
        "candidates": _records(top),
    }
    (OUT / "top25_frozen.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    (OUT / "premarket_status.txt").write_text(
        f"TOP 25 FROZEN — {len(top)} ranked candidates; {payload['a_grade_count']} strict premarket A-grade. Runtime {runtime:.1f}s\n",
        encoding="utf-8",
    )
    log_event(
        "TOP-25 FREEZE",
        "COMPLETED",
        f"Top {len(top)} ranked candidates frozen for the 09:45 live confirmation. {payload['a_grade_count']} are strict premarket A-grade; the rest are high-ranked watch candidates that must prove themselves live.",
        tickers=top.ticker.astype(str).tolist(),
        details={"runtime_seconds": runtime},
    )
    return top


def final_with_timeline(date_override: str | None = None) -> dict:
    log_event("FINAL 09:45 LIVE CONFIRMATION", "STARTED", "Opening-range/VWAP/volume/relative-strength confirmation started on the frozen shortlist only.")
    started = time.monotonic()
    result = final_stage(date_override)
    log_event(
        "FINAL 09:45 LIVE CONFIRMATION",
        "COMPLETED",
        result.get("message", "Final stage completed."),
        tickers=[result["ticker"]] if result.get("ticker") else [],
        details={"runtime_seconds": round(time.monotonic() - started, 3), "status": result.get("status"), "reason": result.get("reason")},
    )
    return result


def self_test() -> None:
    assert TOP_N == 25
    assert BROAD_POOL_SIZE >= TOP_N
    assert DEEP_POOL_SIZE >= TOP_N
    print("ENGINE4_PIPELINE_SELF_TEST_PASS")


def main() -> None:
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
        prescreen_stage(args.date, args.max_symbols)
    elif args.command == "deep":
        deep_stage(args.date)
    elif args.command == "refresh":
        refresh_and_freeze(args.date, args.max_symbols)
    elif args.command == "final":
        final_with_timeline(args.date)
    else:
        self_test()


if __name__ == "__main__":
    main()
