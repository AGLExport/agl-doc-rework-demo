---
title: Extra AGL system
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Extra AGL system

Build the dedicated Qt or Slint Instrument Cluster system using the sequence below. Both start from small userland and select their own cluster application packages.

1. [Setup build environment](setup.md): prepare the master checkout and select cluster features.
2. [Build target image](image.md): choose the Qt or Slint image recipe.
3. [Deploy to board](deploy.md): use the matching board artifacts and check the cluster UI/services.

Momi belongs to the Extra portfolio as a lightweight IVI example, while its execution requires a container host. Its complete build/deployment procedure is under [Container integration > Momi IVI demo](../../../small-integrated/containers/demo/momi-ivi.md).

Review [Extra demo system](../../portfolio/extra/index.md) and [Extra architecture](../../architecture/extra.md). Use separate build directories for different machines and feature selections; see [Supported the other boards](../other-boards.md) for board prerequisites.
