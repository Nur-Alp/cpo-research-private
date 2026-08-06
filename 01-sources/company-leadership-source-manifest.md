# Company leadership source manifest

Access date: 2026-08-06

This manifest maps each provisional company-leadership conclusion to the locally retained official source. The source log remains the canonical metadata index.

| Source ID | Company | Local file | Retained format | Canonical source |
|---|---|---|---|---|
| `CMP-008` | NVIDIA | `product-materials/CMP-008-nvidia-rubin-cpo-production-2026.pdf` | Publisher PDF | <https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer> |
| `CMP-011` | Meta / NVIDIA | `product-materials/CMP-011-meta-nvidia-partnership-2026.html` | Publisher HTML | <https://about.fb.com/news/2026/02/meta-nvidia-announce-long-term-infrastructure-partnership/> |
| `CMP-009` | Broadcom | `product-materials/CMP-009-broadcom-ofc-2026-cpo.pdf` | Publisher PDF | <https://investors.broadcom.com/node/64036/pdf> |
| `CMP-010` | Lumentum | `product-materials/CMP-010-lumentum-q2-fy2026-results.html` | Publisher HTML | <https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Second-Quarter-of-Fiscal-Year-2026-Financial-Results/default.aspx> |
| `PRS-003` | Coherent | `conference-presentations/PRS-003-coherent-ofc-investor-event-2026.pdf` | Publisher PDF | Official Coherent OFC 2026 investor-event material |
| `FIL-001` | Marvell | `filings/FIL-001-marvell-2026-05-02-10q.html` | Publisher-hosted SEC filing HTML | <https://investor.marvell.com/sec-filings/all-sec-filings/content/0001835632-26-000019/mrvl-20260502.htm> |
| `CMP-014` | TSMC | `product-materials/CMP-014-tsmc-coupe-source-note.md` | Local retrieval note | <https://pr.tsmc.com/english/news/3136> |

## Preservation notes

- HTML files are publisher pages saved as received. They may depend on remote styling or images, but their source text remains locally searchable.
- TSMC returned HTTP 403 for both its official HTML page and attached PDF during automated retrieval. `CMP-014` therefore remains URL-canonical; the local note records the failed retrieval and the relevant source boundary without presenting reconstructed text as an original download.
- Local retention does not convert company claims into independently verified facts. Continue to apply the limitations and confidence fields in `source-log.csv`.
