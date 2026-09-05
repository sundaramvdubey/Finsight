# Finsight v1.2 audit notes

## Critique mapped to current state

The current dashboard is backed by a static generated module at `client/src/data/finsightData.ts`; its latest verified dashboard month is October 2025, while the projection table extends only to January 2026. The current data gate is hard-coded to an end date of `2025-10-01` in `scripts/validate_data.py`. The dashboard presents one linear-regression projection and the prior release reports a 1.69% temporal holdout MAPE from only 19 verified observations. The CRED view is currently a latest-month ranking/concentration read rather than a complete share/growth/ranking trend analysis.

The repository already has `LICENSE`, `README.md`, provenance and walkthrough documentation, GitHub Actions validation, and local-first packaging. It does not yet have `citation.cff` or `CONTRIBUTING.md`. The walkthrough was removed from the dashboard UI, but its CSS remains unused and can be cleaned as part of the v1.2 polish.

## Current official data source

The official NPCI UPI Product Statistics page currently exposes monthly statistics through August 2026 in the 2026-27 view. It lists April 2026 through August 2026 with fields for month, banks live, volume in millions, and value in crore. The page states that data excludes transactions having debit/credit to the same account from August 2018 onward.

Source: [NPCI UPI Product Statistics](https://www.npci.org.in/product/upi/product-statistics), accessed for this audit in September 2026.

## Guardrails for implementation

Only data that can be obtained reproducibly from an official or clearly citable source should be added. If the app-level CRED data cannot be refreshed from a source with compatible provenance, the release should not invent or silently extend it; instead, the dashboard should label its app-level analysis as ending in October 2025 while refreshing only the ecosystem-level series that is actually supported.

The model section should compare simple baselines and a linear trend using rolling-origin or expanding-window evaluation. Metrics should be reported with the number of evaluated folds, forecast horizon, and a note that small samples make the comparison directional. “AI-driven” should be replaced with language such as “reproducible analytics dashboard” or “browser-based data analysis product.”
