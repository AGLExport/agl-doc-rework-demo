---
title: Choose a board and image
---
# Choose a board and image

Start with your goal, then match the AGL release, image target, and board. The configured documentation channel is **{{ agl.codename }} / {{ artifact_kind }}**; it is a development channel.

For a first evaluation on a Linux PC, start with the [QEMU x86-64 quickstart](../start/qemu-x86-64.md). A source build is a separate workflow.

| Environment | MACHINE | Documented starting point | Guide |
| --- | --- | --- | --- |
| QEMU x86-64 | qemux86-64 | Prebuilt Qt IVI demo | [Run the image](../start/qemu-x86-64.md) |
| QEMU AArch64 | qemuarm64 | Hardware and artifact reference | [Hardware reference](hardware.md) |
| Raspberry Pi 4 | raspberrypi4 | Prebuilt Qt IVI demo or source build | [Prebuilt](../start/raspberry-pi.md) / [Build](../develop/hardware/raspberry-pi.md) |
| Raspberry Pi 5 | raspberrypi5 | Board and profile-specific source builds | [Build guide](../develop/hardware/raspberry-pi.md) / [IC profile](../develop/demos/instrument-cluster.md) |
| R-Car Gen3 | h3ulcb and related variants | Board-specific source build | [Build guide](../develop/hardware/renesas-rcar-gen3.md) |
| Sparrow Hawk | sparrow-hawk | Board-specific build and IC container profile | [Build guide](../develop/hardware/sparrow-hawk.md) / [IC profile](../develop/demos/instrument-cluster.md) |
| NanoPC-T6 | nanopc-t6 | Rockchip and IC profile guides | [Build guide](../develop/hardware/rockchip.md) / [IC profile](../develop/demos/instrument-cluster.md) |
| Virtio guest | virtio-aarch64 | Virtualized guest build | [Build guide](../develop/hardware/virtio.md) |
| AWS EC2 | aws-ec2-arm64 / aws-ec2-x86-64 | Cloud image build | [Build guide](../develop/hardware/aws-ec2.md) |
| VisionFive2 | visionfive2 | Board-specific source build | [Build guide](../develop/hardware/visionfive2.md) |

## Read support and verification separately

This table is a guide to the supplied documentation, not a release compatibility guarantee. Image availability, feature combinations, and board validation depend on the release.

- [Hardware support levels](hardware.md) explain Reference BSP and Community BSP maintenance.
- [Image targets](images.md) describe IVI, Instrument Cluster, gateway, SDK, and preconfigured demos.
- [Build initialization](../develop/platform/initialize-build.md) lists MACHINE values and features.
- [Hardware image configurations](hardware-images.md) retain the original image recipes.
- [Release guidance](../releases/index.md) links to the official release notes and artifacts.

The imported procedures have not been rerun on hardware as part of this site restructuring. Record the exact release/build identifier, host distribution, image target, MACHINE, features, and test date when validating a combination.

## Select an image

| Goal | Look for | Read next |
| --- | --- | --- |
| Evaluate an IVI user interface | Qt or Flutter IVI demo | [Image targets](images.md) |
| Develop an application | Matching runtime image and SDK/workspace | [Application development](../develop/index.md#apps) |
| Run an Instrument Cluster | IC demo matching the board and profile | [IC container profile](../develop/demos/instrument-cluster.md) or [Slint profile](../develop/demos/slint.md) |
| Integrate a gateway or multi-board demo | Gateway/preconfigured image and its network assumptions | [Image targets](images.md#2-preconfigured-demo-images) |
| Modify the platform | Source build with the required layers and features | [Platform development](../develop/index.md#platform) |

Keep the kernel, root filesystem, SDK, and documentation on the same release or build. Check the [build host requirements](../develop/platform/prepare-host.md) before beginning a source build.
