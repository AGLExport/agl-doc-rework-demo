---
title: Build and boot on VisionFive2
source_path: 01_Getting_Started/02_Building_AGL_Image/06_Building_the_AGL_Image/08_Building_for_VisionFive2_Boards.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# Build and boot on VisionFive2

Complete [host preparation](../prepare-host.md) and [source download](../download-source.md) first. These steps define `AGL_TOP` as the parent workspace and `AGL_SOURCE` as the source checkout. Run each setup command from `$AGL_SOURCE`; `aglsetup.sh` then enters its build directory. Use `-f` only when intentionally replacing existing configuration.

AGL supported StarFive [VisionFive2](https://www.starfivetech.com/en/site/boards) board.<br>
The processor of this board is RISC-V RV64GC.

This section describes the steps you need to take to build the AGL demo image for the VisionFive2 board.

## 1. Making Sure Your Build Environment is Correct

The
"[Initializing Your Build Environment](../initialize-build.md)"
section presented generic information for setting up your build environment
using the `aglsetup.sh` script.
If you are building the AGL demo image for a VisionFive2 board, you need to specify some
specific options when you run the script :

**Basic IVI demo :**

  ```sh
  $ cd "$AGL_SOURCE"
  $ source meta-agl/scripts/aglsetup.sh -m visionfive2 -b build-visionfive2 agl-demo
  $ echo "# reuse download directories" >> $AGL_TOP/site.conf
  $ echo "DL_DIR = \"$HOME/downloads/\"" >> $AGL_TOP/site.conf
  $ echo "SSTATE_DIR = \"$AGL_TOP/sstate-cache/\"" >> $AGL_TOP/site.conf
  $ ln -sf $AGL_TOP/site.conf conf/
  ```

In each case, the "-m" option specifies the machine and the list of AGL features used with script are appropriate for development of
the AGL demo image suited for VisionFive2.

## 2. Configuring the Build

Before launching the build, it is good to be sure your build
configuration is set up correctly (`conf/local.conf` in the initialized build directory).
The "[Customizing Your Build](../../../customize/build-output.md)"
section highlights some common configurations that are useful when
building any AGL image.

## 3. Using BitBake

Select a demo target and build it from the initialized build shell:

```sh
IMAGE_TARGET=agl-ivi-demo-flutter  # use agl-ivi-demo-qt for the Qt IVI demo
bitbake "$IMAGE_TARGET"
```

An initial build can take several hours. Check the [host requirements](../prepare-host.md) for resource planning.

Read the resolved output names from your checkout. The BSP MACHINE name and image suffix can differ from the AGL setup-template name or earlier releases:

```sh
DEPLOY_DIR=$(bitbake-getvar --value -r "$IMAGE_TARGET" DEPLOY_DIR_IMAGE)
IMAGE_BASE=$(bitbake-getvar --value -r "$IMAGE_TARGET" IMAGE_LINK_NAME)
IMAGE_SUFFIX=$(bitbake-getvar --value -r "$IMAGE_TARGET" IMAGE_NAME_SUFFIX)
IMAGE_FILE="$DEPLOY_DIR/$IMAGE_BASE$IMAGE_SUFFIX.wic.zst"
ls -lh "$IMAGE_FILE"
```

Use the actual generated WIC image and compression if your configuration differs. Confirm them with `bitbake-getvar -r "$IMAGE_TARGET" IMAGE_FSTYPES`. See [Yocto's variable inspection guide](https://docs.yoctoproject.org/{{ yocto.codename }}/dev-manual/debugging.html#viewing-variable-values).

## 4. Deploying the AGL Demo Image

Deploying the AGL demo image consists of copying the image on a MicroSD card,
plugging the card into the VisionFive2 board, and then booting the board.

Follow these steps to copy the image to a MicroSD card and boot
the image on the VisionFive2 board:

  1. Plug your MicroSD card into your Build Host (i.e. the system that has your build output), and unmount its mounted partitions before writing.

  2. Extract the image into the SD card of VisionFive2 :
    Use the absolute `IMAGE_FILE` path obtained from the build shell above.

      Be sure you are root, provide the actual device name for *sdcard_device_name*, and the resolved `IMAGE_FILE` path from the build.

      ```sh
      $ lsblk
      $ SD_DEVICE=/dev/sdX  # replace with the verified whole microSD device
      $ zstd -dc "$IMAGE_FILE" | sudo dd of="$SD_DEVICE" bs=4M conv=fsync status=progress
      $ sync
      ```

    **IMPORTANT NOTE:** Before re-writing any device on your Build Host, you need to
        be sure you are actually writing to the removable MicroSD card and not some other
        device.
        Each computer is different and removable devices can change from time to time.
        Consequently, you should repeat the previous operation with the MicroSD card to
        confirm the device name every time you write to the card.

    To summarize this example so far, we have the following:
        The first SATA drive is `/dev/sda` and `/dev/sdc` corresponds to the MicroSD card, and is also marked as a removable device.You can see this in the output of the `lsblk` command where "1" appears in the "RM" column for that device.


## Appendix.

### Serial Debugging

Initially, please refer to [VisionFive2 gpio pin assign page](https://doc-en.rvspace.org/VisionFive2/Datasheet/VisionFive_2/gpio_pin_assig.html).

Connect the cable's GND to pin 6 of the UART.<br>
Connect the cable's UART side RX line to pin 8.<br>
Connect the cable's UART side TX line to pin 10.

The UART speed of VisionFive2 is 115200bps.

### Firmware Update

**Check firmware compatibility before updating a board used with older images.** The master build uses upstream U-Boot and produces corresponding firmware. That firmware is not backward-compatible with every older vendored U-Boot image; preserve the existing firmware or use a separate board when it must continue to boot those images.

If you want to update the firmware, please refer to [U-Boot document Vision Five 2 page](https://docs.u-boot.org/en/latest/board/starfive/visionfive2.html).

