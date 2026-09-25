from __future__ import annotations

"""Engine 4 feeder context.

This module is intentionally strategy-free.  It selects which evidence source may
feed the locked Engine 4 logic.  LIVE preserves the existing provider behavior.
REPLAY is fail-closed: code must explicitly install historical point-in-time
providers before any quote/news/premarket lookup is allowed.
"""

from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import Callable, Optional


class FeedMode(str, Enum):
    LIVE = "live"
    REPLAY = "replay"


class ReplayDataUnavailable(RuntimeError):
    pass


@dataclass(frozen=True)
class FeedContext:
    mode: FeedMode = FeedMode.LIVE
    market_date_et: Optional[date] = None
    asof_et: Optional[datetime] = None
    label: str = "LIVE"


_context = FeedContext()
_replay_catalyst: Optional[Callable] = None
_replay_quote: Optional[Callable] = None
_replay_premarket: Optional[Callable] = None


def current() -> FeedContext:
    return _context


def configure_live() -> None:
    global _context, _replay_catalyst, _replay_quote, _replay_premarket
    _context = FeedContext()
    _replay_catalyst = None
    _replay_quote = None
    _replay_premarket = None


def configure_replay(market_date_et: date, asof_et: datetime) -> None:
    global _context
    if asof_et.date() != market_date_et:
        raise ValueError("Replay as-of timestamp must match replay market date")
    _context = FeedContext(
        mode=FeedMode.REPLAY,
        market_date_et=market_date_et,
        asof_et=asof_et,
        label=f"REPLAY — {market_date_et.isoformat()}",
    )


def install_replay_sources(*, catalyst=None, quote=None, premarket=None) -> None:
    global _replay_catalyst, _replay_quote, _replay_premarket
    _replay_catalyst = catalyst
    _replay_quote = quote
    _replay_premarket = premarket


def require_replay_source(kind: str) -> Callable:
    if _context.mode is not FeedMode.REPLAY:
        raise RuntimeError("Replay source requested while feeder is LIVE")
    source = {
        "catalyst": _replay_catalyst,
        "quote": _replay_quote,
        "premarket": _replay_premarket,
    }.get(kind)
    if source is None:
        raise ReplayDataUnavailable(
            f"{_context.label}: point-in-time {kind} source unavailable; "
            "live fallback is forbidden"
        )
    return source


def catalyst(ticker: str, reference_time, company_name=None):
    return require_replay_source("catalyst")(ticker, reference_time, company_name)


def quote(ticker: str):
    return require_replay_source("quote")(ticker, _context.asof_et)


def premarket_many(tickers):
    return require_replay_source("premarket")(tickers, _context.asof_et)
