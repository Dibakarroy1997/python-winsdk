# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import winsdk

_ns_module = winsdk._import_ns_module("Windows.ApplicationModel.AppExtensions")

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

AppExtension = _ns_module.AppExtension
AppExtensionCatalog = _ns_module.AppExtensionCatalog
AppExtensionPackageInstalledEventArgs = _ns_module.AppExtensionPackageInstalledEventArgs
AppExtensionPackageStatusChangedEventArgs = _ns_module.AppExtensionPackageStatusChangedEventArgs
AppExtensionPackageUninstallingEventArgs = _ns_module.AppExtensionPackageUninstallingEventArgs
AppExtensionPackageUpdatedEventArgs = _ns_module.AppExtensionPackageUpdatedEventArgs
AppExtensionPackageUpdatingEventArgs = _ns_module.AppExtensionPackageUpdatingEventArgs