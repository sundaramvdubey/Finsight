import { describe, expect, it } from "vitest";
import { buildCsvReport } from "./export";

describe("Finsight exports", () => {
  it("builds a source-attributed CSV with all verified report sections", () => {
    const csv = buildCsvReport();
    expect(csv.startsWith("\ufeffFinsight v1.2")).toBe(true);
    expect(csv).toContain("NPCI UPI Ecosystem Statistics");
    expect(csv).toContain("monthly,2023-11-01,11160.79");
    expect(csv).toContain("projection,2025-11-01,20218.51");
    expect(csv).toContain("ranking,2025-10-01,PhonePe");
    expect(csv).toContain("official_pulse,2026-08-01,752,24508.96");
    expect(csv).toContain("benchmark,linear_trend");
    expect(csv).toContain("cred_trend,2025-10-01");
    expect(csv.split("\n").length).toBeGreaterThan(130);
  });
});
