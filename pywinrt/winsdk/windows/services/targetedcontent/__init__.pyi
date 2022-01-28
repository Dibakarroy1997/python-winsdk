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
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class TargetedContentAppInstallationState(enum.IntEnum):
    NOT_APPLICABLE = 0
    NOT_INSTALLED = 1
    INSTALLED = 2

class TargetedContentAvailability(enum.IntEnum):
    NONE = 0
    PARTIAL = 1
    ALL = 2

class TargetedContentInteraction(enum.IntEnum):
    IMPRESSION = 0
    CLICK_THROUGH = 1
    HOVER = 2
    LIKE = 3
    DISLIKE = 4
    DISMISS = 5
    INELIGIBLE = 6
    ACCEPT = 7
    DECLINE = 8
    DEFER = 9
    CANCELED = 10
    CONVERSION = 11
    OPPORTUNITY = 12

class TargetedContentObjectKind(enum.IntEnum):
    COLLECTION = 0
    ITEM = 1
    VALUE = 2

class TargetedContentValueKind(enum.IntEnum):
    STRING = 0
    URI = 1
    NUMBER = 2
    BOOLEAN = 3
    FILE = 4
    IMAGE_FILE = 5
    ACTION = 6
    STRINGS = 7
    URIS = 8
    NUMBERS = 9
    BOOLEANS = 10
    FILES = 11
    IMAGE_FILES = 12
    ACTIONS = 13

class TargetedContentAction(_winrt.Object):
    ...
    def invoke_async() -> winsdk.windows.foundation.IAsyncAction:
        ...

class TargetedContentAvailabilityChangedEventArgs(_winrt.Object):
    ...
    def get_deferral() -> winsdk.windows.foundation.Deferral:
        ...

class TargetedContentChangedEventArgs(_winrt.Object):
    ...
    has_previous_content_expired: _winrt.Boolean
    def get_deferral() -> winsdk.windows.foundation.Deferral:
        ...

class TargetedContentCollection(_winrt.Object):
    ...
    collections: winsdk.windows.foundation.collections.IVectorView[TargetedContentCollection]
    id: str
    items: winsdk.windows.foundation.collections.IVectorView[TargetedContentItem]
    path: str
    properties: winsdk.windows.foundation.collections.IMapView[str, TargetedContentValue]
    def report_custom_interaction(custom_interaction_name: str) -> None:
        ...
    def report_interaction(interaction: TargetedContentInteraction) -> None:
        ...

class TargetedContentContainer(_winrt.Object):
    ...
    availability: TargetedContentAvailability
    content: TargetedContentCollection
    id: str
    timestamp: winsdk.windows.foundation.DateTime
    def get_async(content_id: str) -> winsdk.windows.foundation.IAsyncOperation[TargetedContentContainer]:
        ...
    def select_single_object(path: str) -> TargetedContentObject:
        ...

class TargetedContentFile(winsdk.windows.storage.streams.IRandomAccessStreamReference, _winrt.Object):
    ...
    def open_read_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IRandomAccessStreamWithContentType]:
        ...

class TargetedContentImage(winsdk.windows.storage.streams.IRandomAccessStreamReference, _winrt.Object):
    ...
    height: _winrt.UInt32
    width: _winrt.UInt32
    def open_read_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IRandomAccessStreamWithContentType]:
        ...

class TargetedContentItem(_winrt.Object):
    ...
    collections: winsdk.windows.foundation.collections.IVectorView[TargetedContentCollection]
    path: str
    properties: winsdk.windows.foundation.collections.IMapView[str, TargetedContentValue]
    state: TargetedContentItemState
    def report_custom_interaction(custom_interaction_name: str) -> None:
        ...
    def report_interaction(interaction: TargetedContentInteraction) -> None:
        ...

class TargetedContentItemState(_winrt.Object):
    ...
    app_installation_state: TargetedContentAppInstallationState
    should_display: _winrt.Boolean

class TargetedContentObject(_winrt.Object):
    ...
    collection: TargetedContentCollection
    item: TargetedContentItem
    object_kind: TargetedContentObjectKind
    value: TargetedContentValue

class TargetedContentStateChangedEventArgs(_winrt.Object):
    ...
    def get_deferral() -> winsdk.windows.foundation.Deferral:
        ...

class TargetedContentSubscription(_winrt.Object):
    ...
    id: str
    def get_async(subscription_id: str) -> winsdk.windows.foundation.IAsyncOperation[TargetedContentSubscription]:
        ...
    def get_content_container_async() -> winsdk.windows.foundation.IAsyncOperation[TargetedContentContainer]:
        ...
    def get_options(subscription_id: str) -> TargetedContentSubscriptionOptions:
        ...
    def add_availability_changed(handler: winsdk.windows.foundation.TypedEventHandler[TargetedContentSubscription, TargetedContentAvailabilityChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_availability_changed(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_content_changed(handler: winsdk.windows.foundation.TypedEventHandler[TargetedContentSubscription, TargetedContentChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_content_changed(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_state_changed(handler: winsdk.windows.foundation.TypedEventHandler[TargetedContentSubscription, TargetedContentStateChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_state_changed(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class TargetedContentSubscriptionOptions(_winrt.Object):
    ...
    allow_partial_content_availability: _winrt.Boolean
    cloud_query_parameters: winsdk.windows.foundation.collections.IMap[str, str]
    local_filters: winsdk.windows.foundation.collections.IVector[str]
    subscription_id: str
    def update() -> None:
        ...

class TargetedContentValue(_winrt.Object):
    ...
    action: TargetedContentAction
    actions: winsdk.windows.foundation.collections.IVectorView[TargetedContentAction]
    boolean: _winrt.Boolean
    booleans: winsdk.windows.foundation.collections.IVectorView[_winrt.Boolean]
    file: TargetedContentFile
    files: winsdk.windows.foundation.collections.IVectorView[TargetedContentFile]
    image_file: TargetedContentImage
    image_files: winsdk.windows.foundation.collections.IVectorView[TargetedContentImage]
    number: _winrt.Double
    numbers: winsdk.windows.foundation.collections.IVectorView[_winrt.Double]
    path: str
    string: str
    strings: winsdk.windows.foundation.collections.IVectorView[str]
    uri: winsdk.windows.foundation.Uri
    uris: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.Uri]
    value_kind: TargetedContentValueKind
