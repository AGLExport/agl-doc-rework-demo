---
title: Build SoDeV
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Build SoDeV

The AGL portion of this chapter uses **master**. SoDeV additionally needs a board-specific Xen/control/driver-domain workspace, which has its own source branches, patches and dependency pins. Record both sets of revisions and their integration configuration.

## Build AGL master guest artifacts

Complete [host preparation](../../../distributed/agl-distribution/build/reference/common/prepare-host.md) and [Download AGL source](../../../distributed/agl-distribution/build/reference/common/download-source.md). In a fresh shell, build the master KVM-compatible IVI/Cluster guests for the generic AArch64 VirtIO machine:

```sh
cd "$AGL_SOURCE"
source meta-agl/scripts/aglsetup.sh -m virtio-aarch64 -b build-sodev-master-guests agl-demo agl-devel agl-kvm agl-ic
bitbake agl-ivi-demo-flutter-guest agl-cluster-demo-flutter-guest
bitbake-getvar -r agl-cluster-demo-flutter-guest DEPLOY_DIR_IMAGE
repo manifest -r -o "$AGL_SOURCE/manifest-pinned.xml"
```

The targets come from the [master KVM guest recipes](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/meta-agl-kvm-demo/recipes-platform/images/?h=master). Read [Build a virtio guest](../reference/virtio-guest.md) for guest-device assumptions. A guest root filesystem is one input to SoDeV assembly; the board workspace supplies its compatible guest-kernel and VirtIO backend configuration.

## Prepare the board integration workspace

| Board workspace | Integration authority |
| --- | --- |
| [Sparrow Hawk workspace](https://github.com/automotive-grade-linux/sodev-demo-workspace) | Its README, `build.sh` and board-integration submodules |
| [Raspberry Pi workspace](https://github.com/automotive-grade-linux/sodev-demo-workspace-rpi) | Its README, build configuration, guest pins and board YAML |

Clone the selected workspace with its submodules and record its commit. The source review on 10 October 2026 found that the Sparrow Hawk script assigns its own AGL branch, and the Raspberry Pi script reads that branch through `sync-guest-pins.sh`. Setting an environment variable named `AGL_BRANCH` alone does not make these default builds use master.

For a master-based integration, adapt the workspace's AGL branch/manifest selection to the official master manifest, or its guest-artifact inputs to the matching master outputs above. Inspect local configuration patches and graphics/backends against master recipes before running the complete build. Keep those workspace changes in version control alongside the resolved manifest. The external platform dependencies retain the pins required by that workspace.

## Assemble, deploy and verify

Use the selected workspace's current prerequisites, image assembly, flashing and boot instructions after completing the master guest integration. A guest-less host build does not demonstrate the cockpit: explicitly select the required guests.

Check the control/driver domains, guest startup, VirtIO storage/networking and display ownership. Save host/domain logs and image identifiers. Continue with [Create and Run Guest VM](../customize/guest-vm/index.md). The master guest build above and the external board integration are source-reviewed procedures; a complete master SoDeV hardware configuration has not been validated by this documentation rework.
