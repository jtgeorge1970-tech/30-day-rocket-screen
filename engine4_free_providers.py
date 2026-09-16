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


def cboe_delayed_quote_spread(ticker: str) -> Tuple[float, float, float]:
    """Independent queue-preservation quote; never treated as order-authoritative.

    Cboe labels this public feed as delayed. It is useful for retaining and ranking
    an alternate when both real-time retrieval paths fail, but callers must not use
    it to authorize an official BUY/ARM instruction.
    """
    ticker = ticker.upper()
    url = f"https://cdn.cboe.com/api/global/delayed_quotes/quotes/{ticker}.json"
    try:
        r = requests.get(
            url,
            headers={"User-Agent": NASDAQ_HEADERS["User-Agent"], "Accept-Language": "en-US,en;q=0.9"},
            timeout=10,
        )
        if r.status_code != 200:
            return math.nan, math.nan, math.nan
        data = (r.json() or {}).get("data") or {}
        if str(data.get("symbol") or "").upper() != ticker:
            return math.nan, math.nan, math.nan
        bid = _num(data.get("bid"))
        ask = _num(data.get("ask"))
        if not (math.isfinite(bid) and math.isfinite(ask) and bid > 0 and ask >= bid):
            return bid, ask, math.nan
        mid = (bid + ask) / 2.0
        return bid, ask, (ask - bid) / mid * 100.0
    except Exception:
        return math.nan, math.nan, math.nan


def _rss_news_items(url: str, limit: int = 12) -> list[tuple[str, datetime | None]]:
    try:
        # Do not reuse the Nasdaq session here: its Nasdaq Origin/Referer headers can
        # cause independent RSS providers to reject an otherwise valid request.
        r = requests.get(
            url,
            headers={"User-Agent": NASDAQ_HEADERS["User-Agent"], "Accept-Language": "en-US,en;q=0.9"},
            timeout=5,
        )
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


def _google_news_items(query: str, limit: int = 12) -> list[tuple[str, datetime | None]]:
    q = quote_plus(query)
    url = f"https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"
    return _rss_news_items(url, limit)


def _bing_news_items(query: str, limit: int = 12) -> list[tuple[str, datetime | None]]:
    q = quote_plus(query)
    url = f"https://www.bing.com/news/search?q={q}&format=rss&setlang=en-US"
    return _rss_news_items(url, limit)


def _nasdaq_company_news_items(ticker: str, limit: int = 12) -> list[tuple[str, datetime | None]]:
    """Return Nasdaq-tagged company news with structured ticker evidence.

    Nasdaq supplies ``primarysymbol`` and ``related_symbols`` fields. We still pass
    each result through the same company-name identity check used for RSS results;
    the exact structured symbol is appended to the evidence text so a similarly
    named issuer cannot satisfy the ticker requirement by accident.
    """
    ticker = ticker.upper()
    url = (
        "https://api.nasdaq.com/api/news/topic/articlebysymbol"
        f"?q={quote_plus(ticker + '|stocks')}&limit={limit}&offset=0"
    )
    payload = _get_json(url, attempts=2, timeout=6.0)
    if not payload:
        return []

    rows = ((payload.get("data") or {}).get("rows") or [])[:limit]
    out = []
    for row in rows:
        primary = str(row.get("primarysymbol") or "").upper()
        related = {
            str(value).split("|", 1)[0].upper()
            for value in (row.get("related_symbols") or [])
        }
        if ticker != primary and ticker not in related:
            continue
        title = str(row.get("title") or "").strip()
        description = str(row.get("description") or "").strip()
        if not title:
            continue
        # The appended exact structured ticker is evidence from Nasdaq's response,
        # not an inferred keyword. Company identity must still appear in title/body.
        evidence = f"{title} ({ticker}) {description}".strip()
        ts = None
        raw = str(row.get("created") or "").strip()
        if raw:
            try:
                ts = datetime.strptime(raw, "%b %d, %Y").replace(
                    hour=12, tzinfo=timezone.utc
                )
            except ValueError:
                ts = None
        out.append((evidence, ts))
    return out


_COMPANY_SUFFIXES = {
    "adr", "ads", "class", "common", "company", "co", "corp", "corporation",
    "inc", "incorporated", "limited", "ltd", "lp", "llc", "ordinary", "plc",
    "shares", "stock",
}

_GENERIC_IDENTITY_WORDS = {
    "global", "group", "holding", "holdings", "international", "industries",
    "pharmaceutical", "pharmaceuticals", "solutions", "systems", "technology",
    "technologies", "therapeutics",
}


def _normalized_words(value: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", value.lower())


def _headline_matches_company(text: str, ticker: str, company_name: str | None) -> bool:
    """Fail-closed entity check for a catalyst headline.

    Google News search results are only discovery candidates. They are not evidence
    that a headline belongs to the requested security. A catalyst can score only
    when the headline body (excluding the publisher suffix) contains both the exact
    ticker token and an independent company-name identity token. For companies whose
    legal name is itself the ticker (for example NIO Inc.), the exact ticker/company
    token is sufficient.
    """
    if not company_name:
        return False

    # Google News RSS titles conventionally end in " - Publisher". Do not allow a
    # publisher name to satisfy the company identity test.
    headline = text.rsplit(" - ", 1)[0]
    ticker_pattern = rf"(?<![A-Za-z0-9]){re.escape(ticker)}(?![A-Za-z0-9])"
    if not re.search(ticker_pattern, headline, flags=re.I):
        return False

    ticker_key = "".join(_normalized_words(ticker))
    company_words = [
        word for word in _normalized_words(company_name)
        if word not in _COMPANY_SUFFIXES
    ]
    if not company_words:
        return False

    headline_words = set(_normalized_words(headline))
    independent_terms = [
        word for word in company_words
        if len(word) >= 4
        and word not in _GENERIC_IDENTITY_WORDS
        and word != ticker_key
    ]
    if independent_terms:
        return any(word in headline_words for word in independent_terms)

    # A small number of issuers use their ticker as their company name. This is the
    # only allowed case without a second identity token.
    company_key = "".join(company_words)
    return company_key == ticker_key


def _score_news_items(
    items: list[tuple[str, datetime | None]],
    ticker: str,
    reference_time: datetime,
    catalyst_rules,
    negative_pattern,
    promotional_pattern,
    company_name: str | None = None,
) -> Tuple[float, str, float]:
    ticker = ticker.upper()
    if not company_name:
        # No identity evidence means no catalyst. Never fall back to ticker-only
        # matching because globally ambiguous symbols can name unrelated companies.
        return 0.0, "", math.inf
    if not items:
        return 0.0, "", math.inf

    ref_utc = reference_time.astimezone(timezone.utc)
    best = (0.0, "", math.inf)
    for text, timestamp in items:
        if not _headline_matches_company(text, ticker, company_name):
            continue
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


def _company_news_query(ticker: str, company_name: str) -> str:
    cleaned = re.sub(
        r"\b(Common Stock|Class [A-Z]|Inc\.?|Corporation|Corp\.?|Ltd\.?|PLC|Holdings?)\b",
        "",
        company_name,
        flags=re.I,
    )
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    company_term = f' OR "{cleaned}"' if cleaned else ""
    return f'("{ticker.upper()}" stock{company_term})'


def google_news_catalyst(
    ticker: str,
    reference_time: datetime,
    catalyst_rules,
    negative_pattern,
    promotional_pattern,
    company_name: str | None = None,
) -> Tuple[float, str, float]:
    if not company_name:
        return 0.0, "", math.inf
    query = _company_news_query(ticker, company_name) + " when:2d"
    return _score_news_items(
        _google_news_items(query, limit=15),
        ticker,
        reference_time,
        catalyst_rules,
        negative_pattern,
        promotional_pattern,
        company_name,
    )


def verified_news_catalyst(
    ticker: str,
    reference_time: datetime,
    catalyst_rules,
    negative_pattern,
    promotional_pattern,
    company_name: str | None = None,
) -> tuple[float, str, float, str]:
    """Use independent providers in order without weakening identity validation."""
    if not company_name:
        return 0.0, "", math.inf, "UNAVAILABLE"

    query = _company_news_query(ticker, company_name)
    providers = (
        ("Google News RSS", lambda: _google_news_items(query + " when:2d", limit=15)),
        ("Bing News RSS", lambda: _bing_news_items(query, limit=15)),
        ("Nasdaq company news", lambda: _nasdaq_company_news_items(ticker, limit=15)),
    )
    for source, loader in providers:
        try:
            items = loader()
        except Exception:
            items = []
        score, headline, age = _score_news_items(
            items,
            ticker,
            reference_time,
            catalyst_rules,
            negative_pattern,
            promotional_pattern,
            company_name,
        )
        if score > 0:
            return score, headline, age, source
    return 0.0, "", math.inf, "NO_VERIFIED_CATALYST"


def provider_smoke() -> dict:
    pm = nasdaq_premarket_snapshot("NVDA", attempts=2, timeout=6.0)
    bid, ask, spread = nasdaq_quote_spread("NVDA")
    cboe_bid, cboe_ask, cboe_spread = cboe_delayed_quote_spread("NVDA")
    google_news = _google_news_items('"NVDA" stock when:2d', limit=3)
    bing_news = _bing_news_items('"NVDA" stock', limit=3)
    nasdaq_news = _nasdaq_company_news_items("NVDA", limit=3)
    news_provider_count = sum(bool(items) for items in (google_news, bing_news, nasdaq_news))
    return {
        "nasdaq_premarket_ok": bool(pm.get("ok") and math.isfinite(pm.get("premarket_volume", math.nan))),
        "nasdaq_premarket_volume": pm.get("premarket_volume"),
        "nasdaq_quote_ok": bool(math.isfinite(bid) and math.isfinite(ask) and math.isfinite(spread)),
        "cboe_delayed_quote_ok": bool(
            math.isfinite(cboe_bid) and math.isfinite(cboe_ask) and math.isfinite(cboe_spread)
        ),
        "google_news_ok": bool(google_news),
        "bing_news_ok": bool(bing_news),
        "nasdaq_news_ok": bool(nasdaq_news),
        "news_provider_count": news_provider_count,
        "news_provider_ok": news_provider_count > 0,
    }
