# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Devices.Enumeration.Pnp")

try:
    import winsdk.windows.devices.enumeration
except ImportError:
    pass

try:
    import winsdk.windows.foundation
except ImportError:
    pass

try:
    import winsdk.windows.foundation.collections
except ImportError:
    pass

class PnpObjectType(enum.IntEnum):
    UNKNOWN = 0
    DEVICE_INTERFACE = 1
    DEVICE_CONTAINER = 2
    DEVICE = 3
    DEVICE_INTERFACE_CLASS = 4
    ASSOCIATION_ENDPOINT = 5
    ASSOCIATION_ENDPOINT_CONTAINER = 6
    ASSOCIATION_ENDPOINT_SERVICE = 7
    DEVICE_PANEL = 8

_ns_module._register_PnpObjectType(PnpObjectType)

PnpObject = _ns_module.PnpObject
PnpObjectCollection = _ns_module.PnpObjectCollection
PnpObjectUpdate = _ns_module.PnpObjectUpdate
PnpObjectWatcher = _ns_module.PnpObjectWatcher
