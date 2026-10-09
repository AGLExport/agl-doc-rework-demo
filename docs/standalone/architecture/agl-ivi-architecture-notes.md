---
title: IVI architecture diagram sources and scope
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# IVI architecture diagram sources and scope

The [Basic demo system architecture](basic.md) and its Flutter/Qt SVGs describe **AGL master**, checked on 2026-10-10. The baseline is the official `master` branch of the AGL manifest and layer repositories. Client implementation links use the SRCREV selected by the corresponding master recipe. These are source-derived logical component diagrams.

## What the diagrams describe

Both images build on `agl-ivi-image.bb`. The Flutter base adds `flutter-auto`, its environment/configuration and the persistent storage API; the Qt demo adds the homescreen, launcher and Qt applications. The common IVI base selects platform services, including applaunchd, MPD, radio, HVAC and audio mixer services. Application startup through applaunchd/systemd remains separate from compositor surface activation.

The shared vehicle-data path uses the KUKSA.val databroker and COVESA VSS with AGL extensions. The master package group selects `kuksa-can-provider`, `kuksa-can-provider-conf-agl` and `agl-vss-helper`. The default CAN configuration connects `can0` to the local databroker and reads `agl-vcar.dbc` and the installed VSS mapping. CAN hardware and bidirectional gateway configurations are deployment choices; the dashed diagram path reflects that hardware dependency.

The Flutter diagram includes a direct gRPC path to `agl-persistent-storage-api` for settings/profile persistence. Its recipe uses Rust/tonic and RocksDB, and the homescreen unit requires the service. Optional Flutter camera-streams and Flatpak-store demos are controlled by package-group settings and are outside the core view.

The default IVI demo hosts the databroker locally. The master gateway-client configuration points to a remote broker at `192.168.10.4`. Cluster streaming and container boundaries are described in [Container integration architecture](../../integrated/containers/architecture.md).

## Master source references

| Area | Master recipe or configuration | Selected component revision |
| --- | --- | --- |
| Release and layers | [manifest](https://git.automotivelinux.org/AGL/AGL-repo/tree/default.xml?h=master) | AGL branch `master`; Yocto Wrynose; meta-qt6 6.12 |
| Shared image | [IVI base](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-ivi-image.bb?h=master), [Flutter base](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-ivi-image-flutter.bb?h=master) | Shared compositor/service platform; Flutter-specific additions |
| Demo applications | [Flutter image](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-ivi-demo-flutter.bb?h=master), [Qt image](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-ivi-demo-qt.bb?h=master) | Toolkit-specific HMI/application packages |
| Compositor | [Recipe](https://git.automotivelinux.org/AGL/meta-agl/tree/meta-agl-core/recipes-graphics/wayland/agl-compositor_git.bb?h=master), [protocol and proxy sources](https://git.automotivelinux.org/src/agl-compositor/tree/?id=05cf370ac95d6f2fe62eb24d992e5b3f11c5b58e) | `05cf370ac95d6f2fe62eb24d992e5b3f11c5b58e` |
| Application startup | [Recipe](https://git.automotivelinux.org/AGL/meta-agl/tree/meta-app-framework/recipes-core/applaunchd/applaunchd_git.bb?h=master), [README](https://git.automotivelinux.org/src/applaunchd/tree/README.md?id=c32fe42f40d0af8b31b6113a3140f52b83be7769) | `c32fe42f40d0af8b31b6113a3140f52b83be7769` |
| Flutter clients | [Recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-demo/flutter-ics-homescreen/flutter-ics-homescreen_git.bb?h=master), [providers](https://git.automotivelinux.org/apps/flutter-ics-homescreen/tree/lib/data/data_providers?id=2ce5a77cec61aed021f54100eeb21d98a2c30e84), [unit](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-demo/flutter-ics-homescreen/files/flutter-ics-homescreen.service?h=master) | `2ce5a77cec61aed021f54100eeb21d98a2c30e84` |
| Qt clients | [libqtappfw recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-demo/libqtappfw/libqtappfw_git.bb?h=master), [wrappers](https://git.automotivelinux.org/src/libqtappfw/tree/?id=352c84f60ff6e2a916443a7bb7c19dd704ffc727) | `352c84f60ff6e2a916443a7bb7c19dd704ffc727` |
| CAN integration | [Databroker package group](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/packagegroups/packagegroup-agl-kuksa-val-databroker.bb?h=master), [CAN configuration](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-connectivity/kuksa-val/kuksa-can-provider-conf-agl/config.ini?h=master), [gateway client configuration](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-connectivity/kuksa-val/kuksa-conf/kuksa.toml.gateway-demo?h=master) | `kuksa-can-provider` with AGL DBC/VSS mappings |
| Audio/HVAC services | [Service package group](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/packagegroups/packagegroup-agl-ivi-services.bb?h=master), [multimedia package group](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/packagegroups/packagegroup-agl-ivi-multimedia.bb?h=master) | MPD/radio, PipeWire/WirePlumber, databroker-connected mixer/HVAC |
| Persistence | [Recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-demo/agl-persistent-storage-api/agl-persistent-storage-api_git.bb?h=master) | `de8ecba1279ee2bcb55f0595017165c606fac835`, with the master recipe's dependency patch |

## Version and deployment selection

These diagrams, the image catalog and build guides use AGL `master`. Component implementation links use the SRCREVs selected by the reviewed master recipes, so a component source link can be fixed to a commit while its AGL recipe baseline remains master. The [source-review record](../../assets/source-reviews/master-2026-10-10.json) captures the checked official URLs and hashes. Consult [Releases & migration](../../releases/index.md) to save the resolved master manifest for a concrete image.

Installed applications, optional adapters and service locations differ by profile. Inspect the selected recipes and runtime configuration when deploying another variant.

The review verifies source composition and client/service relationships. It does not report a hardware boot or runtime test of these images.
