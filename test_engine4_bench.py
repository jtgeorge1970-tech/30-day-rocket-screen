import json
from datetime import date
from pathlib import Path

import pandas as pd

import engine4_bench as bench
import engine4_final_guard as final_guard


def _configure_paths(tmp_path, monkeypatch):
    out = tmp_path / "output" / "engine4"
    out.mkdir(parents=True)
    monkeypatch.setattr(bench, "OUT", out)
    monkeypatch.setattr(bench.core, "OUT", out)
    monkeypatch.setattr(bench.core, "TIMELINE", out / "timeline.json")
    return out


def _scored(seed: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for index, ticker in enumerate(seed.ticker.astype(str).tolist()):
        score = 99.0 - index * 0.35
        rows.append(
            {
                "ticker": ticker,
                "score": score,
                "premarket_grade": "A" if score >= 90 else "B",
                "premarket_eligible": True,
                "premarket_a_grade": score >= 90,
                "premarket_gate_count": 7,
                "activity_score": 8.0,
                "last_premarket": 50.0,
                "catalyst_quality": 1.0,
                "premarket_volume_gate_pass": True,
                "atr_pct": 3.0,
                "resistance_room_pct": 12.0,
                "spread_order_authoritative": True,
                "spread_pct": 0.1,
                "sector": "Technology",
            }
        )
    return pd.DataFrame(rows)


def test_bench_is_daily_competition_capped_at_25(tmp_path, monkeypatch):
    out = _configure_paths(tmp_path, monkeypatch)
    today = "2026-09-18"
    current = [{"ticker": f"NEW{i:02d}", "rank": i + 1} for i in range(25)]
    (out / "top25_frozen.json").write_text(
        json.dumps({"target_date_et": today, "candidates": current}), encoding="utf-8"
    )
    state = tmp_path / "state" / "watch_bench.json"
    state.parent.mkdir(parents=True)
    state.write_text(
        json.dumps(
            {
                "target_date_et": "2026-09-17",
                "candidates": [
                    {
                        "ticker": f"OLD{i:02d}",
                        "age_sessions": 1,
                        "last_refreshed_date": "2026-09-17",
                        "first_added_date": "2026-09-17",
                        "tier": "RESERVE",
                    }
                    for i in range(25)
                ],
            }
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(bench, "_fresh_seed_rows", lambda symbols, *_: (pd.DataFrame({"ticker": symbols}), []))
    monkeypatch.setattr(bench.runner, "repaired_score_pool", lambda seed, *_: _scored(seed))
    monkeypatch.setattr(bench.runner, "install_repairs", lambda: None)

    result = bench.update_bench(today, state)
    assert result["competition_universe_count"] == 50
    assert result["naturally_watch_qualified_count"] > 25
    assert result["retained_by_top25_bench_cap"] == 25
    assert result["bench_cap_is_quota"] is False
    assert result["hot_count"] == 5
    assert result["developing_count"] == 10
    assert result["reserve_count"] == 10
    assert any(row["reason"] == "displaced_by_Top25_Bench_cap" for row in result["removals"])


def test_candidate_expires_after_five_completed_watch_sessions(tmp_path, monkeypatch):
    out = _configure_paths(tmp_path, monkeypatch)
    today = "2026-09-18"
    (out / "top25_frozen.json").write_text(
        json.dumps({"target_date_et": today, "candidates": []}), encoding="utf-8"
    )
    state = tmp_path / "state" / "watch_bench.json"
    state.parent.mkdir(parents=True)
    state.write_text(
        json.dumps(
            {
                "target_date_et": "2026-09-17",
                "candidates": [
                    {
                        "ticker": "RIPE",
                        "age_sessions": 5,
                        "last_refreshed_date": "2026-09-17",
                        "first_added_date": "2026-09-14",
                        "tier": "HOT",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(bench, "_fresh_seed_rows", lambda symbols, *_: (pd.DataFrame({"ticker": symbols}), []))
    monkeypatch.setattr(bench.runner, "repaired_score_pool", lambda seed, *_: _scored(seed))
    monkeypatch.setattr(bench.runner, "install_repairs", lambda: None)

    result = bench.update_bench(today, state)
    assert result["retained_by_top25_bench_cap"] == 0
    assert result["removals"] == [
        {"ticker": "RIPE", "reason": "five_session_watch_expired", "age_sessions": 6}
    ]


def test_only_current_date_hot_five_reach_final_guard(tmp_path, monkeypatch):
    state = tmp_path / "watch_bench.json"
    state.write_text(
        json.dumps(
            {
                "target_date_et": "2026-09-18",
                "candidates": [
                    {"ticker": f"H{i}", "tier": "HOT"} for i in range(7)
                ]
                + [{"ticker": "DEV", "tier": "DEVELOPING"}],
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(final_guard, "BENCH_STATE", state)
    hot = final_guard._hot_bench(date(2026, 9, 18))
    assert hot.ticker.tolist() == ["H0", "H1", "H2", "H3", "H4"]
    assert final_guard._hot_bench(date(2026, 9, 19)).empty


def test_bench_constants_match_locked_ssot():
    bench.self_test()
