---
title: Flutter IVI homescreen
source_path: 06_Component_Documentation/40_Demo_Application/01_Flutter_Demo_IVI/01_Flutter_Homescreen.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# Flutter IVI homescreen

`flutter-ics-homescreen` is the main user interface in `agl-ivi-demo-flutter`. It combines the homescreen, dashboard, HVAC, media, weather, settings, and application list in a Flutter application. It also launches separately installed applications and asks the compositor to display their windows. Read the [demo overview](../../start/prebuilt/flutter.md) for the user experience and the [Flutter application guide](../../distributed/applications/flutter.md) for the development workspace.

## Components and service connections

The [application source](https://git.automotivelinux.org/apps/flutter-ics-homescreen/tree/) organizes the UI and service clients as follows:

| Source location | Responsibility |
| --- | --- |
| `lib/main.dart` | Application entry point and provider initialization |
| `lib/presentation/screens/` | Homescreen and the built-in dashboard, HVAC, media, settings, weather, and other pages |
| `lib/presentation/router/` | Navigation between built-in pages |
| `lib/data/data_providers/app_launcher.dart` | gRPC client for `applaunchd` and the AGL shell proxy; lists, starts, and activates external applications |
| `lib/data/data_providers/val_client.dart` and `vehicle_notifier.dart` | KUKSA.val vehicle data subscriptions and updates |
| `lib/core/constants/vss_path.dart` | VSS paths used by the UI |
| `lib/data/data_providers/` | Media/MPD, radio, audio, Bluetooth, storage, and optional voice-agent clients and state |
| `assets/`, `fonts/`, and `lib/data/theme/` | Visual assets, fonts, and theme definitions |

`applaunchd` owns application discovery and process startup; the homescreen uses the [AGL compositor](../services/graphics/agl-compositor.md) shell interface for window activation and switching. Vehicle values are supplied through the KUKSA.val databroker using COVESA VSS paths. Media, radio, persistent storage, and the optional voice agent remain separate services. Changing a page's appearance does not replace those backends.

The [upstream image recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-demo/flutter-ics-homescreen/flutter-ics-homescreen_git.bb) selects the application revision, Flutter build settings, configuration files, and systemd integration. Use the recipe from the same checkout as your target image when tracing a behavior or rebuilding it.

## Runtime configuration

The supplied `flutter-ics-homescreen.service` runs `flutter-auto` as `agl-driver` with Wayland application ID `homescreen`. It requires the compositor, application launcher, and persistent storage API. Its environment is read from `/etc/default/flutter` and optionally `/etc/default/flutter-ics-homescreen`.

The current configuration locations are:

- `/etc/xdg/AGL/flutter-ics-homescreen.toml`: application settings, such as background animation and service endpoint overrides.
- `/etc/xdg/AGL/kuksa.toml`: shared databroker settings.
- `/etc/xdg/AGL/flutter-ics-homescreen/kuksa.toml`: application-specific databroker settings, read after the shared settings.
- `/etc/xdg/AGL/flutter-ics-homescreen/flutter-ics-homescreen.token`: the supplied demo authorization token referenced by the application configuration.
- `/etc/xdg/AGL/flutter-ics-homescreen/radio-presets.toml`: radio presets.

Use [`app_config_provider.dart`](https://git.automotivelinux.org/apps/flutter-ics-homescreen/tree/lib/data/data_providers/app_config_provider.dart) for the accepted keys and defaults. In a setup with a separate gateway or VM backend, update the relevant hostname, port, and TLS settings to match that setup. The recipe also contains `ics-homescreen.toml`, which describes the embedder's background window and activation area; coordinate changes to that geometry with the compositor layout.

The recipe uses build-time Dart defines such as `DISABLE_BKG_ANIMATION` and `ENABLE_VOICE_ASSISTANT`. Change these in a recipe override and rebuild the bundle. Runtime settings and environment files cannot substitute for a compile-time define.

## Inspect and extend

On the target, check the UI and its required services:

```sh
systemctl status flutter-ics-homescreen.service
journalctl -b -u flutter-ics-homescreen.service
systemctl status agl-compositor.service applaunchd.service agl-persistent-storage-api.service
```

If a vehicle value remains unavailable, inspect the configured databroker connection and VSS path before changing the widget. If an external application is missing, check its `agl-app*@*.service` registration and matching Wayland ID using [Package and register an AGL application](../../distributed/applications/create-application.md).

For a visual change, start with the relevant page under `lib/presentation/screens/`, the shared widgets, or theme/assets. For a new vehicle value, add the appropriate VSS path and provider subscription, then connect the provider state to the page. For a new backend, add its client/configuration in `lib/data/data_providers/` and retain the UI's asynchronous state and error handling. Validate the change with the [Flutter workspace](../../distributed/applications/flutter.md), then integrate it through a recipe override rather than modifying files only on a running target.
