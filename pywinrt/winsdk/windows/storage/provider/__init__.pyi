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
import winsdk.windows.storage.streams
import winsdk.windows.ui

class CachedFileOptions(enum.IntFlag):
    NONE = 0
    REQUIRE_UPDATE_ON_ACCESS = 0x1
    USE_CACHED_FILE_WHEN_OFFLINE = 0x2
    DENY_ACCESS_WHEN_OFFLINE = 0x4

class CachedFileTarget(enum.IntEnum):
    LOCAL = 0
    REMOTE = 1

class FileUpdateStatus(enum.IntEnum):
    INCOMPLETE = 0
    COMPLETE = 1
    USER_INPUT_NEEDED = 2
    CURRENTLY_UNAVAILABLE = 3
    FAILED = 4
    COMPLETE_AND_RENAMED = 5

class ReadActivationMode(enum.IntEnum):
    NOT_NEEDED = 0
    BEFORE_ACCESS = 1

class StorageProviderHardlinkPolicy(enum.IntFlag):
    NONE = 0
    ALLOWED = 0x1

class StorageProviderHydrationPolicy(enum.IntEnum):
    PARTIAL = 0
    PROGRESSIVE = 1
    FULL = 2
    ALWAYS_FULL = 3

class StorageProviderHydrationPolicyModifier(enum.IntFlag):
    NONE = 0
    VALIDATION_REQUIRED = 0x1
    STREAMING_ALLOWED = 0x2
    AUTO_DEHYDRATION_ALLOWED = 0x4
    ALLOW_FULL_RESTART_HYDRATION = 0x8

class StorageProviderInSyncPolicy(enum.IntFlag):
    DEFAULT = 0
    FILE_CREATION_TIME = 0x1
    FILE_READ_ONLY_ATTRIBUTE = 0x2
    FILE_HIDDEN_ATTRIBUTE = 0x4
    FILE_SYSTEM_ATTRIBUTE = 0x8
    DIRECTORY_CREATION_TIME = 0x10
    DIRECTORY_READ_ONLY_ATTRIBUTE = 0x20
    DIRECTORY_HIDDEN_ATTRIBUTE = 0x40
    DIRECTORY_SYSTEM_ATTRIBUTE = 0x80
    FILE_LAST_WRITE_TIME = 0x100
    DIRECTORY_LAST_WRITE_TIME = 0x200
    PRESERVE_INSYNC_FOR_SYNC_ENGINE = 0x80000000

class StorageProviderPopulationPolicy(enum.IntEnum):
    FULL = 1
    ALWAYS_FULL = 2

class StorageProviderProtectionMode(enum.IntEnum):
    UNKNOWN = 0
    PERSONAL = 1

class StorageProviderState(enum.IntEnum):
    IN_SYNC = 0
    SYNCING = 1
    PAUSED = 2
    ERROR = 3
    WARNING = 4
    OFFLINE = 5

class StorageProviderUICommandState(enum.IntEnum):
    ENABLED = 0
    DISABLED = 1
    HIDDEN = 2

class StorageProviderUriSourceStatus(enum.IntEnum):
    SUCCESS = 0
    NO_SYNC_ROOT = 1
    FILE_NOT_FOUND = 2

class UIStatus(enum.IntEnum):
    UNAVAILABLE = 0
    HIDDEN = 1
    VISIBLE = 2
    COMPLETE = 3

class WriteActivationMode(enum.IntEnum):
    READ_ONLY = 0
    NOT_NEEDED = 1
    AFTER_WRITE = 2

Self = typing.TypeVar('Self')

class CachedFileUpdater(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> CachedFileUpdater: ...
    @staticmethod
    def set_update_information(file: typing.Optional[winsdk.windows.storage.IStorageFile], content_id: str, read_mode: ReadActivationMode, write_mode: WriteActivationMode, options: CachedFileOptions) -> None: ...

class CachedFileUpdaterUI(_winrt.Object):
    title: str
    u_i_status: UIStatus
    update_target: CachedFileTarget
    update_request: typing.Optional[FileUpdateRequest]
    @staticmethod
    def _from(obj: _winrt.Object) -> CachedFileUpdaterUI: ...
    def get_deferral(self) -> typing.Optional[FileUpdateRequestDeferral]: ...
    def add_file_update_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[CachedFileUpdaterUI, FileUpdateRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_file_update_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_u_i_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[CachedFileUpdaterUI, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_u_i_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class FileUpdateRequest(_winrt.Object):
    status: FileUpdateStatus
    content_id: str
    file: typing.Optional[winsdk.windows.storage.StorageFile]
    user_input_needed_message: str
    @staticmethod
    def _from(obj: _winrt.Object) -> FileUpdateRequest: ...
    def get_deferral(self) -> typing.Optional[FileUpdateRequestDeferral]: ...
    def update_local_file(self, value: typing.Optional[winsdk.windows.storage.IStorageFile]) -> None: ...

class FileUpdateRequestDeferral(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> FileUpdateRequestDeferral: ...
    def complete(self) -> None: ...

class FileUpdateRequestedEventArgs(_winrt.Object):
    request: typing.Optional[FileUpdateRequest]
    @staticmethod
    def _from(obj: _winrt.Object) -> FileUpdateRequestedEventArgs: ...

class StorageProviderFileTypeInfo(_winrt.Object):
    file_extension: str
    icon_resource: str
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageProviderFileTypeInfo: ...
    def __init__(self, file_extension: str, icon_resource: str) -> None: ...

class StorageProviderGetContentInfoForPathResult(_winrt.Object):
    status: StorageProviderUriSourceStatus
    content_uri: str
    content_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageProviderGetContentInfoForPathResult: ...
    def __init__(self) -> None: ...

class StorageProviderGetPathForContentUriResult(_winrt.Object):
    status: StorageProviderUriSourceStatus
    path: str
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageProviderGetPathForContentUriResult: ...
    def __init__(self) -> None: ...

class StorageProviderItemProperties(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageProviderItemProperties: ...
    @staticmethod
    def set_async(item: typing.Optional[winsdk.windows.storage.IStorageItem], item_properties: typing.Iterable[StorageProviderItemProperty]) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...

class StorageProviderItemProperty(_winrt.Object):
    value: str
    id: _winrt.Int32
    icon_resource: str
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageProviderItemProperty: ...
    def __init__(self) -> None: ...

class StorageProviderItemPropertyDefinition(_winrt.Object):
    id: _winrt.Int32
    display_name_resource: str
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageProviderItemPropertyDefinition: ...
    def __init__(self) -> None: ...

class StorageProviderMoreInfoUI(_winrt.Object):
    message: str
    command: typing.Optional[IStorageProviderUICommand]
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageProviderMoreInfoUI: ...
    def __init__(self) -> None: ...

class StorageProviderQuotaUI(_winrt.Object):
    quota_used_label: str
    quota_used_in_bytes: _winrt.UInt64
    quota_used_color: typing.Optional[typing.Optional[winsdk.windows.ui.Color]]
    quota_total_in_bytes: _winrt.UInt64
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageProviderQuotaUI: ...
    def __init__(self) -> None: ...

class StorageProviderStatusUI(_winrt.Object):
    sync_status_command: typing.Optional[IStorageProviderUICommand]
    quota_u_i: typing.Optional[StorageProviderQuotaUI]
    provider_state_label: str
    provider_state_icon: typing.Optional[winsdk.windows.foundation.Uri]
    provider_state: StorageProviderState
    provider_secondary_commands: typing.Optional[winsdk.windows.foundation.collections.IVector[IStorageProviderUICommand]]
    provider_primary_command: typing.Optional[IStorageProviderUICommand]
    more_info_u_i: typing.Optional[StorageProviderMoreInfoUI]
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageProviderStatusUI: ...
    def __init__(self) -> None: ...

class StorageProviderSyncRootInfo(_winrt.Object):
    version: str
    show_siblings_as_group: _winrt.Boolean
    recycle_bin_uri: typing.Optional[winsdk.windows.foundation.Uri]
    protection_mode: StorageProviderProtectionMode
    population_policy: StorageProviderPopulationPolicy
    path: typing.Optional[winsdk.windows.storage.IStorageFolder]
    in_sync_policy: StorageProviderInSyncPolicy
    id: str
    icon_resource: str
    hydration_policy_modifier: StorageProviderHydrationPolicyModifier
    hydration_policy: StorageProviderHydrationPolicy
    hardlink_policy: StorageProviderHardlinkPolicy
    display_name_resource: str
    context: typing.Optional[winsdk.windows.storage.streams.IBuffer]
    allow_pinning: _winrt.Boolean
    storage_provider_item_property_definitions: typing.Optional[winsdk.windows.foundation.collections.IVector[StorageProviderItemPropertyDefinition]]
    provider_id: uuid.UUID
    fallback_file_type_info: typing.Optional[winsdk.windows.foundation.collections.IVector[StorageProviderFileTypeInfo]]
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageProviderSyncRootInfo: ...
    def __init__(self) -> None: ...

class StorageProviderSyncRootManager(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> StorageProviderSyncRootManager: ...
    @staticmethod
    def get_current_sync_roots() -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[StorageProviderSyncRootInfo]]: ...
    @staticmethod
    def get_sync_root_information_for_folder(folder: typing.Optional[winsdk.windows.storage.IStorageFolder]) -> typing.Optional[StorageProviderSyncRootInfo]: ...
    @staticmethod
    def get_sync_root_information_for_id(id: str) -> typing.Optional[StorageProviderSyncRootInfo]: ...
    @staticmethod
    def is_supported() -> _winrt.Boolean: ...
    @staticmethod
    def register(sync_root_information: typing.Optional[StorageProviderSyncRootInfo]) -> None: ...
    @staticmethod
    def unregister(id: str) -> None: ...

class IStorageProviderItemPropertySource(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> IStorageProviderItemPropertySource: ...
    def get_item_properties(self, item_path: str) -> typing.Optional[winsdk.windows.foundation.collections.IIterable[StorageProviderItemProperty]]: ...

class IStorageProviderPropertyCapabilities(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> IStorageProviderPropertyCapabilities: ...
    def is_property_supported(self, property_canonical_name: str) -> _winrt.Boolean: ...

class IStorageProviderStatusUISource(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> IStorageProviderStatusUISource: ...
    def get_status_u_i(self) -> typing.Optional[StorageProviderStatusUI]: ...
    def add_status_u_i_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[IStorageProviderStatusUISource, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_status_u_i_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class IStorageProviderStatusUISourceFactory(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> IStorageProviderStatusUISourceFactory: ...
    def get_status_u_i_source(self, sync_root_id: str) -> typing.Optional[IStorageProviderStatusUISource]: ...

class IStorageProviderUICommand(_winrt.Object):
    description: str
    icon: typing.Optional[winsdk.windows.foundation.Uri]
    label: str
    state: StorageProviderUICommandState
    @staticmethod
    def _from(obj: _winrt.Object) -> IStorageProviderUICommand: ...
    def invoke(self) -> None: ...

class IStorageProviderUriSource(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> IStorageProviderUriSource: ...
    def get_content_info_for_path(self, path: str, result: typing.Optional[StorageProviderGetContentInfoForPathResult]) -> None: ...
    def get_path_for_content_uri(self, content_uri: str, result: typing.Optional[StorageProviderGetPathForContentUriResult]) -> None: ...

