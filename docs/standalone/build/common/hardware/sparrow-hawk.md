---
title: Build and boot on Sparrow Hawk
source_path: 01_Getting_Started/02_Building_AGL_Image/06_Building_the_AGL_Image/04_Building_for_Retronix_Sparrow_Hawk_Board.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# Build and boot on Sparrow Hawk

Complete [host preparation](../prepare-host.md) and [source download](../download-source.md) first. These steps define `AGL_TOP` as the parent workspace and `AGL_SOURCE` as the source checkout. Run each setup command from `$AGL_SOURCE`; `aglsetup.sh` then enters its build directory. Use `-f` only when intentionally replacing existing configuration.

The Retronix Sparrow Hawk is a compact and highly expandable edge AI development board
powered by the Renesas R-Car V4H System-on-Chip. This board targets robotics, industrial
automation, and rapid prototyping, offering a flexible and cost-effective development
platform.

For more information about board specifications and the latest supported software,
visit the [R-Car Community board](https://rcar-community.github.io/) page.

This section provides the build and deployment steps to create an image for the Sparrow Hawk board.

## 1. How to build

### 1.1. Making Sure Your Build Environment is Correct

Refer to
"[Initializing Your Build Environment](../initialize-build.md)"
for generic information on setting up your build environment using the `aglsetup.sh`
script.

Use the following command to run the AGL Setup script:

```sh
cd "$AGL_SOURCE"
source meta-agl/scripts/aglsetup.sh -m sparrow-hawk -b build agl-devel agl-demo
```

* `-m`: Set the board name (sparrow-hawk)
* `-b`: Set your build directory
* `-f` (optional): Overwrite existing configuration. Use only when intentionally replacing
the configuration in the same directory.
* `agl-devel agl-demo`: AGL features to enable in this build. See all supported features in
[Initializing Your Build Environment](../initialize-build.md)
or by running `source meta-agl/scripts/aglsetup.sh --help`

After running the `aglsetup.sh` script, you are automatically placed in the working directory
(i.e., `$AGL_SOURCE/build`).

**NOTE:**
To avoid unnecessary downloads and rebuilds, you can set the DL_DIR and SSTATE_DIR variables to a shared
location for multiple builds.

```sh
echo "# reuse download directories" >> $AGL_TOP/site.conf
echo "DL_DIR = \"$HOME/downloads/\"" >> $AGL_TOP/site.conf
echo "SSTATE_DIR = \"$AGL_TOP/sstate-cache/\"" >> $AGL_TOP/site.conf
ln -sf $AGL_TOP/site.conf conf/
```

### 1.2. Using BitBake

Start the build using the `bitbake` command. Examples:

**Qt-based IVI demo:**
The target is `agl-ivi-demo-qt`:

```sh
bitbake agl-ivi-demo-qt
```

**Flutter-based Instrument Cluster demo:**
The target is `agl-cluster-demo-flutter`:

```sh
$ bitbake agl-cluster-demo-flutter
```

**NOTE:** An initial build can take many hours depending on your
CPU and internet connection speeds. The build also requires approximately
100GB of free disk space.

The resulting images are located in the build directory:

```
<build_directory>/tmp/deploy/images/sparrow-hawk
```

## 2. Deploying the AGL Demo Image

### 2.1. Prepare your hardware

The following equipment is needed to boot the AGL image on the Sparrow Hawk board:

- 65W or higher power adapter with USB-PD (Power Delivery) standard
- USB-A to Micro USB cable for serial console
- Ethernet cable to transfer data with host PC (optional)
- MicroSD card to store the AGL image and data. Ensure the capacity is larger
than the image size. We recommend 16GB or larger.
- DisplayPort cable and monitor to display the AGL graphical interface

**IMPORTANT:** Do not use the board without a heatsink or cooling fan installed.
Overheating may damage the chip or lead to system failure.

### 2.2. Deploy image to MicroSD card

Insert the MicroSD card into your build host.
After insertion, use the `dmesg` command to discover the device name:

```sh
$ dmesg | tail -4
[ 1971.462160] sd 6:0:0:0: [sdc] Mode Sense: 03 00 00 00
[ 1971.462277] sd 6:0:0:0: [sdc] No Caching mode page found
[ 1971.462278] sd 6:0:0:0: [sdc] Assuming drive cache: write through
[ 1971.463870]  sdc: sdc1 sdc2
```

The log shows an example card at `/dev/sdc`. Identify your actual card with `lsblk`, unmount its mounted partitions, and write the image:

```sh
# Run from the initialized build shell; use agl-cluster-demo-flutter if that is your image.
IMAGE_TARGET=agl-ivi-demo-qt
DEPLOY_DIR=$(bitbake-getvar --value -r "$IMAGE_TARGET" DEPLOY_DIR_IMAGE)
IMAGE_BASE=$(bitbake-getvar --value -r "$IMAGE_TARGET" IMAGE_LINK_NAME)
IMAGE_SUFFIX=$(bitbake-getvar --value -r "$IMAGE_TARGET" IMAGE_NAME_SUFFIX)
IMAGE_FILE="$DEPLOY_DIR/$IMAGE_BASE$IMAGE_SUFFIX.wic.zst"
ls -lh "$IMAGE_FILE"
SD_DEVICE=/dev/sdX  # replace with the verified whole microSD device
zstd -dc "$IMAGE_FILE" | sudo dd of="$SD_DEVICE" bs=4M conv=fsync status=progress
sync
```

**IMPORTANT:** Verify the MicroSD card device name. Be careful not to write
the image to other disk devices.

### 2.3. Setup and boot AGL image

#### 2.3.1. Install a serial client on your build host

You need serial port terminal software on your build host. Recommended options:

* [GNU Screen](https://en.wikipedia.org/wiki/GNU_Screen)
* [picocom](https://linux.die.net/man/8/picocom)
* [Minicom](https://en.wikipedia.org/wiki/Minicom)

The examples below use picocom, which has the fewest dependencies and is the most lightweight tool.

#### 2.3.2. Connect your build host to the board's serial port

Connect the USB-A to Micro USB cable from the host PC to the CN4 connector on Sparrow Hawk. This
creates two USB serial devices: `/dev/ttyUSB0` and `/dev/ttyUSB1`. AGL boot uses
`/dev/ttyUSB0` as the primary serial device with baud rate 921600.

```sh
sudo picocom -b 921600 /dev/ttyUSB0
```

#### 2.3.3. Power on the board to access the U-Boot console

Power on the board by pressing switch SW1. The boot log appears as follows:

```
U-Boot SPL 2026.04 (Jul 15 2026 - 12:25:02 +0000)
Trying to boot from SPI


U-Boot 2026.04 (Jul 15 2026 - 12:25:02 +0000)

CPU:   Renesas Electronics R8A779G0 rev 3.0
Model: Retronix Sparrow Hawk board based on r8a779g3
DRAM:  2 GiB (total 16 GiB)
Core:  95 devices, 24 uclasses, devicetree: separate
MMC:   mmc@ee140000: 0
Loading Environment from SPIFlash... SF: Detected w77q51nw with page size 256 Bytes, erase size 64 KiB, total 64 MiB
OK
In:    serial@e6540000
Out:   serial@e6540000
Err:   serial@e6540000
Net:   eth0: ethernet@e6800000
Hit any key to stop autoboot: 0
=>
```

Press any key to stop the boot process, then proceed to the next steps.

#### 2.3.4. Flash firmware and boot AGL demo

Update the loader with the firmware inside the MicroSD card. This step only
needs to be run once. For subsequent builds, simply overwrite the image on
the MicroSD card.

Run this command in the U-Boot console:

```
load mmc 0 ${loadaddr} flash.bin && sf probe && sf update ${loadaddr} 0 ${filesize} && reset
```

The board will automatically reset and boot to the AGL demo after flashing completes.
You should see the AGL Homescreen GUI when connected to a monitor using a DisplayPort
cable.

On the serial console, log in with the "root" account (no password required).

## 3. Troubleshooting

Check the serial boot log, power supply, cooling, and display connection. Record the image build identifier and firmware version. Use [Troubleshooting](../../../../troubleshooting/index.md) for log collection and issue reporting.
