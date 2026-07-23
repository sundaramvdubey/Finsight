# Cleaning Notes

Log every fix as you make it, in plain language, with the month/file it
applied to. Do not write this retroactively — it's the evidence that the
cleaning actually happened and what it changed.

| Date | File / Month | Issue found | Fix applied |
|---|---|---|---|
| 2026-07-23 | July 2024 block | Header row said "2025" but sat chronologically between Jun-2024 and Aug-2024 headers | Relabeled to 2024 based on position in the sheet, not the printed year |
| 2026-07-23 | 48 cells, 16 months (top 3 apps each month) | Value column stored as text with Indian comma-grouping (e.g. `"11,98,690.03"`) instead of numeric | Stripped commas, cast to float |
| 2026-07-23 | All months | App names carried inconsistent trailing `#` footnote markers and mixed casing (`PhonePe` / `PhonePe #` / `Phone Pe #`) | Stripped trailing `#`, normalized whitespace; pure case/spacing/punctuation duplicates (17 groups) auto-merged to one canonical name |
| 2026-07-23 | Oct 2025, Suryoday Bank Apps | Volume/value both `-` | Mapped to `0` — NPCI's own "no transactions" convention that month, not missing data |
| 2026-07-23 | Whole file | 138 distinct raw app names, several were the same entity renamed mid-window (Paytm's PPBL-to-OCL migration, Slice's banking-license merger, FamPay's Trio rebrand) or ambiguous (Jupiter Money vs Jupiter Edge, POP UPI vs Pop Club) | Flagged all 18 semantic cases in `app_reference_review.csv`, held them out of the auto-merge, got explicit yes/no per case, logged each in `DECISIONS.md` before merging |
| 2026-07-23 | 9 (month, app) pairs across Nov 2023-Aug 2025 | Same app listed twice within a single month in NPCI's own raw export (e.g. Mobikwik twice in Nov 2023, Federal Bank Apps twice in Jul 2024) — surfaced only when Supabase's unique(month, app) constraint rejected the import | Summed the volume/value for each duplicate pair rather than dropping either row |
| 2026-07-23 | Dec 2023, Feb 2024, Mar 2024, Sep 2024, Jul 2025 | Per-app volumes exactly matched the prior month, all 68-86 apps, zero variance — confirmed wrong (not just suspicious) against an independently reported Dec-2023 NPCI aggregate of 12.02bn transactions vs. the 11.16bn duplicate in our file | Excluded these 5 months from all downstream analysis rather than fabricate or interpolate a fix; window is effectively 19 real months, documented as a limitation |
