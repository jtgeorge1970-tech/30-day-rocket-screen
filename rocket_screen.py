"""Quality Loser Reversal Engine V2.

Market-wide candidate and entry engine. It starts with recent losers, rejects
investability failures, and requires evidence of a formed bottom. It never
claims a current catalyst, intact thesis, or BUY from quantitative data alone.
"""
from __future__ import annotations

import io
import json
import math
import os
import random
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import requests
import yfinance as yf

OUT = Path("output")
OUT.mkdir(exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 quality-loser-reversal research"}

YAHOO_RATE_CAP_PER_MINUTE = 100
YAHOO_MIN_INTERVAL = 60.0 / YAHOO_RATE_CAP_PER_MINUTE
YAHOO_PRICE_BATCH_SIZE = 10
MAX_PRICE_REQUEST_FAILURE_RATE = 0.01
FUNDAMENTALS_CACHE_TTL_HOURS = 18
MIN_PRICE = 3.0
MIN_DOLLAR_VOLUME = 2_000_000
MIN_MARKET_CAP = 200_000_000
MIN_HEADROOM = 0.15
MAX_SUPPORT_DISTANCE = 0.08
MAX_DISTANCE_FROM_60D_LOW = 0.12
MIN_FUNDAMENTAL_COVERAGE = 0.60
MIN_STABILITY_SESSIONS = 2
VERIFICATION_MAX_AGE_HOURS = 24
_next_yahoo_call = 0.0


def yahoo_pace(request_units=1):
    global _next_yahoo_call
    wait = _next_yahoo_call - time.monotonic()
    if wait > 0:
        time.sleep(wait)
    _next_yahoo_call = time.monotonic() + YAHOO_MIN_INTERVAL * max(1, int(request_units))


def retry_yahoo(fn, label, attempts=6, request_units=1, validator=None):
    last = None
    for attempt in range(attempts):
        yahoo_pace(request_units=request_units)
        try:
            result = fn()
            if validator is not None and not validator(result):
                raise RuntimeError("Yahoo returned an empty or unusable response")
            return result
        except Exception as exc:
            last = exc
            if attempt == attempts - 1:
                break
            delay = min(60, 3 * (2**attempt)) + random.uniform(0, 2)
            print(f"Yahoo retry {attempt + 1}/{attempts - 1} for {label}: {exc}; sleeping {delay:.1f}s", flush=True)
            time.sleep(delay)
    print(f"Yahoo failed after retries for {label}: {last}", flush=True)
    return None


def valid_price_download(data):
    return data is not None and not data.empty and "Close" in data.columns and bool(data["Close"].notna().to_numpy().any())


def universe():
    urls = [
        "https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt",
        "https://www.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt",
    ]
    frames = []
    for url in urls:
        response = requests.get(url, headers=UA, timeout=30)
        response.raise_for_status()
        frames.append(pd.read_csv(io.StringIO(response.text), sep="|"))
    a, b = frames
    a = a.rename(columns={"Symbol": "ticker", "Security Name": "name", "ETF": "etf", "Test Issue": "test"})
    b = b.rename(columns={"ACT Symbol": "ticker", "Security Name": "name", "ETF": "etf", "Test Issue": "test"})
    x = pd.concat([a[["ticker", "name", "etf", "test"]], b[["ticker", "name", "etf", "test"]]], ignore_index=True)
    x = x[(x.etf == "N") & (x.test == "N")].dropna(subset=["ticker"])
    x = x[~x.ticker.str.contains(r"[.$]", regex=True)]
    bad = r"Warrant|Right| Unit|Preferred|Depositary Shares|Acquisition Corp|SPAC"
    x = x[~x.name.str.contains(bad, case=False, na=False, regex=True)]
    return x.drop_duplicates("ticker").reset_index(drop=True)


def pct_rank(series):
    return pd.to_numeric(series, errors="coerce").rank(pct=True) * 100


def weighted_available_score(factors):
    """Renormalize around observed evidence; never invent a neutral value."""
    numerator = denominator = None
    total_weight = sum(weight for _, weight in factors)
    for series, weight in factors:
        numeric = pd.to_numeric(series, errors="coerce")
        available = numeric.notna().astype(float)
        contribution = numeric.fillna(0) * weight
        weight_available = available * weight
        numerator = contribution if numerator is None else numerator + contribution
        denominator = weight_available if denominator is None else denominator + weight_available
    return numerator / denominator.replace(0, np.nan), denominator / total_weight


def load_fresh_checkpoint(checkpoint):
    if not checkpoint.exists():
        return {}
    try:
        frame = pd.read_csv(checkpoint)
    except Exception:
        return {}
    if not {"ticker", "retrieved_at"}.issubset(frame.columns):
        return {}
    now = datetime.now(timezone.utc)
    fresh = {}
    for row in frame.to_dict("records"):
        try:
            dt = datetime.fromisoformat(str(row["retrieved_at"]).replace("Z", "+00:00"))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            age = (now - dt.astimezone(timezone.utc)).total_seconds() / 3600
        except Exception:
            continue
        if 0 <= age <= FUNDAMENTALS_CACHE_TTL_HOURS:
            fresh[row["ticker"]] = row
    return fresh


FUNDAMENTAL_COLUMNS = [
    "ticker", "retrieved_at", "market_cap", "avg_volume", "revenue_growth",
    "earnings_growth", "earnings_q_growth", "forward_pe", "target_upside",
    "recommendation", "sector", "industry", "total_cash", "total_debt",
    "operating_cashflow", "free_cashflow", "current_ratio", "debt_to_equity",
]


def fundamentals(tickers):
    rows, checkpoint = [], OUT / "fundamentals_checkpoint.csv"
    fresh_cache = load_fresh_checkpoint(checkpoint)
    reused = downloaded = 0
    for i, ticker in enumerate(tickers, 1):
        if ticker in fresh_cache:
            rows.append(fresh_cache[ticker])
            reused += 1
            continue
        info = retry_yahoo(lambda: yf.Ticker(ticker).info, f"fundamentals {ticker}", validator=lambda v: isinstance(v, dict) and bool(v))
        row = {"ticker": ticker, "retrieved_at": datetime.now(timezone.utc).isoformat()}
        downloaded += 1
        if info:
            cp, tp = info.get("currentPrice"), info.get("targetMeanPrice")
            row.update(
                market_cap=info.get("marketCap"), avg_volume=info.get("averageVolume"),
                revenue_growth=info.get("revenueGrowth"), earnings_growth=info.get("earningsGrowth"),
                earnings_q_growth=info.get("earningsQuarterlyGrowth"), forward_pe=info.get("forwardPE"),
                target_upside=(tp / cp - 1) if tp and cp else np.nan,
                recommendation=info.get("recommendationMean"), sector=info.get("sector"), industry=info.get("industry"),
                total_cash=info.get("totalCash"), total_debt=info.get("totalDebt"),
                operating_cashflow=info.get("operatingCashflow"), free_cashflow=info.get("freeCashflow"),
                current_ratio=info.get("currentRatio"), debt_to_equity=info.get("debtToEquity"),
            )
        rows.append(row)
        if i % 25 == 0:
            pd.DataFrame(rows).reindex(columns=FUNDAMENTAL_COLUMNS).to_csv(checkpoint, index=False)
            print(f"Fundamentals progress: {i}/{len(tickers)}", flush=True)
    frame = pd.DataFrame(rows).reindex(columns=FUNDAMENTAL_COLUMNS)
    frame.to_csv(checkpoint, index=False)
    return frame, reused, downloaded


def _field(data, field, ticker, batch):
    obj = data[field]
    if isinstance(obj, pd.Series):
        if len(batch) != 1:
            raise ValueError("single-series response for multi-ticker batch")
        return obj
    if isinstance(obj.columns, pd.MultiIndex):
        return obj[ticker]
    if ticker in obj.columns:
        return obj[ticker]
    if len(batch) == 1:
        return obj.iloc[:, 0]
    raise KeyError(f"{field}/{ticker}")


def _rsi(close, period=14):
    delta = close.diff()
    gain = delta.clip(lower=0).tail(period).mean()
    loss = -delta.clip(upper=0).tail(period).mean()
    return 100.0 if loss == 0 else 100 - 100 / (1 + gain / loss)


def _nearest_resistance(close, high, price):
    older = high.iloc[:-5].tail(247)
    local = older[(older.shift(1) < older) & (older.shift(-1) < older)]
    overhead = local[local >= price * 1.02]
    resistance = overhead.min() if len(overhead) else high.tail(252).max()
    return float(resistance), float(resistance / price - 1)


def technical_snapshot(frame):
    """Calculate one session's non-compensable setup gates."""
    frame = frame.dropna(subset=["Close", "High", "Low", "Volume"])
    if len(frame) < 253:
        return None
    c, h, low, v = frame.Close, frame.High, frame.Low, frame.Volume
    price = float(c.iloc[-1])
    returns = c.pct_change()
    tr = pd.concat([(h-low), (h-c.shift()).abs(), (low-c.shift()).abs()], axis=1).max(axis=1)
    atr_pct = float(tr.tail(14).mean() / price)
    resistance, headroom = _nearest_resistance(c, h, price)
    structural_support = float(low.tail(10).min())
    support_distance = price / structural_support - 1
    recent_60_low = float(low.tail(60).min())
    days_since_60_low = int(len(low.tail(60)) - 1 - np.argmin(low.tail(60).to_numpy()))
    prior5_low = float(low.iloc[-10:-5].min())
    current5_low = float(low.tail(5).min())
    higher_low = current5_low > prior5_low * 1.002
    prior_high_reclaim = price > float(h.iloc[-2])
    ma10_reclaim = price > float(c.tail(10).mean())
    down_volume = v.where(returns < 0)
    selling_volume_fades = bool(float(down_volume.tail(3).mean()) <= float(down_volume.tail(20).mean()) * 0.80) if down_volume.tail(20).notna().sum() >= 4 else False
    close_location = float((price - low.iloc[-1]) / max(h.iloc[-1] - low.iloc[-1], 1e-9))
    rejection_candle = close_location >= 0.65
    no_fresh_low = days_since_60_low >= 2
    confirmation_count = sum([higher_low, prior_high_reclaim or ma10_reclaim, selling_volume_fades, rejection_candle, no_fresh_low])
    bottom_confirmed = bool(no_fresh_low and higher_low and (prior_high_reclaim or ma10_reclaim) and confirmation_count >= 4)
    drawdown_52 = price / c.tail(252).max() - 1
    recent_shock = bool(returns.tail(20).min() <= -0.06 or (c / c.shift(5) - 1).tail(30).min() <= -0.12)
    loser_event = bool(recent_shock and drawdown_52 <= -0.15)
    near_bottom = bool(price / recent_60_low - 1 <= MAX_DISTANCE_FROM_60D_LOW)
    stop_price = price * 0.90
    stop_below_support = stop_price < structural_support
    stop_outside_noise = 0.10 >= 2.25 * atr_pct
    support_close_enough = support_distance <= MAX_SUPPORT_DISTANCE
    stop_geometry_pass = bool(stop_below_support and stop_outside_noise and support_close_enough)
    headroom_pass = bool(headroom >= MIN_HEADROOM)
    setup_pass = bool(loser_event and near_bottom and bottom_confirmed and headroom_pass and stop_geometry_pass)
    return {
        "price": price, "ret_1": price / c.iloc[-2] - 1, "ret_3": price / c.iloc[-4] - 1,
        "ret_5": price / c.iloc[-6] - 1, "ret_20": price / c.iloc[-21] - 1,
        "ret_60": price / c.iloc[-61] - 1, "ret_120": price / c.iloc[-121] - 1,
        "drawdown_52": drawdown_52, "off_low_52": price / c.tail(252).min() - 1,
        "worst_day_20": returns.tail(20).min(), "worst_5day_30": (c / c.shift(5) - 1).tail(30).min(),
        "ma10_pct": price / c.tail(10).mean() - 1, "ma20_pct": price / c.tail(20).mean() - 1,
        "ma50_pct": price / c.tail(50).mean() - 1, "ma200_pct": price / c.tail(200).mean() - 1,
        "rsi14": _rsi(c), "atr14_pct": atr_pct, "vol_ratio_5_60": v.tail(5).mean() / (v.tail(60).mean() + 1e-9),
        "dollar_volume": (c.tail(20) * v.tail(20)).mean(), "volatility": returns.tail(60).std() * math.sqrt(252),
        "recent_60_low": recent_60_low, "days_since_60_low": days_since_60_low,
        "structural_support": structural_support, "support_distance": support_distance,
        "nearest_resistance": resistance, "headroom": headroom, "close_location": close_location,
        "higher_low": higher_low, "reclaim": prior_high_reclaim or ma10_reclaim,
        "selling_volume_fades": selling_volume_fades, "rejection_candle": rejection_candle,
        "no_fresh_low": no_fresh_low, "bottom_confirmation_count": confirmation_count,
        "recent_shock": recent_shock, "loser_event": loser_event, "near_bottom": near_bottom, "bottom_confirmed": bottom_confirmed,
        "headroom_pass": headroom_pass, "stop_price_10pct": stop_price,
        "stop_below_support": stop_below_support, "stop_outside_noise": stop_outside_noise,
        "support_close_enough": support_close_enough, "stop_geometry_pass": stop_geometry_pass,
        "technical_setup_pass": setup_pass,
    }


def price_rows_from_download(data, batch):
    rows = []
    for ticker in batch:
        try:
            frame = pd.DataFrame({field: _field(data, field, ticker, batch) for field in ["Close", "High", "Low", "Volume"]}).dropna()
            current = technical_snapshot(frame)
            if current is None:
                continue
            historical_passes = []
            for offset in (0, 1, 2):
                snap = technical_snapshot(frame.iloc[:len(frame)-offset] if offset else frame)
                historical_passes.append(bool(snap and snap["technical_setup_pass"]))
            current["ticker"] = ticker
            current["setup_pass_sessions_3"] = sum(historical_passes)
            current["stability_pass"] = sum(historical_passes) >= MIN_STABILITY_SESSIONS
            rows.append(current)
        except Exception as exc:
            print(f"Price metric skip {ticker}: {exc}", flush=True)
    return rows


def download_prices(batch, label):
    return retry_yahoo(
        lambda: yf.download(batch, period="2y", interval="1d", group_by="column", auto_adjust=True, threads=False, progress=False, timeout=30),
        label, request_units=len(batch), validator=valid_price_download,
    )


def prices(tickers):
    rows, failures = [], []
    for start in range(0, len(tickers), YAHOO_PRICE_BATCH_SIZE):
        batch = tickers[start:start + YAHOO_PRICE_BATCH_SIZE]
        data = download_prices(batch, f"prices batch {start // YAHOO_PRICE_BATCH_SIZE + 1}")
        if data is not None:
            rows.extend(price_rows_from_download(data, batch))
        else:
            for ticker in batch:
                single = download_prices([ticker], f"price fallback {ticker}")
                if single is None:
                    failures.append(ticker)
                else:
                    rows.extend(price_rows_from_download(single, [ticker]))
        if (start // YAHOO_PRICE_BATCH_SIZE + 1) % 10 == 0:
            print(f"Price progress: {min(start + YAHOO_PRICE_BATCH_SIZE, len(tickers))}/{len(tickers)}", flush=True)
    return pd.DataFrame(rows), failures


def automated_quality(frame):
    """Automated triage only; an intact business still requires fresh review."""
    revenue = pd.to_numeric(frame.revenue_growth, errors="coerce")
    cash = pd.to_numeric(frame.total_cash, errors="coerce")
    debt = pd.to_numeric(frame.total_debt, errors="coerce")
    ocf = pd.to_numeric(frame.operating_cashflow, errors="coerce")
    current = pd.to_numeric(frame.current_ratio, errors="coerce")
    frame["revenue_not_collapsing"] = revenue.isna() | (revenue >= -0.15)
    frame["liquidity_evidence_pass"] = current.isna() | (current >= 0.75)
    frame["cash_debt_evidence_pass"] = cash.isna() | debt.isna() | (cash >= debt * 0.20) | (ocf > 0)
    frame["fundamental_coverage"] = frame[["revenue_growth", "total_cash", "total_debt", "operating_cashflow", "current_ratio"]].notna().mean(axis=1)
    frame["automated_quality_pass"] = (
        frame[["revenue_not_collapsing", "liquidity_evidence_pass", "cash_debt_evidence_pass"]].all(axis=1)
        & (frame.fundamental_coverage >= MIN_FUNDAMENTAL_COVERAGE)
    )
    return frame


def rank_candidates(frame):
    frame = frame.copy()
    frame["loss_severity_score"] = pct_rank(-frame.worst_day_20) * .35 + pct_rank(-frame.worst_5day_30) * .35 + pct_rank(-frame.drawdown_52) * .30
    frame["bottom_quality_score"] = (
        frame.bottom_confirmation_count / 5 * 35 + pct_rank(frame.close_location) * .15
        + pct_rank(-frame.support_distance) * .20 + pct_rank(frame.headroom.clip(upper=.50)) * .20
        + pct_rank(-frame.atr14_pct) * .10
    )
    frame["business_quality_score"], frame["business_score_coverage"] = weighted_available_score(
        [(pct_rank(frame.revenue_growth), .35), (pct_rank(frame.operating_cashflow), .20),
         (pct_rank(frame.current_ratio), .15), (pct_rank(frame.dollar_volume), .20),
         (frame.fundamental_coverage * 100, .10)]
    )
    frame["quality_loser_score"] = (frame.loss_severity_score * .20 + frame.bottom_quality_score * .50 + frame.business_quality_score * .30).clip(0, 100)
    return frame.sort_values("quality_loser_score", ascending=False)


VERIFICATION_FIELDS = [
    "ticker", "verified_at", "reviewer", "selloff_reason", "selloff_not_thesis_break",
    "business_intact", "balance_sheet_pass", "no_material_dilution", "future_catalyst_pass",
    "catalyst_date", "catalyst_description", "nonbinary_risk_pass", "multitimeframe_chart_pass",
    "market_regime_pass", "source_urls", "final_status",
]


def verification_template(tickers):
    return pd.DataFrame([{"ticker": t, **{c: "NOT_RESEARCHED" for c in VERIFICATION_FIELDS[1:]}} for t in tickers], columns=VERIFICATION_FIELDS)


def load_current_verification(tickers):
    path = Path("current_verification.csv")
    if not path.exists():
        return verification_template(tickers), set()
    try:
        verified = pd.read_csv(path).reindex(columns=VERIFICATION_FIELDS)
    except Exception:
        return verification_template(tickers), set()
    valid = set()
    required_pass = ["selloff_not_thesis_break", "business_intact", "balance_sheet_pass", "no_material_dilution", "future_catalyst_pass", "nonbinary_risk_pass", "multitimeframe_chart_pass", "market_regime_pass"]
    now = datetime.now(timezone.utc)
    for _, row in verified.iterrows():
        try:
            stamp = datetime.fromisoformat(str(row.verified_at).replace("Z", "+00:00"))
            if stamp.tzinfo is None:
                stamp = stamp.replace(tzinfo=timezone.utc)
            fresh = 0 <= (now - stamp.astimezone(timezone.utc)).total_seconds() / 3600 <= VERIFICATION_MAX_AGE_HOURS
        except Exception:
            fresh = False
        if fresh and all(str(row.get(c, "")).upper() == "PASS" for c in required_pass) and str(row.final_status).upper() == "APPROVED":
            valid.add(row.ticker)
    merged = verification_template(tickers).set_index("ticker")
    supplied = verified[verified.ticker.isin(tickers)].drop_duplicates("ticker", keep="last").set_index("ticker")
    merged.update(supplied)
    return merged.reset_index(), valid


def active_positions_audit(scored):
    path = Path(os.environ.get("ROCKET_ACTIVE_POSITIONS_FILE", "private/active_positions.csv"))
    template = Path("active_positions.template.csv")
    positions = pd.read_csv(path) if path.exists() else pd.read_csv(template)
    audit = positions.merge(scored, on="ticker", how="left", suffixes=("_position", ""))
    audit["present_in_full_scored_universe"] = audit.price.notna() if "price" in audit else False
    audit["position_action"] = "MANAGE_BY_POSITION_SSOT; NOT AN AUTOMATIC SELL/BUY SIGNAL"
    return audit


def main():
    run_at = datetime.now(timezone.utc).isoformat()
    u = universe()
    u.to_csv(OUT / "01_starting_universe.csv", index=False)
    print(f"Starting universe: {len(u)}", flush=True)
    p, failures = prices(u.ticker.tolist())
    p.to_csv(OUT / "02_price_and_pattern_metrics.csv", index=False)
    pd.DataFrame({"ticker": failures}).to_csv(OUT / "02_price_request_failures.csv", index=False)
    failure_rate = len(failures) / max(len(u), 1)
    if failure_rate > MAX_PRICE_REQUEST_FAILURE_RATE:
        raise RuntimeError(f"Price request failure rate {failure_rate:.2%} exceeds {MAX_PRICE_REQUEST_FAILURE_RATE:.2%}")
    if p.empty:
        raise RuntimeError("Price stage empty; refusing incomplete screen")
    investable = u.merge(p, on="ticker", how="inner")
    investable = investable[(investable.price >= MIN_PRICE) & (investable.dollar_volume >= MIN_DOLLAR_VOLUME)]
    investable.to_csv(OUT / "03_investable.csv", index=False)
    f, reused, downloaded = fundamentals(investable.ticker.tolist())
    all_data = investable.merge(f, on="ticker", how="left")
    missing_mc = int(all_data.market_cap.isna().sum())
    all_data = all_data[all_data.market_cap.fillna(0) >= MIN_MARKET_CAP]
    all_data = automated_quality(all_data)
    scored = rank_candidates(all_data)
    scored.to_csv(OUT / "04_all_quality_loser_scored.csv", index=False)

    loser_pool = scored[scored.loser_event & scored.near_bottom & scored.automated_quality_pass].copy()
    loser_pool.to_csv(OUT / "05_quality_loser_pool.csv", index=False)
    bottom_confirmed = loser_pool[loser_pool.bottom_confirmed].copy()
    bottom_confirmed.to_csv(OUT / "06_bottom_confirmed.csv", index=False)
    entry_geometry = bottom_confirmed[bottom_confirmed.headroom_pass & bottom_confirmed.stop_geometry_pass & bottom_confirmed.stability_pass].copy()
    entry_geometry.to_csv(OUT / "07_entry_geometry_pass.csv", index=False)

    research = entry_geometry.head(25).copy()
    verification, valid = load_current_verification(research.ticker.tolist())
    verification.to_csv(OUT / "08_CURRENT_VERIFICATION_REQUIRED.csv", index=False)
    research["current_verification_pass"] = research.ticker.isin(valid)
    research["engine_status"] = np.where(research.current_verification_pass, "ENTRY_READY", "REQUIRES_CURRENT_VERIFICATION")
    research.to_csv(OUT / "08_research_candidates.csv", index=False)
    entry_ready = research[research.current_verification_pass].copy()
    entry_ready.to_csv(OUT / "09_ENTRY_READY.csv", index=False)
    holdings = active_positions_audit(scored)
    holdings.to_csv(OUT / "10_active_positions_audit.csv", index=False)

    audit = {
        "engine": "Quality Loser Reversal V2", "run_at_utc": run_at, "ruleset": "QUALITY_LOSER_SSOT.md",
        "starting_universe": len(u), "price_eligible": len(p), "investable_before_marketcap": len(investable),
        "market_cap_eligible": len(scored), "quality_loser_pool": len(loser_pool), "bottom_confirmed": len(bottom_confirmed),
        "entry_geometry_and_stability_pass": len(entry_geometry), "research_candidates": len(research), "entry_ready": len(entry_ready),
        "price_request_failures": len(failures), "price_request_failure_rate": failure_rate,
        "fundamentals_cache_reused_fresh": reused, "fundamentals_fresh_downloaded": downloaded, "market_cap_missing": missing_mc,
        "thresholds": {"min_price": MIN_PRICE, "min_dollar_volume": MIN_DOLLAR_VOLUME, "min_market_cap": MIN_MARKET_CAP,
            "min_headroom": MIN_HEADROOM, "max_support_distance": MAX_SUPPORT_DISTANCE,
            "max_distance_from_60d_low": MAX_DISTANCE_FROM_60D_LOW,
            "min_fundamental_coverage": MIN_FUNDAMENTAL_COVERAGE,
            "min_setup_pass_sessions_of_last_3": MIN_STABILITY_SESSIONS, "verification_max_age_hours": VERIFICATION_MAX_AGE_HOURS},
        "hard_gates": ["loser_event", "near_bottom", "automated_quality", "bottom_confirmed", "headroom", "stop_geometry", "stability", "current_manual_verification"],
        "current_catalyst_claimed_market_wide": False, "chart_claimed_from_single_timeframe": False,
        "FINAL_LABEL_ALLOWED": bool(len(entry_ready)),
        "note": "ENTRY_READY requires a <=24-hour verification row with every manual gate PASS. Empty ENTRY_READY means cash/no new purchase, not permission to relax a gate.",
    }
    (OUT / "audit_quality_loser.json").write_text(json.dumps(audit, indent=2))
    print(json.dumps(audit, indent=2), flush=True)
    columns = ["ticker", "quality_loser_score", "price", "worst_day_20", "drawdown_52", "headroom", "setup_pass_sessions_3", "engine_status"]
    print(research[columns].to_string(index=False) if len(research) else "No research candidates passed all quantitative gates.", flush=True)


if __name__ == "__main__":
    main()
