from __future__ import annotations

import io
import math
import random
import re
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd
import requests
import yfinance as yf

from engine4_config import (
    BATCH_SIZE_BROAD,
    BATCH_SIZE_DEEP,
    ET,
    MAX_SPREAD_PCT,
    YAHOO_RATE_CAP_PER_MINUTE,
)

BASE_OUT = Path("output")
_last_yahoo_call = 0.0
YAHOO_MIN_INTERVAL = 60.0 / YAHOO_RATE_CAP_PER_MINUTE

CATALYST_RULES = [
    (1.00, re.compile(r"\b(earnings|eps|revenue)\b.*\b(beat|beats|above|surge|record)\b|\b(raises?|raised|boosts?|boosted)\b.*\b(guidance|outlook|forecast)\b", re.I)),
    (1.00, re.compile(r"\b(fda|approval|approved|phase [123]|clinical trial|pdufa|regulatory approval)\b", re.I)),
    (0.95, re.compile(r"\b(acquire[sd]?|acquisition|merger|buyout|takeover|strategic review)\b", re.I)),
    (0.90, re.compile(r"\b(contract|award|deal|partnership|agreement)\b.*\b(million|billion|major|multi[- ]year|exclusive)\b", re.I)),
    (0.80, re.compile(r"\b(upgrade[sd]?|price target)\b.*\b(buy|outperform|overweight|raised|increase)\b", re.I)),
    (0.75, re.compile(r"\b(buyback|repurchase|dividend increase|special dividend)\b", re.I)),
    (0.65, re.compile(r"\b(launch|patent|settlement|court|government|defense|order|customer)\b", re.I)),
]
NEGATIVE_CATALYST = re.compile(r"\b(downgrade|offering|dilution|bankruptcy|chapter 11|fraud|investigation|misses|cuts guidance|lowered guidance)\b", re.I)
PROMOTIONAL = re.compile(r"\b(penny stock|stock promotion|paid promotion|pump|discord|telegram)\b", re.I)


def now_et() -> datetime:
    return datetime.now(timezone.utc).astimezone(ET)


def yahoo_pace() -> None:
    global _last_yahoo_call
    wait = YAHOO_MIN_INTERVAL - (time.monotonic() - _last_yahoo_call)
    if wait > 0:
        time.sleep(wait)
    _last_yahoo_call = time.monotonic()


def retry_yahoo(fn, label: str, attempts: int = 4):
    last = None
    for attempt in range(attempts):
        yahoo_pace()
        try:
            return fn()
        except Exception as exc:
            last = exc
            if attempt < attempts - 1:
                time.sleep(min(12, 1.5 * (2**attempt)) + random.uniform(0, 1))
    print(f"Yahoo failed {label}: {last}", flush=True)
    return None


def batches(items: Sequence[str], n: int) -> Iterable[List[str]]:
    for i in range(0, len(items), n):
        yield list(items[i : i + n])


def ensure_et_index(frame: pd.DataFrame) -> pd.DataFrame:
    if frame is None or frame.empty:
        return pd.DataFrame()
    out = frame.copy()
    idx = pd.DatetimeIndex(out.index)
    if idx.tz is None:
        idx = idx.tz_localize("UTC")
    idx = idx.tz_convert(ET)
    out.index = idx
    return out


def extract_symbol(download: pd.DataFrame, ticker: str) -> pd.DataFrame:
    if download is None or download.empty:
        return pd.DataFrame()
    if isinstance(download.columns, pd.MultiIndex):
        lv0 = set(map(str, download.columns.get_level_values(0)))
        lv1 = set(map(str, download.columns.get_level_values(1)))
        try:
            if ticker in lv1:
                frame = download.xs(ticker, axis=1, level=1)
            elif ticker in lv0:
                frame = download.xs(ticker, axis=1, level=0)
            else:
                return pd.DataFrame()
        except Exception:
            return pd.DataFrame()
    else:
        frame = download.copy()
    return ensure_et_index(frame)


def _fresh_exchange_universe() -> pd.DataFrame:
    """Build today's U.S.-listed common-stock/ADR universe independently of Engines 1-3."""
    urls = [
        "https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt",
        "https://www.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt",
    ]
    frames = []
    headers = {"User-Agent": "Mozilla/5.0 engine4-universe-audit"}
    for url in urls:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        frames.append(pd.read_csv(io.StringIO(response.text), sep="|"))
    a, b = frames
    a = a.rename(columns={"Symbol":"ticker","Security Name":"name","ETF":"etf","Test Issue":"test"})
    b = b.rename(columns={"ACT Symbol":"ticker","Security Name":"name","ETF":"etf","Test Issue":"test"})
    x = pd.concat([a[["ticker","name","etf","test"]], b[["ticker","name","etf","test"]]], ignore_index=True)
    x = x[(x.etf == "N") & (x.test == "N")].dropna(subset=["ticker"])
    x["ticker"] = x.ticker.astype(str).str.upper().str.strip()
    x = x[~x.ticker.str.contains(r"[.$]", regex=True)]
    bad = r"Warrant|Right| Unit|Preferred|Depositary Shares|Acquisition Corp|SPAC"
    x = x[~x.name.str.contains(bad, case=False, na=False, regex=True)]
    return x.drop_duplicates("ticker").reset_index(drop=True)


def load_baseline() -> pd.DataFrame:
    """Fresh universe + market data, with legacy baseline only as metadata fallback.

    This repairs the feeder only. Engine 4 thresholds/scoring/stages are unchanged.
    A ticker is no longer excluded merely because a stale Engines 1-3 output omitted it
    or Yahoo Ticker.info failed during an earlier fundamentals pass.
    """
    universe = _fresh_exchange_universe()
    legacy_inv_path = BASE_OUT / "03_investable.csv"
    legacy_fund_path = BASE_OUT / "fundamentals_checkpoint.csv"
    legacy_inv = pd.read_csv(legacy_inv_path) if legacy_inv_path.exists() else pd.DataFrame()
    legacy_fund = pd.read_csv(legacy_fund_path) if legacy_fund_path.exists() else pd.DataFrame()
    legacy = pd.DataFrame()
    if not legacy_inv.empty:
        legacy = legacy_inv.copy()
        if not legacy_fund.empty and {"ticker","market_cap","sector"}.issubset(legacy_fund.columns):
            legacy = legacy.merge(legacy_fund[["ticker","market_cap","sector"]], on="ticker", how="left", suffixes=("","_fund"))
        legacy["ticker"] = legacy.ticker.astype(str).str.upper()
        legacy = legacy.drop_duplicates("ticker").set_index("ticker")

    rows = []
    batch_size = 100
    symbols = universe.ticker.tolist()
    for number, batch in enumerate(batches(symbols, batch_size), 1):
        data = retry_yahoo(lambda b=batch: yf.download(
            b, period="1mo", interval="1d", group_by="column", auto_adjust=True,
            actions=False, threads=True, progress=False, timeout=30,
        ), f"fresh universe daily batch {number}")
        if data is None or data.empty:
            continue
        for ticker in batch:
            frame = extract_symbol(data, ticker)
            if frame.empty or "Close" not in frame or "Volume" not in frame:
                continue
            close = pd.to_numeric(frame["Close"], errors="coerce").dropna()
            vol = pd.to_numeric(frame["Volume"], errors="coerce").reindex(close.index).fillna(0)
            if close.empty:
                continue
            price = float(close.iloc[-1])
            dollar_volume = float((close.tail(20) * vol.tail(20)).mean())
            name = universe.loc[universe.ticker.eq(ticker), "name"].iloc[0]
            market_cap = np.nan
            sector = ""
            if not legacy.empty and ticker in legacy.index:
                old = legacy.loc[ticker]
                market_cap = pd.to_numeric(old.get("market_cap"), errors="coerce")
                sector = str(old.get("sector") or "")
            # Refresh market cap only where legacy metadata is absent/stale; failure is
            # explicit and auditable rather than silently deleting the symbol upstream.
            if not math.isfinite(float(market_cap)) if pd.notna(market_cap) else True:
                info = retry_yahoo(lambda t=ticker: yf.Ticker(t).fast_info, f"fast fundamentals {ticker}", attempts=3)
                if info:
                    try:
                        market_cap = float(info.get("market_cap") or info.get("marketCap") or np.nan)
                    except Exception:
                        market_cap = np.nan
            rows.append({"ticker":ticker,"name":name,"price":price,"dollar_volume":dollar_volume,
                         "market_cap":market_cap,"sector":sector})

    merged = pd.DataFrame(rows)
    if merged.empty:
        raise RuntimeError("Fresh exchange universe produced no usable market data")
    for col in ["price","dollar_volume","market_cap"]:
        merged[col] = pd.to_numeric(merged[col], errors="coerce")
    audit = {
        "exchange_common_adr_count": int(len(universe)),
        "market_data_count": int(len(merged)),
        "missing_market_cap_count": int(merged.market_cap.isna().sum()),
        "legacy_metadata_overlap": int(merged.ticker.isin(legacy.index if not legacy.empty else []).sum()),
        "source": "Nasdaq Trader nasdaqlisted.txt + otherlisted.txt; fresh Yahoo batched daily market data",
    }
    (BASE_OUT / "engine4_universe_audit.json").write_text(__import__("json").dumps(audit, indent=2), encoding="utf-8")
    return merged.drop_duplicates("ticker").reset_index(drop=True)

def download_intraday(
    tickers: Sequence[str],
    *,
    period: str = "1d",
    interval: str = "1m",
    prepost: bool = True,
    date_et=None,
    lookback_days: int = 0,
) -> Dict[str, pd.DataFrame]:
    result: Dict[str, pd.DataFrame] = {}
    batch_size = BATCH_SIZE_BROAD if period == "1d" and lookback_days <= 1 else BATCH_SIZE_DEEP
    for number, batch in enumerate(batches(list(tickers), batch_size), 1):
        def fetch(b=batch):
            kwargs = dict(
                tickers=b,
                interval=interval,
                prepost=prepost,
                group_by="column",
                auto_adjust=False,
                actions=False,
                threads=True,
                progress=False,
                timeout=25,
            )
            if date_et is None:
                kwargs["period"] = period
            else:
                kwargs["start"] = str(date_et - timedelta(days=lookback_days))
                kwargs["end"] = str(date_et + timedelta(days=1))
            return yf.download(**kwargs)
        data = retry_yahoo(fetch, f"intraday batch {number}")
        if data is None or data.empty:
            continue
        for ticker in batch:
            frame = extract_symbol(data, ticker)
            if not frame.empty:
                result[ticker] = frame
    return result


def slice_window(frame: pd.DataFrame, date_et, start_hhmm: str, end_hhmm: str, inclusive: str = "both") -> pd.DataFrame:
    frame = ensure_et_index(frame)
    if frame.empty:
        return frame
    same_day = frame[frame.index.date == date_et]
    if same_day.empty:
        return same_day
    return same_day.between_time(start_hhmm, end_hhmm, inclusive=inclusive)


def prior_regular_close(frame: pd.DataFrame, date_et) -> float:
    frame = ensure_et_index(frame)
    prior = frame[frame.index.date < date_et]
    if prior.empty:
        return np.nan
    reg = prior.between_time("09:30", "16:00", inclusive="both")
    if reg.empty or "Close" not in reg:
        return np.nan
    close = pd.to_numeric(reg["Close"], errors="coerce").dropna()
    return float(close.iloc[-1]) if not close.empty else np.nan


def historical_premarket_baseline(frame: pd.DataFrame, current_date, end_hhmm: str) -> float:
    frame = ensure_et_index(frame)
    volumes = []
    for d in sorted(set(frame.index.date)):
        if d >= current_date:
            continue
        pm = slice_window(frame, d, "04:00", end_hhmm)
        if not pm.empty and "Volume" in pm:
            vol = float(pd.to_numeric(pm["Volume"], errors="coerce").fillna(0).sum())
            if vol > 0:
                volumes.append(vol)
    return float(np.median(volumes[-5:])) if volumes else np.nan


def download_daily_metrics(tickers: Sequence[str], asof_date=None) -> Dict[str, Dict[str, float]]:
    output: Dict[str, Dict[str, float]] = {}
    for number, batch in enumerate(batches(list(tickers), BATCH_SIZE_DEEP), 1):
        data = retry_yahoo(
            lambda b=batch: yf.download(
                b,
                period="6mo",
                interval="1d",
                group_by="column",
                auto_adjust=True,
                actions=False,
                threads=True,
                progress=False,
                timeout=25,
            ),
            f"daily metrics batch {number}",
        )
        if data is None or data.empty:
            continue
        for ticker in batch:
            frame = extract_symbol(data, ticker)
            if frame.empty:
                continue
            if asof_date is not None:
                frame = frame[frame.index.date < asof_date]
            required = [c for c in ["High", "Low", "Close"] if c in frame.columns]
            if len(required) < 3:
                continue
            frame = frame.dropna(subset=required)
            if len(frame) < 20:
                continue
            high = pd.to_numeric(frame["High"], errors="coerce")
            low = pd.to_numeric(frame["Low"], errors="coerce")
            close = pd.to_numeric(frame["Close"], errors="coerce")
            prev_close = close.shift(1)
            true_range = pd.concat(
                [(high-low).abs(), (high-prev_close).abs(), (low-prev_close).abs()], axis=1
            ).max(axis=1)
            levels = [float(high.tail(n).max()) for n in (5, 20, 60) if len(high) >= n]
            output[ticker] = {
                "atr": float(true_range.tail(14).mean()),
                "high_5": levels[0] if levels else np.nan,
                "high_20": levels[1] if len(levels) > 1 else np.nan,
                "high_60": levels[2] if len(levels) > 2 else np.nan,
            }
    return output


def parse_news_item(item: dict) -> Tuple[str, Optional[datetime]]:
    if not isinstance(item, dict):
        return "", None
    content = item.get("content") if isinstance(item.get("content"), dict) else {}
    title = str(item.get("title") or content.get("title") or "").strip()
    summary = str(content.get("summary") or item.get("summary") or "").strip()
    text = (title + " " + summary).strip()
    raw = item.get("providerPublishTime") or content.get("pubDate") or item.get("pubDate")
    timestamp = None
    try:
        if isinstance(raw, (int, float)):
            timestamp = datetime.fromtimestamp(raw, timezone.utc)
        elif raw:
            timestamp = pd.Timestamp(raw).to_pydatetime()
            if timestamp.tzinfo is None:
                timestamp = timestamp.replace(tzinfo=timezone.utc)
    except Exception:
        timestamp = None
    return text, timestamp


def catalyst_for(ticker: str, reference_time: datetime) -> Tuple[float, str, float]:
    news = retry_yahoo(lambda: yf.Ticker(ticker).news, f"news {ticker}", attempts=3)
    if not news:
        return 0.0, "", math.inf
    best = (0.0, "", math.inf)
    ref_utc = reference_time.astimezone(timezone.utc)
    for item in news[:12]:
        text, timestamp = parse_news_item(item)
        if not text or PROMOTIONAL.search(text):
            continue
        age = math.inf
        if timestamp:
            ts_utc = timestamp.astimezone(timezone.utc)
            if ts_utc > ref_utc:
                continue
            age = max(0.0, (ref_utc - ts_utc).total_seconds() / 3600.0)
        if age > 48:
            continue
        quality = 0.0
        if not NEGATIVE_CATALYST.search(text):
            for score, pattern in CATALYST_RULES:
                if pattern.search(text):
                    quality = max(quality, score)
        freshness = 1.0 if age <= 12 else 0.8 if age <= 24 else 0.6
        quality *= freshness
        if quality > best[0]:
            headline = text.split("  ")[0][:180]
            best = (quality, headline, age)
    return best


def quote_spread(ticker: str) -> Tuple[float, float, float]:
    info = retry_yahoo(lambda: yf.Ticker(ticker).info, f"quote {ticker}", attempts=3)
    if not info:
        return np.nan, np.nan, np.nan
    bid = float(info.get("bid") or np.nan)
    ask = float(info.get("ask") or np.nan)
    if not (math.isfinite(bid) and math.isfinite(ask) and bid > 0 and ask >= bid):
        return bid, ask, np.nan
    mid = (bid + ask) / 2.0
    spread = (ask - bid) / mid * 100.0 if mid > 0 else np.nan
    return bid, ask, spread


def data_smoke(sample: Sequence[str]) -> dict:
    started = time.monotonic()
    intraday = download_intraday(sample, period="5d", interval="1m", prepost=True)
    news_quality, news_text, _ = catalyst_for(sample[0], now_et())
    bid, ask, spread = quote_spread(sample[0])
    return {
        "requested": len(sample),
        "intraday_returned": len(intraday),
        "sample_news_reachable": bool(news_text or news_quality == 0.0),
        "sample_quote_reachable": bool(math.isfinite(bid) or math.isfinite(ask) or math.isnan(spread)),
        "runtime_seconds": round(time.monotonic() - started, 3),
    }
