---
title: Run Flutter IVI demo pre-build image
source_path: 01_Getting_Started/01_Quickstart/01_Using_Ready_Made_Images.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# Run Flutter IVI demo pre-build image

Run the complete Flutter IVI demo without building AGL from source. It includes a homescreen, infotainment applications, and the services needed by the selected image. Read [the demo overview](reference/flutter.md) for its functions and image variants.

1. Choose a version using [Releases & migration](../../../../../community/releases/index.md).
2. Select one boot route below.
3. Download the board-specific image and, for QEMU, a matching kernel.
4. Boot the target and confirm that the Flutter homescreen appears.
5. Collect the build identifier and logs if startup fails.

| Environment | Procedure |
| --- | --- |
| Linux host with QEMU and KVM | [QEMU x86-64](qemu-x86-64/index.md) |
| Raspberry Pi 4 or 5 with a microSD card | [Raspberry Pi 4/5](raspberry-pi/index.md) |

The QEMU procedure covers the launch command and VNC display. The Raspberry Pi procedure covers image selection, writing the card, and startup checks. Keep the kernel, image, and SDK on the same release or build.

Continue with the [Flutter IVI portfolio entry](../../portfolio/basic-demo/flutter-ivi/index.md) or [Flutter IVI homescreen](../../components/reference-applications/flutter-homescreen/index.md).

<span id="qemu-x86-64"></span>
<span id="raspberry-pi-4"></span>
