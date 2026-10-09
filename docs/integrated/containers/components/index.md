---
title: AGL Components
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# AGL Components

The container platform combines host extensions with guest applications. Host components allocate resources and start guests; each guest supplies its own graphical userland. All AGL layer references in this chapter use `master`, reviewed on 10 October 2026.

| Need | Component chapter | Execution context |
| --- | --- | --- |
| Assign displays and manage guests | [Platform extension](../extensions.md) | Container host |
| Understand the Momi applications | [AGL Reference Applications for IC demo](applications.md) | IVI demo guest |
| Select the host and guest composition | [Demo image for container integration](../demo/index.md) | Complete integration |

Use [Architecture](../architecture.md) for shared-kernel and device boundaries, and [Build Container integration](../build.md) for the complete host image. Common IVI services and APIs remain documented in the [distributed base platform's component catalog](../../../components/index.md); the guest recipe determines which of them are installed.
