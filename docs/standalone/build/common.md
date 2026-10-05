---
title: "Common part"
content_status: authored
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

## Further reading

- [Build an AGL image](common/build-image.md)
- [AGL image build workflow](common/build-overview.md)
- [Download AGL source](common/download-source.md)
- [Build and run on AWS EC2](common/hardware/aws-ec2.md)
- [Build and boot on Raspberry Pi](common/hardware/raspberry-pi.md)
- [Raspberry Pi camera setup](common/hardware/raspberry-pi/camera.md)
- [Raspberry Pi peripheral setup](common/hardware/raspberry-pi/devices.md)
- [Raspberry Pi display setup](common/hardware/raspberry-pi/display.md)
- [Build and boot on R-Car Gen3](common/hardware/renesas-rcar-gen3.md)
- [Build and boot on Rockchip boards](common/hardware/rockchip.md)
- [Build and boot on Sparrow Hawk](common/hardware/sparrow-hawk.md)
- [Build and boot on VisionFive2](common/hardware/visionfive2.md)
- [Build and boot on x86](common/hardware/x86.md)
- [Initialize the AGL build environment](common/initialize-build.md)
- [meta-agl-demo](common/layers/meta-agl-demo.md)
- [meta-agl-devel](common/layers/meta-agl-devel.md)
- [meta-agl](common/layers/meta-agl.md)
- [AGL Yocto layer structure](common/layers/overview.md)
- [Prepare a build host](common/prepare-host.md)
- [Hardware image configurations](common/reference/hardware-images.md)
- [Hardware support levels and boards](common/reference/hardware.md)
- [AGL image targets](common/reference/images.md)
- [Choose a board and image](common/reference/matrix.md)
