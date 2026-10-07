---
title: "Build target image"
content_status: authored
---

# Build target image

Use the build shell initialized for the selected profile in [Setup build environment](setup.md). The target and feature selection must match.

| Profile | Features used at setup | Target |
| --- | --- | --- |
| Qt cluster | `agl-demo agl-ic` | `agl-instrument-cluster-standalone-demo` |
| Slint cluster | `agl-demo agl-ic agl-ic-slint` | `agl-instrument-cluster-standalone-demo-slint` |
| Momi with cluster guest | `agl-ic-container` | `agl-instrument-cluster-container-demo` |

Set the target to the row you selected, then build it. This example is for Qt cluster:

~~~sh
IMAGE_TARGET=agl-instrument-cluster-standalone-demo
bitbake "$IMAGE_TARGET"
bitbake-getvar -r "$IMAGE_TARGET" DEPLOY_DIR_IMAGE
bitbake-getvar -r "$IMAGE_TARGET" IMAGE_LINK_NAME
bitbake-getvar -r "$IMAGE_TARGET" IMAGE_NAME_SUFFIX
~~~

For Slint, use `IMAGE_TARGET=agl-instrument-cluster-standalone-demo-slint` in its own build shell. For Momi, use `IMAGE_TARGET=agl-instrument-cluster-container-demo` in the container-profile shell.

The Momi host target declares dependencies on the cluster and IVI guest images. Its [host recipe](https://git.automotivelinux.org/AGL/meta-agl-devel/tree/meta-agl-ic-container/recipes-platform/images/agl-instrument-cluster-container-demo.bb) selects `guest-image-ivi-demo` for the Momi guest. Build and deploy the complete host image; a guest filesystem is not a board boot image.

Use [Qt cluster detail](../cluster/qt.md), [Slint detail](../cluster/slint.md), or [container type 2a detail](../../../integrated/containers/build-guide.md) for profile-specific output and assembly. Type 2b additionally assembles separately built full IVI guests; those extra steps do not apply to the default Momi-only IVI selection.

Continue with [Deploy to board](deploy.md).
