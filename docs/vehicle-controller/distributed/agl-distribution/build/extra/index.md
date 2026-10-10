---
title: Extra AGL system
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Extra AGL system

Build the dedicated Qt or Slint Instrument Cluster system using the sequence below. Both start from small userland and select their own cluster application packages.

1. [Setup build environment](setup/index.md): prepare the master checkout and select cluster features.
2. [Build target image](image/index.md): choose the Qt or Slint image recipe.
3. [Deploy to board](deploy/index.md): use the matching board artifacts and check the cluster UI/services.

Momi belongs to the Extra portfolio as a lightweight IVI example, while its execution requires a container host. Its complete build/deployment procedure is under [Container integration > Momi IVI demo](../../../../small-integrated/container-integration/demo-image/momi-ivi/index.md).

Review [Extra demo system](../../portfolio/extra-demo/index.md) and [Extra architecture](../../architecture/extra-demo/index.md). Use separate build directories for different machines and feature selections; see [Supported the other boards](../other-boards/index.md) for board prerequisites.
