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
| 2026-07-23 | Merged Paytm / Paytm (OCL) / Paytm Payments Bank App into one canonical "Paytm" | Same consumer app across the PPBL-to-OCL backend migration; splitting it would fracture one entity's history mid-window | Final |
| 2026-07-23 | Merged Slice / Slice Small Finance Bank Apps into one canonical "Slice" | Post banking-license merger rebrand of the same entity | Final |
| 2026-07-23 | Merged FAM / FamApp by Trio / Fampay / Fampay by Trio into one canonical "Fampay" | Trio Fintech rebrand labels for the same entity | Final |
| 2026-07-23 | Split Jupiter into two canonical entities: "Jupiter Money" and "Jupiter Edge" | Jupiter Edge is a distinct LivQuick PPI credit-linked product, not the core neobank app — merging them would misattribute volume | Final |
| 2026-07-23 | Kept POP UPI and Pop Club as separate entities | No confirmed evidence they're the same app; defaulting to not merging avoids a false consolidation | Final |

 ### Core Jupiter Money neobank — confirm relation to Jupiter Edge/Jupiter Money below
Distinct PPI/credit-linked product (LivQuick) — likely a separate TPAP entity, do not auto-merge
Same as Jupiter Edge — confirm before any merge
May be the same as "Jupiter" or a distinct reporting label — confirm
<img width="1279" height="85" alt="image" src="https://github.com/user-attachments/assets/15d6328e-72c5-4851-9bd8-a10b557179cf" />

May or may not be the same as Pop Club/POPClub — confirm

Base entity name

Post PPBL-restriction migration to OCL backend — same consumer app, confirm before merging (marks a real business event, worth a DECISIONS.md note either way)
Pre-migration entity name — same consumer app, confirm
<img width="1279" height="128" alt="image" src="https://github.com/user-attachments/assets/d9e80c95-6892-489f-a330-077b80834ecc" />

Now includes "Slice Small Finance Bank Apps" post banking-license merger — confirm same entity
North East SFB merger rebrand — likely same entity as Slice, confirm




Likely same bank, inconsistent NPCI label — confirm
Base entity name
<img width="1279" height="171" alt="image" src="https://github.com/user-attachments/assets/b9b4e978-893e-465f-b85f-ed70d4bcea52" />

### PLEASE GO TO THE NOTEBOOKS DIRECTORY IN THE REPO AND REFER TO DECISIONS(1) FROM THERE FOR THE DECISIONS ON THE DATE 23-07-2026 DURING SUPA BASE IMPORT TASK



