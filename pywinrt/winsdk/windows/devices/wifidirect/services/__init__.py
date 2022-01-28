# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Devices.WiFiDirect.Services")

try:
    import winsdk.windows.devices.enumeration
except Exception:
    pass

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.networking
except Exception:
    pass

try:
    import winsdk.windows.networking.sockets
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class WiFiDirectServiceAdvertisementStatus(enum.IntEnum):
    CREATED = 0
    STARTED = 1
    STOPPED = 2
    ABORTED = 3

class WiFiDirectServiceConfigurationMethod(enum.IntEnum):
    DEFAULT = 0
    PIN_DISPLAY = 1
    PIN_ENTRY = 2

class WiFiDirectServiceError(enum.IntEnum):
    SUCCESS = 0
    RADIO_NOT_AVAILABLE = 1
    RESOURCE_IN_USE = 2
    UNSUPPORTED_HARDWARE = 3
    NO_HARDWARE = 4

class WiFiDirectServiceIPProtocol(enum.IntEnum):
    TCP = 6
    UDP = 17

class WiFiDirectServiceSessionErrorStatus(enum.IntEnum):
    OK = 0
    DISASSOCIATED = 1
    LOCAL_CLOSE = 2
    REMOTE_CLOSE = 3
    SYSTEM_FAILURE = 4
    NO_RESPONSE_FROM_REMOTE = 5

class WiFiDirectServiceSessionStatus(enum.IntEnum):
    CLOSED = 0
    INITIATED = 1
    REQUESTED = 2
    OPEN = 3

class WiFiDirectServiceStatus(enum.IntEnum):
    AVAILABLE = 0
    BUSY = 1
    CUSTOM = 2

WiFiDirectService = _ns_module.WiFiDirectService
WiFiDirectServiceAdvertiser = _ns_module.WiFiDirectServiceAdvertiser
WiFiDirectServiceAutoAcceptSessionConnectedEventArgs = _ns_module.WiFiDirectServiceAutoAcceptSessionConnectedEventArgs
WiFiDirectServiceProvisioningInfo = _ns_module.WiFiDirectServiceProvisioningInfo
WiFiDirectServiceRemotePortAddedEventArgs = _ns_module.WiFiDirectServiceRemotePortAddedEventArgs
WiFiDirectServiceSession = _ns_module.WiFiDirectServiceSession
WiFiDirectServiceSessionDeferredEventArgs = _ns_module.WiFiDirectServiceSessionDeferredEventArgs
WiFiDirectServiceSessionRequest = _ns_module.WiFiDirectServiceSessionRequest
WiFiDirectServiceSessionRequestedEventArgs = _ns_module.WiFiDirectServiceSessionRequestedEventArgs