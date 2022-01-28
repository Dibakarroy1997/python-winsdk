// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.ApplicationModel.ExtendedExecution.Foreground.h"

PyTypeObject* py::winrt_type<winrt::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundRevokedEventArgs>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundSession>::python_type;

namespace py::cpp::Windows::ApplicationModel::ExtendedExecution::Foreground
{
    // ----- ExtendedExecutionForegroundRevokedEventArgs class --------------------
    constexpr const char* const _type_name_ExtendedExecutionForegroundRevokedEventArgs = "ExtendedExecutionForegroundRevokedEventArgs";

    static PyObject* _new_ExtendedExecutionForegroundRevokedEventArgs(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_ExtendedExecutionForegroundRevokedEventArgs);
        return nullptr;
    }

    static void _dealloc_ExtendedExecutionForegroundRevokedEventArgs(py::wrapper::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundRevokedEventArgs* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* ExtendedExecutionForegroundRevokedEventArgs_get_Reason(py::wrapper::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundRevokedEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Reason());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_ExtendedExecutionForegroundRevokedEventArgs(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundRevokedEventArgs>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_ExtendedExecutionForegroundRevokedEventArgs[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_ExtendedExecutionForegroundRevokedEventArgs), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_ExtendedExecutionForegroundRevokedEventArgs[] = {
        { "reason", reinterpret_cast<getter>(ExtendedExecutionForegroundRevokedEventArgs_get_Reason), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_ExtendedExecutionForegroundRevokedEventArgs[] = 
    {
        { Py_tp_new, _new_ExtendedExecutionForegroundRevokedEventArgs },
        { Py_tp_dealloc, _dealloc_ExtendedExecutionForegroundRevokedEventArgs },
        { Py_tp_methods, _methods_ExtendedExecutionForegroundRevokedEventArgs },
        { Py_tp_getset, _getset_ExtendedExecutionForegroundRevokedEventArgs },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_ExtendedExecutionForegroundRevokedEventArgs =
    {
        "_winsdk_Windows_ApplicationModel_ExtendedExecution_Foreground.ExtendedExecutionForegroundRevokedEventArgs",
        sizeof(py::wrapper::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundRevokedEventArgs),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_ExtendedExecutionForegroundRevokedEventArgs
    };

    // ----- ExtendedExecutionForegroundSession class --------------------
    constexpr const char* const _type_name_ExtendedExecutionForegroundSession = "ExtendedExecutionForegroundSession";

    static PyObject* _new_ExtendedExecutionForegroundSession(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        if (kwds != nullptr)
        {
            py::set_invalid_kwd_args_error();
            return nullptr;
        }

        Py_ssize_t arg_count = PyTuple_Size(args);
        if (arg_count == 0)
        {
            try
            {
                winrt::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundSession instance{  };
                return py::wrap(instance, type);
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

    static void _dealloc_ExtendedExecutionForegroundSession(py::wrapper::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundSession* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* ExtendedExecutionForegroundSession_Close(py::wrapper::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundSession* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                self->obj.Close();
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

    static PyObject* ExtendedExecutionForegroundSession_RequestExtensionAsync(py::wrapper::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundSession* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.RequestExtensionAsync());
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

    static PyObject* ExtendedExecutionForegroundSession_get_Reason(py::wrapper::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundSession* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Reason());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int ExtendedExecutionForegroundSession_put_Reason(py::wrapper::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundSession* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundReason>(arg);

            self->obj.Reason(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* ExtendedExecutionForegroundSession_get_Description(py::wrapper::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundSession* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Description());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int ExtendedExecutionForegroundSession_put_Description(py::wrapper::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundSession* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::hstring>(arg);

            self->obj.Description(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* ExtendedExecutionForegroundSession_add_Revoked(py::wrapper::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundSession* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::Windows::Foundation::TypedEventHandler<winrt::Windows::Foundation::IInspectable, winrt::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundRevokedEventArgs>>(arg);

            return py::convert(self->obj.Revoked(param0));
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ExtendedExecutionForegroundSession_remove_Revoked(py::wrapper::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundSession* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::event_token>(arg);

            self->obj.Revoked(param0);
            Py_RETURN_NONE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_ExtendedExecutionForegroundSession(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundSession>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _enter_ExtendedExecutionForegroundSession(py::wrapper::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundSession* self) noexcept
    {
        Py_INCREF(self);
        return reinterpret_cast<PyObject*>(self);
    }

    static PyObject* _exit_ExtendedExecutionForegroundSession(py::wrapper::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundSession* self) noexcept
    {
        try
        {
            self->obj.Close();
            Py_RETURN_FALSE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_ExtendedExecutionForegroundSession[] = {
        { "close", reinterpret_cast<PyCFunction>(ExtendedExecutionForegroundSession_Close), METH_VARARGS, nullptr },
        { "request_extension_async", reinterpret_cast<PyCFunction>(ExtendedExecutionForegroundSession_RequestExtensionAsync), METH_VARARGS, nullptr },
        { "add_revoked", reinterpret_cast<PyCFunction>(ExtendedExecutionForegroundSession_add_Revoked), METH_O, nullptr },
        { "remove_revoked", reinterpret_cast<PyCFunction>(ExtendedExecutionForegroundSession_remove_Revoked), METH_O, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_ExtendedExecutionForegroundSession), METH_O | METH_STATIC, nullptr },
        { "__enter__", reinterpret_cast<PyCFunction>(_enter_ExtendedExecutionForegroundSession), METH_NOARGS, nullptr },
        { "__exit__",  reinterpret_cast<PyCFunction>(_exit_ExtendedExecutionForegroundSession), METH_VARARGS, nullptr },
        { }
    };

    static PyGetSetDef _getset_ExtendedExecutionForegroundSession[] = {
        { "reason", reinterpret_cast<getter>(ExtendedExecutionForegroundSession_get_Reason), reinterpret_cast<setter>(ExtendedExecutionForegroundSession_put_Reason), nullptr, nullptr },
        { "description", reinterpret_cast<getter>(ExtendedExecutionForegroundSession_get_Description), reinterpret_cast<setter>(ExtendedExecutionForegroundSession_put_Description), nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_ExtendedExecutionForegroundSession[] = 
    {
        { Py_tp_new, _new_ExtendedExecutionForegroundSession },
        { Py_tp_dealloc, _dealloc_ExtendedExecutionForegroundSession },
        { Py_tp_methods, _methods_ExtendedExecutionForegroundSession },
        { Py_tp_getset, _getset_ExtendedExecutionForegroundSession },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_ExtendedExecutionForegroundSession =
    {
        "_winsdk_Windows_ApplicationModel_ExtendedExecution_Foreground.ExtendedExecutionForegroundSession",
        sizeof(py::wrapper::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundSession),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_ExtendedExecutionForegroundSession
    };

    // ----- Windows.ApplicationModel.ExtendedExecution.Foreground Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundRevokedEventArgs>::python_type = py::register_python_type(module, _type_name_ExtendedExecutionForegroundRevokedEventArgs, &_type_spec_ExtendedExecutionForegroundRevokedEventArgs, bases.get());
            py::winrt_type<winrt::Windows::ApplicationModel::ExtendedExecution::Foreground::ExtendedExecutionForegroundSession>::python_type = py::register_python_type(module, _type_name_ExtendedExecutionForegroundSession, &_type_spec_ExtendedExecutionForegroundSession, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.ApplicationModel.ExtendedExecution.Foreground");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_ApplicationModel_ExtendedExecution_Foreground",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::ApplicationModel::ExtendedExecution::Foreground

PyMODINIT_FUNC
PyInit__winsdk_Windows_ApplicationModel_ExtendedExecution_Foreground (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::ApplicationModel::ExtendedExecution::Foreground::module_def);
}