---
title: Releases & migration
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Releases & migration

This documentation uses the **AGL `master` development branch** for AGL source, examples and snapshot artifacts. It does not select a named release as its implementation baseline. The official [master documentation](https://docs.automotivelinux.org/en/master/) and [master manifest](https://git.automotivelinux.org/AGL/AGL-repo/tree/default.xml?h=master) are the starting points.

## Current master baseline

The source review on **10 October 2026** confirmed:

| Item | Reviewed master configuration |
| --- | --- |
| AGL manifest default | `revision="master"` for AGL layer repositories |
| Distribution branch | `AGL_BRANCH = "master"` |
| Distribution build identifier | `AGLVERSION = "21.93.0"` at review time |
| Yocto/OpenEmbedded | Wrynose line; external projects pinned by the manifest |
| Qt layer | meta-qt6 6.12 line, with the manifest's selected revision |
| Prebuilt images | `master` snapshots; choose one snapshot directory for all matching artifacts |

The [distribution configuration](https://git.automotivelinux.org/AGL/meta-agl/tree/meta-agl-core/conf/distro/agl.conf?h=master) and manifest define these observations. The branch can advance after review. The [source-review record](../assets/source-reviews/master-2026-10-10.json) contains the checked official URLs and content hashes; source inspection does not report hardware boot tests.

## Record a reproducible master checkout

Follow [Download AGL source](../standalone/build/common/download-source.md), then save the resolved revisions:

```sh
cd "$AGL_SOURCE"
repo manifest -r -o "$AGL_SOURCE/manifest-pinned.xml"
repo status
```

Use the same resolved manifest for the image, SDK and any separately assembled AGL guests. Record board, setup features, image target and artifact filenames. A moving branch name or a `latest` snapshot alone does not identify a reproducible build.

## Update an existing master deployment

1. Save the current resolved manifest, local configuration, application/service settings and boot logs.
2. Review changes in the [master manifest](https://git.automotivelinux.org/AGL/AGL-repo/log/default.xml?h=master) and selected layer recipes.
3. Synchronize a separate source workspace and create a fresh build directory for the chosen machine/features.
4. Rebuild the image and matching SDK. Align protobuf definitions, VSS mappings and runtime client/server configuration.
5. Deploy matching artifacts and verify boot, UI, service health, vehicle-data exchange and any required guest/device boundaries.

External SoDeV board/hypervisor workspaces have their own branches and pins. The [SoDeV build guide](../integrated/sodev/build.md) states how AGL master guests relate to those integrations; do not assume a workspace's default AGL branch is master.

## Choose the next task

- [Quick start](../start/index.md) runs a master snapshot.
- [Build AGL system](../standalone/build/index.md) builds a master source checkout.
- [Diagnose common problems](../troubleshooting/diagnostics.md) identifies version, configuration and service failures.
