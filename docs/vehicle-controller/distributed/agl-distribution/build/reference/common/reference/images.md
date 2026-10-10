---
title: AGL image targets
source_path: 01_Getting_Started/02_Building_AGL_Image/07_Available_Demo_Images.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# AGL image targets

This catalog describes the recipes in the [AGL master image directory](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/?h=master). Use the same resolved master manifest for the image, SDK and separately built guests. See [Releases & migration](../../../../../../../community/releases/index.md) to record and update that baseline.

## 1. Demo Images

Enable the required layers/features with `aglsetup.sh`. Package selection and network configuration depend on the target and selected features. The IVI and IVI-derived cluster recipes include the databroker by default; the control-panel recipe selects client packages instead. The [databroker package group](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/packagegroups/packagegroup-agl-kuksa-val-databroker.bb?h=master) selects `kuksa-can-provider` and its AGL DBC/VSS configuration.

### agl-ivi-image

Common IVI platform image. Other IVI recipes extend it with toolkit and application packages. It is useful when customizing platform services and packaging.

### agl-ivi-image-crosssdk

SDK-oriented image derived from `agl-ivi-image`. For Qt demo development, inspect `agl-ivi-demo-qt-crosssdk` as well.

### agl-ivi-image-flutter

Flutter IVI base derived from `agl-ivi-image`. It adds the Flutter platform package group and persistent storage API. The demo homescreen is selected by the derived demo image.

### agl-ivi-demo-flutter

Flutter IVI demo using `flutter-ics-homescreen` on the common Flutter IVI base. See [Basic demo system architecture](../../../../architecture/basic-demo/index.md) for the graphics, lifecycle, vehicle-data and audio paths.

### agl-ivi-demo-qt

Qt IVI demo with `homescreen`, `launcher` and separate Qt applications on the common IVI platform.

### agl-ivi-demo-qt-crosssdk

Corresponding SDK-oriented image for `agl-ivi-demo-qt`.

### agl-ivi-demo-control-panel

Weston-based image running `agl-demo-control-panel`. Its [recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-ivi-demo-control-panel.bb?h=master) installs KUKSA client/certificate packages and the control application. Connect it to the databroker used by the demo setup.

### agl-cluster-demo-flutter

IVI-derived Flutter Instrument Cluster image with `flutter-cluster-dashboard`, `flutter-auto`, cluster streaming receiver and KUKSA configuration. This differs from the dedicated small-userland cluster platform.

### agl-cluster-demo-qt

IVI-derived Qt Instrument Cluster image selected by `packagegroup-agl-cluster-demo-platform`. For the dedicated Instrument Cluster service and Qt GUI, use the [Qt Cluster build route](../../../extra/reference/cluster/qt.md).

### agl-gateway-demo

Minimal gateway demo image hosting the KUKSA.val databroker and CAN provider. The [recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-gateway-demo.bb?h=master) also installs `agl-vss-proxy` and the open databroker environment; development tools are conditional on `agl-devel`. Configure network access and CAN interfaces for the selected deployment. Read [Connected Gateway architecture](../../../../../../../vehicle-data/connected-gateway/architecture/index.md) for the reviewed data path.

### agl-telematics-demo

Minimal telematics image selecting `packagegroup-agl-telematics-demo-platform`. Its recipe requires the `3g` distribution feature.

## Coordinated demo configuration

The old `*-preconfigured` and `*-preconfigured-gateway` image names, and `agl-ivi-demo-html5`, are absent from the AGL master image directory. Do not use those older target names as master build commands. Coordinated IVI, cluster and gateway setups require configuration of the current image recipes and their client/provider packages.

The [KUKSA application configuration recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-connectivity/kuksa-val/kuksa-conf.bb?h=master) provides `kuksa-conf`, `kuksa-conf-demo-tradeshow`, `kuksa-conf-gateway-demo` and KVM configuration variants. They install alternative `kuksa.toml` files under `/etc/xdg/AGL`; these are configuration packages, not additional image targets.

The [gateway client configuration](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-connectivity/kuksa-val/kuksa-conf/kuksa.toml.gateway-demo?h=master) uses a remote broker at `192.168.10.4`. Confirm the broker address, TLS credentials and service placement on each participating system.

For CAN integration, select the appropriate provider configuration from the [Master CAN recipes](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-connectivity/kuksa-val/?h=master). The default AGL configuration uses `can0`; control-panel, bidirectional and gateway-hardware configurations are separate packages. In particular, `kuksa-can-provider-conf-gw-hardware` supplies a second `kuksa-can-provider-can1.service`. Installing that package and assigning the interfaces requires an explicit deployment configuration; the base gateway image does not imply the complete multi-board hardware setup.
