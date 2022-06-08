// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#include <winrt/Windows.UI.Core.Preview.Communications.h>

namespace py::proj::Windows::UI::Core::Preview::Communications
{}

namespace py::impl::Windows::UI::Core::Preview::Communications
{}

namespace py::wrapper::Windows::UI::Core::Preview::Communications
{
    using PreviewTeamCleanupRequestedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Core::Preview::Communications::PreviewTeamCleanupRequestedEventArgs>;
    using PreviewTeamCommandInvokedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Core::Preview::Communications::PreviewTeamCommandInvokedEventArgs>;
    using PreviewTeamDeviceCredentials = py::winrt_wrapper<winrt::Windows::UI::Core::Preview::Communications::PreviewTeamDeviceCredentials>;
    using PreviewTeamEndMeetingRequestedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Core::Preview::Communications::PreviewTeamEndMeetingRequestedEventArgs>;
    using PreviewTeamJoinMeetingRequestedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Core::Preview::Communications::PreviewTeamJoinMeetingRequestedEventArgs>;
    using PreviewTeamView = py::winrt_wrapper<winrt::Windows::UI::Core::Preview::Communications::PreviewTeamView>;
}

namespace py
{

    template<>
    struct py_type<winrt::Windows::UI::Core::Preview::Communications::PreviewMeetingInfoDisplayKind>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Core::Preview::Communications::PreviewSystemState>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Core::Preview::Communications::PreviewTeamEndMeetingKind>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Core::Preview::Communications::PreviewTeamViewCommand>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Core::Preview::Communications::PreviewTeamCleanupRequestedEventArgs>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Core::Preview::Communications::PreviewTeamCommandInvokedEventArgs>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Core::Preview::Communications::PreviewTeamDeviceCredentials>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Core::Preview::Communications::PreviewTeamEndMeetingRequestedEventArgs>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Core::Preview::Communications::PreviewTeamJoinMeetingRequestedEventArgs>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Core::Preview::Communications::PreviewTeamView>
    {
        static PyTypeObject* get_python_type() noexcept;
    };
}