# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

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

class CrossSlideThresholds:
    selection_start: _winrt.Single
    speed_bump_start: _winrt.Single
    speed_bump_end: _winrt.Single
    rearrange_start: _winrt.Single
    def __init__(self, selection_start: _winrt.Single, speed_bump_start: _winrt.Single, speed_bump_end: _winrt.Single, rearrange_start: _winrt.Single) -> None: ...

class ManipulationDelta:
    translation: winsdk.windows.foundation.Point
    scale: _winrt.Single
    rotation: _winrt.Single
    expansion: _winrt.Single
    def __init__(self, translation: winsdk.windows.foundation.Point, scale: _winrt.Single, rotation: _winrt.Single, expansion: _winrt.Single) -> None: ...

class ManipulationVelocities:
    linear: winsdk.windows.foundation.Point
    angular: _winrt.Single
    expansion: _winrt.Single
    def __init__(self, linear: winsdk.windows.foundation.Point, angular: _winrt.Single, expansion: _winrt.Single) -> None: ...

class AttachableInputObject(winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    def close() -> None:
        ...

class CrossSlidingEventArgs(_winrt.Object):
    ...
    cross_sliding_state: CrossSlidingState
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    contact_count: _winrt.UInt32

class DraggingEventArgs(_winrt.Object):
    ...
    dragging_state: DraggingState
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    contact_count: _winrt.UInt32

class EdgeGesture(_winrt.Object):
    ...
    def get_for_current_view() -> EdgeGesture:
        ...
    def add_canceled(handler: winsdk.windows.foundation.TypedEventHandler[EdgeGesture, EdgeGestureEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_canceled(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_completed(handler: winsdk.windows.foundation.TypedEventHandler[EdgeGesture, EdgeGestureEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_completed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_starting(handler: winsdk.windows.foundation.TypedEventHandler[EdgeGesture, EdgeGestureEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_starting(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class EdgeGestureEventArgs(_winrt.Object):
    ...
    kind: EdgeGestureKind

class GestureRecognizer(_winrt.Object):
    ...
    show_gesture_feedback: _winrt.Boolean
    pivot_radius: _winrt.Single
    pivot_center: winsdk.windows.foundation.Point
    manipulation_exact: _winrt.Boolean
    inertia_translation_displacement: _winrt.Single
    inertia_translation_deceleration: _winrt.Single
    inertia_rotation_deceleration: _winrt.Single
    inertia_rotation_angle: _winrt.Single
    inertia_expansion_deceleration: _winrt.Single
    inertia_expansion: _winrt.Single
    gesture_settings: GestureSettings
    cross_slide_thresholds: CrossSlideThresholds
    cross_slide_horizontally: _winrt.Boolean
    cross_slide_exact: _winrt.Boolean
    auto_process_inertia: _winrt.Boolean
    is_active: _winrt.Boolean
    is_inertial: _winrt.Boolean
    mouse_wheel_parameters: MouseWheelParameters
    translation_min_contact_count: _winrt.UInt32
    translation_max_contact_count: _winrt.UInt32
    tap_min_contact_count: _winrt.UInt32
    tap_max_contact_count: _winrt.UInt32
    hold_start_delay: winsdk.windows.foundation.TimeSpan
    hold_radius: _winrt.Single
    hold_min_contact_count: _winrt.UInt32
    hold_max_contact_count: _winrt.UInt32
    def __init__(self, ) -> None:
        ...
    def can_be_double_tap(value: PointerPoint) -> _winrt.Boolean:
        ...
    def complete_gesture() -> None:
        ...
    def process_down_event(value: PointerPoint) -> None:
        ...
    def process_inertia() -> None:
        ...
    def process_mouse_wheel_event(value: PointerPoint, is_shift_key_down: _winrt.Boolean, is_control_key_down: _winrt.Boolean) -> None:
        ...
    def process_move_events(value: winsdk.windows.foundation.collections.IVector[PointerPoint]) -> None:
        ...
    def process_up_event(value: PointerPoint) -> None:
        ...
    def add_cross_sliding(handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, CrossSlidingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_cross_sliding(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_dragging(handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, DraggingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_dragging(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_holding(handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, HoldingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_holding(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_manipulation_completed(handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, ManipulationCompletedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_manipulation_completed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_manipulation_inertia_starting(handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, ManipulationInertiaStartingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_manipulation_inertia_starting(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_manipulation_started(handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, ManipulationStartedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_manipulation_started(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_manipulation_updated(handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, ManipulationUpdatedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_manipulation_updated(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_right_tapped(handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, RightTappedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_right_tapped(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_tapped(handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, TappedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_tapped(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class HoldingEventArgs(_winrt.Object):
    ...
    holding_state: HoldingState
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    contact_count: _winrt.UInt32
    current_contact_count: _winrt.UInt32

class InputActivationListener(_winrt.Object):
    ...
    state: InputActivationState
    def add_input_activation_changed(handler: winsdk.windows.foundation.TypedEventHandler[InputActivationListener, InputActivationListenerActivationChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_input_activation_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class InputActivationListenerActivationChangedEventArgs(_winrt.Object):
    ...
    state: InputActivationState

class KeyboardDeliveryInterceptor(_winrt.Object):
    ...
    is_interception_enabled_when_in_foreground: _winrt.Boolean
    def get_for_current_view() -> KeyboardDeliveryInterceptor:
        ...
    def add_key_down(handler: winsdk.windows.foundation.TypedEventHandler[KeyboardDeliveryInterceptor, winsdk.windows.ui.core.KeyEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_key_down(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_key_up(handler: winsdk.windows.foundation.TypedEventHandler[KeyboardDeliveryInterceptor, winsdk.windows.ui.core.KeyEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_key_up(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class ManipulationCompletedEventArgs(_winrt.Object):
    ...
    cumulative: ManipulationDelta
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    velocities: ManipulationVelocities
    contact_count: _winrt.UInt32
    current_contact_count: _winrt.UInt32

class ManipulationInertiaStartingEventArgs(_winrt.Object):
    ...
    cumulative: ManipulationDelta
    delta: ManipulationDelta
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    velocities: ManipulationVelocities
    contact_count: _winrt.UInt32

class ManipulationStartedEventArgs(_winrt.Object):
    ...
    cumulative: ManipulationDelta
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    contact_count: _winrt.UInt32

class ManipulationUpdatedEventArgs(_winrt.Object):
    ...
    cumulative: ManipulationDelta
    delta: ManipulationDelta
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    velocities: ManipulationVelocities
    contact_count: _winrt.UInt32
    current_contact_count: _winrt.UInt32

class MouseWheelParameters(_winrt.Object):
    ...
    page_translation: winsdk.windows.foundation.Point
    delta_scale: _winrt.Single
    delta_rotation_angle: _winrt.Single
    char_translation: winsdk.windows.foundation.Point

class PointerPoint(_winrt.Object):
    ...
    frame_id: _winrt.UInt32
    is_in_contact: _winrt.Boolean
    pointer_device: winsdk.windows.devices.input.PointerDevice
    pointer_id: _winrt.UInt32
    position: winsdk.windows.foundation.Point
    properties: PointerPointProperties
    raw_position: winsdk.windows.foundation.Point
    timestamp: _winrt.UInt64
    def get_current_point(pointer_id: _winrt.UInt32) -> PointerPoint:
        ...
    def get_current_point(pointer_id: _winrt.UInt32, transform: IPointerPointTransform) -> PointerPoint:
        ...
    def get_intermediate_points(pointer_id: _winrt.UInt32) -> winsdk.windows.foundation.collections.IVector[PointerPoint]:
        ...
    def get_intermediate_points(pointer_id: _winrt.UInt32, transform: IPointerPointTransform) -> winsdk.windows.foundation.collections.IVector[PointerPoint]:
        ...

class PointerPointProperties(_winrt.Object):
    ...
    contact_rect: winsdk.windows.foundation.Rect
    contact_rect_raw: winsdk.windows.foundation.Rect
    is_barrel_button_pressed: _winrt.Boolean
    is_canceled: _winrt.Boolean
    is_eraser: _winrt.Boolean
    is_horizontal_mouse_wheel: _winrt.Boolean
    is_in_range: _winrt.Boolean
    is_inverted: _winrt.Boolean
    is_left_button_pressed: _winrt.Boolean
    is_middle_button_pressed: _winrt.Boolean
    is_primary: _winrt.Boolean
    is_right_button_pressed: _winrt.Boolean
    is_x_button1_pressed: _winrt.Boolean
    is_x_button2_pressed: _winrt.Boolean
    mouse_wheel_delta: _winrt.Int32
    orientation: _winrt.Single
    pointer_update_kind: PointerUpdateKind
    pressure: _winrt.Single
    touch_confidence: _winrt.Boolean
    twist: _winrt.Single
    x_tilt: _winrt.Single
    y_tilt: _winrt.Single
    z_distance: typing.Optional[_winrt.Single]
    def get_usage_value(usage_page: _winrt.UInt32, usage_id: _winrt.UInt32) -> _winrt.Int32:
        ...
    def has_usage(usage_page: _winrt.UInt32, usage_id: _winrt.UInt32) -> _winrt.Boolean:
        ...

class PointerVisualizationSettings(_winrt.Object):
    ...
    is_contact_feedback_enabled: _winrt.Boolean
    is_barrel_button_feedback_enabled: _winrt.Boolean
    def get_for_current_view() -> PointerVisualizationSettings:
        ...

class RadialController(_winrt.Object):
    ...
    use_automatic_haptic_feedback: _winrt.Boolean
    rotation_resolution_in_degrees: _winrt.Double
    menu: RadialControllerMenu
    def create_for_current_view() -> RadialController:
        ...
    def is_supported() -> _winrt.Boolean:
        ...
    def add_button_clicked(handler: winsdk.windows.foundation.TypedEventHandler[RadialController, RadialControllerButtonClickedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_button_clicked(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_control_acquired(handler: winsdk.windows.foundation.TypedEventHandler[RadialController, RadialControllerControlAcquiredEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_control_acquired(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_control_lost(handler: winsdk.windows.foundation.TypedEventHandler[RadialController, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_control_lost(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_rotation_changed(handler: winsdk.windows.foundation.TypedEventHandler[RadialController, RadialControllerRotationChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_rotation_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_screen_contact_continued(handler: winsdk.windows.foundation.TypedEventHandler[RadialController, RadialControllerScreenContactContinuedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_screen_contact_continued(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_screen_contact_ended(handler: winsdk.windows.foundation.TypedEventHandler[RadialController, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_screen_contact_ended(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_screen_contact_started(handler: winsdk.windows.foundation.TypedEventHandler[RadialController, RadialControllerScreenContactStartedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_screen_contact_started(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_button_holding(handler: winsdk.windows.foundation.TypedEventHandler[RadialController, RadialControllerButtonHoldingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_button_holding(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_button_pressed(handler: winsdk.windows.foundation.TypedEventHandler[RadialController, RadialControllerButtonPressedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_button_pressed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_button_released(handler: winsdk.windows.foundation.TypedEventHandler[RadialController, RadialControllerButtonReleasedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_button_released(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class RadialControllerButtonClickedEventArgs(_winrt.Object):
    ...
    contact: RadialControllerScreenContact
    simple_haptics_controller: winsdk.windows.devices.haptics.SimpleHapticsController

class RadialControllerButtonHoldingEventArgs(_winrt.Object):
    ...
    contact: RadialControllerScreenContact
    simple_haptics_controller: winsdk.windows.devices.haptics.SimpleHapticsController

class RadialControllerButtonPressedEventArgs(_winrt.Object):
    ...
    contact: RadialControllerScreenContact
    simple_haptics_controller: winsdk.windows.devices.haptics.SimpleHapticsController

class RadialControllerButtonReleasedEventArgs(_winrt.Object):
    ...
    contact: RadialControllerScreenContact
    simple_haptics_controller: winsdk.windows.devices.haptics.SimpleHapticsController

class RadialControllerConfiguration(_winrt.Object):
    ...
    is_menu_suppressed: _winrt.Boolean
    active_controller_when_menu_is_suppressed: RadialController
    is_app_controller_enabled: _winrt.Boolean
    app_controller: RadialController
    def get_for_current_view() -> RadialControllerConfiguration:
        ...
    def reset_to_default_menu_items() -> None:
        ...
    def set_default_menu_items(buttons: typing.Iterable[RadialControllerSystemMenuItemKind]) -> None:
        ...
    def try_select_default_menu_item(type: RadialControllerSystemMenuItemKind) -> _winrt.Boolean:
        ...

class RadialControllerControlAcquiredEventArgs(_winrt.Object):
    ...
    contact: RadialControllerScreenContact
    is_button_pressed: _winrt.Boolean
    simple_haptics_controller: winsdk.windows.devices.haptics.SimpleHapticsController

class RadialControllerMenu(_winrt.Object):
    ...
    is_enabled: _winrt.Boolean
    items: winsdk.windows.foundation.collections.IVector[RadialControllerMenuItem]
    def get_selected_menu_item() -> RadialControllerMenuItem:
        ...
    def select_menu_item(menu_item: RadialControllerMenuItem) -> None:
        ...
    def try_select_previously_selected_menu_item() -> _winrt.Boolean:
        ...

class RadialControllerMenuItem(_winrt.Object):
    ...
    tag: _winrt.Object
    display_text: str
    def create_from_font_glyph(display_text: str, glyph: str, font_family: str) -> RadialControllerMenuItem:
        ...
    def create_from_font_glyph(display_text: str, glyph: str, font_family: str, font_uri: winsdk.windows.foundation.Uri) -> RadialControllerMenuItem:
        ...
    def create_from_icon(display_text: str, icon: winsdk.windows.storage.streams.RandomAccessStreamReference) -> RadialControllerMenuItem:
        ...
    def create_from_known_icon(display_text: str, value: RadialControllerMenuKnownIcon) -> RadialControllerMenuItem:
        ...
    def add_invoked(handler: winsdk.windows.foundation.TypedEventHandler[RadialControllerMenuItem, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_invoked(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class RadialControllerRotationChangedEventArgs(_winrt.Object):
    ...
    contact: RadialControllerScreenContact
    rotation_delta_in_degrees: _winrt.Double
    is_button_pressed: _winrt.Boolean
    simple_haptics_controller: winsdk.windows.devices.haptics.SimpleHapticsController

class RadialControllerScreenContact(_winrt.Object):
    ...
    bounds: winsdk.windows.foundation.Rect
    position: winsdk.windows.foundation.Point

class RadialControllerScreenContactContinuedEventArgs(_winrt.Object):
    ...
    contact: RadialControllerScreenContact
    is_button_pressed: _winrt.Boolean
    simple_haptics_controller: winsdk.windows.devices.haptics.SimpleHapticsController

class RadialControllerScreenContactEndedEventArgs(_winrt.Object):
    ...
    is_button_pressed: _winrt.Boolean
    simple_haptics_controller: winsdk.windows.devices.haptics.SimpleHapticsController

class RadialControllerScreenContactStartedEventArgs(_winrt.Object):
    ...
    contact: RadialControllerScreenContact
    is_button_pressed: _winrt.Boolean
    simple_haptics_controller: winsdk.windows.devices.haptics.SimpleHapticsController

class RightTappedEventArgs(_winrt.Object):
    ...
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    contact_count: _winrt.UInt32

class SystemButtonEventController(_winrt.Object):
    ...
    def create_for_dispatcher_queue(queue: winsdk.windows.system.DispatcherQueue) -> SystemButtonEventController:
        ...
    def add_system_function_button_pressed(handler: winsdk.windows.foundation.TypedEventHandler[SystemButtonEventController, SystemFunctionButtonEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_system_function_button_pressed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_system_function_button_released(handler: winsdk.windows.foundation.TypedEventHandler[SystemButtonEventController, SystemFunctionButtonEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_system_function_button_released(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_system_function_lock_changed(handler: winsdk.windows.foundation.TypedEventHandler[SystemButtonEventController, SystemFunctionLockChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_system_function_lock_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_system_function_lock_indicator_changed(handler: winsdk.windows.foundation.TypedEventHandler[SystemButtonEventController, SystemFunctionLockIndicatorChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_system_function_lock_indicator_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class SystemFunctionButtonEventArgs(_winrt.Object):
    ...
    handled: _winrt.Boolean
    timestamp: _winrt.UInt64

class SystemFunctionLockChangedEventArgs(_winrt.Object):
    ...
    handled: _winrt.Boolean
    is_locked: _winrt.Boolean
    timestamp: _winrt.UInt64

class SystemFunctionLockIndicatorChangedEventArgs(_winrt.Object):
    ...
    handled: _winrt.Boolean
    is_indicator_on: _winrt.Boolean
    timestamp: _winrt.UInt64

class TappedEventArgs(_winrt.Object):
    ...
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    tap_count: _winrt.UInt32
    contact_count: _winrt.UInt32

class IPointerPointTransform(_winrt.Object):
    ...
    inverse: IPointerPointTransform
    def transform_bounds(rect: winsdk.windows.foundation.Rect) -> winsdk.windows.foundation.Rect:
        ...
    def try_transform(in_point: winsdk.windows.foundation.Point) -> typing.Tuple[_winrt.Boolean, winsdk.windows.foundation.Point]:
        ...
