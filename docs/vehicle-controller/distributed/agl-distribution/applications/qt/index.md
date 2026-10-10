---
title: Qt application
source_path: 04_Developer_Guides/03_AGL_Application_Development/Develop_using_Qt/01_AGL-SDK_for_Qt.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# Qt application

This example creates a small Qt 6 application, cross-compiles it with the AGL SDK, and registers it with the application launcher in an `agl-ivi-demo-qt` development image. Its executable, Wayland application ID, and systemd instance ID are all `agl-qt-hello`.

## Prepare the image and SDK

Boot the [Qt IVI demo](../../build/basic/reference/ivi/qt-ivi-demo.md), connect its network, and obtain its IP address with `ip address` on the target console. Install a Qt SDK for the same machine, AGL release, and image build using [Set up the AGL SDK](../reference/setup-sdk.md). A Flutter SDK alone does not provide the Qt development packages used here.

In a fresh Bash shell on the Linux development host, source the environment setup file printed by the SDK installer. For a qemux86-64 SDK installed at the location used in that guide:

```sh
source "$HOME/agl-app/agl-sdk/environment-setup-corei7-64-agl-linux"
mkdir -p "$HOME/agl-app/agl-qt-hello"
cd "$HOME/agl-app/agl-qt-hello"
test -f "$OE_CMAKE_TOOLCHAIN_FILE"
```

Use your installer's actual environment filename for an Arm or another target. Run SDK commands in this shell; use a separate shell for BitBake.

## Create the application

Save the following as `CMakeLists.txt`:

```cmake
cmake_minimum_required(VERSION 3.21)
project(agl-qt-hello LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Gui)
qt_add_executable(agl-qt-hello main.cpp)
target_link_libraries(agl-qt-hello PRIVATE Qt6::Gui)
install(TARGETS agl-qt-hello RUNTIME DESTINATION bin)
```

Save the following as `main.cpp`. It uses Qt GUI's raster window to keep the example independent of QML plugins and external assets:

```cpp
#include <QGuiApplication>
#include <QColor>
#include <QFont>
#include <QPaintEvent>
#include <QPainter>
#include <QRasterWindow>

class HelloWindow : public QRasterWindow
{
protected:
    void paintEvent(QPaintEvent *) override
    {
        QPainter painter(this);
        painter.fillRect(0, 0, width(), height(), QColor("#102030"));
        painter.setPen(Qt::white);
        QFont font = painter.font();
        font.setPointSize(28);
        painter.setFont(font);
        painter.drawText(QRect(0, 0, width(), height()), Qt::AlignCenter,
                         QStringLiteral("Hello from AGL and Qt 6"));
    }
};

int main(int argc, char **argv)
{
    QGuiApplication app(argc, argv);
    app.setApplicationName("agl-qt-hello");
    app.setDesktopFileName("agl-qt-hello");
    HelloWindow window;
    window.setTitle(QStringLiteral("AGL Qt Hello"));
    window.resize(800, 480);
    window.show();
    return app.exec();
}
```

Set the desktop file name before showing the first window: Qt's Wayland backend uses it as the application ID. The ID must match the systemd unit's instance name so the homescreen can activate the correct surface. See [Package and register an AGL application](../reference/create-application.md), [Qt GUI](https://doc.qt.io/qt-6/qtgui-index.html), and [QGuiApplication::desktopFileName](https://doc.qt.io/qt-6/qguiapplication.html#desktopFileName-prop).

## Cross-compile and stage

In the SDK shell, run:

```sh
cmake -S . -B build \
    -DCMAKE_TOOLCHAIN_FILE="$OE_CMAKE_TOOLCHAIN_FILE" \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr
cmake --build build --parallel
DESTDIR="$PWD/stage" cmake --install build
file stage/usr/bin/agl-qt-hello
```

The executable's architecture must match the target. If CMake cannot find `Qt6`, check that you installed the Qt SDK, sourced its setup file, and used its toolchain file. When changing SDKs or target machines, use a new build directory to avoid retaining the old CMake toolchain cache. The Qt SDK supplies host tools and target libraries through [meta-qt6's SDK integration](https://code.qt.io/cgit/yocto/meta-qt6.git/tree/classes/populate_sdk_qt6_base.bbclass).

## Deploy and register

Set `AGL_TARGET` to your target's reachable address. For QEMU with SSH port forwarding, also set `AGL_SSH_PORT` to the forwarded host port; use `22` for a board reached directly. This example assumes SSH access as `root` is enabled in the development image.

```sh
export AGL_TARGET=192.168.1.100
export AGL_SSH_PORT=22
scp -P "$AGL_SSH_PORT" stage/usr/bin/agl-qt-hello "root@$AGL_TARGET:/tmp/"
ssh -p "$AGL_SSH_PORT" "root@$AGL_TARGET"
```

Run these commands in the target shell. The symlink makes the instance visible to `applaunchd`; the drop-in adds the display name and Wayland setting while retaining the supplied template's `agl-driver` user and runtime directory:

```sh
install -m 0755 /tmp/agl-qt-hello /usr/bin/agl-qt-hello
test -f /usr/lib/systemd/system/agl-app@.service
ln -s /usr/lib/systemd/system/agl-app@.service \
    /etc/systemd/system/agl-app@agl-qt-hello.service
mkdir -p /etc/systemd/system/agl-app@agl-qt-hello.service.d
cat > /etc/systemd/system/agl-app@agl-qt-hello.service.d/app.conf <<'EOF'
[Unit]
Description=Qt Hello
Requires=agl-compositor.service
After=agl-compositor.service

[Service]
Environment=QT_QPA_PLATFORM=wayland
EOF
systemctl daemon-reload
reboot
```

Run registration once; if the instance symlink already exists, retain it and update the binary or drop-in. Rebooting makes both `applaunchd` and the homescreen read the new application list. Open the launcher and select **Qt Hello**. The window should display `Hello from AGL and Qt 6` in the homescreen's application area.

If it fails, inspect the target logs:

```sh
systemctl status agl-app@agl-qt-hello.service
journalctl -b -u agl-app@agl-qt-hello.service
journalctl -b -u agl-compositor.service -u applaunchd.service
```

A loader or missing-library error usually means the SDK and image do not match. A Wayland connection error requires checking the compositor, the target's `agl-driver` user, and `/run/user/1001/`. A running application whose window cannot be activated requires checking that its application ID matches `agl-qt-hello`.

## Include the application in an image

For repeatable deployment, put the source in a custom layer recipe and inherit `cmake qt6-cmake agl-app`, declare `DEPENDS = "qtbase"`, and set `AGL_APP_ID = "agl-qt-hello"` and `AGL_APP_NAME = "Qt Hello"`. Add the package to the image as described in [Create a custom recipe](../../customize/recipe/index.md) and [Create/Modify an AGL image](../../customize/image/index.md). The [upstream agl-app class](https://git.automotivelinux.org/AGL/meta-agl/tree/meta-app-framework/classes/agl-app.bbclass) installs the instance symlink and launcher metadata. Use a recipe to install an application icon following the [icon convention](../reference/create-application.md#basic-requirements).

For a larger Qt Quick application, add the Qt modules your application uses to both its recipe dependencies and SDK/image, and follow [Qt's CMake application guide](https://doc.qt.io/qt-6/cmake-get-started.html). The [Qt IVI homescreen](../../components/reference-applications/qt-homescreen/index.md) shows AGL shell and service integration beyond this minimal window.
