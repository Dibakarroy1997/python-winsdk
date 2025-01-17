# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.applicationmodel.contacts
import winsdk.windows.applicationmodel.datatransfer
import winsdk.windows.foundation.collections
import winsdk.windows.storage.streams

Self = typing.TypeVar('Self')

class QuickLink(_winrt.Object):
    title: str
    thumbnail: typing.Optional[winsdk.windows.storage.streams.RandomAccessStreamReference]
    id: str
    supported_data_formats: typing.Optional[winsdk.windows.foundation.collections.IVector[str]]
    supported_file_types: typing.Optional[winsdk.windows.foundation.collections.IVector[str]]
    @staticmethod
    def _from(obj: _winrt.Object) -> QuickLink: ...
    def __init__(self) -> None: ...

class ShareOperation(_winrt.Object):
    data: typing.Optional[winsdk.windows.applicationmodel.datatransfer.DataPackageView]
    quick_link_id: str
    contacts: typing.Optional[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.applicationmodel.contacts.Contact]]
    @staticmethod
    def _from(obj: _winrt.Object) -> ShareOperation: ...
    def dismiss_u_i(self) -> None: ...
    def remove_this_quick_link(self) -> None: ...
    @typing.overload
    def report_completed(self) -> None: ...
    @typing.overload
    def report_completed(self, quicklink: typing.Optional[QuickLink]) -> None: ...
    def report_data_retrieved(self) -> None: ...
    def report_error(self, value: str) -> None: ...
    def report_started(self) -> None: ...
    def report_submitted_background_task(self) -> None: ...

