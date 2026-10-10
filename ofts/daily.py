"""Persistent forward research ledger. No brokerage orders or production BUY claims."""
import argparse
import csv
import gzip
import hashlib
import io
import json
import math
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from statistics import median

from ofts.research.v23_replacement import evaluate
from ofts.research.candidate_components import detect_turns

ROOT = Path(__file__).resolve().parents[1]
WATCH = 'HNRG CHTR FUBO EPOW WULF HLIT JACK TGS SPGI CSIQ XPRO SFM DTIL TBLA FWRG NYAX OWLT SRAD ATGL FMC LE MESO NX MBLY IDR'.split()
HORIZONS = (5, 10, 20, 30, 60)
FIELDS = ['date', 'open', 'high', 'low', 'close', 'volume', 'split']
MIN_FRESH_COHORT = 100
DATA_FAILURES = {'STALE_DATA', 'DATA_ERROR', 'INSUFFICIENT_HISTORY'}


def snapshot_is_qualified(snapshot, minimum=MIN_FRESH_COHORT):
    """Only forward-test cohorts that met the market-data gate when frozen."""
    coverage = snapshot.get('coverage', {})
    if 'fresh' in coverage:
        return int(coverage['fresh']) >= int(coverage.get('minimum_fresh', minimum))
    # Compatibility for the first immutable pre-gate snapshot: infer its
    # usable coverage without changing or deleting that historical record.
    return sum(r.get('classification') not in DATA_FAILURES and
               r.get('asof') == snapshot.get('asof') for r in snapshot.get('rows', [])) >= minimum


def load_qualified_snapshots(predictions):
    return [s for p in sorted(predictions.glob('*.json'))
            if snapshot_is_qualified(s := load_json(p, {}))]


def cycle_fingerprint(closes, threshold, structural):
    """Point-in-time natural-cycle description; never reads bars after as-of."""
    turns = detect_turns(closes, threshold)
    peaks = [p[0] for p in turns if p[1] == 'H']
    troughs = [p[0] for p in turns if p[1] == 'L']
    intervals = ([b-a for a, b in zip(peaks, peaks[1:])] +
                 [b-a for a, b in zip(troughs, troughs[1:])])
    swing_pcts = [100 * abs(b[2] / a[2] - 1) for a, b in zip(turns, turns[1:])]
    components = structural['components']
    timing = (components['peak_timing'] + components['trough_timing']) / 2
    amplitude = components['amplitude']
    completed_cycles = len(intervals)
    confidence = ('HIGH' if completed_cycles >= 4 and min(timing, amplitude) >= 60 else
                  'MEDIUM' if completed_cycles >= 2 and min(timing, amplitude) >= 40 else 'LOW')
    return dict(cycle_sessions=median(intervals) if intervals else None,
                median_swing_pct=median(swing_pcts) if swing_pcts else None,
                completed_cycle_intervals=completed_cycles,
                confirmed_turns=len(turns), timing_consistency=timing,
                amplitude_consistency=amplitude, confidence=confidence)


def atomic(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.tmp')
    with tmp.open('wb') as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    tmp.replace(path)


def save_json(path, value):
    atomic(path, (json.dumps(value, indent=2, allow_nan=False) + '\n').encode())


def load_json(path, default):
    return json.loads(path.read_text()) if path.exists() else default


def history_path(state, symbol):
    # Hash prevents provider symbols from becoming filesystem paths.
    return state / 'history' / (hashlib.sha256(symbol.encode()).hexdigest() + '.csv.gz')


def read_history(state, symbol):
    path = history_path(state, symbol)
    if not path.exists():
        return []
    with gzip.open(path, 'rt') as f:
        return list(csv.DictReader(f))


def merge_history(old, new, target):
    rows = {}
    for row in old + new:
        if row['date'] > target:
            continue
        vals = [float(row[k]) for k in ('open', 'high', 'low', 'close')]
        o, h, l, c = vals
        if not all(math.isfinite(v) and v > 0 for v in vals) or not l <= min(o, c) <= max(o, c) <= h:
            continue
        rows[row['date']] = row
    return [rows[k] for k in sorted(rows)]


def save_history(state, symbol, rows):
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=FIELDS, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(rows)
    atomic(history_path(state, symbol), gzip.compress(out.getvalue().encode(), mtime=0))


def frozen_snapshot(path, value):
    """Freeze cohort on first attempt; failed rows remain auditable, never backfill."""
    if path.exists():
        return load_json(path, {})
    save_json(path, value)
    return value


def market_schedule(now):
    import pandas_market_calendars as calendars
    return calendars.get_calendar('NYSE').schedule(
        start_date=(now - timedelta(days=1600)).date(),
        end_date=(now + timedelta(days=120)).date())


def completed_session(schedule, now):
    # Delay beyond closing auction; holidays and early closes come from calendar.
    completed = schedule[schedule.market_close <= now - timedelta(minutes=30)]
    return str(completed.index[-1].date())


def provider_rows(frame, symbol):
    if getattr(frame.columns, 'nlevels', 1) > 1:
        frame = frame[symbol]
    rows = []
    for date, r in frame.iterrows():
        values = {k.lower(): float(r[k]) for k in ('Open', 'High', 'Low', 'Close')}
        volume = r.get('Volume', 0)
        split = r.get('Stock Splits', 0)
        rows.append(dict(date=str(date.date()), **values,
                         volume=float(volume) if math.isfinite(float(volume)) else 0,
                         split=float(split) if math.isfinite(float(split)) else 0))
    return rows


def refresh(state, symbols, target, downloader):
    audit = {}
    for symbol in symbols:
        old = read_history(state, symbol)
        error = ''
        new = []
        for attempt in range(2):
            try:
                kwargs = dict(interval='1d', auto_adjust=False, actions=True,
                              progress=False, threads=False, timeout=20, group_by='ticker')
                if old:
                    kwargs['start'] = str(datetime.fromisoformat(old[-1]['date']).date() - timedelta(days=7))
                    kwargs['end'] = str(datetime.fromisoformat(target).date() + timedelta(days=1))
                else:
                    kwargs['period'] = '2y'
                new = provider_rows(downloader(symbol, **kwargs), symbol)
                if not new:
                    raise ValueError('EMPTY_PROVIDER_RESPONSE')
                merged = merge_history(old, new, target)
                if not merged or merged[-1]['date'] != target:
                    raise ValueError('LATEST_SESSION_MISSING')
                save_history(state, symbol, merged)
                error = ''
                break
            except Exception as exc:
                error = type(exc).__name__ + ': ' + str(exc)[:180]
        # Preserve valid partial downloads but never count a failed refresh as success.
        if error and new:
            merged = merge_history(old, new, target)
            if merged:
                save_history(state, symbol, merged)
        current = read_history(state, symbol)
        audit[symbol] = dict(status='ERROR' if error else 'FRESH', error=error,
                             latest_date=current[-1]['date'] if current else None,
                             bars=len(current))
        print('REFRESH', symbol, audit[symbol]['status'], audit[symbol]['latest_date'], flush=True)
    return audit


def outcomes(snapshot, histories, schedule):
    dates = [str(d.date()) for d in schedule.index]
    start = dates.index(snapshot['asof']) + 1
    recorded = datetime.fromisoformat(snapshot['recorded_at'])
    entry_date = dates[start]
    timely = recorded < schedule.iloc[start].market_open.to_pydatetime()
    benchmark = {r['date']: r for r in histories.get('SPY', [])}
    output = []
    for prediction in snapshot['rows']:
        symbol = prediction['symbol']
        bars = {r['date']: r for r in histories.get(symbol, [])}
        for horizon in HORIZONS:
            end_date = dates[start + horizon - 1]
            row = dict(symbol=symbol, asof=snapshot['asof'], horizon=horizon,
                       score=prediction.get('score'), classification=prediction['classification'],
                       model_hash=snapshot['model_hash'], status='PENDING', entry_date=entry_date,
                       end_date=end_date)
            if not timely:
                row['status'] = 'NOT_PROSPECTIVE_RECORDED_AFTER_ENTRY'
            elif prediction['classification'] in ('STALE_DATA', 'DATA_ERROR', 'INSUFFICIENT_HISTORY'):
                row['status'] = 'INELIGIBLE_DATA'
            elif end_date in bars and entry_date in bars:
                interval = [bars.get(d) for d in dates[start:start + horizon]]
                if any(r is None for r in interval):
                    row['status'] = 'MISSING_SESSIONS'
                elif any(float(r.get('split') or 0) for r in interval):
                    row['status'] = 'CORPORATE_ACTION_REVIEW'
                else:
                    entry = float(bars[entry_date]['open'])
                    gross = 100 * (float(bars[end_date]['close']) / entry - 1)
                    row.update(status='MATURE', gross_price_return_pct=gross,
                               net_assumed_return_pct=gross - 0.20,
                               adverse_excursion_pct=100 * (min(float(r['low']) for r in interval) / entry - 1))
                    if entry_date in benchmark and end_date in benchmark:
                        benchmark_return = 100 * (float(benchmark[end_date]['close']) / float(benchmark[entry_date]['open']) - 1)
                        row.update(benchmark_price_return_pct=benchmark_return,
                                   excess_gross_pct=gross - benchmark_return)
            output.append(row)
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--state', type=Path, default=ROOT / 'ofts-state')
    parser.add_argument('--batch-size', type=int, default=100)
    args = parser.parse_args()
    if not 1 <= args.batch_size <= 500:
        raise SystemExit('INVALID_BATCH_SIZE')
    state = args.state
    state.mkdir(parents=True, exist_ok=True)
    (state / 'history').mkdir(exist_ok=True)
    (state / 'predictions').mkdir(exist_ok=True)
    now = datetime.now(timezone.utc)
    schedule = market_schedule(now)
    target = completed_session(schedule, now)
    with (ROOT / 'ofts/universe.csv').open() as f:
        universe = [r['symbol'].strip().upper() for r in csv.DictReader(f)]
    assert len(universe) == len(set(universe)) == 5502
    control = load_json(state / 'control.json', dict(cursor=0, retry=[], last_session=None))
    snapshot_path = state / 'predictions' / (target + '.json')
    recovery_path = state / 'predictions' / (target + '-qualified.json')
    # Preserve the first attempt forever. If that attempt failed coverage, a
    # later pre-entry recovery becomes a separate immutable qualified cohort.
    previous = load_json(recovery_path, None) or load_json(snapshot_path, None)
    cursor = control['cursor']
    rotation = [universe[((cursor + i) * 137) % len(universe)] for i in range(args.batch_size)]
    selected = previous['selected'] if previous else list(dict.fromkeys(WATCH + rotation + control['retry']))
    snapshots = load_qualified_snapshots(state / 'predictions')
    dates = [str(d.date()) for d in schedule.index]
    pending = {r['symbol'] for s in snapshots if s['asof'] in dates and dates.index(target) - dates.index(s['asof']) <= 65 for r in s['rows']}
    refresh_symbols = list(dict.fromkeys(selected + sorted(pending) + ['SPY']))
    import yfinance as yf
    import pandas as pd
    audit = refresh(state, refresh_symbols, target, yf.download)
    attempt = dict(asof=target, recorded_at=now.isoformat(), symbols=audit)
    save_json(state / 'refresh.json', attempt)
    save_json(state / 'attempts' / (now.strftime('%Y%m%dT%H%M%S%fZ') + '.json'), attempt)
    rows = []
    for symbol in selected:
        bars = read_history(state, symbol)
        cutoff = str((pd.Timestamp(target) - pd.DateOffset(years=2)).date())
        bars = [r for r in bars if r['date'] >= cutoff]
        row = dict(symbol=symbol, score=None, classification='STALE_DATA',
                   asof=bars[-1]['date'] if bars else None, bars=len(bars))
        if audit[symbol]['status'] == 'FRESH':
            if len(bars) < 180:
                row['classification'] = 'INSUFFICIENT_HISTORY'
            else:
                try:
                    # Existing evaluate implementation remains byte-for-byte unchanged.
                    series = [[float(r[k]) for r in bars] for k in ('high', 'low', 'close')]
                    result = evaluate(*series)
                    row.update(score=result.get('candidate_score'), classification=result['status'])
                    if result.get('candidate_score') is not None:
                        row['cycle'] = cycle_fingerprint(series[2], result['threshold_pct'], result['structural'])
                except (ValueError, TypeError, KeyError) as exc:
                    row.update(classification='DATA_ERROR', error=str(exc))
        rows.append(row)
    model_hash = hashlib.sha256(b''.join((ROOT / p).read_bytes() for p in
                               ['ofts/research/v23_replacement.py', 'ofts/research/candidate_components.py'])).hexdigest()
    fresh_count = sum(audit[s]['status'] == 'FRESH' for s in selected)
    required_fresh = min(MIN_FRESH_COHORT, len(selected))
    candidate = dict(asof=target, recorded_at=datetime.now(timezone.utc).isoformat(),
                     model_version='v2.3-research', model_hash=model_hash,
                     protocol_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                     lookback='trailing 2 calendar years', selected=selected, rows=rows,
                     coverage={'fresh': fresh_count, 'selected': len(selected),
                               'minimum_fresh': required_fresh},
                     production_approved=False,
                     execution='Hypothetical next-session open; fixed-session close; no stop/target strategy',
                     cost_assumption_roundtrip_pct=0.20)
    snapshot = None
    if fresh_count >= required_fresh:
        destination = snapshot_path
        if snapshot_path.exists() and not snapshot_is_qualified(load_json(snapshot_path, {})):
            destination = recovery_path
        snapshot = frozen_snapshot(destination, candidate)
    snapshots = load_qualified_snapshots(state / 'predictions')
    histories = {s: read_history(state, s) for s in set(refresh_symbols) | {r['symbol'] for s in snapshots for r in s['rows']}}
    results = [r for s in snapshots for r in outcomes(s, histories, schedule)]
    save_json(state / 'outcomes.json', results)
    # Cursor advances only once per session; failed symbols remain in retry queue.
    if control['last_session'] != target:
        control['cursor'] = (cursor + args.batch_size) % len(universe)
    control.update(last_session=target, retry=[s for s in selected if audit[s]['status'] != 'FRESH'])
    save_json(state / 'control.json', control)
    mature = [r for r in results if r['status'] == 'MATURE']
    summaries = []
    for model in sorted({r['model_hash'] for r in mature}):
        for horizon in HORIZONS:
            for low, high in ((0, 40), (40, 60), (60, 80), (80, 101)):
                group = [r for r in mature if r['model_hash'] == model and r['horizon'] == horizon
                         and r['score'] is not None and low <= r['score'] < high]
                if group:
                    returns = [r['net_assumed_return_pct'] for r in group]
                    wins = [v for v in returns if v > 0]
                    losses = [v for v in returns if v <= 0]
                    excess = [r['excess_gross_pct'] for r in group if 'excess_gross_pct' in r]
                    summaries.append(dict(model_hash=model, horizon=horizon, score_band=f'{low}-{high}',
                        observations=len(group), positive_net_pct=100 * len(wins) / len(group),
                        average_net_pct=sum(returns) / len(returns),
                        average_positive_pct=sum(wins) / len(wins) if wins else None,
                        average_nonpositive_pct=sum(losses) / len(losses) if losses else None,
                        benchmark_pairs=len(excess), average_excess_pct=sum(excess) / len(excess) if excess else None,
                        worst_adverse_excursion_pct=min(r['adverse_excursion_pct'] for r in group)))
    save_json(state / 'validation_summary.json', summaries)
    report_rows = snapshot['rows'] if snapshot else rows
    ranked = sorted((r for r in report_rows if r['score'] is not None), key=lambda r: r['score'], reverse=True)
    counts = {status: sum(r['status'] == status for r in results) for status in sorted({r['status'] for r in results})}
    lines = ['# OFTS daily research', '', f'Market session: {target}',
             f'Selected: {len(selected)}; refreshed: {sum(audit[s]["status"] == "FRESH" for s in selected)}; refresh errors: {len(control["retry"])}',
             f'Qualified prediction cohorts saved: {len(snapshots)}; current coverage: {fresh_count}/{len(selected)}',
             f'Outcome counts: {counts}',
             'Production approval: NO. These are quality scores, not BUY signals.',
             'Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.',
             'Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.', '',
             '| Symbol | Score | Classification | Cycle sessions | Median swing | Confidence |',
             '|---|---:|---|---:|---:|---|']
    lines += [f'| {r["symbol"]} | {r["score"]:.3f} | {r["classification"]} | '
              f'{r.get("cycle", {}).get("cycle_sessions") or "n/a"} | '
              f'{r.get("cycle", {}).get("median_swing_pct") or "n/a"} | '
              f'{r.get("cycle", {}).get("confidence", "n/a")} |' for r in ranked[:25]]
    lines += ['', '## Mature outcomes by score and horizon', '```json', json.dumps(summaries, indent=2), '```']
    lines += ['', '## Refresh failures'] + [f'- {s}: {audit[s]["error"]}' for s in control['retry']]
    atomic(state / 'REPORT.md', ('\n'.join(lines) + '\n').encode())
    print('\n'.join(lines), flush=True)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as f:
            f.write('\n'.join(lines) + '\n')
    if not any(audit[s]['status'] == 'FRESH' for s in selected):
        raise SystemExit('NO_FRESH_SYMBOLS; state saved, run failed')


if __name__ == '__main__':
    main()
