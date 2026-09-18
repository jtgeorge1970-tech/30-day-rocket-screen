from __future__ import annotations

"""Date-locked, SSOT-compliant Engine 4 stage reporting and verification.

This module is read-only with respect to trading decisions.  It reads the JSON
artifacts produced by the existing engine, rejects stale/missing data, writes a
human-readable report for GitHub/SMS, and verifies terminal completeness.
"""

import argparse
import json
import math
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


OUT = Path("output/engine4")
ET = ZoneInfo("America/New_York")


def _read(name: str) -> dict:
    path = OUT / name
    if not path.exists():
        raise RuntimeError(f"ENGINE 4 REPORTING FAILURE — missing {path}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise RuntimeError(f"ENGINE 4 REPORTING FAILURE — unreadable {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise RuntimeError(f"ENGINE 4 REPORTING FAILURE — {path} is not a JSON object")
    return payload


def _date(payload: dict) -> str:
    return str(payload.get("target_date_et") or payload.get("market_date_et") or "")


def _require_date(payload: dict, expected: str, label: str) -> None:
    actual = _date(payload)
    if actual != expected:
        raise RuntimeError(
            f"ENGINE 4 DATE FAILURE — {label} has {actual!r}; expected {expected!r}"
        )


def _number(value, default="UNAVAILABLE"):
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float)) and math.isfinite(float(value)):
        return int(value) if float(value).is_integer() else round(float(value), 4)
    return default


def _time(value) -> str:
    if not value:
        return "UNAVAILABLE"
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00")).astimezone(ET)
        return parsed.strftime("%Y-%m-%d %I:%M:%S %p ET")
    except Exception:
        return "UNAVAILABLE"


def _timeline_times(expected: str, stage_names: set[str]) -> tuple[str, str]:
    timeline = _read("timeline.json")
    _require_date(timeline, expected, "timeline.json")
    events = [e for e in timeline.get("events", []) if e.get("stage") in stage_names]
    started = next((e.get("time_et") for e in events if e.get("status") == "STARTED"), None)
    completed = next(
        (e.get("time_et") for e in reversed(events) if e.get("status") == "COMPLETED"),
        None,
    )
    return _time(started), _time(completed)


def _top_rows(rows: list[dict], limit: int = 10) -> list[str]:
    eligible = [r for r in rows if r.get("premarket_eligible") is True]
    lines = []
    for index, row in enumerate(eligible[:limit], start=1):
        score = _number(row.get("score"))
        grade = row.get("premarket_grade") or "UNAVAILABLE"
        catalyst = row.get("catalyst_source") or "UNAVAILABLE"
        activity = row.get("premarket_volume_metric_source") or "UNAVAILABLE"
        spread = row.get("spread_source") or row.get("quote_source") or "UNAVAILABLE"
        failures = row.get("premarket_failures") or "NONE"
        lines.append(
            f"{index}. {row.get('ticker', 'UNAVAILABLE')} — {score}/{grade}; "
            f"catalyst={catalyst}; activity={activity}; spread={spread}; failures={failures}"
        )
    return lines or ["No eligible finalists."]


def _write(stage: str, expected: str, lines: list[str], sms_lines: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    full = "\n".join(lines).rstrip() + "\n"
    sms = "\n".join(sms_lines).rstrip() + "\n"
    (OUT / f"stage_{stage}_report.md").write_text(full, encoding="utf-8")
    (OUT / f"stage_{stage}_sms.txt").write_text(sms, encoding="utf-8")
    print(full, flush=True)
    summary = os.getenv("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as handle:
            handle.write(full + "\n")


def report_prescreen(expected: str) -> None:
    pre = _read("prescreen_report.json")
    _require_date(pre, expected, "prescreen_report.json")
    started, completed = _timeline_times(expected, {"PRE-SCREEN"})
    counts = {
        "baseline eligible": _number(pre.get("baseline_eligible")),
        "trustworthy price observations": _number(pre.get("trustworthy_observed")),
        "NATURAL broad-qualified": _number(pre.get("broad_qualified")),
        "Nasdaq premarket enriched": _number(pre.get("nasdaq_premarket_enriched")),
        "NONZERO premarket activity": _number(pre.get("nonzero_premarket_activity_count")),
        "strict activity": _number(pre.get("strict_activity_count")),
        "RETAINED BY TOP-100 CAP": _number(pre.get("retained_by_cap")),
    }
    lines = [
        f"## Engine 4 Stage 1 — Pre-screen — {expected} ET",
        f"Actual start: {started}",
        f"Actual completion: {completed}",
        *[f"- {key}: {value}" for key, value in counts.items()],
    ]
    sms = [
        f"STAGE 1 PRE-SCREEN COMPLETE — {expected} ET",
        f"Baseline {counts['baseline eligible']}; trustworthy {counts['trustworthy price observations']}; natural broad {counts['NATURAL broad-qualified']}.",
        f"Nasdaq enriched {counts['Nasdaq premarket enriched']}; nonzero activity {counts['NONZERO premarket activity']}; strict activity {counts['strict activity']}.",
        f"Retained by configured Top-100 cap: {counts['RETAINED BY TOP-100 CAP']}.",
    ]
    _write("prescreen", expected, lines, sms)


def report_deep(expected: str) -> None:
    deep = _read("deep_ranked.json")
    _require_date(deep, expected, "deep_ranked.json")
    started, completed = _timeline_times(expected, {"DEEP 100-POINT ANALYSIS"})
    counts = {
        "SELECTED FOR DEEP ANALYSIS BY TOP-60 CAP": _number(deep.get("selected_for_deep")),
        "ACTUALLY ANALYZED": _number(deep.get("analyzed_count")),
        "SCORE >=80": _number(deep.get("score80_count")),
        "LAUNCHPAD ELIGIBLE": _number(deep.get("launchpad_eligible_count")),
        "B-grade": _number(deep.get("b_grade_count")),
        "STRICT A/A+": _number(deep.get("a_grade_count")),
    }
    leaders = _top_rows(deep.get("ranked", []))
    lines = [
        f"## Engine 4 Stage 2 — Deep analysis — {expected} ET",
        f"Actual start: {started}",
        f"Actual completion: {completed}",
        *[f"- {key}: {value}" for key, value in counts.items()],
        "### Ranked eligible finalists (maximum 10)",
        *leaders,
    ]
    sms = [
        f"STAGE 2 DEEP ANALYSIS COMPLETE — {expected} ET",
        f"Selected by Top-60 cap {counts['SELECTED FOR DEEP ANALYSIS BY TOP-60 CAP']}; actually analyzed {counts['ACTUALLY ANALYZED']}.",
        f">=80 {counts['SCORE >=80']}; launchpad eligible {counts['LAUNCHPAD ELIGIBLE']}; B {counts['B-grade']}; strict A/A+ {counts['STRICT A/A+']}.",
    ]
    _write("deep", expected, lines, sms)


def report_freeze(expected: str) -> None:
    top = _read("top25_frozen.json")
    _require_date(top, expected, "top25_frozen.json")
    started, completed = _timeline_times(
        expected, {"09:18 REFRESH + RANKING", "TOP-25 FREEZE"}
    )
    counts = {
        "baseline eligible": _number(top.get("baseline_eligible")),
        "trustworthy price observations": _number(top.get("trustworthy_observed")),
        "NATURAL broad-qualified": _number(top.get("broad_qualified")),
        "Nasdaq premarket enriched": _number(top.get("nasdaq_premarket_enriched")),
        "NONZERO premarket activity": _number(top.get("nonzero_premarket_activity_count")),
        "strict activity": _number(top.get("strict_activity_count")),
        "RETAINED BY TOP-100 CAP": _number(top.get("retained_by_cap")),
        "SELECTED FOR DEEP ANALYSIS BY TOP-60 CAP": _number(top.get("selected_for_deep")),
        "ACTUALLY ANALYZED": _number(top.get("refresh_analyzed_count")),
        "SCORE >=80": _number(top.get("score80_count")),
        "LAUNCHPAD ELIGIBLE": _number(top.get("launchpad_eligible_count")),
        "B-grade": _number(top.get("b_grade_count")),
        "STRICT A/A+": _number(top.get("a_grade_count")),
        "FROZEN FINAL-SCAN COUNT": _number(top.get("actual_count")),
    }
    leaders = _top_rows(top.get("candidates", []))
    lines = [
        f"## Engine 4 Stage 3 — Refresh and freeze — {expected} ET",
        f"Actual start: {started}",
        f"Actual completion: {completed}",
        *[f"- {key}: {value}" for key, value in counts.items()],
        "### Frozen eligible finalists (maximum 10)",
        *leaders,
    ]
    sms = [
        f"STAGE 3 REFRESH/FREEZE COMPLETE — {expected} ET",
        f"Natural broad {counts['NATURAL broad-qualified']}; retained by Top-100 cap {counts['RETAINED BY TOP-100 CAP']}; selected by Top-60 cap {counts['SELECTED FOR DEEP ANALYSIS BY TOP-60 CAP']}; analyzed {counts['ACTUALLY ANALYZED']}.",
        f">=80 {counts['SCORE >=80']}; eligible {counts['LAUNCHPAD ELIGIBLE']}; B {counts['B-grade']}; strict A/A+ {counts['STRICT A/A+']}; frozen {counts['FROZEN FINAL-SCAN COUNT']}.",
    ]
    _write("freeze", expected, lines, sms)


def report_bench(expected: str) -> None:
    bench = _read("watch_bench_report.json")
    _require_date(bench, expected, "watch_bench_report.json")
    started, completed = _timeline_times(expected, {"TOP-25 MULTI-DAY BENCH"})
    candidates = bench.get("candidates", [])
    roster = [
        f"{row.get('bench_rank')}. {row.get('ticker')} — {row.get('score')}/{row.get('premarket_grade')} — "
        f"{row.get('tier')} — day {row.get('age_sessions')} — {row.get('admission_reason')}"
        for row in candidates[:25]
    ] or ["Bench is empty; the Top-25 cap is not a quota."]
    lines = [
        f"## Engine 4 Stage 3B — Multi-day Bench — {expected} ET",
        f"Actual start: {started}",
        f"Actual completion: {completed}",
        f"- Bench competition universe: {_number(bench.get('competition_universe_count'))}",
        f"- Freshly scored: {_number(bench.get('freshly_scored_count'))}",
        f"- NATURALLY WATCH-QUALIFIED: {_number(bench.get('naturally_watch_qualified_count'))}",
        f"- RETAINED BY TOP-25 BENCH CAP: {_number(bench.get('retained_by_top25_bench_cap'))}",
        f"- Hot: {_number(bench.get('hot_count'))}",
        f"- Developing: {_number(bench.get('developing_count'))}",
        f"- Reserve: {_number(bench.get('reserve_count'))}",
        f"- Added: {', '.join(bench.get('additions', [])) or 'NONE'}",
        f"- Promoted: {', '.join(bench.get('promotions', [])) or 'NONE'}",
        f"- Demoted: {', '.join(bench.get('demotions', [])) or 'NONE'}",
        f"- Removed: {len(bench.get('removals', []))}",
        "### Complete Bench roster (maximum 25)",
        *roster,
    ]
    sms = [
        f"STAGE 3B TOP-25 BENCH COMPLETE — {expected} ET",
        f"Natural watch-qualified {_number(bench.get('naturally_watch_qualified_count'))}; retained by Top-25 Bench cap {_number(bench.get('retained_by_top25_bench_cap'))}.",
        f"Hot {_number(bench.get('hot_count'))}; Developing {_number(bench.get('developing_count'))}; Reserve {_number(bench.get('reserve_count'))}.",
        f"Added {len(bench.get('additions', []))}; promoted {len(bench.get('promotions', []))}; demoted {len(bench.get('demotions', []))}; removed {len(bench.get('removals', []))}.",
    ]
    _write("bench", expected, lines, sms)


def report_signal(expected: str, stage: str) -> None:
    filename = "final_signal.json" if stage == "final" else "recovery_signal.json"
    payload = _read(filename)
    _require_date(payload, expected, filename)
    names = {"FINAL 09:45 LIVE CONFIRMATION"} if stage == "final" else {"POST-OPEN RECOVERY WATCH"}
    started, completed = _timeline_times(expected, names)
    status = str(payload.get("status") or "UNAVAILABLE")
    ticker = str(payload.get("ticker") or "MARKET")
    reason = str(payload.get("reason") or payload.get("message") or "UNAVAILABLE")
    lines = [
        f"## Engine 4 Stage {'4 — Primary entry' if stage == 'final' else '5 — Recovery'} — {expected} ET",
        f"Actual start: {started}",
        f"Actual completion: {completed}",
        f"- Result: {status}",
        f"- Ticker: {ticker}",
        f"- Reason: {reason}",
    ]
    sms = [
        f"STAGE {'4 PRIMARY' if stage == 'final' else '5 RECOVERY'} RESULT — {expected} ET",
        f"{status} — {ticker}",
        reason,
    ]
    _write(stage, expected, lines, sms)


def _audit_entries() -> list[dict]:
    path = OUT / "notification_audit_log.json"
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload if isinstance(payload, list) else []


def verify_notification(expected: str, kind: str, recipients: int) -> None:
    prefix = f"ENGINE4-ALERT:{expected}:{kind}:"
    entries = [e for e in _audit_entries() if str(e.get("marker", "")).startswith(prefix)]
    if not entries:
        raise RuntimeError(f"ENGINE 4 NOTIFICATION FAILURE — no audit entry for {kind}")
    sms = entries[-1].get("sms", {})
    if sms.get("delivery") not in {"API_ACCEPTED", "DEDUPLICATED"}:
        raise RuntimeError(
            f"ENGINE 4 NOTIFICATION FAILURE — {kind} SMS has no accepted proof: {sms}"
        )
    if int(sms.get("recipient_count", 0)) != recipients:
        raise RuntimeError(
            f"ENGINE 4 NOTIFICATION FAILURE — {kind} accepted for "
            f"{sms.get('recipient_count', 0)} recipients; expected {recipients}"
        )
    print(
        f"SMS VERIFIED: {kind} {sms.get('delivery')} for {recipients} recipients",
        flush=True,
    )


def verify_complete(expected: str, recipients: int) -> None:
    artifacts = {
        "prescreen_report.json": _read("prescreen_report.json"),
        "deep_ranked.json": _read("deep_ranked.json"),
        "top25_frozen.json": _read("top25_frozen.json"),
        "watch_bench_report.json": _read("watch_bench_report.json"),
        "final_signal.json": _read("final_signal.json"),
        "recovery_signal.json": _read("recovery_signal.json"),
        "timeline.json": _read("timeline.json"),
    }
    for name, payload in artifacts.items():
        _require_date(payload, expected, name)
    for name in ("final_signal.json", "recovery_signal.json"):
        if artifacts[name].get("status") == "PIPELINE_FAILURE":
            raise RuntimeError(f"ENGINE 4 PIPELINE FAILURE — {name}")

    stages = [e.get("stage") for e in artifacts["timeline.json"].get("events", [])]
    required = [
        "PRE-SCREEN",
        "DEEP 100-POINT ANALYSIS",
        "09:18 REFRESH + RANKING",
        "TOP-25 FREEZE",
        "TOP-25 MULTI-DAY BENCH",
        "FINAL 09:45 LIVE CONFIRMATION",
        "POST-OPEN RECOVERY WATCH",
    ]
    positions = []
    for stage in required:
        if stage not in stages:
            raise RuntimeError(f"ENGINE 4 ORDER FAILURE — missing {stage}")
        positions.append(stages.index(stage))
    if positions != sorted(positions):
        raise RuntimeError(f"ENGINE 4 ORDER FAILURE — stages are out of order: {stages}")
    events = artifacts["timeline.json"].get("events", [])
    for stage in required:
        states = [event.get("status") for event in events if event.get("stage") == stage]
        if "STARTED" not in states or "COMPLETED" not in states:
            raise RuntimeError(
                f"ENGINE 4 COMPLETION FAILURE — {stage} lacks STARTED/COMPLETED proof: {states}"
            )

    for kind in ("start", "prescreen", "deep", "freeze", "bench", "final", "recovery"):
        verify_notification(expected, kind, recipients)
    print(f"ENGINE4_FULL_INVARIANT_PASS date={expected}", flush=True)


def report_complete(expected: str, recipients: int) -> None:
    verify_complete(expected, recipients)
    verify_notification(expected, "complete", recipients)
    pre = _read("prescreen_report.json")
    deep = _read("deep_ranked.json")
    frozen = _read("top25_frozen.json")
    bench = _read("watch_bench_report.json")
    primary = _read("final_signal.json")
    recovery = _read("recovery_signal.json")
    provider = _read("provider_health.json")
    provider_date = str(provider.get("target_date_et") or "")
    if provider_date != expected:
        raise RuntimeError(
            f"ENGINE 4 DATE FAILURE — provider_health.json has {provider_date!r}; expected {expected!r}"
        )

    frozen_count = _number(frozen.get("actual_count"))
    selection = "SUCCESS" if isinstance(frozen_count, int) and frozen_count > 0 else "NO ELIGIBLE SELECTION"
    actionable = {str(primary.get("status")), str(recovery.get("status"))} & {"BUY", "ARM"}
    execution = (
        "UNAVAILABLE — Engine 4 has no broker order/fill integration"
        if actionable
        else "NOT APPLICABLE — no actionable BUY/ARM signal"
    )
    recovery_watch = _read("recovery_watch.json")
    watch_tickers = [str(row.get("ticker")) for row in recovery_watch.get("candidates", [])]
    run_url = ""
    if os.getenv("GITHUB_REPOSITORY") and os.getenv("GITHUB_RUN_ID"):
        run_url = (
            f"{os.getenv('GITHUB_SERVER_URL', 'https://github.com')}/"
            f"{os.environ['GITHUB_REPOSITORY']}/actions/runs/{os.environ['GITHUB_RUN_ID']}"
        )

    lines = [
        f"# Engine 4 terminal report — {expected} ET",
        f"- Workflow run ID: {os.getenv('GITHUB_RUN_ID', 'UNAVAILABLE')}",
        f"- Workflow link: {run_url or 'UNAVAILABLE'}",
        f"- Locked Eastern market date: {expected}",
        f"- Provider health: {provider.get('state', 'UNAVAILABLE')}",
        f"- Artifact/date/order verification: PASS",
        f"- SMS API acceptance: VERIFIED for {recipients} recipients at every required stage and completion",
        "## Separate terminal results",
        f"- SELECTION result: {selection}; frozen final-scan count {frozen_count}",
        f"- PRIMARY ENTRY result: {primary.get('status', 'UNAVAILABLE')} — {primary.get('reason', 'UNAVAILABLE')}",
        f"- BENCH result: {bench.get('retained_by_top25_bench_cap', 'UNAVAILABLE')} retained by Top-25 Bench cap; Hot {bench.get('hot_count', 'UNAVAILABLE')}",
        f"- RECOVERY result: {recovery.get('status', 'UNAVAILABLE')} — {recovery.get('reason', 'UNAVAILABLE')}",
        f"- EXECUTION result: {execution}",
        f"- Recovery-watch count/tickers: {recovery_watch.get('actual_count', 'UNAVAILABLE')} — {', '.join(watch_tickers) or 'NONE'}",
        "## SSOT funnel",
        f"- baseline eligible: {_number(pre.get('baseline_eligible'))}",
        f"- trustworthy price observations: {_number(pre.get('trustworthy_observed'))}",
        f"- NATURAL broad-qualified: {_number(pre.get('broad_qualified'))}",
        f"- Nasdaq premarket enriched: {_number(pre.get('nasdaq_premarket_enriched'))}",
        f"- NONZERO premarket activity: {_number(pre.get('nonzero_premarket_activity_count'))}",
        f"- strict-activity count: {_number(pre.get('strict_activity_count'))}",
        f"- RETAINED BY TOP-100 CAP: {_number(pre.get('retained_by_cap'))}",
        f"- SELECTED FOR DEEP ANALYSIS BY TOP-60 CAP: {_number(deep.get('selected_for_deep'))}",
        f"- ACTUALLY ANALYZED: {_number(deep.get('analyzed_count'))}",
        f"- SCORE >=80: {_number(deep.get('score80_count'))}",
        f"- LAUNCHPAD ELIGIBLE: {_number(deep.get('launchpad_eligible_count'))}",
        f"- B-grade: {_number(deep.get('b_grade_count'))}",
        f"- STRICT A/A+: {_number(deep.get('a_grade_count'))}",
        f"- FROZEN FINAL-SCAN COUNT: {frozen_count}",
        "## Ranked eligible finalists (maximum 10)",
        *_top_rows(frozen.get("candidates", [])),
        "## Exact stage times",
    ]
    timeline = _read("timeline.json")
    for stage in (
        "PRE-SCREEN",
        "DEEP 100-POINT ANALYSIS",
        "09:18 REFRESH + RANKING",
        "TOP-25 FREEZE",
        "TOP-25 MULTI-DAY BENCH",
        "FINAL 09:45 LIVE CONFIRMATION",
        "POST-OPEN RECOVERY WATCH",
    ):
        matching = [event for event in timeline.get("events", []) if event.get("stage") == stage]
        started = next((event.get("time_et") for event in matching if event.get("status") == "STARTED"), None)
        completed = next((event.get("time_et") for event in reversed(matching) if event.get("status") == "COMPLETED"), None)
        lines.append(f"- {stage}: {_time(started)} to {_time(completed)}")
    lines.append("- Exact terminal conclusion: SUCCESS — full live workflow and invariants completed")
    _write(
        "complete",
        expected,
        lines,
        [
            f"ENGINE 4 COMPLETE — {expected} ET",
            f"Selection {selection}; primary {primary.get('status', 'UNAVAILABLE')}; recovery {recovery.get('status', 'UNAVAILABLE')}.",
            f"Bench {bench.get('retained_by_top25_bench_cap', 'UNAVAILABLE')}/25; execution {execution}.",
            "Artifacts, stage order, provider date, and two-recipient SMS proof verified.",
        ],
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command",
        choices=(
            "prescreen",
            "deep",
            "freeze",
            "bench",
            "final",
            "recovery",
            "complete",
            "verify-complete",
            "verify-notification",
        ),
    )
    parser.add_argument("--date", required=True)
    parser.add_argument("--kind")
    parser.add_argument("--recipients", type=int, default=2)
    args = parser.parse_args()

    if args.command == "prescreen":
        report_prescreen(args.date)
    elif args.command == "deep":
        report_deep(args.date)
    elif args.command == "freeze":
        report_freeze(args.date)
    elif args.command == "bench":
        report_bench(args.date)
    elif args.command in {"final", "recovery"}:
        report_signal(args.date, args.command)
    elif args.command == "verify-complete":
        verify_complete(args.date, args.recipients)
    elif args.command == "complete":
        report_complete(args.date, args.recipients)
    else:
        if not args.kind:
            raise SystemExit("--kind is required for verify-notification")
        verify_notification(args.date, args.kind, args.recipients)


if __name__ == "__main__":
    main()
