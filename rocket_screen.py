"""30-Day Rocket Screen — auditable market-wide quantitative funnel.

This engine deliberately separates scalable quantitative screening from current
company-specific verification. A stock cannot be labeled FINAL solely from this
output. See SSOT.md.
"""
from __future__ import annotations

import io
import json
import math
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
UA = {"User-Agent": "Mozilla/5.0 rocket-screen research"}

LENSES = (
    "leadership_momentum",
    "beaten_down_reversal",
    "acceleration_emerging_momentum",
)

YAHOO_RATE_CAP_PER_MINUTE = 100
YAHOO_MIN_INTERVAL = 60.0 / YAHOO_RATE_CAP_PER_MINUTE
YAHOO_PRICE_BATCH_SIZE = 10
MAX_PRICE_REQUEST_FAILURE_RATE = 0.01
FUNDAMENTALS_CACHE_TTL_HOURS = 18
MIN_DATA_CONFIDENCE = 0.55
SEMIFINALISTS_PER_LENS = 40
QUANT_CANDIDATES = 25
_next_yahoo_call = 0.0


def yahoo_pace(request_units=1):
    """Reserve Yahoo capacity for every ticker represented by a call.

    A multi-ticker ``yf.download`` call still causes Yahoo work for every
    ticker. Treating a 20-ticker batch as one request defeated the 100/minute
    cap and could produce silent rate-limit gaps.
    """
    global _next_yahoo_call
    wait = _next_yahoo_call - time.monotonic()
    if wait > 0:
        time.sleep(wait)
    _next_yahoo_call = time.monotonic() + (
        YAHOO_MIN_INTERVAL * max(1, int(request_units))
    )


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
            print(
                f"Yahoo retry {attempt + 1}/{attempts - 1} for {label}: "
                f"{exc}; sleeping {delay:.1f}s",
                flush=True,
            )
            time.sleep(delay)
    print(f"Yahoo failed after retries for {label}: {last}", flush=True)
    return None


def valid_price_download(data):
    if data is None or data.empty or "Close" not in data.columns:
        return False
    close = data["Close"]
    return bool(close.notna().to_numpy().any())


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
    a = a.rename(
        columns={
            "Symbol": "ticker",
            "Security Name": "name",
            "ETF": "etf",
            "Test Issue": "test",
        }
    )
    b = b.rename(
        columns={
            "ACT Symbol": "ticker",
            "Security Name": "name",
            "ETF": "etf",
            "Test Issue": "test",
        }
    )
    x = pd.concat(
        [a[["ticker", "name", "etf", "test"]], b[["ticker", "name", "etf", "test"]]],
        ignore_index=True,
    )
    x = x[(x.etf == "N") & (x.test == "N")].dropna(subset=["ticker"])
    x = x[~x.ticker.str.contains(r"[.$]", regex=True)]

    # Obvious non-common-stock / shell-like structures only. Final special-risk
    # review is intentionally deferred until the candidate set is small enough
    # to investigate correctly.
    bad = r"Warrant|Right| Unit|Preferred|Depositary Shares|Acquisition Corp|SPAC"
    x = x[~x.name.str.contains(bad, case=False, na=False, regex=True)]
    return x.drop_duplicates("ticker").reset_index(drop=True)


def pct_rank(series):
    return pd.to_numeric(series, errors="coerce").rank(pct=True) * 100


def inverse_pct_rank(series):
    numeric = pd.to_numeric(series, errors="coerce")
    positive = numeric.where(numeric > 0)
    ranked = pct_rank(positive)
    return 100 - ranked


def weighted_available_score(factors):
    """Weighted row score using only observed factors; never invent missing evidence.

    factors is an ordered iterable of (series, weight). Returns (score, coverage),
    where coverage is the fraction of intended weight backed by actual data.
    """
    numerator = None
    denominator = None
    total_weight = sum(weight for _, weight in factors)
    for series, weight in factors:
        numeric = pd.to_numeric(series, errors="coerce")
        available = numeric.notna().astype(float)
        contribution = numeric.fillna(0) * weight
        weight_available = available * weight
        numerator = contribution if numerator is None else numerator + contribution
        denominator = weight_available if denominator is None else denominator + weight_available
    score = numerator / denominator.replace(0, np.nan)
    coverage = denominator / total_weight
    return score, coverage


def load_fresh_checkpoint(checkpoint):
    if not checkpoint.exists():
        return {}
    try:
        frame = pd.read_csv(checkpoint)
    except Exception:
        return {}
    if "ticker" not in frame.columns or "retrieved_at" not in frame.columns:
        return {}

    now = datetime.now(timezone.utc)
    fresh = {}
    for row in frame.to_dict("records"):
        stamp = row.get("retrieved_at")
        try:
            dt = datetime.fromisoformat(str(stamp).replace("Z", "+00:00"))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            age_hours = (now - dt.astimezone(timezone.utc)).total_seconds() / 3600
        except Exception:
            continue
        if 0 <= age_hours <= FUNDAMENTALS_CACHE_TTL_HOURS:
            fresh[row["ticker"]] = row
    return fresh


def fundamentals(tickers):
    cols = [
        "ticker",
        "retrieved_at",
        "market_cap",
        "avg_volume",
        "revenue_growth",
        "earnings_growth",
        "earnings_q_growth",
        "forward_pe",
        "target_upside",
        "recommendation",
        "sector",
        "industry",
    ]
    rows = []
    checkpoint = OUT / "fundamentals_checkpoint.csv"
    fresh_cache = load_fresh_checkpoint(checkpoint)
    reused = 0
    downloaded = 0

    for i, ticker in enumerate(tickers, 1):
        if ticker in fresh_cache:
            rows.append(fresh_cache[ticker])
            reused += 1
            continue

        info = retry_yahoo(
            lambda: yf.Ticker(ticker).info,
            f"fundamentals {ticker}",
            validator=lambda value: isinstance(value, dict) and bool(value),
        )
        row = {
            "ticker": ticker,
            "retrieved_at": datetime.now(timezone.utc).isoformat(),
        }
        downloaded += 1
        if info:
            current_price = info.get("currentPrice")
            target_price = info.get("targetMeanPrice")
            row.update(
                market_cap=info.get("marketCap"),
                avg_volume=info.get("averageVolume"),
                revenue_growth=info.get("revenueGrowth"),
                earnings_growth=info.get("earningsGrowth"),
                earnings_q_growth=info.get("earningsQuarterlyGrowth"),
                forward_pe=info.get("forwardPE"),
                target_upside=(target_price / current_price - 1)
                if target_price and current_price
                else np.nan,
                recommendation=info.get("recommendationMean"),
                sector=info.get("sector"),
                industry=info.get("industry"),
            )
        rows.append(row)

        if i % 25 == 0:
            pd.DataFrame(rows).reindex(columns=cols).to_csv(checkpoint, index=False)
            print(f"Fundamentals progress: {i}/{len(tickers)}", flush=True)

    frame = pd.DataFrame(rows).reindex(columns=cols)
    frame.to_csv(checkpoint, index=False)
    return frame, reused, downloaded


def price_rows_from_download(data, batch):
    rows = []
    try:
        close = data["Close"]
        volume = data["Volume"]
    except Exception as exc:
        print(f"Price batch schema failure: {batch}: {exc}", flush=True)
        return rows

    for ticker in batch:
        try:
            if isinstance(close, pd.Series):
                if len(batch) != 1:
                    raise ValueError("single-series response for a multi-ticker batch")
                c = close.dropna()
                v = volume.reindex(c.index)
            elif isinstance(close.columns, pd.MultiIndex):
                c = close[ticker].dropna()
                v = volume[ticker].reindex(c.index)
            elif ticker in close.columns:
                c = close[ticker].dropna()
                v = volume[ticker].reindex(c.index)
            elif len(batch) == 1 and "Close" in data.columns:
                c = data["Close"].dropna()
                v = data["Volume"].reindex(c.index)
            else:
                continue
            if len(c) < 130:
                continue
            price = c.iloc[-1]
            high_52 = c.tail(252).max()
            low_52 = c.tail(252).min()
            rows.append(
                dict(
                    ticker=ticker,
                    price=price,
                    ret_5=price / c.iloc[-6] - 1,
                    ret_20=price / c.iloc[-21] - 1,
                    ret_60=price / c.iloc[-61] - 1,
                    ret_120=price / c.iloc[-121] - 1,
                    drawdown_52=price / high_52 - 1,
                    off_low_52=price / low_52 - 1,
                    ma20=price / c.tail(20).mean() - 1,
                    ma50=price / c.tail(50).mean() - 1,
                    vol_ratio=v.tail(10).mean() / (v.tail(60).mean() + 1e-9),
                    dollar_volume=(c.tail(20) * v.tail(20)).mean(),
                    volatility=c.pct_change().tail(60).std() * math.sqrt(252),
                )
            )
        except Exception as exc:
            print(f"Price metric skip {ticker}: {exc}", flush=True)
    return rows


def download_prices(batch, label):
    return retry_yahoo(
        lambda: yf.download(
            batch,
            period="1y",
            interval="1d",
            group_by="column",
            auto_adjust=True,
            threads=False,
            progress=False,
            timeout=30,
        ),
        label,
        request_units=len(batch),
        validator=valid_price_download,
    )


def prices(tickers):
    rows = []
    request_failures = []
    batch_size = YAHOO_PRICE_BATCH_SIZE
    for start in range(0, len(tickers), batch_size):
        batch = tickers[start : start + batch_size]
        data = download_prices(batch, f"prices batch {start // batch_size + 1}")
        if data is not None:
            rows.extend(price_rows_from_download(data, batch))
        else:
            print(
                f"Batch failed after retries; isolating tickers one by one: {batch}",
                flush=True,
            )
            for ticker in batch:
                single = download_prices([ticker], f"price fallback {ticker}")
                if single is None:
                    request_failures.append(ticker)
                else:
                    rows.extend(price_rows_from_download(single, [ticker]))

        if (start // batch_size + 1) % 10 == 0:
            print(
                f"Price progress: {min(start + batch_size, len(tickers))}/{len(tickers)}",
                flush=True,
            )
    return pd.DataFrame(rows), request_failures


def benchmark_metrics():
    data = retry_yahoo(
        lambda: yf.download(
            "SPY",
            period="1y",
            interval="1d",
            auto_adjust=True,
            threads=False,
            progress=False,
            timeout=30,
        ),
        "SPY benchmark",
        validator=valid_price_download,
    )
    if data is None or data.empty:
        raise RuntimeError("SPY benchmark unavailable; refusing incomplete relative-strength screen")
    close = data["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]
    close = close.dropna()
    if len(close) < 121:
        raise RuntimeError("SPY benchmark history insufficient")
    price = close.iloc[-1]
    return {
        "spy_ret_20": price / close.iloc[-21] - 1,
        "spy_ret_60": price / close.iloc[-61] - 1,
        "spy_ret_120": price / close.iloc[-121] - 1,
    }


def score(df, benchmark):
    # Peer and benchmark relative strength.
    sector_median = df.groupby("sector")["ret_60"].transform("median")
    industry_median = df.groupby("industry")["ret_60"].transform("median")
    df["sector_rs_60"] = df.ret_60 - sector_median
    df["industry_rs_60"] = df.ret_60 - industry_median
    df["spy_rs_20"] = df.ret_20 - benchmark["spy_ret_20"]
    df["spy_rs_60"] = df.ret_60 - benchmark["spy_ret_60"]
    df["spy_rs_120"] = df.ret_120 - benchmark["spy_ret_120"]

    # Fundamental ranks. Missing values remain missing; no arbitrary filler scores.
    rev_growth = pct_rank(df.revenue_growth)
    earn_growth = pct_rank(df.earnings_growth)
    earn_q_growth = pct_rank(df.earnings_q_growth)
    growth_accel_raw = pd.to_numeric(df.earnings_q_growth, errors="coerce") - pd.to_numeric(
        df.earnings_growth, errors="coerce"
    )
    growth_accel = pct_rank(growth_accel_raw)
    valuation = inverse_pct_rank(df.forward_pe)
    target = pct_rank(df.target_upside)
    recommendation = 100 - pct_rank(df.recommendation)
    liquidity = pct_rank(df.dollar_volume)

    # 1) Leadership / Momentum
    df["leadership_momentum"], df["leadership_coverage"] = weighted_available_score(
        [
            (pct_rank(df.ret_60), 0.14),
            (pct_rank(df.ret_20), 0.08),
            (pct_rank(df.spy_rs_60), 0.10),
            (pct_rank(df.sector_rs_60), 0.08),
            (pct_rank(df.industry_rs_60), 0.07),
            (rev_growth, 0.11),
            (earn_growth, 0.10),
            (earn_q_growth, 0.07),
            (pct_rank(df.vol_ratio), 0.06),
            (target, 0.04),
            (recommendation, 0.03),
            (valuation, 0.04),
            (liquidity, 0.08),
        ]
    )

    # 2) Beaten-Down / Reversal: being down alone is not enough; reversal and
    # fundamental confirmation carry more weight than drawdown itself.
    drawdown_rank = pct_rank(-df.drawdown_52)
    reversal_rank = pct_rank((df.ret_5 + df.ret_20 + df.ma20) / 3)
    df["beaten_down_reversal"], df["reversal_coverage"] = weighted_available_score(
        [
            (drawdown_rank, 0.15),
            (reversal_rank, 0.18),
            (pct_rank(df.vol_ratio), 0.08),
            (pct_rank(df.spy_rs_20), 0.08),
            (pct_rank(df.sector_rs_60), 0.06),
            (pct_rank(df.industry_rs_60), 0.05),
            (rev_growth, 0.10),
            (earn_growth, 0.10),
            (earn_q_growth, 0.07),
            (target, 0.04),
            (valuation, 0.03),
            (liquidity, 0.06),
        ]
    )

    # 3) Acceleration / Emerging Momentum. This detects the fingerprints of an
    # emerging move; it deliberately does NOT claim that a catalyst was found.
    return_accel = pct_rank(df.ret_20 - df.ret_60 / 3)
    df["acceleration_emerging_momentum"], df["acceleration_coverage"] = weighted_available_score(
        [
            (return_accel, 0.16),
            (pct_rank(df.vol_ratio), 0.10),
            (pct_rank(df.spy_rs_20), 0.09),
            (pct_rank(df.spy_rs_60), 0.07),
            (pct_rank(df.sector_rs_60), 0.06),
            (pct_rank(df.industry_rs_60), 0.05),
            (rev_growth, 0.10),
            (earn_growth, 0.08),
            (earn_q_growth, 0.09),
            (growth_accel, 0.06),
            (target, 0.04),
            (valuation, 0.03),
            (liquidity, 0.07),
        ]
    )

    # Explicit evidence coverage. Price/volume factors are already mandatory by
    # construction; this measures how much secondary evidence backs the score.
    secondary_cols = [
        "revenue_growth",
        "earnings_growth",
        "earnings_q_growth",
        "forward_pe",
        "target_upside",
        "recommendation",
        "sector",
        "industry",
    ]
    secondary_coverage = df[secondary_cols].notna().mean(axis=1)
    lens_coverage = df[
        ["leadership_coverage", "reversal_coverage", "acceleration_coverage"]
    ].max(axis=1)
    df["data_confidence"] = (0.65 * lens_coverage + 0.35 * secondary_coverage).clip(0, 1)

    lens_values = df[list(LENSES)].apply(pd.to_numeric, errors="coerce")
    all_na = lens_values.isna().all(axis=1)
    df["best_lens"] = lens_values.max(axis=1, skipna=True)
    df["lens_winner"] = pd.Series(pd.NA, index=df.index, dtype="object")
    if (~all_na).any():
        df.loc[~all_na, "lens_winner"] = lens_values.loc[~all_na].idxmax(axis=1, skipna=True)
    df["lens_data_missing"] = all_na

    # Risk is quantitative triage, not the final downside thesis.
    extension = pct_rank(pd.to_numeric(df.ma20, errors="coerce").clip(lower=0))
    df["risk_score"], _ = weighted_available_score(
        [
            (pct_rank(df.volatility), 0.30),
            (100 - pct_rank(df.ret_20), 0.20),
            (100 - liquidity, 0.20),
            (extension, 0.15),
            (pct_rank(-df.drawdown_52), 0.15),
        ]
    )

    mean_lens = lens_values.mean(axis=1, skipna=True)
    confidence_component = df.data_confidence * 100
    df["final_quant_score"] = (
        df.best_lens * 0.75
        + mean_lens * 0.18
        + confidence_component * 0.07
        - np.maximum(df.risk_score - 70, 0) * 0.25
    ).clip(0, 100)
    df.loc[all_na, "final_quant_score"] = np.nan

    # Flags only. These are not substitutes for current company-specific review.
    industry = df.industry.fillna("")
    name = df.name.fillna("")
    df["biotech_review"] = df.sector.eq("Healthcare") & industry.str.contains(
        r"Biotech|Biotechnology", case=False, regex=True
    )
    df["crypto_proxy_review"] = industry.str.contains(
        r"Crypto|Blockchain", case=False, regex=True
    ) | name.str.contains(r"Bitcoin|Crypto|Blockchain", case=False, regex=True)
    df["special_risk_review"] = df.biotech_review | df.crypto_proxy_review

    return df


def main():
    u = universe()
    u.to_csv(OUT / "01_starting_universe.csv", index=False)
    print(f"Starting universe: {len(u)}", flush=True)

    p, price_request_failures = prices(u.ticker.tolist())
    p.to_csv(OUT / "02_price_metrics.csv", index=False)
    pd.DataFrame({"ticker": price_request_failures}).to_csv(
        OUT / "02_price_request_failures.csv", index=False
    )
    failure_rate = len(price_request_failures) / max(len(u), 1)
    if failure_rate > MAX_PRICE_REQUEST_FAILURE_RATE:
        raise RuntimeError(
            f"Price request failure rate {failure_rate:.2%} exceeds "
            f"{MAX_PRICE_REQUEST_FAILURE_RATE:.2%}; refusing incomplete screen"
        )
    if p.empty or not {"ticker", "price", "dollar_volume"}.issubset(p.columns):
        raise RuntimeError("Price stage produced insufficient schema; refusing incomplete screen")

    investable = u.merge(p, on="ticker", how="inner")
    investable = investable[
        (investable.price >= 3) & (investable.dollar_volume >= 2_000_000)
    ]
    investable.to_csv(OUT / "03_investable.csv", index=False)

    benchmark = benchmark_metrics()
    f, cache_reused, fresh_downloaded = fundamentals(investable.ticker.tolist())
    e = investable.merge(f, on="ticker", how="left")
    if "market_cap" not in e.columns:
        raise RuntimeError("market_cap unavailable; refusing incomplete screen")

    missing_mc = int(e.market_cap.isna().sum())
    print(
        f"Fundamentals coverage: {len(e) - missing_mc}/{len(e)} market caps",
        flush=True,
    )
    e = e[e.market_cap.fillna(0) >= 200_000_000]
    if e.empty:
        raise RuntimeError("No eligible securities after investability filters")

    s = score(e, benchmark)
    missing_lens = int(s.lens_data_missing.sum())
    print(f"All-lens missing rows safely excluded: {missing_lens}", flush=True)
    s = s.sort_values("final_quant_score", ascending=False, na_position="last")
    s.to_csv(OUT / "04_all_scored.csv", index=False)

    scoreable = s[s.final_quant_score.notna()].copy()
    if scoreable.empty:
        raise RuntimeError("No securities have scoreable three-lens data")

    confidence_eligible = scoreable[
        scoreable.data_confidence >= MIN_DATA_CONFIDENCE
    ].copy()
    if confidence_eligible.empty:
        raise RuntimeError("No securities passed the explicit data-confidence gate")

    semis = (
        pd.concat(
            [confidence_eligible.nlargest(SEMIFINALISTS_PER_LENS, lens) for lens in LENSES]
        )
        .drop_duplicates("ticker")
        .sort_values("final_quant_score", ascending=False)
    )
    semis.to_csv(OUT / "05_semifinalists.csv", index=False)

    candidates = semis.head(QUANT_CANDIDATES).copy()
    candidates["current_verification_required"] = True
    candidates["catalyst_status"] = "NOT_YET_RESEARCHED"
    candidates["estimate_revision_status"] = "NOT_YET_RESEARCHED"
    candidates["guidance_status"] = "NOT_YET_RESEARCHED"
    candidates["dilution_financing_status"] = "NOT_YET_RESEARCHED"
    candidates["binary_risk_status"] = "NOT_YET_RESEARCHED"
    candidates.to_csv(
        OUT / "06_quant_candidates_REQUIRES_CURRENT_VERIFICATION.csv", index=False
    )

    audit = {
        "starting_universe": len(u),
        "price_eligible": len(p),
        "price_request_failures": len(price_request_failures),
        "price_request_failure_rate": failure_rate,
        "investable_before_marketcap": len(investable),
        "fundamentals_requested": len(f),
        "fundamentals_cache_reused_fresh": cache_reused,
        "fundamentals_fresh_downloaded": fresh_downloaded,
        "fundamentals_cache_ttl_hours": FUNDAMENTALS_CACHE_TTL_HOURS,
        "market_cap_missing": missing_mc,
        "all_lens_missing": missing_lens,
        "scoreable": len(scoreable),
        "confidence_threshold": MIN_DATA_CONFIDENCE,
        "confidence_eligible": len(confidence_eligible),
        "semifinalists": len(semis),
        "quant_candidates": len(candidates),
        "yahoo_rate_cap_per_minute": YAHOO_RATE_CAP_PER_MINUTE,
        "yahoo_price_batch_size": YAHOO_PRICE_BATCH_SIZE,
        "spy_benchmark": benchmark,
        "three_lenses": list(LENSES),
        "market_wide_catalyst_claimed": False,
        "estimate_revisions_claimed_market_wide": False,
        "FINAL_LABEL_ALLOWED": False,
        "note": (
            "Quant candidates require fresh current verification of earnings, guidance, "
            "estimate revisions, beat/raise execution, catalyst if any, technical condition, "
            "valuation/runway, downside, financing/dilution and special/binary risk before FINAL ranking."
        ),
    }
    (OUT / "audit.json").write_text(json.dumps(audit, indent=2))
    print(json.dumps(audit, indent=2), flush=True)
    print(
        candidates[
            ["ticker", "lens_winner", "data_confidence", "final_quant_score", "special_risk_review"]
        ].to_string(index=False),
        flush=True,
    )


if __name__ == "__main__":
    main()
