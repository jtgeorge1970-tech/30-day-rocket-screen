"""Audit durable forward evidence without creating or backfilling predictions."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from ofts.daily import (HORIZONS, WATCH, atomic, completed_session, freshness_gate,
                        load_json, load_qualified_snapshots, market_schedule,
                        outcomes, read_history, save_json, score_interpretation)
from ofts.cycle_ledger import rebuild_cycle_ledger


def band(score):
    if score is None:
        return 'UNSCORED'
    return '<40' if score < 40 else '40-<60' if score < 60 else '60-<80' if score < 80 else '80-100'


def evidence_hashes(state):
    return {str(p.relative_to(state)): hashlib.sha256(p.read_bytes()).hexdigest()
            for directory in ('predictions', 'signals', 'fingerprints', 'attempts')
            for p in sorted((state / directory).glob('*.json'))}


def saved_refresh_gate(state, refresh, target):
    # Audit the attempted session, including a failed first snapshot; never
    # substitute the last successful cohort's selection or watchlist.
    snapshot = (load_json(state / 'predictions' / (target + '-qualified.json'), None)
                or load_json(state / 'predictions' / (target + '.json'), None))
    if snapshot is None:
        return dict(passed=False, reason='MISSING_SESSION_SELECTION',
                    required_stale=[], fresh=0, selected=0)
    gate = freshness_gate(refresh.get('symbols', {}),
                          snapshot.get('watchlist', WATCH), snapshot['selected'])
    if refresh.get('asof') != target:
        gate.update(passed=False, reason='SAVED_REFRESH_NOT_LATEST_COMPLETED_SESSION')
    return gate


def audit_saved(state, now=None):
    now = now or datetime.now(timezone.utc)
    # Fail closed: a missing restore must never bootstrap an empty audit.
    control = json.loads((state / 'control.json').read_text())
    if not (state / 'predictions').is_dir():
        raise ValueError('MISSING_DURABLE_PREDICTIONS')
    before = evidence_hashes(state)
    snapshots = load_qualified_snapshots(state / 'predictions')
    schedule = market_schedule(now)
    target = completed_session(schedule, now)
    symbols = {r['symbol'] for s in snapshots for r in s['rows']}
    for p in (state / 'signals').glob('*.json'):
        symbols.update(r['symbol'] for r in load_json(p, {})['rows'])
    histories = {s: [r for r in read_history(state, s) if r['date'] <= target]
                 for s in symbols | {'SPY'}}
    results = [r for s in snapshots for r in outcomes(s, histories, schedule, target)]
    saved_results = load_json(state / 'outcomes.json', [])
    ledger = rebuild_cycle_ledger(state, histories, schedule)
    groups = []
    for model in sorted({r['model_hash'] for r in results}):
        for horizon in HORIZONS:
            for score_band in ('<40', '40-<60', '60-<80', '80-100', 'UNSCORED'):
                rows = [r for r in results if r['model_hash'] == model
                        and r['horizon'] == horizon and band(r['score']) == score_band]
                mature = [r for r in rows if r['status'] == 'MATURE']
                returns = [r['net_assumed_return_pct'] for r in mature]
                positive = [v for v in returns if v > 0]
                nonpositive = [v for v in returns if v <= 0]
                excess = [r['excess_gross_pct'] for r in mature if 'excess_gross_pct' in r]
                mean = lambda values: sum(values)/len(values) if values else None
                groups.append(dict(model_hash=model, horizon=horizon, score_band=score_band,
                    observations=len(rows), statuses=dict(Counter(r['status'] for r in rows)),
                    mature=len(mature), positive=len(positive), nonpositive=len(nonpositive),
                    average_net_pct=mean(returns), average_positive_pct=mean(positive),
                    average_nonpositive_pct=mean(nonpositive), benchmark_pairs=len(excess),
                    average_excess_gross_pct=mean(excess),
                    worst_adverse_excursion_pct=min((r['adverse_excursion_pct'] for r in mature), default=None)))
    latest = max(snapshots, key=lambda s: (s['asof'], s['recorded_at'])) if snapshots else None
    refresh = load_json(state / 'refresh.json', {})
    gate = saved_refresh_gate(state, refresh, target)
    if before != evidence_hashes(state):
        raise AssertionError('IMMUTABLE_EVIDENCE_CHANGED')
    if control != json.loads((state / 'control.json').read_text()):
        raise AssertionError('AUDIT_CHANGED_ROTATION_CONTROL')
    audit = dict(recorded_at=now.isoformat(), market_asof=target,
                 qualified_cohorts=len(snapshots),
                 all_prediction_files=len(list((state / 'predictions').glob('*.json'))),
                 attempts=len(list((state / 'attempts').glob('*.json'))),
                 cohort_rows=sum(len(s['rows']) for s in snapshots),
                 outcome_counts=dict(Counter(r['status'] for r in results)),
                 outcome_recompute_matches_saved=results == saved_results,
                 immutable_evidence_sha256=before, control_unchanged=control,
                 freshness_gate=gate, cycle_summary=ledger['summary'],
                 horizon_score_report_card=groups,
                 production_gate='RESEARCH_ONLY_NO_GO', validated_buy_threshold=None,
                 source='Restored durable OHLCV and immutable cohorts; no new market-data download',
                 evidence_note='Correlated overlapping horizon observations, not independent trades. Rejected price and quality candidates retained as controls.')
    save_json(state / 'outcomes.json', results)
    stamp = now.strftime('%Y%m%dT%H%M%S%fZ')
    save_json(state / 'audits' / (stamp + '.json'), audit)
    save_json(state / 'latest_audit.json', audit)
    lines = ['# OFTS saved-evidence report card', '', f'Audit UTC: {now.isoformat()}',
             f'Market as-of: {target}; qualified cohorts: {len(snapshots)}; '
             f'cohort rows: {audit["cohort_rows"]}; attempts retained: {audit["attempts"]}.',
             f'Outcome counts: {audit["outcome_counts"]}.',
             f'Saved-data freshness gate: {gate}.',
             f'Cycle ledger: {ledger["summary"]}.',
             'Validated BUY threshold: NONE. Production gate: RESEARCH_ONLY_NO_GO.',
             'Hypothetical next-open entry, price returns excluding dividends, 0.20% round-trip costs.',
             'Rejected candidates are controls. Overlapping horizons are not independent trades.', '',
             '| Horizon (sessions) | Mature | Pending | Data-ineligible | Other errors | First exit date |',
             '|---|---:|---:|---:|---:|---|']
    for h in HORIZONS:
        rs = [r for r in results if r['horizon'] == h]
        counts = Counter(r['status'] for r in rs)
        lines.append(f'| {h} | {counts["MATURE"]} | {counts["PENDING"]} | {counts["INELIGIBLE_DATA"]} | '
                     f'{sum(v for k,v in counts.items() if k not in {"MATURE", "PENDING", "INELIGIBLE_DATA"})} | '
                     f'{min((r["end_date"] for r in rs), default="N/A")} |')
    lines += ['', 'By model, horizon and score band: see latest_audit.json. '
              'Unavailable average gains/losses, net returns, adverse excursions and SPY comparisons are null, not zero.']
    if latest:
        status = score_interpretation(latest['rows'])
        lines += ['', '## Frozen v2.3 baseline quality leaders (not current keepers or BUY recommendations)',
                  f'Cohort recorded: {latest["recorded_at"]}; model: {latest["model_hash"]}.',
                  f'Score distribution: {status}.',
                  '| Symbol | Frozen score | Frozen classification |', '|---|---:|---|']
        leaders = sorted((r for r in latest['rows'] if r.get('score') is not None
                          and r['classification'] == 'CANDIDATE'), key=lambda r: -r['score'])
        lines += [f'| {r["symbol"]} | {r["score"]:.3f} | {r["classification"]} |' for r in leaders[:25]]
    lines += ['', '## Source failures', *[f'- {s}: {r["error"]}' for s,r in refresh.get('symbols', {}).items() if r['status'] != 'FRESH'],
              '', 'Immutable predictions, signals, fingerprints and attempts verified unchanged; rotation cursor unchanged.']
    atomic(state / 'AUDIT_REPORT.md', ('\n'.join(lines)+'\n').encode())
    return audit


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--state', type=Path, required=True)
    args = parser.parse_args()
    report = audit_saved(args.state)
    print(json.dumps({k:v for k,v in report.items() if k not in {'immutable_evidence_sha256', 'horizon_score_report_card'}}, indent=2))
