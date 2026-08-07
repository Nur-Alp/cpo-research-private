# STD-008 — IEEE P802.3dj Key Motions (200G/lane electrical baseline)

- **Publisher:** IEEE 802.3 P802.3dj Task Force
- **Date:** 16 May 2024 (key-motions compilation)
- **Canonical source:** [Key motions PDF](https://www.ieee802.org/3/dj/projdoc/KeyMotions_3dj_240516.pdf)
- **Local preservation:** `STD-008-ieee-p8023dj-key-motions-2024.pdf`
- **Review status:** Read on 2026-08-07

## What it establishes

The task force recorded adoption of a 200 Gb/s-per-lane baseline for the relevant PMAs and adopted a die-to-die insertion-loss objective of **≤40 dB at 53.125 GHz** for 200GBASE-CR1, 400GBASE-CR2, 800GBASE-CR4 and 1.6TBASE-CR8 PHYs. The same record includes adopted BER-allocation motions for 200G/lane AUIs, while noting that the C2C/C2M split and measurement method were still to be determined in that motion.

These are standards-work baselines for 200G/lane electrical interfaces, not a 400G/lane LPO requirement and not evidence of a shipped system. The IEEE P802.3dj public area remains a task-force work area; the companion 400 Gb/s/lane study group is separate and has not supplied an adopted 400G/lane electrical channel budget in the material reviewed here.

## How to use it

Use the 40 dB at 53.125 GHz value only as a clearly labelled 200G/lane standards anchor. It should not be compared numerically with the 106 GHz, 212.5-GBd model in `PAP-011` without matching endpoints, package/host boundaries, FEC and measurement definitions.

