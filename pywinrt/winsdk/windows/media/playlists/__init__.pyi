# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.foundation
import winsdk.windows.foundation.collections
import winsdk.windows.storage

class PlaylistFormat(enum.IntEnum):
    WINDOWS_MEDIA = 0
    ZUNE = 1
    M3U = 2

Self = typing.TypeVar('Self')

class Playlist(_winrt.Object):
    files: typing.Optional[winsdk.windows.foundation.collections.IVector[winsdk.windows.storage.StorageFile]]
    @staticmethod
    def _from(obj: _winrt.Object) -> Playlist: ...
    def __init__(self) -> None: ...
    @staticmethod
    def load_async(file: typing.Optional[winsdk.windows.storage.IStorageFile]) -> winsdk.windows.foundation.IAsyncOperation[Playlist]: ...
    @typing.overload
    def save_as_async(self, save_location: typing.Optional[winsdk.windows.storage.IStorageFolder], desired_name: str, option: winsdk.windows.storage.NameCollisionOption) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]: ...
    @typing.overload
    def save_as_async(self, save_location: typing.Optional[winsdk.windows.storage.IStorageFolder], desired_name: str, option: winsdk.windows.storage.NameCollisionOption, playlist_format: PlaylistFormat) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]: ...
    def save_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...

