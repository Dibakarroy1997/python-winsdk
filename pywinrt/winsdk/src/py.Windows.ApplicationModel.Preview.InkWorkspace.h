// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Graphics.Imaging.h")
#include "py.Windows.Graphics.Imaging.h"
#endif

#include <winrt/Windows.ApplicationModel.Preview.InkWorkspace.h>

namespace py::proj::Windows::ApplicationModel::Preview::InkWorkspace
{}

namespace py::impl::Windows::ApplicationModel::Preview::InkWorkspace
{}

namespace py::wrapper::Windows::ApplicationModel::Preview::InkWorkspace
{
    using InkWorkspaceHostedAppManager = py::winrt_wrapper<winrt::Windows::ApplicationModel::Preview::InkWorkspace::InkWorkspaceHostedAppManager>;
}

namespace py
{

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Preview::InkWorkspace::InkWorkspaceHostedAppManager>
    {
        static PyTypeObject* get_python_type() noexcept;
    };
}