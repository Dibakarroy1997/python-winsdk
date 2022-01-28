// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Media.Playback.h")
#include "py.Windows.Media.Playback.h"
#endif

#include <winrt/Windows.Media.Protection.h>

namespace py::proj::Windows::Media::Protection
{}

namespace py::impl::Windows::Media::Protection
{
    struct ComponentLoadFailedEventHandler
    {
        static winrt::Windows::Media::Protection::ComponentLoadFailedEventHandler get(PyObject* callable)
        {
            py::delegate_callable _delegate{ callable };

            return [delegate = std::move(_delegate)](auto param0, auto param1)
            {
                winrt::handle_type<py::gil_state_traits> gil_state{ PyGILState_Ensure() };

                py::pyobj_handle py_param0{ py::convert(param0) };
                py::pyobj_handle py_param1{ py::convert(param1) };

                py::pyobj_handle args{ PyTuple_Pack(2, py_param0.get(), py_param1.get()) };
                py::pyobj_handle return_value{ PyObject_CallObject(delegate.callable(), args.get()) };

                if (!return_value)
                {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_invalid_argument();
                }
            };
        };
    };

    struct RebootNeededEventHandler
    {
        static winrt::Windows::Media::Protection::RebootNeededEventHandler get(PyObject* callable)
        {
            py::delegate_callable _delegate{ callable };

            return [delegate = std::move(_delegate)](auto param0)
            {
                winrt::handle_type<py::gil_state_traits> gil_state{ PyGILState_Ensure() };

                py::pyobj_handle py_param0{ py::convert(param0) };

                py::pyobj_handle args{ PyTuple_Pack(1, py_param0.get()) };
                py::pyobj_handle return_value{ PyObject_CallObject(delegate.callable(), args.get()) };

                if (!return_value)
                {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_invalid_argument();
                }
            };
        };
    };

    struct ServiceRequestedEventHandler
    {
        static winrt::Windows::Media::Protection::ServiceRequestedEventHandler get(PyObject* callable)
        {
            py::delegate_callable _delegate{ callable };

            return [delegate = std::move(_delegate)](auto param0, auto param1)
            {
                winrt::handle_type<py::gil_state_traits> gil_state{ PyGILState_Ensure() };

                py::pyobj_handle py_param0{ py::convert(param0) };
                py::pyobj_handle py_param1{ py::convert(param1) };

                py::pyobj_handle args{ PyTuple_Pack(2, py_param0.get(), py_param1.get()) };
                py::pyobj_handle return_value{ PyObject_CallObject(delegate.callable(), args.get()) };

                if (!return_value)
                {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_invalid_argument();
                }
            };
        };
    };
}

namespace py::wrapper::Windows::Media::Protection
{
    using ComponentLoadFailedEventArgs = py::winrt_wrapper<winrt::Windows::Media::Protection::ComponentLoadFailedEventArgs>;
    using HdcpSession = py::winrt_wrapper<winrt::Windows::Media::Protection::HdcpSession>;
    using MediaProtectionManager = py::winrt_wrapper<winrt::Windows::Media::Protection::MediaProtectionManager>;
    using MediaProtectionPMPServer = py::winrt_wrapper<winrt::Windows::Media::Protection::MediaProtectionPMPServer>;
    using MediaProtectionServiceCompletion = py::winrt_wrapper<winrt::Windows::Media::Protection::MediaProtectionServiceCompletion>;
    using ProtectionCapabilities = py::winrt_wrapper<winrt::Windows::Media::Protection::ProtectionCapabilities>;
    using RevocationAndRenewalInformation = py::winrt_wrapper<winrt::Windows::Media::Protection::RevocationAndRenewalInformation>;
    using RevocationAndRenewalItem = py::winrt_wrapper<winrt::Windows::Media::Protection::RevocationAndRenewalItem>;
    using ServiceRequestedEventArgs = py::winrt_wrapper<winrt::Windows::Media::Protection::ServiceRequestedEventArgs>;
    using IMediaProtectionServiceRequest = py::winrt_wrapper<winrt::Windows::Media::Protection::IMediaProtectionServiceRequest>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Media::Protection::ComponentLoadFailedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::Protection::HdcpSession>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::Protection::MediaProtectionManager>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::Protection::MediaProtectionPMPServer>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::Protection::MediaProtectionServiceCompletion>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::Protection::ProtectionCapabilities>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::Protection::RevocationAndRenewalInformation>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::Protection::RevocationAndRenewalItem>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::Protection::ServiceRequestedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::Protection::IMediaProtectionServiceRequest>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template <>
    struct delegate_python_type<winrt::Windows::Media::Protection::ComponentLoadFailedEventHandler>
    {
        using type = py::impl::Windows::Media::Protection::ComponentLoadFailedEventHandler;
    };

    template <>
    struct delegate_python_type<winrt::Windows::Media::Protection::RebootNeededEventHandler>
    {
        using type = py::impl::Windows::Media::Protection::RebootNeededEventHandler;
    };

    template <>
    struct delegate_python_type<winrt::Windows::Media::Protection::ServiceRequestedEventHandler>
    {
        using type = py::impl::Windows::Media::Protection::ServiceRequestedEventHandler;
    };

}