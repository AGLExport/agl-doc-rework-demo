---
title: Qt IVI homescreen
source_path: 06_Component_Documentation/40_Demo_Application/02_Qt_Demo_IVI/01_Qt_Homescreen.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# Qt IVI homescreen

The Qt IVI demo uses the `homescreen` shell application, a separate `launcher`, and individual Qt applications. The homescreen supplies the background and panels, reserves an area for application windows, and manages application activation and switching. Build the [Qt IVI demo](../../../build/basic/reference/ivi/qt-ivi-demo.md) or read the [image catalog](../../../build/reference/common/reference/images.md#agl-ivi-demo-qt) for its variants. To add an ordinary Qt application to this shell, follow [Qt application development](../../../applications/qt/index.md).

## Shell, launcher, and backends

The homescreen is an AGL shell client. It binds the compositor's `agl_shell` Wayland extension, assigns the background and activation region, and signals that the shell is ready. It uses the compositor's gRPC shell proxy to receive application window state and to activate surfaces. The separate launcher lists installed applications through `applaunchd`; application startup and visible-window activation are coordinated as described in [Application startup and applaunchd](../../application-framework/lifecycle-services/reference/application-startup.md).

The [homescreen source](https://git.automotivelinux.org/apps/homescreen/tree/) contains these main extension points:

| Source location | Responsibility |
| --- | --- |
| `homescreen/src/main.cpp` | Qt GUI entry point, Wayland shell binding, display selection, background creation, and shell readiness |
| `homescreen/src/homescreenhandler.cpp` | Shortcuts, application stack, startup notifications, and activation/switching |
| `homescreen/src/AglShellGrpcClient.cpp` and `homescreen/proto/agl_shell.proto` | AGL shell proxy client and interface |
| `homescreen/src/statusbarmodel.cpp`, `statusbarserver.cpp`, and `mastervolume.cpp` | Status and volume integration |
| `homescreen/qml/` | Background, panels, shortcuts, status, media, and speech UI components |
| `homescreen/meson.build` | Qt 6 dependencies, generated protocol code, resources, and executable build |

Service integration uses [`libqtappfw`](https://git.automotivelinux.org/apps/libqtappfw/tree/) as well as the compositor and launcher interfaces. Read the corresponding library/client implementation before changing vehicle, media, Bluetooth, or weather behavior. The [separate launcher source](https://git.automotivelinux.org/apps/launcher/tree/) is the place to change application-list presentation.

## Startup and configuration

The [homescreen recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-demo/homescreen/homescreen_git.bb) selects the source revision and installs `homescreen.service`, KUKSA configuration, and the demo token. The current unit:

- runs `/usr/bin/homescreen` as `agl-driver`;
- requires `agl-compositor.service` and `applaunchd.service`;
- uses `/run/user/1001/` as its Wayland runtime directory;
- reads optional environment settings from `/etc/default/homescreen`;
- starts as part of `graphical.target` and reports readiness after shell setup.

The [launcher unit](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-demo/launcher/files/launcher.service) starts `/usr/bin/launcher` after the homescreen and `applaunchd`. It is a separate application window with ID `launcher`.

The homescreen selects the Wayland Qt platform and AGL Qt Quick Controls style in its entry point. `HOMESCREEN_START_SCREEN` selects the named Qt screen for its main background; without it, the primary screen is used. `HOMESCREEN_DEMO_CI=1` selects its CI/demo layout. Keep those settings consistent with the selected board's outputs and the compositor configuration.

Application-specific databroker configuration is installed under `/etc/xdg/AGL/homescreen/`, including `kuksa.toml` and `homescreen.token`. Use the configuration and source revision from your image when changing the databroker endpoint or authorization settings.

## Inspect and extend

On the target, inspect startup and window-management errors:

```sh
systemctl status agl-compositor.service applaunchd.service homescreen.service launcher.service
journalctl -b -u homescreen.service -u launcher.service
```

A shell-binding error requires checking that the AGL compositor is running and that another shell client has not already bound `agl_shell`. For an application that starts but is not displayed, check its Wayland application ID against its registered launcher ID and inspect the shell proxy and compositor messages.

For a layout change, edit the QML component and its resources, and update the activation region in `main.cpp` when panel dimensions change. For shortcut or switching behavior, edit `homescreenhandler.cpp` while preserving the startup/state-event coordination. For a service change, update the corresponding `libqtappfw` client and recipe dependencies together.

Rebuild from the initialized Qt IVI BitBake shell with:

```sh
bitbake homescreen launcher
bitbake agl-ivi-demo-qt
```

Deploy the resulting image using your board's procedure and check shell readiness, launcher enumeration, starting an application, and switching back to it. The homescreen's own build uses Meson and AGL Wayland protocol code; the small CMake application in the Qt application guide is an example of a client launched by this shell.
