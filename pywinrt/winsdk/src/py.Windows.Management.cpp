// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.Management.h"

PyTypeObject* py::winrt_type<winrt::Windows::Management::MdmAlert>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Management::MdmSession>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Management::MdmSessionManager>::python_type;

namespace py::cpp::Windows::Management
{
    // ----- MdmAlert class --------------------
    constexpr const char* const _type_name_MdmAlert = "MdmAlert";

    static PyObject* _new_MdmAlert(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
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
                winrt::Windows::Management::MdmAlert instance{  };
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

    static void _dealloc_MdmAlert(py::wrapper::Windows::Management::MdmAlert* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* MdmAlert_get_Type(py::wrapper::Windows::Management::MdmAlert* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Type());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int MdmAlert_put_Type(py::wrapper::Windows::Management::MdmAlert* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::hstring>(arg);

            self->obj.Type(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* MdmAlert_get_Target(py::wrapper::Windows::Management::MdmAlert* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Target());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int MdmAlert_put_Target(py::wrapper::Windows::Management::MdmAlert* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::hstring>(arg);

            self->obj.Target(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* MdmAlert_get_Source(py::wrapper::Windows::Management::MdmAlert* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Source());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int MdmAlert_put_Source(py::wrapper::Windows::Management::MdmAlert* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::hstring>(arg);

            self->obj.Source(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* MdmAlert_get_Mark(py::wrapper::Windows::Management::MdmAlert* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Mark());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int MdmAlert_put_Mark(py::wrapper::Windows::Management::MdmAlert* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Management::MdmAlertMark>(arg);

            self->obj.Mark(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* MdmAlert_get_Format(py::wrapper::Windows::Management::MdmAlert* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Format());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int MdmAlert_put_Format(py::wrapper::Windows::Management::MdmAlert* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Management::MdmAlertDataType>(arg);

            self->obj.Format(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* MdmAlert_get_Data(py::wrapper::Windows::Management::MdmAlert* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Data());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int MdmAlert_put_Data(py::wrapper::Windows::Management::MdmAlert* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::hstring>(arg);

            self->obj.Data(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* MdmAlert_get_Status(py::wrapper::Windows::Management::MdmAlert* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Status());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_MdmAlert(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Management::MdmAlert>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_MdmAlert[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_MdmAlert), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_MdmAlert[] = {
        { "type", reinterpret_cast<getter>(MdmAlert_get_Type), reinterpret_cast<setter>(MdmAlert_put_Type), nullptr, nullptr },
        { "target", reinterpret_cast<getter>(MdmAlert_get_Target), reinterpret_cast<setter>(MdmAlert_put_Target), nullptr, nullptr },
        { "source", reinterpret_cast<getter>(MdmAlert_get_Source), reinterpret_cast<setter>(MdmAlert_put_Source), nullptr, nullptr },
        { "mark", reinterpret_cast<getter>(MdmAlert_get_Mark), reinterpret_cast<setter>(MdmAlert_put_Mark), nullptr, nullptr },
        { "format", reinterpret_cast<getter>(MdmAlert_get_Format), reinterpret_cast<setter>(MdmAlert_put_Format), nullptr, nullptr },
        { "data", reinterpret_cast<getter>(MdmAlert_get_Data), reinterpret_cast<setter>(MdmAlert_put_Data), nullptr, nullptr },
        { "status", reinterpret_cast<getter>(MdmAlert_get_Status), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_MdmAlert[] = 
    {
        { Py_tp_new, _new_MdmAlert },
        { Py_tp_dealloc, _dealloc_MdmAlert },
        { Py_tp_methods, _methods_MdmAlert },
        { Py_tp_getset, _getset_MdmAlert },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_MdmAlert =
    {
        "_winsdk_Windows_Management.MdmAlert",
        sizeof(py::wrapper::Windows::Management::MdmAlert),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_MdmAlert
    };

    // ----- MdmSession class --------------------
    constexpr const char* const _type_name_MdmSession = "MdmSession";

    static PyObject* _new_MdmSession(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_MdmSession);
        return nullptr;
    }

    static void _dealloc_MdmSession(py::wrapper::Windows::Management::MdmSession* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* MdmSession_AttachAsync(py::wrapper::Windows::Management::MdmSession* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.AttachAsync());
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

    static PyObject* MdmSession_Delete(py::wrapper::Windows::Management::MdmSession* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                self->obj.Delete();
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

    static PyObject* MdmSession_StartAsync(py::wrapper::Windows::Management::MdmSession* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.StartAsync());
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Foundation::Collections::IIterable<winrt::Windows::Management::MdmAlert>>(args, 0);

                return py::convert(self->obj.StartAsync(param0));
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

    static PyObject* MdmSession_get_Alerts(py::wrapper::Windows::Management::MdmSession* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Alerts());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* MdmSession_get_ExtendedError(py::wrapper::Windows::Management::MdmSession* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ExtendedError());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* MdmSession_get_Id(py::wrapper::Windows::Management::MdmSession* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Id());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* MdmSession_get_State(py::wrapper::Windows::Management::MdmSession* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.State());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_MdmSession(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Management::MdmSession>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_MdmSession[] = {
        { "attach_async", reinterpret_cast<PyCFunction>(MdmSession_AttachAsync), METH_VARARGS, nullptr },
        { "delete", reinterpret_cast<PyCFunction>(MdmSession_Delete), METH_VARARGS, nullptr },
        { "start_async", reinterpret_cast<PyCFunction>(MdmSession_StartAsync), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_MdmSession), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_MdmSession[] = {
        { "alerts", reinterpret_cast<getter>(MdmSession_get_Alerts), nullptr, nullptr, nullptr },
        { "extended_error", reinterpret_cast<getter>(MdmSession_get_ExtendedError), nullptr, nullptr, nullptr },
        { "id", reinterpret_cast<getter>(MdmSession_get_Id), nullptr, nullptr, nullptr },
        { "state", reinterpret_cast<getter>(MdmSession_get_State), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_MdmSession[] = 
    {
        { Py_tp_new, _new_MdmSession },
        { Py_tp_dealloc, _dealloc_MdmSession },
        { Py_tp_methods, _methods_MdmSession },
        { Py_tp_getset, _getset_MdmSession },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_MdmSession =
    {
        "_winsdk_Windows_Management.MdmSession",
        sizeof(py::wrapper::Windows::Management::MdmSession),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_MdmSession
    };

    // ----- MdmSessionManager class --------------------
    constexpr const char* const _type_name_MdmSessionManager = "MdmSessionManager";

    static PyObject* _new_MdmSessionManager(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_MdmSessionManager);
        return nullptr;
    }

    static PyObject* MdmSessionManager_DeleteSessionById(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                winrt::Windows::Management::MdmSessionManager::DeleteSessionById(param0);
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

    static PyObject* MdmSessionManager_GetSessionById(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(winrt::Windows::Management::MdmSessionManager::GetSessionById(param0));
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

    static PyObject* MdmSessionManager_TryCreateSession(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(winrt::Windows::Management::MdmSessionManager::TryCreateSession());
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

    static PyObject* MdmSessionManager_get_SessionIds(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Management::MdmSessionManager::SessionIds());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_MdmSessionManager[] = {
        { "delete_session_by_id", reinterpret_cast<PyCFunction>(MdmSessionManager_DeleteSessionById), METH_VARARGS | METH_STATIC, nullptr },
        { "get_session_by_id", reinterpret_cast<PyCFunction>(MdmSessionManager_GetSessionById), METH_VARARGS | METH_STATIC, nullptr },
        { "try_create_session", reinterpret_cast<PyCFunction>(MdmSessionManager_TryCreateSession), METH_VARARGS | METH_STATIC, nullptr },
        { "get_session_ids", reinterpret_cast<PyCFunction>(MdmSessionManager_get_SessionIds), METH_NOARGS | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_MdmSessionManager[] = {
        { }
    };

    static PyType_Slot _type_slots_MdmSessionManager[] = 
    {
        { Py_tp_new, _new_MdmSessionManager },
        { Py_tp_methods, _methods_MdmSessionManager },
        { Py_tp_getset, _getset_MdmSessionManager },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_MdmSessionManager =
    {
        "_winsdk_Windows_Management.MdmSessionManager",
        0,
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_MdmSessionManager
    };

    // ----- Windows.Management Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Management::MdmAlert>::python_type = py::register_python_type(module, _type_name_MdmAlert, &_type_spec_MdmAlert, bases.get());
            py::winrt_type<winrt::Windows::Management::MdmSession>::python_type = py::register_python_type(module, _type_name_MdmSession, &_type_spec_MdmSession, bases.get());
            py::winrt_type<winrt::Windows::Management::MdmSessionManager>::python_type = py::register_python_type(module, _type_name_MdmSessionManager, &_type_spec_MdmSessionManager, nullptr);

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Management");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Management",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Management

PyMODINIT_FUNC
PyInit__winsdk_Windows_Management (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Management::module_def);
}