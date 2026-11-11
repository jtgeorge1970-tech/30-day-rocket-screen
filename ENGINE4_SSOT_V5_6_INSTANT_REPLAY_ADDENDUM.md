# Engine 4 SSOT — Instant Replay Feeder Authorization

Joseph explicitly approved this narrow change on 2026-09-21.

## Immutable production rule
Engine 4 strategy logic remains locked. No scoring, gates, thresholds, ranking rules,
Top-100/Top-25/Top-3 behavior, BUY/WAIT/NO-TRADE logic, production timing, Bench
logic, or production notification behavior may be changed without Joseph's explicit
approval for that specific change.

## Approved interface change
Engine 4 may accept market evidence through one of three explicit feeder contexts:

1. AUTO LIVE — existing scheduled production path.
2. MANUAL LIVE — existing on-demand current-day production path.
3. INSTANT REPLAY — isolated point-in-time historical path.

The replay feeder is an input-source/interface change only. It may not alter strategy
decisions or silently substitute different rules.

## Replay isolation contract
- Replay must be explicitly labeled REPLAY and carry a requested Eastern market date.
- Replay may never fall back to a current/live provider. Missing point-in-time evidence
  is a replay DATA FAILURE for the affected evidence/stage.
- Replay may never send production/trade-like SMS.
- Replay may never write or commit production Bench state.
- Replay artifacts live under an isolated replay directory/run artifact.
- Replay may not overwrite committed production artifacts.
- Replay may not count as a production daily cycle or block the next AUTO/MANUAL live run.
- Live AUTO and MANUAL paths remain the existing default behavior.
- Before merge, tests must prove that the live default path remains unchanged and that
  replay fails closed when point-in-time evidence is unavailable.

## Point-in-time integrity
Every replay decision may use only evidence whose timestamp is at or before that
stage's simulated Eastern time. Historical bars must be truncated to the simulated
clock. Catalysts must include their publication timestamp. Quote/spread evidence must
come from a historical point-in-time source/snapshot; a present-day quote is forbidden.

No hindsight leakage is permitted.
