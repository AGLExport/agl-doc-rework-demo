---
title: Setup build environment
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Setup build environment

Prepare a Linux build host and obtain the AGL source before selecting a Basic demo.

1. Complete [Prepare a build host](../../reference/common/prepare-host.md).
2. Follow [Download AGL source](../../reference/common/download-source.md). It defines `AGL_TOP` as the parent workspace and `AGL_SOURCE` as the selected checkout.
3. Check the [board/image matrix](../../reference/common/reference/matrix.md) and the chosen board's BSP requirements.
4. Initialize a fresh build directory with `agl-demo`.

The following example targets Raspberry Pi 4:

~~~sh
cd "$AGL_SOURCE"
source meta-agl/scripts/aglsetup.sh -m raspberrypi4 -b build-basic-rpi4 agl-demo
~~~

For QEMU x86-64, use `-m qemux86-64 -b build-basic-qemu` in a fresh shell. For Raspberry Pi 5, use `-m raspberrypi5 -b build-basic-rpi5`. Complete the [x86](../../reference/common/hardware/x86.md) or [Raspberry Pi](../../reference/common/hardware/raspberry-pi.md) prerequisites for that target.

The setup script leaves the shell in the initialized build environment. Inspect `conf/local.conf` and `conf/bblayers.conf` before building:

~~~sh
printf '%s\n' "$BUILDDIR"
bitbake-getvar MACHINE
~~~

Record the source manifest, machine, features, and build directory. [Initialize the build environment](../../reference/common/initialize-build.md) explains setup options. [Common build reference](../../reference/common.md) links layer and cache configuration.

Continue with [Build target image](../image/index.md). All three Basic demo targets below use this feature selection; choose the recipe separately.
