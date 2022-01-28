// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.Security.Authentication.Web.h"

PyTypeObject* py::winrt_type<winrt::Windows::Security::Authentication::Web::WebAuthenticationBroker>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Security::Authentication::Web::WebAuthenticationResult>::python_type;

namespace py::cpp::Windows::Security::Authentication::Web
{
    // ----- WebAuthenticationBroker class --------------------
    constexpr const char* const _type_name_WebAuthenticationBroker = "WebAuthenticationBroker";

    static PyObject* _new_WebAuthenticationBroker(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_WebAuthenticationBroker);
        return nullptr;
    }

    static PyObject* WebAuthenticationBroker_AuthenticateAndContinue(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Foundation::Uri>(args, 0);

                winrt::Windows::Security::Authentication::Web::WebAuthenticationBroker::AuthenticateAndContinue(param0);
                Py_RETURN_NONE;
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 2)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Foundation::Uri>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Foundation::Uri>(args, 1);

                winrt::Windows::Security::Authentication::Web::WebAuthenticationBroker::AuthenticateAndContinue(param0, param1);
                Py_RETURN_NONE;
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
                auto param0 = py::convert_to<winrt::Windows::Foundation::Uri>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Foundation::Uri>(args, 1);
                auto param2 = py::convert_to<winrt::Windows::Foundation::Collections::ValueSet>(args, 2);
                auto param3 = py::convert_to<winrt::Windows::Security::Authentication::Web::WebAuthenticationOptions>(args, 3);

                winrt::Windows::Security::Authentication::Web::WebAuthenticationBroker::AuthenticateAndContinue(param0, param1, param2, param3);
                Py_RETURN_NONE;
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

    static PyObject* WebAuthenticationBroker_AuthenticateAsync(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 2)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Security::Authentication::Web::WebAuthenticationOptions>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Foundation::Uri>(args, 1);

                return py::convert(winrt::Windows::Security::Authentication::Web::WebAuthenticationBroker::AuthenticateAsync(param0, param1));
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
                auto param0 = py::convert_to<winrt::Windows::Security::Authentication::Web::WebAuthenticationOptions>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Foundation::Uri>(args, 1);
                auto param2 = py::convert_to<winrt::Windows::Foundation::Uri>(args, 2);

                return py::convert(winrt::Windows::Security::Authentication::Web::WebAuthenticationBroker::AuthenticateAsync(param0, param1, param2));
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

    static PyObject* WebAuthenticationBroker_AuthenticateSilentlyAsync(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Foundation::Uri>(args, 0);

                return py::convert(winrt::Windows::Security::Authentication::Web::WebAuthenticationBroker::AuthenticateSilentlyAsync(param0));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 2)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Foundation::Uri>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Security::Authentication::Web::WebAuthenticationOptions>(args, 1);

                return py::convert(winrt::Windows::Security::Authentication::Web::WebAuthenticationBroker::AuthenticateSilentlyAsync(param0, param1));
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

    static PyObject* WebAuthenticationBroker_GetCurrentApplicationCallbackUri(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(winrt::Windows::Security::Authentication::Web::WebAuthenticationBroker::GetCurrentApplicationCallbackUri());
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

    static PyMethodDef _methods_WebAuthenticationBroker[] = {
        { "authenticate_and_continue", reinterpret_cast<PyCFunction>(WebAuthenticationBroker_AuthenticateAndContinue), METH_VARARGS | METH_STATIC, nullptr },
        { "authenticate_async", reinterpret_cast<PyCFunction>(WebAuthenticationBroker_AuthenticateAsync), METH_VARARGS | METH_STATIC, nullptr },
        { "authenticate_silently_async", reinterpret_cast<PyCFunction>(WebAuthenticationBroker_AuthenticateSilentlyAsync), METH_VARARGS | METH_STATIC, nullptr },
        { "get_current_application_callback_uri", reinterpret_cast<PyCFunction>(WebAuthenticationBroker_GetCurrentApplicationCallbackUri), METH_VARARGS | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_WebAuthenticationBroker[] = {
        { }
    };

    static PyType_Slot _type_slots_WebAuthenticationBroker[] = 
    {
        { Py_tp_new, _new_WebAuthenticationBroker },
        { Py_tp_methods, _methods_WebAuthenticationBroker },
        { Py_tp_getset, _getset_WebAuthenticationBroker },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_WebAuthenticationBroker =
    {
        "_winsdk_Windows_Security_Authentication_Web.WebAuthenticationBroker",
        0,
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_WebAuthenticationBroker
    };

    // ----- WebAuthenticationResult class --------------------
    constexpr const char* const _type_name_WebAuthenticationResult = "WebAuthenticationResult";

    static PyObject* _new_WebAuthenticationResult(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_WebAuthenticationResult);
        return nullptr;
    }

    static void _dealloc_WebAuthenticationResult(py::wrapper::Windows::Security::Authentication::Web::WebAuthenticationResult* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* WebAuthenticationResult_get_ResponseData(py::wrapper::Windows::Security::Authentication::Web::WebAuthenticationResult* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ResponseData());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* WebAuthenticationResult_get_ResponseErrorDetail(py::wrapper::Windows::Security::Authentication::Web::WebAuthenticationResult* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ResponseErrorDetail());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* WebAuthenticationResult_get_ResponseStatus(py::wrapper::Windows::Security::Authentication::Web::WebAuthenticationResult* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ResponseStatus());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_WebAuthenticationResult(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Security::Authentication::Web::WebAuthenticationResult>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_WebAuthenticationResult[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_WebAuthenticationResult), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_WebAuthenticationResult[] = {
        { "response_data", reinterpret_cast<getter>(WebAuthenticationResult_get_ResponseData), nullptr, nullptr, nullptr },
        { "response_error_detail", reinterpret_cast<getter>(WebAuthenticationResult_get_ResponseErrorDetail), nullptr, nullptr, nullptr },
        { "response_status", reinterpret_cast<getter>(WebAuthenticationResult_get_ResponseStatus), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_WebAuthenticationResult[] = 
    {
        { Py_tp_new, _new_WebAuthenticationResult },
        { Py_tp_dealloc, _dealloc_WebAuthenticationResult },
        { Py_tp_methods, _methods_WebAuthenticationResult },
        { Py_tp_getset, _getset_WebAuthenticationResult },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_WebAuthenticationResult =
    {
        "_winsdk_Windows_Security_Authentication_Web.WebAuthenticationResult",
        sizeof(py::wrapper::Windows::Security::Authentication::Web::WebAuthenticationResult),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_WebAuthenticationResult
    };

    // ----- Windows.Security.Authentication.Web Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Security::Authentication::Web::WebAuthenticationBroker>::python_type = py::register_python_type(module, _type_name_WebAuthenticationBroker, &_type_spec_WebAuthenticationBroker, nullptr);
            py::winrt_type<winrt::Windows::Security::Authentication::Web::WebAuthenticationResult>::python_type = py::register_python_type(module, _type_name_WebAuthenticationResult, &_type_spec_WebAuthenticationResult, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Security.Authentication.Web");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Security_Authentication_Web",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Security::Authentication::Web

PyMODINIT_FUNC
PyInit__winsdk_Windows_Security_Authentication_Web (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Security::Authentication::Web::module_def);
}