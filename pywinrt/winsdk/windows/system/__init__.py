# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.System")

try:
    import winsdk.windows.applicationmodel
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
    import winsdk.windows.storage
except Exception:
    pass

try:
    import winsdk.windows.storage.search
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

try:
    import winsdk.windows.system.diagnostics
except Exception:
    pass

try:
    import winsdk.windows.system.remotesystems
except Exception:
    pass

try:
    import winsdk.windows.ui.popups
except Exception:
    pass

try:
    import winsdk.windows.ui.viewmanagement
except Exception:
    pass

class AppDiagnosticInfoWatcherStatus(enum.IntEnum):
    CREATED = 0
    STARTED = 1
    ENUMERATION_COMPLETED = 2
    STOPPING = 3
    STOPPED = 4
    ABORTED = 5

class AppMemoryUsageLevel(enum.IntEnum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    OVER_LIMIT = 3

class AppResourceGroupEnergyQuotaState(enum.IntEnum):
    UNKNOWN = 0
    OVER = 1
    UNDER = 2

class AppResourceGroupExecutionState(enum.IntEnum):
    UNKNOWN = 0
    RUNNING = 1
    SUSPENDING = 2
    SUSPENDED = 3
    NOT_RUNNING = 4

class AppResourceGroupInfoWatcherStatus(enum.IntEnum):
    CREATED = 0
    STARTED = 1
    ENUMERATION_COMPLETED = 2
    STOPPING = 3
    STOPPED = 4
    ABORTED = 5

class AutoUpdateTimeZoneStatus(enum.IntEnum):
    ATTEMPTED = 0
    TIMED_OUT = 1
    FAILED = 2

class DiagnosticAccessStatus(enum.IntEnum):
    UNSPECIFIED = 0
    DENIED = 1
    LIMITED = 2
    ALLOWED = 3

class DispatcherQueuePriority(enum.IntEnum):
    LOW = -10
    NORMAL = 0
    HIGH = 10

class LaunchFileStatus(enum.IntEnum):
    SUCCESS = 0
    APP_UNAVAILABLE = 1
    DENIED_BY_POLICY = 2
    FILE_TYPE_NOT_SUPPORTED = 3
    UNKNOWN = 4

class LaunchQuerySupportStatus(enum.IntEnum):
    AVAILABLE = 0
    APP_NOT_INSTALLED = 1
    APP_UNAVAILABLE = 2
    NOT_SUPPORTED = 3
    UNKNOWN = 4

class LaunchQuerySupportType(enum.IntEnum):
    URI = 0
    URI_FOR_RESULTS = 1

class LaunchUriStatus(enum.IntEnum):
    SUCCESS = 0
    APP_UNAVAILABLE = 1
    PROTOCOL_UNAVAILABLE = 2
    UNKNOWN = 3

class PowerState(enum.IntEnum):
    CONNECTED_STANDBY = 0
    SLEEP_S3 = 1

class ProcessorArchitecture(enum.IntEnum):
    X86 = 0
    ARM = 5
    X64 = 9
    NEUTRAL = 11
    ARM64 = 12
    X86_ON_ARM64 = 14
    UNKNOWN = 65535

class RemoteLaunchUriStatus(enum.IntEnum):
    UNKNOWN = 0
    SUCCESS = 1
    APP_UNAVAILABLE = 2
    PROTOCOL_UNAVAILABLE = 3
    REMOTE_SYSTEM_UNAVAILABLE = 4
    VALUE_SET_TOO_LARGE = 5
    DENIED_BY_LOCAL_SYSTEM = 6
    DENIED_BY_REMOTE_SYSTEM = 7

class ShutdownKind(enum.IntEnum):
    SHUTDOWN = 0
    RESTART = 1

class UserAgeConsentGroup(enum.IntEnum):
    CHILD = 0
    MINOR = 1
    ADULT = 2

class UserAgeConsentResult(enum.IntEnum):
    NOT_ENFORCED = 0
    INCLUDED = 1
    NOT_INCLUDED = 2
    UNKNOWN = 3
    AMBIGUOUS = 4

class UserAuthenticationStatus(enum.IntEnum):
    UNAUTHENTICATED = 0
    LOCALLY_AUTHENTICATED = 1
    REMOTELY_AUTHENTICATED = 2

class UserPictureSize(enum.IntEnum):
    SIZE64X64 = 0
    SIZE208X208 = 1
    SIZE424X424 = 2
    SIZE1080X1080 = 3

class UserType(enum.IntEnum):
    LOCAL_USER = 0
    REMOTE_USER = 1
    LOCAL_GUEST = 2
    REMOTE_GUEST = 3
    SYSTEM_MANAGED = 4

class UserWatcherStatus(enum.IntEnum):
    CREATED = 0
    STARTED = 1
    ENUMERATION_COMPLETED = 2
    STOPPING = 3
    STOPPED = 4
    ABORTED = 5

class UserWatcherUpdateKind(enum.IntEnum):
    PROPERTIES = 0
    PICTURE = 1

class VirtualKey(enum.IntEnum):
    NONE = 0
    LEFT_BUTTON = 1
    RIGHT_BUTTON = 2
    CANCEL = 3
    MIDDLE_BUTTON = 4
    X_BUTTON1 = 5
    X_BUTTON2 = 6
    BACK = 8
    TAB = 9
    CLEAR = 12
    ENTER = 13
    SHIFT = 16
    CONTROL = 17
    MENU = 18
    PAUSE = 19
    CAPITAL_LOCK = 20
    KANA = 21
    HANGUL = 21
    IME_ON = 22
    JUNJA = 23
    FINAL = 24
    HANJA = 25
    KANJI = 25
    IME_OFF = 26
    ESCAPE = 27
    CONVERT = 28
    NON_CONVERT = 29
    ACCEPT = 30
    MODE_CHANGE = 31
    SPACE = 32
    PAGE_UP = 33
    PAGE_DOWN = 34
    END = 35
    HOME = 36
    LEFT = 37
    UP = 38
    RIGHT = 39
    DOWN = 40
    SELECT = 41
    PRINT = 42
    EXECUTE = 43
    SNAPSHOT = 44
    INSERT = 45
    DELETE = 46
    HELP = 47
    NUMBER0 = 48
    NUMBER1 = 49
    NUMBER2 = 50
    NUMBER3 = 51
    NUMBER4 = 52
    NUMBER5 = 53
    NUMBER6 = 54
    NUMBER7 = 55
    NUMBER8 = 56
    NUMBER9 = 57
    A = 65
    B = 66
    C = 67
    D = 68
    E = 69
    F = 70
    G = 71
    H = 72
    I = 73
    J = 74
    K = 75
    L = 76
    M = 77
    N = 78
    O = 79
    P = 80
    Q = 81
    R = 82
    S = 83
    T = 84
    U = 85
    V = 86
    W = 87
    X = 88
    Y = 89
    Z = 90
    LEFT_WINDOWS = 91
    RIGHT_WINDOWS = 92
    APPLICATION = 93
    SLEEP = 95
    NUMBER_PAD0 = 96
    NUMBER_PAD1 = 97
    NUMBER_PAD2 = 98
    NUMBER_PAD3 = 99
    NUMBER_PAD4 = 100
    NUMBER_PAD5 = 101
    NUMBER_PAD6 = 102
    NUMBER_PAD7 = 103
    NUMBER_PAD8 = 104
    NUMBER_PAD9 = 105
    MULTIPLY = 106
    ADD = 107
    SEPARATOR = 108
    SUBTRACT = 109
    DECIMAL = 110
    DIVIDE = 111
    F1 = 112
    F2 = 113
    F3 = 114
    F4 = 115
    F5 = 116
    F6 = 117
    F7 = 118
    F8 = 119
    F9 = 120
    F10 = 121
    F11 = 122
    F12 = 123
    F13 = 124
    F14 = 125
    F15 = 126
    F16 = 127
    F17 = 128
    F18 = 129
    F19 = 130
    F20 = 131
    F21 = 132
    F22 = 133
    F23 = 134
    F24 = 135
    NAVIGATION_VIEW = 136
    NAVIGATION_MENU = 137
    NAVIGATION_UP = 138
    NAVIGATION_DOWN = 139
    NAVIGATION_LEFT = 140
    NAVIGATION_RIGHT = 141
    NAVIGATION_ACCEPT = 142
    NAVIGATION_CANCEL = 143
    NUMBER_KEY_LOCK = 144
    SCROLL = 145
    LEFT_SHIFT = 160
    RIGHT_SHIFT = 161
    LEFT_CONTROL = 162
    RIGHT_CONTROL = 163
    LEFT_MENU = 164
    RIGHT_MENU = 165
    GO_BACK = 166
    GO_FORWARD = 167
    REFRESH = 168
    STOP = 169
    SEARCH = 170
    FAVORITES = 171
    GO_HOME = 172
    GAMEPAD_A = 195
    GAMEPAD_B = 196
    GAMEPAD_X = 197
    GAMEPAD_Y = 198
    GAMEPAD_RIGHT_SHOULDER = 199
    GAMEPAD_LEFT_SHOULDER = 200
    GAMEPAD_LEFT_TRIGGER = 201
    GAMEPAD_RIGHT_TRIGGER = 202
    GAMEPAD_D_PAD_UP = 203
    GAMEPAD_D_PAD_DOWN = 204
    GAMEPAD_D_PAD_LEFT = 205
    GAMEPAD_D_PAD_RIGHT = 206
    GAMEPAD_MENU = 207
    GAMEPAD_VIEW = 208
    GAMEPAD_LEFT_THUMBSTICK_BUTTON = 209
    GAMEPAD_RIGHT_THUMBSTICK_BUTTON = 210
    GAMEPAD_LEFT_THUMBSTICK_UP = 211
    GAMEPAD_LEFT_THUMBSTICK_DOWN = 212
    GAMEPAD_LEFT_THUMBSTICK_RIGHT = 213
    GAMEPAD_LEFT_THUMBSTICK_LEFT = 214
    GAMEPAD_RIGHT_THUMBSTICK_UP = 215
    GAMEPAD_RIGHT_THUMBSTICK_DOWN = 216
    GAMEPAD_RIGHT_THUMBSTICK_RIGHT = 217
    GAMEPAD_RIGHT_THUMBSTICK_LEFT = 218

class VirtualKeyModifiers(enum.IntFlag):
    NONE = 0
    CONTROL = 0x1
    MENU = 0x2
    SHIFT = 0x4
    WINDOWS = 0x8

AppActivationResult = _ns_module.AppActivationResult
AppDiagnosticInfo = _ns_module.AppDiagnosticInfo
AppDiagnosticInfoWatcher = _ns_module.AppDiagnosticInfoWatcher
AppDiagnosticInfoWatcherEventArgs = _ns_module.AppDiagnosticInfoWatcherEventArgs
AppExecutionStateChangeResult = _ns_module.AppExecutionStateChangeResult
AppMemoryReport = _ns_module.AppMemoryReport
AppMemoryUsageLimitChangingEventArgs = _ns_module.AppMemoryUsageLimitChangingEventArgs
AppResourceGroupBackgroundTaskReport = _ns_module.AppResourceGroupBackgroundTaskReport
AppResourceGroupInfo = _ns_module.AppResourceGroupInfo
AppResourceGroupInfoWatcher = _ns_module.AppResourceGroupInfoWatcher
AppResourceGroupInfoWatcherEventArgs = _ns_module.AppResourceGroupInfoWatcherEventArgs
AppResourceGroupInfoWatcherExecutionStateChangedEventArgs = _ns_module.AppResourceGroupInfoWatcherExecutionStateChangedEventArgs
AppResourceGroupMemoryReport = _ns_module.AppResourceGroupMemoryReport
AppResourceGroupStateReport = _ns_module.AppResourceGroupStateReport
AppUriHandlerHost = _ns_module.AppUriHandlerHost
AppUriHandlerRegistration = _ns_module.AppUriHandlerRegistration
AppUriHandlerRegistrationManager = _ns_module.AppUriHandlerRegistrationManager
DateTimeSettings = _ns_module.DateTimeSettings
DispatcherQueue = _ns_module.DispatcherQueue
DispatcherQueueController = _ns_module.DispatcherQueueController
DispatcherQueueShutdownStartingEventArgs = _ns_module.DispatcherQueueShutdownStartingEventArgs
DispatcherQueueTimer = _ns_module.DispatcherQueueTimer
FolderLauncherOptions = _ns_module.FolderLauncherOptions
KnownUserProperties = _ns_module.KnownUserProperties
LaunchUriResult = _ns_module.LaunchUriResult
Launcher = _ns_module.Launcher
LauncherOptions = _ns_module.LauncherOptions
LauncherUIOptions = _ns_module.LauncherUIOptions
MemoryManager = _ns_module.MemoryManager
ProcessLauncher = _ns_module.ProcessLauncher
ProcessLauncherOptions = _ns_module.ProcessLauncherOptions
ProcessLauncherResult = _ns_module.ProcessLauncherResult
ProcessMemoryReport = _ns_module.ProcessMemoryReport
ProtocolForResultsOperation = _ns_module.ProtocolForResultsOperation
RemoteLauncher = _ns_module.RemoteLauncher
RemoteLauncherOptions = _ns_module.RemoteLauncherOptions
ShutdownManager = _ns_module.ShutdownManager
TimeZoneSettings = _ns_module.TimeZoneSettings
User = _ns_module.User
UserAuthenticationStatusChangeDeferral = _ns_module.UserAuthenticationStatusChangeDeferral
UserAuthenticationStatusChangingEventArgs = _ns_module.UserAuthenticationStatusChangingEventArgs
UserChangedEventArgs = _ns_module.UserChangedEventArgs
UserDeviceAssociation = _ns_module.UserDeviceAssociation
UserDeviceAssociationChangedEventArgs = _ns_module.UserDeviceAssociationChangedEventArgs
UserPicker = _ns_module.UserPicker
UserWatcher = _ns_module.UserWatcher
ILauncherViewOptions = _ns_module.ILauncherViewOptions