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
import winsdk.windows.system

class AccessCacheOptions(enum.IntFlag):
    NONE = 0
    DISALLOW_USER_INPUT = 0x1
    FAST_LOCATIONS_ONLY = 0x2
    USE_READ_ONLY_CACHED_COPY = 0x4
    SUPPRESS_ACCESS_TIME_UPDATE = 0x8

class RecentStorageItemVisibility(enum.IntEnum):
    APP_ONLY = 0
    APP_AND_SYSTEM = 1

Self = typing.TypeVar('Self')

class AccessListEntry:
    token: str
    metadata: str
    def __init__(self, token: str, metadata: str) -> None: ...

class AccessListEntryView(_winrt.Object, typing.Sequence[AccessListEntry]):
    size: _winrt.UInt32
    def __len__(self) -> int: ...
    @typing.overload
    def __getitem__(self, index: int) -> AccessListEntry: ...
    @typing.overload
    def __getitem__(self, index: slice) -> typing.Sequence[AccessListEntry]: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> AccessListEntryView: ...
    def first(self) -> typing.Optional[winsdk.windows.foundation.collections.IIterator[AccessListEntry]]: ...
    def get_at(self, index: _winrt.UInt32) -> AccessListEntry: ...
    def get_many(self, start_index: _winrt.UInt32, items_size: _winrt.UInt32) -> typing.Tuple[_winrt.UInt32, typing.List[AccessListEntry]]: ...
    def index_of(self, value: AccessListEntry) -> typing.Tuple[_winrt.Boolean, _winrt.UInt32]: ...

class ItemRemovedEventArgs(_winrt.Object):
    removed_entry: AccessListEntry
    @staticmethod
    def _from(obj: _winrt.Object) -> ItemRemovedEventArgs: ...

class StorageApplicationPermissions(_winrt.Object):
    future_access_list: typing.Optional[StorageItemAccessList]
    most_recently_used_list: typing.Optional[StorageItemMostRecentlyUsedList]
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageApplicationPermissions: ...
    @staticmethod
    def get_future_access_list_for_user(user: typing.Optional[winsdk.windows.system.User]) -> typing.Optional[StorageItemAccessList]: ...
    @staticmethod
    def get_most_recently_used_list_for_user(user: typing.Optional[winsdk.windows.system.User]) -> typing.Optional[StorageItemMostRecentlyUsedList]: ...

class StorageItemAccessList(_winrt.Object):
    entries: typing.Optional[AccessListEntryView]
    maximum_items_allowed: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageItemAccessList: ...
    @typing.overload
    def add(self, file: typing.Optional[winsdk.windows.storage.IStorageItem]) -> str: ...
    @typing.overload
    def add(self, file: typing.Optional[winsdk.windows.storage.IStorageItem], metadata: str) -> str: ...
    @typing.overload
    def add_or_replace(self, token: str, file: typing.Optional[winsdk.windows.storage.IStorageItem]) -> None: ...
    @typing.overload
    def add_or_replace(self, token: str, file: typing.Optional[winsdk.windows.storage.IStorageItem], metadata: str) -> None: ...
    def check_access(self, file: typing.Optional[winsdk.windows.storage.IStorageItem]) -> _winrt.Boolean: ...
    def clear(self) -> None: ...
    def contains_item(self, token: str) -> _winrt.Boolean: ...
    @typing.overload
    def get_file_async(self, token: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]: ...
    @typing.overload
    def get_file_async(self, token: str, options: AccessCacheOptions) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]: ...
    @typing.overload
    def get_folder_async(self, token: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFolder]: ...
    @typing.overload
    def get_folder_async(self, token: str, options: AccessCacheOptions) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFolder]: ...
    @typing.overload
    def get_item_async(self, token: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.IStorageItem]: ...
    @typing.overload
    def get_item_async(self, token: str, options: AccessCacheOptions) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.IStorageItem]: ...
    def remove(self, token: str) -> None: ...

class StorageItemMostRecentlyUsedList(_winrt.Object):
    entries: typing.Optional[AccessListEntryView]
    maximum_items_allowed: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageItemMostRecentlyUsedList: ...
    @typing.overload
    def add(self, file: typing.Optional[winsdk.windows.storage.IStorageItem]) -> str: ...
    @typing.overload
    def add(self, file: typing.Optional[winsdk.windows.storage.IStorageItem], metadata: str) -> str: ...
    @typing.overload
    def add(self, file: typing.Optional[winsdk.windows.storage.IStorageItem], metadata: str, visibility: RecentStorageItemVisibility) -> str: ...
    @typing.overload
    def add_or_replace(self, token: str, file: typing.Optional[winsdk.windows.storage.IStorageItem]) -> None: ...
    @typing.overload
    def add_or_replace(self, token: str, file: typing.Optional[winsdk.windows.storage.IStorageItem], metadata: str) -> None: ...
    @typing.overload
    def add_or_replace(self, token: str, file: typing.Optional[winsdk.windows.storage.IStorageItem], metadata: str, visibility: RecentStorageItemVisibility) -> None: ...
    def check_access(self, file: typing.Optional[winsdk.windows.storage.IStorageItem]) -> _winrt.Boolean: ...
    def clear(self) -> None: ...
    def contains_item(self, token: str) -> _winrt.Boolean: ...
    @typing.overload
    def get_file_async(self, token: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]: ...
    @typing.overload
    def get_file_async(self, token: str, options: AccessCacheOptions) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]: ...
    @typing.overload
    def get_folder_async(self, token: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFolder]: ...
    @typing.overload
    def get_folder_async(self, token: str, options: AccessCacheOptions) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFolder]: ...
    @typing.overload
    def get_item_async(self, token: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.IStorageItem]: ...
    @typing.overload
    def get_item_async(self, token: str, options: AccessCacheOptions) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.IStorageItem]: ...
    def remove(self, token: str) -> None: ...
    def add_item_removed(self, handler: winsdk.windows.foundation.TypedEventHandler[StorageItemMostRecentlyUsedList, ItemRemovedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_item_removed(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class IStorageItemAccessList(_winrt.Object):
    entries: typing.Optional[AccessListEntryView]
    maximum_items_allowed: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> IStorageItemAccessList: ...
    @typing.overload
    def add(self, file: typing.Optional[winsdk.windows.storage.IStorageItem]) -> str: ...
    @typing.overload
    def add(self, file: typing.Optional[winsdk.windows.storage.IStorageItem], metadata: str) -> str: ...
    @typing.overload
    def add_or_replace(self, token: str, file: typing.Optional[winsdk.windows.storage.IStorageItem]) -> None: ...
    @typing.overload
    def add_or_replace(self, token: str, file: typing.Optional[winsdk.windows.storage.IStorageItem], metadata: str) -> None: ...
    def check_access(self, file: typing.Optional[winsdk.windows.storage.IStorageItem]) -> _winrt.Boolean: ...
    def clear(self) -> None: ...
    def contains_item(self, token: str) -> _winrt.Boolean: ...
    @typing.overload
    def get_file_async(self, token: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]: ...
    @typing.overload
    def get_file_async(self, token: str, options: AccessCacheOptions) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]: ...
    @typing.overload
    def get_folder_async(self, token: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFolder]: ...
    @typing.overload
    def get_folder_async(self, token: str, options: AccessCacheOptions) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFolder]: ...
    @typing.overload
    def get_item_async(self, token: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.IStorageItem]: ...
    @typing.overload
    def get_item_async(self, token: str, options: AccessCacheOptions) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.IStorageItem]: ...
    def remove(self, token: str) -> None: ...

