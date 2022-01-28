// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.ApplicationModel.h")
#include "py.Windows.ApplicationModel.h"
#endif

#if __has_include("py.Windows.ApplicationModel.Activation.h")
#include "py.Windows.ApplicationModel.Activation.h"
#endif

#if __has_include("py.Windows.ApplicationModel.Appointments.AppointmentsProvider.h")
#include "py.Windows.ApplicationModel.Appointments.AppointmentsProvider.h"
#endif

#if __has_include("py.Windows.ApplicationModel.Background.h")
#include "py.Windows.ApplicationModel.Background.h"
#endif

#if __has_include("py.Windows.ApplicationModel.Contacts.h")
#include "py.Windows.ApplicationModel.Contacts.h"
#endif

#if __has_include("py.Windows.ApplicationModel.Core.h")
#include "py.Windows.ApplicationModel.Core.h"
#endif

#if __has_include("py.Windows.ApplicationModel.DataTransfer.h")
#include "py.Windows.ApplicationModel.DataTransfer.h"
#endif

#if __has_include("py.Windows.ApplicationModel.DataTransfer.ShareTarget.h")
#include "py.Windows.ApplicationModel.DataTransfer.ShareTarget.h"
#endif

#if __has_include("py.Windows.ApplicationModel.UserDataAccounts.Provider.h")
#include "py.Windows.ApplicationModel.UserDataAccounts.Provider.h"
#endif

#if __has_include("py.Windows.Devices.Enumeration.h")
#include "py.Windows.Devices.Enumeration.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Media.SpeechRecognition.h")
#include "py.Windows.Media.SpeechRecognition.h"
#endif

#if __has_include("py.Windows.Security.Authentication.Web.h")
#include "py.Windows.Security.Authentication.Web.h"
#endif

#if __has_include("py.Windows.Security.Authentication.Web.Provider.h")
#include "py.Windows.Security.Authentication.Web.Provider.h"
#endif

#if __has_include("py.Windows.Storage.h")
#include "py.Windows.Storage.h"
#endif

#if __has_include("py.Windows.Storage.Pickers.Provider.h")
#include "py.Windows.Storage.Pickers.Provider.h"
#endif

#if __has_include("py.Windows.Storage.Provider.h")
#include "py.Windows.Storage.Provider.h"
#endif

#if __has_include("py.Windows.Storage.Search.h")
#include "py.Windows.Storage.Search.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#if __has_include("py.Windows.System.h")
#include "py.Windows.System.h"
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

#if __has_include("py.Windows.Web.UI.h")
#include "py.Windows.Web.UI.h"
#endif

#include <winrt/Windows.UI.WebUI.h>

namespace py::proj::Windows::UI::WebUI
{}

namespace py::impl::Windows::UI::WebUI
{
    struct ActivatedEventHandler
    {
        static winrt::Windows::UI::WebUI::ActivatedEventHandler get(PyObject* callable)
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

    struct BackgroundActivatedEventHandler
    {
        static winrt::Windows::UI::WebUI::BackgroundActivatedEventHandler get(PyObject* callable)
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

    struct EnteredBackgroundEventHandler
    {
        static winrt::Windows::UI::WebUI::EnteredBackgroundEventHandler get(PyObject* callable)
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

    struct LeavingBackgroundEventHandler
    {
        static winrt::Windows::UI::WebUI::LeavingBackgroundEventHandler get(PyObject* callable)
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

    struct NavigatedEventHandler
    {
        static winrt::Windows::UI::WebUI::NavigatedEventHandler get(PyObject* callable)
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

    struct ResumingEventHandler
    {
        static winrt::Windows::UI::WebUI::ResumingEventHandler get(PyObject* callable)
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

    struct SuspendingEventHandler
    {
        static winrt::Windows::UI::WebUI::SuspendingEventHandler get(PyObject* callable)
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

namespace py::wrapper::Windows::UI::WebUI
{
    using ActivatedDeferral = py::winrt_wrapper<winrt::Windows::UI::WebUI::ActivatedDeferral>;
    using ActivatedOperation = py::winrt_wrapper<winrt::Windows::UI::WebUI::ActivatedOperation>;
    using BackgroundActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::BackgroundActivatedEventArgs>;
    using EnteredBackgroundEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::EnteredBackgroundEventArgs>;
    using HtmlPrintDocumentSource = py::winrt_wrapper<winrt::Windows::UI::WebUI::HtmlPrintDocumentSource>;
    using LeavingBackgroundEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::LeavingBackgroundEventArgs>;
    using NewWebUIViewCreatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::NewWebUIViewCreatedEventArgs>;
    using SuspendingDeferral = py::winrt_wrapper<winrt::Windows::UI::WebUI::SuspendingDeferral>;
    using SuspendingEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::SuspendingEventArgs>;
    using SuspendingOperation = py::winrt_wrapper<winrt::Windows::UI::WebUI::SuspendingOperation>;
    using WebUIApplication = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIApplication>;
    using WebUIAppointmentsProviderAddAppointmentActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIAppointmentsProviderAddAppointmentActivatedEventArgs>;
    using WebUIAppointmentsProviderRemoveAppointmentActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIAppointmentsProviderRemoveAppointmentActivatedEventArgs>;
    using WebUIAppointmentsProviderReplaceAppointmentActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIAppointmentsProviderReplaceAppointmentActivatedEventArgs>;
    using WebUIAppointmentsProviderShowAppointmentDetailsActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIAppointmentsProviderShowAppointmentDetailsActivatedEventArgs>;
    using WebUIAppointmentsProviderShowTimeFrameActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIAppointmentsProviderShowTimeFrameActivatedEventArgs>;
    using WebUIBackgroundTaskInstance = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIBackgroundTaskInstance>;
    using WebUIBackgroundTaskInstanceRuntimeClass = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIBackgroundTaskInstanceRuntimeClass>;
    using WebUIBarcodeScannerPreviewActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIBarcodeScannerPreviewActivatedEventArgs>;
    using WebUICachedFileUpdaterActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUICachedFileUpdaterActivatedEventArgs>;
    using WebUICommandLineActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUICommandLineActivatedEventArgs>;
    using WebUIContactPanelActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIContactPanelActivatedEventArgs>;
    using WebUIDeviceActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIDeviceActivatedEventArgs>;
    using WebUIDevicePairingActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIDevicePairingActivatedEventArgs>;
    using WebUIDialReceiverActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIDialReceiverActivatedEventArgs>;
    using WebUIFileActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIFileActivatedEventArgs>;
    using WebUIFileOpenPickerActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIFileOpenPickerActivatedEventArgs>;
    using WebUIFileOpenPickerContinuationEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIFileOpenPickerContinuationEventArgs>;
    using WebUIFileSavePickerActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIFileSavePickerActivatedEventArgs>;
    using WebUIFileSavePickerContinuationEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIFileSavePickerContinuationEventArgs>;
    using WebUIFolderPickerContinuationEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIFolderPickerContinuationEventArgs>;
    using WebUILaunchActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUILaunchActivatedEventArgs>;
    using WebUILockScreenActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUILockScreenActivatedEventArgs>;
    using WebUILockScreenComponentActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUILockScreenComponentActivatedEventArgs>;
    using WebUINavigatedDeferral = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUINavigatedDeferral>;
    using WebUINavigatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUINavigatedEventArgs>;
    using WebUINavigatedOperation = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUINavigatedOperation>;
    using WebUIPhoneCallActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIPhoneCallActivatedEventArgs>;
    using WebUIPrintWorkflowForegroundTaskActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIPrintWorkflowForegroundTaskActivatedEventArgs>;
    using WebUIProtocolActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIProtocolActivatedEventArgs>;
    using WebUIProtocolForResultsActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIProtocolForResultsActivatedEventArgs>;
    using WebUIRestrictedLaunchActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIRestrictedLaunchActivatedEventArgs>;
    using WebUIShareTargetActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIShareTargetActivatedEventArgs>;
    using WebUIStartupTaskActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIStartupTaskActivatedEventArgs>;
    using WebUIToastNotificationActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIToastNotificationActivatedEventArgs>;
    using WebUIUserDataAccountProviderActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIUserDataAccountProviderActivatedEventArgs>;
    using WebUIView = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIView>;
    using WebUIVoiceCommandActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIVoiceCommandActivatedEventArgs>;
    using WebUIWebAccountProviderActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIWebAccountProviderActivatedEventArgs>;
    using WebUIWebAuthenticationBrokerContinuationEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::WebUIWebAuthenticationBrokerContinuationEventArgs>;
    using IActivatedEventArgsDeferral = py::winrt_wrapper<winrt::Windows::UI::WebUI::IActivatedEventArgsDeferral>;
    using IWebUIBackgroundTaskInstance = py::winrt_wrapper<winrt::Windows::UI::WebUI::IWebUIBackgroundTaskInstance>;
    using IWebUINavigatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::WebUI::IWebUINavigatedEventArgs>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::ActivatedDeferral>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::ActivatedOperation>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::BackgroundActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::EnteredBackgroundEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::HtmlPrintDocumentSource>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::LeavingBackgroundEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::NewWebUIViewCreatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::SuspendingDeferral>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::SuspendingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::SuspendingOperation>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIApplication>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIAppointmentsProviderAddAppointmentActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIAppointmentsProviderRemoveAppointmentActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIAppointmentsProviderReplaceAppointmentActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIAppointmentsProviderShowAppointmentDetailsActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIAppointmentsProviderShowTimeFrameActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIBackgroundTaskInstance>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIBackgroundTaskInstanceRuntimeClass>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIBarcodeScannerPreviewActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUICachedFileUpdaterActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUICommandLineActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIContactPanelActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIDeviceActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIDevicePairingActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIDialReceiverActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIFileActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIFileOpenPickerActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIFileOpenPickerContinuationEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIFileSavePickerActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIFileSavePickerContinuationEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIFolderPickerContinuationEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUILaunchActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUILockScreenActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUILockScreenComponentActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUINavigatedDeferral>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUINavigatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUINavigatedOperation>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIPhoneCallActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIPrintWorkflowForegroundTaskActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIProtocolActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIProtocolForResultsActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIRestrictedLaunchActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIShareTargetActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIStartupTaskActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIToastNotificationActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIUserDataAccountProviderActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIView>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIVoiceCommandActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIWebAccountProviderActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::WebUIWebAuthenticationBrokerContinuationEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::IActivatedEventArgsDeferral>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::IWebUIBackgroundTaskInstance>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::WebUI::IWebUINavigatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template <>
    struct delegate_python_type<winrt::Windows::UI::WebUI::ActivatedEventHandler>
    {
        using type = py::impl::Windows::UI::WebUI::ActivatedEventHandler;
    };

    template <>
    struct delegate_python_type<winrt::Windows::UI::WebUI::BackgroundActivatedEventHandler>
    {
        using type = py::impl::Windows::UI::WebUI::BackgroundActivatedEventHandler;
    };

    template <>
    struct delegate_python_type<winrt::Windows::UI::WebUI::EnteredBackgroundEventHandler>
    {
        using type = py::impl::Windows::UI::WebUI::EnteredBackgroundEventHandler;
    };

    template <>
    struct delegate_python_type<winrt::Windows::UI::WebUI::LeavingBackgroundEventHandler>
    {
        using type = py::impl::Windows::UI::WebUI::LeavingBackgroundEventHandler;
    };

    template <>
    struct delegate_python_type<winrt::Windows::UI::WebUI::NavigatedEventHandler>
    {
        using type = py::impl::Windows::UI::WebUI::NavigatedEventHandler;
    };

    template <>
    struct delegate_python_type<winrt::Windows::UI::WebUI::ResumingEventHandler>
    {
        using type = py::impl::Windows::UI::WebUI::ResumingEventHandler;
    };

    template <>
    struct delegate_python_type<winrt::Windows::UI::WebUI::SuspendingEventHandler>
    {
        using type = py::impl::Windows::UI::WebUI::SuspendingEventHandler;
    };

}