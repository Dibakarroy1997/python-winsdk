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
    import winsdk.windows.ui.input.inking
except Exception:
    pass

class InkAnalysisDrawingKind(enum.IntEnum):
    DRAWING = 0
    CIRCLE = 1
    ELLIPSE = 2
    TRIANGLE = 3
    ISOSCELES_TRIANGLE = 4
    EQUILATERAL_TRIANGLE = 5
    RIGHT_TRIANGLE = 6
    QUADRILATERAL = 7
    RECTANGLE = 8
    SQUARE = 9
    DIAMOND = 10
    TRAPEZOID = 11
    PARALLELOGRAM = 12
    PENTAGON = 13
    HEXAGON = 14

class InkAnalysisNodeKind(enum.IntEnum):
    UNCLASSIFIED_INK = 0
    ROOT = 1
    WRITING_REGION = 2
    PARAGRAPH = 3
    LINE = 4
    INK_WORD = 5
    INK_BULLET = 6
    INK_DRAWING = 7
    LIST_ITEM = 8

class InkAnalysisStatus(enum.IntEnum):
    UPDATED = 0
    UNCHANGED = 1

class InkAnalysisStrokeKind(enum.IntEnum):
    AUTO = 0
    WRITING = 1
    DRAWING = 2

class InkAnalysisInkBullet(IInkAnalysisNode, _winrt.Object):
    ...
    recognized_text: str
    bounding_rect: winsdk.windows.foundation.Rect
    children: winsdk.windows.foundation.collections.IVectorView[IInkAnalysisNode]
    id: _winrt.UInt32
    kind: InkAnalysisNodeKind
    parent: IInkAnalysisNode
    rotated_bounding_rect: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.Point]
    def get_stroke_ids() -> winsdk.windows.foundation.collections.IVectorView[_winrt.UInt32]:
        ...

class InkAnalysisInkDrawing(IInkAnalysisNode, _winrt.Object):
    ...
    center: winsdk.windows.foundation.Point
    drawing_kind: InkAnalysisDrawingKind
    points: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.Point]
    bounding_rect: winsdk.windows.foundation.Rect
    children: winsdk.windows.foundation.collections.IVectorView[IInkAnalysisNode]
    id: _winrt.UInt32
    kind: InkAnalysisNodeKind
    parent: IInkAnalysisNode
    rotated_bounding_rect: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.Point]
    def get_stroke_ids() -> winsdk.windows.foundation.collections.IVectorView[_winrt.UInt32]:
        ...

class InkAnalysisInkWord(IInkAnalysisNode, _winrt.Object):
    ...
    recognized_text: str
    text_alternates: winsdk.windows.foundation.collections.IVectorView[str]
    bounding_rect: winsdk.windows.foundation.Rect
    children: winsdk.windows.foundation.collections.IVectorView[IInkAnalysisNode]
    id: _winrt.UInt32
    kind: InkAnalysisNodeKind
    parent: IInkAnalysisNode
    rotated_bounding_rect: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.Point]
    def get_stroke_ids() -> winsdk.windows.foundation.collections.IVectorView[_winrt.UInt32]:
        ...

class InkAnalysisLine(IInkAnalysisNode, _winrt.Object):
    ...
    indent_level: _winrt.Int32
    recognized_text: str
    bounding_rect: winsdk.windows.foundation.Rect
    children: winsdk.windows.foundation.collections.IVectorView[IInkAnalysisNode]
    id: _winrt.UInt32
    kind: InkAnalysisNodeKind
    parent: IInkAnalysisNode
    rotated_bounding_rect: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.Point]
    def get_stroke_ids() -> winsdk.windows.foundation.collections.IVectorView[_winrt.UInt32]:
        ...

class InkAnalysisListItem(IInkAnalysisNode, _winrt.Object):
    ...
    recognized_text: str
    bounding_rect: winsdk.windows.foundation.Rect
    children: winsdk.windows.foundation.collections.IVectorView[IInkAnalysisNode]
    id: _winrt.UInt32
    kind: InkAnalysisNodeKind
    parent: IInkAnalysisNode
    rotated_bounding_rect: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.Point]
    def get_stroke_ids() -> winsdk.windows.foundation.collections.IVectorView[_winrt.UInt32]:
        ...

class InkAnalysisNode(IInkAnalysisNode, _winrt.Object):
    ...
    bounding_rect: winsdk.windows.foundation.Rect
    children: winsdk.windows.foundation.collections.IVectorView[IInkAnalysisNode]
    id: _winrt.UInt32
    kind: InkAnalysisNodeKind
    parent: IInkAnalysisNode
    rotated_bounding_rect: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.Point]
    def get_stroke_ids() -> winsdk.windows.foundation.collections.IVectorView[_winrt.UInt32]:
        ...

class InkAnalysisParagraph(IInkAnalysisNode, _winrt.Object):
    ...
    bounding_rect: winsdk.windows.foundation.Rect
    children: winsdk.windows.foundation.collections.IVectorView[IInkAnalysisNode]
    id: _winrt.UInt32
    kind: InkAnalysisNodeKind
    parent: IInkAnalysisNode
    rotated_bounding_rect: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.Point]
    recognized_text: str
    def get_stroke_ids() -> winsdk.windows.foundation.collections.IVectorView[_winrt.UInt32]:
        ...

class InkAnalysisResult(_winrt.Object):
    ...
    status: InkAnalysisStatus

class InkAnalysisRoot(IInkAnalysisNode, _winrt.Object):
    ...
    bounding_rect: winsdk.windows.foundation.Rect
    children: winsdk.windows.foundation.collections.IVectorView[IInkAnalysisNode]
    id: _winrt.UInt32
    kind: InkAnalysisNodeKind
    parent: IInkAnalysisNode
    rotated_bounding_rect: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.Point]
    recognized_text: str
    def find_nodes(node_kind: InkAnalysisNodeKind) -> winsdk.windows.foundation.collections.IVectorView[IInkAnalysisNode]:
        ...
    def get_stroke_ids() -> winsdk.windows.foundation.collections.IVectorView[_winrt.UInt32]:
        ...

class InkAnalysisWritingRegion(IInkAnalysisNode, _winrt.Object):
    ...
    bounding_rect: winsdk.windows.foundation.Rect
    children: winsdk.windows.foundation.collections.IVectorView[IInkAnalysisNode]
    id: _winrt.UInt32
    kind: InkAnalysisNodeKind
    parent: IInkAnalysisNode
    rotated_bounding_rect: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.Point]
    recognized_text: str
    def get_stroke_ids() -> winsdk.windows.foundation.collections.IVectorView[_winrt.UInt32]:
        ...

class InkAnalyzer(_winrt.Object):
    ...
    analysis_root: InkAnalysisRoot
    is_analyzing: _winrt.Boolean
    def __init__(self, ) -> None:
        ...
    def add_data_for_stroke(stroke: winsdk.windows.ui.input.inking.InkStroke) -> None:
        ...
    def add_data_for_strokes(strokes: typing.Iterable[winsdk.windows.ui.input.inking.InkStroke]) -> None:
        ...
    def analyze_async() -> winsdk.windows.foundation.IAsyncOperation[InkAnalysisResult]:
        ...
    def clear_data_for_all_strokes() -> None:
        ...
    def remove_data_for_stroke(stroke_id: _winrt.UInt32) -> None:
        ...
    def remove_data_for_strokes(stroke_ids: typing.Iterable[_winrt.UInt32]) -> None:
        ...
    def replace_data_for_stroke(stroke: winsdk.windows.ui.input.inking.InkStroke) -> None:
        ...
    def set_stroke_data_kind(stroke_id: _winrt.UInt32, stroke_kind: InkAnalysisStrokeKind) -> None:
        ...

class IInkAnalysisNode(_winrt.Object):
    ...
    bounding_rect: winsdk.windows.foundation.Rect
    children: winsdk.windows.foundation.collections.IVectorView[IInkAnalysisNode]
    id: _winrt.UInt32
    kind: InkAnalysisNodeKind
    parent: IInkAnalysisNode
    rotated_bounding_rect: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.foundation.Point]
    def get_stroke_ids() -> winsdk.windows.foundation.collections.IVectorView[_winrt.UInt32]:
        ...

class IInkAnalyzerFactory(_winrt.Object):
    ...
    def create_analyzer() -> InkAnalyzer:
        ...
