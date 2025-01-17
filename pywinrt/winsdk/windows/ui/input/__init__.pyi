# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.devices.haptics
import winsdk.windows.devices.input
import winsdk.windows.foundation
import winsdk.windows.foundation.collections
import winsdk.windows.storage.streams
import winsdk.windows.system
import winsdk.windows.ui.core

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

Self = typing.TypeVar('Self')

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

class AttachableInputObject(_winrt.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> AttachableInputObject: ...
    def close(self) -> None: ...

class CrossSlidingEventArgs(_winrt.Object):
    cross_sliding_state: CrossSlidingState
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    contact_count: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> CrossSlidingEventArgs: ...

class DraggingEventArgs(_winrt.Object):
    dragging_state: DraggingState
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    contact_count: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> DraggingEventArgs: ...

class EdgeGesture(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> EdgeGesture: ...
    @staticmethod
    def get_for_current_view() -> typing.Optional[EdgeGesture]: ...
    def add_canceled(self, handler: winsdk.windows.foundation.TypedEventHandler[EdgeGesture, EdgeGestureEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_canceled(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_completed(self, handler: winsdk.windows.foundation.TypedEventHandler[EdgeGesture, EdgeGestureEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_completed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_starting(self, handler: winsdk.windows.foundation.TypedEventHandler[EdgeGesture, EdgeGestureEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_starting(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class EdgeGestureEventArgs(_winrt.Object):
    kind: EdgeGestureKind
    @staticmethod
    def _from(obj: _winrt.Object) -> EdgeGestureEventArgs: ...

class GestureRecognizer(_winrt.Object):
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
    mouse_wheel_parameters: typing.Optional[MouseWheelParameters]
    translation_min_contact_count: _winrt.UInt32
    translation_max_contact_count: _winrt.UInt32
    tap_min_contact_count: _winrt.UInt32
    tap_max_contact_count: _winrt.UInt32
    hold_start_delay: winsdk.windows.foundation.TimeSpan
    hold_radius: _winrt.Single
    hold_min_contact_count: _winrt.UInt32
    hold_max_contact_count: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> GestureRecognizer: ...
    def __init__(self) -> None: ...
    def can_be_double_tap(self, value: typing.Optional[PointerPoint]) -> _winrt.Boolean: ...
    def complete_gesture(self) -> None: ...
    def process_down_event(self, value: typing.Optional[PointerPoint]) -> None: ...
    def process_inertia(self) -> None: ...
    def process_mouse_wheel_event(self, value: typing.Optional[PointerPoint], is_shift_key_down: _winrt.Boolean, is_control_key_down: _winrt.Boolean) -> None: ...
    def process_move_events(self, value: winsdk.windows.foundation.collections.IVector[PointerPoint]) -> None: ...
    def process_up_event(self, value: typing.Optional[PointerPoint]) -> None: ...
    def add_cross_sliding(self, handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, CrossSlidingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_cross_sliding(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_dragging(self, handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, DraggingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_dragging(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_holding(self, handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, HoldingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_holding(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_manipulation_completed(self, handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, ManipulationCompletedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_manipulation_completed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_manipulation_inertia_starting(self, handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, ManipulationInertiaStartingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_manipulation_inertia_starting(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_manipulation_started(self, handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, ManipulationStartedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_manipulation_started(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_manipulation_updated(self, handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, ManipulationUpdatedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_manipulation_updated(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_right_tapped(self, handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, RightTappedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_right_tapped(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_tapped(self, handler: winsdk.windows.foundation.TypedEventHandler[GestureRecognizer, TappedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_tapped(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class HoldingEventArgs(_winrt.Object):
    holding_state: HoldingState
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    contact_count: _winrt.UInt32
    current_contact_count: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> HoldingEventArgs: ...

class InputActivationListener(_winrt.Object):
    state: InputActivationState
    @staticmethod
    def _from(obj: _winrt.Object) -> InputActivationListener: ...
    def add_input_activation_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[InputActivationListener, InputActivationListenerActivationChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_input_activation_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class InputActivationListenerActivationChangedEventArgs(_winrt.Object):
    state: InputActivationState
    @staticmethod
    def _from(obj: _winrt.Object) -> InputActivationListenerActivationChangedEventArgs: ...

class KeyboardDeliveryInterceptor(_winrt.Object):
    is_interception_enabled_when_in_foreground: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> KeyboardDeliveryInterceptor: ...
    @staticmethod
    def get_for_current_view() -> typing.Optional[KeyboardDeliveryInterceptor]: ...
    def add_key_down(self, handler: winsdk.windows.foundation.TypedEventHandler[KeyboardDeliveryInterceptor, winsdk.windows.ui.core.KeyEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_key_down(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_key_up(self, handler: winsdk.windows.foundation.TypedEventHandler[KeyboardDeliveryInterceptor, winsdk.windows.ui.core.KeyEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_key_up(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class ManipulationCompletedEventArgs(_winrt.Object):
    cumulative: ManipulationDelta
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    velocities: ManipulationVelocities
    contact_count: _winrt.UInt32
    current_contact_count: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> ManipulationCompletedEventArgs: ...

class ManipulationInertiaStartingEventArgs(_winrt.Object):
    cumulative: ManipulationDelta
    delta: ManipulationDelta
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    velocities: ManipulationVelocities
    contact_count: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> ManipulationInertiaStartingEventArgs: ...

class ManipulationStartedEventArgs(_winrt.Object):
    cumulative: ManipulationDelta
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    contact_count: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> ManipulationStartedEventArgs: ...

class ManipulationUpdatedEventArgs(_winrt.Object):
    cumulative: ManipulationDelta
    delta: ManipulationDelta
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    velocities: ManipulationVelocities
    contact_count: _winrt.UInt32
    current_contact_count: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> ManipulationUpdatedEventArgs: ...

class MouseWheelParameters(_winrt.Object):
    page_translation: winsdk.windows.foundation.Point
    delta_scale: _winrt.Single
    delta_rotation_angle: _winrt.Single
    char_translation: winsdk.windows.foundation.Point
    @staticmethod
    def _from(obj: _winrt.Object) -> MouseWheelParameters: ...

class PointerPoint(_winrt.Object):
    frame_id: _winrt.UInt32
    is_in_contact: _winrt.Boolean
    pointer_device: typing.Optional[winsdk.windows.devices.input.PointerDevice]
    pointer_id: _winrt.UInt32
    position: winsdk.windows.foundation.Point
    properties: typing.Optional[PointerPointProperties]
    raw_position: winsdk.windows.foundation.Point
    timestamp: _winrt.UInt64
    @staticmethod
    def _from(obj: _winrt.Object) -> PointerPoint: ...
    @typing.overload
    @staticmethod
    def get_current_point(pointer_id: _winrt.UInt32) -> typing.Optional[PointerPoint]: ...
    @typing.overload
    @staticmethod
    def get_current_point(pointer_id: _winrt.UInt32, transform: typing.Optional[IPointerPointTransform]) -> typing.Optional[PointerPoint]: ...
    @typing.overload
    @staticmethod
    def get_intermediate_points(pointer_id: _winrt.UInt32) -> typing.Optional[winsdk.windows.foundation.collections.IVector[PointerPoint]]: ...
    @typing.overload
    @staticmethod
    def get_intermediate_points(pointer_id: _winrt.UInt32, transform: typing.Optional[IPointerPointTransform]) -> typing.Optional[winsdk.windows.foundation.collections.IVector[PointerPoint]]: ...

class PointerPointProperties(_winrt.Object):
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
    z_distance: typing.Optional[typing.Optional[_winrt.Single]]
    @staticmethod
    def _from(obj: _winrt.Object) -> PointerPointProperties: ...
    def get_usage_value(self, usage_page: _winrt.UInt32, usage_id: _winrt.UInt32) -> _winrt.Int32: ...
    def has_usage(self, usage_page: _winrt.UInt32, usage_id: _winrt.UInt32) -> _winrt.Boolean: ...

class PointerVisualizationSettings(_winrt.Object):
    is_contact_feedback_enabled: _winrt.Boolean
    is_barrel_button_feedback_enabled: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> PointerVisualizationSettings: ...
    @staticmethod
    def get_for_current_view() -> typing.Optional[PointerVisualizationSettings]: ...

class RadialController(_winrt.Object):
    use_automatic_haptic_feedback: _winrt.Boolean
    rotation_resolution_in_degrees: _winrt.Double
    menu: typing.Optional[RadialControllerMenu]
    @staticmethod
    def _from(obj: _winrt.Object) -> RadialController: ...
    @staticmethod
    def create_for_current_view() -> typing.Optional[RadialController]: ...
    @staticmethod
    def is_supported() -> _winrt.Boolean: ...
    def add_button_clicked(self, handler: winsdk.windows.foundation.TypedEventHandler[RadialController, RadialControllerButtonClickedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_button_clicked(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_control_acquired(self, handler: winsdk.windows.foundation.TypedEventHandler[RadialController, RadialControllerControlAcquiredEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_control_acquired(self, cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_control_lost(self, handler: winsdk.windows.foundation.TypedEventHandler[RadialController, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_control_lost(self, cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_rotation_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[RadialController, RadialControllerRotationChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_rotation_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_screen_contact_continued(self, handler: winsdk.windows.foundation.TypedEventHandler[RadialController, RadialControllerScreenContactContinuedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_screen_contact_continued(self, cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_screen_contact_ended(self, handler: winsdk.windows.foundation.TypedEventHandler[RadialController, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_screen_contact_ended(self, cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_screen_contact_started(self, handler: winsdk.windows.foundation.TypedEventHandler[RadialController, RadialControllerScreenContactStartedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_screen_contact_started(self, cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_button_holding(self, handler: winsdk.windows.foundation.TypedEventHandler[RadialController, RadialControllerButtonHoldingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_button_holding(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_button_pressed(self, handler: winsdk.windows.foundation.TypedEventHandler[RadialController, RadialControllerButtonPressedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_button_pressed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_button_released(self, handler: winsdk.windows.foundation.TypedEventHandler[RadialController, RadialControllerButtonReleasedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_button_released(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class RadialControllerButtonClickedEventArgs(_winrt.Object):
    contact: typing.Optional[RadialControllerScreenContact]
    simple_haptics_controller: typing.Optional[winsdk.windows.devices.haptics.SimpleHapticsController]
    @staticmethod
    def _from(obj: _winrt.Object) -> RadialControllerButtonClickedEventArgs: ...

class RadialControllerButtonHoldingEventArgs(_winrt.Object):
    contact: typing.Optional[RadialControllerScreenContact]
    simple_haptics_controller: typing.Optional[winsdk.windows.devices.haptics.SimpleHapticsController]
    @staticmethod
    def _from(obj: _winrt.Object) -> RadialControllerButtonHoldingEventArgs: ...

class RadialControllerButtonPressedEventArgs(_winrt.Object):
    contact: typing.Optional[RadialControllerScreenContact]
    simple_haptics_controller: typing.Optional[winsdk.windows.devices.haptics.SimpleHapticsController]
    @staticmethod
    def _from(obj: _winrt.Object) -> RadialControllerButtonPressedEventArgs: ...

class RadialControllerButtonReleasedEventArgs(_winrt.Object):
    contact: typing.Optional[RadialControllerScreenContact]
    simple_haptics_controller: typing.Optional[winsdk.windows.devices.haptics.SimpleHapticsController]
    @staticmethod
    def _from(obj: _winrt.Object) -> RadialControllerButtonReleasedEventArgs: ...

class RadialControllerConfiguration(_winrt.Object):
    is_menu_suppressed: _winrt.Boolean
    active_controller_when_menu_is_suppressed: typing.Optional[RadialController]
    is_app_controller_enabled: _winrt.Boolean
    app_controller: typing.Optional[RadialController]
    @staticmethod
    def _from(obj: _winrt.Object) -> RadialControllerConfiguration: ...
    @staticmethod
    def get_for_current_view() -> typing.Optional[RadialControllerConfiguration]: ...
    def reset_to_default_menu_items(self) -> None: ...
    def set_default_menu_items(self, buttons: typing.Iterable[RadialControllerSystemMenuItemKind]) -> None: ...
    def try_select_default_menu_item(self, type: RadialControllerSystemMenuItemKind) -> _winrt.Boolean: ...

class RadialControllerControlAcquiredEventArgs(_winrt.Object):
    contact: typing.Optional[RadialControllerScreenContact]
    is_button_pressed: _winrt.Boolean
    simple_haptics_controller: typing.Optional[winsdk.windows.devices.haptics.SimpleHapticsController]
    @staticmethod
    def _from(obj: _winrt.Object) -> RadialControllerControlAcquiredEventArgs: ...

class RadialControllerMenu(_winrt.Object):
    is_enabled: _winrt.Boolean
    items: typing.Optional[winsdk.windows.foundation.collections.IVector[RadialControllerMenuItem]]
    @staticmethod
    def _from(obj: _winrt.Object) -> RadialControllerMenu: ...
    def get_selected_menu_item(self) -> typing.Optional[RadialControllerMenuItem]: ...
    def select_menu_item(self, menu_item: typing.Optional[RadialControllerMenuItem]) -> None: ...
    def try_select_previously_selected_menu_item(self) -> _winrt.Boolean: ...

class RadialControllerMenuItem(_winrt.Object):
    tag: typing.Optional[_winrt.Object]
    display_text: str
    @staticmethod
    def _from(obj: _winrt.Object) -> RadialControllerMenuItem: ...
    @typing.overload
    @staticmethod
    def create_from_font_glyph(display_text: str, glyph: str, font_family: str) -> typing.Optional[RadialControllerMenuItem]: ...
    @typing.overload
    @staticmethod
    def create_from_font_glyph(display_text: str, glyph: str, font_family: str, font_uri: typing.Optional[winsdk.windows.foundation.Uri]) -> typing.Optional[RadialControllerMenuItem]: ...
    @staticmethod
    def create_from_icon(display_text: str, icon: typing.Optional[winsdk.windows.storage.streams.RandomAccessStreamReference]) -> typing.Optional[RadialControllerMenuItem]: ...
    @staticmethod
    def create_from_known_icon(display_text: str, value: RadialControllerMenuKnownIcon) -> typing.Optional[RadialControllerMenuItem]: ...
    def add_invoked(self, handler: winsdk.windows.foundation.TypedEventHandler[RadialControllerMenuItem, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_invoked(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class RadialControllerRotationChangedEventArgs(_winrt.Object):
    contact: typing.Optional[RadialControllerScreenContact]
    rotation_delta_in_degrees: _winrt.Double
    is_button_pressed: _winrt.Boolean
    simple_haptics_controller: typing.Optional[winsdk.windows.devices.haptics.SimpleHapticsController]
    @staticmethod
    def _from(obj: _winrt.Object) -> RadialControllerRotationChangedEventArgs: ...

class RadialControllerScreenContact(_winrt.Object):
    bounds: winsdk.windows.foundation.Rect
    position: winsdk.windows.foundation.Point
    @staticmethod
    def _from(obj: _winrt.Object) -> RadialControllerScreenContact: ...

class RadialControllerScreenContactContinuedEventArgs(_winrt.Object):
    contact: typing.Optional[RadialControllerScreenContact]
    is_button_pressed: _winrt.Boolean
    simple_haptics_controller: typing.Optional[winsdk.windows.devices.haptics.SimpleHapticsController]
    @staticmethod
    def _from(obj: _winrt.Object) -> RadialControllerScreenContactContinuedEventArgs: ...

class RadialControllerScreenContactEndedEventArgs(_winrt.Object):
    is_button_pressed: _winrt.Boolean
    simple_haptics_controller: typing.Optional[winsdk.windows.devices.haptics.SimpleHapticsController]
    @staticmethod
    def _from(obj: _winrt.Object) -> RadialControllerScreenContactEndedEventArgs: ...

class RadialControllerScreenContactStartedEventArgs(_winrt.Object):
    contact: typing.Optional[RadialControllerScreenContact]
    is_button_pressed: _winrt.Boolean
    simple_haptics_controller: typing.Optional[winsdk.windows.devices.haptics.SimpleHapticsController]
    @staticmethod
    def _from(obj: _winrt.Object) -> RadialControllerScreenContactStartedEventArgs: ...

class RightTappedEventArgs(_winrt.Object):
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    contact_count: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> RightTappedEventArgs: ...

class SystemButtonEventController(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> SystemButtonEventController: ...
    @staticmethod
    def create_for_dispatcher_queue(queue: typing.Optional[winsdk.windows.system.DispatcherQueue]) -> typing.Optional[SystemButtonEventController]: ...
    def add_system_function_button_pressed(self, handler: winsdk.windows.foundation.TypedEventHandler[SystemButtonEventController, SystemFunctionButtonEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_system_function_button_pressed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_system_function_button_released(self, handler: winsdk.windows.foundation.TypedEventHandler[SystemButtonEventController, SystemFunctionButtonEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_system_function_button_released(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_system_function_lock_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[SystemButtonEventController, SystemFunctionLockChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_system_function_lock_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_system_function_lock_indicator_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[SystemButtonEventController, SystemFunctionLockIndicatorChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_system_function_lock_indicator_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class SystemFunctionButtonEventArgs(_winrt.Object):
    handled: _winrt.Boolean
    timestamp: _winrt.UInt64
    @staticmethod
    def _from(obj: _winrt.Object) -> SystemFunctionButtonEventArgs: ...

class SystemFunctionLockChangedEventArgs(_winrt.Object):
    handled: _winrt.Boolean
    is_locked: _winrt.Boolean
    timestamp: _winrt.UInt64
    @staticmethod
    def _from(obj: _winrt.Object) -> SystemFunctionLockChangedEventArgs: ...

class SystemFunctionLockIndicatorChangedEventArgs(_winrt.Object):
    handled: _winrt.Boolean
    is_indicator_on: _winrt.Boolean
    timestamp: _winrt.UInt64
    @staticmethod
    def _from(obj: _winrt.Object) -> SystemFunctionLockIndicatorChangedEventArgs: ...

class TappedEventArgs(_winrt.Object):
    pointer_device_type: winsdk.windows.devices.input.PointerDeviceType
    position: winsdk.windows.foundation.Point
    tap_count: _winrt.UInt32
    contact_count: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> TappedEventArgs: ...

class IPointerPointTransform(_winrt.Object):
    inverse: typing.Optional[IPointerPointTransform]
    @staticmethod
    def _from(obj: _winrt.Object) -> IPointerPointTransform: ...
    def transform_bounds(self, rect: winsdk.windows.foundation.Rect) -> winsdk.windows.foundation.Rect: ...
    def try_transform(self, in_point: winsdk.windows.foundation.Point) -> typing.Tuple[_winrt.Boolean, winsdk.windows.foundation.Point]: ...

