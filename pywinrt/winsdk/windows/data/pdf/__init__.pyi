# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.foundation
import winsdk.windows.storage
import winsdk.windows.storage.streams
import winsdk.windows.ui

class PdfPageRotation(enum.IntEnum):
    NORMAL = 0
    ROTATE90 = 1
    ROTATE180 = 2
    ROTATE270 = 3

Self = typing.TypeVar('Self')

class PdfDocument(_winrt.Object):
    is_password_protected: _winrt.Boolean
    page_count: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> PdfDocument: ...
    def get_page(self, page_index: _winrt.UInt32) -> typing.Optional[PdfPage]: ...
    @typing.overload
    @staticmethod
    def load_from_file_async(file: typing.Optional[winsdk.windows.storage.IStorageFile]) -> winsdk.windows.foundation.IAsyncOperation[PdfDocument]: ...
    @typing.overload
    @staticmethod
    def load_from_file_async(file: typing.Optional[winsdk.windows.storage.IStorageFile], password: str) -> winsdk.windows.foundation.IAsyncOperation[PdfDocument]: ...
    @typing.overload
    @staticmethod
    def load_from_stream_async(input_stream: typing.Optional[winsdk.windows.storage.streams.IRandomAccessStream]) -> winsdk.windows.foundation.IAsyncOperation[PdfDocument]: ...
    @typing.overload
    @staticmethod
    def load_from_stream_async(input_stream: typing.Optional[winsdk.windows.storage.streams.IRandomAccessStream], password: str) -> winsdk.windows.foundation.IAsyncOperation[PdfDocument]: ...

class PdfPage(_winrt.Object):
    dimensions: typing.Optional[PdfPageDimensions]
    index: _winrt.UInt32
    preferred_zoom: _winrt.Single
    rotation: PdfPageRotation
    size: winsdk.windows.foundation.Size
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> PdfPage: ...
    def close(self) -> None: ...
    def prepare_page_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    @typing.overload
    def render_to_stream_async(self, output_stream: typing.Optional[winsdk.windows.storage.streams.IRandomAccessStream]) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    @typing.overload
    def render_to_stream_async(self, output_stream: typing.Optional[winsdk.windows.storage.streams.IRandomAccessStream], options: typing.Optional[PdfPageRenderOptions]) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...

class PdfPageDimensions(_winrt.Object):
    art_box: winsdk.windows.foundation.Rect
    bleed_box: winsdk.windows.foundation.Rect
    crop_box: winsdk.windows.foundation.Rect
    media_box: winsdk.windows.foundation.Rect
    trim_box: winsdk.windows.foundation.Rect
    @staticmethod
    def _from(obj: _winrt.Object) -> PdfPageDimensions: ...

class PdfPageRenderOptions(_winrt.Object):
    source_rect: winsdk.windows.foundation.Rect
    is_ignoring_high_contrast: _winrt.Boolean
    destination_width: _winrt.UInt32
    destination_height: _winrt.UInt32
    bitmap_encoder_id: uuid.UUID
    background_color: winsdk.windows.ui.Color
    @staticmethod
    def _from(obj: _winrt.Object) -> PdfPageRenderOptions: ...
    def __init__(self) -> None: ...

