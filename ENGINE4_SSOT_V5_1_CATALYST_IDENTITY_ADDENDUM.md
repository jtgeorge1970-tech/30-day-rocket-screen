# Engine 4 — SSOT v5.1 Catalyst Identity Addendum
Locked: 2026-09-16

This addendum is part of the Engine 4 SSOT and supersedes conflicting catalyst-identification wording in earlier versions. All non-conflicting rules remain locked.

## Mandatory catalyst identity gate

Google News search results are discovery candidates, not proof that a headline belongs to the screened security.

Before Engine 4 awards any catalyst points, the headline must:

- contain the exact ticker as a standalone token;
- contain a verified identity term from the security's company name, independent of generic legal and industry words;
- pass the existing freshness, promotional-content, negative-catalyst, and positive-catalyst checks.

The publisher suffix may not satisfy the company-identity requirement. If the company name is missing, ambiguous, or cannot be matched, the catalyst must fail closed with zero points. Engine 4 may miss a true catalyst rather than award points to an unrelated company.

The production pipeline must pass the baseline security's company name into the catalyst provider. Ticker-only catalyst scoring is prohibited.

## Required regression protection

Automated tests must include the verified STX collision: a headline about the unrelated South Korean STX entity must score zero for Seagate Technology Holdings PLC. A valid headline containing both Forgent Power Solutions and FPS must remain accepted.
