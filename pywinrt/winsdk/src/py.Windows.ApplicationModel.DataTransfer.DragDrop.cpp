// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.ApplicationModel.DataTransfer.DragDrop.h"


namespace py::cpp::Windows::ApplicationModel::DataTransfer::DragDrop
{
    // ----- Windows.ApplicationModel.DataTransfer.DragDrop Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };


            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.ApplicationModel.DataTransfer.DragDrop");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_ApplicationModel_DataTransfer_DragDrop",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::ApplicationModel::DataTransfer::DragDrop

PyMODINIT_FUNC
PyInit__winsdk_Windows_ApplicationModel_DataTransfer_DragDrop (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::ApplicationModel::DataTransfer::DragDrop::module_def);
}