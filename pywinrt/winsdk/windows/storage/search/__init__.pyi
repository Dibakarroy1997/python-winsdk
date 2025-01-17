# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.data.text
import winsdk.windows.foundation
import winsdk.windows.foundation.collections
import winsdk.windows.storage
import winsdk.windows.storage.fileproperties
import winsdk.windows.storage.streams

class CommonFileQuery(enum.IntEnum):
    DEFAULT_QUERY = 0
    ORDER_BY_NAME = 1
    ORDER_BY_TITLE = 2
    ORDER_BY_MUSIC_PROPERTIES = 3
    ORDER_BY_SEARCH_RANK = 4
    ORDER_BY_DATE = 5

class CommonFolderQuery(enum.IntEnum):
    DEFAULT_QUERY = 0
    GROUP_BY_YEAR = 100
    GROUP_BY_MONTH = 101
    GROUP_BY_ARTIST = 102
    GROUP_BY_ALBUM = 103
    GROUP_BY_ALBUM_ARTIST = 104
    GROUP_BY_COMPOSER = 105
    GROUP_BY_GENRE = 106
    GROUP_BY_PUBLISHED_YEAR = 107
    GROUP_BY_RATING = 108
    GROUP_BY_TAG = 109
    GROUP_BY_AUTHOR = 110
    GROUP_BY_TYPE = 111

class DateStackOption(enum.IntEnum):
    NONE = 0
    YEAR = 1
    MONTH = 2

class FolderDepth(enum.IntEnum):
    SHALLOW = 0
    DEEP = 1

class IndexedState(enum.IntEnum):
    UNKNOWN = 0
    NOT_INDEXED = 1
    PARTIALLY_INDEXED = 2
    FULLY_INDEXED = 3

class IndexerOption(enum.IntEnum):
    USE_INDEXER_WHEN_AVAILABLE = 0
    ONLY_USE_INDEXER = 1
    DO_NOT_USE_INDEXER = 2
    ONLY_USE_INDEXER_AND_OPTIMIZE_FOR_INDEXED_PROPERTIES = 3

Self = typing.TypeVar('Self')

class SortEntry:
    property_name: str
    ascending_order: _winrt.Boolean
    def __init__(self, property_name: str, ascending_order: _winrt.Boolean) -> None: ...

class ContentIndexer(_winrt.Object):
    revision: _winrt.UInt64
    @staticmethod
    def _from(obj: _winrt.Object) -> ContentIndexer: ...
    def add_async(self, indexable_content: typing.Optional[IIndexableContent]) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    @typing.overload
    def create_query(self, search_filter: str, properties_to_retrieve: typing.Iterable[str]) -> typing.Optional[ContentIndexerQuery]: ...
    @typing.overload
    def create_query(self, search_filter: str, properties_to_retrieve: typing.Iterable[str], sort_order: typing.Iterable[SortEntry]) -> typing.Optional[ContentIndexerQuery]: ...
    @typing.overload
    def create_query(self, search_filter: str, properties_to_retrieve: typing.Iterable[str], sort_order: typing.Iterable[SortEntry], search_filter_language: str) -> typing.Optional[ContentIndexerQuery]: ...
    def delete_all_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def delete_async(self, content_id: str) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def delete_multiple_async(self, content_ids: typing.Iterable[str]) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    @typing.overload
    @staticmethod
    def get_indexer() -> typing.Optional[ContentIndexer]: ...
    @typing.overload
    @staticmethod
    def get_indexer(index_name: str) -> typing.Optional[ContentIndexer]: ...
    def retrieve_properties_async(self, content_id: str, properties_to_retrieve: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]]: ...
    def update_async(self, indexable_content: typing.Optional[IIndexableContent]) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...

class ContentIndexerQuery(_winrt.Object):
    query_folder: typing.Optional[winsdk.windows.storage.StorageFolder]
    @staticmethod
    def _from(obj: _winrt.Object) -> ContentIndexerQuery: ...
    @typing.overload
    def get_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[IIndexableContent]]: ...
    @typing.overload
    def get_async(self, start_index: _winrt.UInt32, max_items: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[IIndexableContent]]: ...
    def get_count_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.UInt32]: ...
    @typing.overload
    def get_properties_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]]]: ...
    @typing.overload
    def get_properties_async(self, start_index: _winrt.UInt32, max_items: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]]]: ...

class IndexableContent(_winrt.Object):
    stream_content_type: str
    stream: typing.Optional[winsdk.windows.storage.streams.IRandomAccessStream]
    id: str
    properties: typing.Optional[winsdk.windows.foundation.collections.IMap[str, _winrt.Object]]
    @staticmethod
    def _from(obj: _winrt.Object) -> IndexableContent: ...
    def __init__(self) -> None: ...

class QueryOptions(_winrt.Object):
    user_search_filter: str
    language: str
    indexer_option: IndexerOption
    folder_depth: FolderDepth
    application_search_filter: str
    date_stack_option: DateStackOption
    file_type_filter: typing.Optional[winsdk.windows.foundation.collections.IVector[str]]
    group_property_name: str
    sort_order: typing.Optional[winsdk.windows.foundation.collections.IVector[SortEntry]]
    storage_provider_id_filter: typing.Optional[winsdk.windows.foundation.collections.IVector[str]]
    @staticmethod
    def _from(obj: _winrt.Object) -> QueryOptions: ...
    @typing.overload
    def __init__(self, query: CommonFileQuery, file_type_filter: typing.Iterable[str]) -> None: ...
    @typing.overload
    def __init__(self, query: CommonFolderQuery) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    def load_from_string(self, value: str) -> None: ...
    def save_to_string(self) -> str: ...
    def set_property_prefetch(self, options: winsdk.windows.storage.fileproperties.PropertyPrefetchOptions, properties_to_retrieve: typing.Iterable[str]) -> None: ...
    def set_thumbnail_prefetch(self, mode: winsdk.windows.storage.fileproperties.ThumbnailMode, requested_size: _winrt.UInt32, options: winsdk.windows.storage.fileproperties.ThumbnailOptions) -> None: ...

class SortEntryVector(_winrt.Object, typing.MutableSequence[SortEntry]):
    size: _winrt.UInt32
    def __len__(self) -> int: ...
    @typing.overload
    def __getitem__(self, index: int) -> SortEntry: ...
    @typing.overload
    def __getitem__(self, index: slice) -> typing.MutableSequence[SortEntry]: ...
    def insert(self, index: int, value: SortEntry) -> None: ...
    @typing.overload
    def __delitem__(self, index: int) -> None: ...
    @typing.overload
    def __delitem__(self, index: slice) -> None: ...
    @typing.overload
    def __setitem__(self, index: int, value: SortEntry) -> None: ...
    @typing.overload
    def __setitem__(self, index: slice, value: typing.Iterable[SortEntry]) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> SortEntryVector: ...
    def append(self, value: SortEntry) -> None: ...
    def clear(self) -> None: ...
    def first(self) -> typing.Optional[winsdk.windows.foundation.collections.IIterator[SortEntry]]: ...
    def get_at(self, index: _winrt.UInt32) -> SortEntry: ...
    def get_many(self, start_index: _winrt.UInt32, items_size: _winrt.UInt32) -> typing.Tuple[_winrt.UInt32, typing.List[SortEntry]]: ...
    def get_view(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[SortEntry]]: ...
    def index_of(self, value: SortEntry) -> typing.Tuple[_winrt.Boolean, _winrt.UInt32]: ...
    def insert_at(self, index: _winrt.UInt32, value: SortEntry) -> None: ...
    def remove_at(self, index: _winrt.UInt32) -> None: ...
    def remove_at_end(self) -> None: ...
    def replace_all(self, items: typing.Sequence[SortEntry]) -> None: ...
    def set_at(self, index: _winrt.UInt32, value: SortEntry) -> None: ...

class StorageFileQueryResult(_winrt.Object):
    folder: typing.Optional[winsdk.windows.storage.StorageFolder]
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageFileQueryResult: ...
    def apply_new_query_options(self, new_query_options: typing.Optional[QueryOptions]) -> None: ...
    def find_start_index_async(self, value: typing.Optional[_winrt.Object]) -> winsdk.windows.foundation.IAsyncOperation[_winrt.UInt32]: ...
    def get_current_query_options(self) -> typing.Optional[QueryOptions]: ...
    @typing.overload
    def get_files_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.StorageFile]]: ...
    @typing.overload
    def get_files_async(self, start_index: _winrt.UInt32, max_number_of_items: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.StorageFile]]: ...
    def get_item_count_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.UInt32]: ...
    def get_matching_properties_with_ranges(self, file: typing.Optional[winsdk.windows.storage.StorageFile]) -> typing.Optional[winsdk.windows.foundation.collections.IMap[str, winsdk.windows.foundation.collections.IVectorView[winsdk.windows.data.text.TextSegment]]]: ...
    def add_contents_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[IStorageQueryResultBase, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_contents_changed(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_options_changed(self, changed_handler: winsdk.windows.foundation.TypedEventHandler[IStorageQueryResultBase, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_options_changed(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class StorageFolderQueryResult(_winrt.Object):
    folder: typing.Optional[winsdk.windows.storage.StorageFolder]
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageFolderQueryResult: ...
    def apply_new_query_options(self, new_query_options: typing.Optional[QueryOptions]) -> None: ...
    def find_start_index_async(self, value: typing.Optional[_winrt.Object]) -> winsdk.windows.foundation.IAsyncOperation[_winrt.UInt32]: ...
    def get_current_query_options(self) -> typing.Optional[QueryOptions]: ...
    @typing.overload
    def get_folders_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.StorageFolder]]: ...
    @typing.overload
    def get_folders_async(self, start_index: _winrt.UInt32, max_number_of_items: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.StorageFolder]]: ...
    def get_item_count_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.UInt32]: ...
    def add_contents_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[IStorageQueryResultBase, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_contents_changed(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_options_changed(self, changed_handler: winsdk.windows.foundation.TypedEventHandler[IStorageQueryResultBase, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_options_changed(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class StorageItemQueryResult(_winrt.Object):
    folder: typing.Optional[winsdk.windows.storage.StorageFolder]
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageItemQueryResult: ...
    def apply_new_query_options(self, new_query_options: typing.Optional[QueryOptions]) -> None: ...
    def find_start_index_async(self, value: typing.Optional[_winrt.Object]) -> winsdk.windows.foundation.IAsyncOperation[_winrt.UInt32]: ...
    def get_current_query_options(self) -> typing.Optional[QueryOptions]: ...
    def get_item_count_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.UInt32]: ...
    @typing.overload
    def get_items_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.IStorageItem]]: ...
    @typing.overload
    def get_items_async(self, start_index: _winrt.UInt32, max_number_of_items: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.IStorageItem]]: ...
    def add_contents_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[IStorageQueryResultBase, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_contents_changed(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_options_changed(self, changed_handler: winsdk.windows.foundation.TypedEventHandler[IStorageQueryResultBase, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_options_changed(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class StorageLibraryChangeTrackerTriggerDetails(_winrt.Object):
    change_tracker: typing.Optional[winsdk.windows.storage.StorageLibraryChangeTracker]
    folder: typing.Optional[winsdk.windows.storage.StorageFolder]
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageLibraryChangeTrackerTriggerDetails: ...

class StorageLibraryContentChangedTriggerDetails(_winrt.Object):
    folder: typing.Optional[winsdk.windows.storage.StorageFolder]
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageLibraryContentChangedTriggerDetails: ...
    def create_modified_since_query(self, last_query_time: winsdk.windows.foundation.DateTime) -> typing.Optional[StorageItemQueryResult]: ...

class ValueAndLanguage(_winrt.Object):
    value: typing.Optional[_winrt.Object]
    language: str
    @staticmethod
    def _from(obj: _winrt.Object) -> ValueAndLanguage: ...
    def __init__(self) -> None: ...

class IIndexableContent(_winrt.Object):
    id: str
    properties: typing.Optional[winsdk.windows.foundation.collections.IMap[str, _winrt.Object]]
    stream: typing.Optional[winsdk.windows.storage.streams.IRandomAccessStream]
    stream_content_type: str
    @staticmethod
    def _from(obj: _winrt.Object) -> IIndexableContent: ...

class IStorageFolderQueryOperations(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> IStorageFolderQueryOperations: ...
    def are_query_options_supported(self, query_options: typing.Optional[QueryOptions]) -> _winrt.Boolean: ...
    @typing.overload
    def create_file_query(self) -> typing.Optional[StorageFileQueryResult]: ...
    @typing.overload
    def create_file_query(self, query: CommonFileQuery) -> typing.Optional[StorageFileQueryResult]: ...
    def create_file_query_with_options(self, query_options: typing.Optional[QueryOptions]) -> typing.Optional[StorageFileQueryResult]: ...
    @typing.overload
    def create_folder_query(self) -> typing.Optional[StorageFolderQueryResult]: ...
    @typing.overload
    def create_folder_query(self, query: CommonFolderQuery) -> typing.Optional[StorageFolderQueryResult]: ...
    def create_folder_query_with_options(self, query_options: typing.Optional[QueryOptions]) -> typing.Optional[StorageFolderQueryResult]: ...
    def create_item_query(self) -> typing.Optional[StorageItemQueryResult]: ...
    def create_item_query_with_options(self, query_options: typing.Optional[QueryOptions]) -> typing.Optional[StorageItemQueryResult]: ...
    @typing.overload
    def get_files_async(self, query: CommonFileQuery) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.StorageFile]]: ...
    @typing.overload
    def get_files_async(self, query: CommonFileQuery, start_index: _winrt.UInt32, max_items_to_retrieve: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.StorageFile]]: ...
    @typing.overload
    def get_folders_async(self, query: CommonFolderQuery) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.StorageFolder]]: ...
    @typing.overload
    def get_folders_async(self, query: CommonFolderQuery, start_index: _winrt.UInt32, max_items_to_retrieve: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.StorageFolder]]: ...
    def get_indexed_state_async(self) -> winsdk.windows.foundation.IAsyncOperation[IndexedState]: ...
    def get_items_async(self, start_index: _winrt.UInt32, max_items_to_retrieve: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.IStorageItem]]: ...
    def is_common_file_query_supported(self, query: CommonFileQuery) -> _winrt.Boolean: ...
    def is_common_folder_query_supported(self, query: CommonFolderQuery) -> _winrt.Boolean: ...

class IStorageQueryResultBase(_winrt.Object):
    folder: typing.Optional[winsdk.windows.storage.StorageFolder]
    @staticmethod
    def _from(obj: _winrt.Object) -> IStorageQueryResultBase: ...
    def apply_new_query_options(self, new_query_options: typing.Optional[QueryOptions]) -> None: ...
    def find_start_index_async(self, value: typing.Optional[_winrt.Object]) -> winsdk.windows.foundation.IAsyncOperation[_winrt.UInt32]: ...
    def get_current_query_options(self) -> typing.Optional[QueryOptions]: ...
    def get_item_count_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.UInt32]: ...
    def add_contents_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[IStorageQueryResultBase, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_contents_changed(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_options_changed(self, changed_handler: winsdk.windows.foundation.TypedEventHandler[IStorageQueryResultBase, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_options_changed(self, event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

