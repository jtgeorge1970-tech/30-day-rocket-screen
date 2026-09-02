# Quality Loser Reversal Engine V2

This branch replaces the old hot-runner ranking with a full-universe,
bottom-first entry process. Read `QUALITY_LOSER_SSOT.md` before changing any
threshold or gate.

Run:

```bash
python rocket_screen.py
```

The engine always writes the complete funnel to `output/`. A quantitative
survivor is **not** a recommendation. `output/09_ENTRY_READY.csv` remains empty
until `current_verification.csv` contains a sourced, <=24-hour review with every
mandatory gate marked `PASS` and `final_status` marked `APPROVED`.

An empty entry-ready file means no new purchase.

Actual holdings are private runtime input and must not be committed. Copy
`active_positions.template.csv` to `private/active_positions.csv`, or set
`ROCKET_ACTIVE_POSITIONS_FILE` to a private path. When supplied, every holding
is included in the mandatory output audit regardless of candidate rank.
