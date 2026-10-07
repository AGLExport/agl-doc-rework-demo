---
title: "Setup build environment"
content_status: authored
---

# Setup build environment

Prepare the same host and source workspace used by other AGL builds, then select the Extra profile before creating a build directory.

1. Complete [host preparation](../common/prepare-host.md) and [source download](../common/download-source.md).
2. Confirm `AGL_SOURCE` points to the checkout, and choose a board supported by the selected profile.
3. Use one of the commands below in a fresh shell. Each example targets Raspberry Pi 4 and has a separate directory.

## Qt cluster

~~~sh
cd "$AGL_SOURCE"
source meta-agl/scripts/aglsetup.sh -m raspberrypi4 -b build-extra-qt-rpi4 agl-demo agl-ic
~~~

The [detailed Qt guide](../cluster/qt.md) explains why both features are needed and lists other documented boards.

## Slint cluster

~~~sh
cd "$AGL_SOURCE"
source meta-agl/scripts/aglsetup.sh -m raspberrypi4 -b build-extra-slint-rpi4 agl-demo agl-ic agl-ic-slint
~~~

The [Slint guide](../cluster/slint.md) documents Raspberry Pi 4/5, NanoPC-T6, and its display requirement.

## Momi IVI with its container host

~~~sh
cd "$AGL_SOURCE"
source meta-agl/scripts/aglsetup.sh -m raspberrypi4 -b build-extra-momi-rpi4 agl-ic-container
~~~

Select type 2a in the [container integration guide](../../../integrated/containers/build-guide.md). This profile supplies the host, guest multiconfig, and device-resource configuration. Follow its board-specific requirements and use its type 2b procedure only when adding the full IVI demos.

For Raspberry Pi 5, replace the machine with `raspberrypi5` and use a new directory. Other machines require the selected profile's own support and deployment procedure. Do not switch features inside an existing configured directory.

Continue with [Build target image](image.md).
