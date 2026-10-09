# Documentation Guidelines

These rules apply to technical documents under `docs/`.

This document must be adopt Github Pages.

This document must be describe English.

## Required Structure

Each document must be followed document structure as a follow.

- Home
  - Introduction
  - Distributed system
    - Quick start
      - Run Flutter IVI demo pre-build image 
        - QEMU x86-64
        - Raspberry Pi 4/5

    - Portfolio
      - Basic demo system 
        - Flutter IVI demo
        - Qt IVI demo
        - IVI based Flutter Cluster demo

      - Extra demo system
        - Qt based Cluster demo
        - Slint based Cluster demo
        - Momi IVI demo

    - Architecture
      - Basic demo system 
      - Extra demo system

    - Build AGL system
      - Basic AGL system 
        - Setup build environment
        - Build target image
        - Deploy to board

      - Extra AGL system
        - Setup build environment
        - Build target image
        - Deploy to board

      - Supported the other boards

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

      - AGL API
        - Table for APIs
        - Generic APIs
          - Redundancy file operation (librefop)
        - In-Vehicle Infotainment APIs
          - Persistent storage API
        - Instrument Cluster APIs
          - AGL Instrument Cluster API
        - Gateway APIs

    - Platform Customize
      - Create/Modify an AGL image
      - Create a custom recipe
      - Create a service 

    - Application development
      - Flutter application
      - Qt application

  - Small scale integrated system
    - Container integration
      - Architecture
      - Build Container integration
      - Container integration Customize
        - Create and Run Guest Container
      - Platform extension
        - DRM lease manager
        - Container Manager
  
    - KVM based integration
      - Build Platform


  - Large scale integrated system
    - SoDeV
      - Architecture
      - Build SoDeV
      - SoDeV Customize
        - Create and Run Guest VM
      - Platform extension
        - Unified HMI


  - AGL Development tools
    - Demo Control
      - Demo Control Panel
      - CARLA with AGL

    - Virtual Car CAN definition
      - AGL virtual car

  - Troubleshooting
  - Releases & migration
  - Contribute 

Do not omit, rename, duplicate, or reorder these headings.

## Required Contents at Section

"Home" section must be include the following content:
* What is AGL.
  More detail, should refer to AGL Coverage section.

* AGL Community information.


"Introduction" section must include the following content:
  The Software Defined Vehicle build on various vehicle technical trends. AGL is focusing on "Vehicle EE architecture" and "E2E Vehicle Data Processing".

  Vehicle EE architectures.
    Traditional distributed architecture.
    Figure out the distributed architecture.
    AGL distributed system mainly focuses on this.

    Domain architecture.
    Figure out the domain architecture.
    AGL small-scale integrated system mainly focuses on this.

    Central/Zone architecture.
    Figure out the Central/Zone architecture.
    AGL large-scale integrated system mainly focuses on this.

  E2E Vehicle Data Processing.
    Vehicle data has been processed in the cloud for 10-15 years by collecting it via the cellular network. Now, there are proposals to offload data processing to the vehicle side (Device Edge computing concept).
    This scenario needs to be considered based on E2E (End-to-End) optimization, including the network/cloud sides.


"Distributed system" section must be include the following content:
  AGL develops and provides a Linux distribution for automotive systems.  It focuses on a standalone system built on a single Linux Kernel and userland.


"Basic demo system" section must be include the following content:
  AGL provides a platform for IVI with demo software. This characteristic supports multiple GUI toolkit support. Flutter is the current mainstream GUI toolkit for AGL IVI. Qt6 is supported as well.
  The Flutter-based Instrument Cluster is built on the IVI platform. It's an example of an Instrument Cluster built on COVESA VSS.


"Extra demo system" section must be include the following content:
  Extra AGL system includes Instrument Cluster platform and minimal footprint IVI demo.
  AGL provides a platform for an Instrument Cluster with demo software.
  Qt-based Instrument Cluster is built on minimal userland that is starting point of small foot print userland.
  Slint-based Instrument Cluster is an early example of a Rust language-based Instrument Cluster.


"Basic demo system" section under "Architecture" section must be include the following content:
AGL Flutter IVI demo and AGL Qt IVI demo uses same AGL IVI platform.
Show the Flutter IVI demo detail with architecture diagram "agl-flutter-ivi-architecture.svg".
Show the Qt IVI demo detail with architecture diagram "agl-qt-ivi-architecture.svg".


"Small-scale integrated system" section must include the following content:
  AGL develops and provides a base platform for small-scale integrated systems. It focuses on integrating two or more features into a single system. This base platform integrates one or more AGL Linux distributions and/or other platforms.
  It uses Linux Container technology or Kernel-based Virtual Machine.


"Container integration" section must be include the following content:
  AGL Container integration realize light weight integrated system built on Linux.


"Large scale integrated system" section must be include the following content:
  SoDeV details shall import from https://www.automotivelinux.org/announcements/automotive-grade-linux-releases-open-source-sodev-reference-platform-for-software-defined-vehicles-and-welcomes-five-new-members/.
  Must be include official architecture diagram.


"SoDeV" section must be include the following content:
  SoDeV is large scale integrated system. Distributed system and Small-scale integrated system are possible to integrate on top of SoDeV. It realizes large scale mixed critical integrated system.
  
