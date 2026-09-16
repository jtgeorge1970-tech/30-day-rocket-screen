import math
import re
from datetime import datetime, timezone

import engine4_free_providers as providers


REFERENCE = datetime(2026, 9, 16, 14, 0, tzinfo=timezone.utc)
CATALYST_RULES = [(1.0, re.compile(r"earnings beat|acquisition|approval", re.I))]
NEVER = re.compile(r"(?!)")


def _score(monkeypatch, ticker, company_name, headline):
    monkeypatch.setattr(
        providers,
        "_google_news_items",
        lambda query, limit=15: [(headline, REFERENCE)],
    )
    return providers.google_news_catalyst(
        ticker,
        REFERENCE,
        CATALYST_RULES,
        NEVER,
        NEVER,
        company_name=company_name,
    )


def test_rejects_stx_headline_for_wrong_company(monkeypatch):
    result = _score(
        monkeypatch,
        "STX",
        "Seagate Technology Holdings PLC",
        "South Korean Court Approves STX Rehabilitation Plan, Confirming Acquisition - Example News",
    )
    assert result == (0.0, "", math.inf)


def test_accepts_headline_with_ticker_and_verified_company_identity(monkeypatch):
    score, headline, age = _score(
        monkeypatch,
        "FPS",
        "Forgent Power Solutions Inc.",
        "Forgent Power Solutions (NYSE:FPS) Shares Gap Up Following Earnings Beat - MarketBeat",
    )
    assert score == 1.0
    assert headline.startswith("Forgent Power Solutions")
    assert age == 0.0


def test_rejects_company_name_without_exact_ticker(monkeypatch):
    result = _score(
        monkeypatch,
        "STX",
        "Seagate Technology Holdings PLC",
        "Seagate Technology Announces Acquisition - Example News",
    )
    assert result == (0.0, "", math.inf)


def test_missing_company_name_fails_closed(monkeypatch):
    result = _score(
        monkeypatch,
        "STX",
        None,
        "STX Stock Announces Acquisition - Example News",
    )
    assert result == (0.0, "", math.inf)
