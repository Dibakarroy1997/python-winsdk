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

try:
    import winsdk.windows.web.http
except Exception:
    pass

class AdaptiveMediaSourceCreationStatus(enum.IntEnum):
    SUCCESS = 0
    MANIFEST_DOWNLOAD_FAILURE = 1
    MANIFEST_PARSE_FAILURE = 2
    UNSUPPORTED_MANIFEST_CONTENT_TYPE = 3
    UNSUPPORTED_MANIFEST_VERSION = 4
    UNSUPPORTED_MANIFEST_PROFILE = 5
    UNKNOWN_FAILURE = 6

class AdaptiveMediaSourceDiagnosticType(enum.IntEnum):
    MANIFEST_UNCHANGED_UPON_RELOAD = 0
    MANIFEST_MISMATCH_UPON_RELOAD = 1
    MANIFEST_SIGNALED_END_OF_LIVE_EVENT_UPON_RELOAD = 2
    MEDIA_SEGMENT_SKIPPED = 3
    RESOURCE_NOT_FOUND = 4
    RESOURCE_TIMED_OUT = 5
    RESOURCE_PARSING_ERROR = 6
    BITRATE_DISABLED = 7
    FATAL_MEDIA_SOURCE_ERROR = 8

class AdaptiveMediaSourceDownloadBitrateChangedReason(enum.IntEnum):
    SUFFICIENT_INBOUND_BITS_PER_SECOND = 0
    INSUFFICIENT_INBOUND_BITS_PER_SECOND = 1
    LOW_BUFFER_LEVEL = 2
    POSITION_CHANGED = 3
    TRACK_SELECTION_CHANGED = 4
    DESIRED_BITRATES_CHANGED = 5
    ERROR_IN_PREVIOUS_BITRATE = 6

class AdaptiveMediaSourceResourceType(enum.IntEnum):
    MANIFEST = 0
    INITIALIZATION_SEGMENT = 1
    MEDIA_SEGMENT = 2
    KEY = 3
    INITIALIZATION_VECTOR = 4
    MEDIA_SEGMENT_INDEX = 5

class AdaptiveMediaSource(winsdk.windows.media.core.IMediaSource, winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    initial_bitrate: _winrt.UInt32
    inbound_bits_per_second_window: winsdk.windows.foundation.TimeSpan
    desired_max_bitrate: typing.Optional[_winrt.UInt32]
    desired_live_offset: winsdk.windows.foundation.TimeSpan
    desired_min_bitrate: typing.Optional[_winrt.UInt32]
    current_playback_bitrate: _winrt.UInt32
    audio_only_playback: _winrt.Boolean
    inbound_bits_per_second: _winrt.UInt64
    available_bitrates: winsdk.windows.foundation.collections.IVectorView[_winrt.UInt32]
    current_download_bitrate: _winrt.UInt32
    is_live: _winrt.Boolean
    advanced_settings: AdaptiveMediaSourceAdvancedSettings
    desired_seekable_window_size: typing.Optional[winsdk.windows.foundation.TimeSpan]
    diagnostics: AdaptiveMediaSourceDiagnostics
    max_seekable_window_size: typing.Optional[winsdk.windows.foundation.TimeSpan]
    min_live_offset: typing.Optional[winsdk.windows.foundation.TimeSpan]
    def close() -> None:
        ...
    def create_from_stream_async(stream: winsdk.windows.storage.streams.IInputStream, uri: winsdk.windows.foundation.Uri, content_type: str) -> winsdk.windows.foundation.IAsyncOperation[AdaptiveMediaSourceCreationResult]:
        ...
    def create_from_stream_async(stream: winsdk.windows.storage.streams.IInputStream, uri: winsdk.windows.foundation.Uri, content_type: str, http_client: winsdk.windows.web.http.HttpClient) -> winsdk.windows.foundation.IAsyncOperation[AdaptiveMediaSourceCreationResult]:
        ...
    def create_from_uri_async(uri: winsdk.windows.foundation.Uri) -> winsdk.windows.foundation.IAsyncOperation[AdaptiveMediaSourceCreationResult]:
        ...
    def create_from_uri_async(uri: winsdk.windows.foundation.Uri, http_client: winsdk.windows.web.http.HttpClient) -> winsdk.windows.foundation.IAsyncOperation[AdaptiveMediaSourceCreationResult]:
        ...
    def get_correlated_times() -> AdaptiveMediaSourceCorrelatedTimes:
        ...
    def is_content_type_supported(content_type: str) -> _winrt.Boolean:
        ...
    def add_download_bitrate_changed(handler: winsdk.windows.foundation.TypedEventHandler[AdaptiveMediaSource, AdaptiveMediaSourceDownloadBitrateChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_download_bitrate_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_download_completed(handler: winsdk.windows.foundation.TypedEventHandler[AdaptiveMediaSource, AdaptiveMediaSourceDownloadCompletedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_download_completed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_download_failed(handler: winsdk.windows.foundation.TypedEventHandler[AdaptiveMediaSource, AdaptiveMediaSourceDownloadFailedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_download_failed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_download_requested(handler: winsdk.windows.foundation.TypedEventHandler[AdaptiveMediaSource, AdaptiveMediaSourceDownloadRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_download_requested(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_playback_bitrate_changed(handler: winsdk.windows.foundation.TypedEventHandler[AdaptiveMediaSource, AdaptiveMediaSourcePlaybackBitrateChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_playback_bitrate_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class AdaptiveMediaSourceAdvancedSettings(_winrt.Object):
    ...
    desired_bitrate_headroom_ratio: typing.Optional[_winrt.Double]
    bitrate_downgrade_trigger_ratio: typing.Optional[_winrt.Double]
    all_segments_independent: _winrt.Boolean

class AdaptiveMediaSourceCorrelatedTimes(_winrt.Object):
    ...
    position: typing.Optional[winsdk.windows.foundation.TimeSpan]
    presentation_time_stamp: typing.Optional[winsdk.windows.foundation.TimeSpan]
    program_date_time: typing.Optional[winsdk.windows.foundation.DateTime]

class AdaptiveMediaSourceCreationResult(_winrt.Object):
    ...
    http_response_message: winsdk.windows.web.http.HttpResponseMessage
    media_source: AdaptiveMediaSource
    status: AdaptiveMediaSourceCreationStatus
    extended_error: winsdk.windows.foundation.HResult

class AdaptiveMediaSourceDiagnosticAvailableEventArgs(_winrt.Object):
    ...
    bitrate: typing.Optional[_winrt.UInt32]
    diagnostic_type: AdaptiveMediaSourceDiagnosticType
    position: typing.Optional[winsdk.windows.foundation.TimeSpan]
    request_id: typing.Optional[_winrt.Int32]
    resource_byte_range_length: typing.Optional[_winrt.UInt64]
    resource_byte_range_offset: typing.Optional[_winrt.UInt64]
    resource_type: typing.Optional[AdaptiveMediaSourceResourceType]
    resource_uri: winsdk.windows.foundation.Uri
    segment_id: typing.Optional[_winrt.UInt64]
    extended_error: winsdk.windows.foundation.HResult
    resource_content_type: str
    resource_duration: typing.Optional[winsdk.windows.foundation.TimeSpan]

class AdaptiveMediaSourceDiagnostics(_winrt.Object):
    ...
    def add_diagnostic_available(handler: winsdk.windows.foundation.TypedEventHandler[AdaptiveMediaSourceDiagnostics, AdaptiveMediaSourceDiagnosticAvailableEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_diagnostic_available(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class AdaptiveMediaSourceDownloadBitrateChangedEventArgs(_winrt.Object):
    ...
    new_value: _winrt.UInt32
    old_value: _winrt.UInt32
    reason: AdaptiveMediaSourceDownloadBitrateChangedReason

class AdaptiveMediaSourceDownloadCompletedEventArgs(_winrt.Object):
    ...
    http_response_message: winsdk.windows.web.http.HttpResponseMessage
    resource_byte_range_length: typing.Optional[_winrt.UInt64]
    resource_byte_range_offset: typing.Optional[_winrt.UInt64]
    resource_type: AdaptiveMediaSourceResourceType
    resource_uri: winsdk.windows.foundation.Uri
    position: typing.Optional[winsdk.windows.foundation.TimeSpan]
    request_id: _winrt.Int32
    statistics: AdaptiveMediaSourceDownloadStatistics
    resource_content_type: str
    resource_duration: typing.Optional[winsdk.windows.foundation.TimeSpan]

class AdaptiveMediaSourceDownloadFailedEventArgs(_winrt.Object):
    ...
    http_response_message: winsdk.windows.web.http.HttpResponseMessage
    resource_byte_range_length: typing.Optional[_winrt.UInt64]
    resource_byte_range_offset: typing.Optional[_winrt.UInt64]
    resource_type: AdaptiveMediaSourceResourceType
    resource_uri: winsdk.windows.foundation.Uri
    extended_error: winsdk.windows.foundation.HResult
    position: typing.Optional[winsdk.windows.foundation.TimeSpan]
    request_id: _winrt.Int32
    statistics: AdaptiveMediaSourceDownloadStatistics
    resource_content_type: str
    resource_duration: typing.Optional[winsdk.windows.foundation.TimeSpan]

class AdaptiveMediaSourceDownloadRequestedDeferral(_winrt.Object):
    ...
    def complete() -> None:
        ...

class AdaptiveMediaSourceDownloadRequestedEventArgs(_winrt.Object):
    ...
    resource_byte_range_length: typing.Optional[_winrt.UInt64]
    resource_byte_range_offset: typing.Optional[_winrt.UInt64]
    resource_type: AdaptiveMediaSourceResourceType
    resource_uri: winsdk.windows.foundation.Uri
    result: AdaptiveMediaSourceDownloadResult
    position: typing.Optional[winsdk.windows.foundation.TimeSpan]
    request_id: _winrt.Int32
    resource_content_type: str
    resource_duration: typing.Optional[winsdk.windows.foundation.TimeSpan]
    def get_deferral() -> AdaptiveMediaSourceDownloadRequestedDeferral:
        ...

class AdaptiveMediaSourceDownloadResult(_winrt.Object):
    ...
    resource_uri: winsdk.windows.foundation.Uri
    input_stream: winsdk.windows.storage.streams.IInputStream
    extended_status: _winrt.UInt32
    content_type: str
    buffer: winsdk.windows.storage.streams.IBuffer
    resource_byte_range_offset: typing.Optional[_winrt.UInt64]
    resource_byte_range_length: typing.Optional[_winrt.UInt64]

class AdaptiveMediaSourceDownloadStatistics(_winrt.Object):
    ...
    content_bytes_received_count: _winrt.UInt64
    time_to_first_byte_received: typing.Optional[winsdk.windows.foundation.TimeSpan]
    time_to_headers_received: typing.Optional[winsdk.windows.foundation.TimeSpan]
    time_to_last_byte_received: typing.Optional[winsdk.windows.foundation.TimeSpan]

class AdaptiveMediaSourcePlaybackBitrateChangedEventArgs(_winrt.Object):
    ...
    audio_only: _winrt.Boolean
    new_value: _winrt.UInt32
    old_value: _winrt.UInt32
