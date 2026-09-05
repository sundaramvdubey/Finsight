# Finsight v1 — Data Provenance and Licensing Notes

## What the dashboard uses

Finsight uses the repository’s processed app-wise monthly table at `data/processed/upi_monthly_app_FINAL.csv`. Each row represents one `(month_start, app_name)` observation with transaction volume in millions, transaction value in crore rupees, and a retained `source_file` lineage field. The dashboard uses derived aggregates from that table; it does not collect personal transaction data and it does not connect to user accounts.

## Primary source

The primary source for the ecosystem pulse is the [NPCI UPI Product Statistics page](https://www.npci.org.in/product/upi/product-statistics). The five April–August 2026 rows are retained in `data/raw/npci_upi_monthly_2026_27.csv` with the source URL and source note. The original app-wise workbook exports remain in `data/raw/` as the project’s provenance archive. NPCI monthly press releases are used only as sanity checks, not as a substitute for the app-wise table.

The current NPCI public table exposes ecosystem-level monthly volume, value, and banks-live fields through August 2026. It does not expose a matching app-wise CRED row in the same table, so Finsight refreshes the ecosystem pulse separately and keeps the app-wise CRED analysis bounded at October 2025. The dashboard never silently combines those grains.

## Why only 19 of 24 months are used

The locked research window is November 2023 through October 2025, or 24 calendar months. Five app-wise exports—December 2023, February 2024, March 2024, September 2024, and July 2025—were byte-identical to the preceding month across app-level volumes. They were excluded from the EDA, concentration analysis, and regression rather than interpolated or silently treated as real observations. The effective analysis table therefore contains 19 verified months and 1,482 rows.

This is a data-quality decision, not a claim that UPI activity did not exist in those months. The gap is visible in the dashboard and remains recorded in `DECISIONS.md`.

## Licensing posture

The code in this repository is released under the MIT License. The NPCI source data is attributed to NPCI and is not relicensed by this repository. Because the source page and its current terms were not confirmed during this release audit, treat the raw exports as source-attributed research material and review NPCI’s current terms before commercial redistribution or a public data-download mirror.

The live dashboard is designed as an educational, non-commercial, source-attributed visualization of derived aggregates. Deployment is permitted only if the operator is comfortable with that attribution and licensing posture. No personal or confidential financial information is included.

## Refresh checklist

Before refreshing the dashboard, download official exports, preserve original files unchanged in `data/raw/`, update the cleaning notes, run `python scripts/validate_data.py`, rerun `python scripts/model_benchmark.py`, regenerate the typed module with `python scripts/build_dashboard_data.py`, and record all definition changes in `DECISIONS.md`. Do not patch missing months with invented values or mix ecosystem-level and app-wise data.
