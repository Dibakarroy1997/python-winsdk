# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Devices.Portable")

try:
    import winsdk.windows.storage
except ImportError:
    pass

class ServiceDeviceType(enum.IntEnum):
    CALENDAR_SERVICE = 0
    CONTACTS_SERVICE = 1
    DEVICE_STATUS_SERVICE = 2
    NOTES_SERVICE = 3
    RINGTONES_SERVICE = 4
    SMS_SERVICE = 5
    TASKS_SERVICE = 6

_ns_module._register_ServiceDeviceType(ServiceDeviceType)

ServiceDevice = _ns_module.ServiceDevice
StorageDevice = _ns_module.StorageDevice
