---
title: "Releases & migration"
---

# Releases & migration

Use this section to choose a version or plan an update to an existing environment.

## Version covered by this site

| Item | Site configuration |
| --- | --- |
| AGL name | {{ agl.full_name }} |
| Source branch | `{{ agl.codename }}` |
| Status | Development branch and snapshots |
| Yocto | {{ yocto.codename }} / {{ yocto.version }} |

This site documents the moving development branch rather than a pinned release. On 7 October 2026, the official [distribution configuration](https://git.automotivelinux.org/AGL/meta-agl/tree/meta-agl-core/conf/distro/agl.conf) identified master as Vimba with an AGL version of 21.93.0. The [source manifest](https://git.automotivelinux.org/AGL/AGL-repo/tree/default.xml) at revision f28a8d166fb1a2e792fc69952ae204a522d75a24 used the Wrynose and Qt 6.12 branches; its update recorded Yocto Project 6.0.3. The [official release notes](https://wiki.automotivelinux.org/agl-distro/release-notes#vibrant_vimba) call this release family Vibrant Vimba.

A manifest revision alone does not pin layers that track branches. After downloading source, save a resolved manifest with repo manifest -r as described in [Download AGL source](../standalone/build/common/download-source.md). Match any prebuilt image and SDK to that source revision or to one named release.

The version information above records a source inspection. It does not indicate that every included procedure or environment has been tested against those artifacts.

## Choose a stable release

Use the [official release notes](https://wiki.automotivelinux.org/agl-distro/release-notes) to check release information, supported environments, and known issues. Find version-specific documentation on the [official AGL documentation site](https://docs.automotivelinux.org/).

Use a prebuilt image, source branch, SDK, and documentation for the same version.

## Move to another version

1. Record your current AGL version, source revision, board, image, selected features, and SDK.
2. Check the destination release notes for supported boards, changes, and known issues.
3. Use the destination version's instructions to check [host requirements](../standalone/build/common/prepare-host.md) and SDK requirements.
4. Check the APIs and settings you use against the [API and service catalog](../components/services/index.md) and the destination version's documentation.
5. In the new environment, verify boot, application execution, and the services your application uses.

These steps provide a general checking sequence. For version-specific changes and compatibility information, use the official release notes and documentation for each version.

## Next steps

- To explore a prebuilt image: [Quick start](../start/index.md).
- To build from source: [Platform development](../standalone/index.md#platform).
- To investigate a problem after updating: [Diagnose common problems](../troubleshooting/diagnostics.md), then use [Troubleshooting](../troubleshooting/index.md) to ask for help.
