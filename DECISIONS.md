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
| 2026-07-23 | Market share basis: volume-share primary, value-share secondary | Model is locked to transaction-volume growth; value-share stays as a cross-check column in queries but doesn't drive concentration/projection numbers | Final |
| 2026-07-23 | Merged Paytm / Paytm (OCL) / Paytm Payments Bank App into one canonical "Paytm" | Same consumer app across the PPBL-to-OCL backend migration; splitting it would fracture one entity's history mid-window | Final |
| 2026-07-23 | Merged Slice / Slice Small Finance Bank Apps into one canonical "Slice" | Post banking-license merger rebrand of the same entity | Final |
| 2026-07-23 | Merged FAM / FamApp by Trio / Fampay / Fampay by Trio into one canonical "Fampay" | Trio Fintech rebrand labels for the same entity | Final |
| 2026-07-23 | Split Jupiter into two canonical entities: "Jupiter Money" and "Jupiter Edge" | Jupiter Edge is a distinct LivQuick PPI credit-linked product, not the core neobank app — merging them would misattribute volume | Final |
| 2026-07-23 | Kept POP UPI and Pop Club as separate entities | No confirmed evidence they're the same app; defaulting to not merging avoids a false consolidation | Final |
| 2026-07-23 | Summed 9 (month, app) pairs that appeared twice in the raw NPCI export within the same month (Mobikwik x2 in Nov/Dec 2023, Slice x2 in Nov 2023-Mar 2024, Federal Bank Apps x2 in Jul 2024, Others x2 in Aug 2025) | Genuine duplicate listing in NPCI's source table, not a cleaning artifact — surfaced only when Supabase's unique(month_start, app_name) constraint rejected the import. Summing treats both entries as partial reports of the same entity, consistent with the one-row-per-(month,app) grain. Row count: 1851 -> 1842 | Final |
| 2026-07-23 | Excluded Dec 2023, Feb 2024, Mar 2024, Sep 2024, Jul 2025 from all analysis (EDA, concentration, model) | Per-app volumes for each of these 5 months were byte-identical to the preceding month — confirmed as a real data gap, not rounding, by cross-checking against independently reported Dec-2023 NPCI aggregate volume (12.02bn, vs. the 11.16bn duplicate sitting in our file). No verified app-wise NPCI figures could be sourced for these 5 months in the time available. Effective window is now 19 of 24 months; this is a named limitation in the memo, not silently patched. Row count: 1842 -> 1482 | Final |
