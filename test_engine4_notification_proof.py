from __future__ import annotations

import json

import engine4_notify as notify


def _configure(monkeypatch, tmp_path):
    monkeypatch.setattr(notify, "OUT", tmp_path)
    monkeypatch.setenv("GITHUB_TOKEN", "test-token")
    monkeypatch.setenv("GITHUB_REPOSITORY", "owner/repo")


def test_sms_dedup_requires_and_preserves_two_recipient_proof(tmp_path, monkeypatch):
    _configure(monkeypatch, tmp_path)
    signal = notify._signal_for("start", None)
    date_et = str(signal.get("target_date_et") or notify.datetime.now(notify.ET).date())
    monkeypatch.setenv("GITHUB_RUN_ID", "123456789")
    marker = f"ENGINE4-ALERT:{date_et}:start:STARTED:SYSTEM:RUN:123456789"
    (tmp_path / "notification_audit_log.json").write_text(
        json.dumps(
            [
                {
                    "marker": marker,
                    "sms": {
                        "delivery": "API_ACCEPTED",
                        "recipient_count": 2,
                        "messages": [],
                    },
                    "github": {
                        "delivery": "DISABLED",
                        "reason": "sms_only_user_preference",
                    },
                }
            ]
        ),
        encoding="utf-8",
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
        "proof": "existing_local_notification_audit",
    }
    assert result["github"] == {
        "delivery": "DISABLED",
        "reason": "sms_only_user_preference",
    }


def test_local_audit_without_accepted_sms_resends_sms(tmp_path, monkeypatch):
    _configure(monkeypatch, tmp_path)
    signal = notify._signal_for("start", None)
    date_et = str(signal.get("target_date_et") or notify.datetime.now(notify.ET).date())
    monkeypatch.setenv("GITHUB_RUN_ID", "987654321")
    marker = f"ENGINE4-ALERT:{date_et}:start:STARTED:SYSTEM:RUN:987654321"
    (tmp_path / "notification_audit_log.json").write_text(
        json.dumps(
            [
                {
                    "marker": marker,
                    "sms": {"delivery": "FAILED", "recipient_count": 0},
                }
            ]
        ),
        encoding="utf-8",
    )
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
