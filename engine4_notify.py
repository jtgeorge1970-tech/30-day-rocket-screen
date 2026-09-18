from __future__ import annotations

"""Immediate, deduplicated Engine 4 notifications by SMS and GitHub Issues.

OpenPhone/Quo delivers the primary real-SMS alert. GitHub Issues remains the
independent audit trail and fallback notification channel. Credentials and
phone numbers are read only from encrypted GitHub Actions secrets.
"""

import argparse
import json
import os
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests


OUT = Path("output/engine4")
ET = ZoneInfo("America/New_York")
API = "https://api.github.com"
OPENPHONE_API = "https://api.quo.com/v1/messages"
E164 = re.compile(r"^\+[1-9]\d{7,14}$")
SMS_ACCEPTED_MARKER = "<!-- ENGINE4-SMS-API-ACCEPTED -->"


def _read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _write_audit(payload: dict) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "notification_audit.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )


def _signal_for(kind: str, failure_message: str | None) -> dict:
    if kind == "final":
        return _read_json(OUT / "final_signal.json")
    if kind == "recovery":
        return _read_json(OUT / "recovery_signal.json")
    if kind == "test":
        return {
            "status": "TEST",
            "ticker": "SYSTEM",
            "message": failure_message or "Engine 4 test text delivered successfully.",
        }
    if kind == "preflight":
        return {
            "status": "CHECKING",
            "ticker": "SYSTEM",
            "message": failure_message or "Engine 4 early preflight is active.",
        }
    if kind == "launch":
        return {
            "status": "DISPATCHED",
            "ticker": "SYSTEM",
            "message": failure_message or "Engine 4 early controller dispatched production.",
        }
    if kind == "watchdog":
        return {
            "status": "RECOVERY_DISPATCHED",
            "ticker": "SYSTEM",
            "message": failure_message or "Engine 4 watchdog dispatched a recovery wake.",
        }
    if kind == "start":
        return {
            "status": "STARTED",
            "ticker": "SYSTEM",
            "message": failure_message or "Engine 4 scheduled run started.",
        }
    if kind == "complete":
        return {
            "status": "COMPLETE",
            "ticker": "SYSTEM",
            "message": failure_message or "Engine 4 scheduled run completed.",
        }
    return {
        "status": "PIPELINE_FAILURE",
        "reason": "workflow_stage_failed",
        "message": failure_message or "ENGINE 4 DATA/PIPELINE FAILURE",
    }


def _github_request(method: str, url: str, token: str, **kwargs) -> requests.Response:
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    response = requests.request(method, url, headers=headers, timeout=15, **kwargs)
    response.raise_for_status()
    return response


def _sms_text(kind: str, status: str, ticker: str, message: str, run_url: str) -> str:
    heading = f"ENGINE 4 {kind.upper()}: {status} — {ticker}"
    safety = "Confirm the live broker quote before any order."
    return "\n".join(part for part in (heading, message, safety, run_url) if part)[:1200]


def _send_openphone_sms(content: str) -> dict:
    api_key = os.getenv("OPENPHONE_API_KEY", "").strip()
    from_number = os.getenv("OPENPHONE_FROM_NUMBER", "").strip()
    to_numbers = [
        number.strip()
        for number in os.getenv("ENGINE4_SMS_TO", "").split(",")
        if number.strip()
    ]
    if not api_key or not from_number or not to_numbers:
        return {
            "delivery": "NOT_CONFIGURED",
            "reason": "missing_openphone_api_key_from_number_or_sms_recipient",
        }
    if not E164.fullmatch(from_number) or any(
        not E164.fullmatch(number) for number in to_numbers
    ):
        return {
            "delivery": "FAILED",
            "reason": "phone_numbers_must_use_E.164_format_like_+15551234567",
        }

    try:
        deliveries = []
        for to_number in to_numbers:
            response = requests.post(
                OPENPHONE_API,
                headers={
                    "Authorization": api_key,
                    "Content-Type": "application/json",
                },
                json={"content": content, "from": from_number, "to": [to_number]},
                timeout=20,
            )
            response.raise_for_status()
            try:
                payload = response.json()
            except ValueError:
                payload = {}
            data = payload.get("data") if isinstance(payload, dict) else {}
            deliveries.append(
                {
                    "http_status": response.status_code,
                    "message_id": (data or {}).get("id")
                    if isinstance(data, dict)
                    else None,
                }
            )
        return {
            "delivery": "API_ACCEPTED",
            "recipient_count": len(deliveries),
            "messages": deliveries,
        }
    except Exception as exc:
        return {"delivery": "FAILED", "reason": f"{type(exc).__name__}: {exc}"}


def notify(kind: str, failure_message: str | None = None, dry_run: bool = False) -> dict:
    signal = _signal_for(kind, failure_message)
    status = str(signal.get("status") or "UNKNOWN").upper()
    ticker = str(signal.get("ticker") or "MARKET").upper()
    date_et = str(signal.get("target_date_et") or datetime.now(ET).date())
    marker = f"ENGINE4-ALERT:{date_et}:{kind}:{status}:{ticker}"
    title = f"[ENGINE 4] {kind.upper()} {status} — {ticker} — {date_et}"
    message = str(signal.get("message") or signal.get("reason") or "No message supplied.")
    run_url = ""
    if os.getenv("GITHUB_REPOSITORY") and os.getenv("GITHUB_RUN_ID"):
        run_url = (
            f"{os.getenv('GITHUB_SERVER_URL', 'https://github.com')}/"
            f"{os.environ['GITHUB_REPOSITORY']}/actions/runs/{os.environ['GITHUB_RUN_ID']}"
        )
    body = "\n\n".join(
        part
        for part in (
            f"<!-- {marker} -->",
            message,
            f"Status: `{status}`  \nTicker: `{ticker}`  \nEngine date (ET): `{date_et}`",
            f"Workflow run: {run_url}" if run_url else "",
            "This alert is generated from the committed Engine 4 artifact. Confirm the live broker quote before placing any order.",
        )
        if part
    )
    sms_text = _sms_text(kind, status, ticker, message, run_url)

    if dry_run:
        result = {
            "delivery": "DRY_RUN",
            "marker": marker,
            "title": title,
            "body": body,
            "sms_text": sms_text,
        }
        _write_audit(result)
        return result

    token = os.getenv("GITHUB_TOKEN", "")
    repository = os.getenv("GITHUB_REPOSITORY", "")
    github_result: dict = {"delivery": "NOT_CONFIGURED"}
    issue: dict | None = None
    sms_already_accepted = False
    try:
        if token and "/" in repository:
            issues_url = f"{API}/repos/{repository}/issues"
            issues = _github_request(
                "GET", issues_url, token, params={"state": "all", "per_page": 100}
            ).json()
            issue = next(
                (item for item in issues if marker in str(item.get("body") or "")),
                None,
            )
            if issue:
                sms_already_accepted = SMS_ACCEPTED_MARKER in str(issue.get("body") or "")
                github_result = {
                    "delivery": "DEDUPLICATED",
                    "issue_number": issue.get("number"),
                    "issue_url": issue.get("html_url"),
                }
            else:
                owner = repository.split("/", 1)[0]
                issue = _github_request(
                    "POST",
                    issues_url,
                    token,
                    json={"title": title, "body": body, "assignees": [owner]},
                ).json()
                github_result = {
                    "delivery": "SENT",
                    "issue_number": issue.get("number"),
                    "issue_url": issue.get("html_url"),
                    "assigned_to": owner,
                }
    except Exception as exc:
        github_result = {"delivery": "FAILED", "reason": f"{type(exc).__name__}: {exc}"}

    sms_result = (
        {"delivery": "DEDUPLICATED"}
        if sms_already_accepted
        else _send_openphone_sms(sms_text)
    )

    if (
        sms_result.get("delivery") == "API_ACCEPTED"
        and issue
        and token
        and "/" in repository
    ):
        try:
            issue_body = str(issue.get("body") or body)
            if SMS_ACCEPTED_MARKER not in issue_body:
                issue_body = f"{issue_body}\n\n{SMS_ACCEPTED_MARKER}"
                _github_request(
                    "PATCH",
                    f"{API}/repos/{repository}/issues/{issue['number']}",
                    token,
                    json={"body": issue_body},
                )
        except Exception as exc:
            sms_result["dedup_marker_update"] = f"FAILED: {type(exc).__name__}: {exc}"

    result = {
        "delivery": "SENT"
        if sms_result.get("delivery") in {"API_ACCEPTED", "DEDUPLICATED"}
        else "DEGRADED",
        "marker": marker,
        "sms": sms_result,
        "github": github_result,
    }
    _write_audit(result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "kind",
        choices=(
            "preflight",
            "launch",
            "watchdog",
            "start",
            "final",
            "recovery",
            "complete",
            "failure",
            "test",
        ),
    )
    parser.add_argument("--message")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--require-delivery", action="store_true")
    args = parser.parse_args()
    result = notify(args.kind, args.message, args.dry_run)
    print(json.dumps(result, indent=2), flush=True)
    if args.require_delivery and result.get("delivery") != "SENT":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
