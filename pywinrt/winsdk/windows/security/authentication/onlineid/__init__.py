# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Security.Authentication.OnlineId")

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.system
except Exception:
    pass

class CredentialPromptType(enum.IntEnum):
    PROMPT_IF_NEEDED = 0
    RETYPE_CREDENTIALS = 1
    DO_NOT_PROMPT = 2

class OnlineIdSystemTicketStatus(enum.IntEnum):
    SUCCESS = 0
    ERROR = 1
    SERVICE_CONNECTION_ERROR = 2

OnlineIdAuthenticator = _ns_module.OnlineIdAuthenticator
OnlineIdServiceTicket = _ns_module.OnlineIdServiceTicket
OnlineIdServiceTicketRequest = _ns_module.OnlineIdServiceTicketRequest
OnlineIdSystemAuthenticator = _ns_module.OnlineIdSystemAuthenticator
OnlineIdSystemAuthenticatorForUser = _ns_module.OnlineIdSystemAuthenticatorForUser
OnlineIdSystemIdentity = _ns_module.OnlineIdSystemIdentity
OnlineIdSystemTicketResult = _ns_module.OnlineIdSystemTicketResult
SignOutUserOperation = _ns_module.SignOutUserOperation
UserAuthenticationOperation = _ns_module.UserAuthenticationOperation
UserIdentity = _ns_module.UserIdentity