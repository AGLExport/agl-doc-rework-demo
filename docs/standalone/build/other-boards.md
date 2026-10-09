---
title: Supported the other boards
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Supported the other boards

Use the board's BSP and boot requirements with the image selected in Basic or Extra AGL system. A board appearing in the source tree does not establish support for every demo combination.

| Target | Build and deployment reference |
| --- | --- |
| x86 emulation and hardware | [x86](common/hardware/x86.md) |
| Raspberry Pi 4/5 | [Raspberry Pi](common/hardware/raspberry-pi.md) |
| Renesas R-Car Gen3 | [R-Car Gen3](common/hardware/renesas-rcar-gen3.md) |
| Retronix Sparrow Hawk / R-Car V4H | [Sparrow Hawk](common/hardware/sparrow-hawk.md) |
| Rockchip / NanoPC-T6 | [Rockchip](common/hardware/rockchip.md) |
| StarFive VisionFive2 | [VisionFive2](common/hardware/visionfive2.md) |
| AWS EC2 arm64 or x86-64 | [AWS EC2](common/hardware/aws-ec2.md) |

1. Check the [board/image matrix](common/reference/matrix.md), [support levels](common/reference/hardware.md), and release-specific [hardware image configurations](common/reference/hardware-images.md).
2. Follow the board's firmware, graphics-driver, and source prerequisites.
3. Initialize a new build directory for its actual `MACHINE` and the selected profile's features.
4. Build the target recipe from [Basic](basic/image.md) or [Extra](extra/image.md).
5. Deploy with the board guide's artifact format and bootloader procedure.

Use [Common build reference](common.md) for shared setup and layer documentation. Dedicated cluster and Momi support is limited to their documented profile/board combinations; the generic board list does not extend those profiles automatically.
