---
title: Diagnose common problems
---
# Diagnose common problems

Choose the symptom below, then capture enough context to identify the image and environment.

| Symptom | First checks | Related guide |
| --- | --- | --- |
| QEMU does not start | Host virtualization access, installed QEMU version, file paths, matching kernel and root filesystem. | [QEMU x86-64](../start/prebuilt/qemu-x86-64.md) |
| No display or unexpected resolution | The image's display requirements, selected graphics device, and board/display configuration. | [QEMU x86-64](../start/prebuilt/qemu-x86-64.md), [Raspberry Pi display](../standalone/build/common/hardware/raspberry-pi/display.md) |
| SSH connection fails | Target address and network connection. The supplied x86 QEMU command forwards host port 2222 to target port 22. | [Prebuilt environments](../start/prebuilt/index.md) |
| Source build fails early | Supported host distribution, required tools/packages, free storage, MACHINE, and selected features. | [Prepare a host](../standalone/build/common/prepare-host.md), [Initialize the build](../standalone/build/common/initialize-build.md) |
| An application does not appear in the launcher | Application identifier, matching service unit, and packaging configuration. | [Register an application](../standalone/applications/create-application.md), [Application startup](../components/framework/lifecycle/application-startup.md) |
| A multi-board demo cannot exchange data | Image variant, expected network addresses, and where the databroker runs. | [Preconfigured images](../standalone/build/common/reference/images.md#2-preconfigured-demo-images) |

## Collect target information

Run these commands on the **AGL target**, when a shell is available:

~~~sh
cat /etc/os-release
uname -a
ip address
systemctl --failed
journalctl -b --no-pager -n 100
~~~

For a specific service, replace SERVICE with the unit name documented in its guide:

~~~sh
systemctl status SERVICE --no-pager
journalctl -b -u SERVICE --no-pager -n 100
~~~

## Collect host and build information

On the **build host**, record the host distribution, exact source manifest/build identifier, MACHINE, image target, features, and the first relevant error in the build log. Include whether you used an SDK, a Flutter workspace, or a full image build.

Continue with [Get community help](getting-help.md) or [Report a bug](reporting-bugs.md).
