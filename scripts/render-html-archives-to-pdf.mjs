#!/usr/bin/env node

// Creates readable, local PDF snapshots for retained publisher HTML archives.
// Requires Playwright to be available to Node, for example from a temporary
// tooling directory: npm install playwright && NODE_PATH=... node this-file.

import { createRequire } from "node:module";
import { readdir, stat } from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";

const require = createRequire(path.join(process.env.PLAYWRIGHT_ROOT || import.meta.dirname, "package.json"));
const { chromium } = require("playwright");

const sourceRoot = path.resolve(import.meta.dirname, "../01-sources");
const replace = process.argv.includes("--replace");
const requested = new Set(process.argv.slice(2).filter((argument) => argument !== "--replace"));

async function walk(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = await Promise.all(entries.map(async (entry) => {
    const fullPath = path.join(directory, entry.name);
    return entry.isDirectory() ? walk(fullPath) : [fullPath];
  }));
  return files.flat();
}

function escapeHtml(value) {
  return String(value || "").replace(/[&<>"]/g, (character) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;",
  })[character]);
}

const archives = (await walk(sourceRoot)).filter((file) => file.endsWith(".html"));
const selected = archives.filter((file) => {
  if (!requested.size) return true;
  return requested.has(path.basename(file)) || requested.has(path.basename(file, ".html"));
});

const browser = await chromium.launch({ headless: true });
let created = 0;
let skipped = 0;
let failed = 0;

for (const archive of selected) {
  const stem = archive.slice(0, -".html".length);
  const output = `${stem}-web-archive.pdf`;

  if (!replace) {
    try {
      await stat(output);
      console.log(`SKIP  ${path.relative(sourceRoot, archive)} (PDF already exists)`);
      skipped += 1;
      continue;
    } catch {
      // No snapshot exists yet.
    }
  }

  const page = await browser.newPage({
    viewport: { width: 1440, height: 1000 },
    deviceScaleFactor: 1,
  });

  try {
    await page.goto(pathToFileURL(archive).href, {
      waitUntil: "domcontentloaded",
      timeout: 20_000,
    });
    const metadata = await page.evaluate(() => ({
      title: document.title,
      description: document.querySelector('meta[name="description"]')?.content || "",
      canonical: document.querySelector('link[rel="canonical"]')?.href
        || document.querySelector('meta[property="og:url"]')?.content || "",
    }));
    const bodyText = await page.locator("body").innerText();
    const fallbackHtml = `<!doctype html>
      <html><head><meta charset="utf-8"><title>${escapeHtml(metadata.title || path.basename(archive))}</title>
      <style>
        @page { size: A4; margin: 22mm 18mm; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color:#172033; line-height:1.55; font-size:12pt; }
        .eyebrow { color:#49627a; font-weight:700; text-transform:uppercase; letter-spacing:.08em; font-size:9pt; }
        h1 { font-size:24pt; line-height:1.18; margin:12mm 0 6mm; }
        .card { margin-top:12mm; padding:7mm; border:1px solid #cad5df; border-left:5px solid #2f6fed; background:#f7fafc; }
        a { color:#185abc; overflow-wrap:anywhere; }
        .small { margin-top:12mm; color:#52606d; font-size:10pt; }
      </style></head><body>
        <div class="eyebrow">Archived source - readable reference card</div>
        <h1>${escapeHtml(metadata.title || path.basename(archive, ".html"))}</h1>
        ${metadata.description ? `<p>${escapeHtml(metadata.description)}</p>` : ""}
        <div class="card"><strong>This publisher page could not be fully rendered from its retained local HTML.</strong>
        The original archive is preserved, but this PDF deliberately avoids presenting a blank or broken page as a readable source.</div>
        <p><strong>Original source:</strong><br><a href="${escapeHtml(metadata.canonical)}">${escapeHtml(metadata.canonical || "See the matching Markdown source card for the canonical link.")}</a></p>
        <p class="small">Use the matching Markdown source card for the archive link, source boundary and research notes.</p>
      </body></html>`;
    let usingFallback = false;

    if (bodyText.trim().length < 200) {
      // Some retained pages are JavaScript shells. A fake blank website PDF is
      // worse than a transparent, usable source card pointing to the original.
      await page.setContent(fallbackHtml, { waitUntil: "commit" });
      usingFallback = true;
      console.warn(`FALLBACK ${path.relative(sourceRoot, archive)} (JavaScript shell; reference card created)`);
    }
    await page.emulateMedia({ media: "screen" });
    await page.addStyleTag({ content: `
      @page { size: A4; margin: 14mm 12mm 16mm; }
      html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
      img, svg, video, canvas { max-width: 100% !important; height: auto !important; }
      pre, code { white-space: pre-wrap !important; overflow-wrap: anywhere !important; }
      /* Remove consent managers from a local archival snapshot only. */
      #onetrust-consent-sdk, .onetrust-pc-dark-filter,
      [id*="cookie" i], [class*="cookie" i],
      [id*="consent" i], [class*="consent" i] { display: none !important; }
    ` });
    await page.evaluate(() => {
      for (const element of document.querySelectorAll("[role='dialog'], [aria-modal='true']")) {
        const text = (element.textContent || "").toLowerCase();
        if (text.includes("cookie") || text.includes("privacy choices") || text.includes("consent")) {
          element.style.setProperty("display", "none", "important");
        }
      }
      document.documentElement.style.overflow = "visible";
      document.body.style.overflow = "visible";
    });
    await page.waitForTimeout(300);
    await page.pdf({
      path: output,
      format: "A4",
      printBackground: true,
      margin: { top: "14mm", right: "12mm", bottom: "16mm", left: "12mm" },
      displayHeaderFooter: true,
      headerTemplate: "<span></span>",
      footerTemplate: `<div style="width:100%; font-size:8px; color:#6b7280; padding:0 12mm; text-align:right;">Archived local rendering · <span class="pageNumber"></span> / <span class="totalPages"></span></div>`,
      preferCSSPageSize: true,
    });
    if (!usingFallback && (await stat(output)).size < 25 * 1024) {
      await page.setContent(fallbackHtml, { waitUntil: "commit" });
      await page.pdf({
        path: output,
        format: "A4",
        printBackground: true,
        margin: { top: "14mm", right: "12mm", bottom: "16mm", left: "12mm" },
        displayHeaderFooter: true,
        headerTemplate: "<span></span>",
        footerTemplate: `<div style="width:100%; font-size:8px; color:#6b7280; padding:0 12mm; text-align:right;">Archived local rendering · <span class="pageNumber"></span> / <span class="totalPages"></span></div>`,
        preferCSSPageSize: true,
      });
      console.warn(`FALLBACK ${path.relative(sourceRoot, archive)} (visually empty rendering; reference card created)`);
    }
    console.log(`DONE  ${path.relative(sourceRoot, output)}`);
    created += 1;
  } catch (error) {
    console.error(`FAIL  ${path.relative(sourceRoot, archive)}: ${error.message}`);
    failed += 1;
  } finally {
    await page.close();
  }
}

await browser.close();
console.log(`Completed: ${created} created, ${skipped} already present, ${failed} failed.`);
process.exitCode = failed ? 1 : 0;
