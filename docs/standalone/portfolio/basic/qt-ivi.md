---
title: Qt IVI demo
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Qt IVI demo

The Qt IVI demo provides a Qt homescreen and infotainment applications such as dashboard, HVAC, media, and settings. The image target is `agl-ivi-demo-qt`; use its matching SDK when developing Qt applications.

- [Qt IVI homescreen](../../../components/applications/qt-homescreen.md) explains launcher and lifecycle integration.
- [Basic architecture](../../architecture/basic.md) explains the compositor and platform services.
- [Setup](../../build/basic/setup.md), [build](../../build/basic/image.md), and [deployment](../../build/basic/deploy.md) provide the complete image workflow.
- [Qt application](../../applications/qt.md) provides the SDK and application workflow.
- [Target-specific build notes](../../build/ivi/qt-ivi-demo.md) retain the direct image command.

See the [upstream image recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-ivi-demo-qt.bb) for the applications included at your source revision. Selecting this Qt image does not select the dedicated Instrument Cluster profile.
