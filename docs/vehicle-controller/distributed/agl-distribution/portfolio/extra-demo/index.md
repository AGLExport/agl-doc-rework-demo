---
title: Extra demo system
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Extra demo system

The Extra demo system includes an Instrument Cluster platform with demo software and a minimal-footprint IVI demo. Its Qt-based Instrument Cluster starts from minimal userland, providing a foundation for a small-footprint cluster system. The Slint-based Instrument Cluster is an early example implemented in Rust using the Slint UI toolkit.

Momi IVI provides a lightweight Qt/QML infotainment guest. Its demonstrated deployment uses a container host together with a Cluster guest, so follow the [Small-scale integrated system](../../../../small-integrated/index.md) route for the complete integration. Select the profile before initializing its build directory.

| Demo | Runtime and deployment | Image or integration target |
| --- | --- | --- |
| [Qt based Cluster demo](qt-cluster/index.md) | Qt EGLFS in a dedicated cluster system | `agl-instrument-cluster-standalone-demo` |
| [Slint based Cluster demo](slint-cluster/index.md) | Rust/Slint in a dedicated cluster system | `agl-instrument-cluster-standalone-demo-slint` |
| [Momi IVI demo](momi-ivi/index.md) | Qt/QML guest on a container host | `agl-instrument-cluster-container-demo` builds the host and demo guests |

Read [Extra architecture](../../architecture/extra-demo/index.md). For the dedicated Qt/Slint clusters, follow [Setup build environment](../../build/extra/setup/index.md), [Build target image](../../build/extra/image/index.md) and [Deploy to board](../../build/extra/deploy/index.md). For Momi, follow the [container demo build route](../../../../small-integrated/container-integration/demo-image/momi-ivi/index.md).

The [dedicated cluster guides](../../build/extra/reference/cluster/index.md) and [container integration guide](../../../../small-integrated/container-integration/reference/build-guide.md) provide profile-specific detail.
