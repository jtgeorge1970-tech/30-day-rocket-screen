from __future__ import annotations

import json
import math
import os
from datetime import datetime, time
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

import engine4_pipeline as core
import engine4_pipeline_runner as runner
from engine4_config import (
    BROAD_POOL_SIZE, DEEP_POOL_SIZE, MAX_TRADABLE_PRICE,
    MIN_ATR_PCT, MIN_PREMARKET_RVOL, MIN_SCORE, SECTOR_ETF
)
from engine4_data import download_daily_metrics, download_intraday, prior_regular_close, slice_window
from engine4_score import preliminary_activity_score, score_candidate, premarket_grade

ET = ZoneInfo("America/New_York")
OUT = core.OUT
WINDOW_START = "15:00"
WINDOW_END = "16:00"


def fnum(v, default=math.nan):
    try:
        x = float(v)
        return x if math.isfinite(x) else default
    except Exception:
        return default


def same_hour_baseline(hist: pd.DataFrame, date_et) -> float:
    if hist is None or hist.empty:
        return math.nan
    vols = []
    for d in sorted({ts.date() for ts in hist.index if ts.date() < date_et})[-5:]:
        w = slice_window(hist, d, WINDOW_START, WINDOW_END)
        if not w.empty and "Volume" in w.columns:
            v = float(pd.to_numeric(w["Volume"], errors="coerce").fillna(0).sum())
            if v > 0:
                vols.append(v)
    return float(np.median(vols)) if vols else math.nan


def main():
    date_s = os.environ.get("ENGINE4_CLOSE_DATE_ET") or str(datetime.now(ET).date())
    date_et = datetime.fromisoformat(date_s).date()
    OUT.mkdir(parents=True, exist_ok=True)
    core.reset_timeline(date_et)

    # STAGE 1 — broad universe using only 15:00-16:00 ET bars.
    core.log_event("CLOSE-HOUR STAGE 1", "STARTED", "Scanning eligible universe using only 15:00-16:00 ET one-minute bars.")
    base = core.eligible_baseline()
    symbols = base.ticker.astype(str).tolist()
    frames = download_intraday(symbols, period="1d", interval="1m", prepost=False, date_et=date_et, lookback_days=1)
    idx = base.set_index("ticker")
    rows = []
    for sym in symbols:
        fr = frames.get(sym)
        if fr is None or fr.empty:
            continue
        w = slice_window(fr, date_et, WINDOW_START, WINDOW_END)
        if w.empty or "Close" not in w.columns or "Volume" not in w.columns:
            continue
        closes = pd.to_numeric(w["Close"], errors="coerce").dropna()
        vols = pd.to_numeric(w["Volume"], errors="coerce").fillna(0)
        if len(closes) < 2:
            continue
        start_px = float(closes.iloc[0]); last_px = float(closes.iloc[-1])
        if start_px <= 0 or last_px <= 0:
            continue
        prior = prior_regular_close(fr, date_et)
        if not math.isfinite(prior) or prior <= 0:
            prior = fnum(idx.at[sym, "price"], last_px)
        hour_vol = float(vols.sum())
        hour_dollar = hour_vol * last_px
        hour_ret = (last_px / start_px - 1.0) * 100.0
        day_ret = (last_px / prior - 1.0) * 100.0
        adv_dollar = fnum(idx.at[sym, "dollar_volume"], 0.0)
        rows.append({
            "ticker": sym,
            "name": str(idx.at[sym, "name"]),
            "sector": str(idx.at[sym, "sector"]),
            "market_cap": fnum(idx.at[sym, "market_cap"]),
            "avg_daily_dollar_volume": adv_dollar,
            "previous_close": prior,
            "window_start_price": start_px,
            "last_premarket": last_px,
            "premarket_volume": hour_vol,
            "premarket_dollar_volume": hour_dollar,
            "gap_pct": day_ret,
            "hour_return_pct": hour_ret,
            "activity_score": preliminary_activity_score(day_ret, max(hour_dollar, 1.0), adv_dollar),
            "strict_activity_pass": bool(hour_dollar >= 500000 and last_px <= MAX_TRADABLE_PRICE),
        })
    broad_all = pd.DataFrame(rows)
    if broad_all.empty:
        raise RuntimeError("Close-hour Stage 1 produced zero trustworthy names")
    broad = broad_all.sort_values(
        ["strict_activity_pass", "hour_return_pct", "premarket_dollar_volume", "activity_score"],
        ascending=[False, False, False, False],
    ).head(BROAD_POOL_SIZE).reset_index(drop=True)
    broad.to_csv(OUT / "close_hour_stage1.csv", index=False)
    core.log_event("CLOSE-HOUR STAGE 1", "COMPLETED",
        f"{len(broad_all)} names had trustworthy 15:00-16:00 ET data; Top-{len(broad)} retained.",
        tickers=broad.head(10).ticker.tolist(),
        details={"observed": len(broad_all), "retained": len(broad), "window": "15:00-16:00 ET"})

    # STAGE 2 — deep analysis, including same-hour RVOL versus prior sessions.
    core.log_event("CLOSE-HOUR STAGE 2", "STARTED", "Deep scoring strongest close-hour candidates.")
    selected = broad.head(DEEP_POOL_SIZE).copy()
    syms = selected.ticker.astype(str).tolist()
    hist = download_intraday(syms, period="7d", interval="1m", prepost=False, date_et=date_et, lookback_days=7)
    daily = download_daily_metrics(syms, asof_date=date_et)
    bench_syms = ["SPY", "QQQ"] + sorted({SECTOR_ETF[s] for s in selected.sector if s in SECTOR_ETF})
    bench = download_intraday(bench_syms, period="1d", interval="1m", prepost=False, date_et=date_et, lookback_days=1)
    bench_ret = {}
    for sym, fr in bench.items():
        w = slice_window(fr, date_et, WINDOW_START, WINDOW_END)
        if not w.empty and "Close" in w.columns:
            cc = pd.to_numeric(w["Close"], errors="coerce").dropna()
            if len(cc) >= 2:
                bench_ret[sym] = (float(cc.iloc[-1]) / float(cc.iloc[0]) - 1.0) * 100.0
    market_hour = float(np.nanmean([bench_ret.get("SPY", np.nan), bench_ret.get("QQQ", np.nan)]))
    if not math.isfinite(market_hour):
        market_hour = 0.0

    ranked_rows = []
    reference = datetime.combine(date_et, time(16, 0), tzinfo=ET)
    for row in selected.to_dict("records"):
        sym = row["ticker"]
        h = hist.get(sym)
        baseline = same_hour_baseline(h, date_et)
        rvol = row["premarket_volume"] / baseline if math.isfinite(baseline) and baseline > 0 else math.nan
        dm = daily.get(sym, {})
        atr = fnum(dm.get("atr"))
        atr_pct = atr / row["last_premarket"] * 100.0 if math.isfinite(atr) and row["last_premarket"] > 0 else math.nan
        levels = [fnum(dm.get(k)) for k in ("high_5", "high_20", "high_60")]
        overhead = [x for x in levels if math.isfinite(x) and x > row["last_premarket"]]
        resistance = min(overhead) if overhead else math.nan
        room = (resistance / row["last_premarket"] - 1.0) * 100.0 if math.isfinite(resistance) else 10.0
        sector_ret = bench_ret.get(SECTOR_ETF.get(row["sector"]), market_hour)
        catalyst, headline, age_hours, catalyst_source = runner.provider_catalyst_with_source(sym, reference, row.get("name"))
        row.update({
            "premarket_rvol": fnum(rvol),
            "premarket_volume_metric_source": "historical_same_hour_15_16_rvol",
            "premarket_volume_gate_pass": bool(math.isfinite(rvol) and rvol >= MIN_PREMARKET_RVOL),
            "premarket_volume_intensity_pct": math.nan,
            "atr_pct": fnum(atr_pct),
            "resistance_price": fnum(resistance),
            "resistance_room_pct": fnum(room),
            "market_relative_strength_pct": row["hour_return_pct"] - market_hour,
            "sector_relative_strength_pct": row["hour_return_pct"] - sector_ret,
            "catalyst_quality": catalyst,
            "catalyst_headline": headline,
            "catalyst_age_hours": age_hours,
            "catalyst_source": catalyst_source,
            "bid": math.nan, "ask": math.nan, "spread_pct": math.nan,
            "spread_source": "UNAVAILABLE_FOR_HISTORICAL_16:00_REPLAY",
            "spread_order_authoritative": False,
        })
        score, comps = score_candidate(row)
        row["score"] = float(score)
        for k, v in comps.items():
            row[f"pts_{k}"] = v
        evidence = {
            "catalyst": catalyst > 0,
            "hour_volume_strength": bool(row["premarket_volume_gate_pass"]),
            "atr": math.isfinite(atr_pct) and atr_pct >= MIN_ATR_PCT,
            "room": room > 0,
            "price_cap": row["last_premarket"] <= MAX_TRADABLE_PRICE,
        }
        evidence_pass = all(evidence.values())
        row["replay_evidence_pass"] = bool(evidence_pass)
        row["score80"] = bool(score >= MIN_SCORE)
        row["replay_grade"] = premarket_grade(score, evidence_pass)
        row["historical_order_gate"] = "NOT_VERIFIABLE_NO_16:00_BID_ASK"
        ranked_rows.append(row)

    ranked = pd.DataFrame(ranked_rows).sort_values(
        ["replay_evidence_pass", "score", "hour_return_pct", "premarket_rvol"],
        ascending=[False, False, False, False],
        na_position="last",
    ).reset_index(drop=True)
    ranked.to_csv(OUT / "close_hour_stage2_ranked.csv", index=False)
    core.log_event("CLOSE-HOUR STAGE 2", "COMPLETED",
        f"{len(ranked)} candidates completed close-hour deep scoring.",
        tickers=ranked.head(10).ticker.tolist(),
        details={"analyzed": len(ranked), "score80": int((ranked.score >= MIN_SCORE).sum())})

    # STAGE 3 — freeze strongest evidence-passing B-or-better names.
    core.log_event("CLOSE-HOUR STAGE 3", "STARTED", "Ranking and freezing close-hour shortlist.")
    eligible = ranked[(ranked.score >= MIN_SCORE) & (ranked.replay_evidence_pass)].copy()
    frozen = eligible.head(25).copy().reset_index(drop=True)
    frozen.insert(0, "rank", range(1, len(frozen)+1))
    frozen.to_csv(OUT / "close_hour_stage3_frozen.csv", index=False)
    core.log_event("CLOSE-HOUR STAGE 3", "COMPLETED",
        f"{len(frozen)} candidates frozen from today's 15:00-16:00 ET replay.",
        tickers=frozen.ticker.tolist(),
        details={"actual_count": len(frozen)})

    # STAGE 4 — closing-structure confirmation from the final 20 minutes only.
    core.log_event("CLOSE-HOUR STAGE 4", "STARTED", "Confirming final-20-minute structure on frozen candidates.")
    confirmations = []
    for row in frozen.to_dict("records"):
        fr = frames.get(row["ticker"])
        w = slice_window(fr, date_et, "15:40", "16:00") if fr is not None else pd.DataFrame()
        status = "NO_CONFIRMATION"
        reason = "insufficient_final20_data"
        if not w.empty and "Close" in w.columns:
            cc = pd.to_numeric(w["Close"], errors="coerce").dropna()
            if len(cc) >= 5:
                first = float(cc.iloc[0]); last = float(cc.iloc[-1]); low = float(cc.min()); high = float(cc.max())
                ret20 = (last / first - 1.0) * 100.0
                off_low = (last / low - 1.0) * 100.0 if low > 0 else 0.0
                near_high = (high - last) / high * 100.0 if high > 0 else math.nan
                if ret20 > 0 and off_low >= 0.5 and near_high <= 1.5:
                    status = "CLOSE_HOUR_HOLD"
                    reason = "positive_final20_near_high"
                else:
                    reason = "final20_not_strong_enough"
                confirmations.append({**row, "final20_return_pct": ret20, "final20_off_low_pct": off_low,
                    "final20_from_high_pct": near_high, "confirmation_status": status, "confirmation_reason": reason})
                continue
        confirmations.append({**row, "final20_return_pct": math.nan, "final20_off_low_pct": math.nan,
            "final20_from_high_pct": math.nan, "confirmation_status": status, "confirmation_reason": reason})
    conf = pd.DataFrame(confirmations)
    if not conf.empty:
        conf.to_csv(OUT / "close_hour_stage4_confirmation.csv", index=False)
    core.log_event("CLOSE-HOUR STAGE 4", "COMPLETED",
        "Closing-structure confirmation finished.",
        tickers=conf[conf.confirmation_status == "CLOSE_HOUR_HOLD"].ticker.tolist() if not conf.empty else [],
        details={"confirmed": int((conf.confirmation_status == "CLOSE_HOUR_HOLD").sum()) if not conf.empty else 0})

    # STAGE 5 — replay result. No historical BUY claim because exact 16:00 bid/ask is unavailable.
    holds = conf[conf.confirmation_status == "CLOSE_HOUR_HOLD"].copy() if not conf.empty else pd.DataFrame()
    result = {
        "target_date_et": str(date_et),
        "window_et": "15:00-16:00",
        "generated_at_et": datetime.now(ET).isoformat(),
        "baseline_eligible": len(base),
        "stage1_observed": len(broad_all),
        "stage1_retained": len(broad),
        "stage2_analyzed": len(ranked),
        "stage2_score80": int((ranked.score >= MIN_SCORE).sum()),
        "stage3_frozen": len(frozen),
        "stage4_confirmed": len(holds),
        "status": "REPLAY_COMPLETE",
        "execution_status": "NOT_APPLICABLE_HISTORICAL_BID_ASK_UNAVAILABLE",
        "leaders": holds.head(10)[["ticker","score","replay_grade","hour_return_pct","premarket_rvol","catalyst_headline"]].to_dict("records") if not holds.empty else [],
    }
    (OUT / "close_hour_final_report.json").write_text(json.dumps(result, indent=2, default=str), encoding="utf-8")
    core.log_event("CLOSE-HOUR STAGE 5", "COMPLETED",
        "Close-hour replay complete. Historical order execution is intentionally not claimed.",
        tickers=[x["ticker"] for x in result["leaders"]],
        details=result)
    print("ENGINE4_CLOSE_HOUR_REPLAY_COMPLETE")
    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
