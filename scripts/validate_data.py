"""Validate the processed Finsight dataset before analysis or release.

The checks are intentionally small and auditable: schema, nulls, date window,
unique month/app grain, non-negative metrics, and the documented 19-month
verified observation count.
"""
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed" / "upi_monthly_app_FINAL.csv"
EXPECTED_COLUMNS = ["month_start", "app_name", "volume_mn", "value_cr", "source_file"]
START = pd.Timestamp("2023-11-01")
END = pd.Timestamp("2025-10-01")
EXPECTED_VERIFIED_MONTHS = 19


def fail(message: str) -> None:
    print(f"FAIL  {message}")
    raise SystemExit(1)


def main() -> None:
    if not DATA.exists():
        fail(f"missing processed dataset: {DATA}")
    df = pd.read_csv(DATA)
    if list(df.columns) != EXPECTED_COLUMNS:
        fail(f"schema mismatch: expected {EXPECTED_COLUMNS}, got {list(df.columns)}")
    if df.empty:
        fail("dataset is empty")
    nulls = df[EXPECTED_COLUMNS].isna().sum()
    if int(nulls.sum()) > 0:
        fail(f"null values present: {nulls[nulls > 0].to_dict()}")
    df["month_start"] = pd.to_datetime(df["month_start"], errors="coerce")
    if df["month_start"].isna().any():
        fail("month_start contains an unparseable date")
    if df["month_start"].min() < START or df["month_start"].max() > END:
        fail(f"date range outside locked window: {df['month_start'].min().date()} to {df['month_start'].max().date()}")
    if df["month_start"].nunique() != EXPECTED_VERIFIED_MONTHS:
        fail(f"expected {EXPECTED_VERIFIED_MONTHS} verified months, got {df['month_start'].nunique()}")
    if int(df.duplicated().sum()) > 0:
        fail(f"full duplicate rows found: {int(df.duplicated().sum())}")
    grain_dupes = int(df.duplicated(["month_start", "app_name"]).sum())
    if grain_dupes > 0:
        fail(f"duplicate month/app keys found: {grain_dupes}")
    for column in ["volume_mn", "value_cr"]:
        if not pd.api.types.is_numeric_dtype(df[column]):
            fail(f"{column} is not numeric")
        if (df[column] < 0).any():
            fail(f"{column} contains negative values")
    print("PASS  schema: expected columns present")
    print("PASS  nulls: no nulls in required fields")
    print(f"PASS  date range: {df['month_start'].min():%Y-%m-%d} to {df['month_start'].max():%Y-%m-%d}")
    print(f"PASS  verified months: {df['month_start'].nunique()} (five documented gaps excluded)")
    print("PASS  duplicates: no full-row or month/app duplicates")
    print(f"PASS  non-negative metrics: {len(df):,} rows")


if __name__ == "__main__":
    main()
