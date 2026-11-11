from datetime import date, datetime
from zoneinfo import ZoneInfo

import pytest

import engine4_feed as feed
from engine4_replay import replay_manifest

ET = ZoneInfo("America/New_York")


def setup_function():
    feed.configure_live()


def test_live_is_default_and_preserved():
    ctx = feed.current()
    assert ctx.mode is feed.FeedMode.LIVE
    assert ctx.label == "LIVE"


def test_replay_never_falls_back_to_live_sources():
    d = date(2026, 9, 16)
    feed.configure_replay(d, datetime(2026, 9, 16, 9, 18, tzinfo=ET))
    for kind in ("catalyst", "quote", "premarket"):
        with pytest.raises(feed.ReplayDataUnavailable):
            feed.require_replay_source(kind)


def test_replay_source_must_be_explicitly_installed():
    d = date(2026, 9, 16)
    feed.configure_replay(d, datetime(2026, 9, 16, 9, 45, tzinfo=ET))
    feed.install_replay_sources(quote=lambda ticker, asof: (10.0, 10.01, 0.1))
    assert feed.quote("TEST") == (10.0, 10.01, 0.1)
    with pytest.raises(feed.ReplayDataUnavailable):
        feed.require_replay_source("catalyst")


def test_manifest_is_production_isolated():
    manifest = replay_manifest("2026-09-16")
    assert manifest["mode"] == "INSTANT_REPLAY"
    assert manifest["production_state_writes"] is False
    assert manifest["production_sms"] is False
    assert manifest["live_provider_fallback"] is False
    assert [x["stage"] for x in manifest["stages"]] == [
        "PRE-SCREEN",
        "DEEP 100-POINT ANALYSIS",
        "REFRESH + TOP-25 FREEZE",
        "FINAL CONFIRMATION",
    ]
