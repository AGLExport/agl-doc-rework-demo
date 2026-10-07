---
title: "Build AGL system"
content_status: authored
---

# Build AGL system

Build the system selected in the portfolio. Each route separates source and host setup, image selection, and board deployment.

| Route | Demos | Sequence |
| --- | --- | --- |
| [Basic AGL system](basic/index.md) | Flutter IVI, Qt IVI, IVI-based Flutter Cluster | [Setup](basic/setup.md) → [Build](basic/image.md) → [Deploy](basic/deploy.md) |
| [Extra AGL system](extra/index.md) | Qt Cluster, Slint Cluster, Momi IVI | [Setup](extra/setup.md) → [Build](extra/image.md) → [Deploy](extra/deploy.md) |
| [Supported the other boards](other-boards.md) | Additional hardware and cloud targets | Check BSP requirements and the supported image combination first. |

Use [Common build reference](common.md) for shared host, source, cache, layer, and hardware documentation. It supplements these routes. Guest VM and host integration builds belong in [AGL integrated system](../../integrated/index.md).

Before building, choose a release or snapshot through [Releases & migration](../../releases/index.md). Keep the source, SDK, and deployed artifacts aligned.
