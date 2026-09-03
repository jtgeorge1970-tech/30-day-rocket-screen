"""Engine #3: strict full-universe extreme-winner continuation screen.

The module deliberately separates scalable quantitative detection from fresh
company and intraday verification. Quantitative Top 3 rows are research inputs,
not recommendations. See EXTREME_WINNER_SSOT.md.
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


OUT = Path(os.environ.get("EXTREME_WINNER_OUTPUT", "output"))
MIN_PRICE = 3.0
MIN_DOLLAR_VOLUME = 2_000_000.0
MIN_MARKET_CAP = 200_000_000.0
ONE_DAY_EVENT = 0.20
FIVE_DAY_EVENT = 0.30
LOOKBACK_EVENT_SESSIONS = 30
MIN_CLOSE_LOCATION = 0.70
MIN_VOLUME_RATIO = 3.0
MAX_EXTENSION_MA20 = 0.35
MAX_ATR14_PCT = 0.05
MAX_PRICE_REQUEST_FAILURE_RATE = 0.02
PRICE_BATCH_SIZE = 20
YAHOO_RATE_CAP_PER_MINUTE = 100
YAHOO_MIN_INTERVAL = 60.0 / YAHOO_RATE_CAP_PER_MINUTE
FUNDAMENTALS_CACHE_TTL_HOURS = 18
VERIFICATION_MAX_AGE_HOURS = 24

VERIFICATION_GATES = [
    "catalyst_quality",
    "news_freshness",
    "business_quality",
    "dilution_supply_risk",
    "float_manipulation_risk",
    "intraday_structure",
    "liquidity_spread",
    "sector_market_regime",
    "stop_geometry",
    "headroom_10pct",
]

UA = {"User-Agent": "Mozilla/5.0 extreme-winner-research"}
_last_yahoo_call = 0.0


def yahoo_pace():
    global _last_yahoo_call
    wait = YAHOO_MIN_INTERVAL - (time.monotonic() - _last_yahoo_call)
    if wait > 0:
        time.sleep(wait)
    _last_yahoo_call = time.monotonic()


def retry_yahoo(fn, label, attempts=6, validator=None):
    last = None
    for attempt in range(attempts):
        yahoo_pace()
        try:
            value = fn()
            if validator is not None and not validator(value):
                raise ValueError(f"invalid or incomplete response for {label}")
            return value
        except Exception as exc:
            last = exc
            if attempt == attempts - 1:
                break
            delay = min(60, 3 * (2**attempt)) + random.uniform(0, 2)
            print(
                f"Yahoo retry {attempt + 1}/{attempts - 1} for {label}: "
                f"{exc}; sleeping {delay:.1f}s",
                flush=True,
            )
            time.sleep(delay)
    print(f"Yahoo failed after retries for {label}: {last}", flush=True)
    return None


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
    nasdaq, other = frames
    nasdaq = nasdaq.rename(
        columns={"Symbol": "ticker", "Security Name": "name", "ETF": "etf", "Test Issue": "test"}
    )
    other = other.rename(
        columns={"ACT Symbol": "ticker", "Security Name": "name", "ETF": "etf", "Test Issue": "test"}
    )
    listed = pd.concat(
        [nasdaq[["ticker", "name", "etf", "test"]], other[["ticker", "name", "etf", "test"]]],
        ignore_index=True,
    )
    listed = listed[(listed.etf == "N") & (listed.test == "N")].dropna(subset=["ticker", "name"])
    listed = listed[~listed.ticker.astype(str).str.contains(r"[.$]", regex=True)]
    excluded = r"Warrant|Right| Unit|Units|Preferred|Depositary Shares|Acquisition Corp|SPAC"
    listed = listed[~listed.name.str.contains(excluded, case=False, na=False, regex=True)]
    return listed.drop_duplicates("ticker").reset_index(drop=True)


def _valid_download(data):
    return data is not None and isinstance(data, pd.DataFrame) and not data.empty and "Close" in data.columns


def _field(data, field, ticker, batch):
    values = data[field]
    if isinstance(values, pd.Series):
        return values
    if ticker in values.columns:
        return values[ticker]
    if len(batch) == 1 and len(values.columns) == 1:
        return values.iloc[:, 0]
    return pd.Series(dtype=float)


def ohlcv(data, ticker, batch):
    frame = pd.DataFrame(
        {field: _field(data, field, ticker, batch) for field in ["Open", "High", "Low", "Close", "Volume"]}
    )
    return frame.apply(pd.to_numeric, errors="coerce").dropna()


def _atr(frame, shift_for_event=False):
    close, high, low = frame.Close, frame.High, frame.Low
    true_range = pd.concat(
        [(high - low), (high - close.shift()).abs(), (low - close.shift()).abs()], axis=1
    ).max(axis=1)
    if shift_for_event:
        true_range = true_range.shift(1)
    return true_range.rolling(14, min_periods=14).mean()


def analyze_history(frame, ticker):
    """Return latest 30-session event/current structure metrics for one ticker."""
    frame = frame.dropna(subset=["Open", "High", "Low", "Close", "Volume"]).copy()
    if len(frame) < 22:
        return {
            "ticker": ticker,
            "as_of": frame.index[-1].date().isoformat() if len(frame) else "",
            "price": float(frame.Close.iloc[-1]) if len(frame) else np.nan,
            "current_dollar_volume_20": np.nan,
            "current_return_20": np.nan,
            "sufficient_history": False,
            "event_detected": False,
        }
    close, high, low, open_, volume = (
        frame.Close,
        frame.High,
        frame.Low,
        frame.Open,
        frame.Volume,
    )
    day_return = close.pct_change()
    five_day_return = close / close.shift(5) - 1
    current_price = float(close.iloc[-1])
    current_dollar_volume = float((close * volume).tail(20).mean())
    result = {
        "ticker": ticker,
        "as_of": frame.index[-1].date().isoformat(),
        "price": current_price,
        "current_dollar_volume_20": current_dollar_volume,
        "current_return_20": float(close.iloc[-1] / close.iloc[-21] - 1),
        "sufficient_history": True,
        "event_detected": False,
    }
    start = max(21, len(frame) - LOOKBACK_EVENT_SESSIONS)
    event_positions = [
        idx
        for idx in range(start, len(frame))
        if day_return.iloc[idx] >= ONE_DAY_EVENT or five_day_return.iloc[idx] >= FIVE_DAY_EVENT
    ]
    if not event_positions:
        return result
    idx = event_positions[-1]
    prior_close = float(close.iloc[idx - 1])
    event_range = max(float(high.iloc[idx] - low.iloc[idx]), 1e-9)
    prior_volume = float(volume.iloc[idx - 20:idx].mean())
    event_dollar_volume = float((close * volume).iloc[idx - 20:idx].mean())
    atr = _atr(frame, shift_for_event=True)
    ma10 = float(close.tail(10).mean())
    ma20 = float(close.tail(20).mean())
    midpoint = float(low.iloc[idx] + 0.5 * event_range)
    peak_denominator = max(float(high.iloc[idx]) - prior_close, 1e-9)
    event_type = (
        "BOTH"
        if day_return.iloc[idx] >= ONE_DAY_EVENT and five_day_return.iloc[idx] >= FIVE_DAY_EVENT
        else ("ONE_DAY" if day_return.iloc[idx] >= ONE_DAY_EVENT else "FIVE_DAY")
    )
    prior_52_high = float(high.iloc[max(0, idx - 252):idx].max())
    result.update(
        event_detected=True,
        event_date=frame.index[idx].date().isoformat(),
        event_age_sessions=int(len(frame) - 1 - idx),
        event_type=event_type,
        event_open=float(open_.iloc[idx]),
        event_high=float(high.iloc[idx]),
        event_low=float(low.iloc[idx]),
        event_close=float(close.iloc[idx]),
        event_day_return=float(day_return.iloc[idx]),
        event_five_day_return=float(five_day_return.iloc[idx]),
        event_gap=float(open_.iloc[idx] / prior_close - 1),
        event_intraday_return=float(close.iloc[idx] / open_.iloc[idx] - 1),
        event_close_location=float((close.iloc[idx] - low.iloc[idx]) / event_range),
        event_peak_retention=float(np.clip((close.iloc[idx] - prior_close) / peak_denominator, 0, 1)),
        event_volume_ratio_20=float(volume.iloc[idx] / max(prior_volume, 1e-9)),
        event_dollar_volume_20=event_dollar_volume,
        event_atr14_pct=float(atr.iloc[idx] / close.iloc[idx]),
        event_pre_return_20=float(close.iloc[idx - 1] / close.iloc[idx - 21] - 1),
        event_new_52w_high=bool(high.iloc[idx] >= prior_52_high),
        event_midpoint=midpoint,
        current_above_event_midpoint=bool(current_price >= midpoint),
        current_above_ma10=bool(current_price >= ma10),
        current_extension_ma20=float(current_price / ma20 - 1),
        post_event_return=float(current_price / close.iloc[idx] - 1),
        post_event_low=float(low.iloc[idx:].min()),
        current_atr14_pct=float(_atr(frame).iloc[-1] / current_price),
    )
    return result


def download_price_metrics(tickers, period="2y"):
    rows, failures = [], []
    for start in range(0, len(tickers), PRICE_BATCH_SIZE):
        batch = tickers[start:start + PRICE_BATCH_SIZE]
        data = retry_yahoo(
            lambda b=batch: yf.download(
                b,
                period=period,
                interval="1d",
                group_by="column",
                auto_adjust=True,
                threads=False,
                progress=False,
                timeout=30,
            ),
            f"winner prices batch {start // PRICE_BATCH_SIZE + 1}",
            validator=_valid_download,
        )
        if data is None:
            failures.extend(batch)
            continue
        for ticker in batch:
            try:
                row = analyze_history(ohlcv(data, ticker, batch), ticker)
                rows.append(row)
            except Exception as exc:
                print(f"Price metric skip {ticker}: {exc}", flush=True)
                failures.append(ticker)
        if (start // PRICE_BATCH_SIZE + 1) % 10 == 0:
            print(f"Price progress: {min(start + PRICE_BATCH_SIZE, len(tickers))}/{len(tickers)}", flush=True)
    return pd.DataFrame(rows), sorted(set(failures))


def benchmark_return_20():
    data = retry_yahoo(
        lambda: yf.download(
            "SPY", period="3mo", interval="1d", auto_adjust=True, threads=False, progress=False, timeout=30
        ),
        "SPY benchmark",
        validator=_valid_download,
    )
    if data is None:
        raise RuntimeError("SPY unavailable; refusing incomplete relative-strength screen")
    close = data["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]
    close = close.dropna()
    if len(close) < 21:
        raise RuntimeError("SPY history insufficient")
    return float(close.iloc[-1] / close.iloc[-21] - 1)


def _fresh_cache(path):
    if not path.exists():
        return {}
    try:
        frame = pd.read_csv(path)
    except Exception:
        return {}
    if not {"ticker", "retrieved_at"}.issubset(frame.columns):
        return {}
    now = datetime.now(timezone.utc)
    result = {}
    for row in frame.to_dict("records"):
        try:
            stamp = datetime.fromisoformat(str(row["retrieved_at"]).replace("Z", "+00:00"))
            if stamp.tzinfo is None:
                stamp = stamp.replace(tzinfo=timezone.utc)
            age = (now - stamp.astimezone(timezone.utc)).total_seconds() / 3600
        except Exception:
            continue
        if 0 <= age <= FUNDAMENTALS_CACHE_TTL_HOURS:
            result[str(row["ticker"])] = row
    return result


def fundamentals(tickers):
    columns = [
        "ticker", "retrieved_at", "market_cap", "float_shares", "shares_outstanding",
        "revenue_growth", "earnings_growth", "debt_to_equity", "current_ratio",
        "target_upside", "recommendation", "sector", "industry",
    ]
    checkpoint = OUT / "fundamentals_checkpoint.csv"
    cache = _fresh_cache(checkpoint)
    rows = []
    for index, ticker in enumerate(tickers, 1):
        if ticker in cache:
            rows.append(cache[ticker])
            continue
        info = retry_yahoo(lambda t=ticker: yf.Ticker(t).info, f"winner fundamentals {ticker}")
        row = {"ticker": ticker, "retrieved_at": datetime.now(timezone.utc).isoformat()}
        if info:
            current = info.get("currentPrice") or info.get("regularMarketPrice")
            target = info.get("targetMeanPrice")
            row.update(
                market_cap=info.get("marketCap"),
                float_shares=info.get("floatShares"),
                shares_outstanding=info.get("sharesOutstanding"),
                revenue_growth=info.get("revenueGrowth"),
                earnings_growth=info.get("earningsGrowth"),
                debt_to_equity=info.get("debtToEquity"),
                current_ratio=info.get("currentRatio"),
                target_upside=(target / current - 1) if target and current else np.nan,
                recommendation=info.get("recommendationMean"),
                sector=info.get("sector"),
                industry=info.get("industry"),
            )
        rows.append(row)
        if index % 25 == 0:
            pd.DataFrame(rows).reindex(columns=columns).to_csv(checkpoint, index=False)
            print(f"Winner fundamentals progress: {index}/{len(tickers)}", flush=True)
    result = pd.DataFrame(rows).reindex(columns=columns)
    result.to_csv(checkpoint, index=False)
    return result


def pct_rank(series):
    return pd.to_numeric(series, errors="coerce").rank(pct=True) * 100


def inverse_pct_rank(series):
    return 100 - pct_rank(series)


def score_events(events, spy_return_20):
    scored = events.copy()
    scored["spy_return_20"] = spy_return_20
    scored["spy_relative_20"] = scored.current_return_20 - spy_return_20
    scored["sector_relative_20"] = scored.current_return_20 - scored.groupby("sector")[
        "current_return_20"
    ].transform("median")
    scored["automated_gate_pass"] = (
        (scored.price >= MIN_PRICE)
        & (scored.event_dollar_volume_20 >= MIN_DOLLAR_VOLUME)
        & (scored.market_cap >= MIN_MARKET_CAP)
        & (scored.event_close_location >= MIN_CLOSE_LOCATION)
        & (scored.event_volume_ratio_20 >= MIN_VOLUME_RATIO)
        & scored.current_above_event_midpoint.fillna(False)
        & scored.current_above_ma10.fillna(False)
        & (scored.current_extension_ma20 <= MAX_EXTENSION_MA20)
        & (scored.event_atr14_pct <= MAX_ATR14_PCT)
        & (scored.event_age_sessions < LOOKBACK_EVENT_SESSIONS)
    )
    event_strength = pct_rank(
        np.maximum(scored.event_day_return / ONE_DAY_EVENT, scored.event_five_day_return / FIVE_DAY_EVENT)
    )
    business = pd.concat(
        [
            pct_rank(scored.revenue_growth),
            pct_rank(scored.earnings_growth),
            inverse_pct_rank(scored.debt_to_equity),
            pct_rank(scored.current_ratio),
        ],
        axis=1,
    )
    scored["business_evidence_coverage"] = business.notna().mean(axis=1)
    scored["business_quality_available"] = business.mean(axis=1, skipna=True)
    factors = pd.DataFrame(
        {
            "event_strength": event_strength,
            "volume": pct_rank(scored.event_volume_ratio_20),
            "close": pct_rank(scored.event_close_location),
            "retention": pct_rank(scored.event_peak_retention),
            "relative_strength": pct_rank(scored.spy_relative_20),
            "sector_strength": pct_rank(scored.sector_relative_20),
            "post_event_hold": pct_rank(scored.post_event_return),
            "liquidity": pct_rank(scored.event_dollar_volume_20),
            "low_volatility": inverse_pct_rank(scored.event_atr14_pct),
            "low_extension": inverse_pct_rank(scored.current_extension_ma20.clip(lower=0)),
            "business": scored.business_quality_available,
        }
    )
    weights = pd.Series(
        {
            "event_strength": 0.13,
            "volume": 0.15,
            "close": 0.12,
            "retention": 0.10,
            "relative_strength": 0.11,
            "sector_strength": 0.06,
            "post_event_hold": 0.10,
            "liquidity": 0.08,
            "low_volatility": 0.08,
            "low_extension": 0.06,
            "business": 0.06,
        }
    )
    available = factors.notna().astype(float)
    scored["data_confidence"] = (available * weights).sum(axis=1) / weights.sum()
    scored["continuation_score"] = (factors.fillna(0) * weights).sum(axis=1) / (
        available * weights
    ).sum(axis=1).replace(0, np.nan)
    return scored.sort_values("continuation_score", ascending=False, na_position="last")


def _empty_like(frame):
    return frame.iloc[0:0].copy()


def approved_entries(top3, path=Path("current_verification.csv")):
    if top3.empty or not path.exists():
        return _empty_like(top3)
    review = pd.read_csv(path)
    required = {"ticker", "retrieved_at", "final_status", *VERIFICATION_GATES}
    if not required.issubset(review.columns):
        return _empty_like(top3)
    now = datetime.now(timezone.utc)
    accepted = []
    for row in review.to_dict("records"):
        try:
            stamp = datetime.fromisoformat(str(row["retrieved_at"]).replace("Z", "+00:00"))
            if stamp.tzinfo is None:
                stamp = stamp.replace(tzinfo=timezone.utc)
            age = (now - stamp.astimezone(timezone.utc)).total_seconds() / 3600
        except Exception:
            continue
        gates_pass = all(str(row.get(gate, "")).upper() == "PASS" for gate in VERIFICATION_GATES)
        if 0 <= age <= VERIFICATION_MAX_AGE_HOURS and gates_pass and str(row["final_status"]).upper() == "APPROVED":
            accepted.append(str(row["ticker"]))
    entries = top3[top3.ticker.astype(str).isin(accepted)].copy()
    if len(entries):
        entries = entries.merge(review, on="ticker", how="left", suffixes=("", "_verification"))
    return entries


def main():
    OUT.mkdir(exist_ok=True)
    run_at = datetime.now(timezone.utc).isoformat()
    listed = universe()
    listed.to_csv(OUT / "01_starting_universe.csv", index=False)
    print(f"Starting universe: {len(listed)}", flush=True)

    metrics, failures = download_price_metrics(listed.ticker.tolist())
    metrics.to_csv(OUT / "02_price_metrics.csv", index=False)
    pd.DataFrame({"ticker": failures}).to_csv(OUT / "02_price_failures.csv", index=False)
    failure_rate = len(failures) / max(len(listed), 1)
    if failure_rate > MAX_PRICE_REQUEST_FAILURE_RATE:
        raise RuntimeError("Price failure rate exceeded locked cap")

    event_metrics = metrics[metrics.event_detected.fillna(False)].copy()
    names = listed[["ticker", "name"]]
    event_metrics = names.merge(event_metrics, on="ticker", how="inner")
    event_metrics.to_csv(OUT / "03_extreme_winner_events.csv", index=False)

    fundamental = fundamentals(event_metrics.ticker.tolist()) if len(event_metrics) else pd.DataFrame(columns=["ticker", "market_cap"])
    investable = event_metrics.merge(fundamental, on="ticker", how="left")
    investable = investable[
        (investable.price >= MIN_PRICE)
        & (investable.event_dollar_volume_20 >= MIN_DOLLAR_VOLUME)
        & (pd.to_numeric(investable.market_cap, errors="coerce") >= MIN_MARKET_CAP)
    ].copy()
    investable.to_csv(OUT / "04_investable_events.csv", index=False)

    spy_return = benchmark_return_20()
    scored = score_events(investable, spy_return) if len(investable) else investable.assign(
        automated_gate_pass=pd.Series(dtype=bool), continuation_score=pd.Series(dtype=float)
    )
    scored.to_csv(OUT / "05_all_scored_events.csv", index=False)
    eligible = scored[scored.automated_gate_pass.fillna(False)].copy()
    top50 = eligible.head(50)
    top25 = top50.head(25)
    top10 = top25.head(10)
    top5 = top10.head(5)
    top3 = top5.head(3).copy()
    top3["current_verification_required"] = True
    top3["status"] = "RESEARCH_ONLY_NOT_BUY"
    stages = [
        ("06_top50.csv", top50),
        ("07_top25.csv", top25),
        ("08_top10.csv", top10),
        ("08_top5.csv", top5),
        ("09_top3_REQUIRES_CURRENT_VERIFICATION.csv", top3),
    ]
    for filename, frame in stages:
        frame.to_csv(OUT / filename, index=False)
    entries = approved_entries(top3)
    entries.to_csv(OUT / "11_ENTRY_READY.csv", index=False)

    audit = {
        "engine": "Engine #3 Extreme-Winner Continuation",
        "run_at_utc": run_at,
        "ruleset": "EXTREME_WINNER_SSOT.md",
        "starting_universe": len(listed),
        "price_metrics": len(metrics),
        "price_failures": len(failures),
        "price_failure_rate": failure_rate,
        "lookback_event_sessions": LOOKBACK_EVENT_SESSIONS,
        "one_day_event_threshold": ONE_DAY_EVENT,
        "five_day_event_threshold": FIVE_DAY_EVENT,
        "events_detected": len(event_metrics),
        "investable_events": len(investable),
        "automated_gate_pass": len(eligible),
        "top50": len(top50),
        "top25": len(top25),
        "top10": len(top10),
        "top5": len(top5),
        "top3": len(top3),
        "entry_ready": len(entries),
        "FINAL_LABEL_ALLOWED": bool(len(entries)),
        "scarcity_rule": "Zero candidates is valid; never loosen thresholds to create a trade.",
        "orders_placed_automatically": False,
        "known_limitations": [
            "intraday VWAP/opening range requires current manual verification",
            "current market cap is not historical point-in-time market cap",
        ],
    }
    (OUT / "audit_extreme_winner.json").write_text(json.dumps(audit, indent=2))
    print(json.dumps(audit, indent=2), flush=True)


if __name__ == "__main__":
    main()
