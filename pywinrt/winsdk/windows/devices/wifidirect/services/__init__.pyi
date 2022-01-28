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

class WiFiDirectService(_winrt.Object):
    ...
    session_info: winsdk.windows.storage.streams.IBuffer
    prefer_group_owner_mode: _winrt.Boolean
    remote_service_info: winsdk.windows.storage.streams.IBuffer
    service_error: WiFiDirectServiceError
    supported_configuration_methods: winsdk.windows.foundation.collections.IVectorView[WiFiDirectServiceConfigurationMethod]
    def connect_async() -> winsdk.windows.foundation.IAsyncOperation[WiFiDirectServiceSession]:
        ...
    def connect_async(pin: str) -> winsdk.windows.foundation.IAsyncOperation[WiFiDirectServiceSession]:
        ...
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[WiFiDirectService]:
        ...
    def get_provisioning_info_async(selected_configuration_method: WiFiDirectServiceConfigurationMethod) -> winsdk.windows.foundation.IAsyncOperation[WiFiDirectServiceProvisioningInfo]:
        ...
    def get_selector(service_name: str) -> str:
        ...
    def get_selector(service_name: str, service_info_filter: winsdk.windows.storage.streams.IBuffer) -> str:
        ...
    def add_session_deferred(handler: winsdk.windows.foundation.TypedEventHandler[WiFiDirectService, WiFiDirectServiceSessionDeferredEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_session_deferred(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class WiFiDirectServiceAdvertiser(_winrt.Object):
    ...
    service_status: WiFiDirectServiceStatus
    service_info: winsdk.windows.storage.streams.IBuffer
    prefer_group_owner_mode: _winrt.Boolean
    deferred_session_info: winsdk.windows.storage.streams.IBuffer
    custom_service_status_code: _winrt.UInt32
    auto_accept_session: _winrt.Boolean
    service_error: WiFiDirectServiceError
    preferred_configuration_methods: winsdk.windows.foundation.collections.IVector[WiFiDirectServiceConfigurationMethod]
    service_name: str
    service_name_prefixes: winsdk.windows.foundation.collections.IVector[str]
    advertisement_status: WiFiDirectServiceAdvertisementStatus
    def __init__(self, service_name: str) -> None:
        ...
    def connect_async(device_info: winsdk.windows.devices.enumeration.DeviceInformation) -> winsdk.windows.foundation.IAsyncOperation[WiFiDirectServiceSession]:
        ...
    def connect_async(device_info: winsdk.windows.devices.enumeration.DeviceInformation, pin: str) -> winsdk.windows.foundation.IAsyncOperation[WiFiDirectServiceSession]:
        ...
    def start() -> None:
        ...
    def stop() -> None:
        ...
    def add_advertisement_status_changed(handler: winsdk.windows.foundation.TypedEventHandler[WiFiDirectServiceAdvertiser, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_advertisement_status_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_auto_accept_session_connected(handler: winsdk.windows.foundation.TypedEventHandler[WiFiDirectServiceAdvertiser, WiFiDirectServiceAutoAcceptSessionConnectedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_auto_accept_session_connected(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_session_requested(handler: winsdk.windows.foundation.TypedEventHandler[WiFiDirectServiceAdvertiser, WiFiDirectServiceSessionRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_session_requested(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class WiFiDirectServiceAutoAcceptSessionConnectedEventArgs(_winrt.Object):
    ...
    session: WiFiDirectServiceSession
    session_info: winsdk.windows.storage.streams.IBuffer

class WiFiDirectServiceProvisioningInfo(_winrt.Object):
    ...
    is_group_formation_needed: _winrt.Boolean
    selected_configuration_method: WiFiDirectServiceConfigurationMethod

class WiFiDirectServiceRemotePortAddedEventArgs(_winrt.Object):
    ...
    endpoint_pairs: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.networking.EndpointPair]
    protocol: WiFiDirectServiceIPProtocol

class WiFiDirectServiceSession(winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    advertisement_id: _winrt.UInt32
    error_status: WiFiDirectServiceSessionErrorStatus
    service_address: str
    service_name: str
    session_address: str
    session_id: _winrt.UInt32
    status: WiFiDirectServiceSessionStatus
    def add_datagram_socket_async(value: winsdk.windows.networking.sockets.DatagramSocket) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def add_stream_socket_listener_async(value: winsdk.windows.networking.sockets.StreamSocketListener) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def close() -> None:
        ...
    def get_connection_endpoint_pairs() -> winsdk.windows.foundation.collections.IVectorView[winsdk.windows.networking.EndpointPair]:
        ...
    def add_remote_port_added(handler: winsdk.windows.foundation.TypedEventHandler[WiFiDirectServiceSession, WiFiDirectServiceRemotePortAddedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_remote_port_added(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_session_status_changed(handler: winsdk.windows.foundation.TypedEventHandler[WiFiDirectServiceSession, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_session_status_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class WiFiDirectServiceSessionDeferredEventArgs(_winrt.Object):
    ...
    deferred_session_info: winsdk.windows.storage.streams.IBuffer

class WiFiDirectServiceSessionRequest(winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    device_information: winsdk.windows.devices.enumeration.DeviceInformation
    provisioning_info: WiFiDirectServiceProvisioningInfo
    session_info: winsdk.windows.storage.streams.IBuffer
    def close() -> None:
        ...

class WiFiDirectServiceSessionRequestedEventArgs(_winrt.Object):
    ...
    def get_session_request() -> WiFiDirectServiceSessionRequest:
        ...
