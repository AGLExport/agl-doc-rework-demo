---
title: Build host, target, image, and SDK
---
# Build host, target, image, and SDK

AGL image development and application development use related tools, but have different starting points.

## Build host and target

The **build host** is the Linux computer that downloads the source and runs the Yocto build tools. The **target** is the board or virtual machine running AGL. A command that changes a build configuration belongs on the host; runtime diagnostics belong on the target.

A **MACHINE** selects the target board configuration. An **image target** selects the software to include. Features passed to aglsetup.sh select AGL configuration fragments and dependencies. See [build initialization](../standalone/build/common/initialize-build.md) for the available values.

## Image development

Use this workflow when changing the operating system, services, layers, or recipes:

[Prepare the host](../standalone/build/common/prepare-host.md) → [download source](../standalone/build/common/download-source.md) → [initialize the build](../standalone/build/common/initialize-build.md) → [build an image](../standalone/build/common/build-image.md) → [Distributed system](../standalone/index.md#hardware).

The [layer structure](../standalone/build/common/layers/overview.md) explains where platform changes belong.

## Application development

An SDK provides tools and libraries matched to a target image. The Flutter workspace provides another documented development route, including QEMU integration.

Begin with the [Distributed system](../standalone/index.md#apps). Once the application runs, use the [application packaging guide](../standalone/applications/create-application.md) to register it with the AGL launcher.

## Keep a matched environment

Record the AGL release/build, Yocto release, host distribution, MACHINE, image target, and features. Use a matching SDK and runtime image. The [board and image guide](../standalone/build/common/reference/matrix.md) connects these choices to the detailed procedures.
