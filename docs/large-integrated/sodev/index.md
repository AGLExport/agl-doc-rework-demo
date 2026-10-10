---
title: SoDeV
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# SoDeV

SoDeV is AGL's large-scale integrated system reference platform for software-defined vehicles. It supports large-scale mixed-criticality designs by combining workloads in configured guest domains. [Base platform for the distributed systems](../../distributed/index.md) and [small-scale integrated systems](../../small-integrated/index.md) can be integrated on top of SoDeV; their execution environment and device interfaces must match the chosen workspace.

Begin with its domain and device architecture, then build the complete board workspace before customizing guests.

1. [Architecture](architecture.md).
2. [Build SoDeV](build.md).
3. [SoDeV Customize](customize/index.md), including guest VM creation.
4. [Platform extension](extensions.md), including Unified HMI.

The [Base platform for the large-scale integrated system overview](../index.md) provides the official announcement and context. [Build a virtio guest](virtio-guest.md) is a supporting guest-image procedure; it does not replace the workspace's host orchestration.
