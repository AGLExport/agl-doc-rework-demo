---
title: API & configuration
---

# API & configuration

Find specifications for boards, images, and services here. For a guided workflow, use [Get started](../start/index.md) or [Develop](../develop/index.md).

For terminology, start with the [AGL glossary](glossary.md). To understand the development environment, read [Build host, target, image, and SDK](../explanation/build-and-runtime.md).

## Boards and images

| Information | Reference |
| --- | --- |
| Board and image combinations | [Board and image matrix](matrix.md) |
| Board support and BSP categories | [Hardware support](hardware.md) |
| Image types and build settings | [Image types](images.md) |

Check the board-specific documentation for your version when selecting `MACHINE`, an image name, and features. The matrix describes the information included in this documentation.

## APIs and services

Use the [API and service catalog](services/index.md) to find specifications and related documentation for a feature. It brings existing API and component documentation into one entry point.

## Build and SDK configuration

- [Initialize the build environment](../develop/platform/initialize-build.md): select targets and features.
- [Configure caches and build output](../develop/platform/customize-build.md): manage build history, storage, and shared build data.
- [Customize an image](../develop/platform/customize-image.md): change image configuration.
- [SDK overview](../develop/apps/sdk-overview.md) and [SDK setup](../develop/apps/setup-sdk.md): prepare an application development environment.

## Check the version

This site targets the **{{ agl.full_name }} / `{{ agl.codename }}` development branch**. APIs, configuration, and supported environments may change between versions. Align your image, source, and SDK, and use [Releases & migration](../releases/index.md) for documentation about other versions.
