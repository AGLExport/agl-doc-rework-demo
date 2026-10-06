---
title: "Build and boot on Raspberry Pi"
source_path: "01_Getting_Started/02_Building_AGL_Image/06_Building_the_AGL_Image/03_Building_for_Raspberry_Pi_x.md"
content_status: adapted
---

# Build and boot on Raspberry Pi

This guide builds a Flutter or Qt IVI demo for Raspberry Pi 4 or 5. Use the image for the exact board. For a first evaluation without a source build, use the [Raspberry Pi 4/5 quickstart](../../../../start/prebuilt/raspberry-pi.md).

## 1. Initialize the build environment

Complete [host preparation](../prepare-host.md) and [source download](../download-source.md). Those steps define `AGL_SOURCE` as the selected source checkout. Run one of the following setups from that directory.

For Raspberry Pi 5:

```sh
cd "$AGL_SOURCE"
source meta-agl/scripts/aglsetup.sh -m raspberrypi5 -b raspberrypi5 agl-demo agl-devel
```

For Raspberry Pi 4:

```sh
cd "$AGL_SOURCE"
source meta-agl/scripts/aglsetup.sh -m raspberrypi4 -b raspberrypi4 agl-demo agl-devel
```

The Pi 4 AGL setup template selects the 64-bit BSP MACHINE `raspberrypi4-64`; its deploy directory and image filenames use that name. `raspberrypi4` is the name passed to `aglsetup.sh`, and the build directory above is also named `raspberrypi4`.

`agl-demo` supplies the demo layers, and `agl-devel` enables development facilities. The script enters the chosen build directory. Add `-f` only when intentionally replacing an existing configuration. See [build initialization](../initialize-build.md) for other options.

## 2. Configure the build

Edit `conf/local.conf` in the initialized build directory. See [Customizing Your Build](../../../customize/build-output.md) for shared downloads, cache locations, and image settings.

If a selected recipe has restricted license flags, review its license and accept only the required flags through `LICENSE_FLAGS_ACCEPTED`. For example, `LICENSE_FLAGS_ACCEPTED:append = " commercial_<recipe-name>"` uses a placeholder that must be replaced with the recipe's actual flag. This accepts a build flag; it does not install a package. See [Yocto's license flag documentation](https://docs.yoctoproject.org/{{ yocto.codename }}/dev-manual/licenses.html#enabling-commercially-licensed-recipes).

The legacy `LICENSE_FLAGS_WHITELIST` variable has been replaced by `LICENSE_FLAGS_ACCEPTED`. Package additions use the current override syntax, such as `IMAGE_INSTALL:append = " package-name"`, with a leading space. Select packages that actually support the chosen board and checkout.

## 3. Build and locate the image

Choose the Flutter IVI demo:

```sh
bitbake agl-ivi-demo-flutter
```

Or build the Qt IVI demo:

```sh
bitbake agl-ivi-demo-qt
```

The first build can take several hours; check the [host requirements](../prepare-host.md) before starting. The stable WIC filenames in the [Pi 4 artifact directory]({{ agl_download_base }}/latest/raspberrypi4/deploy/images/raspberrypi4-64/) and [Pi 5 artifact directory]({{ agl_download_base }}/latest/raspberrypi5/deploy/images/raspberrypi5/) are:

| Board | Build output directory | Flutter image | Qt image |
| --- | --- | --- | --- |
| Pi 4 | `$AGL_SOURCE/raspberrypi4/tmp/deploy/images/raspberrypi4-64/` | `agl-ivi-demo-flutter-raspberrypi4-64.wic.zst` | `agl-ivi-demo-qt-raspberrypi4-64.wic.zst` |
| Pi 5 | `$AGL_SOURCE/raspberrypi5/tmp/deploy/images/raspberrypi5/` | `agl-ivi-demo-flutter-raspberrypi5.wic.zst` | `agl-ivi-demo-qt-raspberrypi5.wic.zst` |

Use the actual filenames from your build; release-specific configuration can change image suffixes or compression. To inspect the resolved output directory and formats from the initialized build shell:

```sh
bitbake-getvar -r agl-ivi-demo-flutter DEPLOY_DIR_IMAGE
bitbake-getvar -r agl-ivi-demo-flutter IMAGE_FSTYPES
```

Substitute `agl-ivi-demo-qt` for the Qt build. See [Yocto's variable inspection guide](https://docs.yoctoproject.org/{{ yocto.codename }}/dev-manual/debugging.html#viewing-variable-values).

## 4. Write the microSD card and boot

Insert a microSD card with capacity greater than the uncompressed WIC disk size. On the build host, identify the whole removable device with `lsblk`, then unmount its mounted partitions.

```sh
lsblk
```

Confirm the device before every write. The following example replaces the selected device's contents. Use the Pi 5 directory and filename for a Pi 5, or the matching Qt filename for Qt:

```sh
cd "$AGL_SOURCE/raspberrypi4/tmp/deploy/images/raspberrypi4-64"
IMAGE=agl-ivi-demo-flutter-raspberrypi4-64.wic.zst
SD_DEVICE=/dev/sdX  # replace after checking lsblk
zstd -dc "$IMAGE" | sudo dd of="$SD_DEVICE" bs=4M conv=fsync status=progress
sync
```

Insert the card into the board, connect its display and network, and power on. Check that the selected demo starts. When the board has a network address and the image permits root SSH login:

```sh
ssh root@<Raspberry-Pi-ip-address>
```

See the [display guide](raspberry-pi/display.md), [camera guide](raspberry-pi/camera.md), and [device guide](raspberry-pi/devices.md) for peripheral configuration. Verify those settings for the exact board and release.

## 5. Collect a serial boot log

Use a 3.3 V UART adapter and the connector/pinout for the specific board. Raspberry Pi 4 and 5 have different UART arrangements; follow the [official UART documentation](https://www.raspberrypi.com/documentation/computers/configuration.html#configuring-uarts). Identify wires by the adapter's TX, RX, and GND labels, since wire colors are vendor-specific.

Check the AGL image's console device and baud rate in its generated kernel command line. Connect adapter RX to board TX, adapter TX to board RX, and GND to GND. Open the corresponding host serial device at that baud rate; for a 115200-baud console, for example:

```sh
sudo screen /dev/ttyUSB0 115200
```

Record the board model, image build identifier, and complete boot log when diagnosing a failure. See [Troubleshooting](../../../../troubleshooting/index.md).
