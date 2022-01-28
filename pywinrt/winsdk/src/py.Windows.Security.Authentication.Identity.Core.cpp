// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.Security.Authentication.Identity.Core.h"

PyTypeObject* py::winrt_type<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorAuthenticationManager>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorGetSessionsResult>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorOneTimeCodedInfo>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorSessionInfo>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo>::python_type;

namespace py::cpp::Windows::Security::Authentication::Identity::Core
{
    // ----- MicrosoftAccountMultiFactorAuthenticationManager class --------------------
    constexpr const char* const _type_name_MicrosoftAccountMultiFactorAuthenticationManager = "MicrosoftAccountMultiFactorAuthenticationManager";

    static PyObject* _new_MicrosoftAccountMultiFactorAuthenticationManager(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_MicrosoftAccountMultiFactorAuthenticationManager);
        return nullptr;
    }

    static void _dealloc_MicrosoftAccountMultiFactorAuthenticationManager(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorAuthenticationManager* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* MicrosoftAccountMultiFactorAuthenticationManager_AddDeviceAsync(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorAuthenticationManager* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 3)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);
                auto param1 = py::convert_to<winrt::hstring>(args, 1);
                auto param2 = py::convert_to<winrt::hstring>(args, 2);

                return py::convert(self->obj.AddDeviceAsync(param0, param1, param2));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorAuthenticationManager_ApproveSessionAsync(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorAuthenticationManager* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 2)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorSessionAuthenticationStatus>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorSessionInfo>(args, 1);

                return py::convert(self->obj.ApproveSessionAsync(param0, param1));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 4)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorSessionAuthenticationStatus>(args, 0);
                auto param1 = py::convert_to<winrt::hstring>(args, 1);
                auto param2 = py::convert_to<winrt::hstring>(args, 2);
                auto param3 = py::convert_to<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorAuthenticationType>(args, 3);

                return py::convert(self->obj.ApproveSessionAsync(param0, param1, param2, param3));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorAuthenticationManager_DenySessionAsync(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorAuthenticationManager* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorSessionInfo>(args, 0);

                return py::convert(self->obj.DenySessionAsync(param0));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 3)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);
                auto param1 = py::convert_to<winrt::hstring>(args, 1);
                auto param2 = py::convert_to<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorAuthenticationType>(args, 2);

                return py::convert(self->obj.DenySessionAsync(param0, param1, param2));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorAuthenticationManager_GetOneTimePassCodeAsync(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorAuthenticationManager* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 2)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);
                auto param1 = py::convert_to<uint32_t>(args, 1);

                return py::convert(self->obj.GetOneTimePassCodeAsync(param0, param1));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorAuthenticationManager_GetSessionsAndUnregisteredAccountsAsync(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorAuthenticationManager* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Foundation::Collections::IIterable<winrt::hstring>>(args, 0);

                return py::convert(self->obj.GetSessionsAndUnregisteredAccountsAsync(param0));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorAuthenticationManager_GetSessionsAsync(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorAuthenticationManager* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Foundation::Collections::IIterable<winrt::hstring>>(args, 0);

                return py::convert(self->obj.GetSessionsAsync(param0));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorAuthenticationManager_RemoveDeviceAsync(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorAuthenticationManager* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(self->obj.RemoveDeviceAsync(param0));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorAuthenticationManager_UpdateWnsChannelAsync(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorAuthenticationManager* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 2)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);
                auto param1 = py::convert_to<winrt::hstring>(args, 1);

                return py::convert(self->obj.UpdateWnsChannelAsync(param0, param1));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorAuthenticationManager_get_Current(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorAuthenticationManager::Current());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_MicrosoftAccountMultiFactorAuthenticationManager(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorAuthenticationManager>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_MicrosoftAccountMultiFactorAuthenticationManager[] = {
        { "add_device_async", reinterpret_cast<PyCFunction>(MicrosoftAccountMultiFactorAuthenticationManager_AddDeviceAsync), METH_VARARGS, nullptr },
        { "approve_session_async", reinterpret_cast<PyCFunction>(MicrosoftAccountMultiFactorAuthenticationManager_ApproveSessionAsync), METH_VARARGS, nullptr },
        { "deny_session_async", reinterpret_cast<PyCFunction>(MicrosoftAccountMultiFactorAuthenticationManager_DenySessionAsync), METH_VARARGS, nullptr },
        { "get_one_time_pass_code_async", reinterpret_cast<PyCFunction>(MicrosoftAccountMultiFactorAuthenticationManager_GetOneTimePassCodeAsync), METH_VARARGS, nullptr },
        { "get_sessions_and_unregistered_accounts_async", reinterpret_cast<PyCFunction>(MicrosoftAccountMultiFactorAuthenticationManager_GetSessionsAndUnregisteredAccountsAsync), METH_VARARGS, nullptr },
        { "get_sessions_async", reinterpret_cast<PyCFunction>(MicrosoftAccountMultiFactorAuthenticationManager_GetSessionsAsync), METH_VARARGS, nullptr },
        { "remove_device_async", reinterpret_cast<PyCFunction>(MicrosoftAccountMultiFactorAuthenticationManager_RemoveDeviceAsync), METH_VARARGS, nullptr },
        { "update_wns_channel_async", reinterpret_cast<PyCFunction>(MicrosoftAccountMultiFactorAuthenticationManager_UpdateWnsChannelAsync), METH_VARARGS, nullptr },
        { "get_current", reinterpret_cast<PyCFunction>(MicrosoftAccountMultiFactorAuthenticationManager_get_Current), METH_NOARGS | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_MicrosoftAccountMultiFactorAuthenticationManager), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_MicrosoftAccountMultiFactorAuthenticationManager[] = {
        { }
    };

    static PyType_Slot _type_slots_MicrosoftAccountMultiFactorAuthenticationManager[] = 
    {
        { Py_tp_new, _new_MicrosoftAccountMultiFactorAuthenticationManager },
        { Py_tp_dealloc, _dealloc_MicrosoftAccountMultiFactorAuthenticationManager },
        { Py_tp_methods, _methods_MicrosoftAccountMultiFactorAuthenticationManager },
        { Py_tp_getset, _getset_MicrosoftAccountMultiFactorAuthenticationManager },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_MicrosoftAccountMultiFactorAuthenticationManager =
    {
        "_winsdk_Windows_Security_Authentication_Identity_Core.MicrosoftAccountMultiFactorAuthenticationManager",
        sizeof(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorAuthenticationManager),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_MicrosoftAccountMultiFactorAuthenticationManager
    };

    // ----- MicrosoftAccountMultiFactorGetSessionsResult class --------------------
    constexpr const char* const _type_name_MicrosoftAccountMultiFactorGetSessionsResult = "MicrosoftAccountMultiFactorGetSessionsResult";

    static PyObject* _new_MicrosoftAccountMultiFactorGetSessionsResult(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_MicrosoftAccountMultiFactorGetSessionsResult);
        return nullptr;
    }

    static void _dealloc_MicrosoftAccountMultiFactorGetSessionsResult(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorGetSessionsResult* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* MicrosoftAccountMultiFactorGetSessionsResult_get_ServiceResponse(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorGetSessionsResult* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ServiceResponse());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorGetSessionsResult_get_Sessions(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorGetSessionsResult* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Sessions());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_MicrosoftAccountMultiFactorGetSessionsResult(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorGetSessionsResult>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_MicrosoftAccountMultiFactorGetSessionsResult[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_MicrosoftAccountMultiFactorGetSessionsResult), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_MicrosoftAccountMultiFactorGetSessionsResult[] = {
        { "service_response", reinterpret_cast<getter>(MicrosoftAccountMultiFactorGetSessionsResult_get_ServiceResponse), nullptr, nullptr, nullptr },
        { "sessions", reinterpret_cast<getter>(MicrosoftAccountMultiFactorGetSessionsResult_get_Sessions), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_MicrosoftAccountMultiFactorGetSessionsResult[] = 
    {
        { Py_tp_new, _new_MicrosoftAccountMultiFactorGetSessionsResult },
        { Py_tp_dealloc, _dealloc_MicrosoftAccountMultiFactorGetSessionsResult },
        { Py_tp_methods, _methods_MicrosoftAccountMultiFactorGetSessionsResult },
        { Py_tp_getset, _getset_MicrosoftAccountMultiFactorGetSessionsResult },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_MicrosoftAccountMultiFactorGetSessionsResult =
    {
        "_winsdk_Windows_Security_Authentication_Identity_Core.MicrosoftAccountMultiFactorGetSessionsResult",
        sizeof(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorGetSessionsResult),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_MicrosoftAccountMultiFactorGetSessionsResult
    };

    // ----- MicrosoftAccountMultiFactorOneTimeCodedInfo class --------------------
    constexpr const char* const _type_name_MicrosoftAccountMultiFactorOneTimeCodedInfo = "MicrosoftAccountMultiFactorOneTimeCodedInfo";

    static PyObject* _new_MicrosoftAccountMultiFactorOneTimeCodedInfo(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_MicrosoftAccountMultiFactorOneTimeCodedInfo);
        return nullptr;
    }

    static void _dealloc_MicrosoftAccountMultiFactorOneTimeCodedInfo(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorOneTimeCodedInfo* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* MicrosoftAccountMultiFactorOneTimeCodedInfo_get_Code(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorOneTimeCodedInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Code());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorOneTimeCodedInfo_get_ServiceResponse(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorOneTimeCodedInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ServiceResponse());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorOneTimeCodedInfo_get_TimeInterval(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorOneTimeCodedInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.TimeInterval());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorOneTimeCodedInfo_get_TimeToLive(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorOneTimeCodedInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.TimeToLive());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_MicrosoftAccountMultiFactorOneTimeCodedInfo(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorOneTimeCodedInfo>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_MicrosoftAccountMultiFactorOneTimeCodedInfo[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_MicrosoftAccountMultiFactorOneTimeCodedInfo), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_MicrosoftAccountMultiFactorOneTimeCodedInfo[] = {
        { "code", reinterpret_cast<getter>(MicrosoftAccountMultiFactorOneTimeCodedInfo_get_Code), nullptr, nullptr, nullptr },
        { "service_response", reinterpret_cast<getter>(MicrosoftAccountMultiFactorOneTimeCodedInfo_get_ServiceResponse), nullptr, nullptr, nullptr },
        { "time_interval", reinterpret_cast<getter>(MicrosoftAccountMultiFactorOneTimeCodedInfo_get_TimeInterval), nullptr, nullptr, nullptr },
        { "time_to_live", reinterpret_cast<getter>(MicrosoftAccountMultiFactorOneTimeCodedInfo_get_TimeToLive), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_MicrosoftAccountMultiFactorOneTimeCodedInfo[] = 
    {
        { Py_tp_new, _new_MicrosoftAccountMultiFactorOneTimeCodedInfo },
        { Py_tp_dealloc, _dealloc_MicrosoftAccountMultiFactorOneTimeCodedInfo },
        { Py_tp_methods, _methods_MicrosoftAccountMultiFactorOneTimeCodedInfo },
        { Py_tp_getset, _getset_MicrosoftAccountMultiFactorOneTimeCodedInfo },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_MicrosoftAccountMultiFactorOneTimeCodedInfo =
    {
        "_winsdk_Windows_Security_Authentication_Identity_Core.MicrosoftAccountMultiFactorOneTimeCodedInfo",
        sizeof(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorOneTimeCodedInfo),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_MicrosoftAccountMultiFactorOneTimeCodedInfo
    };

    // ----- MicrosoftAccountMultiFactorSessionInfo class --------------------
    constexpr const char* const _type_name_MicrosoftAccountMultiFactorSessionInfo = "MicrosoftAccountMultiFactorSessionInfo";

    static PyObject* _new_MicrosoftAccountMultiFactorSessionInfo(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_MicrosoftAccountMultiFactorSessionInfo);
        return nullptr;
    }

    static void _dealloc_MicrosoftAccountMultiFactorSessionInfo(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorSessionInfo* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* MicrosoftAccountMultiFactorSessionInfo_get_ApprovalStatus(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorSessionInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ApprovalStatus());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorSessionInfo_get_AuthenticationType(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorSessionInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.AuthenticationType());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorSessionInfo_get_DisplaySessionId(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorSessionInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.DisplaySessionId());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorSessionInfo_get_ExpirationTime(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorSessionInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ExpirationTime());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorSessionInfo_get_RequestTime(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorSessionInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.RequestTime());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorSessionInfo_get_SessionId(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorSessionInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.SessionId());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorSessionInfo_get_UserAccountId(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorSessionInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.UserAccountId());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_MicrosoftAccountMultiFactorSessionInfo(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorSessionInfo>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_MicrosoftAccountMultiFactorSessionInfo[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_MicrosoftAccountMultiFactorSessionInfo), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_MicrosoftAccountMultiFactorSessionInfo[] = {
        { "approval_status", reinterpret_cast<getter>(MicrosoftAccountMultiFactorSessionInfo_get_ApprovalStatus), nullptr, nullptr, nullptr },
        { "authentication_type", reinterpret_cast<getter>(MicrosoftAccountMultiFactorSessionInfo_get_AuthenticationType), nullptr, nullptr, nullptr },
        { "display_session_id", reinterpret_cast<getter>(MicrosoftAccountMultiFactorSessionInfo_get_DisplaySessionId), nullptr, nullptr, nullptr },
        { "expiration_time", reinterpret_cast<getter>(MicrosoftAccountMultiFactorSessionInfo_get_ExpirationTime), nullptr, nullptr, nullptr },
        { "request_time", reinterpret_cast<getter>(MicrosoftAccountMultiFactorSessionInfo_get_RequestTime), nullptr, nullptr, nullptr },
        { "session_id", reinterpret_cast<getter>(MicrosoftAccountMultiFactorSessionInfo_get_SessionId), nullptr, nullptr, nullptr },
        { "user_account_id", reinterpret_cast<getter>(MicrosoftAccountMultiFactorSessionInfo_get_UserAccountId), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_MicrosoftAccountMultiFactorSessionInfo[] = 
    {
        { Py_tp_new, _new_MicrosoftAccountMultiFactorSessionInfo },
        { Py_tp_dealloc, _dealloc_MicrosoftAccountMultiFactorSessionInfo },
        { Py_tp_methods, _methods_MicrosoftAccountMultiFactorSessionInfo },
        { Py_tp_getset, _getset_MicrosoftAccountMultiFactorSessionInfo },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_MicrosoftAccountMultiFactorSessionInfo =
    {
        "_winsdk_Windows_Security_Authentication_Identity_Core.MicrosoftAccountMultiFactorSessionInfo",
        sizeof(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorSessionInfo),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_MicrosoftAccountMultiFactorSessionInfo
    };

    // ----- MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo class --------------------
    constexpr const char* const _type_name_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo = "MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo";

    static PyObject* _new_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo);
        return nullptr;
    }

    static void _dealloc_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo_get_ServiceResponse(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ServiceResponse());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo_get_Sessions(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Sessions());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo_get_UnregisteredAccounts(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.UnregisteredAccounts());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo[] = {
        { "service_response", reinterpret_cast<getter>(MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo_get_ServiceResponse), nullptr, nullptr, nullptr },
        { "sessions", reinterpret_cast<getter>(MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo_get_Sessions), nullptr, nullptr, nullptr },
        { "unregistered_accounts", reinterpret_cast<getter>(MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo_get_UnregisteredAccounts), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo[] = 
    {
        { Py_tp_new, _new_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo },
        { Py_tp_dealloc, _dealloc_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo },
        { Py_tp_methods, _methods_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo },
        { Py_tp_getset, _getset_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo =
    {
        "_winsdk_Windows_Security_Authentication_Identity_Core.MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo",
        sizeof(py::wrapper::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo
    };

    // ----- Windows.Security.Authentication.Identity.Core Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorAuthenticationManager>::python_type = py::register_python_type(module, _type_name_MicrosoftAccountMultiFactorAuthenticationManager, &_type_spec_MicrosoftAccountMultiFactorAuthenticationManager, bases.get());
            py::winrt_type<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorGetSessionsResult>::python_type = py::register_python_type(module, _type_name_MicrosoftAccountMultiFactorGetSessionsResult, &_type_spec_MicrosoftAccountMultiFactorGetSessionsResult, bases.get());
            py::winrt_type<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorOneTimeCodedInfo>::python_type = py::register_python_type(module, _type_name_MicrosoftAccountMultiFactorOneTimeCodedInfo, &_type_spec_MicrosoftAccountMultiFactorOneTimeCodedInfo, bases.get());
            py::winrt_type<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorSessionInfo>::python_type = py::register_python_type(module, _type_name_MicrosoftAccountMultiFactorSessionInfo, &_type_spec_MicrosoftAccountMultiFactorSessionInfo, bases.get());
            py::winrt_type<winrt::Windows::Security::Authentication::Identity::Core::MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo>::python_type = py::register_python_type(module, _type_name_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo, &_type_spec_MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Security.Authentication.Identity.Core");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Security_Authentication_Identity_Core",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Security::Authentication::Identity::Core

PyMODINIT_FUNC
PyInit__winsdk_Windows_Security_Authentication_Identity_Core (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Security::Authentication::Identity::Core::module_def);
}