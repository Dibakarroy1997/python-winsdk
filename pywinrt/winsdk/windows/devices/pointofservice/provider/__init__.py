# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Devices.PointOfService.Provider")

try:
    import winsdk.windows.devices.pointofservice
except Exception:
    pass

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.graphics.imaging
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class BarcodeScannerTriggerState(enum.IntEnum):
    RELEASED = 0
    PRESSED = 1

BarcodeScannerDisableScannerRequest = _ns_module.BarcodeScannerDisableScannerRequest
BarcodeScannerDisableScannerRequestEventArgs = _ns_module.BarcodeScannerDisableScannerRequestEventArgs
BarcodeScannerEnableScannerRequest = _ns_module.BarcodeScannerEnableScannerRequest
BarcodeScannerEnableScannerRequestEventArgs = _ns_module.BarcodeScannerEnableScannerRequestEventArgs
BarcodeScannerFrameReader = _ns_module.BarcodeScannerFrameReader
BarcodeScannerFrameReaderFrameArrivedEventArgs = _ns_module.BarcodeScannerFrameReaderFrameArrivedEventArgs
BarcodeScannerGetSymbologyAttributesRequest = _ns_module.BarcodeScannerGetSymbologyAttributesRequest
BarcodeScannerGetSymbologyAttributesRequestEventArgs = _ns_module.BarcodeScannerGetSymbologyAttributesRequestEventArgs
BarcodeScannerHideVideoPreviewRequest = _ns_module.BarcodeScannerHideVideoPreviewRequest
BarcodeScannerHideVideoPreviewRequestEventArgs = _ns_module.BarcodeScannerHideVideoPreviewRequestEventArgs
BarcodeScannerProviderConnection = _ns_module.BarcodeScannerProviderConnection
BarcodeScannerProviderTriggerDetails = _ns_module.BarcodeScannerProviderTriggerDetails
BarcodeScannerSetActiveSymbologiesRequest = _ns_module.BarcodeScannerSetActiveSymbologiesRequest
BarcodeScannerSetActiveSymbologiesRequestEventArgs = _ns_module.BarcodeScannerSetActiveSymbologiesRequestEventArgs
BarcodeScannerSetSymbologyAttributesRequest = _ns_module.BarcodeScannerSetSymbologyAttributesRequest
BarcodeScannerSetSymbologyAttributesRequestEventArgs = _ns_module.BarcodeScannerSetSymbologyAttributesRequestEventArgs
BarcodeScannerStartSoftwareTriggerRequest = _ns_module.BarcodeScannerStartSoftwareTriggerRequest
BarcodeScannerStartSoftwareTriggerRequestEventArgs = _ns_module.BarcodeScannerStartSoftwareTriggerRequestEventArgs
BarcodeScannerStopSoftwareTriggerRequest = _ns_module.BarcodeScannerStopSoftwareTriggerRequest
BarcodeScannerStopSoftwareTriggerRequestEventArgs = _ns_module.BarcodeScannerStopSoftwareTriggerRequestEventArgs
BarcodeScannerVideoFrame = _ns_module.BarcodeScannerVideoFrame
BarcodeSymbologyAttributesBuilder = _ns_module.BarcodeSymbologyAttributesBuilder