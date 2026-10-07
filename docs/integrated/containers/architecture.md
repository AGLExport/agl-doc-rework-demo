---
title: "Architecture"
content_status: authored
---

# Architecture

Container integration provides a lightweight integrated system on Linux. Guests have separate userlands and processes while sharing the host kernel. Display, audio, storage, network, and CAN access therefore depend on host configuration and explicit guest resource assignment.

![Cluster and Momi guests sharing a container host kernel with container management and leased display access.](../../assets/diagrams/extra-system.svg)

| Layer | Responsibility |
| --- | --- |
| Host kernel and board support | Drivers, physical devices, and isolation facilities |
| Container Manager and liblxc | Guest lifecycle, registration, resources, and switching |
| DRM lease manager | Display-resource leases for guest graphics |
| Cluster guest | Cluster GUI and vehicle-data services |
| Momi IVI guest | Qt/QML homescreen, navigation, media, and weather examples |

The [host image recipe](https://git.automotivelinux.org/AGL/meta-agl-devel/tree/meta-agl-ic-container/recipes-platform/images/agl-instrument-cluster-container-demo.bb) assembles cluster and Momi guests through multiconfig. A simple `lxc-host-image-minimal` does not include the same demo composition. Type 2b adds separately built full IVI guests and has extra assembly steps.

Read [DRM lease manager](../../components/services/graphics/drm-lease-manager.md) for graphics ownership and [Container Manager](../../components/extensions/container-manager.md) for guest configuration. The [Momi portfolio](../../standalone/portfolio/extra/momi-ivi.md) describes the guest applications.

Continue with [Build Container integration](build.md) and its [detailed profile guide](build-guide.md), then [Create and Run Guest Container](customize/guest-container.md).
