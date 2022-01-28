# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.foundation
except Exception:
    pass

class PerceptionTimestamp(_winrt.Object):
    ...
    prediction_amount: winsdk.windows.foundation.TimeSpan
    target_time: winsdk.windows.foundation.DateTime
    system_relative_target_time: winsdk.windows.foundation.TimeSpan

class PerceptionTimestampHelper(_winrt.Object):
    ...
    def from_historical_target_time(target_time: winsdk.windows.foundation.DateTime) -> PerceptionTimestamp:
        ...
    def from_system_relative_target_time(target_time: winsdk.windows.foundation.TimeSpan) -> PerceptionTimestamp:
        ...
