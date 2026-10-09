---
title: Redundancy file operation (librefop)
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Redundancy file operation (librefop)

`librefop` is a compact file-storage library with redundant copies. Its upstream description presents it as another implementation of the AGL basesystem backup-manager function. It stages new data, rotates previous data to backup, and chooses usable data during recovery. [Algorithm and recovery cases](https://git.automotivelinux.org/src/librefop/tree/README)

## Interface

| Operation | Public function |
| --- | --- |
| Create a handle | `refop_create_redundancy_handle` |
| Release the handle | `refop_release_redundancy_handle` |
| Store data | `refop_set_redundancy_data` |
| Retrieve data and size | `refop_get_redundancy_data` |
| Remove stored data | `refop_remove_redundancy_data` |

The [public header](https://git.automotivelinux.org/src/librefop/tree/include/librefop.h) defines argument types and return values. Distinguish ordinary success, recovery, missing or broken data, invalid arguments, and system errors. Check the returned size when reading into a buffer.

## Integration

Select the library recipe and dependencies in your release, include the public header, and follow [upstream examples and tests](https://git.automotivelinux.org/src/librefop/tree/) for allocation/error handling. The README describes optional address-sanitizer, coverage, and unit-test configuration.

This file API differs from the service interface in [Persistent storage API](../ivi/persistent-storage.md). Choose the interface that fits your storage model.
