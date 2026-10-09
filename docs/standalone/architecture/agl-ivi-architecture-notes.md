---
title: "IVI architecture diagram sources and scope"
content_status: authored
---

# IVI architecture diagram sources and scope

The [Basic demo system architecture](basic.md) and its Flutter/Qt SVGs describe **Vibrant Vimba 22.0.0**, checked on 2026-10-09. The baseline is the official `vimba/22.0.0` tag in the AGL layer repositories. Client implementation links use the SRCREV selected by the corresponding tagged recipe. These are source-derived logical component diagrams.

## What the diagrams describe

Both images build on `agl-ivi-image.bb`. The Flutter base adds `flutter-auto`, its environment/configuration and the persistent storage API; the Qt demo adds the homescreen, launcher and Qt applications. The common IVI base selects platform services, including applaunchd, MPD, radio, HVAC and audio mixer services. Application startup through applaunchd/systemd remains separate from compositor surface activation.

The shared vehicle-data path uses the KUKSA.val databroker and COVESA VSS with AGL extensions. The Vimba package group selects `kuksa-can-provider`, `kuksa-can-provider-conf-agl` and `agl-vss-helper`. The default CAN configuration connects `can0` to the local databroker and reads `agl-vcar.dbc` and the installed VSS mapping. CAN hardware and bidirectional gateway configurations are deployment choices; the dashed diagram path reflects that hardware dependency.

The Flutter diagram includes a direct gRPC path to `agl-persistent-storage-api` for settings/profile persistence. Its recipe uses Rust/tonic and RocksDB, and the homescreen unit requires the service. Optional Flutter camera-streams and Flatpak-store demos are controlled by package-group settings and are outside the core view.

The default IVI demo hosts the databroker locally. The tagged gateway-client configuration points to a remote broker at `192.168.10.4`. Cluster streaming and container boundaries are described in [Container integration architecture](../../integrated/containers/architecture.md).

## Vimba source references

| Area | Tagged recipe or configuration | Selected component revision |
| --- | --- | --- |
| Release and layers | [Vimba 22.0.0 tag](https://git.automotivelinux.org/AGL/AGL-repo/tag/?h=vimba/22.0.0), [manifest](https://git.automotivelinux.org/AGL/AGL-repo/tree/default.xml?h=vimba/22.0.0) | AGL branch `vimba`; Yocto Wrynose; meta-qt6 6.12 |
| Shared image | [IVI base](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-ivi-image.bb?h=vimba/22.0.0), [Flutter base](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-ivi-image-flutter.bb?h=vimba/22.0.0) | Shared compositor/service platform; Flutter-specific additions |
| Demo applications | [Flutter image](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-ivi-demo-flutter.bb?h=vimba/22.0.0), [Qt image](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-ivi-demo-qt.bb?h=vimba/22.0.0) | Toolkit-specific HMI/application packages |
| Compositor | [Recipe](https://git.automotivelinux.org/AGL/meta-agl/tree/meta-agl-core/recipes-graphics/wayland/agl-compositor_git.bb?h=vimba/22.0.0), [protocol and proxy sources](https://git.automotivelinux.org/src/agl-compositor/tree/?id=05cf370ac95d6f2fe62eb24d992e5b3f11c5b58e) | `05cf370ac95d6f2fe62eb24d992e5b3f11c5b58e` |
| Application startup | [Recipe](https://git.automotivelinux.org/AGL/meta-agl/tree/meta-app-framework/recipes-core/applaunchd/applaunchd_git.bb?h=vimba/22.0.0), [README](https://git.automotivelinux.org/src/applaunchd/tree/README.md?id=c32fe42f40d0af8b31b6113a3140f52b83be7769) | `c32fe42f40d0af8b31b6113a3140f52b83be7769` |
| Flutter clients | [Recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-demo/flutter-ics-homescreen/flutter-ics-homescreen_git.bb?h=vimba/22.0.0), [providers](https://git.automotivelinux.org/apps/flutter-ics-homescreen/tree/lib/data/data_providers?id=2ce5a77cec61aed021f54100eeb21d98a2c30e84), [unit](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-demo/flutter-ics-homescreen/files/flutter-ics-homescreen.service?h=vimba/22.0.0) | `2ce5a77cec61aed021f54100eeb21d98a2c30e84` |
| Qt clients | [libqtappfw recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-demo/libqtappfw/libqtappfw_git.bb?h=vimba/22.0.0), [wrappers](https://git.automotivelinux.org/src/libqtappfw/tree/?id=352c84f60ff6e2a916443a7bb7c19dd704ffc727) | `352c84f60ff6e2a916443a7bb7c19dd704ffc727` |
| CAN integration | [Databroker package group](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/packagegroups/packagegroup-agl-kuksa-val-databroker.bb?h=vimba/22.0.0), [CAN configuration](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-connectivity/kuksa-val/kuksa-can-provider-conf-agl/config.ini?h=vimba/22.0.0), [gateway client configuration](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-connectivity/kuksa-val/kuksa-conf/kuksa.toml.gateway-demo?h=vimba/22.0.0) | `kuksa-can-provider` with AGL DBC/VSS mappings |
| Audio/HVAC services | [Service package group](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/packagegroups/packagegroup-agl-ivi-services.bb?h=vimba/22.0.0), [multimedia package group](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/packagegroups/packagegroup-agl-ivi-multimedia.bb?h=vimba/22.0.0) | MPD/radio, PipeWire/WirePlumber, databroker-connected mixer/HVAC |
| Persistence | [Recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-demo/agl-persistent-storage-api/agl-persistent-storage-api_git.bb?h=vimba/22.0.0) | `de8ecba1279ee2bcb55f0595017165c606fac835`, with the tagged recipe's dependency patch |

## Version and deployment selection

These diagrams use the tagged Vimba 22.0.0 baseline. The site's build guides use the branch configured in `mkdocs.yml`; consult [Releases & migration](../../releases/index.md) to distinguish the named release from development snapshots. For a concrete image, inspect the recipes and runtime configuration from its resolved source manifest. Installed applications, optional adapters and service locations can differ by variant.

The review verifies source composition and client/service relationships. It does not report a hardware boot or runtime test of these images.
