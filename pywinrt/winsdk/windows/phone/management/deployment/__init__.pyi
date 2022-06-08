# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.applicationmodel
import winsdk.windows.foundation
import winsdk.windows.foundation.collections
import winsdk.windows.management.deployment

class EnterpriseEnrollmentStatus(enum.IntEnum):
    SUCCESS = 0
    CANCELLED_BY_USER = 1
    UNKNOWN_FAILURE = 2

class EnterpriseStatus(enum.IntEnum):
    ENROLLED = 0
    DISABLED = 1
    REVOKED = 2
    EXPIRED = 3

Self = typing.TypeVar('Self')

class Enterprise(_winrt.Object):
    enrollment_valid_from: winsdk.windows.foundation.DateTime
    enrollment_valid_to: winsdk.windows.foundation.DateTime
    id: uuid.UUID
    name: str
    status: EnterpriseStatus
    workplace_id: _winrt.Int32
    @staticmethod
    def _from(obj: _winrt.Object) -> Enterprise: ...

class EnterpriseEnrollmentManager(_winrt.Object):
    current_enterprise: typing.Optional[Enterprise]
    enrolled_enterprises: typing.Optional[winsdk.windows.foundation.collections.IVectorView[Enterprise]]
    @staticmethod
    def _from(obj: _winrt.Object) -> EnterpriseEnrollmentManager: ...
    @staticmethod
    def request_enrollment_async(enrollment_token: str) -> winsdk.windows.foundation.IAsyncOperation[EnterpriseEnrollmentResult]: ...
    @staticmethod
    def request_unenrollment_async(enterprise: typing.Optional[Enterprise]) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @staticmethod
    def validate_enterprises_async() -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...

class EnterpriseEnrollmentResult(_winrt.Object):
    enrolled_enterprise: typing.Optional[Enterprise]
    status: EnterpriseEnrollmentStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> EnterpriseEnrollmentResult: ...

class InstallationManager(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> InstallationManager: ...
    @typing.overload
    @staticmethod
    def add_package_async(title: str, source_location: typing.Optional[winsdk.windows.foundation.Uri]) -> winsdk.windows.foundation.IAsyncOperationWithProgress[PackageInstallResult, _winrt.UInt32]: ...
    @typing.overload
    @staticmethod
    def add_package_async(title: str, source_location: typing.Optional[winsdk.windows.foundation.Uri], instance_id: str, offer_id: str, license: typing.Optional[winsdk.windows.foundation.Uri]) -> winsdk.windows.foundation.IAsyncOperationWithProgress[PackageInstallResult, _winrt.UInt32]: ...
    @typing.overload
    @staticmethod
    def find_packages() -> typing.Optional[winsdk.windows.foundation.collections.IIterable[winsdk.windows.applicationmodel.Package]]: ...
    @typing.overload
    @staticmethod
    def find_packages(package_name: str, package_publisher: str) -> typing.Optional[winsdk.windows.foundation.collections.IIterable[winsdk.windows.applicationmodel.Package]]: ...
    @staticmethod
    def find_packages_for_current_publisher() -> typing.Optional[winsdk.windows.foundation.collections.IIterable[winsdk.windows.applicationmodel.Package]]: ...
    @staticmethod
    def get_pending_package_installs() -> typing.Optional[winsdk.windows.foundation.collections.IIterable[winsdk.windows.foundation.IAsyncOperationWithProgress[PackageInstallResult, _winrt.UInt32]]]: ...
    @staticmethod
    def register_package_async(manifest_uri: typing.Optional[winsdk.windows.foundation.Uri], dependency_package_uris: typing.Iterable[winsdk.windows.foundation.Uri], deployment_options: winsdk.windows.management.deployment.DeploymentOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[PackageInstallResult, _winrt.UInt32]: ...
    @staticmethod
    def remove_package_async(package_full_name: str, removal_options: winsdk.windows.management.deployment.RemovalOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[PackageInstallResult, _winrt.UInt32]: ...

class PackageInstallResult(_winrt.Object):
    install_state: winsdk.windows.management.deployment.PackageInstallState
    product_id: str
    error_text: str
    @staticmethod
    def _from(obj: _winrt.Object) -> PackageInstallResult: ...
