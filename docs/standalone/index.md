---
title: "Distributed system"
content_status: authored
---

# Distributed system

AGL develops and provides a Linux distribution for automotive systems. It focuses on a standalone system built on a single Linux kernel and userland. Deploy it on an individual ECU, or connect several such systems across a vehicle network. Choose a demo from the portfolio, understand its architecture, and then build and deploy the selected image.

Basic and Extra are the documentation's groups for the demos below. They are not names of `aglsetup.sh` features; each target has its own actual feature list.

| Goal | Chapter |
| --- | --- |
| Run a ready-made Flutter IVI image | [Quick start](../start/index.md) |
| Compare demos and their intended roles | [Portfolio](portfolio/index.md) |
| Understand runtimes, services, and display access | [Architecture](architecture/index.md) |
| Prepare source, build an image, and boot a target | [Build AGL system](build/index.md) |
| Understand reference applications, services, lifecycle, and APIs | [AGL Components](../components/index.md) |
| Change image contents, recipes, and services | [Platform Customize](customize/index.md) |
| Build and deploy Flutter or Qt applications | [Application development](applications/index.md) |

<span id="platform"></span>
<span id="hardware"></span>

Follow the Basic or Extra build sequence after selecting a demo. The [board and image matrix](build/common/reference/matrix.md) provides supporting hardware information.

<span id="apps"></span>

Read [AGL Components](../components/index.md) for the reference applications, services, framework, and APIs used by a distributed system. Continue with the sibling chapters [Platform Customize](customize/index.md) or [Application development](applications/index.md) to change platform behavior or applications. For guest isolation and shared computing resources, use [Small scale integrated system](../integrated/index.md) or [Large scale integrated system](../integrated/large-scale.md).

## Vehicle roles

IVI and Instrument Cluster reference software is introduced in the [Basic demo system](portfolio/basic/index.md) and [Extra demo system](portfolio/extra/index.md) portfolios. AGL also provides a Connected Gateway platform; its detailed overview and setup remain **TBD**. Existing references are the [gateway image catalog entry](build/common/reference/images.md#agl-gateway-demo) and [Gateway APIs](../components/api/gateway.md).
