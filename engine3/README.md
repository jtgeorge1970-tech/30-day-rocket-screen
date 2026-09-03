# Engine #3 — Extreme-Winner Continuation

This engine is isolated from the original Rocket Engine and Quality-Loser V2.
It processes the full listed universe and examines every extreme upward event
from the latest 30 completed trading sessions, but advances only the rare names
that still retain strong continuation structure.

Local validation:

```bash
cd engine3
python -m unittest discover -s tests
python extreme_winner_engine.py
python validate_engine.py
python winner_continuation_study.py
python validate_study.py
```

`output/09_top3_REQUIRES_CURRENT_VERIFICATION.csv` is not a buy list.
`output/11_ENTRY_READY.csv` remains empty unless every fresh manual gate in
`current_verification.csv` is `PASS` and `final_status` is `APPROVED`.

Historical results are exploratory because the initial data source is a
current-universe/Yahoo dataset rather than a point-in-time database containing
delisted securities.
