---
title: Choose a board and image
---
# Choose a board and image

Start with your goal, then match the AGL release, image target, and board. The configured documentation channel is **{{ agl.codename }} / {{ artifact_kind }}**; it is a development channel.

For a first evaluation on a Linux PC, start with the [QEMU x86-64 quickstart](../../../../start/prebuilt/qemu-x86-64.md). A source build is a separate workflow.

| Environment | MACHINE | Documented starting point | Guide |
| --- | --- | --- | --- |
| QEMU x86-64 | qemux86-64 | Prebuilt Flutter IVI demo | [Run the image](../../../../start/prebuilt/qemu-x86-64.md) |
| QEMU AArch64 | qemuarm64 | Hardware and artifact reference | [Hardware reference](hardware.md) |
| Raspberry Pi 4 | `raspberrypi4-64` (AGL setup: `raspberrypi4`) | Prebuilt Flutter IVI demo or source build | [Prebuilt](../../../../start/prebuilt/raspberry-pi.md) / [Build](../hardware/raspberry-pi.md) |
| Raspberry Pi 5 | raspberrypi5 | Prebuilt Flutter IVI demo or profile-specific source build | [Prebuilt](../../../../start/prebuilt/raspberry-pi.md) / [Build guide](../hardware/raspberry-pi.md) / [IC profile](../../../../integrated/containers/build-guide.md) |
| R-Car Gen3 | h3ulcb and related variants | Board-specific source build | [Build guide](../hardware/renesas-rcar-gen3.md) |
| Sparrow Hawk | sparrow-hawk | Board-specific build and IC container profile | [Build guide](../hardware/sparrow-hawk.md) / [IC profile](../../../../integrated/containers/build-guide.md) |
| NanoPC-T6 | nanopc-t6 | Rockchip and IC profile guides | [Build guide](../hardware/rockchip.md) / [IC profile](../../../../integrated/containers/build-guide.md) |
| Virtio guest | virtio-aarch64 | Virtualized guest build | [Build guide](../../../../integrated/sodev/virtio-guest.md) |
| AWS EC2 | aws-ec2-arm64 / aws-ec2-x86-64 | Cloud image build | [Build guide](../hardware/aws-ec2.md) |
| VisionFive2 | visionfive2 | Board-specific source build | [Build guide](../hardware/visionfive2.md) |

## Read support and verification separately

This table is a guide to the supplied documentation, not a release compatibility guarantee. Image availability, feature combinations, and board validation depend on the release.

- [Hardware support levels](hardware.md) explain Reference BSP and Community BSP maintenance.
- [Image targets](images.md) describe IVI, Instrument Cluster, gateway, SDK, and preconfigured demos.
- [Build initialization](../initialize-build.md) lists MACHINE values and features.
- [Hardware image configurations](hardware-images.md) retain the original image recipes.
- [Release guidance](../../../../releases/index.md) links to the official release notes and artifacts.

The imported procedures have not been rerun on hardware as part of this site restructuring. Record the exact release/build identifier, host distribution, image target, MACHINE, features, and test date when validating a combination.

## Select an image

| Goal | Look for | Read next |
| --- | --- | --- |
| Evaluate an IVI user interface | Qt or Flutter IVI demo | [Image targets](images.md) |
| Develop an application | Matching runtime image and SDK/workspace | [Application development](../../../index.md#apps) |
| Run an Instrument Cluster | IC demo matching the board and profile | [IC container profile](../../../../integrated/containers/build-guide.md) or [Slint profile](../../cluster/slint.md) |
| Integrate a gateway or multi-board demo | Gateway/preconfigured image and its network assumptions | [Image targets](images.md#2-preconfigured-demo-images) |
| Modify the platform | Source build with the required layers and features | [Platform development](../../../index.md#platform) |

Keep the kernel, root filesystem, SDK, and documentation on the same release or build. Check the [build host requirements](../prepare-host.md) before beginning a source build.
