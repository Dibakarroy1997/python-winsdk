// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.ApplicationModel.h")
#include "py.Windows.ApplicationModel.h"
#endif

#if __has_include("py.Windows.Data.Xml.Dom.h")
#include "py.Windows.Data.Xml.Dom.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.System.h")
#include "py.Windows.System.h"
#endif

#include <winrt/Windows.UI.Notifications.h>

namespace py::proj::Windows::UI::Notifications
{}

namespace py::impl::Windows::UI::Notifications
{}

namespace py::wrapper::Windows::UI::Notifications
{
    using AdaptiveNotificationText = py::winrt_wrapper<winrt::Windows::UI::Notifications::AdaptiveNotificationText>;
    using BadgeNotification = py::winrt_wrapper<winrt::Windows::UI::Notifications::BadgeNotification>;
    using BadgeUpdateManager = py::winrt_wrapper<winrt::Windows::UI::Notifications::BadgeUpdateManager>;
    using BadgeUpdateManagerForUser = py::winrt_wrapper<winrt::Windows::UI::Notifications::BadgeUpdateManagerForUser>;
    using BadgeUpdater = py::winrt_wrapper<winrt::Windows::UI::Notifications::BadgeUpdater>;
    using KnownAdaptiveNotificationHints = py::winrt_wrapper<winrt::Windows::UI::Notifications::KnownAdaptiveNotificationHints>;
    using KnownAdaptiveNotificationTextStyles = py::winrt_wrapper<winrt::Windows::UI::Notifications::KnownAdaptiveNotificationTextStyles>;
    using KnownNotificationBindings = py::winrt_wrapper<winrt::Windows::UI::Notifications::KnownNotificationBindings>;
    using Notification = py::winrt_wrapper<winrt::Windows::UI::Notifications::Notification>;
    using NotificationBinding = py::winrt_wrapper<winrt::Windows::UI::Notifications::NotificationBinding>;
    using NotificationData = py::winrt_wrapper<winrt::Windows::UI::Notifications::NotificationData>;
    using NotificationVisual = py::winrt_wrapper<winrt::Windows::UI::Notifications::NotificationVisual>;
    using ScheduledTileNotification = py::winrt_wrapper<winrt::Windows::UI::Notifications::ScheduledTileNotification>;
    using ScheduledToastNotification = py::winrt_wrapper<winrt::Windows::UI::Notifications::ScheduledToastNotification>;
    using ScheduledToastNotificationShowingEventArgs = py::winrt_wrapper<winrt::Windows::UI::Notifications::ScheduledToastNotificationShowingEventArgs>;
    using ShownTileNotification = py::winrt_wrapper<winrt::Windows::UI::Notifications::ShownTileNotification>;
    using TileFlyoutNotification = py::winrt_wrapper<winrt::Windows::UI::Notifications::TileFlyoutNotification>;
    using TileFlyoutUpdateManager = py::winrt_wrapper<winrt::Windows::UI::Notifications::TileFlyoutUpdateManager>;
    using TileFlyoutUpdater = py::winrt_wrapper<winrt::Windows::UI::Notifications::TileFlyoutUpdater>;
    using TileNotification = py::winrt_wrapper<winrt::Windows::UI::Notifications::TileNotification>;
    using TileUpdateManager = py::winrt_wrapper<winrt::Windows::UI::Notifications::TileUpdateManager>;
    using TileUpdateManagerForUser = py::winrt_wrapper<winrt::Windows::UI::Notifications::TileUpdateManagerForUser>;
    using TileUpdater = py::winrt_wrapper<winrt::Windows::UI::Notifications::TileUpdater>;
    using ToastActivatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Notifications::ToastActivatedEventArgs>;
    using ToastCollection = py::winrt_wrapper<winrt::Windows::UI::Notifications::ToastCollection>;
    using ToastCollectionManager = py::winrt_wrapper<winrt::Windows::UI::Notifications::ToastCollectionManager>;
    using ToastDismissedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Notifications::ToastDismissedEventArgs>;
    using ToastFailedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Notifications::ToastFailedEventArgs>;
    using ToastNotification = py::winrt_wrapper<winrt::Windows::UI::Notifications::ToastNotification>;
    using ToastNotificationActionTriggerDetail = py::winrt_wrapper<winrt::Windows::UI::Notifications::ToastNotificationActionTriggerDetail>;
    using ToastNotificationHistory = py::winrt_wrapper<winrt::Windows::UI::Notifications::ToastNotificationHistory>;
    using ToastNotificationHistoryChangedTriggerDetail = py::winrt_wrapper<winrt::Windows::UI::Notifications::ToastNotificationHistoryChangedTriggerDetail>;
    using ToastNotificationManager = py::winrt_wrapper<winrt::Windows::UI::Notifications::ToastNotificationManager>;
    using ToastNotificationManagerForUser = py::winrt_wrapper<winrt::Windows::UI::Notifications::ToastNotificationManagerForUser>;
    using ToastNotifier = py::winrt_wrapper<winrt::Windows::UI::Notifications::ToastNotifier>;
    using UserNotification = py::winrt_wrapper<winrt::Windows::UI::Notifications::UserNotification>;
    using UserNotificationChangedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Notifications::UserNotificationChangedEventArgs>;
    using IAdaptiveNotificationContent = py::winrt_wrapper<winrt::Windows::UI::Notifications::IAdaptiveNotificationContent>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::AdaptiveNotificationText>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::BadgeNotification>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::BadgeUpdateManager>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::BadgeUpdateManagerForUser>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::BadgeUpdater>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::KnownAdaptiveNotificationHints>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::KnownAdaptiveNotificationTextStyles>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::KnownNotificationBindings>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::Notification>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::NotificationBinding>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::NotificationData>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::NotificationVisual>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::ScheduledTileNotification>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::ScheduledToastNotification>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::ScheduledToastNotificationShowingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::ShownTileNotification>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::TileFlyoutNotification>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::TileFlyoutUpdateManager>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::TileFlyoutUpdater>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::TileNotification>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::TileUpdateManager>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::TileUpdateManagerForUser>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::TileUpdater>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::ToastActivatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::ToastCollection>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::ToastCollectionManager>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::ToastDismissedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::ToastFailedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::ToastNotification>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::ToastNotificationActionTriggerDetail>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::ToastNotificationHistory>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::ToastNotificationHistoryChangedTriggerDetail>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::ToastNotificationManager>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::ToastNotificationManagerForUser>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::ToastNotifier>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::UserNotification>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::UserNotificationChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Notifications::IAdaptiveNotificationContent>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}