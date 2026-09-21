from __future__ import annotations

import engine4_notify as notify


class _Response:
    def __init__(self, payload):
        self._payload = payload

    def json(self):
        return self._payload


def _configure(monkeypatch, tmp_path, issue_body: str):
    monkeypatch.setattr(notify, "OUT", tmp_path)
    monkeypatch.setenv("GITHUB_TOKEN", "test-token")
    monkeypatch.setenv("GITHUB_REPOSITORY", "owner/repo")
    monkeypatch.setattr(
        notify,
        "_github_request",
        lambda method, url, token, **kwargs: _Response(
            [
                {
                    "number": 7,
                    "html_url": "https://example.test/issues/7",
                    "body": issue_body,
                }
            ]
        ),
    )


def test_sms_dedup_requires_and_preserves_two_recipient_proof(tmp_path, monkeypatch):
    signal = notify._signal_for("start", None)
    date_et = str(signal.get("target_date_et") or notify.datetime.now(notify.ET).date())
    monkeypatch.setenv("GITHUB_RUN_ID", "123456789")
    marker = f"<!-- ENGINE4-ALERT:{date_et}:start:STARTED:SYSTEM:RUN:123456789 -->"
    _configure(
        monkeypatch,
        tmp_path,
        f"{marker}\n<!-- ENGINE4-SMS-API-ACCEPTED recipients=2 -->",
    )
    monkeypatch.setattr(
        notify,
        "_send_openphone_sms",
        lambda content: (_ for _ in ()).throw(AssertionError("SMS must be deduplicated")),
    )

    result = notify.notify("start")

    assert result["delivery"] == "SENT"
    assert result["sms"] == {
        "delivery": "DEDUPLICATED",
        "recipient_count": 2,
        "proof": "existing_GitHub_issue_SMS_acceptance_marker",
    }


def test_legacy_marker_without_recipient_count_resends_sms(tmp_path, monkeypatch):
    signal = notify._signal_for("start", None)
    date_et = str(signal.get("target_date_et") or notify.datetime.now(notify.ET).date())
    monkeypatch.setenv("GITHUB_RUN_ID", "987654321")
    marker = f"<!-- ENGINE4-ALERT:{date_et}:start:STARTED:SYSTEM:RUN:987654321 -->"
    _configure(monkeypatch, tmp_path, f"{marker}\n<!-- ENGINE4-SMS-API-ACCEPTED -->")
    calls = []
    monkeypatch.setattr(
        notify,
        "_send_openphone_sms",
        lambda content: calls.append(content)
        or {"delivery": "API_ACCEPTED", "recipient_count": 2, "messages": []},
    )

    result = notify.notify("start")

    assert len(calls) == 1
    assert result["sms"]["delivery"] == "API_ACCEPTED"
    assert result["sms"]["recipient_count"] == 2
