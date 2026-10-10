---
title: Troubleshooting
agl_branch: master
last_reviewed: '2026-10-10'
---

# Troubleshooting

Start with [Diagnose common problems](reference/diagnostics.md) for symptom checks and commands to collect target information. Use the task that failed and the message you received to find the related guide below.

## Find a starting point

| Problem | Information to check first |
| --- | --- |
| An image is missing or a target is unclear | [Version selection](../community/releases/index.md), [board and image matrix](../vehicle-controller/distributed/agl-distribution/build/reference/common/reference/matrix.md), [image types](../vehicle-controller/distributed/agl-distribution/build/reference/common/reference/images.md) |
| QEMU or hardware does not boot | [Prebuilt image guide](../vehicle-controller/distributed/agl-distribution/quick-start/prebuilt/index.md), [hardware support](../vehicle-controller/distributed/agl-distribution/build/reference/common/reference/hardware.md) |
| Required build tools are missing | [Prepare your build host](../vehicle-controller/distributed/agl-distribution/build/reference/common/prepare-host.md) |
| Source checkout or build initialization fails | [Download AGL source](../vehicle-controller/distributed/agl-distribution/build/reference/common/download-source.md), [initialize the build environment](../vehicle-controller/distributed/agl-distribution/build/reference/common/initialize-build.md) |
| An application does not build or run | [SDK setup](../vehicle-controller/distributed/agl-distribution/applications/reference/setup-sdk.md), [build applications](../vehicle-controller/distributed/agl-distribution/applications/reference/build-apps.md), [create a new application](../vehicle-controller/distributed/agl-distribution/applications/reference/create-application.md) |
| An API's usage is unclear | [API and service catalog](../vehicle-controller/distributed/agl-distribution/components/services/index.md) |

Also check the [official release notes](https://wiki.automotivelinux.org/agl-distro/release-notes) for known issues and limitations in your version.

## Gather context {#gather-context}

The following information helps others understand a question or bug report.

- AGL version, source branch, and revision.
- Board or virtual environment, image name, `MACHINE`, and selected features.
- Host OS and the versions of tools and SDKs used.
- Instructions followed, commands run, and steps leading to the failure.
- Expected and actual results, with relevant console output or build logs.

Record whether the problem reproduces under the same conditions and which steps completed successfully. The [diagnostics guide](reference/diagnostics.md) provides commands for target logs and system information, and explains which details to collect on the build host.

## Ask for help or report a bug

For usage questions or help diagnosing a problem, read [Getting help](reference/getting-help.md). For a reproducible defect, follow [Reporting bugs](reference/reporting-bugs.md).

To fix an error or fill a gap in this GitHub Pages site, follow [Contribute to the documentation](../community/contributing/reference/documentation.md) for local editing, validation, and pull request submission. That guide also identifies the separate Gerrit route for changes to the original AGL documentation.
