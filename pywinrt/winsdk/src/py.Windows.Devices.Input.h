// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Devices.Haptics.h")
#include "py.Windows.Devices.Haptics.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#include <winrt/Windows.Devices.Input.h>

namespace py::proj::Windows::Devices::Input
{}

namespace py::impl::Windows::Devices::Input
{}

namespace py::wrapper::Windows::Devices::Input
{
    using KeyboardCapabilities = py::winrt_wrapper<winrt::Windows::Devices::Input::KeyboardCapabilities>;
    using MouseCapabilities = py::winrt_wrapper<winrt::Windows::Devices::Input::MouseCapabilities>;
    using MouseDevice = py::winrt_wrapper<winrt::Windows::Devices::Input::MouseDevice>;
    using MouseEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Input::MouseEventArgs>;
    using PenButtonListener = py::winrt_wrapper<winrt::Windows::Devices::Input::PenButtonListener>;
    using PenDevice = py::winrt_wrapper<winrt::Windows::Devices::Input::PenDevice>;
    using PenDockListener = py::winrt_wrapper<winrt::Windows::Devices::Input::PenDockListener>;
    using PenDockedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Input::PenDockedEventArgs>;
    using PenTailButtonClickedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Input::PenTailButtonClickedEventArgs>;
    using PenTailButtonDoubleClickedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Input::PenTailButtonDoubleClickedEventArgs>;
    using PenTailButtonLongPressedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Input::PenTailButtonLongPressedEventArgs>;
    using PenUndockedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Input::PenUndockedEventArgs>;
    using PointerDevice = py::winrt_wrapper<winrt::Windows::Devices::Input::PointerDevice>;
    using TouchCapabilities = py::winrt_wrapper<winrt::Windows::Devices::Input::TouchCapabilities>;
    using MouseDelta = py::winrt_struct_wrapper<winrt::Windows::Devices::Input::MouseDelta>;
    using PointerDeviceUsage = py::winrt_struct_wrapper<winrt::Windows::Devices::Input::PointerDeviceUsage>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Devices::Input::KeyboardCapabilities>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::MouseCapabilities>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::MouseDevice>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::MouseEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::PenButtonListener>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::PenDevice>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::PenDockListener>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::PenDockedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::PenTailButtonClickedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::PenTailButtonDoubleClickedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::PenTailButtonLongPressedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::PenUndockedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::PointerDevice>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::TouchCapabilities>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::MouseDelta>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::PointerDeviceUsage>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct converter<winrt::Windows::Devices::Input::MouseDelta>
    {
        static PyObject* convert(winrt::Windows::Devices::Input::MouseDelta instance) noexcept;
        static winrt::Windows::Devices::Input::MouseDelta convert_to(PyObject* obj);
    };

    template<>
    struct converter<winrt::Windows::Devices::Input::PointerDeviceUsage>
    {
        static PyObject* convert(winrt::Windows::Devices::Input::PointerDeviceUsage instance) noexcept;
        static winrt::Windows::Devices::Input::PointerDeviceUsage convert_to(PyObject* obj);
    };

}