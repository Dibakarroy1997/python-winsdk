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

class PhoneCallBlockedReason(enum.IntEnum):
    IN_CALL_BLOCKING_LIST = 0
    PRIVATE_NUMBER = 1
    UNKNOWN_NUMBER = 2

class PhoneIncomingCallDismissedReason(enum.IntEnum):
    UNKNOWN = 0
    CALL_REJECTED = 1
    TEXT_REPLY = 2
    CONNECTION_LOST = 3

class PhoneLineChangeKind(enum.IntEnum):
    ADDED = 0
    REMOVED = 1
    PROPERTIES_CHANGED = 2

class PhoneLineProperties(enum.IntFlag):
    NONE = 0
    BRANDING_OPTIONS = 0x1
    CAN_DIAL = 0x2
    CELLULAR_DETAILS = 0x4
    DISPLAY_COLOR = 0x8
    DISPLAY_NAME = 0x10
    NETWORK_NAME = 0x20
    NETWORK_STATE = 0x40
    TRANSPORT = 0x80
    VOICEMAIL = 0x100

class PhoneTriggerType(enum.IntEnum):
    NEW_VOICEMAIL_MESSAGE = 0
    CALL_HISTORY_CHANGED = 1
    LINE_CHANGED = 2
    AIRPLANE_MODE_DISABLED_FOR_EMERGENCY_CALL = 3
    CALL_ORIGIN_DATA_REQUEST = 4
    CALL_BLOCKED = 5
    INCOMING_CALL_DISMISSED = 6
    INCOMING_CALL_NOTIFICATION = 7

class PhoneCallBlockedTriggerDetails(_winrt.Object):
    ...
    call_blocked_reason: PhoneCallBlockedReason
    line_id: uuid.UUID
    phone_number: str

class PhoneCallOriginDataRequestTriggerDetails(_winrt.Object):
    ...
    phone_number: str
    request_id: uuid.UUID

class PhoneIncomingCallDismissedTriggerDetails(_winrt.Object):
    ...
    dismissal_time: winsdk.windows.foundation.DateTime
    display_name: str
    line_id: uuid.UUID
    phone_number: str
    reason: PhoneIncomingCallDismissedReason
    text_reply_message: str

class PhoneIncomingCallNotificationTriggerDetails(_winrt.Object):
    ...
    call_id: str
    line_id: uuid.UUID

class PhoneLineChangedTriggerDetails(_winrt.Object):
    ...
    change_type: PhoneLineChangeKind
    line_id: uuid.UUID
    def has_line_property_changed(line_property: PhoneLineProperties) -> _winrt.Boolean:
        ...

class PhoneNewVoicemailMessageTriggerDetails(_winrt.Object):
    ...
    line_id: uuid.UUID
    operator_message: str
    voicemail_count: _winrt.Int32
