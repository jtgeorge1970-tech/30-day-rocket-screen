"""Point-in-time security identity boundaries for oscillation research.

Do not concatenate a predecessor SPAC's prices with a post-combination
operating-company security to infer repeated oscillations. Add only verified,
dated identity events; the list is NOT a comprehensive corporate-actions feed.
Historical immutable cohorts remain untouched.
"""

IDENTITY_BOUNDARIES = {
    "IQMX": {
        "start": "2026-07-02",
        "event": "IQM Quantum Computers ADS commenced trading after RAAQ business combination",
        "source": "https://www.nasdaq.com/press-release/iqm-quantum-computers-and-real-asset-acquisition-corp-complete-combination-trading",
    },
}


def post_identity_bars(symbol, bars, asof=None):
    """Return eligible bars and identity-event metadata; fail closed on bad dates.

    Only enforce events effective on or before asof, to avoid retroactive
    application of future knowledge to older historical research timestamps.
    """
    event = IDENTITY_BOUNDARIES.get(symbol.upper())
    if not event:
        return list(bars), None
    if asof is None:
        if not bars or any(not r.get("date") for r in bars):
            raise ValueError("IDENTITY_BOUNDARY_REQUIRES_DATED_HISTORY")
        asof = max(r["date"] for r in bars)
    if asof < event["start"]:
        return list(bars), None
    if any(not r.get("date") for r in bars):
        raise ValueError("IDENTITY_BOUNDARY_REQUIRES_DATED_HISTORY")
    return [r for r in bars if r["date"] >= event["start"]], dict(event)
