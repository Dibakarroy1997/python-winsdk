// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.Media.Ocr.h"

PyTypeObject* py::winrt_type<winrt::Windows::Media::Ocr::OcrEngine>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Media::Ocr::OcrLine>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Media::Ocr::OcrResult>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Media::Ocr::OcrWord>::python_type;

namespace py::cpp::Windows::Media::Ocr
{
    // ----- OcrEngine class --------------------
    constexpr const char* const _type_name_OcrEngine = "OcrEngine";

    static PyObject* _new_OcrEngine(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_OcrEngine);
        return nullptr;
    }

    static void _dealloc_OcrEngine(py::wrapper::Windows::Media::Ocr::OcrEngine* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* OcrEngine_IsLanguageSupported(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Globalization::Language>(args, 0);

                return py::convert(winrt::Windows::Media::Ocr::OcrEngine::IsLanguageSupported(param0));
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

    static PyObject* OcrEngine_RecognizeAsync(py::wrapper::Windows::Media::Ocr::OcrEngine* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Graphics::Imaging::SoftwareBitmap>(args, 0);

                return py::convert(self->obj.RecognizeAsync(param0));
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

    static PyObject* OcrEngine_TryCreateFromLanguage(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Globalization::Language>(args, 0);

                return py::convert(winrt::Windows::Media::Ocr::OcrEngine::TryCreateFromLanguage(param0));
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

    static PyObject* OcrEngine_TryCreateFromUserProfileLanguages(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(winrt::Windows::Media::Ocr::OcrEngine::TryCreateFromUserProfileLanguages());
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

    static PyObject* OcrEngine_get_RecognizerLanguage(py::wrapper::Windows::Media::Ocr::OcrEngine* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.RecognizerLanguage());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* OcrEngine_get_AvailableRecognizerLanguages(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Media::Ocr::OcrEngine::AvailableRecognizerLanguages());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* OcrEngine_get_MaxImageDimension(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Media::Ocr::OcrEngine::MaxImageDimension());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_OcrEngine(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Media::Ocr::OcrEngine>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_OcrEngine[] = {
        { "is_language_supported", reinterpret_cast<PyCFunction>(OcrEngine_IsLanguageSupported), METH_VARARGS | METH_STATIC, nullptr },
        { "recognize_async", reinterpret_cast<PyCFunction>(OcrEngine_RecognizeAsync), METH_VARARGS, nullptr },
        { "try_create_from_language", reinterpret_cast<PyCFunction>(OcrEngine_TryCreateFromLanguage), METH_VARARGS | METH_STATIC, nullptr },
        { "try_create_from_user_profile_languages", reinterpret_cast<PyCFunction>(OcrEngine_TryCreateFromUserProfileLanguages), METH_VARARGS | METH_STATIC, nullptr },
        { "get_available_recognizer_languages", reinterpret_cast<PyCFunction>(OcrEngine_get_AvailableRecognizerLanguages), METH_NOARGS | METH_STATIC, nullptr },
        { "get_max_image_dimension", reinterpret_cast<PyCFunction>(OcrEngine_get_MaxImageDimension), METH_NOARGS | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_OcrEngine), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_OcrEngine[] = {
        { "recognizer_language", reinterpret_cast<getter>(OcrEngine_get_RecognizerLanguage), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_OcrEngine[] = 
    {
        { Py_tp_new, _new_OcrEngine },
        { Py_tp_dealloc, _dealloc_OcrEngine },
        { Py_tp_methods, _methods_OcrEngine },
        { Py_tp_getset, _getset_OcrEngine },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_OcrEngine =
    {
        "_winsdk_Windows_Media_Ocr.OcrEngine",
        sizeof(py::wrapper::Windows::Media::Ocr::OcrEngine),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_OcrEngine
    };

    // ----- OcrLine class --------------------
    constexpr const char* const _type_name_OcrLine = "OcrLine";

    static PyObject* _new_OcrLine(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_OcrLine);
        return nullptr;
    }

    static void _dealloc_OcrLine(py::wrapper::Windows::Media::Ocr::OcrLine* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* OcrLine_get_Text(py::wrapper::Windows::Media::Ocr::OcrLine* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Text());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* OcrLine_get_Words(py::wrapper::Windows::Media::Ocr::OcrLine* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Words());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_OcrLine(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Media::Ocr::OcrLine>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_OcrLine[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_OcrLine), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_OcrLine[] = {
        { "text", reinterpret_cast<getter>(OcrLine_get_Text), nullptr, nullptr, nullptr },
        { "words", reinterpret_cast<getter>(OcrLine_get_Words), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_OcrLine[] = 
    {
        { Py_tp_new, _new_OcrLine },
        { Py_tp_dealloc, _dealloc_OcrLine },
        { Py_tp_methods, _methods_OcrLine },
        { Py_tp_getset, _getset_OcrLine },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_OcrLine =
    {
        "_winsdk_Windows_Media_Ocr.OcrLine",
        sizeof(py::wrapper::Windows::Media::Ocr::OcrLine),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_OcrLine
    };

    // ----- OcrResult class --------------------
    constexpr const char* const _type_name_OcrResult = "OcrResult";

    static PyObject* _new_OcrResult(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_OcrResult);
        return nullptr;
    }

    static void _dealloc_OcrResult(py::wrapper::Windows::Media::Ocr::OcrResult* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* OcrResult_get_Lines(py::wrapper::Windows::Media::Ocr::OcrResult* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Lines());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* OcrResult_get_Text(py::wrapper::Windows::Media::Ocr::OcrResult* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Text());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* OcrResult_get_TextAngle(py::wrapper::Windows::Media::Ocr::OcrResult* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.TextAngle());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_OcrResult(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Media::Ocr::OcrResult>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_OcrResult[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_OcrResult), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_OcrResult[] = {
        { "lines", reinterpret_cast<getter>(OcrResult_get_Lines), nullptr, nullptr, nullptr },
        { "text", reinterpret_cast<getter>(OcrResult_get_Text), nullptr, nullptr, nullptr },
        { "text_angle", reinterpret_cast<getter>(OcrResult_get_TextAngle), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_OcrResult[] = 
    {
        { Py_tp_new, _new_OcrResult },
        { Py_tp_dealloc, _dealloc_OcrResult },
        { Py_tp_methods, _methods_OcrResult },
        { Py_tp_getset, _getset_OcrResult },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_OcrResult =
    {
        "_winsdk_Windows_Media_Ocr.OcrResult",
        sizeof(py::wrapper::Windows::Media::Ocr::OcrResult),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_OcrResult
    };

    // ----- OcrWord class --------------------
    constexpr const char* const _type_name_OcrWord = "OcrWord";

    static PyObject* _new_OcrWord(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_OcrWord);
        return nullptr;
    }

    static void _dealloc_OcrWord(py::wrapper::Windows::Media::Ocr::OcrWord* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* OcrWord_get_BoundingRect(py::wrapper::Windows::Media::Ocr::OcrWord* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.BoundingRect());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* OcrWord_get_Text(py::wrapper::Windows::Media::Ocr::OcrWord* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Text());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_OcrWord(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Media::Ocr::OcrWord>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_OcrWord[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_OcrWord), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_OcrWord[] = {
        { "bounding_rect", reinterpret_cast<getter>(OcrWord_get_BoundingRect), nullptr, nullptr, nullptr },
        { "text", reinterpret_cast<getter>(OcrWord_get_Text), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_OcrWord[] = 
    {
        { Py_tp_new, _new_OcrWord },
        { Py_tp_dealloc, _dealloc_OcrWord },
        { Py_tp_methods, _methods_OcrWord },
        { Py_tp_getset, _getset_OcrWord },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_OcrWord =
    {
        "_winsdk_Windows_Media_Ocr.OcrWord",
        sizeof(py::wrapper::Windows::Media::Ocr::OcrWord),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_OcrWord
    };

    // ----- Windows.Media.Ocr Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Media::Ocr::OcrEngine>::python_type = py::register_python_type(module, _type_name_OcrEngine, &_type_spec_OcrEngine, bases.get());
            py::winrt_type<winrt::Windows::Media::Ocr::OcrLine>::python_type = py::register_python_type(module, _type_name_OcrLine, &_type_spec_OcrLine, bases.get());
            py::winrt_type<winrt::Windows::Media::Ocr::OcrResult>::python_type = py::register_python_type(module, _type_name_OcrResult, &_type_spec_OcrResult, bases.get());
            py::winrt_type<winrt::Windows::Media::Ocr::OcrWord>::python_type = py::register_python_type(module, _type_name_OcrWord, &_type_spec_OcrWord, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Media.Ocr");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Media_Ocr",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Media::Ocr

PyMODINIT_FUNC
PyInit__winsdk_Windows_Media_Ocr (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Media::Ocr::module_def);
}