# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.ApplicationModel.Contacts.Provider")

try:
    import winsdk.windows.applicationmodel.contacts
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

class AddContactResult(enum.IntEnum):
    ADDED = 0
    ALREADY_ADDED = 1
    UNAVAILABLE = 2

ContactPickerUI = _ns_module.ContactPickerUI
ContactRemovedEventArgs = _ns_module.ContactRemovedEventArgs