---
title: "Rust and Slint Instrument Cluster demo"
source_path: "01_Getting_Started/03_Build_and_Boot_guide_Profile/03_Slint_Demo_Image.md"
content_status: imported
---

# Build and Boot Rust based Instrument Cluster Demo Images


This document describes how to build Rust based Instrument Cluster Demo Images.

## 1. Available target board

Rust based Instrument Cluster Demo Images is available on table 1 boards.

**Table1. Supported board.**

| Board |
|:---:|
| NanoPC-T6 (4G or 8G or 16G) |
| Raspberry Pi4/5 (4G or 8G) |

## 2. Setup build environment

Build environment for Rust based Instrument Cluster Demo is same as AGL other profile build environment. 

### 1st step:
Please read [[Build Process Overview]](../platform/build-overview.md) in AGL doc.

### 2nd step:
Please read [[Preparing Your Build Host]](../platform/prepare-host.md) in AGL doc.

### 3rd step: 
Define Your Top-Level Directory.

```bash
$ export AGL_TOP=$HOME/AGL
$ mkdir -p $AGL_TOP
```

### 4th step: Download the repo Tool and Set Permissions

If your environment already install google repo, please skip this step.

```bash
$ mkdir -p $HOME/bin
$ export PATH=$HOME/bin:$PATH
$ curl https://storage.googleapis.com/git-repo-downloads/repo > $HOME/bin/repo
$ chmod a+x $HOME/bin/repo
```

### 5th step: Setup git

If your environment already setup user information for git, please skip this step.

```bash
$ git config \--global user.email "you@example.com"
$ git config \--global user.name "Your Name"
```

### 6th step: Download the AGL Source Files

```bash
$ cd $AGL_TOP
$ mkdir master
$ export AGL_TOP=$HOME/AGL/master
$ cd $AGL_TOP
$ repo init -b master -u https://gerrit.automotivelinux.org/gerrit/AGL/AGL-repo
$ repo sync
```


## 3. Configure to target board and build.

### 1st step:  Run the aglsetup.sh Script.

```bash
$ cd $AGL_TOP
```

When your board is NanoPC T6
```bash
$ source meta-agl/scripts/aglsetup.sh -f -m nanopc-t6 -b build-ic-nanopc-t6 agl-demo agl-ic agl-ic-slint
```

When your board is Raspberry Pi 4
```bash
$ source meta-agl/scripts/aglsetup.sh -f -m raspberrypi4 -b build-ic-rpi4 agl-demo agl-ic agl-ic-slint
```

When your board is Raspberry Pi 5
```bash
$ source meta-agl/scripts/aglsetup.sh -f -m raspberrypi5 -b build-ic-rpi5 agl-demo agl-ic agl-ic-slint
```


### 2nd step: Build target image.

```bash
$ bitbake  agl-instrument-cluster-standalone-demo-slint
```

## 4. Write image to SD card.

The image is constructed by wic image, that include partition table and each partition data into one image file.

In default setting, that wic image is compressed zstd.  When that wic
image to the SD card, you need to use zstdcat and dd commands on your
build PC.

```bash
$ sudo bash -c "zstdcat -d /path/to/image/directory/agl-instrument-cluster-standalone-demo-slint-XXXXX.rootfs.wic.zst | dd of=/dev/sdXXX bs=128M"
```

**If you are missing to set SD card device "/dev/sdXXX", it cause
SSD/HDD data break (only logical, not physical).**

For example;

A /dev/sda is SSD for your PC.  A /dev/sdb is SD card.  You should use
/dev/sdb, must not use /dev/sda.

When your PC has direct SD card interface not a use card reader, your SD
card device is /dev/mmcblkX may be.

## 6. Power on.


# Attention

Current demo image requires to 1920 x 720 display.

