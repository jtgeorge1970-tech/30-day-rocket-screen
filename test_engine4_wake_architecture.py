from pathlib import Path

import engine4_notify


ROOT = Path(__file__).parent


def test_wake_notification_kinds_are_distinct(tmp_path, monkeypatch):
    monkeypatch.setattr(engine4_notify, "OUT", tmp_path)
    kinds = ("preflight", "launch", "watchdog", "start")
    markers = {engine4_notify.notify(kind, dry_run=True)["marker"] for kind in kinds}
    assert len(markers) == len(kinds)
    assert engine4_notify._signal_for("preflight", None)["status"] == "CHECKING"
    assert engine4_notify._signal_for("launch", None)["status"] == "DISPATCHED"
    assert engine4_notify._signal_for("watchdog", None)["status"] == "RECOVERY_DISPATCHED"


def test_early_controller_has_seasonal_guard_and_dispatch_proof():
    workflow = (ROOT / ".github/workflows/engine4-early-wake.yml").read_text()
    assert "cron: '20 12 * * 1-5'" in workflow
    assert "cron: '20 13 * * 1-5'" in workflow
    assert 'if [ "$T" -lt 495 ] || [ "$T" -gt 510 ]' in workflow
    assert "wait_until" not in workflow or "08:35 ET launch checkpoint" in workflow
    assert "engine4_notify.py preflight --require-delivery" in workflow
    assert "engine4_notify.py launch --require-delivery" in workflow


def test_primary_wake_retries_and_recognizes_manual_failsafe():
    workflow = (ROOT / ".github/workflows/engine4-production.yml").read_text()
    assert "cron: '35,40,45,50 12 * * 1-5'" in workflow
    assert "cron: '35,40,45,50 13 * * 1-5'" in workflow
    assert "engine4-manual-on-demand.yml" in workflow
    assert "is_morning_manual" in workflow


def test_watchdog_has_seasonal_guard_and_intervention_sms():
    workflow = (ROOT / ".github/workflows/engine4-watchdog.yml").read_text()
    assert 'if [ "$T" -lt 522 ] || [ "$T" -gt 535 ]' in workflow
    assert "engine4_notify.py watchdog --require-delivery" in workflow
    assert "engine4-manual-on-demand.yml" in workflow
    assert "is_morning_manual" in workflow
    assert "steps.wake.outputs.dispatched == 'true'" in workflow


def test_early_manual_failsafe_preserves_live_stage_times():
    workflow = (ROOT / ".github/workflows/engine4-manual-on-demand.yml").read_text()
    assert "08:50-15:30 ET" in workflow
    for minute in (535, 545, 558, 585):
        assert f"wait_until_et {minute}" in workflow


def test_primary_result_sms_cannot_claim_full_completion():
    text = engine4_notify._sms_text(
        "final", "NO_TRADE", "MARKET", "No primary trade.", "https://example.test/run"
    )
    assert "PRIMARY RESULT — RUN STILL ACTIVE" in text
    assert "full Engine 4 run is NOT complete" in text
    assert "ENGINE 4 FINAL" not in text

    completed = engine4_notify._sms_text(
        "complete", "COMPLETE", "SYSTEM", "All stages finished.", ""
    )
    assert completed.startswith("ENGINE 4 COMPLETE:")
