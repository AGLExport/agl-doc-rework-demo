---
title: "meta-agl-demo"
source_path: "04_Developer_Guides/02_AGL_Platform_Development/01_AGL_Yocto_Layers/03_meta_agl_demo.md"
content_status: imported
---

## Introduction

The `meta-agl-demo` layer is the reference user interface layer for the DEMO
platform of Automotive Grade Linux (AGL).
The layer provides a demo applications and images.

## Sub-Layers

The `meta-agl-demo` layer itself contains many sub-layers and files.
Following is a "tree" look at the layer structure:

```
.
├── meta-agl-demo-shared
└── meta-agl-kvm-demo
```

This list provides some overview information on the sub-layers
in `meta-agl-demo`:

* `meta-agl-demo-shared`: The layer for common recipe between AGL Demo IVI and AGL Container based instrument cluster platform demo.
* `meta-agl-kvm-demo`: The layer for KVM demo.

## Layer Dependencies

This section describes dependencies for the `meta-agl-demo` layer.
Dependencies are grouped into base, hardware, and feature dependencies.

### Base Dependencies

The `meta-agl-demo` layer has the following base dependencies:

* Yocto Project Release:

  - URI: git://git.yoctoproject.org/poky
  - Branch: "{{ yocto.codename }}"
  - Tested Revision: See the [`default.xml`](https://git.automotivelinux.org/AGL/AGL-repo/tree/default.xml)
    manifest file for the `AGL-repo` repository for revision information.

* AGL `meta-agl` Layer:

  - URI: https://gerrit.automotivelinux.org/gerrit/AGL/meta-agl
  - Branch: "{{ agl.codename }}"

* OpenEmbedded `meta-openembedded` Layer:

  - Branch: "{{ yocto.codename }}"
  - Tested Revision: See the [`default.xml`](https://git.automotivelinux.org/AGL/AGL-repo/tree/default.xml)
    manifest file for the `AGL-repo` repository for revision
    information.

    Specifically, out of `meta-openembedded`, these sub-layers are used:

    - `meta-oe`
    - `meta-multimedia`
    - `meta-networking`
    - `meta-python`

* qt.io `meta-qt6` Layer from the
  [code.qt.io](https://code.qt.io/cgit/yocto/meta-qt6.git/):

  - URI: https://code.qt.io/yocto/meta-qt6.git
  - Branch: "{{ qt_layer_branch }}"
  - Tested Revision: See the [`default.xml`](https://git.automotivelinux.org/AGL/AGL-repo/tree/default.xml)
    manifest file for the `AGL-repo` repository for revision
    information.

* meta-flutter `meta-flutter` Layer from the
  [github/meta-flutter](https://github.com/meta-flutter):

  - URI: https://github.com/meta-flutter/meta-flutter.git
  - Branch: "{{ yocto.codename }}"
  - Tested Revision: See the [`default.xml`](https://git.automotivelinux.org/AGL/AGL-repo/tree/default.xml)
    manifest file for the `AGL-repo` repository for revision
    information.


### Feature Dependencies

The `meta-agl-demo` layer has the following AGL
[feature](../../../develop/platform/initialize-build.md#agl-features)
dependencies:

* Yocto Project `meta-security` Layer:

  - URI: https://git.yoctoproject.org/cgit/cgit.cgi/meta-security
  - Branch: "{{ yocto.codename }}"
  - Tested Revision: See the [`default.xml`](https://git.automotivelinux.org/AGL/AGL-repo/tree/default.xml)
    manifest file for the `AGL-repo` repository for revision
    information.

* `meta-agl` sub layers:

  - URI: https://gerrit.automotivelinux.org/gerrit/AGL/meta-agl
  - Branch: "{{ agl.codename }}"

* OpenEmbedded's `meta-openembedded` Layer:

  - URI: https://github.com/openembedded/meta-openembedded
  - Branch: "{{ yocto.codename }}"
  - Tested Revision: See the [`default.xml`](https://git.automotivelinux.org/AGL/AGL-repo/tree/default.xml)
    manifest file for the `AGL-repo` repository for revision
    information.

    Specifically, out of `meta-openembedded`, these sub-layers are used:

    - `meta-filesystems`
    - `meta-oe`
    - `meta-python`<br/><br/>

## Maintenance

All patches must be submitted via the AGL Gerrit instance at
<https://gerrit.automotivelinux.org>.  See this wiki page for
details:

<https://wiki.automotivelinux.org/agl-distro/contributing>

Layer maintainers:
* Jan-Simon Möller <jsmoeller@linuxfoundation.org>
