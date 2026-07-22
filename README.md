# Finsight — The UPI Growth Story

**Question:** Is UPI's growth broadening across apps, or concentrating into a
duopoly? What does that mean for a challenger like CRED?

**Answer target:** A dashboard, a one-page memo, and a defensible projection —
built on NPCI's public record, not assumptions.

## Scope (locked — see DECISIONS.md before changing any of this)

- **Window:** Nov 2023 – Oct 2025 (24 months, app-wise).
- **Grain:** `month, app` — volume, value, market share.
- **Long tail:** handled at source — NPCI buckets sub-threshold apps under
  "Other Apps," so no separate long-tail engineering is needed.
- **Model:** one linear regression, transaction-volume growth, next-quarter
  projection. No second model.
- **Out of scope:** bank-wise splits, additional cities/products, additional
  models. If you're about to add one, it goes in DECISIONS.md as a proposal
  first, not straight into the branch.

## Data source

- Primary: [NPCI UPI Ecosystem Statistics](https://www.npci.org.in/what-we-do/upi/upi-ecosystem-statistics)
  — official, monthly, app-wise (PSP-wise) volume and value.
- Cross-check only (not a data source): NPCI monthly press releases, for
  sanity-checking totals.

## Repo layout

```
finsight/
├── README.md              you are here
├── DECISIONS.md            running log — every scope/definition call, dated
├── TEAM_MEMBERS.md          who did what, plainly
├── data/
│   ├── raw/                 untouched exports from NPCI, as downloaded
│   └── processed/           cleaned CSVs that feed SQL/Supabase
├── sql/                    schema + queries (window functions, CTEs)
├── notebooks/              pandas/sklearn — cleaning, EDA, model
├── memo/                   the one-page deliverable
└── ai-appendix/            where AI was trusted, where it wasn't, and why
```

## Deliverables checklist

- [ ] Raw data assembled (24 months, app-wise) and loaded to Supabase
- [ ] SQL: market share over time (window fn), MoM growth, rankings, CTE
      concentration query
- [ ] Cleaning notes logged as they happen (not reconstructed after)
- [ ] EDA: growth trend, seasonality, concentration curve
- [ ] Linear regression: next-quarter volume projection, error reported
      honestly, overfitting check, named risks to the projection
- [ ] Dashboard (owner: TBD)
- [ ] One-page memo: broadening or concentrating, evidence, so-what for CRED
- [ ] AI appendix: real example of catching AI being wrong
- [ ] 3-minute walkthrough video (owner: TBD)

## Status

Day 1 in progress — data assembly.
