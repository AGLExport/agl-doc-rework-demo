---
title: Develop
---

# Develop

Application development and AGL image development require different environments. Choose the path that matches your goal.

This site targets the **{{ agl.full_name }} / `{{ agl.codename }}` development branch**. Use an SDK, source checkout, and target image that match the same version and configuration. See [Releases & migration](../releases/index.md) for version selection.

## Develop an application {#apps}

### Develop with Flutter

Use [Set up a Flutter workspace](apps/flutter-workspace.md) to prepare your development environment and workspace. This is the entry point for working with Flutter applications on an appropriate AGL image.

### Develop with an SDK

1. Read the [SDK overview](apps/sdk-overview.md) to understand its role and the development workflow.
2. [Set up the SDK](apps/setup-sdk.md) for your version and target.
3. Follow [Build applications with the SDK](apps/build-apps.md).
4. Read [Create a new application](apps/create-application.md) for application structure and deployment.

Check the scope of each guide before applying its instructions. To find the interfaces your application uses, see the [API and service catalog](../reference/services/index.md).

!!! note "Qt instructions"
    The Qt-specific source guide remains incomplete. The [Qt application development page](apps/qt-sdk.md) links to the available starting points. For general SDK preparation, use the [SDK overview](apps/sdk-overview.md) and [SDK setup](apps/setup-sdk.md). To run an existing Qt demo image, choose an environment in the [prebuilt image overview](../start/prebuilt-images.md).

## Build an image {#platform}

Choose a target from the [board and image matrix](../reference/matrix.md), then follow these steps.

1. [Build process overview](platform/build-overview.md): understand the workflow.
2. [Prepare your build host](platform/prepare-host.md): set up the host environment and tools.
3. [Download AGL source](platform/download-source.md): check out the source for your branch.
4. [Initialize the build environment](platform/initialize-build.md): select the target and features.
5. [Build an AGL image](platform/build-image.md): follow the build instructions for the selected target.
6. [Boot your target](#hardware): use the board-specific guide to locate the output image and follow its boot instructions.

Host requirements also depend on the Yocto version. This site's configuration uses **Yocto {{ yocto.codename }} / {{ yocto.version }}**. Check the host OS and tool versions in the existing guides against the requirements for your target release.

### Optional customization

Once the basic workflow is clear, choose the changes you need:

- [Customize an image](platform/customize-image.md): change the image configuration.
- [Create a recipe](platform/custom-recipe.md): add software to the build.
- [Configure caches and build output](platform/customize-build.md): manage build history, storage, and shared build data.

For the relationship between these tools and the running system, see [Build host, target, image, and SDK](../explanation/build-and-runtime.md).

## Boot your target {#hardware}

Use [hardware support](../reference/hardware.md) and the [board and image matrix](../reference/matrix.md) to choose a target. For a source build, follow the relevant target guide below for build options, image output, and boot instructions.

| Target | Build and boot guide |
| --- | --- |
| x86 emulation or hardware | [x86 guide](hardware/x86.md) |
| Raspberry Pi 4 or 5 | [Raspberry Pi guide](hardware/raspberry-pi.md) |
| Renesas R-Car Gen3 | [R-Car Gen3 guide](hardware/renesas-rcar-gen3.md) |
| Sparrow Hawk | [Sparrow Hawk guide](hardware/sparrow-hawk.md) |
| Rockchip / NanoPC-T6 | [Rockchip guide](hardware/rockchip.md) |
| Virtio guest | [Virtio guide](hardware/virtio.md) |
| AWS EC2 | [AWS EC2 guide](hardware/aws-ec2.md) |
| VisionFive2 | [VisionFive2 guide](hardware/visionfive2.md) |

To use an existing image instead, choose an environment from the [prebuilt image overview](../start/prebuilt-images.md).

Check the Reference BSP or Community BSP category, required `MACHINE`, and features in the documentation for your board and version.

## Related information

- [Understand AGL](../explanation/index.md): read about the components you want to change.
- [API & configuration](../reference/index.md): look up specifications during development.
- [Troubleshooting](../troubleshooting/index.md): find help with builds and execution.
- [Contribute](../contributing/index.md): propose your changes to AGL.
