# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.system.power
except Exception:
    pass

class Battery(_winrt.Object):
    ...
    device_id: str
    aggregate_battery: Battery
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[Battery]:
        ...
    def get_device_selector() -> str:
        ...
    def get_report() -> BatteryReport:
        ...
    def add_report_updated(handler: winsdk.windows.foundation.TypedEventHandler[Battery, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_report_updated(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class BatteryReport(_winrt.Object):
    ...
    charge_rate_in_milliwatts: typing.Optional[_winrt.Int32]
    design_capacity_in_milliwatt_hours: typing.Optional[_winrt.Int32]
    full_charge_capacity_in_milliwatt_hours: typing.Optional[_winrt.Int32]
    remaining_capacity_in_milliwatt_hours: typing.Optional[_winrt.Int32]
    status: winsdk.windows.system.power.BatteryStatus
