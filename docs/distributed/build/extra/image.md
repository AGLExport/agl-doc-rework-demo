---
title: Build target image
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Build target image

Use the build shell initialized for the selected profile in [Setup build environment](setup.md). The target and feature selection must match.

| Profile | Features used at setup | Target |
| --- | --- | --- |
| Qt cluster | `agl-demo agl-ic` | `agl-instrument-cluster-standalone-demo` |
| Slint cluster | `agl-demo agl-ic agl-ic-slint` | `agl-instrument-cluster-standalone-demo-slint` |

Set the target to the row you selected, then build it. This example is for Qt cluster:

~~~sh
IMAGE_TARGET=agl-instrument-cluster-standalone-demo
bitbake "$IMAGE_TARGET"
bitbake-getvar -r "$IMAGE_TARGET" DEPLOY_DIR_IMAGE
bitbake-getvar -r "$IMAGE_TARGET" IMAGE_LINK_NAME
bitbake-getvar -r "$IMAGE_TARGET" IMAGE_NAME_SUFFIX
~~~

For Slint, use `IMAGE_TARGET=agl-instrument-cluster-standalone-demo-slint` in its own build shell. The [Qt](../cluster/qt.md) and [Slint](../cluster/slint.md) guides explain profile-specific output.

Momi's complete host and guests are built through the [Container integration Momi guide](../../../small-integrated/containers/demo/momi-ivi.md). Use its integrated target and storage assembly procedure.

Continue with [Deploy to board](deploy.md).
