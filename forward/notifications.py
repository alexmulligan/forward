import sys

from winrt.windows.foundation.metadata import ApiInformation
from winrt.windows.ui.notifications.management import UserNotificationListener, UserNotificationListenerAccessStatus
from winrt.windows.ui.notifications import NotificationKinds, KnownNotificationBindings

import config
from notif import Notif

def check_NotificationListener() -> bool:
    """Prechecks to make sure Windows NotificationListener API works"""
    if not ApiInformation.is_type_present('Windows.UI.Notifications.Management.UserNotificationListener'):
        print("UserNotificationListener not supported")
        sys.exit(1)


async def get_NotificationListener() -> UserNotificationListener:
    """Get listener object from NotificationLister and check for access"""
    listener = UserNotificationListener.get_current()
    accessStatus = await listener.request_access_async()

    if not accessStatus == UserNotificationListenerAccessStatus.ALLOWED:
        print("UserNotificationListener access unavailable")
        sys.exit(1)
    
    return listener


def handle_notif(windows_notif, notif_listener):
    """extract necessary data from windows notification object and put it into Notif object in order to call outputs"""

    if hasattr(windows_notif, 'app_info'):
        app_name = windows_notif.app_info.display_info.display_name
        text_sequence = windows_notif.notification.visual.get_binding(
            KnownNotificationBindings.get_toast_generic()).get_text_elements()
        
        it = iter(text_sequence)
        title = it.current.text
        text = []
        while True:
            next(it, None)
            if it.has_current:
                text.append(it.current.text)
            else:
                break

        # check if whitelist is enabled and skip unlisted notifs
        if len(config.APP_WHITELIST) > 0:
            skip = True
            for app in config.APP_WHITELIST:
                if app in app_name.lower():
                    if config.DEBUG:
                        print(f"DEBUG: found notif in whitelist - {app}")
                    skip = False
                else:
                    if config.DEBUG:
                        print(f"DEBUG: skipping notif - {app}")
            if skip:
                return

        # call outputs for notification
        notif = Notif(app_name, title, text)
        for option in config.OUTPUTS:
            if option == 'console':
                if config.DEBUG:
                    print(f"DEBUG: calling console output - {notif.app_name}")
                notif.output_console()

            elif option == 'telegram':
                if config.DEBUG:
                    print(f"DEBUG: calling telegram output - {notif.app_name}")
                notif.output_telegram()
            
            elif option == 'email':
                if config.DEBUG:
                    print(f"DEBUG: calling email output - {notif.app_name}")
                notif.output_email()

            else:
                print(f"ERROR: Unknown output option: {option}")

        # clear notitification so it's not handled again
        notif_listener.remove_notification(windows_notif.id)
