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
    import winsdk.windows.graphics.printing
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class PrintOptionStates(enum.IntFlag):
    NONE = 0
    ENABLED = 0x1
    CONSTRAINED = 0x2

class PrintOptionType(enum.IntEnum):
    UNKNOWN = 0
    NUMBER = 1
    TEXT = 2
    ITEM_LIST = 3
    TOGGLE = 4

class PrintBindingOptionDetails(IPrintOptionDetails, IPrintItemListOptionDetails, _winrt.Object):
    ...
    warning_text: str
    description: str
    items: winsdk.windows.foundation.collections.IVectorView[_winrt.Object]
    state: PrintOptionStates
    error_text: str
    option_id: str
    option_type: PrintOptionType
    value: _winrt.Object
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class PrintBorderingOptionDetails(IPrintOptionDetails, IPrintItemListOptionDetails, _winrt.Object):
    ...
    warning_text: str
    description: str
    items: winsdk.windows.foundation.collections.IVectorView[_winrt.Object]
    state: PrintOptionStates
    error_text: str
    option_id: str
    option_type: PrintOptionType
    value: _winrt.Object
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class PrintCollationOptionDetails(IPrintOptionDetails, IPrintItemListOptionDetails, _winrt.Object):
    ...
    warning_text: str
    description: str
    items: winsdk.windows.foundation.collections.IVectorView[_winrt.Object]
    state: PrintOptionStates
    error_text: str
    option_id: str
    option_type: PrintOptionType
    value: _winrt.Object
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class PrintColorModeOptionDetails(IPrintOptionDetails, IPrintItemListOptionDetails, _winrt.Object):
    ...
    warning_text: str
    description: str
    items: winsdk.windows.foundation.collections.IVectorView[_winrt.Object]
    state: PrintOptionStates
    error_text: str
    option_id: str
    option_type: PrintOptionType
    value: _winrt.Object
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class PrintCopiesOptionDetails(IPrintOptionDetails, IPrintNumberOptionDetails, _winrt.Object):
    ...
    warning_text: str
    description: str
    max_value: _winrt.UInt32
    min_value: _winrt.UInt32
    state: PrintOptionStates
    error_text: str
    option_id: str
    option_type: PrintOptionType
    value: _winrt.Object
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class PrintCustomItemDetails(_winrt.Object):
    ...
    item_display_name: str
    item_id: str

class PrintCustomItemListOptionDetails(IPrintOptionDetails, IPrintCustomOptionDetails, IPrintItemListOptionDetails, _winrt.Object):
    ...
    warning_text: str
    description: str
    display_name: str
    items: winsdk.windows.foundation.collections.IVectorView[_winrt.Object]
    state: PrintOptionStates
    error_text: str
    option_id: str
    option_type: PrintOptionType
    value: _winrt.Object
    def add_item(item_id: str, display_name: str) -> None:
        ...
    def add_item(item_id: str, display_name: str, description: str, icon: winsdk.windows.storage.streams.IRandomAccessStreamWithContentType) -> None:
        ...
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class PrintCustomTextOptionDetails(IPrintOptionDetails, IPrintCustomOptionDetails, _winrt.Object):
    ...
    display_name: str
    max_characters: _winrt.UInt32
    warning_text: str
    description: str
    state: PrintOptionStates
    error_text: str
    option_id: str
    option_type: PrintOptionType
    value: _winrt.Object
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class PrintCustomToggleOptionDetails(IPrintOptionDetails, IPrintCustomOptionDetails, _winrt.Object):
    ...
    display_name: str
    warning_text: str
    description: str
    state: PrintOptionStates
    error_text: str
    option_id: str
    option_type: PrintOptionType
    value: _winrt.Object
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class PrintDuplexOptionDetails(IPrintOptionDetails, IPrintItemListOptionDetails, _winrt.Object):
    ...
    warning_text: str
    description: str
    items: winsdk.windows.foundation.collections.IVectorView[_winrt.Object]
    state: PrintOptionStates
    error_text: str
    option_id: str
    option_type: PrintOptionType
    value: _winrt.Object
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class PrintHolePunchOptionDetails(IPrintOptionDetails, IPrintItemListOptionDetails, _winrt.Object):
    ...
    warning_text: str
    description: str
    items: winsdk.windows.foundation.collections.IVectorView[_winrt.Object]
    state: PrintOptionStates
    error_text: str
    option_id: str
    option_type: PrintOptionType
    value: _winrt.Object
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class PrintMediaSizeOptionDetails(IPrintOptionDetails, IPrintItemListOptionDetails, _winrt.Object):
    ...
    items: winsdk.windows.foundation.collections.IVectorView[_winrt.Object]
    warning_text: str
    description: str
    state: PrintOptionStates
    error_text: str
    option_id: str
    option_type: PrintOptionType
    value: _winrt.Object
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class PrintMediaTypeOptionDetails(IPrintOptionDetails, IPrintItemListOptionDetails, _winrt.Object):
    ...
    items: winsdk.windows.foundation.collections.IVectorView[_winrt.Object]
    warning_text: str
    description: str
    state: PrintOptionStates
    error_text: str
    option_id: str
    option_type: PrintOptionType
    value: _winrt.Object
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class PrintOrientationOptionDetails(IPrintOptionDetails, IPrintItemListOptionDetails, _winrt.Object):
    ...
    items: winsdk.windows.foundation.collections.IVectorView[_winrt.Object]
    state: PrintOptionStates
    error_text: str
    option_id: str
    option_type: PrintOptionType
    value: _winrt.Object
    warning_text: str
    description: str
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class PrintPageRangeOptionDetails(IPrintOptionDetails, _winrt.Object):
    ...
    state: PrintOptionStates
    error_text: str
    option_id: str
    option_type: PrintOptionType
    value: _winrt.Object
    warning_text: str
    description: str
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class PrintQualityOptionDetails(IPrintOptionDetails, IPrintItemListOptionDetails, _winrt.Object):
    ...
    items: winsdk.windows.foundation.collections.IVectorView[_winrt.Object]
    state: PrintOptionStates
    error_text: str
    option_id: str
    option_type: PrintOptionType
    value: _winrt.Object
    warning_text: str
    description: str
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class PrintStapleOptionDetails(IPrintOptionDetails, IPrintItemListOptionDetails, _winrt.Object):
    ...
    items: winsdk.windows.foundation.collections.IVectorView[_winrt.Object]
    state: PrintOptionStates
    error_text: str
    option_id: str
    option_type: PrintOptionType
    value: _winrt.Object
    warning_text: str
    description: str
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class PrintTaskOptionChangedEventArgs(_winrt.Object):
    ...
    option_id: _winrt.Object

class PrintTaskOptionDetails(winsdk.windows.graphics.printing.IPrintTaskOptionsCore, winsdk.windows.graphics.printing.IPrintTaskOptionsCoreUIConfiguration, _winrt.Object):
    ...
    displayed_options: winsdk.windows.foundation.collections.IVector[str]
    options: winsdk.windows.foundation.collections.IMapView[str, IPrintOptionDetails]
    def create_item_list_option(option_id: str, display_name: str) -> PrintCustomItemListOptionDetails:
        ...
    def create_text_option(option_id: str, display_name: str) -> PrintCustomTextOptionDetails:
        ...
    def create_toggle_option(option_id: str, display_name: str) -> PrintCustomToggleOptionDetails:
        ...
    def get_from_print_task_options(print_task_options: winsdk.windows.graphics.printing.PrintTaskOptions) -> PrintTaskOptionDetails:
        ...
    def get_page_description(job_page_number: _winrt.UInt32) -> winsdk.windows.graphics.printing.PrintPageDescription:
        ...
    def add_begin_validation(event_handler: winsdk.windows.foundation.TypedEventHandler[PrintTaskOptionDetails, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_begin_validation(event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_option_changed(event_handler: winsdk.windows.foundation.TypedEventHandler[PrintTaskOptionDetails, PrintTaskOptionChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_option_changed(event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class IPrintCustomOptionDetails(IPrintOptionDetails, _winrt.Object):
    ...
    display_name: str
    error_text: str
    option_id: str
    option_type: PrintOptionType
    state: PrintOptionStates
    value: _winrt.Object
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class IPrintItemListOptionDetails(IPrintOptionDetails, _winrt.Object):
    ...
    items: winsdk.windows.foundation.collections.IVectorView[_winrt.Object]
    error_text: str
    option_id: str
    option_type: PrintOptionType
    state: PrintOptionStates
    value: _winrt.Object
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class IPrintNumberOptionDetails(IPrintOptionDetails, _winrt.Object):
    ...
    max_value: _winrt.UInt32
    min_value: _winrt.UInt32
    error_text: str
    option_id: str
    option_type: PrintOptionType
    state: PrintOptionStates
    value: _winrt.Object
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class IPrintOptionDetails(_winrt.Object):
    ...
    error_text: str
    option_id: str
    option_type: PrintOptionType
    state: PrintOptionStates
    value: _winrt.Object
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...

class IPrintTextOptionDetails(IPrintOptionDetails, _winrt.Object):
    ...
    max_characters: _winrt.UInt32
    error_text: str
    option_id: str
    option_type: PrintOptionType
    state: PrintOptionStates
    value: _winrt.Object
    def try_set_value(value: _winrt.Object) -> _winrt.Boolean:
        ...
