// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.ApplicationModel.DataTransfer.h")
#include "py.Windows.ApplicationModel.DataTransfer.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#if __has_include("py.Windows.UI.h")
#include "py.Windows.UI.h"
#endif

#if __has_include("py.Windows.Web.h")
#include "py.Windows.Web.h"
#endif

#if __has_include("py.Windows.Web.Http.h")
#include "py.Windows.Web.Http.h"
#endif

#include <winrt/Windows.Web.UI.h>

namespace py::proj::Windows::Web::UI
{}

namespace py::impl::Windows::Web::UI
{}

namespace py::wrapper::Windows::Web::UI
{
    using WebViewControlContentLoadingEventArgs = py::winrt_wrapper<winrt::Windows::Web::UI::WebViewControlContentLoadingEventArgs>;
    using WebViewControlDOMContentLoadedEventArgs = py::winrt_wrapper<winrt::Windows::Web::UI::WebViewControlDOMContentLoadedEventArgs>;
    using WebViewControlDeferredPermissionRequest = py::winrt_wrapper<winrt::Windows::Web::UI::WebViewControlDeferredPermissionRequest>;
    using WebViewControlLongRunningScriptDetectedEventArgs = py::winrt_wrapper<winrt::Windows::Web::UI::WebViewControlLongRunningScriptDetectedEventArgs>;
    using WebViewControlNavigationCompletedEventArgs = py::winrt_wrapper<winrt::Windows::Web::UI::WebViewControlNavigationCompletedEventArgs>;
    using WebViewControlNavigationStartingEventArgs = py::winrt_wrapper<winrt::Windows::Web::UI::WebViewControlNavigationStartingEventArgs>;
    using WebViewControlNewWindowRequestedEventArgs = py::winrt_wrapper<winrt::Windows::Web::UI::WebViewControlNewWindowRequestedEventArgs>;
    using WebViewControlPermissionRequest = py::winrt_wrapper<winrt::Windows::Web::UI::WebViewControlPermissionRequest>;
    using WebViewControlPermissionRequestedEventArgs = py::winrt_wrapper<winrt::Windows::Web::UI::WebViewControlPermissionRequestedEventArgs>;
    using WebViewControlScriptNotifyEventArgs = py::winrt_wrapper<winrt::Windows::Web::UI::WebViewControlScriptNotifyEventArgs>;
    using WebViewControlSettings = py::winrt_wrapper<winrt::Windows::Web::UI::WebViewControlSettings>;
    using WebViewControlUnsupportedUriSchemeIdentifiedEventArgs = py::winrt_wrapper<winrt::Windows::Web::UI::WebViewControlUnsupportedUriSchemeIdentifiedEventArgs>;
    using WebViewControlUnviewableContentIdentifiedEventArgs = py::winrt_wrapper<winrt::Windows::Web::UI::WebViewControlUnviewableContentIdentifiedEventArgs>;
    using WebViewControlWebResourceRequestedEventArgs = py::winrt_wrapper<winrt::Windows::Web::UI::WebViewControlWebResourceRequestedEventArgs>;
    using IWebViewControl = py::winrt_wrapper<winrt::Windows::Web::UI::IWebViewControl>;
    using IWebViewControl2 = py::winrt_wrapper<winrt::Windows::Web::UI::IWebViewControl2>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Web::UI::WebViewControlContentLoadingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Web::UI::WebViewControlDOMContentLoadedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Web::UI::WebViewControlDeferredPermissionRequest>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Web::UI::WebViewControlLongRunningScriptDetectedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Web::UI::WebViewControlNavigationCompletedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Web::UI::WebViewControlNavigationStartingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Web::UI::WebViewControlNewWindowRequestedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Web::UI::WebViewControlPermissionRequest>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Web::UI::WebViewControlPermissionRequestedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Web::UI::WebViewControlScriptNotifyEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Web::UI::WebViewControlSettings>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Web::UI::WebViewControlUnsupportedUriSchemeIdentifiedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Web::UI::WebViewControlUnviewableContentIdentifiedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Web::UI::WebViewControlWebResourceRequestedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Web::UI::IWebViewControl>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Web::UI::IWebViewControl2>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}