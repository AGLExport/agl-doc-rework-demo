---
title: Raspberry Pi 4/5
source_path: 01_Getting_Started/01_Quickstart/01_Using_Ready_Made_Images.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# Raspberry Pi 4/5

Use a Raspberry Pi 4 or 5, a suitable display, network access, and a microSD card. Select the image for the exact board; Pi 4 and Pi 5 images are not interchangeable.

## Download the Flutter IVI image

The configured channel is **{{ agl.codename }} / {{ artifact_kind }}**. The following artifact directories were checked on 7 October 2026; select matching files from your chosen release/build.

| Board | Artifact directory | Image |
| --- | --- | --- |
| Raspberry Pi 4 | [Pi 4 images]({{ agl_download_base }}/latest/raspberrypi4/deploy/images/raspberrypi4-64/) | `agl-ivi-demo-flutter-raspberrypi4-64.wic.zst` |
| Raspberry Pi 5 | [Pi 5 images]({{ agl_download_base }}/latest/raspberrypi5/deploy/images/raspberrypi5/) | `agl-ivi-demo-flutter-raspberrypi5.wic.zst` |

Download the selected compressed WIC image. This disk image includes the board's boot files and filesystem. Use the filenames and compression provided by your release.

## Write the microSD card

Run these commands on the **host**. Identify the removable card with `lsblk` and unmount its mounted partitions.

```sh
lsblk
```

!!! warning "Choose the card device carefully"
    Writing the image replaces the selected device's contents. Confirm the device every time. Replace `/dev/sdX` with the whole microSD device, not a partition or the host's system disk.

Set the downloaded filename and verified card device, then write the image:

```sh
IMAGE=agl-ivi-demo-flutter-raspberrypi4-64.wic.zst  # use the Pi 5 filename for Pi 5
SD_DEVICE=/dev/sdX                             # replace after checking lsblk
zstd -dc "$IMAGE" | sudo dd of="$SD_DEVICE" bs=4M conv=fsync status=progress
sync
```

## Boot and check

Insert the card, connect the display/network, and power on the board. Confirm that the Flutter homescreen appears. Use the [board build/boot guide](../../../build/reference/common/hardware/raspberry-pi.md) for display and board-specific notes. The presence of a downloaded artifact does not establish validation for every display or peripheral combination.

When the target has a network address, connect from the host if the image's login configuration permits it:

```sh
ssh root@<target-ip-address>
```

See [Flutter IVI demo](../reference/flutter.md) for an explanation of the UI and [Troubleshooting](../../../../../../troubleshooting/index.md) for logs and boot diagnosis.
