---
title: Application Framework
source_path: 06_Component_Documentation/20_IVI_Application_Framework/01_Introduction.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# Application Framework

The AGL master application framework uses systemd for process lifecycle and applaunchd's gRPC interface for application discovery, startup and status notifications. The compositor controls surface presentation separately. This chapter describes the current model rather than the migration history of older AGL frameworks.

## Service and application lifecycle

Package each service or application with its systemd unit and dependencies. Applications use system units with an explicit `User` setting when required; startup does not depend on creating a per-user desktop session. Unit configuration controls restart behavior, resource access and sandboxing.

The [master applaunchd recipe](https://git.automotivelinux.org/AGL/meta-agl/tree/meta-app-framework/recipes-core/applaunchd/applaunchd_git.bb?h=master) installs its service, AGL application templates and sandboxing drop-ins. Read [Create a service](../../../standalone/customize/service.md) and [Package and register an application](../../../standalone/applications/create-application.md) for packaging and unit examples.

## Application discovery and startup

Applaunchd enumerates systemd units matching `agl-app*@*.service`. Clients can request the installed application list, start an application and subscribe to lifecycle events through its protobuf/gRPC interface. Notifications concern applications started through applaunchd; do not infer equivalent events for every process started directly by another mechanism.

The [master launcher documentation](https://git.automotivelinux.org/AGL/documentation/tree/docs/06_Component_Documentation/20_IVI_Application_Framework/02_Application_Startup.md?h=master) and [Application startup and applaunchd](application-startup.md) describe IDs, requests and notifications. Use the interface revision selected by the master recipe for generated client code.

## Inter-process communication

AGL framework interfaces use gRPC. System software such as ConnMan and BlueZ can retain D-Bus interfaces; inspect each service's implementation and access policy rather than treating every installed service as the same API.

## Graphics and guest boundaries

Starting an application process and activating its graphical surface are separate operations. Flutter and Qt homescreens use [the AGL compositor](../../../components/services/graphics/agl-compositor.md) for display integration. Host [Container Manager](../../extensions/container-manager.md) and SoDeV domain management control guests independently of the launcher inside an AGL guest.

Use [Table for APIs](../../api/table.md) to locate the relevant interface, and [Releases & migration](../../../releases/index.md) to record the resolved master manifest used by the image and SDK.
