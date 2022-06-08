// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.UI.Notifications.h")
#include "py.Windows.UI.Notifications.h"
#endif

#include <winrt/Windows.Phone.StartScreen.h>

namespace py::proj::Windows::Phone::StartScreen
{}

namespace py::impl::Windows::Phone::StartScreen
{}

namespace py::wrapper::Windows::Phone::StartScreen
{
    using DualSimTile = py::winrt_wrapper<winrt::Windows::Phone::StartScreen::DualSimTile>;
    using IToastNotificationManagerStatics3 = py::winrt_wrapper<winrt::Windows::Phone::StartScreen::IToastNotificationManagerStatics3>;
}

namespace py
{

    template<>
    struct winrt_type<winrt::Windows::Phone::StartScreen::DualSimTile>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Phone::StartScreen::IToastNotificationManagerStatics3>
    {
        static PyTypeObject* get_python_type() noexcept;
    };
}