---
title: Explore the demos
content_status: authored
last_reviewed: 2026-10-04
---

# Explore the Flutter IVI Demo

The Flutter IVI Demo brings AGL's infotainment software together in a working user interface. It combines a Flutter homescreen with vehicle controls, media playback, and system settings on the Yocto-based AGL Unified Code Base. AGL's official demonstration shows how these parts can be used and customized together. [AGL's demo walkthrough](https://www.automotivelinux.org/blog/automotive-grade-linux-at-automotive-world-tokyo-2026/)

## What you can explore

| Area | What to look for |
| --- | --- |
| Homescreen | The entry point for moving between the demo's functions. |
| Climate control | HVAC controls, including air conditioning and synchronization. |
| Media | Playback controls and interaction with the audio system. |
| Settings | The interface for system configuration. |

These are the main functions described in AGL's public walkthrough. The screens and available controls depend on the release, image configuration, and connected devices. [Official Flutter HMI demonstration](https://www.automotivelinux.org/blog/automotive-grade-linux-at-automotive-world-tokyo-2026/)

## How the demo fits together

The standard image target is **`agl-ivi-demo-flutter`**, which includes the **`flutter-ics-homescreen`** application. It builds on `agl-ivi-image-flutter`, the base image containing Flutter runtime components. [Official image catalog](https://docs.automotivelinux.org/en/master/01_Getting_Started/02_Building_AGL_Image/07_Available_Demo_Images/)

The interface uses several platform services:

- **Graphics and application switching:** the Flutter embedder handles Wayland integration; the homescreen activates applications through the compositor integration. The AGL compositor provides the window-management interfaces. [Compositor integration](https://docs.automotivelinux.org/en/unagi/06_Component_Documentation/01_Graphics_Service/01_agl_compositor/#how-to-integrate-or-incorporate-your-own-ui)
- **Audio:** PipeWire provides playback and capture, while WirePlumber manages audio policy and devices. [Audio services](https://docs.automotivelinux.org/en/master/06_Component_Documentation/02_Sound_Service/01_pipewire_wireplumber/)
- **Vehicle data:** the standard demo image includes a KUKSA.val databroker. A multi-board configuration can place the databroker on another device. [Demo image configurations](https://docs.automotivelinux.org/en/master/01_Getting_Started/02_Building_AGL_Image/07_Available_Demo_Images/)

For local explanations and specifications, see [How AGL services fit together](../../explanation/services.md) and the [service catalog](../../reference/services/index.md).

## Choose the right demo image

| Image target | Intended use |
| --- | --- |
| `agl-ivi-demo-flutter` | Start with the standard Flutter IVI demo. |
| `agl-ivi-demo-flutter-preconfigured` | A coordinated demo with Instrument Cluster navigation streaming and the databroker on the IVI board. |
| `agl-ivi-demo-flutter-preconfigured-gateway` | A coordinated demo with the databroker on a separate gateway. |

The preconfigured images assume a particular multi-board network setup. Use the standard image for an initial evaluation; read the [image configuration reference](../../reference/images.md#2-preconfigured-demo-images) before choosing a preconfigured variant. [Official image descriptions](https://docs.automotivelinux.org/en/master/01_Getting_Started/02_Building_AGL_Image/07_Available_Demo_Images/)

## Try the demo

1. Choose an AGL version using [Releases & migration](../../releases/index.md). This site follows the **{{ agl.full_name }} / `{{ agl.codename }}` development branch**.
2. Choose [QEMU x86-64](../qemu-x86-64.md) or [Raspberry Pi 4](../raspberry-pi.md). Use `agl-ivi-demo-flutter` artifacts for that target and keep the kernel and image on the same build. The quickstarts currently use Qt example filenames; substitute the matching Flutter filenames when following those boot steps.
3. Explore the homescreen, climate controls, media, and settings. Check whether the services and devices needed for each function are available in your setup.
4. If a function does not respond, collect the build identifier and logs using [Diagnose common problems](../../troubleshooting/diagnostics.md).

To build the demo from source, follow [Platform development](../../develop/index.md#platform) and select `agl-ivi-demo-flutter` as the image target. To modify its UI or add an application, start with [Set up a Flutter workspace](../../develop/apps/flutter-workspace.md).

## About this overview

This page summarizes official AGL web documentation and the public demo walkthrough, reviewed on **4 October 2026**. The compositor reference above is versioned for Unagi; consult your release's documentation for implementation details. Image contents and feature availability can change between releases.
