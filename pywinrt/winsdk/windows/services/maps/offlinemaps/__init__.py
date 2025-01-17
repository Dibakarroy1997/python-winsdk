# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Services.Maps.OfflineMaps")

try:
    import winsdk.windows.devices.geolocation
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

class OfflineMapPackageQueryStatus(enum.IntEnum):
    SUCCESS = 0
    UNKNOWN_ERROR = 1
    INVALID_CREDENTIALS = 2
    NETWORK_FAILURE = 3

class OfflineMapPackageStartDownloadStatus(enum.IntEnum):
    SUCCESS = 0
    UNKNOWN_ERROR = 1
    INVALID_CREDENTIALS = 2
    DENIED_WITHOUT_CAPABILITY = 3

class OfflineMapPackageStatus(enum.IntEnum):
    NOT_DOWNLOADED = 0
    DOWNLOADING = 1
    DOWNLOADED = 2
    DELETING = 3

_ns_module._register_OfflineMapPackageQueryStatus(OfflineMapPackageQueryStatus)
_ns_module._register_OfflineMapPackageStartDownloadStatus(OfflineMapPackageStartDownloadStatus)
_ns_module._register_OfflineMapPackageStatus(OfflineMapPackageStatus)

OfflineMapPackage = _ns_module.OfflineMapPackage
OfflineMapPackageQueryResult = _ns_module.OfflineMapPackageQueryResult
OfflineMapPackageStartDownloadResult = _ns_module.OfflineMapPackageStartDownloadResult
