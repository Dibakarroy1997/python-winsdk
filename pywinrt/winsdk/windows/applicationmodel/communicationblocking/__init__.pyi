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
    import winsdk.windows.foundation.collections
except Exception:
    pass

class CommunicationBlockingAccessManager(_winrt.Object):
    ...
    is_blocking_active: _winrt.Boolean
    def is_blocked_number_async(number: str) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]:
        ...
    def show_block_numbers_u_i(phone_numbers: typing.Iterable[str]) -> _winrt.Boolean:
        ...
    def show_blocked_calls_u_i() -> None:
        ...
    def show_blocked_messages_u_i() -> None:
        ...
    def show_unblock_numbers_u_i(phone_numbers: typing.Iterable[str]) -> _winrt.Boolean:
        ...

class CommunicationBlockingAppManager(_winrt.Object):
    ...
    is_current_app_active_blocking_app: _winrt.Boolean
    def request_set_as_active_blocking_app_async() -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]:
        ...
    def show_communication_blocking_settings_u_i() -> None:
        ...
