// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Devices.Sensors.h")
#include "py.Windows.Devices.Sensors.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#include <winrt/Windows.System.Preview.h>

namespace py::proj::Windows::System::Preview
{}

namespace py::impl::Windows::System::Preview
{}

namespace py::wrapper::Windows::System::Preview
{
    using TwoPanelHingedDevicePosturePreview = py::winrt_wrapper<winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreview>;
    using TwoPanelHingedDevicePosturePreviewReading = py::winrt_wrapper<winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReading>;
    using TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreview>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReading>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}