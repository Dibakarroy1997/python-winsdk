# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

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
    import winsdk.windows.globalization
except Exception:
    pass

try:
    import winsdk.windows.graphics.imaging
except Exception:
    pass

class OcrEngine(_winrt.Object):
    ...
    recognizer_language: winsdk.windows.globalization.Language
    available_recognizer_languages: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.globalization.Language]
    max_image_dimension: _winrt.UInt32
    def is_language_supported(language: winsdk.windows.globalization.Language) -> _winrt.Boolean:
        ...
    def recognize_async(bitmap: winsdk.windows.graphics.imaging.SoftwareBitmap) -> winsdk.windows.foundation.IAsyncOperation[OcrResult]:
        ...
    def try_create_from_language(language: winsdk.windows.globalization.Language) -> OcrEngine:
        ...
    def try_create_from_user_profile_languages() -> OcrEngine:
        ...

class OcrLine(_winrt.Object):
    ...
    text: str
    words: winsdk.windows.foundation.collections.IVectorView[OcrWord]

class OcrResult(_winrt.Object):
    ...
    lines: winsdk.windows.foundation.collections.IVectorView[OcrLine]
    text: str
    text_angle: typing.Optional[_winrt.Double]

class OcrWord(_winrt.Object):
    ...
    bounding_rect: winsdk.windows.foundation.Rect
    text: str
