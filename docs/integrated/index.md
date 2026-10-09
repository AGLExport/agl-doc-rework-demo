---
title: "Small scale integrated system"
content_status: authored
---

# Small scale integrated system

AGL develops and provides a base platform for small-scale integrated systems. It integrates two or more features into a single system by combining one or more AGL Linux distributions and/or other platforms. This category mainly addresses domain-level consolidation, such as running Instrument Cluster and IVI together on one board.

The integration uses Linux Container technology or Kernel-based Virtual Machine (KVM). Select the guest isolation and device-access model before choosing a build workspace.

| Integration | Execution model | Start here |
| --- | --- | --- |
| [Container integration](containers/index.md) | Separate guest userlands share one host Linux kernel through LXC | [Architecture](containers/architecture.md), then [Build Container integration](containers/build.md) |
| [KVM based integration](kvm/index.md) | Virtual machines have their own guest kernels on a Linux KVM/QEMU host | [Build Platform](kvm/build.md) |

Container integration includes guest customization, DRM lease management and Container Manager. KVM retains its own image and host/guest procedure. In both cases, host configuration determines access to displays, networks, storage and devices.

A small-scale integration can itself be incorporated into a [Large scale integrated system](large-scale.md) based on SoDeV. The outer platform then determines how its guest environment receives resources and device interfaces.

Use [Introduction](../home/index.md) for vehicle E/E architecture context and [Releases & migration](../releases/index.md) to keep workspace, host and guest revisions compatible.
