from __future__ import annotations

import math
import random
import re
import threading
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from typing import Dict, Iterable, Tuple
from urllib.parse import quote_plus

import requests

NASDAQ_HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://www.nasdaq.com",
    "Referer": "https://www.nasdaq.com/",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/138 Safari/537.36",
}

_thread_local = threading.local()


def _session() -> requests.Session:
    s = getattr(_thread_local, "session", None)
    if s is None:
        s = requests.Session()
        s.headers.update(NASDAQ_HEADERS)
        _thread_local.session = s
    return s


def _num(value) -> float:
    if value is None:
        return math.nan
    text = str(value).strip().replace(",", "").replace("$", "").replace("%", "")
    text = re.sub(r"[^0-9.+-]", "", text)
    if text in {"", ".", "+", "-"}:
        return math.nan
    try:
        return float(text)
    except Exception:
        return math.nan


def _get_json(url: str, attempts: int = 2, timeout: float = 6.0) -> dict | None:
    for attempt in range(attempts):
        try:
            r = _session().get(url, timeout=timeout)
            if r.status_code == 200:
                payload = r.json()
                if isinstance(payload, dict) and payload.get("data") is not None:
                    return payload
        except Exception:
            pass
        if attempt < attempts - 1:
            time.sleep(0.20 * (attempt + 1) + random.uniform(0.0, 0.15))
    return None


def nasdaq_premarket_snapshot(ticker: str, *, attempts: int = 2, timeout: float = 6.0) -> dict:
    ticker = ticker.upper()
    url = f"https://api.nasdaq.com/api/quote/{ticker}/extended-trading?assetclass=stocks&markettype=pre"
    payload = _get_json(url, attempts=attempts, timeout=timeout)
    out = {
        "ticker": ticker,
        "ok": False,
        "premarket_volume": math.nan,
        "premarket_price": math.nan,
        "premarket_high": math.nan,
        "premarket_low": math.nan,
        "source": "Nasdaq extended-trading",
    }
    if not payload:
        return out
    try:
        data = payload.get("data") or {}
        rows = (((data.get("infoTable") or {}).get("rows")) or [])
        if not rows:
            return out
        row = rows[0] or {}
        consolidated = str(row.get("consolidated") or "")
        price_match = re.search(r"\$?([0-9][0-9,]*(?:\.[0-9]+)?)", consolidated)
        price = _num(price_match.group(1)) if price_match else math.nan
        volume = _num(row.get("volume"))
        high = _num(row.get("highPrice"))
        low = _num(row.get("lowPrice"))
        out.update(
            ok=bool(math.isfinite(price) and price > 0 and math.isfinite(volume) and volume >= 0),
            premarket_volume=volume,
            premarket_price=price,
            premarket_high=high,
            premarket_low=low,
        )
    except Exception:
        return out
    return out


def nasdaq_premarket_many(tickers: Iterable[str], max_workers: int = 24) -> Dict[str, dict]:
    """Fast bulk enrichment.

    Bulk calls use one 4-second attempt per symbol. A few misses are acceptable because the
    enrichment pool is intentionally much larger than the final Top-100. Provider health is
    checked separately with retries before the stage begins.
    """
    symbols = list(dict.fromkeys(str(t).upper() for t in tickers if str(t).strip()))
    results: Dict[str, dict] = {}
    if not symbols:
        return results
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futs = {
            pool.submit(nasdaq_premarket_snapshot, t, attempts=1, timeout=4.0): t
            for t in symbols
        }
        for fut in as_completed(futs):
            ticker = futs[fut]
            try:
                results[ticker] = fut.result()
            except Exception:
                results[ticker] = {"ticker": ticker, "ok": False, "source": "Nasdaq extended-trading"}
    return results


def nasdaq_quote_spread(ticker: str) -> Tuple[float, float, float]:
    ticker = ticker.upper()
    url = f"https://api.nasdaq.com/api/quote/{ticker}/info?assetclass=stocks"
    payload = _get_json(url, attempts=2, timeout=5.0)
    if not payload:
        return math.nan, math.nan, math.nan
    try:
        primary = ((payload.get("data") or {}).get("primaryData") or {})
        bid = _num(primary.get("bidPrice"))
        ask = _num(primary.get("askPrice"))
        if not (math.isfinite(bid) and math.isfinite(ask) and bid > 0 and ask >= bid):
            return bid, ask, math.nan
        mid = (bid + ask) / 2.0
        spread = (ask - bid) / mid * 100.0 if mid > 0 else math.nan
        return bid, ask, spread
    except Exception:
        return math.nan, math.nan, math.nan


def _google_news_items(query: str, limit: int = 12) -> list[tuple[str, datetime | None]]:
    q = quote_plus(query)
    url = f"https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"
    try:
        r = _session().get(url, headers={"User-Agent": NASDAQ_HEADERS["User-Agent"]}, timeout=5)
        if r.status_code != 200:
            return []
        root = ET.fromstring(r.content)
    except Exception:
        return []
    out = []
    for item in root.findall(".//item")[:limit]:
        title = (item.findtext("title") or "").strip()
        raw = (item.findtext("pubDate") or "").strip()
        ts = None
        if raw:
            try:
                from email.utils import parsedate_to_datetime
                ts = parsedate_to_datetime(raw)
                if ts.tzinfo is None:
                    ts = ts.replace(tzinfo=timezone.utc)
            except Exception:
                ts = None
        if title:
            out.append((title, ts))
    return out


def google_news_catalyst(
    ticker: str,
    reference_time: datetime,
    catalyst_rules,
    negative_pattern,
    promotional_pattern,
    company_name: str | None = None,
) -> Tuple[float, str, float]:
    ticker = ticker.upper()
    company_term = ""
    if company_name:
        cleaned = re.sub(r"\b(Common Stock|Class [A-Z]|Inc\.?|Corporation|Corp\.?|Ltd\.?|PLC|Holdings?)\b", "", company_name, flags=re.I)
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        if cleaned:
            company_term = f' OR "{cleaned}"'
    query = f'("{ticker}" stock{company_term}) when:2d'
    items = _google_news_items(query, limit=15)
    if not items:
        return 0.0, "", math.inf

    ref_utc = reference_time.astimezone(timezone.utc)
    best = (0.0, "", math.inf)
    for text, timestamp in items:
        if promotional_pattern.search(text):
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
        if not negative_pattern.search(text):
            for score, pattern in catalyst_rules:
                if pattern.search(text):
                    quality = max(quality, score)
        freshness = 1.0 if age <= 12 else 0.8 if age <= 24 else 0.6
        quality *= freshness
        if quality > best[0]:
            best = (quality, text[:180], age)
    return best


def provider_smoke() -> dict:
    pm = nasdaq_premarket_snapshot("NVDA", attempts=2, timeout=6.0)
    bid, ask, spread = nasdaq_quote_spread("NVDA")
    news = _google_news_items('"NVDA" stock when:2d', limit=3)
    return {
        "nasdaq_premarket_ok": bool(pm.get("ok") and math.isfinite(pm.get("premarket_volume", math.nan))),
        "nasdaq_premarket_volume": pm.get("premarket_volume"),
        "nasdaq_quote_ok": bool(math.isfinite(bid) and math.isfinite(ask) and math.isfinite(spread)),
        "google_news_ok": bool(news),
    }
