# Finsight v1 — UPI growth, read with receipts

Finsight is a transparent, evidence-first dashboard and strategy memo about India’s UPI app ecosystem. It asks one focused question: **is UPI growth broadening across apps, or is it still concentrated in a duopoly—and what does that mean for a challenger like CRED?**

The answer is intentionally modest: **UPI is growing, but distribution remains concentrated.** In the verified record, monthly transaction volume rises from 11.16 billion in November 2023 to 19.97 billion in October 2025. PhonePe and Google Pay together account for 83.01% of October 2025 transaction volume. Scale is table stakes; distribution is the moat.

## What shipped in v1

| Deliverable | Status |
|---|---|
| Static dashboard with volume, concentration, app ranking, projection, and method sections | Complete |
| Owner labels replacing `TBD` | Complete — maintained by Sundaram Dubey |
| Three-minute walkthrough script and shot list | Complete — `docs/WALKTHROUGH.md` |
| Explanation of 19 verified months out of a 24-month window | Complete — visible in dashboard, README, memo, and decisions log |
| Honest model error reporting | Complete — 1.69% temporal holdout MAPE vs 2.15% train MAPE |
| Data provenance and licensing posture | Complete — `docs/DATA_PROVENANCE.md` |
| Automated checks for schema, nulls, date range, and duplicate rows | Complete — `python scripts/validate_data.py` and GitHub Actions |
| Release license | Complete — MIT for code; NPCI data remains source-attributed |

## Scope (locked)

The analysis covers November 2023 through October 2025 at the `month_start, app_name` grain, with transaction volume in millions and value in crore rupees. The model is one linear regression on total transaction-volume growth using a calendar-month index. Bank-wise splits, additional models, additional cities or products, and custom long-tail engineering remain out of scope.

## The 19-of-24-month decision

The nominal research window has 24 calendar months. Five app-wise exports—December 2023, February 2024, March 2024, September 2024, and July 2025—were byte-identical to their preceding month across app-level volumes. They were excluded from EDA, concentration analysis, and modeling rather than interpolated or silently treated as real observations. The effective table therefore contains **19 verified months and 1,482 rows**. This is a named limitation, not a claim that activity did not exist in those months. See `DECISIONS.md` and `docs/DATA_PROVENANCE.md`.

## Model error, reported honestly

A temporal holdout keeps the last four real months out of training. Test MAPE is **1.69%**, while train MAPE is **2.15%**. That split does not make the projection universally reliable: the sample is small, the model has no seasonality term, and structural changes can move actual volume outside the approximate residual band. The projection is directional evidence, not a promise.

## Data provenance and licensing

The primary source is [NPCI UPI Ecosystem Statistics](https://www.npci.org.in/what-we-do/upi/upi-ecosystem-statistics). NPCI monthly press releases are cross-checks only. Raw exports are retained in `data/raw/`; cleaned rows retain `source_file` lineage. The code is MIT-licensed. NPCI data is attributed to NPCI and is not relicensed by this repository. Review current NPCI terms before commercial redistribution or publishing a raw-data mirror. The dashboard is designed as a source-attributed, educational visualization and contains no personal transaction data.

## Run the checks

```bash
python3 -m pip install pandas
python3 scripts/validate_data.py
```

The gate checks the expected schema, required-field nulls, locked date window, 19 verified months, full-row duplicates, duplicate `(month_start, app_name)` keys, numeric types, and non-negative metrics. The same gate runs on pushes and pull requests through `.github/workflows/validate.yml`.

## Repository map

```text
Finsight/
├── data/raw/                    untouched NPCI workbook exports
├── data/processed/              cleaned data, totals, projections, notes
├── notebooks/model.py           EDA and linear regression
├── sql/                         schema and analytical queries
├── memo/memo.md                 one-page strategy memo
├── docs/DATA_PROVENANCE.md      source and licensing notes
├── docs/WALKTHROUGH.md          three-minute recording script
├── scripts/validate_data.py     automated release gate
├── ai-appendix/                 where AI was trusted and caught
├── DECISIONS.md                 dated scope and cleaning decisions
├── TEAM_MEMBERS.md              plain ownership record
└── LICENSE                      MIT code license
```

## Dashboard and release

The live dashboard is a static frontend designed for personal use and optional public viewing. It reads the verified derived aggregates bundled with the dashboard and does not require login, a database, or a paid API. If the deployment operator accepts the NPCI attribution and licensing posture in `docs/DATA_PROVENANCE.md`, publish the static demo through the project hosting UI. The repository’s tagged v1 release should include the source, raw archive, processed outputs, validation script, walkthrough script, and memo together.

## Credits

Built as a capstone project at Himshikhar IIT Mandi. Current maintainer and dashboard owner: **Sundaram Dubey**.
