---
title: "Set up the AGL SDK"
source_path: "04_Developer_Guides/01_Basic/02_Setting_Up_AGL_SDK.md"
content_status: adapted
---

# Set up the AGL SDK

Install an SDK that matches your target's machine, AGL release, image variant, and build. The SDK contains a host compiler and target sysroot; it does not update the target image. In particular, use the Qt IVI SDK for [Qt application development](qt.md).

## Choose the matching installer

The development-branch SDK directories are:

- [qemux86-64 SDKs]({{ agl_download_base }}/latest/qemux86-64/deploy/sdk/)
- [qemuarm64 SDKs]({{ agl_download_base }}/latest/qemuarm64/deploy/sdk/)

For a released image, select its release/build directory in the [AGL downloads](https://download.automotivelinux.org/AGL/) instead of taking a different build from `latest`. The latter changes as snapshots are published. For another board, use that board's SDK directory or generate its SDK from your source build.

Choose the `.sh` installer for the **Qt** image and your target architecture. The current development artifacts use names such as `agl-glibc-x86_64-agl-ivi-demo-qt-corei7-64-qemux86-64-toolchain-<version>.sh` and `agl-glibc-x86_64-agl-ivi-demo-qt-aarch64-qemuarm64-toolchain-<version>.sh`. Older releases and locally built cross-SDK images can use a `poky-` prefix or `-crosssdk` in the filename. Copy the exact filename from your selected directory rather than assuming either naming scheme.

The `x86_64` before the image name describes the Linux SDK host. The later `corei7-64` or `aarch64` identifies the target tune. Keep the installer's companion manifests and the target image's build information to document this pairing.

## Install and activate

Download the selected installer to `~/Downloads`. Replace the example path below with its exact filename; do not use a wildcard that could select several releases:

```sh
mkdir -p "$HOME/agl-app"
export AGL_SDK_INSTALLER="$HOME/Downloads/agl-glibc-x86_64-agl-ivi-demo-qt-corei7-64-qemux86-64-toolchain-<version>.sh"
test -f "$AGL_SDK_INSTALLER"
chmod u+x "$AGL_SDK_INSTALLER"
"$AGL_SDK_INSTALLER" -d "$HOME/agl-app/agl-sdk"
```

Use a new installation directory when changing SDK versions. The installer prints the environment setup filename at completion. Source that exact file in every shell used for application builds. For the qemux86-64 example:

```sh
source "$HOME/agl-app/agl-sdk/environment-setup-corei7-64-agl-linux"
printf 'Target sysroot: %s\n' "$SDKTARGETSYSROOT"
printf 'CMake toolchain: %s\n' "$OE_CMAKE_TOOLCHAIN_FILE"
test -d "$SDKTARGETSYSROOT"
test -f "$OE_CMAKE_TOOLCHAIN_FILE"
```

For an Arm SDK, use its printed environment setup filename instead. Do not activate two SDKs or a BitBake build environment in the same shell. Continue with [Qt application](qt.md) for a complete create/build/deploy/run example, or [Build applications with the SDK](build-apps.md) for C and Autotools applications.

## Generate an SDK from your build

When using a custom image or a board without a matching prebuilt SDK, generate one from the same checkout and build configuration as the target. In the initialized Qt IVI BitBake shell:

```sh
bitbake agl-ivi-demo-qt-crosssdk
ls tmp/deploy/sdk/*.sh
```

The [cross-SDK image recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-ivi-demo-qt-crosssdk.bb) inherits the Qt 6 SDK support and includes development headers and libraries from the Qt IVI image. To generate an SDK for another image that supports this task, use `bitbake <image-name> -c populate_sdk` and ensure its SDK configuration includes the Qt modules your application needs. See [Yocto's standard SDK workflow](https://docs.yoctoproject.org/{{ yocto.codename }}/sdk-manual/using.html).
