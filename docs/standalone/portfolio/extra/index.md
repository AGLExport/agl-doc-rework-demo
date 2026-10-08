---
title: "Extra demo system"
content_status: authored
---

# Extra demo system

The Extra demo system includes an Instrument Cluster platform with demo software and a minimal-footprint IVI demo. Its Qt-based Instrument Cluster starts from minimal userland, providing a foundation for a small-footprint cluster system. The Slint-based Instrument Cluster is an early example implemented in Rust using the Slint UI toolkit.

Momi IVI provides a lightweight Qt/QML infotainment guest. Its demonstrated deployment uses a container host together with a Cluster guest, so follow the [Small scale integrated system](../../../integrated/index.md) route for the complete integration. Select the profile before initializing its build directory.

| Demo | Runtime and deployment | Image or integration target |
| --- | --- | --- |
| [Qt based Cluster demo](qt-cluster.md) | Qt EGLFS in a dedicated cluster system | `agl-instrument-cluster-standalone-demo` |
| [Slint based Cluster demo](slint-cluster.md) | Rust/Slint in a dedicated cluster system | `agl-instrument-cluster-standalone-demo-slint` |
| [Momi IVI demo](momi-ivi.md) | Qt/QML guest on a container host | `agl-instrument-cluster-container-demo` builds the host and demo guests |

Read [Extra architecture](../../architecture/extra.md), then follow [Setup build environment](../../build/extra/setup.md), [Build target image](../../build/extra/image.md), and [Deploy to board](../../build/extra/deploy.md).

The [dedicated cluster guides](../../build/cluster/index.md) and [container integration guide](../../../integrated/containers/build-guide.md) provide profile-specific detail.
