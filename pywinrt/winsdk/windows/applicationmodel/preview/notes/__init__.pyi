# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.foundation
import winsdk.windows.graphics.imaging
import winsdk.windows.storage.streams

Self = typing.TypeVar('Self')

class NotePlacementChangedPreviewEventArgs(_winrt.Object):
    view_id: _winrt.Int32
    @staticmethod
    def _from(obj: _winrt.Object) -> NotePlacementChangedPreviewEventArgs: ...

class NoteVisibilityChangedPreviewEventArgs(_winrt.Object):
    is_visible: _winrt.Boolean
    view_id: _winrt.Int32
    @staticmethod
    def _from(obj: _winrt.Object) -> NoteVisibilityChangedPreviewEventArgs: ...

class NotesWindowManagerPreview(_winrt.Object):
    is_screen_locked: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> NotesWindowManagerPreview: ...
    @staticmethod
    def get_for_current_app() -> typing.Optional[NotesWindowManagerPreview]: ...
    def get_note_placement(self, note_view_id: _winrt.Int32) -> typing.Optional[winsdk.windows.storage.streams.IBuffer]: ...
    def hide_note(self, note_view_id: _winrt.Int32) -> None: ...
    def set_focus_to_next_view(self) -> None: ...
    def set_focus_to_previous_view(self) -> None: ...
    def set_notes_thumbnail_async(self, thumbnail: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def set_thumbnail_image_for_task_switcher_async(self, bitmap: typing.Optional[winsdk.windows.graphics.imaging.SoftwareBitmap]) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def show_note(self, note_view_id: _winrt.Int32) -> None: ...
    @typing.overload
    def show_note_relative_to(self, note_view_id: _winrt.Int32, anchor_note_view_id: _winrt.Int32) -> None: ...
    @typing.overload
    def show_note_relative_to(self, note_view_id: _winrt.Int32, anchor_note_view_id: _winrt.Int32, options: typing.Optional[NotesWindowManagerPreviewShowNoteOptions]) -> None: ...
    @typing.overload
    def show_note_with_placement(self, note_view_id: _winrt.Int32, data: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> None: ...
    @typing.overload
    def show_note_with_placement(self, note_view_id: _winrt.Int32, data: typing.Optional[winsdk.windows.storage.streams.IBuffer], options: typing.Optional[NotesWindowManagerPreviewShowNoteOptions]) -> None: ...
    def try_set_note_size(self, note_view_id: _winrt.Int32, size: winsdk.windows.foundation.Size) -> _winrt.Boolean: ...
    def add_note_placement_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[NotesWindowManagerPreview, NotePlacementChangedPreviewEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_note_placement_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_note_visibility_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[NotesWindowManagerPreview, NoteVisibilityChangedPreviewEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_note_visibility_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_system_lock_state_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[NotesWindowManagerPreview, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_system_lock_state_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class NotesWindowManagerPreviewShowNoteOptions(_winrt.Object):
    show_with_focus: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> NotesWindowManagerPreviewShowNoteOptions: ...
    def __init__(self) -> None: ...

