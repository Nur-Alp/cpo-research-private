# STD-007 — OIF Next Generation CEI-224G Framework

- **Publisher:** Optical Internetworking Forum (OIF)
- **Date:** 7 February 2022
- **Canonical source:** [OIF-FD-CEI-224G-01.0](https://www.oiforum.com/wp-content/uploads/OIF-FD-CEI-224G-01.0.pdf)
- **Local preservation:** `STD-007-oif-cei-224g-framework.pdf`
- **Review status:** Read and text-extracted on 2026-08-07

## What it establishes

The framework is an OIF consensus document identifying application spaces and technical questions for future 224 Gb/s-per-lane electrical interfaces. It explicitly says that it does not define a specific technical solution or prioritize the application spaces.

Its historical table lists 224 Gb/s per lane as a target for 200/400/800/1600G systems, with the 224G insertion-loss and pre-FEC BER values still **TBD**. This is important: the document is a standards-development context, not a final 224G channel budget.

The architecture map distinguishes:

- die-to-optical-engine links within an MCM/CPO package, typically under 50 mm of package-substrate trace;
- chip-to-nearby-OE links, anticipated under 150 mm of PCB trace; and
- chip-to-module links that can exceed 200 mm of host PCB trace, plus a connector and at least 20 mm of module trace.

For the chip-to-module case it explicitly discusses linear chip-to-OE interfaces for CPO, NPO and VSR applications. The framework therefore supports a topology argument for moving optics inward as electrical reach and loss rise, but it does not prove that CPO wins on cost, yield, reliability or deployment.

## How to use it

Use this source as a primary architecture-boundary anchor alongside the measured/modelled papers in `02-architecture/linear-drive-boundary-benchmark.md`. Do not treat the historical 224G row, the sub-50-mm / sub-150-mm examples, or the framework's discussion of CPO/NPO as adopted product requirements.

