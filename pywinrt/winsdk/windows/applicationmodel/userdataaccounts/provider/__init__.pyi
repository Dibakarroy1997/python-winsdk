# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.applicationmodel.userdataaccounts
import winsdk.windows.foundation.collections

class UserDataAccountProviderOperationKind(enum.IntEnum):
    ADD_ACCOUNT = 0
    SETTINGS = 1
    RESOLVE_ERRORS = 2

class UserDataAccountProviderPartnerAccountKind(enum.IntEnum):
    EXCHANGE = 0
    POP_OR_IMAP = 1

Self = typing.TypeVar('Self')

class UserDataAccountPartnerAccountInfo(_winrt.Object):
    account_kind: UserDataAccountProviderPartnerAccountKind
    display_name: str
    priority: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> UserDataAccountPartnerAccountInfo: ...

class UserDataAccountProviderAddAccountOperation(_winrt.Object):
    content_kinds: winsdk.windows.applicationmodel.userdataaccounts.UserDataAccountContentKinds
    partner_account_infos: typing.Optional[winsdk.windows.foundation.collections.IVectorView[UserDataAccountPartnerAccountInfo]]
    kind: UserDataAccountProviderOperationKind
    @staticmethod
    def _from(obj: _winrt.Object) -> UserDataAccountProviderAddAccountOperation: ...
    def report_completed(self, user_data_account_id: str) -> None: ...

class UserDataAccountProviderResolveErrorsOperation(_winrt.Object):
    kind: UserDataAccountProviderOperationKind
    user_data_account_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> UserDataAccountProviderResolveErrorsOperation: ...
    def report_completed(self) -> None: ...

class UserDataAccountProviderSettingsOperation(_winrt.Object):
    kind: UserDataAccountProviderOperationKind
    user_data_account_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> UserDataAccountProviderSettingsOperation: ...
    def report_completed(self) -> None: ...

class IUserDataAccountProviderOperation(_winrt.Object):
    kind: UserDataAccountProviderOperationKind
    @staticmethod
    def _from(obj: _winrt.Object) -> IUserDataAccountProviderOperation: ...

