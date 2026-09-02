/* Signal Ledger export utilities: local-only downloads, source-attributed, no backend. */
import html2canvas from "html2canvas";
import jsPDF from "jspdf";
import { finsightData } from "@/data/finsightData";

const downloadBlob = (blob: Blob, filename: string) => {
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = filename;
  anchor.click();
  window.setTimeout(() => URL.revokeObjectURL(url), 1000);
};

const csvEscape = (value: unknown) => {
  const text = String(value ?? "");
  return /[",\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
};

export function buildCsvReport() {
  const rows: string[][] = [
    ["Finsight v1 — verified monthly aggregates"],
    ["Source", "NPCI UPI Ecosystem Statistics"],
    ["Window", "2023-11-01 to 2025-10-01; 19 verified months of 24 calendar months"],
    [],
    ["section", "month_start", "volume_mn", "value_cr", "top2_share_pct", "gap_from_prior_month"],
    ...finsightData.monthly.map((row) => ["monthly", row.month_start, String(row.volume_mn), String(row.value_cr), String(row.top2_share_pct), String(row.gap_from_prior_month)]),
    [],
    ["section", "month", "projected_volume_mn", "lower_95", "upper_95"],
    ...finsightData.projection.map((row) => ["projection", row.month, String(row.projected_volume_mn), String(row.lower_95), String(row.upper_95)]),
    [],
    ["section", "month_start", "app_name", "rank", "volume_mn", "share_pct"],
    ...finsightData.rankings.map((row) => ["ranking", row.month_start, row.app_name, String(row.rank), String(row.volume_mn), String(row.share_pct)]),
  ];
  return `\ufeff${rows.map((row) => row.map(csvEscape).join(",")).join("\n")}\n`;
}

export function downloadCsvReport() {
  downloadBlob(new Blob([buildCsvReport()], { type: "text/csv;charset=utf-8" }), "finsight-v1-report.csv");
}

function sliceCanvas(source: HTMLCanvasElement, y: number, height: number) {
  const slice = document.createElement("canvas");
  slice.width = source.width;
  slice.height = height;
  const context = slice.getContext("2d");
  if (!context) throw new Error("Could not create PDF canvas");
  context.fillStyle = "#F8F4EB";
  context.fillRect(0, 0, slice.width, slice.height);
  context.drawImage(source, 0, y, source.width, height, 0, 0, source.width, height);
  return slice.toDataURL("image/jpeg", 0.9);
}

export async function downloadPdfReport() {
  const element = document.querySelector<HTMLElement>(".main-canvas");
  if (!element) throw new Error("Dashboard surface not found");
  const canvas = await html2canvas(element, {
    backgroundColor: "#F8F4EB",
    scale: Math.min(window.devicePixelRatio || 1, 1.5),
    useCORS: true,
    logging: false,
    windowWidth: document.documentElement.scrollWidth,
    windowHeight: document.documentElement.scrollHeight,
  });
  const pdf = new jsPDF({ orientation: "portrait", unit: "pt", format: "a4", compress: true });
  const pageWidth = pdf.internal.pageSize.getWidth();
  const pageHeight = pdf.internal.pageSize.getHeight();
  const margin = 20;
  const contentWidth = pageWidth - margin * 2;
  const sliceHeight = Math.floor((pageHeight - margin * 2) * (canvas.width / contentWidth));
  let y = 0;
  let page = 0;
  while (y < canvas.height) {
    if (page > 0) pdf.addPage();
    const height = Math.min(sliceHeight, canvas.height - y);
    const dataUrl = sliceCanvas(canvas, y, height);
    const renderedHeight = (height / canvas.width) * contentWidth;
    pdf.addImage(dataUrl, "JPEG", margin, margin, contentWidth, renderedHeight, undefined, "FAST");
    pdf.setFontSize(7);
    pdf.setTextColor("#7C837B");
    pdf.text(`Finsight v1 · source-attributed dashboard export · page ${page + 1}`, margin, pageHeight - 8);
    y += height;
    page += 1;
  }
  pdf.save("finsight-v1-dashboard-report.pdf");
}
