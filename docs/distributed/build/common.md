---
title: Common part
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Common part

Complete the shared build preparation before choosing an IVI or Instrument Cluster image.

1. Read the [build workflow](common/build-overview.md) and [host requirements](common/prepare-host.md).
2. [Download the source](common/download-source.md) for your release.
3. [Initialize the build](common/initialize-build.md) with a target `MACHINE`, build directory, and profile features.
4. Select an image from the [IVI](ivi/index.md) or [Instrument Cluster](cluster/index.md) chapter.
5. Follow the [generic image build steps](common/build-image.md) and a board guide to deploy the result.

Use the [board and image matrix](common/reference/matrix.md), [hardware support reference](common/reference/hardware.md), and [image catalog](common/reference/images.md) to choose a target. The documented Yocto baseline is **{{ yocto.codename }} / {{ yocto.version }}**; check release-specific host requirements.

## Board guides

| Target | Guide |
| --- | --- |
| x86 | [Build and boot](common/hardware/x86.md) |
| Raspberry Pi 4/5 | [Build and boot](common/hardware/raspberry-pi.md) |
| Renesas R-Car Gen3 | [Build and boot](common/hardware/renesas-rcar-gen3.md) |
| Sparrow Hawk | [Build and boot](common/hardware/sparrow-hawk.md) |
| Rockchip / NanoPC-T6 | [Build and boot](common/hardware/rockchip.md) |
| VisionFive2 | [Build and boot](common/hardware/visionfive2.md) |
| AWS EC2 | [Build and run](common/hardware/aws-ec2.md) |

The board guides retain the supplied procedures. Their presence is not a claim that every image has been validated on every board.
