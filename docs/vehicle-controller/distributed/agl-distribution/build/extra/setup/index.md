---
title: Setup build environment
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Setup build environment

Prepare the same host and source workspace used by other AGL builds, then select the Extra profile before creating a build directory.

1. Complete [host preparation](../../reference/common/prepare-host.md) and [source download](../../reference/common/download-source.md).
2. Confirm `AGL_SOURCE` points to the checkout, and choose a board supported by the selected profile.
3. Use one of the commands below in a fresh shell. Each example targets Raspberry Pi 4 and has a separate directory.

## Qt cluster

~~~sh
cd "$AGL_SOURCE"
source meta-agl/scripts/aglsetup.sh -m raspberrypi4 -b build-extra-qt-rpi4 agl-demo agl-ic
~~~

The [detailed Qt guide](../reference/cluster/qt.md) explains why both features are needed and lists other documented boards.

## Slint cluster

~~~sh
cd "$AGL_SOURCE"
source meta-agl/scripts/aglsetup.sh -m raspberrypi4 -b build-extra-slint-rpi4 agl-demo agl-ic agl-ic-slint
~~~

The [Slint guide](../reference/cluster/slint.md) documents Raspberry Pi 4/5, NanoPC-T6, and its display requirement.

## Momi IVI with its container host

Use the [Container integration Momi guide](../../../../../small-integrated/container-integration/demo-image/momi-ivi/index.md) for its complete master host/guest setup. This chapter's Qt/Slint build directories are dedicated cluster configurations.

For Raspberry Pi 5, replace the machine with `raspberrypi5` and use a new directory. Other machines require the selected profile's own support and deployment procedure. Do not switch features inside an existing configured directory.

Continue with [Build target image](../image/index.md).
