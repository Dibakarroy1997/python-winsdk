# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

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
    import winsdk.windows.storage.streams
except Exception:
    pass

try:
    import winsdk.windows.ui.popups
except Exception:
    pass

class DialAppLaunchResult(enum.IntEnum):
    LAUNCHED = 0
    FAILED_TO_LAUNCH = 1
    NOT_FOUND = 2
    NETWORK_FAILURE = 3

class DialAppState(enum.IntEnum):
    UNKNOWN = 0
    STOPPED = 1
    RUNNING = 2
    NETWORK_FAILURE = 3

class DialAppStopResult(enum.IntEnum):
    STOPPED = 0
    STOP_FAILED = 1
    OPERATION_NOT_SUPPORTED = 2
    NETWORK_FAILURE = 3

class DialDeviceDisplayStatus(enum.IntEnum):
    NONE = 0
    CONNECTING = 1
    CONNECTED = 2
    DISCONNECTING = 3
    DISCONNECTED = 4
    ERROR = 5

class DialApp(_winrt.Object):
    ...
    app_name: str
    def get_app_state_async() -> winsdk.windows.foundation.IAsyncOperation[DialAppStateDetails]:
        ...
    def request_launch_async(app_argument: str) -> winsdk.windows.foundation.IAsyncOperation[DialAppLaunchResult]:
        ...
    def stop_async() -> winsdk.windows.foundation.IAsyncOperation[DialAppStopResult]:
        ...

class DialAppStateDetails(_winrt.Object):
    ...
    full_xml: str
    state: DialAppState

class DialDevice(_winrt.Object):
    ...
    id: str
    friendly_name: str
    thumbnail: winsdk.windows.storage.streams.IRandomAccessStreamReference
    def device_info_supports_dial_async(device: winsdk.windows.devices.enumeration.DeviceInformation) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]:
        ...
    def from_id_async(value: str) -> winsdk.windows.foundation.IAsyncOperation[DialDevice]:
        ...
    def get_device_selector(app_name: str) -> str:
        ...
    def get_dial_app(app_name: str) -> DialApp:
        ...

class DialDevicePicker(_winrt.Object):
    ...
    appearance: winsdk.windows.devices.enumeration.DevicePickerAppearance
    filter: DialDevicePickerFilter
    def __init__(self, ) -> None:
        ...
    def hide() -> None:
        ...
    def pick_single_dial_device_async(selection: winsdk.windows.foundation.Rect) -> winsdk.windows.foundation.IAsyncOperation[DialDevice]:
        ...
    def pick_single_dial_device_async(selection: winsdk.windows.foundation.Rect, preferred_placement: winsdk.windows.ui.popups.Placement) -> winsdk.windows.foundation.IAsyncOperation[DialDevice]:
        ...
    def set_display_status(device: DialDevice, status: DialDeviceDisplayStatus) -> None:
        ...
    def show(selection: winsdk.windows.foundation.Rect) -> None:
        ...
    def show(selection: winsdk.windows.foundation.Rect, preferred_placement: winsdk.windows.ui.popups.Placement) -> None:
        ...
    def add_dial_device_picker_dismissed(handler: winsdk.windows.foundation.TypedEventHandler[DialDevicePicker, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_dial_device_picker_dismissed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_dial_device_selected(handler: winsdk.windows.foundation.TypedEventHandler[DialDevicePicker, DialDeviceSelectedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_dial_device_selected(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_disconnect_button_clicked(handler: winsdk.windows.foundation.TypedEventHandler[DialDevicePicker, DialDisconnectButtonClickedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_disconnect_button_clicked(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class DialDevicePickerFilter(_winrt.Object):
    ...
    supported_app_names: winsdk.windows.foundation.collections.IVector[str]

class DialDeviceSelectedEventArgs(_winrt.Object):
    ...
    selected_dial_device: DialDevice

class DialDisconnectButtonClickedEventArgs(_winrt.Object):
    ...
    device: DialDevice

class DialReceiverApp(_winrt.Object):
    ...
    current: DialReceiverApp
    def get_additional_data_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IMap[str, str]]:
        ...
    def get_unique_device_name_async() -> winsdk.windows.foundation.IAsyncOperation[str]:
        ...
    def set_additional_data_async(additional_data: typing.Iterable[winsdk.windows.foundation.collections.IKeyValuePair[str, str]]) -> winsdk.windows.foundation.IAsyncAction:
        ...
