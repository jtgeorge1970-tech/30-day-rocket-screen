"""Deterministic, restart-safe accounting for frozen OFTS research signals."""
from datetime import datetime, timezone
import json
from statistics import median


def _load(path, default):
    return json.loads(path.read_text()) if path.exists() else default


def _save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.tmp')
    tmp.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')
    tmp.replace(path)


def load_complete_signal_snapshots(directory):
    """Choose one complete immutable snapshot per date, preferring recovery files."""
    chosen = {}
    for path in sorted(directory.glob('*.json')):
        snapshot = _load(path, {})
        rows = snapshot.get('rows', [])
        complete = bool(rows) and all(
            row.get('signal', {}).get('state') in {'BUY', 'SELL', 'NO_TRADE'}
            for row in rows)
        if not complete or not snapshot.get('asof'):
            continue
        asof = snapshot['asof']
        if asof not in chosen or path.stem.endswith('-qualified'):
            chosen[asof] = snapshot
    return [chosen[date] for date in sorted(chosen)]


def active_ledger_symbols(state):
    ledger = _load(state / 'cycle_ledger.json', {})
    return sorted({p['symbol'] for p in ledger.get('positions', [])
                   if p.get('status') in {'PENDING_ENTRY', 'OPEN', 'OPEN_PENDING_EXIT'}})


def _cycle_class(trade):
    sessions = (trade.get('entry_cycle') or {}).get('cycle_sessions')
    if sessions is None:
        return 'UNKNOWN'
    if sessions <= 10:
        return 'FAST_1_TO_10'
    if sessions <= 25:
        return 'MEDIUM_11_TO_25'
    return 'SLOW_OVER_25'


def build_cycle_report_card(ledger):
    """Compare cycle speeds fairly without treating research states as advice."""
    trades = [trade for trade in ledger.get('trades', []) if trade.get('status') == 'CLOSED']
    groups = {}
    for label in sorted({_cycle_class(trade) for trade in trades}):
        group = [trade for trade in trades if _cycle_class(trade) == label]
        returns = [float(trade['net_assumed_return_pct']) for trade in group]
        holds = [int(trade['holding_sessions']) for trade in group]
        captures = [float(trade['captured_observed_swing_pct']) for trade in group
                    if trade.get('captured_observed_swing_pct') is not None]
        missed = [float(trade['missed_observed_swing_pct']) for trade in group
                  if trade.get('missed_observed_swing_pct') is not None]
        excess = [float(trade['excess_gross_pct']) for trade in group
                  if trade.get('excess_gross_pct') is not None]
        total_sessions = sum(holds)
        groups[label] = dict(
            trades=len(group), positive_net_trades=sum(value > 0 for value in returns),
            net_win_rate_pct=100 * sum(value > 0 for value in returns) / len(group),
            mean_net_return_pct=sum(returns) / len(group),
            median_net_return_pct=median(returns),
            total_holding_sessions=total_sessions,
            capital_time_efficiency_pct_per_20_sessions=(
                20 * sum(returns) / total_sessions if total_sessions else None),
            average_captured_observed_swing_pct=(
                sum(captures) / len(captures) if captures else None),
            average_missed_observed_swing_pct=(
                sum(missed) / len(missed) if missed else None),
            benchmark_pairs=len(excess),
            average_excess_gross_pct=sum(excess) / len(excess) if excess else None,
            review_trades=sum('review' in trade for trade in group))
    return dict(
        status='READY' if trades else 'AWAITING_CLOSED_FORWARD_TRADES',
        production_approved=False,
        methodology=('Cycle classes use the point-in-time entry fingerprint. Capital-time efficiency '
                     'is total net percentage return divided by total holding sessions, scaled to 20 sessions; '
                     'it is descriptive, not an annualized or portfolio return.'),
        closed_trades=len(trades), groups=groups)


def rebuild_cycle_ledger(state, histories, schedule, roundtrip_cost_pct=0.20):
    """Rebuild positions/trades from immutable signals; execution is next-session open.

    Rebuilding makes restarts idempotent and avoids mutable event-consumption flags.
    No position is filled until its next-session open exists in saved market data.
    """
    snapshots = load_complete_signal_snapshots(state / 'signals')
    dates = [str(d.date()) for d in schedule.index]
    date_index = {date: i for i, date in enumerate(dates)}
    positions = {}
    trades = []
    exceptions = []

    for snapshot in snapshots:
        signal_date = snapshot['asof']
        if signal_date not in date_index or date_index[signal_date] + 1 >= len(dates):
            exceptions.append(dict(signal_date=signal_date, reason='NO_NEXT_SESSION_IN_CALENDAR'))
            continue
        execution_date = dates[date_index[signal_date] + 1]
        for row in sorted(snapshot['rows'], key=lambda item: item['symbol']):
            signal = row['signal']['state']
            if signal == 'NO_TRADE':
                continue
            symbol = row['symbol']
            bars = {bar['date']: bar for bar in histories.get(symbol, [])}
            execution_bar = bars.get(execution_date)

            if signal == 'BUY':
                if symbol in positions:
                    exceptions.append(dict(symbol=symbol, signal_date=signal_date,
                                           signal='BUY', reason='POSITION_ALREADY_EXISTS'))
                    continue
                position = dict(symbol=symbol, status='PENDING_ENTRY',
                                entry_signal_date=signal_date,
                                planned_entry_date=execution_date,
                                entry_score=row.get('score'),
                                cycle=row.get('cycle'),
                                model_hash=snapshot.get('model_hash'))
                if execution_bar:
                    position.update(status='OPEN', entry_date=execution_date,
                                    entry_open=float(execution_bar['open']))
                positions[symbol] = position
                continue

            position = positions.get(symbol)
            if not position:
                exceptions.append(dict(symbol=symbol, signal_date=signal_date,
                                       signal='SELL', reason='NO_OPEN_POSITION'))
                continue
            if position['status'] == 'PENDING_ENTRY':
                exceptions.append(dict(symbol=symbol, signal_date=signal_date,
                                       signal='SELL', reason='ENTRY_NOT_EXECUTABLE'))
                continue
            if not execution_bar:
                position.update(status='OPEN_PENDING_EXIT', exit_signal_date=signal_date,
                                planned_exit_date=execution_date)
                continue

            entry_date = position['entry_date']
            entry_open = float(position['entry_open'])
            exit_open = float(execution_bar['open'])
            interval_dates = dates[date_index[entry_date]:date_index[execution_date] + 1]
            interval = [bars.get(date) for date in interval_dates]
            gross = 100 * (exit_open / entry_open - 1)
            trade = dict(symbol=symbol, status='CLOSED',
                         entry_signal_date=position['entry_signal_date'], entry_date=entry_date,
                         entry_open=entry_open, exit_signal_date=signal_date,
                         exit_date=execution_date, exit_open=exit_open,
                         holding_sessions=date_index[execution_date] - date_index[entry_date],
                         gross_return_pct=gross,
                         net_assumed_return_pct=gross - roundtrip_cost_pct,
                         roundtrip_cost_pct=roundtrip_cost_pct,
                         entry_score=position.get('entry_score'),
                         entry_cycle=position.get('cycle'),
                         model_hash=position.get('model_hash'))
            if any(bar is None for bar in interval):
                trade['review'] = 'MISSING_SESSIONS'
            else:
                lows = [float(bar['low']) for bar in interval]
                highs = [float(bar['high']) for bar in interval]
                trade['adverse_excursion_pct'] = 100 * (min(lows) / entry_open - 1)
                trade['best_high_return_pct'] = 100 * (max(highs) / entry_open - 1)
                best_swing = max(
                    100 * (max(highs[i:]) / lows[i] - 1) for i in range(len(interval)))
                trade['observed_ordered_swing_pct'] = best_swing
                trade['captured_observed_swing_pct'] = (
                    100 * gross / best_swing if best_swing > 0 else None)
                trade['missed_observed_swing_pct'] = best_swing - max(gross, 0)
                if any(float(bar.get('split') or 0) for bar in interval):
                    trade['review'] = 'CORPORATE_ACTION'
            spy = {bar['date']: bar for bar in histories.get('SPY', [])}
            if entry_date in spy and execution_date in spy:
                benchmark = 100 * (float(spy[execution_date]['open']) /
                                   float(spy[entry_date]['open']) - 1)
                trade['benchmark_price_return_pct'] = benchmark
                trade['excess_gross_pct'] = gross - benchmark
            trades.append(trade)
            del positions[symbol]

    ledger = dict(
        generated_at=datetime.now(timezone.utc).isoformat(),
        methodology='Frozen close-confirmed BUY/SELL; hypothetical next-session open; 0.20% round-trip cost',
        production_approved=False,
        positions=sorted(positions.values(), key=lambda p: p['symbol']),
        trades=trades,
        exceptions=exceptions,
        summary=dict(
            complete_signal_cohorts=len(snapshots),
            pending_entries=sum(p['status'] == 'PENDING_ENTRY' for p in positions.values()),
            open_positions=sum(p['status'] in {'OPEN', 'OPEN_PENDING_EXIT'} for p in positions.values()),
            closed_trades=len(trades),
            benchmark_pairs=sum('benchmark_price_return_pct' in t for t in trades),
            review_trades=sum('review' in t for t in trades)))
    _save(state / 'cycle_ledger.json', ledger)
    _save(state / 'cycle_report_card.json', build_cycle_report_card(ledger))
    return ledger
