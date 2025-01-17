// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Storage.h")
#include "py.Windows.Storage.h"
#endif

#include <winrt/Windows.Media.Playlists.h>

namespace py::proj::Windows::Media::Playlists
{}

namespace py::impl::Windows::Media::Playlists
{}

namespace py::wrapper::Windows::Media::Playlists
{
    using Playlist = py::winrt_wrapper<winrt::Windows::Media::Playlists::Playlist>;
}

namespace py
{

    template<>
    struct py_type<winrt::Windows::Media::Playlists::PlaylistFormat>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Media::Playlists::Playlist>
    {
        static PyTypeObject* get_python_type() noexcept;
    };
}
