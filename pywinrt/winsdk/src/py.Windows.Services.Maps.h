// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Devices.Geolocation.h")
#include "py.Windows.Devices.Geolocation.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.UI.Popups.h")
#include "py.Windows.UI.Popups.h"
#endif

#include <winrt/Windows.Services.Maps.h>

namespace py::proj::Windows::Services::Maps
{}

namespace py::impl::Windows::Services::Maps
{}

namespace py::wrapper::Windows::Services::Maps
{
    using EnhancedWaypoint = py::winrt_wrapper<winrt::Windows::Services::Maps::EnhancedWaypoint>;
    using ManeuverWarning = py::winrt_wrapper<winrt::Windows::Services::Maps::ManeuverWarning>;
    using MapAddress = py::winrt_wrapper<winrt::Windows::Services::Maps::MapAddress>;
    using MapLocation = py::winrt_wrapper<winrt::Windows::Services::Maps::MapLocation>;
    using MapLocationFinder = py::winrt_wrapper<winrt::Windows::Services::Maps::MapLocationFinder>;
    using MapLocationFinderResult = py::winrt_wrapper<winrt::Windows::Services::Maps::MapLocationFinderResult>;
    using MapManager = py::winrt_wrapper<winrt::Windows::Services::Maps::MapManager>;
    using MapRoute = py::winrt_wrapper<winrt::Windows::Services::Maps::MapRoute>;
    using MapRouteDrivingOptions = py::winrt_wrapper<winrt::Windows::Services::Maps::MapRouteDrivingOptions>;
    using MapRouteFinder = py::winrt_wrapper<winrt::Windows::Services::Maps::MapRouteFinder>;
    using MapRouteFinderResult = py::winrt_wrapper<winrt::Windows::Services::Maps::MapRouteFinderResult>;
    using MapRouteLeg = py::winrt_wrapper<winrt::Windows::Services::Maps::MapRouteLeg>;
    using MapRouteManeuver = py::winrt_wrapper<winrt::Windows::Services::Maps::MapRouteManeuver>;
    using MapService = py::winrt_wrapper<winrt::Windows::Services::Maps::MapService>;
    using PlaceInfo = py::winrt_wrapper<winrt::Windows::Services::Maps::PlaceInfo>;
    using PlaceInfoCreateOptions = py::winrt_wrapper<winrt::Windows::Services::Maps::PlaceInfoCreateOptions>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Services::Maps::EnhancedWaypoint>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::ManeuverWarning>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::MapAddress>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::MapLocation>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::MapLocationFinder>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::MapLocationFinderResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::MapManager>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::MapRoute>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::MapRouteDrivingOptions>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::MapRouteFinder>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::MapRouteFinderResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::MapRouteLeg>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::MapRouteManeuver>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::MapService>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::PlaceInfo>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::PlaceInfoCreateOptions>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}