---
title: "Build target image"
content_status: authored
---

# Build target image

Run BitBake from the shell initialized in [Setup build environment](setup.md). Select one recipe based on the [Basic demo system](../../portfolio/basic/index.md).

| Demo | `IMAGE_TARGET` |
| --- | --- |
| Flutter IVI | `agl-ivi-demo-flutter` |
| Qt IVI | `agl-ivi-demo-qt` |
| IVI-based Flutter Cluster | `agl-cluster-demo-flutter` |

This example builds the Flutter IVI demo. Replace the target value with the selected recipe when choosing another demo.

~~~sh
IMAGE_TARGET=agl-ivi-demo-flutter
bitbake "$IMAGE_TARGET"
bitbake-getvar -r "$IMAGE_TARGET" DEPLOY_DIR_IMAGE
bitbake-getvar -r "$IMAGE_TARGET" IMAGE_LINK_NAME
bitbake-getvar -r "$IMAGE_TARGET" IMAGE_NAME_SUFFIX
~~~

Use the reported deployment directory and filenames. Raspberry Pi 4 uses the output machine `raspberrypi4-64`; Raspberry Pi 5 uses `raspberrypi5`. Current board disk images are generally compressed WIC files, while QEMU launch procedures can use a kernel and ext4 filesystem. The actual recipe configuration determines output types.

The [generic image build reference](../common/build-image.md) explains build output and the [image catalog](../common/reference/images.md) describes variants. Supporting guides cover [Flutter IVI](../ivi/flutter.md), [Qt IVI](../ivi/qt-ivi-demo.md), and [Flutter Cluster](../ivi/flutter-cluster.md).

Keep all required boot artifacts from this build together. Continue with [Deploy to board](deploy.md).
