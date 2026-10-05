---
title: "Hardware support levels and boards"
source_path: "02_Hardware_Support/01_Supported_Hardware_Overview.md"
content_status: imported
---

### Supported Hardware

AGL makes two types of hardware support available: Reference BSPs and Community BSPs.

1) **Reference Boards** have Board Support Packages (BSPs) that are maintained by their sponsoring companies and are included in our Jenkins CI system. Reference BSPs have snapshot builds that are made available daily and are fully validated with test results made available for every major AGL release.

2) **Community Boards** have BSPs that are maintained as a best effort by the AGL community based on upstream BSPs. Community Boards include some of the most-used Hobbyist boards such as older automotive boards.

The following table briefs about the various hardware platforms, supported by AGL :

### AGL Reference Boards

|          BOARD         |     MACHINE    | ARCHITECTURE | QUICK START GUIDE| LATEST SNAPSHOT |
|:----------------------:|:--------------:|:------------:|:----------------:|:--------------------:|
|          QEMU          |   qemu-x86-64  |      x86      |[QEMU Quick Start](../../../../start/prebuilt/index.md)| [qemu-x86-64]({{ agl_download_base }}/latest/qemux86-64/)|
|                        |    qemu-arm    |     arm32     | | [qemu-arm]({{ agl_download_base }}/latest/qemuarm/)|
|                        |   qemu-arm64   |     arm64     | | [qemu-arm64]({{ agl_download_base }}/latest/qemuarm64/)|
|                        |                |               |
|       RCar Gen 3       |     h3ulcb     |     arm64     |[RCar Gen 3 Quick Start](../hardware/renesas-rcar-gen3.md)| [h3ulcb-nogfx]({{ agl_download_base }}/latest/h3ulcb-nogfx/)|
|                        | h3-salvator-x  |     arm64     |
|                        |      h3-kf     |     arm64     |
|                        |     m3ulcb     |     arm64     |
|                        | m3-salvator-x  |     arm64     |
|                        |      m3-kf     |     arm64     |
|                        |   agl-refhw    |     arm64     |
| Sparrow Hawk R-Car V4H | sparrow-hawk   |     arm64     |
|                        |                |               |
|      Raspberry Pi      |  raspberrypi4  |     arm64     |[Raspberry Pi Quick Start](../../../../start/prebuilt/index.md#raspberry-pi-4)|[raspberrypi4]({{ agl_download_base }}/latest/raspberrypi4/)|

**Note:** Latest stable release source tar and binary for all the boards can be found [here](https://wiki.automotivelinux.org/agl-distro/release-notes#latest_stable_release)

### Community Supported Boards

|    BOARD      |      MACHINE          | ARCHITECTURE  |
|:-------------:|:---------------------:|:-------------:|
|  BeagleBone   |        bbe            |     arm32     |
|               |    beaglebone         |     arm32     |
|               |                       |               |
|   i.MX 6      |      cubox-i          |     arm32     |
|               | imx6qdlsabreauto      |     arm32     |
|               |                       |               |
|   i.MX 8      |     imx8mqevk         |     arm64     |
|               |   imx8mqevk-viv       |     arm64     |
|               |                       |               |
|     virtio    | virtio-aarch64        |     arm64     |
