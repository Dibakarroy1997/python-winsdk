# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.foundation
import winsdk.windows.foundation.collections
import winsdk.windows.graphics
import winsdk.windows.graphics.directx.direct3d11
import winsdk.windows.graphics.imaging
import winsdk.windows.media
import winsdk.windows.storage
import winsdk.windows.storage.streams

class LearningModelDeviceKind(enum.IntEnum):
    DEFAULT = 0
    CPU = 1
    DIRECT_X = 2
    DIRECT_X_HIGH_PERFORMANCE = 3
    DIRECT_X_MIN_POWER = 4

class LearningModelFeatureKind(enum.IntEnum):
    TENSOR = 0
    SEQUENCE = 1
    MAP = 2
    IMAGE = 3

class LearningModelPixelRange(enum.IntEnum):
    ZERO_TO255 = 0
    ZERO_TO_ONE = 1
    MINUS_ONE_TO_ONE = 2

class TensorKind(enum.IntEnum):
    UNDEFINED = 0
    FLOAT = 1
    UINT8 = 2
    INT8 = 3
    UINT16 = 4
    INT16 = 5
    INT32 = 6
    INT64 = 7
    STRING = 8
    BOOLEAN = 9
    FLOAT16 = 10
    DOUBLE = 11
    UINT32 = 12
    UINT64 = 13
    COMPLEX64 = 14
    COMPLEX128 = 15

Self = typing.TypeVar('Self')

class ImageFeatureDescriptor(_winrt.Object):
    bitmap_alpha_mode: winsdk.windows.graphics.imaging.BitmapAlphaMode
    bitmap_pixel_format: winsdk.windows.graphics.imaging.BitmapPixelFormat
    height: _winrt.UInt32
    width: _winrt.UInt32
    pixel_range: LearningModelPixelRange
    description: str
    is_required: _winrt.Boolean
    kind: LearningModelFeatureKind
    name: str
    @staticmethod
    def _from(obj: _winrt.Object) -> ImageFeatureDescriptor: ...

class ImageFeatureValue(_winrt.Object):
    video_frame: typing.Optional[winsdk.windows.media.VideoFrame]
    kind: LearningModelFeatureKind
    @staticmethod
    def _from(obj: _winrt.Object) -> ImageFeatureValue: ...
    @staticmethod
    def create_from_video_frame(image: typing.Optional[winsdk.windows.media.VideoFrame]) -> typing.Optional[ImageFeatureValue]: ...

class LearningModel(_winrt.Object):
    author: str
    description: str
    domain: str
    input_features: typing.Optional[winsdk.windows.foundation.collections.IVectorView[ILearningModelFeatureDescriptor]]
    metadata: typing.Optional[winsdk.windows.foundation.collections.IMapView[str, str]]
    name: str
    output_features: typing.Optional[winsdk.windows.foundation.collections.IVectorView[ILearningModelFeatureDescriptor]]
    version: _winrt.Int64
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> LearningModel: ...
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def load_from_file_path(file_path: str) -> typing.Optional[LearningModel]: ...
    @typing.overload
    @staticmethod
    def load_from_file_path(file_path: str, operator_provider: typing.Optional[ILearningModelOperatorProvider]) -> typing.Optional[LearningModel]: ...
    @typing.overload
    @staticmethod
    def load_from_storage_file_async(model_file: typing.Optional[winsdk.windows.storage.IStorageFile]) -> winsdk.windows.foundation.IAsyncOperation[LearningModel]: ...
    @typing.overload
    @staticmethod
    def load_from_storage_file_async(model_file: typing.Optional[winsdk.windows.storage.IStorageFile], operator_provider: typing.Optional[ILearningModelOperatorProvider]) -> winsdk.windows.foundation.IAsyncOperation[LearningModel]: ...
    @typing.overload
    @staticmethod
    def load_from_stream(model_stream: typing.Optional[winsdk.windows.storage.streams.IRandomAccessStreamReference]) -> typing.Optional[LearningModel]: ...
    @typing.overload
    @staticmethod
    def load_from_stream(model_stream: typing.Optional[winsdk.windows.storage.streams.IRandomAccessStreamReference], operator_provider: typing.Optional[ILearningModelOperatorProvider]) -> typing.Optional[LearningModel]: ...
    @typing.overload
    @staticmethod
    def load_from_stream_async(model_stream: typing.Optional[winsdk.windows.storage.streams.IRandomAccessStreamReference]) -> winsdk.windows.foundation.IAsyncOperation[LearningModel]: ...
    @typing.overload
    @staticmethod
    def load_from_stream_async(model_stream: typing.Optional[winsdk.windows.storage.streams.IRandomAccessStreamReference], operator_provider: typing.Optional[ILearningModelOperatorProvider]) -> winsdk.windows.foundation.IAsyncOperation[LearningModel]: ...

class LearningModelBinding(_winrt.Object, typing.Mapping[str, _winrt.Object]):
    size: _winrt.UInt32
    def __len__(self) -> int: ...
    def __iter__(self) -> typing.Iterator[str]: ...
    def __contains__(self, key: object) -> bool:...
    def __getitem__(self, key: str) -> _winrt.Object: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> LearningModelBinding: ...
    def __init__(self, session: typing.Optional[LearningModelSession]) -> None: ...
    @typing.overload
    def bind(self, name: str, value: typing.Optional[_winrt.Object]) -> None: ...
    @typing.overload
    def bind(self, name: str, value: typing.Optional[_winrt.Object], props: typing.Optional[winsdk.windows.foundation.collections.IPropertySet]) -> None: ...
    def clear(self) -> None: ...
    def first(self) -> typing.Optional[winsdk.windows.foundation.collections.IIterator[winsdk.windows.foundation.collections.IKeyValuePair[str, _winrt.Object]]]: ...
    def has_key(self, key: str) -> _winrt.Boolean: ...
    def lookup(self, key: str) -> typing.Optional[_winrt.Object]: ...
    def split(self) -> typing.Tuple[typing.Optional[winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]], typing.Optional[winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]]]: ...

class LearningModelDevice(_winrt.Object):
    adapter_id: winsdk.windows.graphics.DisplayAdapterId
    direct3_d11_device: typing.Optional[winsdk.windows.graphics.directx.direct3d11.IDirect3DDevice]
    @staticmethod
    def _from(obj: _winrt.Object) -> LearningModelDevice: ...
    def __init__(self, device_kind: LearningModelDeviceKind) -> None: ...
    @staticmethod
    def create_from_direct3_d11_device(device: typing.Optional[winsdk.windows.graphics.directx.direct3d11.IDirect3DDevice]) -> typing.Optional[LearningModelDevice]: ...

class LearningModelEvaluationResult(_winrt.Object):
    correlation_id: str
    error_status: _winrt.Int32
    outputs: typing.Optional[winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]]
    succeeded: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> LearningModelEvaluationResult: ...

class LearningModelSession(_winrt.Object):
    device: typing.Optional[LearningModelDevice]
    evaluation_properties: typing.Optional[winsdk.windows.foundation.collections.IPropertySet]
    model: typing.Optional[LearningModel]
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> LearningModelSession: ...
    @typing.overload
    def __init__(self, model: typing.Optional[LearningModel], device_to_run_on: typing.Optional[LearningModelDevice], learning_model_session_options: typing.Optional[LearningModelSessionOptions]) -> None: ...
    @typing.overload
    def __init__(self, model: typing.Optional[LearningModel]) -> None: ...
    @typing.overload
    def __init__(self, model: typing.Optional[LearningModel], device_to_run_on: typing.Optional[LearningModelDevice]) -> None: ...
    def close(self) -> None: ...
    def evaluate(self, bindings: typing.Optional[LearningModelBinding], correlation_id: str) -> typing.Optional[LearningModelEvaluationResult]: ...
    def evaluate_async(self, bindings: typing.Optional[LearningModelBinding], correlation_id: str) -> winsdk.windows.foundation.IAsyncOperation[LearningModelEvaluationResult]: ...
    def evaluate_features(self, features: winsdk.windows.foundation.collections.IMap[str, _winrt.Object], correlation_id: str) -> typing.Optional[LearningModelEvaluationResult]: ...
    def evaluate_features_async(self, features: winsdk.windows.foundation.collections.IMap[str, _winrt.Object], correlation_id: str) -> winsdk.windows.foundation.IAsyncOperation[LearningModelEvaluationResult]: ...

class LearningModelSessionOptions(_winrt.Object):
    batch_size_override: _winrt.UInt32
    close_model_on_session_creation: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> LearningModelSessionOptions: ...
    def __init__(self) -> None: ...
    def override_named_dimension(self, name: str, dimension: _winrt.UInt32) -> None: ...

class MapFeatureDescriptor(_winrt.Object):
    description: str
    is_required: _winrt.Boolean
    kind: LearningModelFeatureKind
    name: str
    key_kind: TensorKind
    value_descriptor: typing.Optional[ILearningModelFeatureDescriptor]
    @staticmethod
    def _from(obj: _winrt.Object) -> MapFeatureDescriptor: ...

class SequenceFeatureDescriptor(_winrt.Object):
    description: str
    is_required: _winrt.Boolean
    kind: LearningModelFeatureKind
    name: str
    element_descriptor: typing.Optional[ILearningModelFeatureDescriptor]
    @staticmethod
    def _from(obj: _winrt.Object) -> SequenceFeatureDescriptor: ...

class TensorBoolean(_winrt.Object):
    kind: LearningModelFeatureKind
    shape: typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int64]]
    tensor_kind: TensorKind
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> TensorBoolean: ...
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def create() -> typing.Optional[TensorBoolean]: ...
    @typing.overload
    @staticmethod
    def create(shape: typing.Iterable[_winrt.Int64]) -> typing.Optional[TensorBoolean]: ...
    @staticmethod
    def create_from_array(shape: typing.Iterable[_winrt.Int64], data: typing.Sequence[_winrt.Boolean]) -> typing.Optional[TensorBoolean]: ...
    @staticmethod
    def create_from_buffer(shape: typing.Sequence[_winrt.Int64], buffer: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> typing.Optional[TensorBoolean]: ...
    @staticmethod
    def create_from_iterable(shape: typing.Iterable[_winrt.Int64], data: typing.Iterable[_winrt.Boolean]) -> typing.Optional[TensorBoolean]: ...
    @staticmethod
    def create_from_shape_array_and_data_array(shape: typing.Sequence[_winrt.Int64], data: typing.Sequence[_winrt.Boolean]) -> typing.Optional[TensorBoolean]: ...
    def create_reference(self) -> typing.Optional[winsdk.windows.foundation.IMemoryBufferReference]: ...
    def get_as_vector_view(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Boolean]]: ...

class TensorDouble(_winrt.Object):
    kind: LearningModelFeatureKind
    shape: typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int64]]
    tensor_kind: TensorKind
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> TensorDouble: ...
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def create() -> typing.Optional[TensorDouble]: ...
    @typing.overload
    @staticmethod
    def create(shape: typing.Iterable[_winrt.Int64]) -> typing.Optional[TensorDouble]: ...
    @staticmethod
    def create_from_array(shape: typing.Iterable[_winrt.Int64], data: typing.Sequence[_winrt.Double]) -> typing.Optional[TensorDouble]: ...
    @staticmethod
    def create_from_buffer(shape: typing.Sequence[_winrt.Int64], buffer: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> typing.Optional[TensorDouble]: ...
    @staticmethod
    def create_from_iterable(shape: typing.Iterable[_winrt.Int64], data: typing.Iterable[_winrt.Double]) -> typing.Optional[TensorDouble]: ...
    @staticmethod
    def create_from_shape_array_and_data_array(shape: typing.Sequence[_winrt.Int64], data: typing.Sequence[_winrt.Double]) -> typing.Optional[TensorDouble]: ...
    def create_reference(self) -> typing.Optional[winsdk.windows.foundation.IMemoryBufferReference]: ...
    def get_as_vector_view(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Double]]: ...

class TensorFeatureDescriptor(_winrt.Object):
    description: str
    is_required: _winrt.Boolean
    kind: LearningModelFeatureKind
    name: str
    shape: typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int64]]
    tensor_kind: TensorKind
    @staticmethod
    def _from(obj: _winrt.Object) -> TensorFeatureDescriptor: ...

class TensorFloat(_winrt.Object):
    kind: LearningModelFeatureKind
    shape: typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int64]]
    tensor_kind: TensorKind
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> TensorFloat: ...
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def create() -> typing.Optional[TensorFloat]: ...
    @typing.overload
    @staticmethod
    def create(shape: typing.Iterable[_winrt.Int64]) -> typing.Optional[TensorFloat]: ...
    @staticmethod
    def create_from_array(shape: typing.Iterable[_winrt.Int64], data: typing.Sequence[_winrt.Single]) -> typing.Optional[TensorFloat]: ...
    @staticmethod
    def create_from_buffer(shape: typing.Sequence[_winrt.Int64], buffer: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> typing.Optional[TensorFloat]: ...
    @staticmethod
    def create_from_iterable(shape: typing.Iterable[_winrt.Int64], data: typing.Iterable[_winrt.Single]) -> typing.Optional[TensorFloat]: ...
    @staticmethod
    def create_from_shape_array_and_data_array(shape: typing.Sequence[_winrt.Int64], data: typing.Sequence[_winrt.Single]) -> typing.Optional[TensorFloat]: ...
    def create_reference(self) -> typing.Optional[winsdk.windows.foundation.IMemoryBufferReference]: ...
    def get_as_vector_view(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Single]]: ...

class TensorFloat16Bit(_winrt.Object):
    kind: LearningModelFeatureKind
    shape: typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int64]]
    tensor_kind: TensorKind
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> TensorFloat16Bit: ...
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def create() -> typing.Optional[TensorFloat16Bit]: ...
    @typing.overload
    @staticmethod
    def create(shape: typing.Iterable[_winrt.Int64]) -> typing.Optional[TensorFloat16Bit]: ...
    @staticmethod
    def create_from_array(shape: typing.Iterable[_winrt.Int64], data: typing.Sequence[_winrt.Single]) -> typing.Optional[TensorFloat16Bit]: ...
    @staticmethod
    def create_from_buffer(shape: typing.Sequence[_winrt.Int64], buffer: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> typing.Optional[TensorFloat16Bit]: ...
    @staticmethod
    def create_from_iterable(shape: typing.Iterable[_winrt.Int64], data: typing.Iterable[_winrt.Single]) -> typing.Optional[TensorFloat16Bit]: ...
    @staticmethod
    def create_from_shape_array_and_data_array(shape: typing.Sequence[_winrt.Int64], data: typing.Sequence[_winrt.Single]) -> typing.Optional[TensorFloat16Bit]: ...
    def create_reference(self) -> typing.Optional[winsdk.windows.foundation.IMemoryBufferReference]: ...
    def get_as_vector_view(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Single]]: ...

class TensorInt16Bit(_winrt.Object):
    kind: LearningModelFeatureKind
    shape: typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int64]]
    tensor_kind: TensorKind
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> TensorInt16Bit: ...
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def create() -> typing.Optional[TensorInt16Bit]: ...
    @typing.overload
    @staticmethod
    def create(shape: typing.Iterable[_winrt.Int64]) -> typing.Optional[TensorInt16Bit]: ...
    @staticmethod
    def create_from_array(shape: typing.Iterable[_winrt.Int64], data: typing.Sequence[_winrt.Int16]) -> typing.Optional[TensorInt16Bit]: ...
    @staticmethod
    def create_from_buffer(shape: typing.Sequence[_winrt.Int64], buffer: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> typing.Optional[TensorInt16Bit]: ...
    @staticmethod
    def create_from_iterable(shape: typing.Iterable[_winrt.Int64], data: typing.Iterable[_winrt.Int16]) -> typing.Optional[TensorInt16Bit]: ...
    @staticmethod
    def create_from_shape_array_and_data_array(shape: typing.Sequence[_winrt.Int64], data: typing.Sequence[_winrt.Int16]) -> typing.Optional[TensorInt16Bit]: ...
    def create_reference(self) -> typing.Optional[winsdk.windows.foundation.IMemoryBufferReference]: ...
    def get_as_vector_view(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int16]]: ...

class TensorInt32Bit(_winrt.Object):
    kind: LearningModelFeatureKind
    shape: typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int64]]
    tensor_kind: TensorKind
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> TensorInt32Bit: ...
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def create() -> typing.Optional[TensorInt32Bit]: ...
    @typing.overload
    @staticmethod
    def create(shape: typing.Iterable[_winrt.Int64]) -> typing.Optional[TensorInt32Bit]: ...
    @staticmethod
    def create_from_array(shape: typing.Iterable[_winrt.Int64], data: typing.Sequence[_winrt.Int32]) -> typing.Optional[TensorInt32Bit]: ...
    @staticmethod
    def create_from_buffer(shape: typing.Sequence[_winrt.Int64], buffer: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> typing.Optional[TensorInt32Bit]: ...
    @staticmethod
    def create_from_iterable(shape: typing.Iterable[_winrt.Int64], data: typing.Iterable[_winrt.Int32]) -> typing.Optional[TensorInt32Bit]: ...
    @staticmethod
    def create_from_shape_array_and_data_array(shape: typing.Sequence[_winrt.Int64], data: typing.Sequence[_winrt.Int32]) -> typing.Optional[TensorInt32Bit]: ...
    def create_reference(self) -> typing.Optional[winsdk.windows.foundation.IMemoryBufferReference]: ...
    def get_as_vector_view(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int32]]: ...

class TensorInt64Bit(_winrt.Object):
    kind: LearningModelFeatureKind
    shape: typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int64]]
    tensor_kind: TensorKind
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> TensorInt64Bit: ...
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def create() -> typing.Optional[TensorInt64Bit]: ...
    @typing.overload
    @staticmethod
    def create(shape: typing.Iterable[_winrt.Int64]) -> typing.Optional[TensorInt64Bit]: ...
    @staticmethod
    def create_from_array(shape: typing.Iterable[_winrt.Int64], data: typing.Sequence[_winrt.Int64]) -> typing.Optional[TensorInt64Bit]: ...
    @staticmethod
    def create_from_buffer(shape: typing.Sequence[_winrt.Int64], buffer: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> typing.Optional[TensorInt64Bit]: ...
    @staticmethod
    def create_from_iterable(shape: typing.Iterable[_winrt.Int64], data: typing.Iterable[_winrt.Int64]) -> typing.Optional[TensorInt64Bit]: ...
    @staticmethod
    def create_from_shape_array_and_data_array(shape: typing.Sequence[_winrt.Int64], data: typing.Sequence[_winrt.Int64]) -> typing.Optional[TensorInt64Bit]: ...
    def create_reference(self) -> typing.Optional[winsdk.windows.foundation.IMemoryBufferReference]: ...
    def get_as_vector_view(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int64]]: ...

class TensorInt8Bit(_winrt.Object):
    kind: LearningModelFeatureKind
    shape: typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int64]]
    tensor_kind: TensorKind
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> TensorInt8Bit: ...
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def create() -> typing.Optional[TensorInt8Bit]: ...
    @typing.overload
    @staticmethod
    def create(shape: typing.Iterable[_winrt.Int64]) -> typing.Optional[TensorInt8Bit]: ...
    @staticmethod
    def create_from_array(shape: typing.Iterable[_winrt.Int64], data: typing.Sequence[_winrt.UInt8]) -> typing.Optional[TensorInt8Bit]: ...
    @staticmethod
    def create_from_buffer(shape: typing.Sequence[_winrt.Int64], buffer: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> typing.Optional[TensorInt8Bit]: ...
    @staticmethod
    def create_from_iterable(shape: typing.Iterable[_winrt.Int64], data: typing.Iterable[_winrt.UInt8]) -> typing.Optional[TensorInt8Bit]: ...
    @staticmethod
    def create_from_shape_array_and_data_array(shape: typing.Sequence[_winrt.Int64], data: typing.Sequence[_winrt.UInt8]) -> typing.Optional[TensorInt8Bit]: ...
    def create_reference(self) -> typing.Optional[winsdk.windows.foundation.IMemoryBufferReference]: ...
    def get_as_vector_view(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.UInt8]]: ...

class TensorString(_winrt.Object):
    kind: LearningModelFeatureKind
    shape: typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int64]]
    tensor_kind: TensorKind
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> TensorString: ...
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def create() -> typing.Optional[TensorString]: ...
    @typing.overload
    @staticmethod
    def create(shape: typing.Iterable[_winrt.Int64]) -> typing.Optional[TensorString]: ...
    @staticmethod
    def create_from_array(shape: typing.Iterable[_winrt.Int64], data: typing.Sequence[str]) -> typing.Optional[TensorString]: ...
    @staticmethod
    def create_from_iterable(shape: typing.Iterable[_winrt.Int64], data: typing.Iterable[str]) -> typing.Optional[TensorString]: ...
    @staticmethod
    def create_from_shape_array_and_data_array(shape: typing.Sequence[_winrt.Int64], data: typing.Sequence[str]) -> typing.Optional[TensorString]: ...
    def create_reference(self) -> typing.Optional[winsdk.windows.foundation.IMemoryBufferReference]: ...
    def get_as_vector_view(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[str]]: ...

class TensorUInt16Bit(_winrt.Object):
    kind: LearningModelFeatureKind
    shape: typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int64]]
    tensor_kind: TensorKind
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> TensorUInt16Bit: ...
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def create() -> typing.Optional[TensorUInt16Bit]: ...
    @typing.overload
    @staticmethod
    def create(shape: typing.Iterable[_winrt.Int64]) -> typing.Optional[TensorUInt16Bit]: ...
    @staticmethod
    def create_from_array(shape: typing.Iterable[_winrt.Int64], data: typing.Sequence[_winrt.UInt16]) -> typing.Optional[TensorUInt16Bit]: ...
    @staticmethod
    def create_from_buffer(shape: typing.Sequence[_winrt.Int64], buffer: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> typing.Optional[TensorUInt16Bit]: ...
    @staticmethod
    def create_from_iterable(shape: typing.Iterable[_winrt.Int64], data: typing.Iterable[_winrt.UInt16]) -> typing.Optional[TensorUInt16Bit]: ...
    @staticmethod
    def create_from_shape_array_and_data_array(shape: typing.Sequence[_winrt.Int64], data: typing.Sequence[_winrt.UInt16]) -> typing.Optional[TensorUInt16Bit]: ...
    def create_reference(self) -> typing.Optional[winsdk.windows.foundation.IMemoryBufferReference]: ...
    def get_as_vector_view(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.UInt16]]: ...

class TensorUInt32Bit(_winrt.Object):
    kind: LearningModelFeatureKind
    shape: typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int64]]
    tensor_kind: TensorKind
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> TensorUInt32Bit: ...
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def create() -> typing.Optional[TensorUInt32Bit]: ...
    @typing.overload
    @staticmethod
    def create(shape: typing.Iterable[_winrt.Int64]) -> typing.Optional[TensorUInt32Bit]: ...
    @staticmethod
    def create_from_array(shape: typing.Iterable[_winrt.Int64], data: typing.Sequence[_winrt.UInt32]) -> typing.Optional[TensorUInt32Bit]: ...
    @staticmethod
    def create_from_buffer(shape: typing.Sequence[_winrt.Int64], buffer: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> typing.Optional[TensorUInt32Bit]: ...
    @staticmethod
    def create_from_iterable(shape: typing.Iterable[_winrt.Int64], data: typing.Iterable[_winrt.UInt32]) -> typing.Optional[TensorUInt32Bit]: ...
    @staticmethod
    def create_from_shape_array_and_data_array(shape: typing.Sequence[_winrt.Int64], data: typing.Sequence[_winrt.UInt32]) -> typing.Optional[TensorUInt32Bit]: ...
    def create_reference(self) -> typing.Optional[winsdk.windows.foundation.IMemoryBufferReference]: ...
    def get_as_vector_view(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.UInt32]]: ...

class TensorUInt64Bit(_winrt.Object):
    kind: LearningModelFeatureKind
    shape: typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int64]]
    tensor_kind: TensorKind
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> TensorUInt64Bit: ...
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def create() -> typing.Optional[TensorUInt64Bit]: ...
    @typing.overload
    @staticmethod
    def create(shape: typing.Iterable[_winrt.Int64]) -> typing.Optional[TensorUInt64Bit]: ...
    @staticmethod
    def create_from_array(shape: typing.Iterable[_winrt.Int64], data: typing.Sequence[_winrt.UInt64]) -> typing.Optional[TensorUInt64Bit]: ...
    @staticmethod
    def create_from_buffer(shape: typing.Sequence[_winrt.Int64], buffer: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> typing.Optional[TensorUInt64Bit]: ...
    @staticmethod
    def create_from_iterable(shape: typing.Iterable[_winrt.Int64], data: typing.Iterable[_winrt.UInt64]) -> typing.Optional[TensorUInt64Bit]: ...
    @staticmethod
    def create_from_shape_array_and_data_array(shape: typing.Sequence[_winrt.Int64], data: typing.Sequence[_winrt.UInt64]) -> typing.Optional[TensorUInt64Bit]: ...
    def create_reference(self) -> typing.Optional[winsdk.windows.foundation.IMemoryBufferReference]: ...
    def get_as_vector_view(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.UInt64]]: ...

class TensorUInt8Bit(_winrt.Object):
    kind: LearningModelFeatureKind
    shape: typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int64]]
    tensor_kind: TensorKind
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> TensorUInt8Bit: ...
    def close(self) -> None: ...
    @typing.overload
    @staticmethod
    def create() -> typing.Optional[TensorUInt8Bit]: ...
    @typing.overload
    @staticmethod
    def create(shape: typing.Iterable[_winrt.Int64]) -> typing.Optional[TensorUInt8Bit]: ...
    @staticmethod
    def create_from_array(shape: typing.Iterable[_winrt.Int64], data: typing.Sequence[_winrt.UInt8]) -> typing.Optional[TensorUInt8Bit]: ...
    @staticmethod
    def create_from_buffer(shape: typing.Sequence[_winrt.Int64], buffer: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> typing.Optional[TensorUInt8Bit]: ...
    @staticmethod
    def create_from_iterable(shape: typing.Iterable[_winrt.Int64], data: typing.Iterable[_winrt.UInt8]) -> typing.Optional[TensorUInt8Bit]: ...
    @staticmethod
    def create_from_shape_array_and_data_array(shape: typing.Sequence[_winrt.Int64], data: typing.Sequence[_winrt.UInt8]) -> typing.Optional[TensorUInt8Bit]: ...
    def create_reference(self) -> typing.Optional[winsdk.windows.foundation.IMemoryBufferReference]: ...
    def get_as_vector_view(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.UInt8]]: ...

class ILearningModelFeatureDescriptor(_winrt.Object):
    description: str
    is_required: _winrt.Boolean
    kind: LearningModelFeatureKind
    name: str
    @staticmethod
    def _from(obj: _winrt.Object) -> ILearningModelFeatureDescriptor: ...

class ILearningModelFeatureValue(_winrt.Object):
    kind: LearningModelFeatureKind
    @staticmethod
    def _from(obj: _winrt.Object) -> ILearningModelFeatureValue: ...

class ILearningModelOperatorProvider(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> ILearningModelOperatorProvider: ...

class ITensor(_winrt.Object):
    shape: typing.Optional[winsdk.windows.foundation.collections.IVectorView[_winrt.Int64]]
    tensor_kind: TensorKind
    kind: LearningModelFeatureKind
    @staticmethod
    def _from(obj: _winrt.Object) -> ITensor: ...

