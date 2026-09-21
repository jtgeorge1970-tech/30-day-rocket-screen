# Engine 4 Five-Day Failure Audit and Repair Register

Audit closed: 2026-09-18
Scope: operational and reporting failures observed from 2026-09-14 through 2026-09-18.

| Problem or excuse | Operational effect | Repair / enforced state |
|---|---|---|
| Wrong-season duplicate cron was treated as a failure | Successful Sep. 14–15 cycles were followed by false red runs | Wrong-season and unusably late scheduled events now exit as neutral skips |
| A single unavailable Google News path aborted Sep. 16 | Screening stages ran but the day could not finish | Provider resilience and verified fallback paths are enforced; missing required evidence is labeled, not silently invented |
| Sep. 17 scheduled delivery arrived hours late | The event was correctly rejected but no independent fallback produced a timely run | Four primary retries, three GitHub watchdog checks, plus the independent 08:20 ET manual guard |
| Sep. 18 automatic start did not occur | Manual intervention began late | At 08:36 ET the independent guard requires an actual run ID and repeatedly triggers the live manual path until verified or explicitly blocked |
| The old manual workflow bundled every stage | Counts and artifacts were hidden until recovery completed | Automatic and manual runners now expose, report, notify, and upload every stage immediately |
| A configured cap was described like a natural survivor count | Funnel reporting overstated results | SSOT reporter separates natural qualification from Top-100, Top-60, Top-25, and Bench caps |
| Exact funnel counts were unavailable and prior-day values were tempting substitutes | Live status could not meet the SSOT contract | Date-locked stage artifacts are required; unavailable values are labeled and never inferred |
| A primary result was presented as final while recovery still ran | Completion was claimed too early | Primary SMS says RUN STILL ACTIVE; only post-recovery invariant verification may send COMPLETE |
| Obsolete VERA fixture evidence appeared in live reporting | Historical test evidence could be confused with current candidates | Live reports are generated only from current dated artifacts; acceptance replay remains isolated |
| Overnight acceptance required live premarket enrichment | A healthy historical replay failed because it ran at 01:21 ET | Timing-dependent live assertion removed; acceptance validates the dated historical evidence actually under test |
| Acceptance/manual runs could be mistaken for the morning live run | A test run could suppress production or a watchdog intervention | Duplicate detection now classifies manual trigger content and accepts only `mode=live_today` |
| SMS deduplication did not prove recipient count | A deduplicated alert could be called delivered without proof for both phones | Audit marker records accepted recipient count; terminal verification requires exactly two |
| Notifications were “best effort” | Workflow could look green despite missing required alerts | Start, every stage, recovery, and completion require delivery and are terminally verified |
| Strong B candidates were discarded after one imperfect setup | Near-ripe candidates could be forgotten | New daily Top-25 Bench with Hot 5, Developing 10, Reserve 10, five-session expiry, and fresh competition |
| Watch candidates could accumulate without bound | A watch list could grow to 50–200 stale names | Top-25 is a hard capacity; weak, stale, expired, or displaced names are removed daily |
| A prior setup could be chased after price deterioration | Stale entry logic could create unsafe execution | Bench never carries trade approval; live gates and a fresh setup are mandatory, with the $100 official price cap retained |

No repair is considered proven by this register alone. Deployment plus three
consecutive green full acceptance workflow runs is the release gate.
