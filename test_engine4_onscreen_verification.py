from __future__ import annotations

import json
import pytest
import engine4_notify as notify
import engine4_stage_report as report


def _record(tmp_path, monkeypatch):
    monkeypatch.setattr(notify, "OUT", tmp_path)
    monkeypatch.setattr(report, "OUT", tmp_path)
    monkeypatch.setenv("GITHUB_RUN_ID", "123456789")
    for key in ("OPENPHONE_API_KEY", "OPENPHONE_FROM_NUMBER", "ENGINE4_SMS_TO"):
        monkeypatch.delenv(key, raising=False)
    return notify.notify("start")


def test_zero_recipient_contract_accepts_actual_saved_onscreen_record(tmp_path, monkeypatch):
    record = _record(tmp_path, monkeypatch)
    report.verify_notification(record["target_date_et"], "start", 0)


def test_zero_recipient_contract_rejects_another_runs_record(tmp_path, monkeypatch):
    record = _record(tmp_path, monkeypatch)
    monkeypatch.setenv("GITHUB_RUN_ID", "987654321")
    with pytest.raises(RuntimeError, match="another run"):
        report.verify_notification(record["target_date_et"], "start", 0)


def test_zero_recipient_contract_rejects_mismatched_artifact_date(tmp_path, monkeypatch):
    record = _record(tmp_path, monkeypatch)
    history = json.loads((tmp_path / "notification_audit_log.json").read_text())
    history[-1]["target_date_et"] = "2000-01-01"
    (tmp_path / "notification_audit_log.json").write_text(json.dumps(history))
    with pytest.raises(RuntimeError, match="DATE FAILURE"):
        report.verify_notification(record["target_date_et"], "start", 0)


def test_zero_recipient_contract_rejects_missing_completion_proof(tmp_path, monkeypatch):
    record = _record(tmp_path, monkeypatch)
    with pytest.raises(RuntimeError, match="no audit entry for complete"):
        report.verify_notification(record["target_date_et"], "complete", 0)
