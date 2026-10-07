---
title: "Extra AGL system"
content_status: authored
---

# Extra AGL system

Extra covers a dedicated cluster userland and a lightweight Qt IVI guest. Select a profile before initializing its build directory.

| Demo | Runtime and deployment | Image or integration target |
| --- | --- | --- |
| [Qt based Cluster demo](qt-cluster.md) | Qt EGLFS in a dedicated cluster system | `agl-instrument-cluster-standalone-demo` |
| [Slint based Cluster demo](slint-cluster.md) | Rust/Slint in a dedicated cluster system | `agl-instrument-cluster-standalone-demo-slint` |
| [Momi IVI demo](momi-ivi.md) | Qt/QML guest on a container host | `agl-instrument-cluster-container-demo` builds the host and demo guests |

Read [Extra architecture](../../architecture/extra.md), then follow [Setup build environment](../../build/extra/setup.md), [Build target image](../../build/extra/image.md), and [Deploy to board](../../build/extra/deploy.md).

The [dedicated cluster guides](../../build/cluster/index.md) and [container integration guide](../../../integrated/containers/build-guide.md) provide profile-specific detail.
