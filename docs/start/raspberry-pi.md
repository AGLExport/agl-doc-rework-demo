---
title: "Run AGL on Raspberry Pi 4"
source_path: "01_Getting_Started/01_Quickstart/01_Using_Ready_Made_Images.md"
content_status: imported
---

# Run AGL on Raspberry Pi 4

## Before you start

A Raspberry Pi 4, a suitable display, a network connection, and a microSD card.

Use artifacts from the same AGL build. The configured channel is **{{ agl.codename }} / {{ artifact_kind }}**.

## Start AGL

1. Download the [compressed prebuilt image]({{ agl_download_base }}/latest/raspberrypi4/deploy/images/raspberrypi4-64/agl-ivi-demo-qt-raspberrypi4-64.wic.zst).

  2. Extract the image into the SD card of Raspberry Pi 4 :

    ```sh
    $ lsblk
    $ sudo umount <sdcard_device_name>
    $ zstdcat -d agl-ivi-demo-qt-raspberrypi4-64.wic.zst | sudo dd of=<sdcard_device_name> bs=4M
    $ sync
    ```

    **IMPORTANT NOTE:** Before re-writing any device on your Build Host, you need to
        be sure you are actually writing to the removable MicroSD card and not some other
        device.
        Each computer is different and removable devices can change from time to time.
        Consequently, you should repeat the previous operation with the MicroSD card to
        confirm the device name every time you write to the card.

      To summarize this example so far, we have the following:
        The first SATA drive is `/dev/sda` and `/dev/sdc` corresponds to the MicroSD card, and is also marked as a removable device.You can see this in the output of the `lsblk` command where "1" appears in the "RM" column for that device.

  3. SSH into Raspberry Pi :
    - Connect Raspberry Pi to network : `Homescreen > Settings`, IP address mentioned here.
    - `ssh root@<Raspberry-Pi-ip-address>`


  4. Serial Debugging :

    When things go wrong, you can take steps to debug your Raspberry Pi.
    For debugging, you need a 3.3 Volt USB Serial cable to facilitate
    communication between your Raspberry Pi board and your build host.

    You can reference the following diagram for information on the following steps:

    ![](../assets/source/01_Getting_Started/01_Quickstart/images/RaspberryPi2-ModelB-debug-serial-cable.png)

    1. Connect the TTL cable to the Universal Asynchronous Receiver-Transmitter
      (UART) connection on your Raspberry Pi board.
      Do not connect the USB side of the cable to your build host at this time.

          **CAUTION:** No warranty is provided using the following procedure.
          Pay particular attention to the colors of your cable as they could
          vary depending on the vendor.

    2. Connect the cable's BLUE wire to pin 6 (i.e. Ground) of the UART.

    3. Connect the cable's GREEN RX line to pin 8 (i.e. the TXD line) of
      the UART.

    4. Connect the cable's RED TX line to pin 10 (i.e. the RXD line) of
      the UART.

    5. Plug the USB connector of the cable into your build host's USB port.

    6. Use your favorite tool for serial communication between your build host
      and your Raspberry Pi.
      For example, if your build host is a native Linux machine (e.g. Ubuntu)
      you could use `screen` as follows from a terminal on the build host:

      ```sh
      $ sudo screen /dev/ttyUSB0 115200
      ```

## Confirm the result

Confirm that the AGL console or demo UI starts. Check the image and kernel names if boot fails, and record the build identifier before reporting a problem.

## Next steps

- [Troubleshooting](../troubleshooting/index.md)
- [Develop an application](../develop/index.md#apps)
- [Choose another environment](prebuilt-images.md)
