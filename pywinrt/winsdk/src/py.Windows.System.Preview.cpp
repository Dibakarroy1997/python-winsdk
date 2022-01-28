// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.System.Preview.h"

PyTypeObject* py::winrt_type<winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreview>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReading>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs>::python_type;

namespace py::cpp::Windows::System::Preview
{
    // ----- TwoPanelHingedDevicePosturePreview class --------------------
    constexpr const char* const _type_name_TwoPanelHingedDevicePosturePreview = "TwoPanelHingedDevicePosturePreview";

    static PyObject* _new_TwoPanelHingedDevicePosturePreview(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_TwoPanelHingedDevicePosturePreview);
        return nullptr;
    }

    static void _dealloc_TwoPanelHingedDevicePosturePreview(py::wrapper::Windows::System::Preview::TwoPanelHingedDevicePosturePreview* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* TwoPanelHingedDevicePosturePreview_GetCurrentPostureAsync(py::wrapper::Windows::System::Preview::TwoPanelHingedDevicePosturePreview* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.GetCurrentPostureAsync());
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

    static PyObject* TwoPanelHingedDevicePosturePreview_GetDefaultAsync(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreview::GetDefaultAsync());
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

    static PyObject* TwoPanelHingedDevicePosturePreview_add_PostureChanged(py::wrapper::Windows::System::Preview::TwoPanelHingedDevicePosturePreview* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::Windows::Foundation::TypedEventHandler<winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreview, winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs>>(arg);

            return py::convert(self->obj.PostureChanged(param0));
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* TwoPanelHingedDevicePosturePreview_remove_PostureChanged(py::wrapper::Windows::System::Preview::TwoPanelHingedDevicePosturePreview* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::event_token>(arg);

            self->obj.PostureChanged(param0);
            Py_RETURN_NONE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_TwoPanelHingedDevicePosturePreview(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreview>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_TwoPanelHingedDevicePosturePreview[] = {
        { "get_current_posture_async", reinterpret_cast<PyCFunction>(TwoPanelHingedDevicePosturePreview_GetCurrentPostureAsync), METH_VARARGS, nullptr },
        { "get_default_async", reinterpret_cast<PyCFunction>(TwoPanelHingedDevicePosturePreview_GetDefaultAsync), METH_VARARGS | METH_STATIC, nullptr },
        { "add_posture_changed", reinterpret_cast<PyCFunction>(TwoPanelHingedDevicePosturePreview_add_PostureChanged), METH_O, nullptr },
        { "remove_posture_changed", reinterpret_cast<PyCFunction>(TwoPanelHingedDevicePosturePreview_remove_PostureChanged), METH_O, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_TwoPanelHingedDevicePosturePreview), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_TwoPanelHingedDevicePosturePreview[] = {
        { }
    };

    static PyType_Slot _type_slots_TwoPanelHingedDevicePosturePreview[] = 
    {
        { Py_tp_new, _new_TwoPanelHingedDevicePosturePreview },
        { Py_tp_dealloc, _dealloc_TwoPanelHingedDevicePosturePreview },
        { Py_tp_methods, _methods_TwoPanelHingedDevicePosturePreview },
        { Py_tp_getset, _getset_TwoPanelHingedDevicePosturePreview },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_TwoPanelHingedDevicePosturePreview =
    {
        "_winsdk_Windows_System_Preview.TwoPanelHingedDevicePosturePreview",
        sizeof(py::wrapper::Windows::System::Preview::TwoPanelHingedDevicePosturePreview),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_TwoPanelHingedDevicePosturePreview
    };

    // ----- TwoPanelHingedDevicePosturePreviewReading class --------------------
    constexpr const char* const _type_name_TwoPanelHingedDevicePosturePreviewReading = "TwoPanelHingedDevicePosturePreviewReading";

    static PyObject* _new_TwoPanelHingedDevicePosturePreviewReading(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_TwoPanelHingedDevicePosturePreviewReading);
        return nullptr;
    }

    static void _dealloc_TwoPanelHingedDevicePosturePreviewReading(py::wrapper::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReading* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* TwoPanelHingedDevicePosturePreviewReading_get_HingeState(py::wrapper::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReading* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.HingeState());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* TwoPanelHingedDevicePosturePreviewReading_get_Panel1Id(py::wrapper::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReading* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Panel1Id());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* TwoPanelHingedDevicePosturePreviewReading_get_Panel1Orientation(py::wrapper::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReading* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Panel1Orientation());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* TwoPanelHingedDevicePosturePreviewReading_get_Panel2Id(py::wrapper::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReading* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Panel2Id());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* TwoPanelHingedDevicePosturePreviewReading_get_Panel2Orientation(py::wrapper::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReading* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Panel2Orientation());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* TwoPanelHingedDevicePosturePreviewReading_get_Timestamp(py::wrapper::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReading* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Timestamp());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_TwoPanelHingedDevicePosturePreviewReading(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReading>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_TwoPanelHingedDevicePosturePreviewReading[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_TwoPanelHingedDevicePosturePreviewReading), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_TwoPanelHingedDevicePosturePreviewReading[] = {
        { "hinge_state", reinterpret_cast<getter>(TwoPanelHingedDevicePosturePreviewReading_get_HingeState), nullptr, nullptr, nullptr },
        { "panel1_id", reinterpret_cast<getter>(TwoPanelHingedDevicePosturePreviewReading_get_Panel1Id), nullptr, nullptr, nullptr },
        { "panel1_orientation", reinterpret_cast<getter>(TwoPanelHingedDevicePosturePreviewReading_get_Panel1Orientation), nullptr, nullptr, nullptr },
        { "panel2_id", reinterpret_cast<getter>(TwoPanelHingedDevicePosturePreviewReading_get_Panel2Id), nullptr, nullptr, nullptr },
        { "panel2_orientation", reinterpret_cast<getter>(TwoPanelHingedDevicePosturePreviewReading_get_Panel2Orientation), nullptr, nullptr, nullptr },
        { "timestamp", reinterpret_cast<getter>(TwoPanelHingedDevicePosturePreviewReading_get_Timestamp), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_TwoPanelHingedDevicePosturePreviewReading[] = 
    {
        { Py_tp_new, _new_TwoPanelHingedDevicePosturePreviewReading },
        { Py_tp_dealloc, _dealloc_TwoPanelHingedDevicePosturePreviewReading },
        { Py_tp_methods, _methods_TwoPanelHingedDevicePosturePreviewReading },
        { Py_tp_getset, _getset_TwoPanelHingedDevicePosturePreviewReading },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_TwoPanelHingedDevicePosturePreviewReading =
    {
        "_winsdk_Windows_System_Preview.TwoPanelHingedDevicePosturePreviewReading",
        sizeof(py::wrapper::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReading),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_TwoPanelHingedDevicePosturePreviewReading
    };

    // ----- TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs class --------------------
    constexpr const char* const _type_name_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs = "TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs";

    static PyObject* _new_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs);
        return nullptr;
    }

    static void _dealloc_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs(py::wrapper::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs_get_Reading(py::wrapper::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Reading());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs[] = {
        { "reading", reinterpret_cast<getter>(TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs_get_Reading), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs[] = 
    {
        { Py_tp_new, _new_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs },
        { Py_tp_dealloc, _dealloc_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs },
        { Py_tp_methods, _methods_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs },
        { Py_tp_getset, _getset_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs =
    {
        "_winsdk_Windows_System_Preview.TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs",
        sizeof(py::wrapper::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs
    };

    // ----- Windows.System.Preview Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreview>::python_type = py::register_python_type(module, _type_name_TwoPanelHingedDevicePosturePreview, &_type_spec_TwoPanelHingedDevicePosturePreview, bases.get());
            py::winrt_type<winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReading>::python_type = py::register_python_type(module, _type_name_TwoPanelHingedDevicePosturePreviewReading, &_type_spec_TwoPanelHingedDevicePosturePreviewReading, bases.get());
            py::winrt_type<winrt::Windows::System::Preview::TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs>::python_type = py::register_python_type(module, _type_name_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs, &_type_spec_TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.System.Preview");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_System_Preview",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::System::Preview

PyMODINIT_FUNC
PyInit__winsdk_Windows_System_Preview (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::System::Preview::module_def);
}