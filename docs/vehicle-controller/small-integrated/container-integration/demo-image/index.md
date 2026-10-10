---
title: Demo image for container integration
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Demo image for container integration

The master IC/IVI container demonstration supplies a host Linux kernel and isolated guest userlands. The default integrated target combines an Instrument Cluster guest with the lightweight Momi IVI guest.

| Composition | Guest images | Build entry |
| --- | --- | --- |
| Default type 2a | `guest-image-cluster-demo` and `guest-image-ivi-demo` (Momi) | [Momi IVI demo](momi-ivi/index.md) |
| Type 2b with full IVI demos | Default guests plus separately built Flutter/Qt IVI root filesystems | [Detailed profile guide](../reference/build-guide.md) |

Build the complete `agl-instrument-cluster-container-demo` host image. The [master host recipe](https://git.automotivelinux.org/AGL/meta-agl-devel/tree/meta-agl-ic-container/recipes-platform/images/agl-instrument-cluster-container-demo.bb?h=master) selects the default guests and Container Manager configuration. Guest root filesystems need host storage, registration and display allocation before they can run.

Start with [Architecture](../architecture/index.md), then [Build Container integration](../build/index.md). Use [AGL Components](../components/index.md) to distinguish host extensions from guest applications.
