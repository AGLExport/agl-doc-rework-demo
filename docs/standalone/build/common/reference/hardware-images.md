---
title: Hardware image configurations
source_path: 02_Hardware_Support/02_Supported_Hardware_Images.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# Hardware image configurations

### Supported Hardware Images

AGL supports a variety of interfaces, each requiring unique setup configuration.

#### 1. In-Vehicle Infotainment (IVI)

**Supported boards** :

AGL Reference Boards [QEMU, RCar Gen 3, Raspberry Pi 4](hardware.md), & agl-refhw

Community supported Boards [BBE, i. MX 6, i. MX 8](hardware.md)

* Qt Based :

    * Setting up flags at `aglsetup` script :

        ```sh
        $ source meta-agl/scripts/aglsetup.sh -f -m $MACHINE -b build-$MACHINE agl-demo

        #To enable Developer Options
        $ source meta-agl/scripts/aglsetup.sh -f -m $MACHINE -b build-$MACHINE agl-demo agl-devel
        ```

    * Building target image :

        ```sh
        $ time bitbake agl-ivi-demo-qt
        ```

* HTML5 Based :

    * Setting up flags at `aglsetup` script :

        ```sh
        $ source meta-agl/scripts/aglsetup.sh -f -m $MACHINE -b build-$MACHINE agl-demo

        # To enable Developer Options
        $ source meta-agl/scripts/aglsetup.sh -f -m $MACHINE -b build-$MACHINE agl-demo agl-devel
        ```

    * Building target image :

        ```sh
        $ time bitbake agl-ivi-demo-html5
        ```


#### 2. Instrument Cluster

**Supported boards** :

AGL Reference Boards [QEMU, RCar Gen 3, & Raspberry Pi 4](hardware.md)

* Setting up flags at `aglsetup` script :

    ```sh
    $ source meta-agl/scripts/aglsetup.sh -f -m $MACHINE -b build-$MACHINE agl-demo

    # To enable Developer Options
    $ source meta-agl/scripts/aglsetup.sh -f -m $MACHINE -b build-$MACHINE agl-demo agl-devel
    ```

* Building target image :

    ```sh
    $ time bitbake agl-cluster-demo
    ```

#### 3. Telematics

Headless demo platform for low-spec boards.

**Supported boards** :

Community supported Boards [BeagleBone](hardware.md)


* Setting up flags at `aglsetup` script :

    ```sh
    $ source meta-agl/scripts/aglsetup.sh -f -m $MACHINE -b build-$MACHINE agl-demo

    # To enable Developer Options
    $ source meta-agl/scripts/aglsetup.sh -f -m $MACHINE -b build-$MACHINE agl-demo agl-devel
    ```

* Building target image :

    ```sh
    $ time bitbake agl-telematics-demo
    ```
