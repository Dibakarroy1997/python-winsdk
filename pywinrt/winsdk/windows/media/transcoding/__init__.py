# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Media.Transcoding")

try:
    import winsdk.windows.foundation
except ImportError:
    pass

try:
    import winsdk.windows.foundation.collections
except ImportError:
    pass

try:
    import winsdk.windows.media.core
except ImportError:
    pass

try:
    import winsdk.windows.media.mediaproperties
except ImportError:
    pass

try:
    import winsdk.windows.storage
except ImportError:
    pass

try:
    import winsdk.windows.storage.streams
except ImportError:
    pass

class MediaVideoProcessingAlgorithm(enum.IntEnum):
    DEFAULT = 0
    MRF_CRF444 = 1

class TranscodeFailureReason(enum.IntEnum):
    NONE = 0
    UNKNOWN = 1
    INVALID_PROFILE = 2
    CODEC_NOT_FOUND = 3

_ns_module._register_MediaVideoProcessingAlgorithm(MediaVideoProcessingAlgorithm)
_ns_module._register_TranscodeFailureReason(TranscodeFailureReason)

MediaTranscoder = _ns_module.MediaTranscoder
PrepareTranscodeResult = _ns_module.PrepareTranscodeResult
