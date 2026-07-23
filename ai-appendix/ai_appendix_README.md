# AI Appendix

Where AI was trusted, where it wasn't, and why. One real example minimum.

## Example 1: caught before it entered the analysis

An earlier draft of this project contained a fully-written "UPI Ecosystem
Analysis Report" with specific volume/value figures — before any real data
had been loaded or queried. It read as a finished deliverable. It wasn't:
it was AI-generated placeholder shaped like a result. It was discarded and
logged in `DECISIONS.md` rather than treated as a starting point, because
letting fabricated numbers survive into a real analysis is the single
easiest way to produce a confident, wrong memo.

## Example 2: caught by cross-month comparison, not by inspection

The cleaned CSV passed every check that looks at one month at a time — correct
row counts, correct numeric types, correct date range. It still had a real
error: 5 of 24 months (Dec 2023, Feb 2024, Mar 2024, Sep 2024, Jul 2025) were
byte-for-byte duplicates of the adjacent month, all the way down to individual
app volumes. AI-assisted cleaning had no reason to check *across* months for
exact repeats, and the per-month validation looked clean because a duplicated
month is internally consistent — it just isn't real.

It surfaced only because a follow-up MoM growth query returned exact
`0.000000%` values in five places, which was itself a signal that should have
been caught immediately rather than glossed over. Once flagged, it was
confirmed — not assumed — by cross-checking the Dec 2023 total against an
independently reported NPCI aggregate (12.02bn transactions), which didn't
match the 11.16bn duplicate sitting in the file. The 5 months were excluded
from all downstream analysis rather than patched or interpolated, and the gap
is stated directly in the memo rather than hidden in a footnote.

**Lesson:** row-level and month-level checks aren't enough for time-series
data — the validation that actually catches silent duplication has to compare
adjacent periods against each other, not just check each one in isolation.
