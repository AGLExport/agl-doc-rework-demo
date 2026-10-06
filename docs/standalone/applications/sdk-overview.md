---
title: "Application development and SDK workflow"
source_path: "04_Developer_Guides/01_Basic/01_Overview.md"
content_status: adapted
---

# Application development and SDK workflow

Use an AGL SDK to cross-compile applications on a Linux development host for a target running the matching AGL image. Start with a [prebuilt image](../../start/prebuilt/index.md) or build an image using [Common part](../build/common.md), then select the development route for your toolkit.

1. [Set up the AGL SDK](setup-sdk.md) for the target's machine, release, and image build.
2. Create and build a [Qt application](qt.md), or use [Build applications with the SDK](build-apps.md) for C and Autotools projects. Flutter uses its separate [workspace workflow](flutter.md).
3. [Package and register the application](create-application.md), deploy it to the target, and launch it through the homescreen. The Qt guide includes an executable example and target-side diagnostics.
4. For repeatable image integration, [create a custom recipe](../customize/recipe.md) and [add its package to your image](../customize/image.md).

Keep application source, SDK identity, target image build identifier, and deployment settings together. Use a new shell and build directory when changing SDKs or target architectures.
