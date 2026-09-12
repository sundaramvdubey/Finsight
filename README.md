# Finsight

> **A reproducible analytics dashboard and strategy memo about India’s UPI app ecosystem.**

[![Status](https://img.shields.io/badge/status-v1.2-365746?style=flat-square)](https://github.com/sundaramvdubey/Finsight)
[![Data](https://img.shields.io/badge/data-NPCI%20sourced-D59B48?style=flat-square)](https://www.npci.org.in/product/upi/product-statistics)
[![License](https://img.shields.io/badge/code-MIT-162233?style=flat-square)](LICENSE)

Finsight asks one focused question: **is UPI growth broadening across apps, or is it still concentrated—and what might that mean for a challenger such as CRED?** It answers with inspectable data, deterministic Python/pandas analysis, SQL queries, and a static React dashboard rather than unsupported “AI-driven” claims.

## The short answer

UPI is growing, but distribution remains concentrated. The verified app-wise record rises from **11.16 billion transactions in November 2023** to **19.97 billion in October 2025**; PhonePe and Google Pay account for **83.01% of October 2025 app-wise volume**. A separate official NPCI ecosystem pulse reports **24.51 billion transactions in August 2026**. These series remain separate because they do not have the same grain or app-level coverage.

## Why this project is credible

| Evidence | Current result |
|---|---|
| App-wise research window | 19 verified months, 1,482 cleaned rows |
| Concentration lens | Top-2 share and HHI over time |
| Forecasting benchmark | Expanding-window, one-step validation across 11 folds |
| Best benchmark | Linear trend at 3.22% MAPE on the small verified sequence |
| Reproducibility | Python validation, generated frontend data, SQL, cited provenance |

## Explore the project

- **[Open the strategy memo](memo/memo.md)** for the decision-oriented narrative.
- **[Review the data provenance](docs/DATA_PROVENANCE.md)** for sources, cleaning, and licensing boundaries.
- **[Inspect the audit](docs/V1_2_AUDIT.md)** for the critique-to-implementation record.
- **[Browse the analysis figures](notebooks/figures/)** for growth, concentration, seasonality, app share, and projection.

## Run it locally

```bash
python3 -m pip install pandas
python3 scripts/validate_data.py
python3 scripts/model_benchmark.py
python3 scripts/build_dashboard_data.py
pnpm install
pnpm check
pnpm test
pnpm build
pnpm dev
```

Then open the local Vite URL shown in the terminal. The dashboard is static, local-first, and requires no account, database, paid API, or backend service.

## Project positioning

Finsight is a **data and strategy project**, not a production financial product or investment recommendation. Its forecasts are directional because the verified sequence is small and contains named gaps. The repository keeps those limitations visible instead of smoothing them away.

## v1.2 improvements

| Area | What changed |
|---|---|
| Current data | Added a cited official NPCI ecosystem pulse through August 2026 without silently mixing it into the older app-wise series. |
| Missing months | Kept the five excluded app-wise months named and visible: December 2023, February 2024, March 2024, September 2024, and July 2025. |
| Forecasting | Added expanding-window one-step validation across 11 folds comparing last value, rolling mean, drift, and linear trend. Linear trend leads at 3.22% MAPE on this small verified sequence. |
| CRED lens | Added an app-wise CRED volume trend with latest verified share, rank, and volume, while keeping the October 2025 source boundary explicit. |
| Repository quality | Added `citation.cff`, `CONTRIBUTING.md`, official pulse validation, benchmark output, and refreshed release documentation. |
| Product language | Removed unsupported “AI-driven” positioning and replaced it with precise reproducible-analytics language. |

## The 19-of-24-month decision

The nominal app-wise research window contains 24 calendar months. Five exports were byte-identical to their preceding month across app-level volumes. They were excluded from EDA, concentration analysis, and modeling rather than interpolated or silently treated as real observations. The effective app-wise table contains **19 verified months and 1,482 rows**. This is a named limitation, not a claim that activity did not exist in those months. See `DECISIONS.md`, `docs/DATA_PROVENANCE.md`, and `docs/V1_2_AUDIT.md`.

## Model error, reported honestly

The v1.2 benchmark uses an expanding-window, one-step-ahead design with a minimum training window of eight verified observations and 11 evaluated folds. Linear trend records 3.22% MAPE, compared with 4.57% for a three-point rolling mean, 5.08% for a last-value baseline, and 5.52% for drift. The sample is small, the series contains named gaps, and the displayed Jan 2026 projection remains directional rather than a production forecast.

## Data provenance and licensing

The primary source is [NPCI UPI Product Statistics](https://www.npci.org.in/product/upi/product-statistics). NPCI monthly press releases are cross-checks only. The official August 2026 pulse is stored in `data/raw/npci_upi_monthly_2026_27.csv` with its source URL and note. App-wise cleaned rows retain `source_file` lineage. The code is MIT-licensed; NPCI data is attributed to NPCI and is not relicensed by this repository. Review current NPCI terms before commercial redistribution or publishing a raw-data mirror.

## Export and local-first app

The dashboard includes browser-local CSV and PDF exports. It is installable as a PWA from a hosted HTTPS demo or `localhost`. For a dependency-free static bundle, run `bash scripts/package_portable.sh`, unzip the resulting archive, run `./run-local.sh`, and open `http://localhost:4173`. No account, database, paid API, or backend is required.

## Run the checks

```bash
python3 -m pip install pandas
python3 scripts/validate_data.py
python3 scripts/model_benchmark.py
python3 scripts/build_dashboard_data.py
pnpm install
pnpm check
pnpm test
pnpm build
```

The data gate checks schema, required-field nulls, date windows, 19 verified app-wise months, duplicate rows, duplicate `(month_start, app_name)` keys, numeric types, non-negative metrics, and the separately sourced official pulse file. GitHub Actions runs the validation gate on pushes and pull requests.

## Repository map

```text
Finsight/
├── data/raw/                    source exports and cited official pulse
├── data/processed/              cleaned data, totals, projections, benchmarks
├── notebooks/model.py           EDA and baseline linear regression
├── scripts/validate_data.py     automated data-quality gate
├── scripts/model_benchmark.py   expanding-window model comparison
├── scripts/build_dashboard_data.py  deterministic frontend data refresh
├── memo/memo.md                 one-page strategy memo
├── docs/DATA_PROVENANCE.md      source and licensing notes
├── docs/V1_2_AUDIT.md           critique-to-implementation audit
├── CONTRIBUTING.md              contribution and evidence standards
├── citation.cff                 software citation metadata
├── DECISIONS.md                 dated scope and cleaning decisions
├── TEAM_MEMBERS.md              ownership record
└── LICENSE                      MIT code license
```

## Dashboard and release

The live dashboard is a static frontend for personal use and optional public viewing. It reads verified derived aggregates bundled with the dashboard and does not require login, a database, or a paid API. The v1.2 release is published from the existing GitHub repository with source, processed outputs, validation scripts, benchmark artifacts, documentation, and portable packaging.

## References

1. [NPCI UPI Product Statistics](https://www.npci.org.in/product/upi/product-statistics)
2. [GitHub citation file format](https://citation-file-format.github.io/)

## Credits

Built as a capstone project at Himshikhar IIT Mandi. Current maintainer and dashboard owner: **Sundaram Dubey**.
