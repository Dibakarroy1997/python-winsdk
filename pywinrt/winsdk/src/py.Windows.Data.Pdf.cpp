// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.Data.Pdf.h"

PyTypeObject* py::winrt_type<winrt::Windows::Data::Pdf::PdfDocument>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Data::Pdf::PdfPage>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Data::Pdf::PdfPageDimensions>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Data::Pdf::PdfPageRenderOptions>::python_type;

namespace py::cpp::Windows::Data::Pdf
{
    // ----- PdfDocument class --------------------
    constexpr const char* const _type_name_PdfDocument = "PdfDocument";

    static PyObject* _new_PdfDocument(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_PdfDocument);
        return nullptr;
    }

    static void _dealloc_PdfDocument(py::wrapper::Windows::Data::Pdf::PdfDocument* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* PdfDocument_GetPage(py::wrapper::Windows::Data::Pdf::PdfDocument* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<uint32_t>(args, 0);

                return py::convert(self->obj.GetPage(param0));
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

    static PyObject* PdfDocument_LoadFromFileAsync(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::IStorageFile>(args, 0);

                return py::convert(winrt::Windows::Data::Pdf::PdfDocument::LoadFromFileAsync(param0));
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
                auto param0 = py::convert_to<winrt::Windows::Storage::IStorageFile>(args, 0);
                auto param1 = py::convert_to<winrt::hstring>(args, 1);

                return py::convert(winrt::Windows::Data::Pdf::PdfDocument::LoadFromFileAsync(param0, param1));
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

    static PyObject* PdfDocument_LoadFromStreamAsync(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IRandomAccessStream>(args, 0);

                return py::convert(winrt::Windows::Data::Pdf::PdfDocument::LoadFromStreamAsync(param0));
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
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IRandomAccessStream>(args, 0);
                auto param1 = py::convert_to<winrt::hstring>(args, 1);

                return py::convert(winrt::Windows::Data::Pdf::PdfDocument::LoadFromStreamAsync(param0, param1));
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

    static PyObject* PdfDocument_get_IsPasswordProtected(py::wrapper::Windows::Data::Pdf::PdfDocument* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.IsPasswordProtected());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PdfDocument_get_PageCount(py::wrapper::Windows::Data::Pdf::PdfDocument* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.PageCount());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_PdfDocument(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Data::Pdf::PdfDocument>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_PdfDocument[] = {
        { "get_page", reinterpret_cast<PyCFunction>(PdfDocument_GetPage), METH_VARARGS, nullptr },
        { "load_from_file_async", reinterpret_cast<PyCFunction>(PdfDocument_LoadFromFileAsync), METH_VARARGS | METH_STATIC, nullptr },
        { "load_from_stream_async", reinterpret_cast<PyCFunction>(PdfDocument_LoadFromStreamAsync), METH_VARARGS | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_PdfDocument), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_PdfDocument[] = {
        { "is_password_protected", reinterpret_cast<getter>(PdfDocument_get_IsPasswordProtected), nullptr, nullptr, nullptr },
        { "page_count", reinterpret_cast<getter>(PdfDocument_get_PageCount), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_PdfDocument[] = 
    {
        { Py_tp_new, _new_PdfDocument },
        { Py_tp_dealloc, _dealloc_PdfDocument },
        { Py_tp_methods, _methods_PdfDocument },
        { Py_tp_getset, _getset_PdfDocument },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_PdfDocument =
    {
        "_winsdk_Windows_Data_Pdf.PdfDocument",
        sizeof(py::wrapper::Windows::Data::Pdf::PdfDocument),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_PdfDocument
    };

    // ----- PdfPage class --------------------
    constexpr const char* const _type_name_PdfPage = "PdfPage";

    static PyObject* _new_PdfPage(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_PdfPage);
        return nullptr;
    }

    static void _dealloc_PdfPage(py::wrapper::Windows::Data::Pdf::PdfPage* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* PdfPage_Close(py::wrapper::Windows::Data::Pdf::PdfPage* self, PyObject* args) noexcept
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

    static PyObject* PdfPage_PreparePageAsync(py::wrapper::Windows::Data::Pdf::PdfPage* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.PreparePageAsync());
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

    static PyObject* PdfPage_RenderToStreamAsync(py::wrapper::Windows::Data::Pdf::PdfPage* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IRandomAccessStream>(args, 0);

                return py::convert(self->obj.RenderToStreamAsync(param0));
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
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IRandomAccessStream>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Data::Pdf::PdfPageRenderOptions>(args, 1);

                return py::convert(self->obj.RenderToStreamAsync(param0, param1));
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

    static PyObject* PdfPage_get_Dimensions(py::wrapper::Windows::Data::Pdf::PdfPage* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Dimensions());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PdfPage_get_Index(py::wrapper::Windows::Data::Pdf::PdfPage* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Index());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PdfPage_get_PreferredZoom(py::wrapper::Windows::Data::Pdf::PdfPage* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.PreferredZoom());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PdfPage_get_Rotation(py::wrapper::Windows::Data::Pdf::PdfPage* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Rotation());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PdfPage_get_Size(py::wrapper::Windows::Data::Pdf::PdfPage* self, void* /*unused*/) noexcept
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

    static PyObject* _from_PdfPage(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Data::Pdf::PdfPage>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _enter_PdfPage(py::wrapper::Windows::Data::Pdf::PdfPage* self) noexcept
    {
        Py_INCREF(self);
        return reinterpret_cast<PyObject*>(self);
    }

    static PyObject* _exit_PdfPage(py::wrapper::Windows::Data::Pdf::PdfPage* self) noexcept
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

    static PyMethodDef _methods_PdfPage[] = {
        { "close", reinterpret_cast<PyCFunction>(PdfPage_Close), METH_VARARGS, nullptr },
        { "prepare_page_async", reinterpret_cast<PyCFunction>(PdfPage_PreparePageAsync), METH_VARARGS, nullptr },
        { "render_to_stream_async", reinterpret_cast<PyCFunction>(PdfPage_RenderToStreamAsync), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_PdfPage), METH_O | METH_STATIC, nullptr },
        { "__enter__", reinterpret_cast<PyCFunction>(_enter_PdfPage), METH_NOARGS, nullptr },
        { "__exit__",  reinterpret_cast<PyCFunction>(_exit_PdfPage), METH_VARARGS, nullptr },
        { }
    };

    static PyGetSetDef _getset_PdfPage[] = {
        { "dimensions", reinterpret_cast<getter>(PdfPage_get_Dimensions), nullptr, nullptr, nullptr },
        { "index", reinterpret_cast<getter>(PdfPage_get_Index), nullptr, nullptr, nullptr },
        { "preferred_zoom", reinterpret_cast<getter>(PdfPage_get_PreferredZoom), nullptr, nullptr, nullptr },
        { "rotation", reinterpret_cast<getter>(PdfPage_get_Rotation), nullptr, nullptr, nullptr },
        { "size", reinterpret_cast<getter>(PdfPage_get_Size), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_PdfPage[] = 
    {
        { Py_tp_new, _new_PdfPage },
        { Py_tp_dealloc, _dealloc_PdfPage },
        { Py_tp_methods, _methods_PdfPage },
        { Py_tp_getset, _getset_PdfPage },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_PdfPage =
    {
        "_winsdk_Windows_Data_Pdf.PdfPage",
        sizeof(py::wrapper::Windows::Data::Pdf::PdfPage),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_PdfPage
    };

    // ----- PdfPageDimensions class --------------------
    constexpr const char* const _type_name_PdfPageDimensions = "PdfPageDimensions";

    static PyObject* _new_PdfPageDimensions(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_PdfPageDimensions);
        return nullptr;
    }

    static void _dealloc_PdfPageDimensions(py::wrapper::Windows::Data::Pdf::PdfPageDimensions* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* PdfPageDimensions_get_ArtBox(py::wrapper::Windows::Data::Pdf::PdfPageDimensions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ArtBox());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PdfPageDimensions_get_BleedBox(py::wrapper::Windows::Data::Pdf::PdfPageDimensions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.BleedBox());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PdfPageDimensions_get_CropBox(py::wrapper::Windows::Data::Pdf::PdfPageDimensions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.CropBox());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PdfPageDimensions_get_MediaBox(py::wrapper::Windows::Data::Pdf::PdfPageDimensions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.MediaBox());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PdfPageDimensions_get_TrimBox(py::wrapper::Windows::Data::Pdf::PdfPageDimensions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.TrimBox());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_PdfPageDimensions(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Data::Pdf::PdfPageDimensions>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_PdfPageDimensions[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_PdfPageDimensions), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_PdfPageDimensions[] = {
        { "art_box", reinterpret_cast<getter>(PdfPageDimensions_get_ArtBox), nullptr, nullptr, nullptr },
        { "bleed_box", reinterpret_cast<getter>(PdfPageDimensions_get_BleedBox), nullptr, nullptr, nullptr },
        { "crop_box", reinterpret_cast<getter>(PdfPageDimensions_get_CropBox), nullptr, nullptr, nullptr },
        { "media_box", reinterpret_cast<getter>(PdfPageDimensions_get_MediaBox), nullptr, nullptr, nullptr },
        { "trim_box", reinterpret_cast<getter>(PdfPageDimensions_get_TrimBox), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_PdfPageDimensions[] = 
    {
        { Py_tp_new, _new_PdfPageDimensions },
        { Py_tp_dealloc, _dealloc_PdfPageDimensions },
        { Py_tp_methods, _methods_PdfPageDimensions },
        { Py_tp_getset, _getset_PdfPageDimensions },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_PdfPageDimensions =
    {
        "_winsdk_Windows_Data_Pdf.PdfPageDimensions",
        sizeof(py::wrapper::Windows::Data::Pdf::PdfPageDimensions),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_PdfPageDimensions
    };

    // ----- PdfPageRenderOptions class --------------------
    constexpr const char* const _type_name_PdfPageRenderOptions = "PdfPageRenderOptions";

    static PyObject* _new_PdfPageRenderOptions(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
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
                winrt::Windows::Data::Pdf::PdfPageRenderOptions instance{  };
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

    static void _dealloc_PdfPageRenderOptions(py::wrapper::Windows::Data::Pdf::PdfPageRenderOptions* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* PdfPageRenderOptions_get_SourceRect(py::wrapper::Windows::Data::Pdf::PdfPageRenderOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.SourceRect());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int PdfPageRenderOptions_put_SourceRect(py::wrapper::Windows::Data::Pdf::PdfPageRenderOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Foundation::Rect>(arg);

            self->obj.SourceRect(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* PdfPageRenderOptions_get_IsIgnoringHighContrast(py::wrapper::Windows::Data::Pdf::PdfPageRenderOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.IsIgnoringHighContrast());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int PdfPageRenderOptions_put_IsIgnoringHighContrast(py::wrapper::Windows::Data::Pdf::PdfPageRenderOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<bool>(arg);

            self->obj.IsIgnoringHighContrast(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* PdfPageRenderOptions_get_DestinationWidth(py::wrapper::Windows::Data::Pdf::PdfPageRenderOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.DestinationWidth());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int PdfPageRenderOptions_put_DestinationWidth(py::wrapper::Windows::Data::Pdf::PdfPageRenderOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<uint32_t>(arg);

            self->obj.DestinationWidth(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* PdfPageRenderOptions_get_DestinationHeight(py::wrapper::Windows::Data::Pdf::PdfPageRenderOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.DestinationHeight());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int PdfPageRenderOptions_put_DestinationHeight(py::wrapper::Windows::Data::Pdf::PdfPageRenderOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<uint32_t>(arg);

            self->obj.DestinationHeight(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* PdfPageRenderOptions_get_BitmapEncoderId(py::wrapper::Windows::Data::Pdf::PdfPageRenderOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.BitmapEncoderId());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int PdfPageRenderOptions_put_BitmapEncoderId(py::wrapper::Windows::Data::Pdf::PdfPageRenderOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::guid>(arg);

            self->obj.BitmapEncoderId(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* PdfPageRenderOptions_get_BackgroundColor(py::wrapper::Windows::Data::Pdf::PdfPageRenderOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.BackgroundColor());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int PdfPageRenderOptions_put_BackgroundColor(py::wrapper::Windows::Data::Pdf::PdfPageRenderOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::UI::Color>(arg);

            self->obj.BackgroundColor(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* _from_PdfPageRenderOptions(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Data::Pdf::PdfPageRenderOptions>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_PdfPageRenderOptions[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_PdfPageRenderOptions), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_PdfPageRenderOptions[] = {
        { "source_rect", reinterpret_cast<getter>(PdfPageRenderOptions_get_SourceRect), reinterpret_cast<setter>(PdfPageRenderOptions_put_SourceRect), nullptr, nullptr },
        { "is_ignoring_high_contrast", reinterpret_cast<getter>(PdfPageRenderOptions_get_IsIgnoringHighContrast), reinterpret_cast<setter>(PdfPageRenderOptions_put_IsIgnoringHighContrast), nullptr, nullptr },
        { "destination_width", reinterpret_cast<getter>(PdfPageRenderOptions_get_DestinationWidth), reinterpret_cast<setter>(PdfPageRenderOptions_put_DestinationWidth), nullptr, nullptr },
        { "destination_height", reinterpret_cast<getter>(PdfPageRenderOptions_get_DestinationHeight), reinterpret_cast<setter>(PdfPageRenderOptions_put_DestinationHeight), nullptr, nullptr },
        { "bitmap_encoder_id", reinterpret_cast<getter>(PdfPageRenderOptions_get_BitmapEncoderId), reinterpret_cast<setter>(PdfPageRenderOptions_put_BitmapEncoderId), nullptr, nullptr },
        { "background_color", reinterpret_cast<getter>(PdfPageRenderOptions_get_BackgroundColor), reinterpret_cast<setter>(PdfPageRenderOptions_put_BackgroundColor), nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_PdfPageRenderOptions[] = 
    {
        { Py_tp_new, _new_PdfPageRenderOptions },
        { Py_tp_dealloc, _dealloc_PdfPageRenderOptions },
        { Py_tp_methods, _methods_PdfPageRenderOptions },
        { Py_tp_getset, _getset_PdfPageRenderOptions },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_PdfPageRenderOptions =
    {
        "_winsdk_Windows_Data_Pdf.PdfPageRenderOptions",
        sizeof(py::wrapper::Windows::Data::Pdf::PdfPageRenderOptions),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_PdfPageRenderOptions
    };

    // ----- Windows.Data.Pdf Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Data::Pdf::PdfDocument>::python_type = py::register_python_type(module, _type_name_PdfDocument, &_type_spec_PdfDocument, bases.get());
            py::winrt_type<winrt::Windows::Data::Pdf::PdfPage>::python_type = py::register_python_type(module, _type_name_PdfPage, &_type_spec_PdfPage, bases.get());
            py::winrt_type<winrt::Windows::Data::Pdf::PdfPageDimensions>::python_type = py::register_python_type(module, _type_name_PdfPageDimensions, &_type_spec_PdfPageDimensions, bases.get());
            py::winrt_type<winrt::Windows::Data::Pdf::PdfPageRenderOptions>::python_type = py::register_python_type(module, _type_name_PdfPageRenderOptions, &_type_spec_PdfPageRenderOptions, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Data.Pdf");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Data_Pdf",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Data::Pdf

PyMODINIT_FUNC
PyInit__winsdk_Windows_Data_Pdf (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Data::Pdf::module_def);
}