import { describe, expect, it } from "vitest";
import { buildCsvReport } from "./export";

describe("Finsight exports", () => {
  it("builds a source-attributed CSV with all verified report sections", () => {
    const csv = buildCsvReport();
    expect(csv.startsWith("\ufeffFinsight v1")).toBe(true);
    expect(csv).toContain("NPCI UPI Ecosystem Statistics");
    expect(csv).toContain("monthly,2023-11-01,11160.79");
    expect(csv).toContain("projection,2025-11-01,20218.51");
    expect(csv).toContain("ranking,2025-10-01,PhonePe");
    expect(csv.split("\n").length).toBeGreaterThan(130);
  });
});
