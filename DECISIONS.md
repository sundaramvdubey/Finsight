# Decision Log

Every scope, definition, or data call, dated, with why. If it's not here, it
didn't happen — this replaces a Notion board, since Notion isn't in the
toolset for this build.

| Date | Decision | Rationale | Status |
|---|---|---|---|
| 2026-07-22 | Locked window to Nov 2023–Oct 2025 (24 months) | Previous draft claimed 24 months but the labeled date range was actually 28; picked a clean 24-month window that matches the stated number | Final |
| 2026-07-22 | Dropped bank-wise dataset from scope | Brief requires "top apps plus a long tail bucket, one model" — a second full dataset is scope creep against a 40-hour/5-day budget and isn't required | Final |
| 2026-07-22 | Long tail handled via NPCI's own "Other Apps" bucket | NPCI's ecosystem statistics page already aggregates apps under a reporting threshold into "Other Apps" — no custom long-tail engineering needed | Final |
| 2026-07-22 | Discarded prior "UPI Ecosystem Analysis Report" draft | It contained finished-looking numbers written before any real data was loaded or queried; kept as a shape reference only, not a data source | Final |
| 2026-07-22 | Market share basis: TBD | Volume-share and value-share can diverge (see PhonePe/GPay vs. value-weighted apps) — decide once first month is loaded and both are visible | Open |


## Dataset change

From Jan 2025 onward, NPCI removed columns K and L from the app-wise dataset.
Columns retained as-is; missing values remain blank for Jan 2025–Oct 2025.
