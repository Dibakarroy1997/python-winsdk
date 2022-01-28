# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

class IPwmControllerProvider(_winrt.Object):
    ...
    actual_frequency: _winrt.Double
    max_frequency: _winrt.Double
    min_frequency: _winrt.Double
    pin_count: _winrt.Int32
    def acquire_pin(pin: _winrt.Int32) -> None:
        ...
    def disable_pin(pin: _winrt.Int32) -> None:
        ...
    def enable_pin(pin: _winrt.Int32) -> None:
        ...
    def release_pin(pin: _winrt.Int32) -> None:
        ...
    def set_desired_frequency(frequency: _winrt.Double) -> _winrt.Double:
        ...
    def set_pulse_parameters(pin: _winrt.Int32, duty_cycle: _winrt.Double, invert_polarity: _winrt.Boolean) -> None:
        ...

class IPwmProvider(_winrt.Object):
    ...
    def get_controllers() -> winsdk.windows.foundation.collections.IVectorView[IPwmControllerProvider]:
        ...
