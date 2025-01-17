# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.foundation
import winsdk.windows.foundation.collections
import winsdk.windows.networking
import winsdk.windows.networking.connectivity
import winsdk.windows.networking.sockets

class DnssdRegistrationStatus(enum.IntEnum):
    SUCCESS = 0
    INVALID_SERVICE_NAME = 1
    SERVER_ERROR = 2
    SECURITY_ERROR = 3

class DnssdServiceWatcherStatus(enum.IntEnum):
    CREATED = 0
    STARTED = 1
    ENUMERATION_COMPLETED = 2
    STOPPING = 3
    STOPPED = 4
    ABORTED = 5

Self = typing.TypeVar('Self')

class DnssdRegistrationResult(_winrt.Object):
    has_instance_name_changed: _winrt.Boolean
    ip_address: typing.Optional[winsdk.windows.networking.HostName]
    status: DnssdRegistrationStatus
    def __str__(self) -> str: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> DnssdRegistrationResult: ...
    def __init__(self) -> None: ...
    def to_string(self) -> str: ...

class DnssdServiceInstance(_winrt.Object):
    weight: _winrt.UInt16
    priority: _winrt.UInt16
    port: _winrt.UInt16
    host_name: typing.Optional[winsdk.windows.networking.HostName]
    dnssd_service_instance_name: str
    text_attributes: typing.Optional[winsdk.windows.foundation.collections.IMap[str, str]]
    def __str__(self) -> str: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> DnssdServiceInstance: ...
    def __init__(self, dnssd_service_instance_name: str, host_name: typing.Optional[winsdk.windows.networking.HostName], port: _winrt.UInt16) -> None: ...
    @typing.overload
    def register_datagram_socket_async(self, socket: typing.Optional[winsdk.windows.networking.sockets.DatagramSocket]) -> winsdk.windows.foundation.IAsyncOperation[DnssdRegistrationResult]: ...
    @typing.overload
    def register_datagram_socket_async(self, socket: typing.Optional[winsdk.windows.networking.sockets.DatagramSocket], adapter: typing.Optional[winsdk.windows.networking.connectivity.NetworkAdapter]) -> winsdk.windows.foundation.IAsyncOperation[DnssdRegistrationResult]: ...
    @typing.overload
    def register_stream_socket_listener_async(self, socket: typing.Optional[winsdk.windows.networking.sockets.StreamSocketListener]) -> winsdk.windows.foundation.IAsyncOperation[DnssdRegistrationResult]: ...
    @typing.overload
    def register_stream_socket_listener_async(self, socket: typing.Optional[winsdk.windows.networking.sockets.StreamSocketListener], adapter: typing.Optional[winsdk.windows.networking.connectivity.NetworkAdapter]) -> winsdk.windows.foundation.IAsyncOperation[DnssdRegistrationResult]: ...
    def to_string(self) -> str: ...

class DnssdServiceInstanceCollection(_winrt.Object, typing.Sequence[DnssdServiceInstance]):
    size: _winrt.UInt32
    def __len__(self) -> int: ...
    @typing.overload
    def __getitem__(self, index: int) -> DnssdServiceInstance: ...
    @typing.overload
    def __getitem__(self, index: slice) -> typing.Sequence[DnssdServiceInstance]: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> DnssdServiceInstanceCollection: ...
    def first(self) -> typing.Optional[winsdk.windows.foundation.collections.IIterator[DnssdServiceInstance]]: ...
    def get_at(self, index: _winrt.UInt32) -> typing.Optional[DnssdServiceInstance]: ...
    def get_many(self, start_index: _winrt.UInt32, items_size: _winrt.UInt32) -> typing.Tuple[_winrt.UInt32, typing.List[DnssdServiceInstance]]: ...
    def index_of(self, value: typing.Optional[DnssdServiceInstance]) -> typing.Tuple[_winrt.Boolean, _winrt.UInt32]: ...

class DnssdServiceWatcher(_winrt.Object):
    status: DnssdServiceWatcherStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> DnssdServiceWatcher: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def add_added(self, handler: winsdk.windows.foundation.TypedEventHandler[DnssdServiceWatcher, DnssdServiceInstance]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_added(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_enumeration_completed(self, handler: winsdk.windows.foundation.TypedEventHandler[DnssdServiceWatcher, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_enumeration_completed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_stopped(self, handler: winsdk.windows.foundation.TypedEventHandler[DnssdServiceWatcher, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_stopped(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

