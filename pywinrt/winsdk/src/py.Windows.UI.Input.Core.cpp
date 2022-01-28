// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.UI.Input.Core.h"

PyTypeObject* py::winrt_type<winrt::Windows::UI::Input::Core::RadialControllerIndependentInputSource>::python_type;

namespace py::cpp::Windows::UI::Input::Core
{
    // ----- RadialControllerIndependentInputSource class --------------------
    constexpr const char* const _type_name_RadialControllerIndependentInputSource = "RadialControllerIndependentInputSource";

    static PyObject* _new_RadialControllerIndependentInputSource(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_RadialControllerIndependentInputSource);
        return nullptr;
    }

    static void _dealloc_RadialControllerIndependentInputSource(py::wrapper::Windows::UI::Input::Core::RadialControllerIndependentInputSource* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* RadialControllerIndependentInputSource_CreateForView(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::ApplicationModel::Core::CoreApplicationView>(args, 0);

                return py::convert(winrt::Windows::UI::Input::Core::RadialControllerIndependentInputSource::CreateForView(param0));
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

    static PyObject* RadialControllerIndependentInputSource_get_Controller(py::wrapper::Windows::UI::Input::Core::RadialControllerIndependentInputSource* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Controller());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* RadialControllerIndependentInputSource_get_Dispatcher(py::wrapper::Windows::UI::Input::Core::RadialControllerIndependentInputSource* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Dispatcher());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* RadialControllerIndependentInputSource_get_DispatcherQueue(py::wrapper::Windows::UI::Input::Core::RadialControllerIndependentInputSource* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.DispatcherQueue());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_RadialControllerIndependentInputSource(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::UI::Input::Core::RadialControllerIndependentInputSource>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_RadialControllerIndependentInputSource[] = {
        { "create_for_view", reinterpret_cast<PyCFunction>(RadialControllerIndependentInputSource_CreateForView), METH_VARARGS | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_RadialControllerIndependentInputSource), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_RadialControllerIndependentInputSource[] = {
        { "controller", reinterpret_cast<getter>(RadialControllerIndependentInputSource_get_Controller), nullptr, nullptr, nullptr },
        { "dispatcher", reinterpret_cast<getter>(RadialControllerIndependentInputSource_get_Dispatcher), nullptr, nullptr, nullptr },
        { "dispatcher_queue", reinterpret_cast<getter>(RadialControllerIndependentInputSource_get_DispatcherQueue), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_RadialControllerIndependentInputSource[] = 
    {
        { Py_tp_new, _new_RadialControllerIndependentInputSource },
        { Py_tp_dealloc, _dealloc_RadialControllerIndependentInputSource },
        { Py_tp_methods, _methods_RadialControllerIndependentInputSource },
        { Py_tp_getset, _getset_RadialControllerIndependentInputSource },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_RadialControllerIndependentInputSource =
    {
        "_winsdk_Windows_UI_Input_Core.RadialControllerIndependentInputSource",
        sizeof(py::wrapper::Windows::UI::Input::Core::RadialControllerIndependentInputSource),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_RadialControllerIndependentInputSource
    };

    // ----- Windows.UI.Input.Core Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::UI::Input::Core::RadialControllerIndependentInputSource>::python_type = py::register_python_type(module, _type_name_RadialControllerIndependentInputSource, &_type_spec_RadialControllerIndependentInputSource, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.UI.Input.Core");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_UI_Input_Core",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::UI::Input::Core

PyMODINIT_FUNC
PyInit__winsdk_Windows_UI_Input_Core (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::UI::Input::Core::module_def);
}