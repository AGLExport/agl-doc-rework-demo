---
title: "AGL virtual car"
source_path: "06_Component_Documentation/80_DevTools/03_AGL_Virtual_Car_CAN/01_agl-vcar.md"
content_status: imported
---

# The CAN signal specification for the AGL virtual car.

## Overview
AGL's virtual car CAN signal specification provides an open, freely reusable set of CAN signals.  It's independent of existing CAN signal specifications.  AGL uses this specification for open-source development.  AGL users will be able to change the source code to adopt internal/confidential CAN signal specifications.

These CAN signal specification based on [AGL Instrument Cluster API specification](https://lf-automotivelinux.atlassian.net/wiki/spaces/IC/pages/17991785/IC-Service+API), [VSS specification](https://github.com/COVESA/vehicle_signal_specification), and passed demo development.

## Details of the AGL virtual car CAN signals

### Message list
| Category | Overview |
|:-----|:-----|
| [Vehicle Signal](../../reference/vehicle-signals/vehicle.md) | Vehicle speed, engine rpm, and turning signal. |
| [Body](../../reference/vehicle-signals/body.md) | . |
| [Sensor](../../reference/vehicle-signals/sensors.md) | Steering sensor, GNSS, and etc. |
