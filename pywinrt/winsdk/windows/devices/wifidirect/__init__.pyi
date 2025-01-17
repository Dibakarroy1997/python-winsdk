# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.devices.enumeration
import winsdk.windows.foundation
import winsdk.windows.foundation.collections
import winsdk.windows.networking
import winsdk.windows.security.credentials
import winsdk.windows.storage.streams

class WiFiDirectAdvertisementListenStateDiscoverability(enum.IntEnum):
    NONE = 0
    NORMAL = 1
    INTENSIVE = 2

class WiFiDirectAdvertisementPublisherStatus(enum.IntEnum):
    CREATED = 0
    STARTED = 1
    STOPPED = 2
    ABORTED = 3

class WiFiDirectConfigurationMethod(enum.IntEnum):
    PROVIDE_PIN = 0
    DISPLAY_PIN = 1
    PUSH_BUTTON = 2

class WiFiDirectConnectionStatus(enum.IntEnum):
    DISCONNECTED = 0
    CONNECTED = 1

class WiFiDirectDeviceSelectorType(enum.IntEnum):
    DEVICE_INTERFACE = 0
    ASSOCIATION_ENDPOINT = 1

class WiFiDirectError(enum.IntEnum):
    SUCCESS = 0
    RADIO_NOT_AVAILABLE = 1
    RESOURCE_IN_USE = 2

class WiFiDirectPairingProcedure(enum.IntEnum):
    GROUP_OWNER_NEGOTIATION = 0
    INVITATION = 1

Self = typing.TypeVar('Self')

class WiFiDirectAdvertisement(_winrt.Object):
    listen_state_discoverability: WiFiDirectAdvertisementListenStateDiscoverability
    is_autonomous_group_owner_enabled: _winrt.Boolean
    information_elements: typing.Optional[winsdk.windows.foundation.collections.IVector[WiFiDirectInformationElement]]
    legacy_settings: typing.Optional[WiFiDirectLegacySettings]
    supported_configuration_methods: typing.Optional[winsdk.windows.foundation.collections.IVector[WiFiDirectConfigurationMethod]]
    @staticmethod
    def _from(obj: _winrt.Object) -> WiFiDirectAdvertisement: ...

class WiFiDirectAdvertisementPublisher(_winrt.Object):
    advertisement: typing.Optional[WiFiDirectAdvertisement]
    status: WiFiDirectAdvertisementPublisherStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> WiFiDirectAdvertisementPublisher: ...
    def __init__(self) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def add_status_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[WiFiDirectAdvertisementPublisher, WiFiDirectAdvertisementPublisherStatusChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_status_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class WiFiDirectAdvertisementPublisherStatusChangedEventArgs(_winrt.Object):
    error: WiFiDirectError
    status: WiFiDirectAdvertisementPublisherStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> WiFiDirectAdvertisementPublisherStatusChangedEventArgs: ...

class WiFiDirectConnectionListener(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> WiFiDirectConnectionListener: ...
    def __init__(self) -> None: ...
    def add_connection_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[WiFiDirectConnectionListener, WiFiDirectConnectionRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_connection_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class WiFiDirectConnectionParameters(_winrt.Object):
    group_owner_intent: _winrt.Int16
    preferred_pairing_procedure: WiFiDirectPairingProcedure
    preference_ordered_configuration_methods: typing.Optional[winsdk.windows.foundation.collections.IVector[WiFiDirectConfigurationMethod]]
    @staticmethod
    def _from(obj: _winrt.Object) -> WiFiDirectConnectionParameters: ...
    def __init__(self) -> None: ...
    @staticmethod
    def get_device_pairing_kinds(configuration_method: WiFiDirectConfigurationMethod) -> winsdk.windows.devices.enumeration.DevicePairingKinds: ...

class WiFiDirectConnectionRequest(_winrt.Object):
    device_information: typing.Optional[winsdk.windows.devices.enumeration.DeviceInformation]
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> WiFiDirectConnectionRequest: ...
    def close(self) -> None: ...

class WiFiDirectConnectionRequestedEventArgs(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> WiFiDirectConnectionRequestedEventArgs: ...
    def get_connection_request(self) -> typing.Optional[WiFiDirectConnectionRequest]: ...

class WiFiDirectDevice(_winrt.Object):
    connection_status: WiFiDirectConnectionStatus
    device_id: str
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> WiFiDirectDevice: ...
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[WiFiDirectDevice]: ...
    @typing.overload
    @staticmethod
    def from_id_async(device_id: str, connection_parameters: typing.Optional[WiFiDirectConnectionParameters]) -> winsdk.windows.foundation.IAsyncOperation[WiFiDirectDevice]: ...
    def get_connection_endpoint_pairs(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.networking.EndpointPair]]: ...
    @typing.overload
    @staticmethod
    def get_device_selector() -> str: ...
    @typing.overload
    @staticmethod
    def get_device_selector(type: WiFiDirectDeviceSelectorType) -> str: ...
    def add_connection_status_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[WiFiDirectDevice, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_connection_status_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class WiFiDirectInformationElement(_winrt.Object):
    value: typing.Optional[winsdk.windows.storage.streams.IBuffer]
    oui_type: _winrt.UInt8
    oui: typing.Optional[winsdk.windows.storage.streams.IBuffer]
    @staticmethod
    def _from(obj: _winrt.Object) -> WiFiDirectInformationElement: ...
    def __init__(self) -> None: ...
    @staticmethod
    def create_from_buffer(buffer: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> typing.Optional[winsdk.windows.foundation.collections.IVector[WiFiDirectInformationElement]]: ...
    @staticmethod
    def create_from_device_information(device_information: typing.Optional[winsdk.windows.devices.enumeration.DeviceInformation]) -> typing.Optional[winsdk.windows.foundation.collections.IVector[WiFiDirectInformationElement]]: ...

class WiFiDirectLegacySettings(_winrt.Object):
    ssid: str
    passphrase: typing.Optional[winsdk.windows.security.credentials.PasswordCredential]
    is_enabled: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> WiFiDirectLegacySettings: ...

