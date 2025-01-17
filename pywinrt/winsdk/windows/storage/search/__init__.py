# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Storage.Search")

try:
    import winsdk.windows.data.text
except ImportError:
    pass

try:
    import winsdk.windows.foundation
except ImportError:
    pass

try:
    import winsdk.windows.foundation.collections
except ImportError:
    pass

try:
    import winsdk.windows.storage
except ImportError:
    pass

try:
    import winsdk.windows.storage.fileproperties
except ImportError:
    pass

try:
    import winsdk.windows.storage.streams
except ImportError:
    pass

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

_ns_module._register_CommonFileQuery(CommonFileQuery)
_ns_module._register_CommonFolderQuery(CommonFolderQuery)
_ns_module._register_DateStackOption(DateStackOption)
_ns_module._register_FolderDepth(FolderDepth)
_ns_module._register_IndexedState(IndexedState)
_ns_module._register_IndexerOption(IndexerOption)

SortEntry = _ns_module.SortEntry
ContentIndexer = _ns_module.ContentIndexer
ContentIndexerQuery = _ns_module.ContentIndexerQuery
IndexableContent = _ns_module.IndexableContent
QueryOptions = _ns_module.QueryOptions
SortEntryVector = _ns_module.SortEntryVector
StorageFileQueryResult = _ns_module.StorageFileQueryResult
StorageFolderQueryResult = _ns_module.StorageFolderQueryResult
StorageItemQueryResult = _ns_module.StorageItemQueryResult
StorageLibraryChangeTrackerTriggerDetails = _ns_module.StorageLibraryChangeTrackerTriggerDetails
StorageLibraryContentChangedTriggerDetails = _ns_module.StorageLibraryContentChangedTriggerDetails
ValueAndLanguage = _ns_module.ValueAndLanguage
IIndexableContent = _ns_module.IIndexableContent
IStorageFolderQueryOperations = _ns_module.IStorageFolderQueryOperations
IStorageQueryResultBase = _ns_module.IStorageQueryResultBase
