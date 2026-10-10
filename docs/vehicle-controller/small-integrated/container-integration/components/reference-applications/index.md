---
title: AGL Reference Applications for IC demo
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# AGL Reference Applications for IC demo

These reference applications provide the Momi IVI side of the IC/IVI container demonstration. They run in the IVI guest alongside a separate Instrument Cluster guest. The [Momi IVI demo](../../demo-image/momi-ivi/index.md) explains their execution environment and build route.

| Application | Function |
| --- | --- |
| [Momi Screen](momi-screen/index.md) | Homescreen and application selection |
| [Momi navigation](momi-navigation/index.md) | Navigation and map display |
| [Momi Weather](momi-weather/index.md) | Network-based weather example |
| [Momi Player](momi-player/index.md) | Media playback |

The guest packages and runtime configuration come from the `master` container profile. Read [Platform extension](../platform-extensions/index.md) for host resource control and [Architecture](../../architecture/index.md) for the display and optional audio paths.
