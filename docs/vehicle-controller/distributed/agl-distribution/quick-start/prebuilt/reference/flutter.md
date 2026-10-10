---
title: Flutter IVI demo
content_status: authored
last_reviewed: '2026-10-10'
agl_branch: master
---

# Flutter IVI demo

The Flutter IVI demo runs `flutter-ics-homescreen` on the AGL `master` IVI platform. It combines Home, dashboard, HVAC, media, settings and application selection, with behavior determined by the installed services and connected devices.

## What you can explore

| Area | Demo behavior |
| --- | --- |
| Homescreen and applications | Navigate built-in pages and launch installed applications |
| Vehicle data and climate | Read VSS signals and request supported HVAC changes |
| Media and radio | Control MPD playback and the radio backend |
| Settings and profile | Retain selected data through the persistent storage API |

The [master image recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-ivi-demo-flutter.bb?h=master) extends the Flutter IVI base. Read [Basic architecture](../../../architecture/basic-demo/index.md) for the source-reviewed component diagram and [Flutter IVI homescreen](../../../components/reference-applications/flutter-homescreen/index.md) for client configuration.

## Select a master snapshot

Use the standard **`agl-ivi-demo-flutter`** image for initial evaluation. Choose [QEMU x86-64](../qemu-x86-64/index.md) or [Raspberry Pi 4/5](../raspberry-pi/index.md), and take all required boot artifacts from the same master snapshot directory.

Coordinated IVI/cluster/gateway deployments configure the current images and their KUKSA client/provider packages. Use [Coordinated demo configuration](../../../build/reference/common/reference/images.md#coordinated-demo-configuration); older preconfigured image names are not current master targets.

## Try and develop the demo

1. Read [Releases & migration](../../../../../../community/releases/index.md) to record the selected snapshot/build identifier.
2. Boot with the chosen board's quick-start procedure and confirm the homescreen appears.
3. Check vehicle-data, audio and device services for the functions you want to exercise.
4. Collect logs with [Diagnose common problems](../../../../../../troubleshooting/reference/diagnostics.md) if a function fails.

To build an image, use [Basic AGL system](../../../build/basic/index.md). To modify the UI, use [Flutter application development](../../../applications/flutter/index.md) with the workspace configuration matching the master image.

This overview was checked against master source composition on 10 October 2026. It does not report a hardware or emulator runtime test.
