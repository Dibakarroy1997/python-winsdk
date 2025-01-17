# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.ApplicationModel.ExtendedExecution")

try:
    import winsdk.windows.foundation
except ImportError:
    pass

class ExtendedExecutionReason(enum.IntEnum):
    UNSPECIFIED = 0
    LOCATION_TRACKING = 1
    SAVING_DATA = 2

class ExtendedExecutionResult(enum.IntEnum):
    ALLOWED = 0
    DENIED = 1

class ExtendedExecutionRevokedReason(enum.IntEnum):
    RESUMED = 0
    SYSTEM_POLICY = 1

_ns_module._register_ExtendedExecutionReason(ExtendedExecutionReason)
_ns_module._register_ExtendedExecutionResult(ExtendedExecutionResult)
_ns_module._register_ExtendedExecutionRevokedReason(ExtendedExecutionRevokedReason)

ExtendedExecutionRevokedEventArgs = _ns_module.ExtendedExecutionRevokedEventArgs
ExtendedExecutionSession = _ns_module.ExtendedExecutionSession
