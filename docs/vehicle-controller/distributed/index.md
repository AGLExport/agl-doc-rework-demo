---
title: Distributed system
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Distributed system

AGL develops and provides a Linux distribution for automotive systems. It focuses on a standalone system built on a single Linux kernel and userland. Deploy it on an individual ECU, or connect several such systems across a vehicle network. Each deployment runs the software selected for its vehicle role and exchanges data through the configured interfaces.

The [AGL Distribution](agl-distribution/index.md) chapter describes this Linux platform and provides the complete path from running a prebuilt demo to building, customizing and developing applications. It contains Quick start, Portfolio, Architecture, Build AGL system, AGL Components, Platform Customize and Application development.

## Vehicle roles

IVI and Instrument Cluster reference software is introduced in the [Basic demo system](agl-distribution/portfolio/basic-demo/index.md) and [Extra demo system](agl-distribution/portfolio/extra-demo/index.md) portfolios. The [Connected Gateway](../../vehicle-data/connected-gateway/index.md) chapter describes the vehicle-data role of the AGL gateway image. Its [Architecture](../../vehicle-data/connected-gateway/architecture/index.md) is TBD.

<span id="platform"></span>
<span id="hardware"></span>

Select a demo in [AGL Distribution](agl-distribution/index.md), then follow its Basic or Extra build sequence. The [board and image matrix](agl-distribution/build/reference/common/reference/matrix.md) provides supporting hardware information.

<span id="apps"></span>

Use [AGL Components](agl-distribution/components/index.md) for reference applications, services, lifecycle and APIs. Continue with [Platform Customize](agl-distribution/customize/index.md) or [Application development](agl-distribution/applications/index.md) to change the distribution or its applications.

## Integration with other platforms

For guest isolation and shared computing resources, use [Small-scale integrated system](../small-integrated/index.md) or [Large-scale integrated system](../large-integrated/index.md). An AGL distribution can provide an integrated system's guest userland; its kernel, device access and deployment format depend on the container or virtual-machine environment. Follow that integration's build procedure when assembling host and guest artifacts.
