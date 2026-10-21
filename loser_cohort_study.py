"""Strict 30-session major-loser cohort and outcome study.

This module measures events without issuing buy recommendations. Its initial
Yahoo/current-universe dataset is explicitly exploratory because it is not a
point-in-time security master and does not include delisted securities.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

import rocket_screen as engine


OUT = Path("cohort_output")
LOOKBACK_SESSIONS = 30
EVENT_COOLDOWN_SESSIONS = 10
MIN_EVENT_HISTORY = 253
MAX_EVENT_FAILURE_RATE = engine.MAX_PRICE_REQUEST_FAILURE_RATE
HORIZONS = (5, 10, 20, 30)

EVENT_COLUMNS = [
    "ticker", "name", "event_date", "event_type", "event_close", "next_open",
    "day_return", "five_day_return", "drawdown_52", "off_prior_52w_low",
    "undercut_prior_52w_low", "pre_event_return_20", "event_volume_ratio_20",
    "event_atr14_pct", "event_close_location", "event_dollar_volume_20",
    "available_forward_sessions", "primary_outcome", "target_day",
    "stop_day", "observed_mfe", "observed_mae",
] + [f"return_{h}" for h in HORIZONS] + [f"mfe_{h}" for h in HORIZONS] + [f"mae_{h}" for h in HORIZONS]


def _ohlcv(data, ticker, batch):
    return pd.DataFrame({
        field: engine._field(data, field, ticker, batch)
        for field in ["Open", "High", "Low", "Close", "Volume"]
    }).dropna()


def _outcome(frame, event_idx):
    future = frame.iloc[event_idx + 1:event_idx + 31].copy()
    if future.empty:
        return {
            "next_open": np.nan, "available_forward_sessions": 0,
            "primary_outcome": "OPEN", "target_day": np.nan,
            "stop_day": np.nan, "observed_mfe": np.nan, "observed_mae": np.nan,
            **{f"return_{h}": np.nan for h in HORIZONS},
            **{f"mfe_{h}": np.nan for h in HORIZONS},
            **{f"mae_{h}": np.nan for h in HORIZONS},
        }
    entry = float(future.Open.iloc[0])
    target, stop = entry * 1.10, entry * 0.90
    target_hits = np.flatnonzero(future.High.to_numpy() >= target)
    stop_hits = np.flatnonzero(future.Low.to_numpy() <= stop)
    target_day = int(target_hits[0] + 1) if len(target_hits) else np.nan
    stop_day = int(stop_hits[0] + 1) if len(stop_hits) else np.nan
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
        "next_open": entry, "available_forward_sessions": len(future),
        "primary_outcome": label, "target_day": target_day, "stop_day": stop_day,
        "observed_mfe": float(future.High.max() / entry - 1),
        "observed_mae": float(future.Low.min() / entry - 1),
    }
    for horizon in HORIZONS:
        complete = len(future) >= horizon
        window = future.iloc[:horizon]
        result[f"return_{horizon}"] = float(window.Close.iloc[-1] / entry - 1) if complete else np.nan
        result[f"mfe_{horizon}"] = float(window.High.max() / entry - 1) if complete else np.nan
        result[f"mae_{horizon}"] = float(window.Low.min() / entry - 1) if complete else np.nan
    return result


def event_rows(frame, ticker, name=""):
    """Return de-duplicated qualifying events from the latest 30 sessions."""
    frame = frame.dropna(subset=["Open", "High", "Low", "Close", "Volume"]).copy()
    if len(frame) < MIN_EVENT_HISTORY:
        return []
    close, high, low, volume = frame.Close, frame.High, frame.Low, frame.Volume
    day_ret = close.pct_change()
    five_ret = close / close.shift(5) - 1
    trailing_high = close.rolling(252, min_periods=252).max()
    prior_low = low.shift(1).rolling(252, min_periods=252).min()
    dollar_volume = (close * volume).shift(1).rolling(20, min_periods=20).mean()
    volume_avg = volume.shift(1).rolling(20, min_periods=20).mean()
    pre_ret20 = close.shift(1) / close.shift(21) - 1
    returns = close.pct_change()
    tr = pd.concat([(high-low), (high-close.shift()).abs(), (low-close.shift()).abs()], axis=1).max(axis=1)
    atr = tr.shift(1).rolling(14, min_periods=14).mean()
    start = max(MIN_EVENT_HISTORY - 1, len(frame) - LOOKBACK_SESSIONS)
    rows, last_event_idx = [], -10_000
    for idx in range(start, len(frame)):
        one_day = day_ret.iloc[idx] <= -0.06
        five_day = five_ret.iloc[idx] <= -0.12
        drawdown = close.iloc[idx] / trailing_high.iloc[idx] - 1
        qualifies = (
            (one_day or five_day) and drawdown <= -0.15
            and close.iloc[idx] >= engine.MIN_PRICE
            and dollar_volume.iloc[idx] >= engine.MIN_DOLLAR_VOLUME
        )
        if not bool(qualifies) or idx - last_event_idx < EVENT_COOLDOWN_SESSIONS:
            continue
        last_event_idx = idx
        bar_range = max(float(high.iloc[idx] - low.iloc[idx]), 1e-9)
        event_type = "BOTH" if one_day and five_day else ("ONE_DAY" if one_day else "FIVE_DAY")
        row = {
            "ticker": ticker, "name": name, "event_date": frame.index[idx].date().isoformat(),
            "event_type": event_type, "event_close": float(close.iloc[idx]),
            "day_return": float(day_ret.iloc[idx]), "five_day_return": float(five_ret.iloc[idx]),
            "drawdown_52": float(drawdown),
            "off_prior_52w_low": float(close.iloc[idx] / prior_low.iloc[idx] - 1),
            "undercut_prior_52w_low": bool(low.iloc[idx] < prior_low.iloc[idx]),
            "pre_event_return_20": float(pre_ret20.iloc[idx]),
            "event_volume_ratio_20": float(volume.iloc[idx] / volume_avg.iloc[idx]),
            "event_atr14_pct": float(atr.iloc[idx] / close.iloc[idx]),
            "event_close_location": float((close.iloc[idx] - low.iloc[idx]) / bar_range),
            "event_dollar_volume_20": float(dollar_volume.iloc[idx]),
        }
        row.update(_outcome(frame, idx))
        rows.append(row)
    return rows


def fingerprint_summary(events):
    if events.empty:
        return pd.DataFrame(columns=["fingerprint", "events", "resolved", "wins", "losses", "ambiguous", "win_rate_resolved"])
    x = events.copy()
    x["severity"] = pd.cut(-x[["day_return", "five_day_return"]].min(axis=1), [-np.inf, .08, .15, np.inf], labels=["6-8%", "8-15%", ">15%"])
    x["volume"] = pd.cut(x.event_volume_ratio_20, [-np.inf, 1.5, 3, np.inf], labels=["<1.5x", "1.5-3x", ">3x"])
    x["close"] = pd.cut(x.event_close_location, [-np.inf, .35, .65, np.inf], labels=["weak", "middle", "strong"])
    x["low_relation"] = np.where(x.undercut_prior_52w_low, "undercut prior low", "held prior low")
    parts = []
    for field in ["event_type", "severity", "volume", "close", "low_relation"]:
        for value, group in x.groupby(field, observed=True, dropna=False):
            wins = int((group.primary_outcome == "WIN_10_BEFORE_10").sum())
            losses = int((group.primary_outcome == "LOSS_10_BEFORE_10").sum())
            ambiguous = int((group.primary_outcome == "AMBIGUOUS_SAME_BAR").sum())
            resolved = wins + losses
            parts.append({
                "fingerprint": f"{field}={value}", "events": len(group), "resolved": resolved,
                "wins": wins, "losses": losses, "ambiguous": ambiguous,
                "win_rate_resolved": wins / resolved if resolved else np.nan,
            })
    return pd.DataFrame(parts).sort_values(["events", "fingerprint"], ascending=[False, True])


def download_cohort_prices(tickers):
    rows, failures = [], []
    for start in range(0, len(tickers), engine.YAHOO_PRICE_BATCH_SIZE):
        batch = tickers[start:start + engine.YAHOO_PRICE_BATCH_SIZE]
        data = engine.retry_yahoo(
            lambda b=batch: yf.download(b, period="2y", interval="1d", group_by="column", auto_adjust=True, threads=False, progress=False, timeout=30),
            f"cohort prices batch {start // engine.YAHOO_PRICE_BATCH_SIZE + 1}",
            request_units=len(batch), validator=engine.valid_price_download,
        )
        if data is None:
            failures.extend(batch)
            continue
        for ticker in batch:
            try:
                rows.extend(event_rows(_ohlcv(data, ticker, batch), ticker))
            except Exception as exc:
                print(f"Cohort metric skip {ticker}: {exc}", flush=True)
                failures.append(ticker)
        if (start // engine.YAHOO_PRICE_BATCH_SIZE + 1) % 10 == 0:
            print(f"Cohort price progress: {min(start + engine.YAHOO_PRICE_BATCH_SIZE, len(tickers))}/{len(tickers)}", flush=True)
    return pd.DataFrame(rows).reindex(columns=EVENT_COLUMNS), sorted(set(failures))


def current_strict_candidates(events):
    path = Path("output/07_entry_geometry_pass.csv")
    if not path.exists() or events.empty:
        return pd.DataFrame(columns=["ticker", "event_date", "primary_outcome", "status"])
    geometry = pd.read_csv(path)
    open_events = events[events.primary_outcome == "OPEN"].sort_values("event_date").drop_duplicates("ticker", keep="last")
    candidates = geometry.merge(open_events, on="ticker", how="inner", suffixes=("_current", "_event"))
    candidates["status"] = "RESEARCH_ONLY_NOT_BUY"
    return candidates


def main():
    OUT.mkdir(exist_ok=True)
    run_at = datetime.now(timezone.utc).isoformat()
    universe = engine.universe()
    universe.to_csv(OUT / "01_current_universe.csv", index=False)
    name_map = dict(zip(universe.ticker, universe.name))
    events, failures = download_cohort_prices(universe.ticker.tolist())
    if len(failures) / max(len(universe), 1) > MAX_EVENT_FAILURE_RATE:
        raise RuntimeError("Cohort price failure rate exceeded locked cap")
    if len(events):
        events["name"] = events.ticker.map(name_map).fillna(events.name)
        events = events.sort_values(["event_date", "ticker"]).reset_index(drop=True)
    events.to_csv(OUT / "02_loser_event_ledger.csv", index=False)
    pd.DataFrame({"ticker": failures}).to_csv(OUT / "02_price_failures.csv", index=False)
    completed = events[events.primary_outcome != "OPEN"].copy()
    open_cohorts = events[events.primary_outcome == "OPEN"].copy()
    completed.to_csv(OUT / "03_resolved_outcomes.csv", index=False)
    open_cohorts.to_csv(OUT / "04_open_cohorts.csv", index=False)
    fingerprint_summary(events).to_csv(OUT / "05_fingerprint_summary_EXPLORATORY.csv", index=False)
    events[events.primary_outcome == "WIN_10_BEFORE_10"].to_csv(OUT / "06_retrospective_winners.csv", index=False)
    strict = current_strict_candidates(events)
    strict.to_csv(OUT / "07_CURRENT_RESEARCH_CANDIDATES_NOT_BUY.csv", index=False)
    audit = {
        "study": "30-Session Loser Cohort & Fingerprint Study",
        "run_at_utc": run_at, "ruleset": "FINGERPRINT_STUDY_SSOT.md",
        "current_universe_count": len(universe), "lookback_sessions": LOOKBACK_SESSIONS,
        "event_count": len(events), "resolved_count": len(completed), "open_count": len(open_cohorts),
        "wins_10_before_10": int((events.primary_outcome == "WIN_10_BEFORE_10").sum()),
        "losses_10_before_10": int((events.primary_outcome == "LOSS_10_BEFORE_10").sum()),
        "ambiguous_same_bar": int((events.primary_outcome == "AMBIGUOUS_SAME_BAR").sum()),
        "current_strict_research_candidates": len(strict), "entry_ready_created_by_study": 0,
        "price_failures": len(failures), "price_failure_rate": len(failures) / max(len(universe), 1),
        "scarcity_rule": "Zero candidates is valid; thresholds may not be loosened to force a pick.",
        "data_status": "EXPLORATORY_CURRENT_UNIVERSE_NOT_POINT_IN_TIME",
        "known_limitations": ["survivorship bias", "no delisted security master", "no point-in-time fundamentals"],
    }
    (OUT / "audit_loser_cohort.json").write_text(json.dumps(audit, indent=2))
    print(json.dumps(audit, indent=2), flush=True)


if __name__ == "__main__":
    main()
