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
from ofts.research.security_regimes import post_identity_bars
from ofts.research.swing_health import recent_swing_health
from ofts.research.recent_viability import recent_swing_viability
from ofts.cycle_ledger import active_ledger_symbols, rebuild_cycle_ledger, build_cycle_report_card

ROOT = Path(__file__).resolve().parents[1]
WATCH = 'HNRG CHTR FUBO EPOW WULF HLIT JACK TGS SPGI CSIQ XPRO SFM DTIL TBLA FWRG NYAX OWLT SRAD ATGL FMC LE MESO NX MBLY IDR'.split()
HORIZONS = (5, 10, 20, 30, 60)
FIELDS = ['date', 'open', 'high', 'low', 'close', 'volume', 'split']
MIN_FRESH_COHORT = 100
DATA_FAILURES = {'STALE_DATA', 'DATA_ERROR', 'INSUFFICIENT_HISTORY', 'INSUFFICIENT_POST_REGIME_HISTORY'}


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



def score_interpretation(rows):
    """Expose score scale and evidence gate without inventing a BUY cutoff."""
    scores = [float(row['score']) for row in rows if row.get('score') is not None]
    bands = {'BELOW_40': 0, '40_TO_49_999': 0, '50_TO_59_999': 0,
             '60_TO_69_999': 0, '70_TO_79_999': 0, '80_TO_89_999': 0,
             '90_TO_100': 0}
    for score in scores:
        key = ('BELOW_40' if score < 40 else '40_TO_49_999' if score < 50 else
               '50_TO_59_999' if score < 60 else '60_TO_69_999' if score < 70 else
               '70_TO_79_999' if score < 80 else '80_TO_89_999' if score < 90 else
               '90_TO_100')
        bands[key] += 1
    return dict(theoretical_scale_min=0, theoretical_scale_max=100,
                observed_min=min(scores) if scores else None,
                observed_max=max(scores) if scores else None,
                scored_rows=len(scores), distribution=bands,
                validated_buy_threshold=None,
                system_actionability_gate='RESEARCH_ONLY_NO_GO',
                gate_reason='OUT_OF_SAMPLE_PREDICTIVE_VALIDATION_NOT_VERIFIED')

def signal_snapshot_complete(snapshot):
    rows = snapshot.get('rows', [])
    return bool(rows) and all(r.get('signal', {}).get('state') in {'BUY', 'SELL', 'NO_TRADE'} for r in rows)


def current_signal_state(closes, threshold, classification):
    """Close-confirmed state for hypothetical next-open execution."""
    if classification != 'CANDIDATE':
        return dict(state='NO_TRADE', reason=classification)
    turns = detect_turns(closes, threshold)
    if not turns:
        return dict(state='NO_TRADE', reason='NO_CONFIRMED_TURN')
    latest = turns[-1]
    prior_turns = detect_turns(closes[:-1], threshold) if len(closes) > 1 else []
    if latest in prior_turns:
        return dict(state='NO_TRADE', reason='NO_NEW_CONFIRMED_TURN',
                    last_pivot_type=latest[1], last_pivot_index=latest[0])
    return dict(state='BUY' if latest[1] == 'L' else 'SELL',
                reason='NEW_CONFIRMED_REVERSAL', pivot_type=latest[1],
                pivot_index=latest[0], confirmation_index=len(closes)-1,
                confirmation_lag_bars=len(closes)-1-latest[0])


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
            elif prediction['classification'] in DATA_FAILURES:
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
    (state / 'fingerprints').mkdir(exist_ok=True)
    (state / 'signals').mkdir(exist_ok=True)
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
    refresh_symbols = list(dict.fromkeys(selected + sorted(pending) + active_ledger_symbols(state) + ['SPY']))
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
            try:
                # Do not blend a predecessor SPAC's trading history with a
                # newly listed operating-company security (verified event dates).
                eligible_bars, regime = post_identity_bars(symbol, bars, target)
                if regime:
                    row.update(raw_bars=len(bars), bars=len(eligible_bars),
                               regime_start=regime['start'], regime_source=regime['source'])
                if len(eligible_bars) < 180:
                    row['classification'] = ('INSUFFICIENT_POST_REGIME_HISTORY'
                                             if regime else 'INSUFFICIENT_HISTORY')
                else:
                    # Existing evaluate implementation remains byte-for-byte unchanged.
                    series = [[float(r[k]) for r in eligible_bars] for k in ('high', 'low', 'close')]
                    result = evaluate(*series)
                    row.update(score=result.get('candidate_score'), classification=result['status'])
                    if result.get('candidate_score') is not None:
                        row['cycle'] = cycle_fingerprint(series[2], result['threshold_pct'], result['structural'])
                        # Experimental diagnostic; original BUY/SELL research
                        # signal and v2.3 score remain unchanged.
                        row['swing_health'] = recent_swing_health(series[2], result['threshold_pct'])
                        row['recent_viability'] = recent_swing_viability(series[2], result['threshold_pct'])
                        row['experimental_research_entry'] = (
                            'REVIEW' if result['status'] == 'CANDIDATE'
                            and row['swing_health']['proposed_entry'] == 'REVIEW'
                            and row['recent_viability']['proposed_entry'] == 'REVIEW'
                            else 'NO_TRADE')
                    row['signal'] = current_signal_state(series[2], result.get('threshold_pct', 6), result['status'])
            except (ValueError, TypeError, KeyError) as exc:
                row.update(classification='DATA_ERROR', error=str(exc))
        row.setdefault('signal', dict(state='NO_TRADE', reason=row['classification']))
        rows.append(row)
    model_hash = hashlib.sha256(b''.join((ROOT / p).read_bytes() for p in
                               ['ofts/research/v23_replacement.py', 'ofts/research/candidate_components.py',
                                 'ofts/research/security_regimes.py', 'ofts/research/swing_health.py',
                                  'ofts/research/recent_viability.py'])).hexdigest()
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
    fingerprint_snapshot = None
    signal_snapshot = None
    if fresh_count >= required_fresh:
        fingerprint_snapshot = frozen_snapshot(
            state / 'fingerprints' / (target + '.json'),
            dict(asof=target, recorded_at=datetime.now(timezone.utc).isoformat(),
                 model_hash=model_hash, rows=rows,
                 note='Point-in-time research fingerprints; not production BUY/SELL signals'))
        signal_candidate = dict(asof=target, recorded_at=datetime.now(timezone.utc).isoformat(),
                                execution='Hypothetical next-session open', model_hash=model_hash,
                                rows=rows, production_approved=False,
                                note='Close-confirmed research states; not brokerage instructions')
        signal_path = state / 'signals' / (target + '.json')
        if signal_path.exists() and not signal_snapshot_complete(load_json(signal_path, {})):
            signal_path = state / 'signals' / (target + '-qualified.json')
        signal_snapshot = frozen_snapshot(signal_path, signal_candidate)
    histories = {s: read_history(state, s) for s in set(refresh_symbols) | {r['symbol'] for s in snapshots for r in s['rows']}}
    results = [r for s in snapshots for r in outcomes(s, histories, schedule)]
    save_json(state / 'outcomes.json', results)
    cycle_ledger = rebuild_cycle_ledger(state, histories, schedule)
    cycle_card = build_cycle_report_card(cycle_ledger)
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
    report_rows = signal_snapshot['rows'] if signal_snapshot else (fingerprint_snapshot['rows'] if fingerprint_snapshot else (snapshot['rows'] if snapshot else rows))
    ranked = sorted((r for r in report_rows if r['score'] is not None and r['classification'] == 'CANDIDATE'), key=lambda r: r['score'], reverse=True)
    score_status = score_interpretation(report_rows)
    counts = {status: sum(r['status'] == status for r in results) for status in sorted({r['status'] for r in results})}
    lines = ['# OFTS daily research', '', f'Market session: {target}',
             f'Selected: {len(selected)}; refreshed: {sum(audit[s]["status"] == "FRESH" for s in selected)}; refresh errors: {len(control["retry"])}',
             f'Qualified prediction cohorts saved: {len(snapshots)}; current coverage: {fresh_count}/{len(selected)}',
             f'Outcome counts: {counts}',
             f'Cycle fingerprints saved: {sum("cycle" in r for r in report_rows)}/{len(report_rows)}',
             f'Signal states: BUY={sum(r.get("signal", {}).get("state") == "BUY" for r in report_rows)}, '
             f'SELL={sum(r.get("signal", {}).get("state") == "SELL" for r in report_rows)}, '
             f'NO_TRADE={sum(r.get("signal", {}).get("state") == "NO_TRADE" for r in report_rows)}',
             f'Cycle ledger: pending entries={cycle_ledger["summary"]["pending_entries"]}; '
             f'open positions={cycle_ledger["summary"]["open_positions"]}; '
             f'closed trades={cycle_ledger["summary"]["closed_trades"]}; '
             f'SPY pairs={cycle_ledger["summary"]["benchmark_pairs"]}',
             f'Cycle-speed report card: {cycle_card["status"]}; '
             f'closed forward trades={cycle_card["closed_trades"]}; '
             f'groups={list(cycle_card["groups"])}',
             f'Score scale: theoretical 0-100; observed '
             f'{score_status["observed_min"]:.3f}-{score_status["observed_max"]:.3f}; '
             f'validated BUY threshold=NONE',
             f'Score distribution: {score_status["distribution"]}',
             f'System actionability gate: {score_status["system_actionability_gate"]}; '
             f'{score_status["gate_reason"]}',
             'Production approval: NO. These are quality scores, not BUY signals.',
             'Experimental recent viability v0.4: last three minor swings, last three UP legs,'
             ' old-outlier dominance, peak/trough spacing 10-40 sessions, and hypothetical capture after costs; NOT validated.',
             f'Experimental viable REVIEW={sum(r.get("experimental_research_entry") == "REVIEW" for r in report_rows)}; '
             f'viability NO_TRADE={sum(r.get("recent_viability", {}).get("proposed_entry") == "NO_TRADE" for r in report_rows)}',
             'Experimental swing-health v0.1: last-four-leg stability and'
             ' lower-high/lower-low deterioration (NOT validated for trading).',
             f'Experimental swing-health NO_TRADE={sum(r.get("swing_health", {}).get("proposed_entry") == "NO_TRADE" for r in report_rows)}; '
             f'REVIEW={sum(r.get("swing_health", {}).get("proposed_entry") == "REVIEW" for r in report_rows)}; '
             f'INSUFFICIENT={sum(r.get("swing_health", {}).get("state") == "INSUFFICIENT" for r in report_rows)}',
             'Forward returns use next-session open, exclude dividends, and assume 0.20% round-trip costs.',
             'Overlapping observations are not independent trades. No portfolio win rate or drawdown claim.', '',
             '| Symbol | Score | Classification | Legacy signal | Swing health | Last 3 swings | Last 3 UP % | >=5% count | Repeatability | Peak gaps (sessions) | Trough gaps (sessions) | Cycle timing | Latest UP % | Old avg | Viability | Experimental review | Highs | Lows | Cycle sessions | Median swing | Confidence |',
             '|---|---:|---|---|---:|---|---:|---|---:|---:|---|---|---|---|---:|---:|---|']
    lines += [f'| {r["symbol"]} | {r["score"]:.3f} | {r["classification"]} | '
              f'{r.get("signal", {}).get("state", "NO_TRADE")} | '
              f'{r.get("swing_health", {}).get("state", "n/a")} | '
              f'{r.get("recent_viability", {}).get("last_three_median_swing_pct") or "n/a"} | '
              f'{[round(v, 2) for v in r.get("recent_viability", {}).get("last_three_up_pct", [])]} | '
              f'{r.get("recent_viability", {}).get("repeated_up_pass_count", "n/a")} | '
              f'{r.get("recent_viability", {}).get("recent_up_repeatability", "n/a")} | '
              f'{r.get("recent_viability", {}).get("last_three_peak_to_peak_sessions", [])} | '
              f'{r.get("recent_viability", {}).get("last_three_trough_to_trough_sessions", [])} | '
              f'{r.get("recent_viability", {}).get("cycle_timing_pass", "n/a")} | '
              f'{r.get("recent_viability", {}).get("last_up_pct") or "n/a"} | '
              f'{r.get("recent_viability", {}).get("historical_mean_swing_pct") or "n/a"} | '
              f'{r.get("recent_viability", {}).get("state", "n/a")} | '
              f'{r.get("experimental_research_entry", "NO_TRADE")} | '
              f'{r.get("swing_health", {}).get("high_progression", "n/a")} | '
              f'{r.get("swing_health", {}).get("low_progression", "n/a")} | '
              f'{r.get("cycle", {}).get("cycle_sessions") or "n/a"} | '
              f'{r.get("cycle", {}).get("median_swing_pct") or "n/a"} | '
              f'{r.get("cycle", {}).get("confidence", "n/a")} |' for r in ranked[:25]]
    # This separate challenger shortlist NEVER replaces the original quality
    # ranking, signal ledger or frozen historical predictions.
    review = [r for r in ranked if r.get('experimental_research_entry') == 'REVIEW']
    lines += ['', '## Experimental recent-swing review shortlist (NOT BUY signals)',
              f'Count: {len(review)} of {len(ranked)} scored CANDIDATE names',
              '| Symbol | Quality score | Last 3 swings % | Last 3 UP % | >=5% count | Peak gaps | Trough gaps | Historical avg % |',
              '|---|---:|---:|---|---:|---|---|---:|']
    lines += [f'| {r["symbol"]} | {r["score"]:.3f} | '
              f'{r["recent_viability"].get("last_three_median_swing_pct") or "n/a"} | '
              f'{[round(v, 2) for v in r["recent_viability"].get("last_three_up_pct", [])]} | '
              f'{r["recent_viability"].get("repeated_up_pass_count", "n/a")} | '
              f'{r["recent_viability"].get("last_three_peak_to_peak_sessions", [])} | '
              f'{r["recent_viability"].get("last_three_trough_to_trough_sessions", [])} | '
              f'{r["recent_viability"].get("historical_mean_swing_pct") or "n/a"} |'
              for r in review[:25]]
    lines += ['', '## Mature outcomes by score and horizon', '```json', json.dumps(summaries, indent=2), '```']
    lines += ['', '## Identity-boundary exclusions (current processing; prior snapshots immutable)']
    lines += [f'- {r["symbol"]}: {r["classification"]}; '
              f'post-event bars={r["bars"]}; raw bars={r["raw_bars"]}; '
              f'event={r["regime_start"]}; source={r["regime_source"]}'
              for r in rows if r.get('regime_start')]
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
