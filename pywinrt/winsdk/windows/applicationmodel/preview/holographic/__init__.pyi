# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.applicationmodel.activation
except Exception:
    pass

try:
    import winsdk.windows.foundation.numerics
except Exception:
    pass

try:
    import winsdk.windows.perception.spatial
except Exception:
    pass

class HolographicApplicationPreview(_winrt.Object):
    ...
    def is_current_view_presented_on_holographic_display() -> _winrt.Boolean:
        ...
    def is_holographic_activation(activated_event_args: winsdk.windows.applicationmodel.activation.IActivatedEventArgs) -> _winrt.Boolean:
        ...

class HolographicKeyboardPlacementOverridePreview(_winrt.Object):
    ...
    def get_for_current_view() -> HolographicKeyboardPlacementOverridePreview:
        ...
    def reset_placement_override() -> None:
        ...
    def set_placement_override(coordinate_system: winsdk.windows.perception.spatial.SpatialCoordinateSystem, top_center_position: winsdk.windows.foundation.numerics.Vector3, normal: winsdk.windows.foundation.numerics.Vector3) -> None:
        ...
    def set_placement_override(coordinate_system: winsdk.windows.perception.spatial.SpatialCoordinateSystem, top_center_position: winsdk.windows.foundation.numerics.Vector3, normal: winsdk.windows.foundation.numerics.Vector3, max_size: winsdk.windows.foundation.numerics.Vector2) -> None:
        ...
