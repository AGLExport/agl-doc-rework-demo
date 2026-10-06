# Documentation Guidelines

These rules apply to technical documents under `docs/`.

This document must be adopt Github Pages.

This document must be describe English.

## Required Structure

Each document must be followed document structure as a follow.

- Home
  - AGL Artifact
    - Linux Distribution
      - In-Vehicle Infotainment
      - Instrument Cluster
      - Connected Gateway
    - Base platform for integrated system
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

Home section must be include the following content:
* What is AGL.
  More detail, should refer to AGL Coverage section.

* AGL Community information.


AGL Artifact section must be include the following content:
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


Linux Distribution section must be include the following content:
  AGL develops and provides a Linux distribution for automotive systems.  It focuses on a standalone system built on a single Linux Kernel and userland.


In-Vehicle Infotainment section must be include the following content:
  AGL provides a platform for IVI with demo software. This characteristic supports multiple GUI toolkit support. Flutter is the current mainstream GUI toolkit for AGL IVI. Qt6 is supported as well.


Instrument Cluster section must be include the following content:
  AGL provides a platform for an Instrument Cluster with demo software.
  The Flutter-based Instrument Cluster is built on the IVI platform. It's an example of an Instrument Cluster built on COVESA VSS.
  Qt-based Instrument Cluster is built on minimal userland that is starting point of small foot print userland.
  Slint-based Instrument Cluster is an early example of a Rust language-based Instrument Cluster.


Connected Gateway section must be include the following content:
  AGL provides a platform for Connected Gateway. More details are TBD.


Base platform for integrated system section must be include the following content:
  AGL develops and provides a base platform for automotive integrated systems. It focuses on a multi feature on one integrated system.
  This base platform integrates one or more AGL Linux distributions and/or other platforms.
  

SoDeV section must be include the following content:
  SoDeV details shall import from https://www.automotivelinux.org/announcements/automotive-grade-linux-releases-open-source-sodev-reference-platform-for-software-defined-vehicles-and-welcomes-five-new-members/.
  Must be include official architecture diagram.


Container integration section must be include the following content:
  AGL Container integration realize light weight integrated system built on Linux.


KVM based integration section must be include the following content:
  KVM based integration is another example for SoDeV.

