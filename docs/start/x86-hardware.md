---
title: "Run AGL on x86-64 physical system"
source_path: "01_Getting_Started/01_Quickstart/01_Using_Ready_Made_Images.md"
content_status: imported
---

# Run AGL on x86-64 physical system

## Before you start

A UEFI-capable x86-64 system and a USB drive.

Use artifacts from the same AGL build. The configured channel is **{{ agl.codename }} / {{ artifact_kind }}**.

## Start AGL

**NOTE :** UEFI enabled system is required.

  1. Download the [compressed prebuilt image]({{ agl_download_base }}/latest/qemux86-64/deploy/images/qemux86-64/agl-ivi-demo-qt-qemux86-64.wic.zst).

  2. Extract the image into USB drive :

     ```sh
     $ lsblk
     $ sudo umount <usb_device_name>
     $ zstdcat -d agl-ivi-demo-qt-qemux86-64.wic.zst | sudo dd of=<usb_device_name> bs=4M
     $ sync
     ```


  3. Boot from USB drive on the x86 system.

## Confirm the result

Confirm that the AGL console or demo UI starts. Check the image and kernel names if boot fails, and record the build identifier before reporting a problem.

## Next steps

- [Troubleshooting](../troubleshooting/index.md)
- [Develop an application](../develop/index.md#apps)
- [Choose another environment](prebuilt-images.md)
