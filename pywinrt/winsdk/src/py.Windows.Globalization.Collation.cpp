// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.Globalization.Collation.h"

PyTypeObject* py::winrt_type<winrt::Windows::Globalization::Collation::CharacterGrouping>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Globalization::Collation::CharacterGroupings>::python_type;

namespace py::cpp::Windows::Globalization::Collation
{
    // ----- CharacterGrouping class --------------------
    constexpr const char* const _type_name_CharacterGrouping = "CharacterGrouping";

    static PyObject* _new_CharacterGrouping(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_CharacterGrouping);
        return nullptr;
    }

    static void _dealloc_CharacterGrouping(py::wrapper::Windows::Globalization::Collation::CharacterGrouping* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* CharacterGrouping_get_First(py::wrapper::Windows::Globalization::Collation::CharacterGrouping* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.First());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* CharacterGrouping_get_Label(py::wrapper::Windows::Globalization::Collation::CharacterGrouping* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Label());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_CharacterGrouping(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Globalization::Collation::CharacterGrouping>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_CharacterGrouping[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_CharacterGrouping), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_CharacterGrouping[] = {
        { "first", reinterpret_cast<getter>(CharacterGrouping_get_First), nullptr, nullptr, nullptr },
        { "label", reinterpret_cast<getter>(CharacterGrouping_get_Label), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_CharacterGrouping[] = 
    {
        { Py_tp_new, _new_CharacterGrouping },
        { Py_tp_dealloc, _dealloc_CharacterGrouping },
        { Py_tp_methods, _methods_CharacterGrouping },
        { Py_tp_getset, _getset_CharacterGrouping },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_CharacterGrouping =
    {
        "_winsdk_Windows_Globalization_Collation.CharacterGrouping",
        sizeof(py::wrapper::Windows::Globalization::Collation::CharacterGrouping),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_CharacterGrouping
    };

    // ----- CharacterGroupings class --------------------
    constexpr const char* const _type_name_CharacterGroupings = "CharacterGroupings";

    static PyObject* _new_CharacterGroupings(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        if (kwds != nullptr)
        {
            py::set_invalid_kwd_args_error();
            return nullptr;
        }

        Py_ssize_t arg_count = PyTuple_Size(args);
        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                winrt::Windows::Globalization::Collation::CharacterGroupings instance{ param0 };
                return py::wrap(instance, type);
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 0)
        {
            try
            {
                winrt::Windows::Globalization::Collation::CharacterGroupings instance{  };
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

    static void _dealloc_CharacterGroupings(py::wrapper::Windows::Globalization::Collation::CharacterGroupings* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* CharacterGroupings_First(py::wrapper::Windows::Globalization::Collation::CharacterGroupings* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.First());
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

    static PyObject* CharacterGroupings_GetAt(py::wrapper::Windows::Globalization::Collation::CharacterGroupings* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<uint32_t>(args, 0);

                return py::convert(self->obj.GetAt(param0));
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

    static PyObject* CharacterGroupings_GetMany(py::wrapper::Windows::Globalization::Collation::CharacterGroupings* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 2)
        {
            try
            {
                auto param0 = py::convert_to<uint32_t>(args, 0);
                auto param1_count = py::convert_to<winrt::com_array<winrt::Windows::Globalization::Collation::CharacterGrouping>::size_type>(args, 1);
                winrt::com_array<winrt::Windows::Globalization::Collation::CharacterGrouping> param1 ( param1_count, py::empty_instance<winrt::Windows::Globalization::Collation::CharacterGrouping>::get() );

                auto return_value = self->obj.GetMany(param0, param1);

                py::pyobj_handle out_return_value{ py::convert(return_value) };
                if (!out_return_value)
                {
                    return nullptr;
                }
                py::pyobj_handle out1{ py::convert(param1) };
                if (!out1)
                {
                    return nullptr;
                }
                return PyTuple_Pack(2, out_return_value.get(), out1.get());
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

    static PyObject* CharacterGroupings_IndexOf(py::wrapper::Windows::Globalization::Collation::CharacterGroupings* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Globalization::Collation::CharacterGrouping>(args, 0);
                uint32_t param1 {  };

                auto return_value = self->obj.IndexOf(param0, param1);

                py::pyobj_handle out_return_value{ py::convert(return_value) };
                if (!out_return_value)
                {
                    return nullptr;
                }
                py::pyobj_handle out1{ py::convert(param1) };
                if (!out1)
                {
                    return nullptr;
                }
                return PyTuple_Pack(2, out_return_value.get(), out1.get());
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

    static PyObject* CharacterGroupings_Lookup(py::wrapper::Windows::Globalization::Collation::CharacterGroupings* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(self->obj.Lookup(param0));
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

    static PyObject* CharacterGroupings_get_Size(py::wrapper::Windows::Globalization::Collation::CharacterGroupings* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Size());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_CharacterGroupings(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Globalization::Collation::CharacterGroupings>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _iterator_CharacterGroupings(py::wrapper::Windows::Globalization::Collation::CharacterGroupings* self) noexcept
    {
        try
        {
            return py::convert(self->obj.First());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static Py_ssize_t _seq_length_CharacterGroupings(py::wrapper::Windows::Globalization::Collation::CharacterGroupings* self) noexcept
    {
        try
        {
            return static_cast<Py_ssize_t>(self->obj.Size());
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* _seq_item_CharacterGroupings(py::wrapper::Windows::Globalization::Collation::CharacterGroupings* self, Py_ssize_t i) noexcept
    {
        try
        {
            return py::convert(self->obj.GetAt(static_cast<uint32_t>(i)));
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_CharacterGroupings[] = {
        { "first", reinterpret_cast<PyCFunction>(CharacterGroupings_First), METH_VARARGS, nullptr },
        { "get_at", reinterpret_cast<PyCFunction>(CharacterGroupings_GetAt), METH_VARARGS, nullptr },
        { "get_many", reinterpret_cast<PyCFunction>(CharacterGroupings_GetMany), METH_VARARGS, nullptr },
        { "index_of", reinterpret_cast<PyCFunction>(CharacterGroupings_IndexOf), METH_VARARGS, nullptr },
        { "lookup", reinterpret_cast<PyCFunction>(CharacterGroupings_Lookup), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_CharacterGroupings), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_CharacterGroupings[] = {
        { "size", reinterpret_cast<getter>(CharacterGroupings_get_Size), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_CharacterGroupings[] = 
    {
        { Py_tp_new, _new_CharacterGroupings },
        { Py_tp_dealloc, _dealloc_CharacterGroupings },
        { Py_tp_methods, _methods_CharacterGroupings },
        { Py_tp_getset, _getset_CharacterGroupings },
        { Py_tp_iter, _iterator_CharacterGroupings },
        { Py_sq_length, _seq_length_CharacterGroupings },
        { Py_sq_item, _seq_item_CharacterGroupings },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_CharacterGroupings =
    {
        "_winsdk_Windows_Globalization_Collation.CharacterGroupings",
        sizeof(py::wrapper::Windows::Globalization::Collation::CharacterGroupings),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_CharacterGroupings
    };

    // ----- Windows.Globalization.Collation Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Globalization::Collation::CharacterGrouping>::python_type = py::register_python_type(module, _type_name_CharacterGrouping, &_type_spec_CharacterGrouping, bases.get());
            py::winrt_type<winrt::Windows::Globalization::Collation::CharacterGroupings>::python_type = py::register_python_type(module, _type_name_CharacterGroupings, &_type_spec_CharacterGroupings, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Globalization.Collation");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Globalization_Collation",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Globalization::Collation

PyMODINIT_FUNC
PyInit__winsdk_Windows_Globalization_Collation (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Globalization::Collation::module_def);
}