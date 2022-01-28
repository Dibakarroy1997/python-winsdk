# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum
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
    import winsdk.windows.gaming.input
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class GipFirmwareUpdateStatus(enum.IntEnum):
    COMPLETED = 0
    UP_TO_DATE = 1
    FAILED = 2

class GipMessageClass(enum.IntEnum):
    COMMAND = 0
    LOW_LATENCY = 1
    STANDARD_LATENCY = 2

class XusbDeviceSubtype(enum.IntEnum):
    UNKNOWN = 0
    GAMEPAD = 1
    ARCADE_PAD = 2
    ARCADE_STICK = 3
    FLIGHT_STICK = 4
    WHEEL = 5
    GUITAR = 6
    GUITAR_ALTERNATE = 7
    GUITAR_BASS = 8
    DRUM_KIT = 9
    DANCE_PAD = 10

class XusbDeviceType(enum.IntEnum):
    UNKNOWN = 0
    GAMEPAD = 1

class GameControllerVersionInfo:
    major: _winrt.UInt16
    minor: _winrt.UInt16
    build: _winrt.UInt16
    revision: _winrt.UInt16
    def __init__(self, major: _winrt.UInt16, minor: _winrt.UInt16, build: _winrt.UInt16, revision: _winrt.UInt16) -> None: ...

class GipFirmwareUpdateProgress:
    percent_completed: _winrt.Double
    current_component_id: _winrt.UInt32
    def __init__(self, percent_completed: _winrt.Double, current_component_id: _winrt.UInt32) -> None: ...

class GameControllerFactoryManager(_winrt.Object):
    ...
    def register_custom_factory_for_gip_interface(factory: ICustomGameControllerFactory, interface_id: uuid.UUID) -> None:
        ...
    def register_custom_factory_for_hardware_id(factory: ICustomGameControllerFactory, hardware_vendor_id: _winrt.UInt16, hardware_product_id: _winrt.UInt16) -> None:
        ...
    def register_custom_factory_for_xusb_type(factory: ICustomGameControllerFactory, xusb_type: XusbDeviceType, xusb_subtype: XusbDeviceSubtype) -> None:
        ...
    def try_get_factory_controller_from_game_controller(factory: ICustomGameControllerFactory, game_controller: winsdk.windows.gaming.input.IGameController) -> winsdk.windows.gaming.input.IGameController:
        ...

class GipFirmwareUpdateResult(_winrt.Object):
    ...
    extended_error_code: _winrt.UInt32
    final_component_id: _winrt.UInt32
    status: GipFirmwareUpdateStatus

class GipGameControllerProvider(IGameControllerProvider, _winrt.Object):
    ...
    firmware_version_info: GameControllerVersionInfo
    hardware_product_id: _winrt.UInt16
    hardware_vendor_id: _winrt.UInt16
    hardware_version_info: GameControllerVersionInfo
    is_connected: _winrt.Boolean
    def send_message(message_class: GipMessageClass, message_id: _winrt.UInt8, message_buffer: typing.Sequence[_winrt.UInt8]) -> None:
        ...
    def send_receive_message(message_class: GipMessageClass, message_id: _winrt.UInt8, request_message_buffer: typing.Sequence[_winrt.UInt8], response_message_buffer_size: _winrt.UInt32) -> typing.List[_winrt.UInt8]:
        ...
    def update_firmware_async(firmware_image: winsdk.windows.storage.streams.IInputStream) -> winsdk.windows.foundation.IAsyncOperationWithProgress[GipFirmwareUpdateResult, GipFirmwareUpdateProgress]:
        ...

class HidGameControllerProvider(IGameControllerProvider, _winrt.Object):
    ...
    firmware_version_info: GameControllerVersionInfo
    hardware_product_id: _winrt.UInt16
    hardware_vendor_id: _winrt.UInt16
    hardware_version_info: GameControllerVersionInfo
    is_connected: _winrt.Boolean
    usage_id: _winrt.UInt16
    usage_page: _winrt.UInt16
    def get_feature_report(report_id: _winrt.UInt8, report_buffer_size: _winrt.UInt32) -> typing.List[_winrt.UInt8]:
        ...
    def send_feature_report(report_id: _winrt.UInt8, report_buffer: typing.Sequence[_winrt.UInt8]) -> None:
        ...
    def send_output_report(report_id: _winrt.UInt8, report_buffer: typing.Sequence[_winrt.UInt8]) -> None:
        ...

class XusbGameControllerProvider(IGameControllerProvider, _winrt.Object):
    ...
    firmware_version_info: GameControllerVersionInfo
    hardware_product_id: _winrt.UInt16
    hardware_vendor_id: _winrt.UInt16
    hardware_version_info: GameControllerVersionInfo
    is_connected: _winrt.Boolean
    def set_vibration(low_frequency_motor_speed: _winrt.Double, high_frequency_motor_speed: _winrt.Double) -> None:
        ...

class ICustomGameControllerFactory(_winrt.Object):
    ...
    def create_game_controller(provider: IGameControllerProvider) -> _winrt.Object:
        ...
    def on_game_controller_added(value: winsdk.windows.gaming.input.IGameController) -> None:
        ...
    def on_game_controller_removed(value: winsdk.windows.gaming.input.IGameController) -> None:
        ...

class IGameControllerInputSink(_winrt.Object):
    ...
    def on_input_resumed(timestamp: _winrt.UInt64) -> None:
        ...
    def on_input_suspended(timestamp: _winrt.UInt64) -> None:
        ...

class IGameControllerProvider(_winrt.Object):
    ...
    firmware_version_info: GameControllerVersionInfo
    hardware_product_id: _winrt.UInt16
    hardware_vendor_id: _winrt.UInt16
    hardware_version_info: GameControllerVersionInfo
    is_connected: _winrt.Boolean

class IGipGameControllerInputSink(IGameControllerInputSink, _winrt.Object):
    ...
    def on_key_received(timestamp: _winrt.UInt64, key_code: _winrt.UInt8, is_pressed: _winrt.Boolean) -> None:
        ...
    def on_message_received(timestamp: _winrt.UInt64, message_class: GipMessageClass, message_id: _winrt.UInt8, sequence_id: _winrt.UInt8, message_buffer: typing.Sequence[_winrt.UInt8]) -> None:
        ...
    def on_input_resumed(timestamp: _winrt.UInt64) -> None:
        ...
    def on_input_suspended(timestamp: _winrt.UInt64) -> None:
        ...

class IHidGameControllerInputSink(IGameControllerInputSink, _winrt.Object):
    ...
    def on_input_report_received(timestamp: _winrt.UInt64, report_id: _winrt.UInt8, report_buffer: typing.Sequence[_winrt.UInt8]) -> None:
        ...
    def on_input_resumed(timestamp: _winrt.UInt64) -> None:
        ...
    def on_input_suspended(timestamp: _winrt.UInt64) -> None:
        ...

class IXusbGameControllerInputSink(IGameControllerInputSink, _winrt.Object):
    ...
    def on_input_received(timestamp: _winrt.UInt64, report_id: _winrt.UInt8, input_buffer: typing.Sequence[_winrt.UInt8]) -> None:
        ...
    def on_input_resumed(timestamp: _winrt.UInt64) -> None:
        ...
    def on_input_suspended(timestamp: _winrt.UInt64) -> None:
        ...
