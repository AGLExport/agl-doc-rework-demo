---
title: Build AGL system
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Build AGL system

Build the system selected in the portfolio. Each route separates source and host setup, image selection, and board deployment.

| Route | Demos | Sequence |
| --- | --- | --- |
| [Basic AGL system](basic/index.md) | Flutter IVI, Qt IVI, IVI-based Flutter Cluster | [Setup](basic/setup/index.md) → [Build](basic/image/index.md) → [Deploy](basic/deploy/index.md) |
| [Extra AGL system](extra/index.md) | Dedicated Qt Cluster and Slint Cluster | [Setup](extra/setup/index.md) → [Build](extra/image/index.md) → [Deploy](extra/deploy/index.md) |
| [Supported the other boards](other-boards/index.md) | Additional hardware and cloud targets | Check BSP requirements and the supported image combination first. |

Use [Common build reference](reference/common.md) for shared host, source, cache, layer, and hardware documentation. It supplements these routes. Container and KVM host/guest builds belong in [Small-scale integrated system](../../../small-integrated/index.md); SoDeV workspaces belong in [Large-scale integrated system](../../../large-integrated/index.md).

Before building, record the resolved master manifest through [Releases & migration](../../../../community/releases/index.md). Keep the source, SDK, and deployed artifacts aligned.
