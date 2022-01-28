// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.ApplicationModel.AppService.h")
#include "py.Windows.ApplicationModel.AppService.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Graphics.DirectX.h")
#include "py.Windows.Graphics.DirectX.h"
#endif

#if __has_include("py.Windows.Graphics.DirectX.Direct3D11.h")
#include "py.Windows.Graphics.DirectX.Direct3D11.h"
#endif

#if __has_include("py.Windows.Graphics.Imaging.h")
#include "py.Windows.Graphics.Imaging.h"
#endif

#if __has_include("py.Windows.Storage.h")
#include "py.Windows.Storage.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#include <winrt/Windows.Media.h>

namespace py::proj::Windows::Media
{}

namespace py::impl::Windows::Media
{}

namespace py::wrapper::Windows::Media
{
    using AudioBuffer = py::winrt_wrapper<winrt::Windows::Media::AudioBuffer>;
    using AudioFrame = py::winrt_wrapper<winrt::Windows::Media::AudioFrame>;
    using AutoRepeatModeChangeRequestedEventArgs = py::winrt_wrapper<winrt::Windows::Media::AutoRepeatModeChangeRequestedEventArgs>;
    using ImageDisplayProperties = py::winrt_wrapper<winrt::Windows::Media::ImageDisplayProperties>;
    using MediaExtensionManager = py::winrt_wrapper<winrt::Windows::Media::MediaExtensionManager>;
    using MediaMarkerTypes = py::winrt_wrapper<winrt::Windows::Media::MediaMarkerTypes>;
    using MediaProcessingTriggerDetails = py::winrt_wrapper<winrt::Windows::Media::MediaProcessingTriggerDetails>;
    using MediaTimelineController = py::winrt_wrapper<winrt::Windows::Media::MediaTimelineController>;
    using MediaTimelineControllerFailedEventArgs = py::winrt_wrapper<winrt::Windows::Media::MediaTimelineControllerFailedEventArgs>;
    using MusicDisplayProperties = py::winrt_wrapper<winrt::Windows::Media::MusicDisplayProperties>;
    using PlaybackPositionChangeRequestedEventArgs = py::winrt_wrapper<winrt::Windows::Media::PlaybackPositionChangeRequestedEventArgs>;
    using PlaybackRateChangeRequestedEventArgs = py::winrt_wrapper<winrt::Windows::Media::PlaybackRateChangeRequestedEventArgs>;
    using ShuffleEnabledChangeRequestedEventArgs = py::winrt_wrapper<winrt::Windows::Media::ShuffleEnabledChangeRequestedEventArgs>;
    using SystemMediaTransportControls = py::winrt_wrapper<winrt::Windows::Media::SystemMediaTransportControls>;
    using SystemMediaTransportControlsButtonPressedEventArgs = py::winrt_wrapper<winrt::Windows::Media::SystemMediaTransportControlsButtonPressedEventArgs>;
    using SystemMediaTransportControlsDisplayUpdater = py::winrt_wrapper<winrt::Windows::Media::SystemMediaTransportControlsDisplayUpdater>;
    using SystemMediaTransportControlsPropertyChangedEventArgs = py::winrt_wrapper<winrt::Windows::Media::SystemMediaTransportControlsPropertyChangedEventArgs>;
    using SystemMediaTransportControlsTimelineProperties = py::winrt_wrapper<winrt::Windows::Media::SystemMediaTransportControlsTimelineProperties>;
    using VideoDisplayProperties = py::winrt_wrapper<winrt::Windows::Media::VideoDisplayProperties>;
    using VideoEffects = py::winrt_wrapper<winrt::Windows::Media::VideoEffects>;
    using VideoFrame = py::winrt_wrapper<winrt::Windows::Media::VideoFrame>;
    using IMediaExtension = py::winrt_wrapper<winrt::Windows::Media::IMediaExtension>;
    using IMediaFrame = py::winrt_wrapper<winrt::Windows::Media::IMediaFrame>;
    using IMediaMarker = py::winrt_wrapper<winrt::Windows::Media::IMediaMarker>;
    using IMediaMarkers = py::winrt_wrapper<winrt::Windows::Media::IMediaMarkers>;
    using MediaTimeRange = py::winrt_struct_wrapper<winrt::Windows::Media::MediaTimeRange>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Media::AudioBuffer>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::AudioFrame>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::AutoRepeatModeChangeRequestedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::ImageDisplayProperties>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::MediaExtensionManager>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::MediaMarkerTypes>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::MediaProcessingTriggerDetails>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::MediaTimelineController>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::MediaTimelineControllerFailedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::MusicDisplayProperties>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::PlaybackPositionChangeRequestedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::PlaybackRateChangeRequestedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::ShuffleEnabledChangeRequestedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::SystemMediaTransportControls>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::SystemMediaTransportControlsButtonPressedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::SystemMediaTransportControlsDisplayUpdater>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::SystemMediaTransportControlsPropertyChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::SystemMediaTransportControlsTimelineProperties>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::VideoDisplayProperties>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::VideoEffects>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::VideoFrame>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::IMediaExtension>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::IMediaFrame>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::IMediaMarker>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::IMediaMarkers>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::MediaTimeRange>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct converter<winrt::Windows::Media::MediaTimeRange>
    {
        static PyObject* convert(winrt::Windows::Media::MediaTimeRange instance) noexcept;
        static winrt::Windows::Media::MediaTimeRange convert_to(PyObject* obj);
    };

}