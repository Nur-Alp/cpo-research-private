# CMP-078 — CoreWeave Spectrum-X platform benchmark without CPO SKU

**Canonical source:** https://www.coreweave.com/blog/coreweave-trains-deepseek-v3-in-two-minutes
**Reviewed:** 2026-08-12

CoreWeave reports an 8,192-GPU MLPerf training benchmark using the NVIDIA
Spectrum-X Ethernet networking platform.

The post does not identify `SN6800`, `SN6810`, the matching `-LD` ordering
labels, or whether the switches in the benchmark used CPO or pluggable optics.
It therefore provides platform-scale deployment context only and cannot be
used as a Spectrum-X CPO unit or port numerator.
