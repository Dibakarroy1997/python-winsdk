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
    import winsdk.windows.system.threading
except Exception:
    pass

class PreallocatedWorkItem(_winrt.Object):
    ...
    def __init__(self, handler: winsdk.windows.system.threading.WorkItemHandler) -> None:
        ...
    def __init__(self, handler: winsdk.windows.system.threading.WorkItemHandler, priority: winsdk.windows.system.threading.WorkItemPriority) -> None:
        ...
    def __init__(self, handler: winsdk.windows.system.threading.WorkItemHandler, priority: winsdk.windows.system.threading.WorkItemPriority, options: winsdk.windows.system.threading.WorkItemOptions) -> None:
        ...
    def run_async() -> winsdk.windows.foundation.IAsyncAction:
        ...

class SignalNotifier(_winrt.Object):
    ...
    def attach_to_event(name: str, handler: SignalHandler) -> SignalNotifier:
        ...
    def attach_to_event(name: str, handler: SignalHandler, timeout: winsdk.windows.foundation.TimeSpan) -> SignalNotifier:
        ...
    def attach_to_semaphore(name: str, handler: SignalHandler) -> SignalNotifier:
        ...
    def attach_to_semaphore(name: str, handler: SignalHandler, timeout: winsdk.windows.foundation.TimeSpan) -> SignalNotifier:
        ...
    def enable() -> None:
        ...
    def terminate() -> None:
        ...

SignalHandler = typing.Callable[[SignalNotifier, _winrt.Boolean], None]
