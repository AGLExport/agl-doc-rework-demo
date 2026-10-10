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
| [Basic AGL system](basic/index.md) | Flutter IVI, Qt IVI, IVI-based Flutter Cluster | [Setup](basic/setup.md) → [Build](basic/image.md) → [Deploy](basic/deploy.md) |
| [Extra AGL system](extra/index.md) | Dedicated Qt Cluster and Slint Cluster | [Setup](extra/setup.md) → [Build](extra/image.md) → [Deploy](extra/deploy.md) |
| [Supported the other boards](other-boards.md) | Additional hardware and cloud targets | Check BSP requirements and the supported image combination first. |

Use [Common build reference](common.md) for shared host, source, cache, layer, and hardware documentation. It supplements these routes. Container and KVM host/guest builds belong in [Base platform for the small-scale integrated system](../../small-integrated/index.md); SoDeV workspaces belong in [Base platform for the large-scale integrated system](../../large-integrated/index.md).

Before building, record the resolved master manifest through [Releases & migration](../../releases/index.md). Keep the source, SDK, and deployed artifacts aligned.
