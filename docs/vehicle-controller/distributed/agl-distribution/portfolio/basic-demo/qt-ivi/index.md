---
title: Qt IVI demo
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Qt IVI demo

The Qt IVI demo provides a Qt homescreen and infotainment applications such as dashboard, HVAC, media, and settings. The image target is `agl-ivi-demo-qt`; use its matching SDK when developing Qt applications.

- [Qt IVI homescreen](../../../components/reference-applications/qt-homescreen/index.md) explains launcher and lifecycle integration.
- [Basic architecture](../../../architecture/basic-demo/index.md) explains the compositor and platform services.
- [Setup](../../../build/basic/setup/index.md), [build](../../../build/basic/image/index.md), and [deployment](../../../build/basic/deploy/index.md) provide the complete image workflow.
- [Qt application](../../../applications/qt/index.md) provides the SDK and application workflow.
- [Target-specific build notes](../../../build/basic/reference/ivi/qt-ivi-demo.md) retain the direct image command.

See the [upstream image recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-ivi-demo-qt.bb) for the applications included at your source revision. Selecting this Qt image does not select the dedicated Instrument Cluster profile.
