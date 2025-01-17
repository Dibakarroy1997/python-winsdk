# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.foundation
import winsdk.windows.ui.uiautomation

class AutomationRemoteOperationStatus(enum.IntEnum):
    SUCCESS = 0
    MALFORMED_BYTECODE = 1
    INSTRUCTION_LIMIT_EXCEEDED = 2
    UNHANDLED_EXCEPTION = 3
    EXECUTION_FAILURE = 4

Self = typing.TypeVar('Self')

class AutomationAnnotationTypeRegistration:
    local_id: _winrt.Int32
    def __init__(self, local_id: _winrt.Int32) -> None: ...

class AutomationRemoteOperationOperandId:
    value: _winrt.Int32
    def __init__(self, value: _winrt.Int32) -> None: ...

class AutomationRemoteOperationResult(_winrt.Object):
    error_location: _winrt.Int32
    extended_error: winsdk.windows.foundation.HResult
    status: AutomationRemoteOperationStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> AutomationRemoteOperationResult: ...
    def get_operand(self, operand_id: AutomationRemoteOperationOperandId) -> typing.Optional[_winrt.Object]: ...
    def has_operand(self, operand_id: AutomationRemoteOperationOperandId) -> _winrt.Boolean: ...

class CoreAutomationRegistrar(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> CoreAutomationRegistrar: ...
    @staticmethod
    def register_annotation_type(guid: uuid.UUID) -> AutomationAnnotationTypeRegistration: ...
    @staticmethod
    def unregister_annotation_type(registration: AutomationAnnotationTypeRegistration) -> None: ...

class CoreAutomationRemoteOperation(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> CoreAutomationRemoteOperation: ...
    def __init__(self) -> None: ...
    def add_to_results(self, operand_id: AutomationRemoteOperationOperandId) -> None: ...
    def execute(self, bytecode_buffer: typing.Sequence[_winrt.UInt8]) -> typing.Optional[AutomationRemoteOperationResult]: ...
    def import_connection_bound_object(self, operand_id: AutomationRemoteOperationOperandId, connection_bound_object: typing.Optional[winsdk.windows.ui.uiautomation.AutomationConnectionBoundObject]) -> None: ...
    def import_element(self, operand_id: AutomationRemoteOperationOperandId, element: typing.Optional[winsdk.windows.ui.uiautomation.AutomationElement]) -> None: ...
    def import_text_range(self, operand_id: AutomationRemoteOperationOperandId, text_range: typing.Optional[winsdk.windows.ui.uiautomation.AutomationTextRange]) -> None: ...
    def is_opcode_supported(self, opcode: _winrt.UInt32) -> _winrt.Boolean: ...

class CoreAutomationRemoteOperationContext(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> CoreAutomationRemoteOperationContext: ...
    def get_operand(self, id: AutomationRemoteOperationOperandId) -> typing.Optional[_winrt.Object]: ...
    @typing.overload
    def set_operand(self, id: AutomationRemoteOperationOperandId, operand: typing.Optional[_winrt.Object]) -> None: ...
    @typing.overload
    def set_operand(self, id: AutomationRemoteOperationOperandId, operand: typing.Optional[_winrt.Object], operand_interface_id: uuid.UUID) -> None: ...

class RemoteAutomationClientSession(_winrt.Object):
    session_id: uuid.UUID
    @staticmethod
    def _from(obj: _winrt.Object) -> RemoteAutomationClientSession: ...
    @typing.overload
    def __init__(self, name: str) -> None: ...
    @typing.overload
    def __init__(self, name: str, session_id: uuid.UUID) -> None: ...
    def create_window_async(self, remote_window_id: _winrt.UInt64, remote_process_id: _winrt.UInt32, parent_automation_element: typing.Optional[_winrt.Object]) -> winsdk.windows.foundation.IAsyncOperation[RemoteAutomationWindow]: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def add_connection_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[RemoteAutomationClientSession, RemoteAutomationConnectionRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_connection_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_disconnected(self, handler: winsdk.windows.foundation.TypedEventHandler[RemoteAutomationClientSession, RemoteAutomationDisconnectedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_disconnected(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class RemoteAutomationConnectionRequestedEventArgs(_winrt.Object):
    local_pipe_name: str
    remote_process_id: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> RemoteAutomationConnectionRequestedEventArgs: ...

class RemoteAutomationDisconnectedEventArgs(_winrt.Object):
    local_pipe_name: str
    @staticmethod
    def _from(obj: _winrt.Object) -> RemoteAutomationDisconnectedEventArgs: ...

class RemoteAutomationServer(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> RemoteAutomationServer: ...
    @staticmethod
    def report_session(session_id: uuid.UUID) -> None: ...

class RemoteAutomationWindow(_winrt.Object):
    automation_provider: typing.Optional[_winrt.Object]
    @staticmethod
    def _from(obj: _winrt.Object) -> RemoteAutomationWindow: ...
    def unregister_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...

class ICoreAutomationConnectionBoundObjectProvider(_winrt.Object):
    is_com_threading_required: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> ICoreAutomationConnectionBoundObjectProvider: ...

class ICoreAutomationRemoteOperationExtensionProvider(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> ICoreAutomationRemoteOperationExtensionProvider: ...
    def call_extension(self, extension_id: uuid.UUID, context: typing.Optional[CoreAutomationRemoteOperationContext], operand_ids: typing.Sequence[AutomationRemoteOperationOperandId]) -> None: ...
    def is_extension_supported(self, extension_id: uuid.UUID) -> _winrt.Boolean: ...

