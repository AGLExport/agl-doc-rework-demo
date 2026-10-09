---
title: AGL Reference Applications for IC demo
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# AGL Reference Applications for IC demo

These reference applications provide the Momi IVI side of the IC/IVI container demonstration. They run in the IVI guest alongside a separate Instrument Cluster guest. The [Momi IVI demo](../demo/momi-ivi.md) explains their execution environment and build route.

| Application | Function |
| --- | --- |
| [Momi Screen](../../../components/applications/momi-screen.md) | Homescreen and application selection |
| [Momi navigation](../../../components/applications/momi-navigation.md) | Navigation and map display |
| [Momi Weather](../../../components/applications/momi-weather.md) | Network-based weather example |
| [Momi Player](../../../components/applications/momi-player.md) | Media playback |

The guest packages and runtime configuration come from the `master` container profile. Read [Platform extension](../extensions.md) for host resource control and [Architecture](../architecture.md) for the display and optional audio paths.
