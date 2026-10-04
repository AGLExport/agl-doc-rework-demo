---
title: "meta-agl-devel"
source_path: "04_Developer_Guides/02_AGL_Platform_Development/01_AGL_Yocto_Layers/04_meta_agl_devel.md"
content_status: imported
---

## Introduction

The `meta-agl-devel` layer contains components that are being tested or
still in development.
The layer also contains software packages that Original Equipment
Manufacturers (OEMs) need but are not included in the AGL software.

## Sub-Layers

The `meta-agl-devel` layer contains the following files and sub-layers:

```
.
├── docs
├── meta-agl-ic-container
├── meta-agl-rdp
├── meta-agl-ros2
├── meta-agl-test
├── meta-egvirt
├── placeholder veloRT
├── placeholder veloFLUX
├── meta-offline-voice-agent
├── meta-uhmi
└── templates
```

The following list provides a summary of these sub-layers:

* `meta-agl-ic-container`: Provides Linux container based integrated system platform.
* `meta-agl-rdp`: Provides feature for video output over rdp.
* `meta-agl-ros2`: Provides demo with ROS2.
* `meta-agl-test`: Provides the test sets and test framework.
* `meta-egvirt`: Provides VirtIO features into AGL.
*  placeholder veloRT
*  placeholder veloFLUX
* `meta-offline-voice-agent`: Provides offline speech recognition and command execution features.
* `meta-uhmi`: Provides Unified HMI features into AGL.
* `templates`: Feature templates that support the `meta-agl-devel` layer.
