#!/usr/bin/env python3
"""OFTS fail-closed data acquisition. This is NOT the locked v2.2 scorer."""
import csv, json, os, pathlib, sys, time, urllib.request
ROOT=pathlib.Path("ofts")
SOURCE=ROOT/"universe.csv"
OUT=pathlib.Path("ofts-output")
OUT.mkdir(exist_ok=True)
if not SOURCE.exists():
    print("INPUT_MISSING: ofts/universe.csv; no symbols processed",flush=True)
    sys.exit(2)
with SOURCE.open(newline="",encoding="utf-8-sig") as f:
    rows=list(csv.DictReader(f))
symbols=[(r.get("Symbol") or r.get("symbol") or r.get("Ticker") or "").strip().upper() for r in rows]
symbols=[s for s in symbols if s]
if len(symbols)!=5502 or len(set(symbols))!=5502:
    raise SystemExit(f"Universe invalid: {len(symbols)} entries / {len(set(symbols))} unique")
result={"universe":len(symbols),"stage":"INPUT_VALIDATED","v22_scores":0,"scoring_ready":(ROOT/"locked_v22.py").exists()}
(OUT/"status.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result),flush=True)
if not result["scoring_ready"]:
    raise SystemExit("LOCKED_V22_IMPLEMENTATION_MISSING: no fabricated scores")
