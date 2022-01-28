// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.ApplicationModel.Appointments.AppointmentsProvider.h"

PyTypeObject* py::winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentsProvider::AddAppointmentOperation>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentsProvider::AppointmentsProviderLaunchActionVerbs>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentsProvider::RemoveAppointmentOperation>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentsProvider::ReplaceAppointmentOperation>::python_type;

namespace py::cpp::Windows::ApplicationModel::Appointments::AppointmentsProvider
{
    // ----- AddAppointmentOperation class --------------------
    constexpr const char* const _type_name_AddAppointmentOperation = "AddAppointmentOperation";

    static PyObject* _new_AddAppointmentOperation(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_AddAppointmentOperation);
        return nullptr;
    }

    static void _dealloc_AddAppointmentOperation(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::AddAppointmentOperation* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* AddAppointmentOperation_DismissUI(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::AddAppointmentOperation* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                self->obj.DismissUI();
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

    static PyObject* AddAppointmentOperation_ReportCanceled(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::AddAppointmentOperation* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                self->obj.ReportCanceled();
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

    static PyObject* AddAppointmentOperation_ReportCompleted(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::AddAppointmentOperation* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                self->obj.ReportCompleted(param0);
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

    static PyObject* AddAppointmentOperation_ReportError(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::AddAppointmentOperation* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                self->obj.ReportError(param0);
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

    static PyObject* AddAppointmentOperation_get_AppointmentInformation(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::AddAppointmentOperation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.AppointmentInformation());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* AddAppointmentOperation_get_SourcePackageFamilyName(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::AddAppointmentOperation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.SourcePackageFamilyName());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_AddAppointmentOperation(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::ApplicationModel::Appointments::AppointmentsProvider::AddAppointmentOperation>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_AddAppointmentOperation[] = {
        { "dismiss_u_i", reinterpret_cast<PyCFunction>(AddAppointmentOperation_DismissUI), METH_VARARGS, nullptr },
        { "report_canceled", reinterpret_cast<PyCFunction>(AddAppointmentOperation_ReportCanceled), METH_VARARGS, nullptr },
        { "report_completed", reinterpret_cast<PyCFunction>(AddAppointmentOperation_ReportCompleted), METH_VARARGS, nullptr },
        { "report_error", reinterpret_cast<PyCFunction>(AddAppointmentOperation_ReportError), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_AddAppointmentOperation), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_AddAppointmentOperation[] = {
        { "appointment_information", reinterpret_cast<getter>(AddAppointmentOperation_get_AppointmentInformation), nullptr, nullptr, nullptr },
        { "source_package_family_name", reinterpret_cast<getter>(AddAppointmentOperation_get_SourcePackageFamilyName), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_AddAppointmentOperation[] = 
    {
        { Py_tp_new, _new_AddAppointmentOperation },
        { Py_tp_dealloc, _dealloc_AddAppointmentOperation },
        { Py_tp_methods, _methods_AddAppointmentOperation },
        { Py_tp_getset, _getset_AddAppointmentOperation },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_AddAppointmentOperation =
    {
        "_winsdk_Windows_ApplicationModel_Appointments_AppointmentsProvider.AddAppointmentOperation",
        sizeof(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::AddAppointmentOperation),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_AddAppointmentOperation
    };

    // ----- AppointmentsProviderLaunchActionVerbs class --------------------
    constexpr const char* const _type_name_AppointmentsProviderLaunchActionVerbs = "AppointmentsProviderLaunchActionVerbs";

    static PyObject* _new_AppointmentsProviderLaunchActionVerbs(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_AppointmentsProviderLaunchActionVerbs);
        return nullptr;
    }

    static PyObject* AppointmentsProviderLaunchActionVerbs_get_AddAppointment(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::ApplicationModel::Appointments::AppointmentsProvider::AppointmentsProviderLaunchActionVerbs::AddAppointment());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* AppointmentsProviderLaunchActionVerbs_get_RemoveAppointment(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::ApplicationModel::Appointments::AppointmentsProvider::AppointmentsProviderLaunchActionVerbs::RemoveAppointment());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* AppointmentsProviderLaunchActionVerbs_get_ReplaceAppointment(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::ApplicationModel::Appointments::AppointmentsProvider::AppointmentsProviderLaunchActionVerbs::ReplaceAppointment());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* AppointmentsProviderLaunchActionVerbs_get_ShowTimeFrame(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::ApplicationModel::Appointments::AppointmentsProvider::AppointmentsProviderLaunchActionVerbs::ShowTimeFrame());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* AppointmentsProviderLaunchActionVerbs_get_ShowAppointmentDetails(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::ApplicationModel::Appointments::AppointmentsProvider::AppointmentsProviderLaunchActionVerbs::ShowAppointmentDetails());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_AppointmentsProviderLaunchActionVerbs[] = {
        { "get_add_appointment", reinterpret_cast<PyCFunction>(AppointmentsProviderLaunchActionVerbs_get_AddAppointment), METH_NOARGS | METH_STATIC, nullptr },
        { "get_remove_appointment", reinterpret_cast<PyCFunction>(AppointmentsProviderLaunchActionVerbs_get_RemoveAppointment), METH_NOARGS | METH_STATIC, nullptr },
        { "get_replace_appointment", reinterpret_cast<PyCFunction>(AppointmentsProviderLaunchActionVerbs_get_ReplaceAppointment), METH_NOARGS | METH_STATIC, nullptr },
        { "get_show_time_frame", reinterpret_cast<PyCFunction>(AppointmentsProviderLaunchActionVerbs_get_ShowTimeFrame), METH_NOARGS | METH_STATIC, nullptr },
        { "get_show_appointment_details", reinterpret_cast<PyCFunction>(AppointmentsProviderLaunchActionVerbs_get_ShowAppointmentDetails), METH_NOARGS | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_AppointmentsProviderLaunchActionVerbs[] = {
        { }
    };

    static PyType_Slot _type_slots_AppointmentsProviderLaunchActionVerbs[] = 
    {
        { Py_tp_new, _new_AppointmentsProviderLaunchActionVerbs },
        { Py_tp_methods, _methods_AppointmentsProviderLaunchActionVerbs },
        { Py_tp_getset, _getset_AppointmentsProviderLaunchActionVerbs },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_AppointmentsProviderLaunchActionVerbs =
    {
        "_winsdk_Windows_ApplicationModel_Appointments_AppointmentsProvider.AppointmentsProviderLaunchActionVerbs",
        0,
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_AppointmentsProviderLaunchActionVerbs
    };

    // ----- RemoveAppointmentOperation class --------------------
    constexpr const char* const _type_name_RemoveAppointmentOperation = "RemoveAppointmentOperation";

    static PyObject* _new_RemoveAppointmentOperation(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_RemoveAppointmentOperation);
        return nullptr;
    }

    static void _dealloc_RemoveAppointmentOperation(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::RemoveAppointmentOperation* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* RemoveAppointmentOperation_DismissUI(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::RemoveAppointmentOperation* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                self->obj.DismissUI();
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

    static PyObject* RemoveAppointmentOperation_ReportCanceled(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::RemoveAppointmentOperation* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                self->obj.ReportCanceled();
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

    static PyObject* RemoveAppointmentOperation_ReportCompleted(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::RemoveAppointmentOperation* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                self->obj.ReportCompleted();
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

    static PyObject* RemoveAppointmentOperation_ReportError(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::RemoveAppointmentOperation* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                self->obj.ReportError(param0);
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

    static PyObject* RemoveAppointmentOperation_get_AppointmentId(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::RemoveAppointmentOperation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.AppointmentId());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* RemoveAppointmentOperation_get_InstanceStartDate(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::RemoveAppointmentOperation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.InstanceStartDate());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* RemoveAppointmentOperation_get_SourcePackageFamilyName(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::RemoveAppointmentOperation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.SourcePackageFamilyName());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_RemoveAppointmentOperation(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::ApplicationModel::Appointments::AppointmentsProvider::RemoveAppointmentOperation>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_RemoveAppointmentOperation[] = {
        { "dismiss_u_i", reinterpret_cast<PyCFunction>(RemoveAppointmentOperation_DismissUI), METH_VARARGS, nullptr },
        { "report_canceled", reinterpret_cast<PyCFunction>(RemoveAppointmentOperation_ReportCanceled), METH_VARARGS, nullptr },
        { "report_completed", reinterpret_cast<PyCFunction>(RemoveAppointmentOperation_ReportCompleted), METH_VARARGS, nullptr },
        { "report_error", reinterpret_cast<PyCFunction>(RemoveAppointmentOperation_ReportError), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_RemoveAppointmentOperation), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_RemoveAppointmentOperation[] = {
        { "appointment_id", reinterpret_cast<getter>(RemoveAppointmentOperation_get_AppointmentId), nullptr, nullptr, nullptr },
        { "instance_start_date", reinterpret_cast<getter>(RemoveAppointmentOperation_get_InstanceStartDate), nullptr, nullptr, nullptr },
        { "source_package_family_name", reinterpret_cast<getter>(RemoveAppointmentOperation_get_SourcePackageFamilyName), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_RemoveAppointmentOperation[] = 
    {
        { Py_tp_new, _new_RemoveAppointmentOperation },
        { Py_tp_dealloc, _dealloc_RemoveAppointmentOperation },
        { Py_tp_methods, _methods_RemoveAppointmentOperation },
        { Py_tp_getset, _getset_RemoveAppointmentOperation },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_RemoveAppointmentOperation =
    {
        "_winsdk_Windows_ApplicationModel_Appointments_AppointmentsProvider.RemoveAppointmentOperation",
        sizeof(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::RemoveAppointmentOperation),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_RemoveAppointmentOperation
    };

    // ----- ReplaceAppointmentOperation class --------------------
    constexpr const char* const _type_name_ReplaceAppointmentOperation = "ReplaceAppointmentOperation";

    static PyObject* _new_ReplaceAppointmentOperation(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_ReplaceAppointmentOperation);
        return nullptr;
    }

    static void _dealloc_ReplaceAppointmentOperation(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::ReplaceAppointmentOperation* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* ReplaceAppointmentOperation_DismissUI(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::ReplaceAppointmentOperation* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                self->obj.DismissUI();
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

    static PyObject* ReplaceAppointmentOperation_ReportCanceled(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::ReplaceAppointmentOperation* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                self->obj.ReportCanceled();
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

    static PyObject* ReplaceAppointmentOperation_ReportCompleted(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::ReplaceAppointmentOperation* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                self->obj.ReportCompleted(param0);
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

    static PyObject* ReplaceAppointmentOperation_ReportError(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::ReplaceAppointmentOperation* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                self->obj.ReportError(param0);
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

    static PyObject* ReplaceAppointmentOperation_get_AppointmentId(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::ReplaceAppointmentOperation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.AppointmentId());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ReplaceAppointmentOperation_get_AppointmentInformation(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::ReplaceAppointmentOperation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.AppointmentInformation());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ReplaceAppointmentOperation_get_InstanceStartDate(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::ReplaceAppointmentOperation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.InstanceStartDate());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ReplaceAppointmentOperation_get_SourcePackageFamilyName(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::ReplaceAppointmentOperation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.SourcePackageFamilyName());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_ReplaceAppointmentOperation(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::ApplicationModel::Appointments::AppointmentsProvider::ReplaceAppointmentOperation>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_ReplaceAppointmentOperation[] = {
        { "dismiss_u_i", reinterpret_cast<PyCFunction>(ReplaceAppointmentOperation_DismissUI), METH_VARARGS, nullptr },
        { "report_canceled", reinterpret_cast<PyCFunction>(ReplaceAppointmentOperation_ReportCanceled), METH_VARARGS, nullptr },
        { "report_completed", reinterpret_cast<PyCFunction>(ReplaceAppointmentOperation_ReportCompleted), METH_VARARGS, nullptr },
        { "report_error", reinterpret_cast<PyCFunction>(ReplaceAppointmentOperation_ReportError), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_ReplaceAppointmentOperation), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_ReplaceAppointmentOperation[] = {
        { "appointment_id", reinterpret_cast<getter>(ReplaceAppointmentOperation_get_AppointmentId), nullptr, nullptr, nullptr },
        { "appointment_information", reinterpret_cast<getter>(ReplaceAppointmentOperation_get_AppointmentInformation), nullptr, nullptr, nullptr },
        { "instance_start_date", reinterpret_cast<getter>(ReplaceAppointmentOperation_get_InstanceStartDate), nullptr, nullptr, nullptr },
        { "source_package_family_name", reinterpret_cast<getter>(ReplaceAppointmentOperation_get_SourcePackageFamilyName), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_ReplaceAppointmentOperation[] = 
    {
        { Py_tp_new, _new_ReplaceAppointmentOperation },
        { Py_tp_dealloc, _dealloc_ReplaceAppointmentOperation },
        { Py_tp_methods, _methods_ReplaceAppointmentOperation },
        { Py_tp_getset, _getset_ReplaceAppointmentOperation },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_ReplaceAppointmentOperation =
    {
        "_winsdk_Windows_ApplicationModel_Appointments_AppointmentsProvider.ReplaceAppointmentOperation",
        sizeof(py::wrapper::Windows::ApplicationModel::Appointments::AppointmentsProvider::ReplaceAppointmentOperation),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_ReplaceAppointmentOperation
    };

    // ----- Windows.ApplicationModel.Appointments.AppointmentsProvider Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentsProvider::AddAppointmentOperation>::python_type = py::register_python_type(module, _type_name_AddAppointmentOperation, &_type_spec_AddAppointmentOperation, bases.get());
            py::winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentsProvider::AppointmentsProviderLaunchActionVerbs>::python_type = py::register_python_type(module, _type_name_AppointmentsProviderLaunchActionVerbs, &_type_spec_AppointmentsProviderLaunchActionVerbs, nullptr);
            py::winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentsProvider::RemoveAppointmentOperation>::python_type = py::register_python_type(module, _type_name_RemoveAppointmentOperation, &_type_spec_RemoveAppointmentOperation, bases.get());
            py::winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentsProvider::ReplaceAppointmentOperation>::python_type = py::register_python_type(module, _type_name_ReplaceAppointmentOperation, &_type_spec_ReplaceAppointmentOperation, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.ApplicationModel.Appointments.AppointmentsProvider");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_ApplicationModel_Appointments_AppointmentsProvider",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::ApplicationModel::Appointments::AppointmentsProvider

PyMODINIT_FUNC
PyInit__winsdk_Windows_ApplicationModel_Appointments_AppointmentsProvider (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::ApplicationModel::Appointments::AppointmentsProvider::module_def);
}