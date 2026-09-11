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
    if isinstance(v, np.floating):
        v = float(v)
    if isinstance(v, np.integer):
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


def _write_timeline_text(payload: dict) -> None:
    lines = [f"ENGINE 4 DAILY TIMELINE — {payload.get('market_date_et', '')}"]
    for e in payload.get("events", []):
        try:
            stamp = datetime.fromisoformat(e["time_et"]).strftime("%I:%M:%S %p ET")
        except Exception:
            stamp = e.get("time_et", "")
        lines.append(f"{stamp} — {e.get('stage')} — {e.get('status')}")
        lines.append(f"  {e.get('summary', '')}")
        if e.get("tickers"):
            lines.append("  Stocks: " + ", ".join(e["tickers"]))
        if e.get("details"):
            d = e["details"]
            ordered = [
                "baseline_eligible",
                "trustworthy_observed",
                "broad_qualified",
                "strict_activity_count",
                "retained_by_cap",
                "selected_for_deep",
                "analyzed_count",
                "score70_count",
                "b_grade_count",
                "a_grade_count",
                "runtime_seconds",
            ]
            shown = [f"{k}={d[k]}" for k in ordered if k in d]
            if shown:
                lines.append("  Counts: " + " | ".join(shown))
    (OUT / "timeline.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def log_event(stage: str, status: str, summary: str, tickers: list[str] | None = None, details: dict | None = None) -> None:
    payload = _load_timeline()
    event = {"time_et": _now_iso(), "stage": stage, "status": status, "summary": summary}
    if tickers is not None:
        event["tickers"] = tickers
    if details:
        event["details"] = {k: _ser(v) for k, v in details.items()}
    payload["events"].append(event)
    payload["last_updated_et"] = event["time_et"]
    TIMELINE.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    _write_timeline_text(payload)
    print(f"{event['time_et']} | {stage} | {status} | {summary}", flush=True)


def reset_timeline(date_et) -> None:
    payload = {"market_date_et": str(date_et), "events": []}
    TIMELINE.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    _write_timeline_text(payload)


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


def build_broad_pool(date_et, cutoff: str, max_symbols: int | None = None) -> tuple[pd.DataFrame, dict]:
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
            "broad_qualifier": bool(pm_dollar > 0),
            "strict_activity_pass": bool(gap >= 0.50 and gap <= 25.0 and pm_dollar >= 500_000),
            "activity_score": preliminary_activity_score(gap, max(pm_dollar, 1.0), daily_dollar),
        })

    observed = pd.DataFrame(rows)
    meta = {
        "baseline_eligible": len(base),
        "symbols_with_intraday_data": len(frames),
        "trustworthy_observed": len(observed),
        "broad_qualified": 0,
        "strict_activity_count": 0,
        "retained_by_cap": 0,
        "broad_pool_cap": BROAD_POOL_SIZE,
    }
    if observed.empty:
        return observed, meta

    # Natural broad qualification is intentionally permissive: a baseline-eligible
    # stock with a trustworthy premarket price and non-zero premarket dollar volume.
    # This count is reported BEFORE any configured ranking cap is applied.
    qualified = observed[observed.broad_qualifier].copy()
    meta["broad_qualified"] = len(qualified)
    meta["strict_activity_count"] = int(qualified.strict_activity_pass.sum()) if not qualified.empty else 0
    if qualified.empty:
        return qualified, meta

    broad = qualified.sort_values(
        ["strict_activity_pass", "activity_score", "premarket_dollar_volume"],
        ascending=False,
    ).head(BROAD_POOL_SIZE).reset_index(drop=True)
    meta["retained_by_cap"] = len(broad)
    return broad, meta


def prescreen_stage(date_override: str | None = None, max_symbols: int | None = None) -> pd.DataFrame:
    reference = _reference(date_override, "08:55")
    date_et = reference.date()
    if date_override is None:
        reset_timeline(date_et)
    log_event("PRE-SCREEN", "STARTED", "Broad liquid U.S. universe scan started.")
    started = time.monotonic()
    broad, meta = build_broad_pool(date_et, "09:05", max_symbols)
    runtime = round(time.monotonic() - started, 3)

    if broad.empty:
        log_event(
            "PRE-SCREEN",
            "DATA FAILURE",
            "No stocks met the permissive broad qualification because no trustworthy non-zero premarket activity was available.",
            details={**meta, "runtime_seconds": runtime},
        )
        raise RuntimeError("Engine 4 pre-screen data failure: zero broad-qualified names")

    broad.to_csv(OUT / "prescreen_retained.csv", index=False)
    payload = {
        "target_date_et": str(date_et),
        "generated_at_et": _now_iso(),
        **meta,
        "runtime_seconds": runtime,
        "retained_candidates": _records(broad),
    }
    (OUT / "prescreen_report.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

    log_event(
        "PRE-SCREEN",
        "COMPLETED",
        f"{meta['broad_qualified']} stocks naturally met the broad qualification; the strongest {meta['retained_by_cap']} were retained by the configured Top-{BROAD_POOL_SIZE} cap.",
        tickers=broad.ticker.astype(str).tolist(),
        details={**meta, "runtime_seconds": runtime},
    )
    return broad


def _score_pool(broad: pd.DataFrame, date_et, reference: datetime, cutoff: str) -> pd.DataFrame:
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
    for row in selected.to_dict("records"):
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
    return ranked.sort_values(
        ["premarket_a_grade", "score", "premarket_gate_count", "premarket_rvol", "premarket_dollar_volume"],
        ascending=False,
        na_position="last",
    ).reset_index(drop=True)


def deep_stage(date_override: str | None = None) -> pd.DataFrame:
    reference = _reference(date_override, "09:05")
    date_et = reference.date()
    log_event("DEEP 100-POINT ANALYSIS", "STARTED", "Detailed 100-point analysis started on the highest-ranked retained pre-screen candidates.")
    started = time.monotonic()
    path = OUT / "prescreen_retained.csv"
    if not path.exists() or path.stat().st_size < 5:
        raise RuntimeError("Pre-screen retained candidates missing; refusing to skip stages")

    broad = pd.read_csv(path)
    selected_count = min(DEEP_POOL_SIZE, len(broad))
    ranked = _score_pool(broad, date_et, reference, "09:05")
    if ranked.empty:
        log_event("DEEP 100-POINT ANALYSIS", "DATA FAILURE", "No selected candidates had enough trustworthy data to complete the deep analysis.")
        raise RuntimeError("Engine 4 deep-analysis data failure")

    runtime = round(time.monotonic() - started, 3)
    score70_count = int((ranked.score >= MIN_SCORE).sum())
    a_grade_count = int(ranked.premarket_a_grade.sum())
    b_grade_count = int((ranked.premarket_grade == "B").sum())
    ranked.to_csv(OUT / "deep_ranked.csv", index=False)
    payload = {
        "target_date_et": str(date_et),
        "generated_at_et": _now_iso(),
        "selected_for_deep": selected_count,
        "deep_pool_cap": DEEP_POOL_SIZE,
        "analyzed_count": len(ranked),
        "score70_count": score70_count,
        "b_grade_count": b_grade_count,
        "a_grade_count": a_grade_count,
        "runtime_seconds": runtime,
        "ranked": _records(ranked),
    }
    (OUT / "deep_ranked.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    leaders = ranked.head(10).ticker.astype(str).tolist()

    log_event(
        "DEEP 100-POINT ANALYSIS",
        "COMPLETED",
        f"Top {selected_count} were selected for deep analysis by the configured cap; {len(ranked)} actually completed scoring. Of those, {score70_count} scored >=70 and {a_grade_count} met every strict premarket A-grade gate.",
        tickers=leaders,
        details={
            "selected_for_deep": selected_count,
            "analyzed_count": len(ranked),
            "score70_count": score70_count,
            "b_grade_count": b_grade_count,
            "a_grade_count": a_grade_count,
            "runtime_seconds": runtime,
        },
    )
    return ranked


def refresh_and_freeze(date_override: str | None = None, max_symbols: int | None = None) -> pd.DataFrame:
    reference = _reference(date_override, "09:18")
    date_et = reference.date()
    log_event("09:18 REFRESH + RANKING", "STARTED", "Mandatory fresh full-universe premarket refresh/rerank started.")
    started = time.monotonic()

    broad, meta = build_broad_pool(date_et, "09:18", max_symbols)
    if broad.empty:
        log_event("09:18 REFRESH + RANKING", "DATA FAILURE", "Refresh produced zero naturally broad-qualified names.", details=meta)
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
        **meta,
        "selected_for_deep": min(DEEP_POOL_SIZE, len(broad)),
        "refresh_analyzed_count": len(ranked_all),
        "score70_count": int((ranked_all.score >= MIN_SCORE).sum()),
        "requested_top_n": TOP_N,
        "actual_count": len(top),
        "a_grade_count": int(top.premarket_a_grade.sum()),
        "runtime_seconds": runtime,
        "candidates": _records(top),
    }
    (OUT / "top25_frozen.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    (OUT / "premarket_status.txt").write_text(
        f"REFRESH: {meta['broad_qualified']} naturally broad-qualified; {meta['retained_by_cap']} retained by Top-{BROAD_POOL_SIZE} cap; {len(ranked_all)} completed refreshed deep scoring; Top {len(top)} frozen; {payload['a_grade_count']} strict A-grade. Runtime {runtime:.1f}s\n",
        encoding="utf-8",
    )

    log_event(
        "TOP-25 FREEZE",
        "COMPLETED",
        f"Refresh found {meta['broad_qualified']} naturally broad-qualified names; {meta['retained_by_cap']} were retained by cap, {len(ranked_all)} completed refreshed deep scoring, and the best {len(top)} were frozen for the 09:45 live confirmation.",
        tickers=top.ticker.astype(str).tolist(),
        details={
            **meta,
            "selected_for_deep": min(DEEP_POOL_SIZE, len(broad)),
            "analyzed_count": len(ranked_all),
            "score70_count": int((ranked_all.score >= MIN_SCORE).sum()),
            "a_grade_count": int(top.premarket_a_grade.sum()),
            "runtime_seconds": runtime,
        },
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
        details={
            "runtime_seconds": round(time.monotonic() - started, 3),
            "status": result.get("status"),
            "reason": result.get("reason"),
        },
    )
    return result


def self_test() -> None:
    assert TOP_N == 25
    assert BROAD_POOL_SIZE >= TOP_N
    assert DEEP_POOL_SIZE >= TOP_N
    assert BROAD_POOL_SIZE == 100
    assert DEEP_POOL_SIZE == 60
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
