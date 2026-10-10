---
title: Base platform for the distributed system
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Base platform for the distributed system

AGL develops and provides a Linux distribution for automotive systems. It focuses on a standalone system built on a single Linux kernel and userland. Deploy it on an individual ECU, or connect several such systems across a vehicle network. Each deployment runs the software selected for its vehicle role and exchanges data through the configured interfaces.

The [AGL Distribution](distribution/index.md) chapter describes this Linux platform and provides the complete path from running a prebuilt demo to building, customizing and developing applications. It contains Quick start, Portfolio, Architecture, Build AGL system, AGL Components, Platform Customize and Application development.

## Vehicle roles

IVI and Instrument Cluster reference software is introduced in the [Basic demo system](portfolio/basic/index.md) and [Extra demo system](portfolio/extra/index.md) portfolios. AGL also provides a Connected Gateway platform; its detailed overview and setup remain **TBD**. Existing references are the [gateway image catalog entry](build/common/reference/images.md#agl-gateway-demo) and [Gateway APIs](../components/api/gateway.md).

<span id="platform"></span>
<span id="hardware"></span>

Select a demo in [AGL Distribution](distribution/index.md), then follow its Basic or Extra build sequence. The [board and image matrix](build/common/reference/matrix.md) provides supporting hardware information.

<span id="apps"></span>

Use [AGL Components](../components/index.md) for reference applications, services, lifecycle and APIs. Continue with [Platform Customize](customize/index.md) or [Application development](applications/index.md) to change the distribution or its applications.

## Integration with other platforms

For guest isolation and shared computing resources, use [Base platform for the small-scale integrated system](../small-integrated/index.md) or [Base platform for the large-scale integrated system](../large-integrated/index.md). An AGL distribution can provide an integrated system's guest userland; its kernel, device access and deployment format depend on the container or virtual-machine environment. Follow that integration's build procedure when assembling host and guest artifacts.
