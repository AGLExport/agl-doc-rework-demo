# Documentation Guidelines

These rules apply to technical documents under `docs/`.

This document must be adopt Github Pages.

This document must be describe English.

## Required Structure

Each document must be followed document structure as a follow.

- Home
  - AGL Coverage
    - AGL distributed system.
      - In-Vehicle Infotainment
      - Instrument Cluster
      - Connected Gateway
    - AGL integrated system
      - SoDeV
      - Container integration
      - KVM based integration
  - Get started
    - Pre-build image for IVI demo
      - Flutter IVI demo
      - QEMU x86-64
      - Raspberry Pi 4/5
  - AGL standalone distribution development
    - Build
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
      - Build
      - SoDeV Customize
        - Create and Run Guest VM
    - Container integration
      - Build
      - Container integration Customize
        - Create and Run Guest Container
    - KVM based integration
      - Build
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
* What is AGL
* Background
  * Traditional distributed architecture.
  * Domain architecture.
  * Central/Zone architecture.
* AGL distributed system overview.
* AGL integrated system overview.




