"""Cycle-adjusted next-open BUY-to-SELL execution audit.

Research only. Entry and exit decisions use confirmed pivots available by the
prior close. A chronological 70/30 split and 20-session embargo keep training
selection separate from test trades. No brokerage authorization.
"""
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean, median

ROOT = Path(__file__).resolve().parents[2]
BARS = ROOT / "ofts/research/extended_history_ohlcv.csv"
EVENTS = ROOT / "ofts/validation/extended_fingerprint_events.csv"
OUT = ROOT / "ofts/validation/cycle_execution_trades.csv"
SUMMARY = ROOT / "ofts/validation/cycle_execution_summary.txt"


def grouped(path):
    out = defaultdict(list)
    with path.open(newline="") as f:
        for row in csv.DictReader(f):
            out[row["symbol"]].append(row)
    return out


def protected_return(bars, entry_idx, exit_idx, stop_pct=None, trail_pct=None):
    entry = float(bars[entry_idx]["open"])
    fixed = entry * (1 - stop_pct / 100) if stop_pct else None
    prior_peak = entry
    for i in range(entry_idx, exit_idx + 1):
        day = bars[i]
        op, low, high = map(float, (day["open"], day["low"], day["high"]))
        level = fixed
        if trail_pct is not None:
            trail = prior_peak * (1 - trail_pct / 100)
            level = max(level or trail, trail)
        if level is not None:
            if op <= level:
                return 100 * (op / entry - 1)
            if low <= level:
                return 100 * (level / entry - 1)
        # Today's high can tighten only tomorrow's stop; this avoids assuming
        # whether today's high occurred before today's low.
        prior_peak = max(prior_peak, high)
    return 100 * (float(bars[exit_idx]["open"]) / entry - 1)


def main():
    bars = grouped(BARS)
    events = grouped(EVENTS)
    for rows in bars.values():
        rows.sort(key=lambda r: r["date"])
    trades = []
    eligible_symbols = 0
    for symbol, all_events in sorted(events.items()):
        all_events.sort(key=lambda r: int(r["confirmation_index"]))
        split = int(0.7 * len(all_events))
        if split < 8 or split >= len(all_events):
            continue
        boundary = int(all_events[split]["confirmation_index"])
        train_buys = [
            float(r["future_20d_pct"]) for r in all_events[:split]
            if r["pivot_type"] == "L"
            and int(r["confirmation_index"]) + 20 < boundary
        ]
        if len(train_buys) < 8 or mean(train_buys) <= 0:
            continue
        eligible_symbols += 1
        test = all_events[split:]
        b = bars.get(symbol, [])
        last_exit = -1
        for pos, buy in enumerate(test):
            if buy["pivot_type"] != "L":
                continue
            sell = next((r for r in test[pos + 1:]
                         if r["pivot_type"] == "H"
                         and int(r["confirmation_index"]) > int(buy["confirmation_index"])), None)
            if sell is None:
                continue
            buy_confirm = int(buy["confirmation_index"])
            sell_confirm = int(sell["confirmation_index"])
            entry_idx, exit_idx = buy_confirm + 1, sell_confirm + 1
            if entry_idx <= last_exit or exit_idx >= len(b) or entry_idx >= exit_idx:
                continue
            entry = float(b[entry_idx]["open"])
            exit_open = float(b[exit_idx]["open"])
            gross = 100 * (exit_open / entry - 1)
            ideal = 100 * (float(sell["pivot_price"]) / float(buy["pivot_price"]) - 1)
            suspect = any(
                float(b[j]["close"]) / float(b[j - 1]["close"]) < 0.55
                or float(b[j]["close"]) / float(b[j - 1]["close"]) > 1.8
                for j in range(entry_idx, exit_idx + 1)
            )
            trades.append(dict(
                symbol=symbol,
                buy_confirmation_date=b[buy_confirm]["date"],
                entry_date=b[entry_idx]["date"],
                sell_confirmation_date=b[sell_confirm]["date"],
                exit_date=b[exit_idx]["date"],
                entry_open=round(entry, 6),
                exit_open=round(exit_open, 6),
                hold_sessions=exit_idx - entry_idx,
                ideal_pivot_swing_pct=round(ideal, 6),
                gross_cycle_return_pct=round(gross, 6),
                captured_swing_pct=round(100 * gross / ideal, 6) if ideal > 0 else "",
                net_20bp_pct=round(gross - 0.20, 6),
                fixed_stop_12_pct=round(protected_return(b, entry_idx, exit_idx, stop_pct=12), 6),
                trailing_stop_12_pct=round(protected_return(b, entry_idx, exit_idx, trail_pct=12), 6),
                possible_split_window=suspect,
                production_approved=False,
            ))
            last_exit = exit_idx
    if not trades:
        raise RuntimeError("NO_CYCLE_TRADES; preserve prior evidence and fail closed")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(trades[0]))
        writer.writeheader()
        writer.writerows(trades)
    clean = [r for r in trades if not r["possible_split_window"]]
    values = [r["net_20bp_pct"] for r in clean]
    captures = [r["captured_swing_pct"] for r in clean if r["captured_swing_pct"] != ""]
    lines = [
        "OFTS CYCLE EXECUTION AUDIT — RESEARCH ONLY",
        f"Training-selected symbols: {eligible_symbols}",
        f"Chronological nonoverlapping cycle trades: {len(trades)}",
        f"Clean trades excluding possible split windows: {len(clean)}",
        f"Positive net trades: {sum(v > 0 for v in values)}/{len(values)}",
        f"Net win rate pct: {100 * sum(v > 0 for v in values) / len(values):.3f}",
        f"Mean net cycle return pct: {mean(values):.3f}",
        f"Median net cycle return pct: {median(values):.3f}",
        f"Mean captured ideal swing pct: {mean(captures):.3f}" if captures else "Mean captured ideal swing pct: n/a",
        f"Median holding sessions: {median(r['hold_sessions'] for r in clean):.3f}",
        f"Mean fixed 12pct stop return pct: {mean(r['fixed_stop_12_pct'] for r in clean):.3f}",
        f"Mean trailing 12pct stop return pct: {mean(r['trailing_stop_12_pct'] for r in clean):.3f}",
        "Entry: next session open after confirmed low reversal.",
        "Exit: next session open after later confirmed high reversal.",
        "Chronological 70/30 split; 20-session training embargo; no overlapping trades per symbol.",
        "SPY benchmark: not available in this historical cohort; forward daily audits retain SPY comparison.",
        "Production approval: NO",
    ]
    SUMMARY.write_text("\n".join(lines) + "\n")
    print(SUMMARY.read_text())


if __name__ == "__main__":
    main()
