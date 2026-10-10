---
title: Base platform for Vehicle Controller
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Base platform for Vehicle Controller

AGL provides platforms for vehicle-resident software, including infotainment and Instrument Cluster demonstrations. This chapter groups the platforms by how workloads share computing resources and operating systems. Use [Introduction](../introduction/index.md#vehicle-ee-architectures) for their relationship to vehicle E/E architecture.

| System | Execution model | Development route |
| --- | --- | --- |
| [Distributed system](distributed/index.md) | One Linux kernel and userland per standalone deployment | [AGL Distribution](distributed/agl-distribution/index.md), then its demo and build guides |
| [Small-scale integrated system](small-integrated/index.md) | Two or more functions share a container or KVM host | [Container integration](small-integrated/container-integration/index.md) or [KVM based integration](small-integrated/kvm/index.md) |
| [Large-scale integrated system](large-integrated/index.md) | SoDeV combines guest systems and mixed-criticality workloads | [SoDeV architecture](large-integrated/sodev/architecture/index.md), then [Build SoDeV](large-integrated/sodev/build/index.md) |

Select the workload and isolation model before the board and build configuration. A distributed AGL image can also supply a guest in an integrated platform; follow that integration's procedure when assembling host and guest artifacts.

For vehicle-signal acquisition and sharing, continue with [Base platform for Vehicle Data Processing](../vehicle-data/index.md). Use [Development & Usage](../development/index.md) for tools and application workflows. This documentation follows AGL master; [Releases & migration](../community/releases/index.md) explains how to record a reproducible source baseline.
