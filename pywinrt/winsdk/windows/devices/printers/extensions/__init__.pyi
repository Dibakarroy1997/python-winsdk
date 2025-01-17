# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.foundation

class Print3DWorkflowDetail(enum.IntEnum):
    UNKNOWN = 0
    MODEL_EXCEEDS_PRINT_BED = 1
    UPLOAD_FAILED = 2
    INVALID_MATERIAL_SELECTION = 3
    INVALID_MODEL = 4
    MODEL_NOT_MANIFOLD = 5
    INVALID_PRINT_TICKET = 6

class Print3DWorkflowStatus(enum.IntEnum):
    ABANDONED = 0
    CANCELED = 1
    FAILED = 2
    SLICING = 3
    SUBMITTED = 4

Self = typing.TypeVar('Self')

class Print3DWorkflow(_winrt.Object):
    is_print_ready: _winrt.Boolean
    device_i_d: str
    @staticmethod
    def _from(obj: _winrt.Object) -> Print3DWorkflow: ...
    def get_print_model_package(self) -> typing.Optional[_winrt.Object]: ...
    def add_print_requested(self, event_handler: winsdk.windows.foundation.TypedEventHandler[Print3DWorkflow, Print3DWorkflowPrintRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_print_requested(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_printer_changed(self, event_handler: winsdk.windows.foundation.TypedEventHandler[Print3DWorkflow, Print3DWorkflowPrinterChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_printer_changed(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class Print3DWorkflowPrintRequestedEventArgs(_winrt.Object):
    status: Print3DWorkflowStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> Print3DWorkflowPrintRequestedEventArgs: ...
    def set_extended_status(self, value: Print3DWorkflowDetail) -> None: ...
    def set_source(self, source: typing.Optional[_winrt.Object]) -> None: ...
    def set_source_changed(self, value: _winrt.Boolean) -> None: ...

class Print3DWorkflowPrinterChangedEventArgs(_winrt.Object):
    new_device_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> Print3DWorkflowPrinterChangedEventArgs: ...

class PrintExtensionContext(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintExtensionContext: ...
    @staticmethod
    def from_device_id(device_id: str) -> typing.Optional[_winrt.Object]: ...

class PrintNotificationEventDetails(_winrt.Object):
    event_data: str
    printer_name: str
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintNotificationEventDetails: ...

class PrintTaskConfiguration(_winrt.Object):
    printer_extension_context: typing.Optional[_winrt.Object]
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintTaskConfiguration: ...
    def add_save_requested(self, event_handler: winsdk.windows.foundation.TypedEventHandler[PrintTaskConfiguration, PrintTaskConfigurationSaveRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_save_requested(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class PrintTaskConfigurationSaveRequest(_winrt.Object):
    deadline: winsdk.windows.foundation.DateTime
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintTaskConfigurationSaveRequest: ...
    def cancel(self) -> None: ...
    def get_deferral(self) -> typing.Optional[PrintTaskConfigurationSaveRequestedDeferral]: ...
    def save(self, printer_extension_context: typing.Optional[_winrt.Object]) -> None: ...

class PrintTaskConfigurationSaveRequestedDeferral(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintTaskConfigurationSaveRequestedDeferral: ...
    def complete(self) -> None: ...

class PrintTaskConfigurationSaveRequestedEventArgs(_winrt.Object):
    request: typing.Optional[PrintTaskConfigurationSaveRequest]
    @staticmethod
    def _from(obj: _winrt.Object) -> PrintTaskConfigurationSaveRequestedEventArgs: ...

