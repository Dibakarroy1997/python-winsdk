# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.UI.Input")

try:
    import winsdk.windows.devices.haptics
except Exception:
    pass

try:
    import winsdk.windows.devices.input
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
    import winsdk.windows.storage.streams
except Exception:
    pass

try:
    import winsdk.windows.system
except Exception:
    pass

try:
    import winsdk.windows.ui.core
except Exception:
    pass

class CrossSlidingState(enum.IntEnum):
    STARTED = 0
    DRAGGING = 1
    SELECTING = 2
    SELECT_SPEED_BUMPING = 3
    SPEED_BUMPING = 4
    REARRANGING = 5
    COMPLETED = 6

class DraggingState(enum.IntEnum):
    STARTED = 0
    CONTINUING = 1
    COMPLETED = 2

class EdgeGestureKind(enum.IntEnum):
    TOUCH = 0
    KEYBOARD = 1
    MOUSE = 2

class GazeInputAccessStatus(enum.IntEnum):
    UNSPECIFIED = 0
    ALLOWED = 1
    DENIED_BY_USER = 2
    DENIED_BY_SYSTEM = 3

class GestureSettings(enum.IntFlag):
    NONE = 0
    TAP = 0x1
    DOUBLE_TAP = 0x2
    HOLD = 0x4
    HOLD_WITH_MOUSE = 0x8
    RIGHT_TAP = 0x10
    DRAG = 0x20
    MANIPULATION_TRANSLATE_X = 0x40
    MANIPULATION_TRANSLATE_Y = 0x80
    MANIPULATION_TRANSLATE_RAILS_X = 0x100
    MANIPULATION_TRANSLATE_RAILS_Y = 0x200
    MANIPULATION_ROTATE = 0x400
    MANIPULATION_SCALE = 0x800
    MANIPULATION_TRANSLATE_INERTIA = 0x1000
    MANIPULATION_ROTATE_INERTIA = 0x2000
    MANIPULATION_SCALE_INERTIA = 0x4000
    CROSS_SLIDE = 0x8000
    MANIPULATION_MULTIPLE_FINGER_PANNING = 0x10000

class HoldingState(enum.IntEnum):
    STARTED = 0
    COMPLETED = 1
    CANCELED = 2

class InputActivationState(enum.IntEnum):
    NONE = 0
    DEACTIVATED = 1
    ACTIVATED_NOT_FOREGROUND = 2
    ACTIVATED_IN_FOREGROUND = 3

class PointerUpdateKind(enum.IntEnum):
    OTHER = 0
    LEFT_BUTTON_PRESSED = 1
    LEFT_BUTTON_RELEASED = 2
    RIGHT_BUTTON_PRESSED = 3
    RIGHT_BUTTON_RELEASED = 4
    MIDDLE_BUTTON_PRESSED = 5
    MIDDLE_BUTTON_RELEASED = 6
    X_BUTTON1_PRESSED = 7
    X_BUTTON1_RELEASED = 8
    X_BUTTON2_PRESSED = 9
    X_BUTTON2_RELEASED = 10

class RadialControllerMenuKnownIcon(enum.IntEnum):
    SCROLL = 0
    ZOOM = 1
    UNDO_REDO = 2
    VOLUME = 3
    NEXT_PREVIOUS_TRACK = 4
    RULER = 5
    INK_COLOR = 6
    INK_THICKNESS = 7
    PEN_TYPE = 8

class RadialControllerSystemMenuItemKind(enum.IntEnum):
    SCROLL = 0
    ZOOM = 1
    UNDO_REDO = 2
    VOLUME = 3
    NEXT_PREVIOUS_TRACK = 4

CrossSlideThresholds = _ns_module.CrossSlideThresholds
ManipulationDelta = _ns_module.ManipulationDelta
ManipulationVelocities = _ns_module.ManipulationVelocities
AttachableInputObject = _ns_module.AttachableInputObject
CrossSlidingEventArgs = _ns_module.CrossSlidingEventArgs
DraggingEventArgs = _ns_module.DraggingEventArgs
EdgeGesture = _ns_module.EdgeGesture
EdgeGestureEventArgs = _ns_module.EdgeGestureEventArgs
GestureRecognizer = _ns_module.GestureRecognizer
HoldingEventArgs = _ns_module.HoldingEventArgs
InputActivationListener = _ns_module.InputActivationListener
InputActivationListenerActivationChangedEventArgs = _ns_module.InputActivationListenerActivationChangedEventArgs
KeyboardDeliveryInterceptor = _ns_module.KeyboardDeliveryInterceptor
ManipulationCompletedEventArgs = _ns_module.ManipulationCompletedEventArgs
ManipulationInertiaStartingEventArgs = _ns_module.ManipulationInertiaStartingEventArgs
ManipulationStartedEventArgs = _ns_module.ManipulationStartedEventArgs
ManipulationUpdatedEventArgs = _ns_module.ManipulationUpdatedEventArgs
MouseWheelParameters = _ns_module.MouseWheelParameters
PointerPoint = _ns_module.PointerPoint
PointerPointProperties = _ns_module.PointerPointProperties
PointerVisualizationSettings = _ns_module.PointerVisualizationSettings
RadialController = _ns_module.RadialController
RadialControllerButtonClickedEventArgs = _ns_module.RadialControllerButtonClickedEventArgs
RadialControllerButtonHoldingEventArgs = _ns_module.RadialControllerButtonHoldingEventArgs
RadialControllerButtonPressedEventArgs = _ns_module.RadialControllerButtonPressedEventArgs
RadialControllerButtonReleasedEventArgs = _ns_module.RadialControllerButtonReleasedEventArgs
RadialControllerConfiguration = _ns_module.RadialControllerConfiguration
RadialControllerControlAcquiredEventArgs = _ns_module.RadialControllerControlAcquiredEventArgs
RadialControllerMenu = _ns_module.RadialControllerMenu
RadialControllerMenuItem = _ns_module.RadialControllerMenuItem
RadialControllerRotationChangedEventArgs = _ns_module.RadialControllerRotationChangedEventArgs
RadialControllerScreenContact = _ns_module.RadialControllerScreenContact
RadialControllerScreenContactContinuedEventArgs = _ns_module.RadialControllerScreenContactContinuedEventArgs
RadialControllerScreenContactEndedEventArgs = _ns_module.RadialControllerScreenContactEndedEventArgs
RadialControllerScreenContactStartedEventArgs = _ns_module.RadialControllerScreenContactStartedEventArgs
RightTappedEventArgs = _ns_module.RightTappedEventArgs
SystemButtonEventController = _ns_module.SystemButtonEventController
SystemFunctionButtonEventArgs = _ns_module.SystemFunctionButtonEventArgs
SystemFunctionLockChangedEventArgs = _ns_module.SystemFunctionLockChangedEventArgs
SystemFunctionLockIndicatorChangedEventArgs = _ns_module.SystemFunctionLockIndicatorChangedEventArgs
TappedEventArgs = _ns_module.TappedEventArgs
IPointerPointTransform = _ns_module.IPointerPointTransform