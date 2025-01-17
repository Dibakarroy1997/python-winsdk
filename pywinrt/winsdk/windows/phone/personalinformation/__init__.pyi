# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.foundation
import winsdk.windows.foundation.collections
import winsdk.windows.storage.streams

class ContactChangeType(enum.IntEnum):
    CREATED = 0
    MODIFIED = 1
    DELETED = 2

class ContactQueryResultOrdering(enum.IntEnum):
    SYSTEM_DEFAULT = 0
    GIVEN_NAME_FAMILY_NAME = 1
    FAMILY_NAME_GIVEN_NAME = 2

class ContactStoreApplicationAccessMode(enum.IntEnum):
    LIMITED_READ_ONLY = 0
    READ_ONLY = 1

class ContactStoreSystemAccessMode(enum.IntEnum):
    READ_ONLY = 0
    READ_WRITE = 1

class VCardFormat(enum.IntEnum):
    VERSION2_1 = 0
    VERSION3 = 1

Self = typing.TypeVar('Self')

class ContactAddress(_winrt.Object):
    street_address: str
    region: str
    postal_code: str
    locality: str
    country: str
    @staticmethod
    def _from(obj: _winrt.Object) -> ContactAddress: ...
    def __init__(self) -> None: ...

class ContactChangeRecord(_winrt.Object):
    change_type: ContactChangeType
    id: str
    remote_id: str
    revision_number: _winrt.UInt64
    @staticmethod
    def _from(obj: _winrt.Object) -> ContactChangeRecord: ...

class ContactInformation(_winrt.Object):
    honorific_suffix: str
    honorific_prefix: str
    given_name: str
    family_name: str
    display_name: str
    display_picture: typing.Optional[winsdk.windows.storage.streams.IRandomAccessStreamReference]
    @staticmethod
    def _from(obj: _winrt.Object) -> ContactInformation: ...
    def __init__(self) -> None: ...
    def get_display_picture_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IRandomAccessStream]: ...
    def get_properties_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IMap[str, _winrt.Object]]: ...
    @staticmethod
    def parse_vcard_async(vcard: typing.Optional[winsdk.windows.storage.streams.IInputStream]) -> winsdk.windows.foundation.IAsyncOperation[ContactInformation]: ...
    def set_display_picture_async(self, stream: typing.Optional[winsdk.windows.storage.streams.IInputStream]) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    @typing.overload
    def to_vcard_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IRandomAccessStream]: ...
    @typing.overload
    def to_vcard_async(self, format: VCardFormat) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IRandomAccessStream]: ...

class ContactQueryOptions(_winrt.Object):
    order_by: ContactQueryResultOrdering
    desired_fields: typing.Optional[winsdk.windows.foundation.collections.IVector[str]]
    @staticmethod
    def _from(obj: _winrt.Object) -> ContactQueryOptions: ...
    def __init__(self) -> None: ...

class ContactQueryResult(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> ContactQueryResult: ...
    def get_contact_count_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.UInt32]: ...
    @typing.overload
    def get_contacts_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[StoredContact]]: ...
    @typing.overload
    def get_contacts_async(self, start_index: _winrt.UInt32, max_number_of_items: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[StoredContact]]: ...
    def get_current_query_options(self) -> typing.Optional[ContactQueryOptions]: ...

class ContactStore(_winrt.Object):
    revision_number: _winrt.UInt64
    @staticmethod
    def _from(obj: _winrt.Object) -> ContactStore: ...
    @typing.overload
    def create_contact_query(self) -> typing.Optional[ContactQueryResult]: ...
    @typing.overload
    def create_contact_query(self, options: typing.Optional[ContactQueryOptions]) -> typing.Optional[ContactQueryResult]: ...
    def create_me_contact_async(self, id: str) -> winsdk.windows.foundation.IAsyncOperation[StoredContact]: ...
    @typing.overload
    @staticmethod
    def create_or_open_async() -> winsdk.windows.foundation.IAsyncOperation[ContactStore]: ...
    @typing.overload
    @staticmethod
    def create_or_open_async(access: ContactStoreSystemAccessMode, sharing: ContactStoreApplicationAccessMode) -> winsdk.windows.foundation.IAsyncOperation[ContactStore]: ...
    def delete_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def delete_contact_async(self, id: str) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def find_contact_by_id_async(self, id: str) -> winsdk.windows.foundation.IAsyncOperation[StoredContact]: ...
    def find_contact_by_remote_id_async(self, id: str) -> winsdk.windows.foundation.IAsyncOperation[StoredContact]: ...
    def get_changes_async(self, base_revision_number: _winrt.UInt64) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[ContactChangeRecord]]: ...
    def load_extended_properties_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IMap[str, _winrt.Object]]: ...
    def save_extended_properties_async(self, data: winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...

class KnownContactProperties(_winrt.Object):
    additional_name: str
    address: str
    alternate_mobile_telephone: str
    alternate_telephone: str
    alternate_work_telephone: str
    anniversary: str
    birthdate: str
    children: str
    company_name: str
    company_telephone: str
    display_name: str
    email: str
    family_name: str
    given_name: str
    home_fax: str
    honorific_prefix: str
    honorific_suffix: str
    job_title: str
    manager: str
    mobile_telephone: str
    nickname: str
    notes: str
    office_location: str
    other_address: str
    other_email: str
    significant_other: str
    telephone: str
    url: str
    work_address: str
    work_email: str
    work_fax: str
    work_telephone: str
    yomi_company_name: str
    yomi_family_name: str
    yomi_given_name: str
    @staticmethod
    def _from(obj: _winrt.Object) -> KnownContactProperties: ...

class StoredContact(_winrt.Object):
    honorific_suffix: str
    honorific_prefix: str
    given_name: str
    family_name: str
    display_name: str
    display_picture: typing.Optional[winsdk.windows.storage.streams.IRandomAccessStreamReference]
    display_picture_date: winsdk.windows.foundation.DateTime
    remote_id: str
    id: str
    store: typing.Optional[ContactStore]
    @staticmethod
    def _from(obj: _winrt.Object) -> StoredContact: ...
    @typing.overload
    def __init__(self, store: typing.Optional[ContactStore]) -> None: ...
    @typing.overload
    def __init__(self, store: typing.Optional[ContactStore], contact: typing.Optional[ContactInformation]) -> None: ...
    def get_display_picture_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IRandomAccessStream]: ...
    def get_extended_properties_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IMap[str, _winrt.Object]]: ...
    def get_properties_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IMap[str, _winrt.Object]]: ...
    def replace_existing_contact_async(self, id: str) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def save_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def set_display_picture_async(self, stream: typing.Optional[winsdk.windows.storage.streams.IInputStream]) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    @typing.overload
    def to_vcard_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IRandomAccessStream]: ...
    @typing.overload
    def to_vcard_async(self, format: VCardFormat) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IRandomAccessStream]: ...

class IContactInformation(_winrt.Object):
    display_name: str
    display_picture: typing.Optional[winsdk.windows.storage.streams.IRandomAccessStreamReference]
    family_name: str
    given_name: str
    honorific_prefix: str
    honorific_suffix: str
    @staticmethod
    def _from(obj: _winrt.Object) -> IContactInformation: ...
    def get_display_picture_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IRandomAccessStream]: ...
    def get_properties_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IMap[str, _winrt.Object]]: ...
    def set_display_picture_async(self, stream: typing.Optional[winsdk.windows.storage.streams.IInputStream]) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    @typing.overload
    def to_vcard_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IRandomAccessStream]: ...
    @typing.overload
    def to_vcard_async(self, format: VCardFormat) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IRandomAccessStream]: ...

class IContactInformation2(_winrt.Object):
    display_picture_date: winsdk.windows.foundation.DateTime
    @staticmethod
    def _from(obj: _winrt.Object) -> IContactInformation2: ...

