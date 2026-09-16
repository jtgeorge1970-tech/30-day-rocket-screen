from __future__ import annotations

"""Immediate, deduplicated Engine 4 notifications through GitHub Issues.

The production workflow already runs on GitHub and therefore has a short-lived,
repository-scoped token. Assigning the alert issue to the repository owner uses
GitHub's native push/email notification path without storing another credential.
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests


OUT = Path("output/engine4")
ET = ZoneInfo("America/New_York")
API = "https://api.github.com"


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
    return {
        "status": "PIPELINE_FAILURE",
        "reason": "workflow_stage_failed",
        "message": failure_message or "ENGINE 4 DATA/PIPELINE FAILURE",
    }


def _request(method: str, url: str, token: str, **kwargs) -> requests.Response:
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    response = requests.request(method, url, headers=headers, timeout=15, **kwargs)
    response.raise_for_status()
    return response


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

    if dry_run:
        result = {"delivery": "DRY_RUN", "marker": marker, "title": title, "body": body}
        _write_audit(result)
        return result

    token = os.getenv("GITHUB_TOKEN", "")
    repository = os.getenv("GITHUB_REPOSITORY", "")
    if not token or "/" not in repository:
        result = {
            "delivery": "FAILED",
            "marker": marker,
            "reason": "missing_github_token_or_repository",
        }
        _write_audit(result)
        return result

    issues_url = f"{API}/repos/{repository}/issues"
    try:
        issues = _request(
            "GET", issues_url, token, params={"state": "all", "per_page": 100}
        ).json()
        for issue in issues:
            if marker in str(issue.get("body") or ""):
                result = {
                    "delivery": "DEDUPLICATED",
                    "marker": marker,
                    "issue_url": issue.get("html_url"),
                }
                _write_audit(result)
                return result

        owner = repository.split("/", 1)[0]
        issue = _request(
            "POST",
            issues_url,
            token,
            json={"title": title, "body": body, "assignees": [owner]},
        ).json()
        result = {
            "delivery": "SENT",
            "marker": marker,
            "issue_number": issue.get("number"),
            "issue_url": issue.get("html_url"),
            "assigned_to": owner,
        }
    except Exception as exc:
        result = {
            "delivery": "FAILED",
            "marker": marker,
            "reason": f"{type(exc).__name__}: {exc}",
        }
    _write_audit(result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=("final", "recovery", "failure"))
    parser.add_argument("--message")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    result = notify(args.kind, args.message, args.dry_run)
    print(json.dumps(result, indent=2), flush=True)


if __name__ == "__main__":
    main()
