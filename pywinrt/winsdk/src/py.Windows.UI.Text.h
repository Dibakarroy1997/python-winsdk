// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#if __has_include("py.Windows.UI.h")
#include "py.Windows.UI.h"
#endif

#include <winrt/Windows.UI.Text.h>

namespace py::proj::Windows::UI::Text
{}

namespace py::impl::Windows::UI::Text
{}

namespace py::wrapper::Windows::UI::Text
{
    using ContentLinkInfo = py::winrt_wrapper<winrt::Windows::UI::Text::ContentLinkInfo>;
    using FontWeights = py::winrt_wrapper<winrt::Windows::UI::Text::FontWeights>;
    using RichEditTextDocument = py::winrt_wrapper<winrt::Windows::UI::Text::RichEditTextDocument>;
    using RichEditTextRange = py::winrt_wrapper<winrt::Windows::UI::Text::RichEditTextRange>;
    using TextConstants = py::winrt_wrapper<winrt::Windows::UI::Text::TextConstants>;
    using ITextCharacterFormat = py::winrt_wrapper<winrt::Windows::UI::Text::ITextCharacterFormat>;
    using ITextDocument = py::winrt_wrapper<winrt::Windows::UI::Text::ITextDocument>;
    using ITextParagraphFormat = py::winrt_wrapper<winrt::Windows::UI::Text::ITextParagraphFormat>;
    using ITextRange = py::winrt_wrapper<winrt::Windows::UI::Text::ITextRange>;
    using ITextSelection = py::winrt_wrapper<winrt::Windows::UI::Text::ITextSelection>;
    using FontWeight = py::winrt_struct_wrapper<winrt::Windows::UI::Text::FontWeight>;
}

namespace py
{

    template<>
    struct py_type<winrt::Windows::UI::Text::CaretType>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::FindOptions>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::FontStretch>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::FontStyle>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::FormatEffect>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::HorizontalCharacterAlignment>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::LetterCase>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::LineSpacingRule>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::LinkType>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::MarkerAlignment>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::MarkerStyle>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::MarkerType>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::ParagraphAlignment>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::ParagraphStyle>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::PointOptions>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::RangeGravity>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::RichEditMathMode>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::SelectionOptions>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::SelectionType>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::TabAlignment>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::TabLeader>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::TextDecorations>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::TextGetOptions>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::TextRangeUnit>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::TextScript>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::TextSetOptions>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::UnderlineType>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::UI::Text::VerticalCharacterAlignment>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Text::ContentLinkInfo>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Text::FontWeights>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Text::RichEditTextDocument>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Text::RichEditTextRange>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Text::TextConstants>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Text::ITextCharacterFormat>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Text::ITextDocument>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Text::ITextParagraphFormat>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Text::ITextRange>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Text::ITextSelection>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Text::FontWeight>
    {
        static PyTypeObject* get_python_type() noexcept;
    };
    template<>
    struct converter<winrt::Windows::UI::Text::FontWeight>
    {
        static PyObject* convert(winrt::Windows::UI::Text::FontWeight instance) noexcept;
        static winrt::Windows::UI::Text::FontWeight convert_to(PyObject* obj);
    };

}
