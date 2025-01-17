# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5


import sys

if sys.version_info >= (3, 9):
    from typing import Annotated
    # type aliases with struct format string annotation
    Boolean = Annotated[bool, "?"]
    Int8 = Annotated[int, "b"]
    UInt8 = Annotated[int, "B"]
    Int16 = Annotated[int, "h"]
    UInt16 = Annotated[int, "H"]
    Int32 = Annotated[int, "i"]
    UInt32 = Annotated[int, "I"]
    Int64 = Annotated[int, "q"]
    UInt64 = Annotated[int, "Q"]
    Single = Annotated[float, "f"]
    Double = Annotated[float, "d"]
else:
    Boolean = bool
    Int8 = int
    UInt8 = int
    Int16 = int
    UInt16 = int
    Int32 = int
    UInt32 = int
    Int64 = int
    UInt64 = int
    Single = float
    Double = float

Char16 = UInt16  # Char16 also implies valid UTF-16 codepoint

MTA: int
STA: int

def init_apartment(apartment_type: int) -> None: ...
def uninit_apartment() -> None: ...
def initialize_with_window(obj: Object, hwnd: int) -> None: ...

class Object:
    pass
