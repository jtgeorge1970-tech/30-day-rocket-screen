"""Strict 30-session extreme-winner cohort and continuation study.

The initial current-universe/Yahoo dataset is exploratory. It does not contain
delisted securities or point-in-time fundamentals and cannot prove an edge.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

import extreme_winner_engine as engine


OUT = Path(os.environ.get("WINNER_STUDY_OUTPUT", "study_output"))
LOOKBACK_SESSIONS = 30
EVENT_COOLDOWN_SESSIONS = 10
MIN_EVENT_HISTORY = 253
HORIZONS = (5, 10, 20, 30)
TARGETS = (10, 20, 30)

EVENT_COLUMNS = [
    "ticker", "name", "event_date", "event_type", "event_open", "event_high",
    "event_low", "event_close", "day_return", "five_day_return", "event_gap",
    "event_intraday_return", "event_close_location", "event_peak_retention",
    "event_volume_ratio_20", "event_dollar_volume_20", "event_atr14_pct",
    "pre_event_return_20", "event_return_20", "new_52w_high", "spy_return_20",
    "event_relative_spy_20", "spy_above_200dma", "historical_catalyst_status",
    "historical_supply_status", "next_open",
    "available_forward_sessions", "primary_outcome", "stop_day",
    "observed_mfe", "observed_mae",
] + [f"target_{target}_day" for target in TARGETS] + [
    f"return_{h}" for h in HORIZONS
] + [f"mfe_{h}" for h in HORIZONS] + [f"mae_{h}" for h in HORIZONS] + [
    "trail_7_return", "trail_7_status", "trail_10_return", "trail_10_status"
]


def _trailing_result(future, entry, activation_day, disaster_stop_day, trail_pct):
    """Conservative daily-bar trail activated after +10%.

    A trail starts on the session after the activation bar because the order of
    intraday high/low observations on the activation bar is unknowable from
    daily data. The activation bar therefore never receives a favorable assumed
    sequence.
    """
    if not np.isnan(disaster_stop_day) and (
        np.isnan(activation_day) or disaster_stop_day < activation_day
    ):
        stop_index = int(disaster_stop_day) - 1
        fill = min(float(future.Open.iloc[stop_index]), entry * 0.90)
        return float(fill / entry - 1), "DISASTER_STOP"
    if (
        not np.isnan(disaster_stop_day)
        and not np.isnan(activation_day)
        and disaster_stop_day == activation_day
    ):
        return np.nan, "AMBIGUOUS_ACTIVATION_BAR"
    if np.isnan(activation_day):
        if len(future) >= 30:
            return float(future.Close.iloc[29] / entry - 1), "NO_ACTIVATION_TIME_EXIT"
        return np.nan, "OPEN"
    activation_index = int(activation_day) - 1
    peak = float(future.High.iloc[activation_index])
    for idx in range(activation_index + 1, len(future)):
        stop = peak * (1 - trail_pct)
        if float(future.Low.iloc[idx]) <= stop:
            fill = min(float(future.Open.iloc[idx]), stop)
            return float(fill / entry - 1), "TRAIL_EXIT"
        peak = max(peak, float(future.High.iloc[idx]))
    if len(future) >= 30:
        return float(future.Close.iloc[29] / entry - 1), "TIME_EXIT_30"
    return np.nan, "OPEN"


def outcome(frame, event_idx):
    future = frame.iloc[event_idx + 1:event_idx + 31].copy()
    empty = {
        "next_open": np.nan,
        "available_forward_sessions": 0,
        "primary_outcome": "OPEN",
        "stop_day": np.nan,
        "observed_mfe": np.nan,
        "observed_mae": np.nan,
        **{f"target_{target}_day": np.nan for target in TARGETS},
        **{f"return_{h}": np.nan for h in HORIZONS},
        **{f"mfe_{h}": np.nan for h in HORIZONS},
        **{f"mae_{h}": np.nan for h in HORIZONS},
        "trail_7_return": np.nan,
        "trail_7_status": "OPEN",
        "trail_10_return": np.nan,
        "trail_10_status": "OPEN",
    }
    if future.empty:
        return empty
    entry = float(future.Open.iloc[0])
    target_days = {}
    for target in TARGETS:
        hits = np.flatnonzero(future.High.to_numpy() >= entry * (1 + target / 100))
        target_days[target] = int(hits[0] + 1) if len(hits) else np.nan
    stop_hits = np.flatnonzero(future.Low.to_numpy() <= entry * 0.90)
    stop_day = int(stop_hits[0] + 1) if len(stop_hits) else np.nan
    target_day = target_days[10]
    if not np.isnan(target_day) and not np.isnan(stop_day):
        if target_day < stop_day:
            label = "WIN_10_BEFORE_10"
        elif stop_day < target_day:
            label = "LOSS_10_BEFORE_10"
        else:
            label = "AMBIGUOUS_SAME_BAR"
    elif not np.isnan(target_day):
        label = "WIN_10_BEFORE_10"
    elif not np.isnan(stop_day):
        label = "LOSS_10_BEFORE_10"
    elif len(future) >= 30:
        label = "NEITHER_WITHIN_30"
    else:
        label = "OPEN"
    result = {
        "next_open": entry,
        "available_forward_sessions": len(future),
        "primary_outcome": label,
        "stop_day": stop_day,
        "observed_mfe": float(future.High.max() / entry - 1),
        "observed_mae": float(future.Low.min() / entry - 1),
        **{f"target_{target}_day": target_days[target] for target in TARGETS},
    }
    for horizon in HORIZONS:
        complete = len(future) >= horizon
        window = future.iloc[:horizon]
        result[f"return_{horizon}"] = float(window.Close.iloc[-1] / entry - 1) if complete else np.nan
        result[f"mfe_{horizon}"] = float(window.High.max() / entry - 1) if complete else np.nan
        result[f"mae_{horizon}"] = float(window.Low.min() / entry - 1) if complete else np.nan
    for points, fraction in [(7, 0.07), (10, 0.10)]:
        value, status = _trailing_result(future, entry, target_day, stop_day, fraction)
        result[f"trail_{points}_return"] = value
        result[f"trail_{points}_status"] = status
    return result


def event_rows(frame, ticker, name="", spy_close=None):
    frame = frame.dropna(subset=["Open", "High", "Low", "Close", "Volume"]).copy()
    if len(frame) < MIN_EVENT_HISTORY:
        return []
    close, high, low, open_, volume = frame.Close, frame.High, frame.Low, frame.Open, frame.Volume
    day_return = close.pct_change()
    five_return = close / close.shift(5) - 1
    prior_volume = volume.shift(1).rolling(20, min_periods=20).mean()
    dollar_volume = (close * volume).shift(1).rolling(20, min_periods=20).mean()
    prior_52_high = high.shift(1).rolling(252, min_periods=252).max()
    true_range = pd.concat(
        [(high - low), (high - close.shift()).abs(), (low - close.shift()).abs()], axis=1
    ).max(axis=1)
    atr = true_range.shift(1).rolling(14, min_periods=14).mean()
    start = max(MIN_EVENT_HISTORY - 1, len(frame) - LOOKBACK_SESSIONS)
    rows, last_event_idx = [], -10_000
    for idx in range(start, len(frame)):
        one_day = day_return.iloc[idx] >= engine.ONE_DAY_EVENT
        five_day = five_return.iloc[idx] >= engine.FIVE_DAY_EVENT
        qualifies = (
            (one_day or five_day)
            and close.iloc[idx] >= engine.MIN_PRICE
            and dollar_volume.iloc[idx] >= engine.MIN_DOLLAR_VOLUME
        )
        if not bool(qualifies) or idx - last_event_idx < EVENT_COOLDOWN_SESSIONS:
            continue
        last_event_idx = idx
        prior_close = float(close.iloc[idx - 1])
        bar_range = max(float(high.iloc[idx] - low.iloc[idx]), 1e-9)
        peak_denominator = max(float(high.iloc[idx]) - prior_close, 1e-9)
        event_type = "BOTH" if one_day and five_day else ("ONE_DAY" if one_day else "FIVE_DAY")
        event_return_20 = float(close.iloc[idx] / close.iloc[idx - 20] - 1)
        spy_return_20 = np.nan
        spy_above_200dma = np.nan
        if spy_close is not None and len(spy_close):
            aligned_spy = spy_close.reindex(frame.index).ffill()
            if idx >= 20 and pd.notna(aligned_spy.iloc[idx]) and pd.notna(aligned_spy.iloc[idx - 20]):
                spy_return_20 = float(aligned_spy.iloc[idx] / aligned_spy.iloc[idx - 20] - 1)
            if idx >= 199 and aligned_spy.iloc[idx - 199:idx + 1].notna().all():
                spy_above_200dma = bool(aligned_spy.iloc[idx] >= aligned_spy.iloc[idx - 199:idx + 1].mean())
        row = {
            "ticker": ticker,
            "name": name,
            "event_date": frame.index[idx].date().isoformat(),
            "event_type": event_type,
            "event_open": float(open_.iloc[idx]),
            "event_high": float(high.iloc[idx]),
            "event_low": float(low.iloc[idx]),
            "event_close": float(close.iloc[idx]),
            "day_return": float(day_return.iloc[idx]),
            "five_day_return": float(five_return.iloc[idx]),
            "event_gap": float(open_.iloc[idx] / prior_close - 1),
            "event_intraday_return": float(close.iloc[idx] / open_.iloc[idx] - 1),
            "event_close_location": float((close.iloc[idx] - low.iloc[idx]) / bar_range),
            "event_peak_retention": float(np.clip((close.iloc[idx] - prior_close) / peak_denominator, 0, 1)),
            "event_volume_ratio_20": float(volume.iloc[idx] / max(float(prior_volume.iloc[idx]), 1e-9)),
            "event_dollar_volume_20": float(dollar_volume.iloc[idx]),
            "event_atr14_pct": float(atr.iloc[idx] / close.iloc[idx]),
            "pre_event_return_20": float(close.iloc[idx - 1] / close.iloc[idx - 21] - 1),
            "event_return_20": event_return_20,
            "new_52w_high": bool(high.iloc[idx] >= prior_52_high.iloc[idx]),
            "spy_return_20": spy_return_20,
            "event_relative_spy_20": event_return_20 - spy_return_20 if pd.notna(spy_return_20) else np.nan,
            "spy_above_200dma": spy_above_200dma,
            "historical_catalyst_status": "NOT_CLASSIFIED_REQUIRES_POINT_IN_TIME_NEWS",
            "historical_supply_status": "NOT_CLASSIFIED_REQUIRES_POINT_IN_TIME_FILINGS",
        }
        row.update(outcome(frame, idx))
        rows.append(row)
    return rows


def download_spy_history():
    data = engine.retry_yahoo(
        lambda: yf.download(
            "SPY", period="2y", interval="1d", auto_adjust=True, threads=False, progress=False, timeout=30
        ),
        "winner cohort SPY history",
        validator=engine._valid_download,
    )
    if data is None:
        raise RuntimeError("SPY history unavailable; refusing regime-blind cohort study")
    close = data["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]
    return pd.to_numeric(close, errors="coerce").dropna()


def download_history(tickers, name_map, spy_close):
    rows, failures = [], []
    for start in range(0, len(tickers), engine.PRICE_BATCH_SIZE):
        batch = tickers[start:start + engine.PRICE_BATCH_SIZE]
        data = engine.retry_yahoo(
            lambda b=batch: yf.download(
                b,
                period="2y",
                interval="1d",
                group_by="column",
                auto_adjust=True,
                threads=False,
                progress=False,
                timeout=30,
            ),
            f"winner cohort prices batch {start // engine.PRICE_BATCH_SIZE + 1}",
            validator=engine._valid_download,
        )
        if data is None:
            failures.extend(batch)
            continue
        for ticker in batch:
            try:
                frame = engine.ohlcv(data, ticker, batch)
                if len(frame) < MIN_EVENT_HISTORY:
                    continue
                rows.extend(event_rows(frame, ticker, name_map.get(ticker, ""), spy_close))
            except Exception as exc:
                print(f"Winner cohort skip {ticker}: {exc}", flush=True)
                failures.append(ticker)
        if (start // engine.PRICE_BATCH_SIZE + 1) % 10 == 0:
            print(f"Winner cohort progress: {min(start + engine.PRICE_BATCH_SIZE, len(tickers))}/{len(tickers)}", flush=True)
    return pd.DataFrame(rows).reindex(columns=EVENT_COLUMNS), sorted(set(failures))


def fingerprint_summary(events):
    columns = ["fingerprint", "events", "resolved", "wins", "losses", "ambiguous", "win_rate_resolved"]
    if events.empty:
        return pd.DataFrame(columns=columns)
    data = events.copy()
    magnitude = data[["day_return", "five_day_return"]].max(axis=1)
    data["magnitude"] = pd.cut(magnitude, [-np.inf, 0.30, 0.60, np.inf], labels=["20-30%", "30-60%", ">60%"])
    data["volume"] = pd.cut(data.event_volume_ratio_20, [-np.inf, 3, 6, np.inf], labels=["<3x", "3-6x", ">6x"])
    data["close"] = pd.cut(data.event_close_location, [-np.inf, 0.5, 0.8, np.inf], labels=["weak", "middle", "strong"])
    data["gap"] = pd.cut(data.event_gap, [-np.inf, 0.05, 0.20, np.inf], labels=["<5%", "5-20%", ">20%"])
    data["high"] = np.where(data.new_52w_high, "new 52w high", "below 52w high")
    data["market"] = np.where(data.spy_above_200dma == True, "SPY above 200d", "SPY below/unknown 200d")
    parts = []
    for field in ["event_type", "magnitude", "volume", "close", "gap", "high", "market"]:
        for value, group in data.groupby(field, observed=True, dropna=False):
            wins = int((group.primary_outcome == "WIN_10_BEFORE_10").sum())
            losses = int((group.primary_outcome == "LOSS_10_BEFORE_10").sum())
            ambiguous = int((group.primary_outcome == "AMBIGUOUS_SAME_BAR").sum())
            resolved = wins + losses
            parts.append(
                {
                    "fingerprint": f"{field}={value}",
                    "events": len(group),
                    "resolved": resolved,
                    "wins": wins,
                    "losses": losses,
                    "ambiguous": ambiguous,
                    "win_rate_resolved": wins / resolved if resolved else np.nan,
                }
            )
    return pd.DataFrame(parts, columns=columns).sort_values(["events", "fingerprint"], ascending=[False, True])


def exit_policy_summary(events):
    rows = []
    policies = {"day_30_close": "return_30", "trail_7_after_10": "trail_7_return", "trail_10_after_10": "trail_10_return"}
    for policy, column in policies.items():
        values = pd.to_numeric(events.get(column, pd.Series(dtype=float)), errors="coerce").dropna()
        rows.append(
            {
                "policy": policy,
                "completed_events": len(values),
                "mean_return": values.mean() if len(values) else np.nan,
                "median_return": values.median() if len(values) else np.nan,
                "positive_rate": (values > 0).mean() if len(values) else np.nan,
            }
        )
    return pd.DataFrame(rows)


def main():
    OUT.mkdir(exist_ok=True)
    run_at = datetime.now(timezone.utc).isoformat()
    listed = engine.universe()
    listed.to_csv(OUT / "01_current_universe.csv", index=False)
    name_map = dict(zip(listed.ticker, listed.name))
    spy_close = download_spy_history()
    events, failures = download_history(listed.ticker.tolist(), name_map, spy_close)
    failure_rate = len(failures) / max(len(listed), 1)
    if failure_rate > engine.MAX_PRICE_REQUEST_FAILURE_RATE:
        raise RuntimeError("Winner cohort price failure rate exceeded locked cap")
    if len(events):
        events = events.sort_values(["event_date", "ticker"]).reset_index(drop=True)
    events.to_csv(OUT / "02_winner_event_ledger.csv", index=False)
    pd.DataFrame({"ticker": failures}).to_csv(OUT / "02_price_failures.csv", index=False)
    resolved = events[events.primary_outcome != "OPEN"].copy()
    open_events = events[events.primary_outcome == "OPEN"].copy()
    resolved.to_csv(OUT / "03_resolved_outcomes.csv", index=False)
    open_events.to_csv(OUT / "04_open_cohorts.csv", index=False)
    fingerprint_summary(events).to_csv(OUT / "05_fingerprint_summary_EXPLORATORY.csv", index=False)
    exit_policy_summary(events).to_csv(OUT / "06_exit_policy_summary_EXPLORATORY.csv", index=False)
    events[events.primary_outcome == "WIN_10_BEFORE_10"].to_csv(OUT / "07_retrospective_continuation_winners.csv", index=False)
    open_events.to_csv(OUT / "08_CURRENT_OPEN_EVENTS_NOT_BUY.csv", index=False)
    audit = {
        "study": "30-Session Extreme-Winner Continuation Cohort",
        "run_at_utc": run_at,
        "ruleset": "EXTREME_WINNER_SSOT.md",
        "current_universe_count": len(listed),
        "lookback_event_sessions": LOOKBACK_SESSIONS,
        "event_count": len(events),
        "resolved_count": len(resolved),
        "open_count": len(open_events),
        "wins_10_before_10": int((events.primary_outcome == "WIN_10_BEFORE_10").sum()),
        "losses_10_before_10": int((events.primary_outcome == "LOSS_10_BEFORE_10").sum()),
        "ambiguous_same_bar": int((events.primary_outcome == "AMBIGUOUS_SAME_BAR").sum()),
        "hit_20_percent": int(events.target_20_day.notna().sum()),
        "hit_30_percent": int(events.target_30_day.notna().sum()),
        "price_failures": len(failures),
        "price_failure_rate": failure_rate,
        "entry_ready_created_by_study": 0,
        "data_status": "EXPLORATORY_CURRENT_UNIVERSE_NOT_POINT_IN_TIME",
        "scarcity_rule": "Zero candidates is valid; thresholds may not be loosened.",
        "known_limitations": [
            "survivorship bias",
            "no delisted security master",
            "no point-in-time fundamentals or historical shares outstanding",
            "daily bars cannot reconstruct historical opening-range or VWAP paths",
            "historical catalysts and supply/dilution filings are explicitly unclassified",
            "spread and slippage are not yet modeled",
        ],
    }
    (OUT / "audit_winner_cohort.json").write_text(json.dumps(audit, indent=2))
    print(json.dumps(audit, indent=2), flush=True)


if __name__ == "__main__":
    main()
