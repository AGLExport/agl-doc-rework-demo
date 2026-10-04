---
title: Releases & migration
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

This site reorganizes existing documentation for the development branch. It does not indicate that every included procedure or environment has been tested against the current artifacts.

## Choose a stable release

Use the [official release notes](https://wiki.automotivelinux.org/agl-distro/release-notes) to check release information, supported environments, and known issues. Find version-specific documentation on the [official AGL documentation site](https://docs.automotivelinux.org/).

Use a prebuilt image, source branch, SDK, and documentation for the same version.

## Move to another version

1. Record your current AGL version, source revision, board, image, selected features, and SDK.
2. Check the destination release notes for supported boards, changes, and known issues.
3. Use the destination version's instructions to check [host requirements](../develop/platform/prepare-host.md) and SDK requirements.
4. Check the APIs and settings you use against the [API and service catalog](../reference/services/index.md) and the destination version's documentation.
5. In the new environment, verify boot, application execution, and the services your application uses.

These steps provide a general checking sequence. For version-specific changes and compatibility information, use the official release notes and documentation for each version.

## Next steps

- To explore a prebuilt image: [Get started](../start/index.md).
- To build from source: [Platform development](../develop/index.md#platform).
- To investigate a problem after updating: [Diagnose common problems](../troubleshooting/diagnostics.md), then use [Troubleshooting](../troubleshooting/index.md) to ask for help.
