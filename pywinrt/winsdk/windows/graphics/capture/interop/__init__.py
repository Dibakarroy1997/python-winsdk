# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.4

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Graphics.Capture.Interop")

try:
    import winsdk.windows.graphics.capture
except Exception:
    pass

create_for_monitor = _ns_module.create_for_monitor
create_for_window = _ns_module.create_for_window