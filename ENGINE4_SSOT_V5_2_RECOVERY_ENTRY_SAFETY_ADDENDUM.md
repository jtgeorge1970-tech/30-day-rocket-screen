# Engine 4 — SSOT v5.2 Recovery Entry Safety Addendum
Locked: 2026-09-16

This addendum is part of the Engine 4 SSOT and supersedes conflicting recovery-entry wording in earlier versions. All non-conflicting rules remain locked.

## Why v5.2 exists

The September 16 FPS dry run exposed a false-positive recovery ARM. The old trigger cleared a small recent base but remained below the existing session high after an approximately 10% gap-up move. The maximum permitted fill also did not preserve the locked 2:1 reward/risk requirement.

## Mandatory recovery-entry safety gates

Before Engine 4 may issue RECOVERY ARM or RECOVERY BUY:

- The trigger must clear both the recent recovery-base high and the current session high, plus the locked confirmation buffer. A base-only trigger below session-high resistance is prohibited.
- The prior regular-session close must be present and verified. Missing prior-close data fails closed.
- The recovery trigger may be no more than 8.0% above the verified prior close during validation. A more extended move remains WATCH and cannot generate an official order.
- The first management level is the nearer of the formula 2.5R objective and verified overhead resistance when that resistance is above the trigger.
- At least 2.0:1 reward/risk must exist at the trigger before known resistance.
- The maximum permitted purchase price—not merely the theoretical trigger—must preserve at least 2.0:1 reward/risk. The chase band must shrink when necessary. If no positive safe chase band remains, the setup fails closed.

## Required audit fields

Recovery audit output must preserve the session high, breakout level, trigger, raw chase limit, safe maximum purchase price, prior close, trigger extension percentage, resistance price when known, reward/risk at the trigger, and reward/risk at the maximum permitted fill.

## FPS regression requirement

An FPS-style case with a prior close of $31.36, a session high of $34.49, and a recovery base high near $34.30 must not produce RECOVERY ARM or RECOVERY BUY. Its trigger must clear the session high and the excessive-extension gate must fail closed.
