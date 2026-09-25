from __future__ import annotations

import json
import engine4_notify as notify


def _configure(monkeypatch, tmp_path):
    monkeypatch.setattr(notify, "OUT", tmp_path)


def test_saved_onscreen_notification_is_persisted_and_audited(tmp_path, monkeypatch):
    _configure(monkeypatch, tmp_path)
    monkeypatch.setenv("GITHUB_RUN_ID", "123456789")
    result = notify.notify("start")
    assert result["delivery"] == "SAVED_ONSCREEN"
    assert result["run_id"] == "123456789"
    assert (tmp_path / "notification_start.txt").exists()
    assert (tmp_path / "notification_start.json").exists()
    history = json.loads((tmp_path / "notification_audit_log.json").read_text(encoding="utf-8"))
    assert history[-1]["marker"] == result["marker"]
    assert history[-1]["notification_text"] == result["notification_text"]


def test_saved_onscreen_notification_does_not_require_sms_credentials(tmp_path, monkeypatch):
    _configure(monkeypatch, tmp_path)
    monkeypatch.delenv("OPENPHONE_API_KEY", raising=False)
    monkeypatch.delenv("OPENPHONE_FROM_NUMBER", raising=False)
    monkeypatch.delenv("ENGINE4_SMS_TO", raising=False)
    result = notify.notify("start")
    assert result["delivery"] == "SAVED_ONSCREEN"
    assert "ENGINE 4 START: STARTED" in result["notification_text"]
