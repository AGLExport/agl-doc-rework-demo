---
title: Momi IVI demo
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Momi IVI demo

Momi is the lightweight Qt/QML IVI guest in the master IC/IVI container demonstration. Its homescreen, navigation, weather and player run inside a guest root filesystem; Container Manager and DRM lease manager run on the host. The [application catalog](../../components/reference-applications/index.md) introduces each Momi component.

## Build the default integration

Complete [host preparation](../../../../distributed/agl-distribution/build/reference/common/prepare-host.md) and [Download AGL source](../../../../distributed/agl-distribution/build/reference/common/download-source.md), which selects `master` and defines `AGL_SOURCE`. In a fresh build shell, initialize the Raspberry Pi 4 example:

```sh
cd "$AGL_SOURCE"
source meta-agl/scripts/aglsetup.sh -m raspberrypi4 -b build-container-momi-rpi4 agl-ic-container
bitbake agl-instrument-cluster-container-demo
bitbake-getvar -r agl-instrument-cluster-container-demo DEPLOY_DIR_IMAGE
bitbake-getvar -r agl-instrument-cluster-container-demo IMAGE_LINK_NAME
```

For another board, use its procedure in the [detailed container guide](../../reference/build-guide.md). Select type 2a for the default Momi composition. The [master host recipe](https://git.automotivelinux.org/AGL/meta-agl-devel/tree/meta-agl-ic-container/recipes-platform/images/agl-instrument-cluster-container-demo.bb?h=master) builds `guest-image-cluster-demo` and `guest-image-ivi-demo` through multiconfig. Its WIC assembly stages guest filesystems with the host; building `guest-image-ivi-demo` alone does not produce the complete board image.

## Deploy and verify

Follow the same board/type 2a flashing and boot procedure in the detailed guide. Preserve the host and guest artifacts from one resolved master manifest. On the host console:

```sh
cmcontrol --get-guest-list
systemctl --failed
```

Confirm that the registered Cluster and IVI guests are present, then use the guide's role-switching controls to display Momi. Check the IVI guest console and logs when its applications fail. Host service status alone does not establish that the guest UI works.

Momi's [Qt/multimedia package group](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/meta-agl-demo-shared/recipes-platform/packagegroups/packagegroup-agl-momi-ivi-qt.bb?h=master) selects its own audio packages. Consult [Architecture](../../architecture/index.md) before changing display or audio allocation. Full Flutter/Qt IVI guests use the separate type 2b assembly procedure. Continue with [Create and Run Guest Container](../../customize/guest-container/index.md) when changing guest composition.
