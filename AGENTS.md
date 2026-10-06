# Documentation Guidelines

These rules apply to technical documents under `docs/`.

This document must be adopt Github Pages.

This document must be describe English.

## Required Structure

Each document must be followed document structure as a follow.

- Home
  - AGL Coverage
    - AGL distributed system
      - In-Vehicle Infotainment
      - Instrument Cluster
      - Connected Gateway
    - AGL integrated system
      - SoDeV
      - Container integration
      - KVM based integration
  
  - AGL distributed system distribution
    - Quick start
      - Pre-build image for IVI demo
        - Flutter IVI demo
        - QEMU x86-64
        - Raspberry Pi 4/5

    - Build Platform
      - Common part
      - In-Vehicle Infotainment
        - Flutter IVI demo
        - Qt IVI demo
        - IVI based Flutter Cluster
      - Instrument Cluster
        - Qt based Cluster
        - Slint based Cluster

    - Platform Customize
      - Create/Modify an AGL image
      - Create a custom recipe
      - Create a service 
    - Application development
      - Flutter application
      - Qt application

  - AGL integrated system development
    - SoDeV
      - Build Platform
      - SoDeV Customize
        - Create and Run Guest VM
    - Container integration
      - Build Platform
      - Container integration Customize
        - Create and Run Guest Container
    - KVM based integration
      - Build Platform

  - AGL Components
    - AGL Reference Applications
      - Flutter IVI homescreen
      - Flutter Cluster
      - Qt IVI homescreen
      - Instrument Cluster reference GUI (Qt)
      - Momi Screen
      - Momi navigation
      - Momi Weather
      - Momi Player
    - AGL Services
      - Graphics
        - The AGL compositor
        - DRM lease manager
      - Sound
        - Pipewire & Wireplumber
      - Policies
        - Rule based arbitrator
      - Misc
        - Voice agent assistant
      - Instrument Cluster
        - Instrument Cluster service
    - IVI Application Framework
      - Application Lifecycle and Services
        - Application Framework
    - Platform extension
      - Unified HMI
      - Container Manager
    - Development Tools
      - Demo Control
        - Demo Control Panel
        - CARLA with AGL
      - Virtual Car CAN definition
        - AGL virtual car
    - AGL API
      - Table for APIs
      - Generic APIs
        - Redundancy file operation (librefop)
      - In-Vehicle Infotainment APIs
        - Persistent storage API
      - Instrument Cluster APIs
        - AGL Instrument Cluster API
      - Gateway APIs
  - Troubleshooting
  - Releases & migration
  - Contribute 

Do not omit, rename, duplicate, or reorder these headings.

## Required Contents at Section

Home section must be include these contents:
* What is AGL.
  More detail, should refer to AGL Coverage section.

* AGL Community information.


AGL Coverage section must be include these contents:
* Vehicle EE architectures.
  * Traditional distributed architecture.
    Figure out for distributed architecture.

  * Domain architecture.
    Figure out for Domain architecture.

  * Central/Zone architecture.
    Figure out for Central/Zone architecture.

* AGL distributed system.
  Overview. It's a base distribution for distributed ECUs.

* AGL integrated system.
  Overview. It's a base platform for Domain or Central/Zone architecture.

These contents should link to sub-sections.

