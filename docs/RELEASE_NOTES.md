# Finsight v1.0.0

Finsight v1 ships the finished static dashboard for the UPI Growth Story capstone.

## Included

- Editorial dashboard with verified volume trend, top-two concentration toggle, app ranking lens, next-quarter projection, method cards, source dockets, and guided walkthrough.
- Owner assignment consolidated under Sundaram Dubey while preserving the historical contribution record.
- Three-minute walkthrough narration and in-dashboard guided read.
- Explicit 19-of-24-month explanation, model train/test MAPE, projection limits, and data provenance notes.
- Automated Python checks for schema, nulls, date range, duplicates, numeric types, and non-negative metrics, wired to GitHub Actions.
- MIT license for code. NPCI source data remains attributed and subject to its current terms.

## Verification

```text
python3 scripts/validate_data.py  -> PASS
pnpm check                        -> PASS
pnpm build                        -> PASS
```

The dashboard is static and requires no login, database, or paid API. Publish a public demo only after accepting the source-attribution and licensing posture documented in `docs/DATA_PROVENANCE.md`.
