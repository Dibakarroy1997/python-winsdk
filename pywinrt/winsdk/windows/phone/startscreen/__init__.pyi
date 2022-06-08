# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.foundation
import winsdk.windows.ui.notifications

Self = typing.TypeVar('Self')

class DualSimTile(_winrt.Object):
    display_name: str
    is_pinned_to_start: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> DualSimTile: ...
    def __init__(self) -> None: ...
    def create_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @staticmethod
    def create_badge_updater_for_sim1() -> typing.Optional[winsdk.windows.ui.notifications.BadgeUpdater]: ...
    @staticmethod
    def create_badge_updater_for_sim2() -> typing.Optional[winsdk.windows.ui.notifications.BadgeUpdater]: ...
    @staticmethod
    def create_tile_updater_for_sim1() -> typing.Optional[winsdk.windows.ui.notifications.TileUpdater]: ...
    @staticmethod
    def create_tile_updater_for_sim2() -> typing.Optional[winsdk.windows.ui.notifications.TileUpdater]: ...
    @staticmethod
    def create_toast_notifier_for_sim1() -> typing.Optional[winsdk.windows.ui.notifications.ToastNotifier]: ...
    @staticmethod
    def create_toast_notifier_for_sim2() -> typing.Optional[winsdk.windows.ui.notifications.ToastNotifier]: ...
    def delete_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @staticmethod
    def get_tile_for_sim2() -> typing.Optional[DualSimTile]: ...
    def update_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @staticmethod
    def update_display_name_for_sim1_async(name: str) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...

class IToastNotificationManagerStatics3(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> IToastNotificationManagerStatics3: ...
    def create_toast_notifier_for_secondary_tile(self, tile_id: str) -> typing.Optional[winsdk.windows.ui.notifications.ToastNotifier]: ...
