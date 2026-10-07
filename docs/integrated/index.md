---
title: "AGL integrated system"
content_status: authored
---

# AGL integrated system

Integrated systems combine workloads on shared computing resources. Select the guest isolation and device-access model before choosing a build workspace.

| Integration | Execution model | Start here |
| --- | --- | --- |
| SoDeV | Reference platform with virtualized domains and device interfaces | [Architecture](sodev/architecture.md), then [Build SoDeV](sodev/build.md) |
| Container integration | Guest userlands share one host Linux kernel | [Architecture](containers/architecture.md), then [Build Container integration](containers/build.md) |
| KVM based integration | Host and guest virtual machines | [Build Platform](kvm/build.md) |

The [SoDeV chapter](sodev/index.md) includes guest customization and Unified HMI. [Container integration](containers/index.md) includes container customization, DRM lease management, and Container Manager. [KVM based integration](kvm/index.md) retains its own image and host/guest procedure.

Use [AGL Artifact](../home/index.md) for vehicle E/E architecture context and [Releases & migration](../releases/index.md) to keep workspace, host, and guest revisions compatible.
