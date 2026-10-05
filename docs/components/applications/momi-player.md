---
title: "Momi Player"
content_status: authored
---

# Momi Player

Momi Player is a media-player reference application for AGL container integration. Its upstream README describes its origin in the Qt Media Player example. [Application README](https://git.automotivelinux.org/apps/momiplayer/tree/README.md)

The implementation includes playlists, audio/video playback, seeking, track selection, metadata display, and playback-error feedback. [Main.qml](https://git.automotivelinux.org/apps/momiplayer/tree/Main.qml)

Use it in a Momi guest prepared by the [container guide](../../integrated/containers/build-guide.md). [Momi Screen](momi-screen.md) explains application selection. Check guest access to media files and configured audio/display resources.

For playback failures, inspect the file, codecs, guest permissions, audio routing, and error message. Read the upstream license before copying implementation code; the README describes licensing separately from this documentation.
