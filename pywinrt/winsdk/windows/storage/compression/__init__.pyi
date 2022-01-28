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
    import winsdk.windows.storage.streams
except Exception:
    pass

class CompressAlgorithm(enum.IntEnum):
    INVALID_ALGORITHM = 0
    NULL_ALGORITHM = 1
    MSZIP = 2
    XPRESS = 3
    XPRESS_HUFF = 4
    LZMS = 5

class Compressor(winsdk.windows.storage.streams.IOutputStream, winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    def __init__(self, underlying_stream: winsdk.windows.storage.streams.IOutputStream) -> None:
        ...
    def __init__(self, underlying_stream: winsdk.windows.storage.streams.IOutputStream, algorithm: CompressAlgorithm, block_size: _winrt.UInt32) -> None:
        ...
    def close() -> None:
        ...
    def detach_stream() -> winsdk.windows.storage.streams.IOutputStream:
        ...
    def finish_async() -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]:
        ...
    def flush_async() -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]:
        ...
    def write_async(buffer: winsdk.windows.storage.streams.IBuffer) -> winsdk.windows.foundation.IAsyncOperationWithProgress[_winrt.UInt32, _winrt.UInt32]:
        ...

class Decompressor(winsdk.windows.storage.streams.IInputStream, winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    def __init__(self, underlying_stream: winsdk.windows.storage.streams.IInputStream) -> None:
        ...
    def close() -> None:
        ...
    def detach_stream() -> winsdk.windows.storage.streams.IInputStream:
        ...
    def read_async(buffer: winsdk.windows.storage.streams.IBuffer, count: _winrt.UInt32, options: winsdk.windows.storage.streams.InputStreamOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[winsdk.windows.storage.streams.IBuffer, _winrt.UInt32]:
        ...
