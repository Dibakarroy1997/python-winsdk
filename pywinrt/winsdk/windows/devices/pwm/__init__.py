# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Devices.Pwm")

try:
    import winsdk.windows.devices.pwm.provider
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

class PwmPulsePolarity(enum.IntEnum):
    ACTIVE_HIGH = 0
    ACTIVE_LOW = 1

PwmController = _ns_module.PwmController
PwmPin = _ns_module.PwmPin