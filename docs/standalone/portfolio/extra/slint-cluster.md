---
title: Slint based Cluster demo
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Slint based Cluster demo

The Slint cluster is an early example of an Instrument Cluster implemented with Rust and Slint. It uses a dedicated cluster image rather than the Flutter IVI image.

| Setting | Selection |
| --- | --- |
| Features | `agl-demo agl-ic agl-ic-slint` |
| Image | `agl-instrument-cluster-standalone-demo-slint` |
| GUI service | `agl-slint-cluster.service` |
| Documented targets | Raspberry Pi 4/5 and NanoPC-T6 |

The profile adds the Rust and Slint layers through the [upstream feature template](https://git.automotivelinux.org/AGL/meta-agl-devel/tree/templates/feature/agl-ic-slint). The [image recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/meta-agl-demo-shared/dynamic-layers/meta-slint/recipes-platform/images/agl-instrument-cluster-standalone-demo-slint.bb) selects the Slint cluster application.

Follow [Extra setup](../../build/extra/setup.md), [image build](../../build/extra/image.md), and [deployment](../../build/extra/deploy.md). Check the [detailed Slint guide](../../build/cluster/slint.md) for the documented 1920 x 720 display requirement.
