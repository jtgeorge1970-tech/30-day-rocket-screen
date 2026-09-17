import json
import math
import re
from datetime import datetime, timezone

import engine4_free_providers as providers
import engine4_notify as notifier
import engine4_pipeline_runner as runner


REFERENCE = datetime(2026, 9, 16, 14, 0, tzinfo=timezone.utc)
RULES = [(1.0, re.compile(r"acquisition|earnings beat", re.I))]
NEVER = re.compile(r"(?!)")


def test_news_chain_uses_bing_when_google_is_down(monkeypatch):
    monkeypatch.setattr(providers, "_google_news_items", lambda *args, **kwargs: [])
    monkeypatch.setattr(
        providers,
        "_bing_news_items",
        lambda *args, **kwargs: [
            (
                "Seagate Technology (NASDAQ:STX) Announces Acquisition - Example",
                REFERENCE,
            )
        ],
    )
    monkeypatch.setattr(
        providers,
        "_nasdaq_company_news_items",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("not needed")),
    )
    score, headline, age, source = providers.verified_news_catalyst(
        "STX",
        REFERENCE,
        RULES,
        NEVER,
        NEVER,
        company_name="Seagate Technology Holdings PLC",
    )
    assert score == 1.0
    assert headline.startswith("Seagate Technology")
    assert age == 0.0
    assert source == "Bing News RSS"


def test_all_news_sources_down_fails_catalyst_only(monkeypatch):
    monkeypatch.setattr(providers, "_google_news_items", lambda *args, **kwargs: [])
    monkeypatch.setattr(providers, "_bing_news_items", lambda *args, **kwargs: [])
    monkeypatch.setattr(providers, "_nasdaq_company_news_items", lambda *args, **kwargs: [])
    result = providers.verified_news_catalyst(
        "STX",
        REFERENCE,
        RULES,
        NEVER,
        NEVER,
        company_name="Seagate Technology Holdings PLC",
    )
    assert result == (0.0, "", math.inf, "NO_VERIFIED_CATALYST")


def test_quote_chain_uses_yahoo_when_nasdaq_is_down(monkeypatch):
    monkeypatch.setattr(runner, "nasdaq_quote_spread", lambda ticker: (math.nan,) * 3)
    monkeypatch.setattr(runner, "yahoo_quote_spread", lambda ticker: (34.10, 34.14, 0.1172))
    bid, ask, spread, source = runner.quote_spread_with_source("FPS")
    assert (bid, ask, spread) == (34.10, 34.14, 0.1172)
    assert source == "Yahoo quote fallback"


def test_third_quote_path_preserves_queue_but_is_not_order_authoritative(monkeypatch):
    monkeypatch.setattr(runner, "nasdaq_quote_spread", lambda ticker: (math.nan,) * 3)
    monkeypatch.setattr(runner, "yahoo_quote_spread", lambda ticker: (math.nan,) * 3)
    monkeypatch.setattr(
        runner, "cboe_delayed_quote_spread", lambda ticker: (34.08, 34.16, 0.2345)
    )
    bid, ask, spread, source = runner.quote_spread_with_source("FPS")
    assert (bid, ask, spread) == (34.08, 34.16, 0.2345)
    assert source == "Cboe delayed quote fallback"
    assert all(math.isnan(value) for value in runner.resilient_quote_spread("FPS"))


def test_health_report_can_be_degraded_without_terminating_pipeline(monkeypatch):
    monkeypatch.setattr(
        runner,
        "provider_smoke",
        lambda: {
            "nasdaq_premarket_ok": False,
            "nasdaq_quote_ok": False,
            "news_provider_ok": False,
        },
    )
    health = runner.assert_provider_health()
    assert health["news_provider_ok"] is False


def test_notification_dry_run_contains_committed_instruction(tmp_path, monkeypatch):
    monkeypatch.setattr(notifier, "OUT", tmp_path)
    (tmp_path / "recovery_signal.json").write_text(
        json.dumps(
            {
                "status": "ARM",
                "ticker": "FPS",
                "target_date_et": "2026-09-16",
                "message": "PLACE RECOVERY BUY STOP-LIMIT NOW — FPS",
            }
        ),
        encoding="utf-8",
    )
    result = notifier.notify("recovery", dry_run=True)
    assert result["delivery"] == "DRY_RUN"
    assert "PLACE RECOVERY BUY STOP-LIMIT NOW" in result["body"]
    assert "PLACE RECOVERY BUY STOP-LIMIT NOW" in result["sms_text"]
    assert "ENGINE4-ALERT:2026-09-16:recovery:ARM:FPS" in result["marker"]


def test_openphone_sms_uses_official_api_and_e164_numbers(monkeypatch):
    monkeypatch.setenv("OPENPHONE_API_KEY", "secret-test-key")
    monkeypatch.setenv("OPENPHONE_FROM_NUMBER", "+15551234567")
    monkeypatch.setenv("ENGINE4_SMS_TO", "+15557654321")

    class Response:
        status_code = 202

        @staticmethod
        def raise_for_status():
            return None

        @staticmethod
        def json():
            return {"data": {"id": "AC123"}}

    captured = {}

    def fake_post(url, **kwargs):
        captured["url"] = url
        captured.update(kwargs)
        return Response()

    monkeypatch.setattr(notifier.requests, "post", fake_post)
    result = notifier._send_openphone_sms("Engine 4 test")
    assert result == {
        "delivery": "API_ACCEPTED",
        "recipient_count": 1,
        "messages": [{"http_status": 202, "message_id": "AC123"}],
    }
    assert captured["url"] == "https://api.quo.com/v1/messages"
    assert captured["headers"]["Authorization"] == "secret-test-key"
    assert captured["json"] == {
        "content": "Engine 4 test",
        "from": "+15551234567",
        "to": ["+15557654321"],
    }


def test_openphone_sms_rejects_non_e164_number(monkeypatch):
    monkeypatch.setenv("OPENPHONE_API_KEY", "secret-test-key")
    monkeypatch.setenv("OPENPHONE_FROM_NUMBER", "555-123-4567")
    monkeypatch.setenv("ENGINE4_SMS_TO", "+15557654321")
    result = notifier._send_openphone_sms("Engine 4 test")
    assert result["delivery"] == "FAILED"
    assert "E.164" in result["reason"]


def test_openphone_sms_sends_separate_message_to_each_recipient(monkeypatch):
    monkeypatch.setenv("OPENPHONE_API_KEY", "secret-test-key")
    monkeypatch.setenv("OPENPHONE_FROM_NUMBER", "+15551234567")
    monkeypatch.setenv("ENGINE4_SMS_TO", "+15557654321,+15559876543")

    class Response:
        status_code = 202

        @staticmethod
        def raise_for_status():
            return None

        @staticmethod
        def json():
            return {"data": {"id": "AC123"}}

    payloads = []

    def fake_post(url, **kwargs):
        payloads.append(kwargs["json"])
        return Response()

    monkeypatch.setattr(notifier.requests, "post", fake_post)
    result = notifier._send_openphone_sms("Engine 4 test")
    assert result["recipient_count"] == 2
    assert [payload["to"] for payload in payloads] == [
        ["+15557654321"],
        ["+15559876543"],
    ]
