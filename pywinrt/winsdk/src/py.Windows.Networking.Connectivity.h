// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Networking.h")
#include "py.Windows.Networking.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#include <winrt/Windows.Networking.Connectivity.h>

namespace py::proj::Windows::Networking::Connectivity
{}

namespace py::impl::Windows::Networking::Connectivity
{
    struct NetworkStatusChangedEventHandler
    {
        static winrt::Windows::Networking::Connectivity::NetworkStatusChangedEventHandler get(PyObject* callable)
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
}

namespace py::wrapper::Windows::Networking::Connectivity
{
    using AttributedNetworkUsage = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::AttributedNetworkUsage>;
    using CellularApnContext = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::CellularApnContext>;
    using ConnectionCost = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::ConnectionCost>;
    using ConnectionProfile = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::ConnectionProfile>;
    using ConnectionProfileFilter = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::ConnectionProfileFilter>;
    using ConnectionSession = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::ConnectionSession>;
    using ConnectivityInterval = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::ConnectivityInterval>;
    using ConnectivityManager = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::ConnectivityManager>;
    using DataPlanStatus = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::DataPlanStatus>;
    using DataPlanUsage = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::DataPlanUsage>;
    using DataUsage = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::DataUsage>;
    using IPInformation = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::IPInformation>;
    using LanIdentifier = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::LanIdentifier>;
    using LanIdentifierData = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::LanIdentifierData>;
    using NetworkAdapter = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::NetworkAdapter>;
    using NetworkInformation = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::NetworkInformation>;
    using NetworkItem = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::NetworkItem>;
    using NetworkSecuritySettings = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::NetworkSecuritySettings>;
    using NetworkStateChangeEventDetails = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::NetworkStateChangeEventDetails>;
    using NetworkUsage = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::NetworkUsage>;
    using ProviderNetworkUsage = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::ProviderNetworkUsage>;
    using ProxyConfiguration = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::ProxyConfiguration>;
    using RoutePolicy = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::RoutePolicy>;
    using WlanConnectionProfileDetails = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::WlanConnectionProfileDetails>;
    using WwanConnectionProfileDetails = py::winrt_wrapper<winrt::Windows::Networking::Connectivity::WwanConnectionProfileDetails>;
    using NetworkUsageStates = py::winrt_struct_wrapper<winrt::Windows::Networking::Connectivity::NetworkUsageStates>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::AttributedNetworkUsage>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::CellularApnContext>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::ConnectionCost>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::ConnectionProfile>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::ConnectionProfileFilter>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::ConnectionSession>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::ConnectivityInterval>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::ConnectivityManager>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::DataPlanStatus>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::DataPlanUsage>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::DataUsage>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::IPInformation>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::LanIdentifier>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::LanIdentifierData>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::NetworkAdapter>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::NetworkInformation>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::NetworkItem>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::NetworkSecuritySettings>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::NetworkStateChangeEventDetails>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::NetworkUsage>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::ProviderNetworkUsage>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::ProxyConfiguration>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::RoutePolicy>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::WlanConnectionProfileDetails>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::WwanConnectionProfileDetails>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Connectivity::NetworkUsageStates>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template <>
    struct delegate_python_type<winrt::Windows::Networking::Connectivity::NetworkStatusChangedEventHandler>
    {
        using type = py::impl::Windows::Networking::Connectivity::NetworkStatusChangedEventHandler;
    };

    template<>
    struct converter<winrt::Windows::Networking::Connectivity::NetworkUsageStates>
    {
        static PyObject* convert(winrt::Windows::Networking::Connectivity::NetworkUsageStates instance) noexcept;
        static winrt::Windows::Networking::Connectivity::NetworkUsageStates convert_to(PyObject* obj);
    };

}