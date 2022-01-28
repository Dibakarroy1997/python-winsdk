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

class WebErrorStatus(enum.IntEnum):
    UNKNOWN = 0
    CERTIFICATE_COMMON_NAME_IS_INCORRECT = 1
    CERTIFICATE_EXPIRED = 2
    CERTIFICATE_CONTAINS_ERRORS = 3
    CERTIFICATE_REVOKED = 4
    CERTIFICATE_IS_INVALID = 5
    SERVER_UNREACHABLE = 6
    TIMEOUT = 7
    ERROR_HTTP_INVALID_SERVER_RESPONSE = 8
    CONNECTION_ABORTED = 9
    CONNECTION_RESET = 10
    DISCONNECTED = 11
    HTTP_TO_HTTPS_ON_REDIRECTION = 12
    HTTPS_TO_HTTP_ON_REDIRECTION = 13
    CANNOT_CONNECT = 14
    HOST_NAME_NOT_RESOLVED = 15
    OPERATION_CANCELED = 16
    REDIRECT_FAILED = 17
    UNEXPECTED_STATUS_CODE = 18
    UNEXPECTED_REDIRECTION = 19
    UNEXPECTED_CLIENT_ERROR = 20
    UNEXPECTED_SERVER_ERROR = 21
    INSUFFICIENT_RANGE_SUPPORT = 22
    MISSING_CONTENT_LENGTH_SUPPORT = 23
    MULTIPLE_CHOICES = 300
    MOVED_PERMANENTLY = 301
    FOUND = 302
    SEE_OTHER = 303
    NOT_MODIFIED = 304
    USE_PROXY = 305
    TEMPORARY_REDIRECT = 307
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    PROXY_AUTHENTICATION_REQUIRED = 407
    REQUEST_TIMEOUT = 408
    CONFLICT = 409
    GONE = 410
    LENGTH_REQUIRED = 411
    PRECONDITION_FAILED = 412
    REQUEST_ENTITY_TOO_LARGE = 413
    REQUEST_URI_TOO_LONG = 414
    UNSUPPORTED_MEDIA_TYPE = 415
    REQUESTED_RANGE_NOT_SATISFIABLE = 416
    EXPECTATION_FAILED = 417
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504
    HTTP_VERSION_NOT_SUPPORTED = 505

class WebError(_winrt.Object):
    ...
    def get_status(hresult: _winrt.Int32) -> WebErrorStatus:
        ...

class IUriToStreamResolver(_winrt.Object):
    ...
    def uri_to_stream_async(uri: winsdk.windows.foundation.Uri) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IInputStream]:
        ...
