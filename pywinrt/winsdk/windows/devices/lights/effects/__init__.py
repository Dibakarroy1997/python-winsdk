# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Devices.Lights.Effects")

try:
    import winsdk.windows.devices.lights
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
    import winsdk.windows.graphics.imaging
except Exception:
    pass

try:
    import winsdk.windows.ui
except Exception:
    pass

class LampArrayEffectCompletionBehavior(enum.IntEnum):
    CLEAR_STATE = 0
    KEEP_STATE = 1

class LampArrayEffectStartMode(enum.IntEnum):
    SEQUENTIAL = 0
    SIMULTANEOUS = 1

class LampArrayRepetitionMode(enum.IntEnum):
    OCCURRENCES = 0
    FOREVER = 1

LampArrayBitmapEffect = _ns_module.LampArrayBitmapEffect
LampArrayBitmapRequestedEventArgs = _ns_module.LampArrayBitmapRequestedEventArgs
LampArrayBlinkEffect = _ns_module.LampArrayBlinkEffect
LampArrayColorRampEffect = _ns_module.LampArrayColorRampEffect
LampArrayCustomEffect = _ns_module.LampArrayCustomEffect
LampArrayEffectPlaylist = _ns_module.LampArrayEffectPlaylist
LampArraySolidEffect = _ns_module.LampArraySolidEffect
LampArrayUpdateRequestedEventArgs = _ns_module.LampArrayUpdateRequestedEventArgs
ILampArrayEffect = _ns_module.ILampArrayEffect