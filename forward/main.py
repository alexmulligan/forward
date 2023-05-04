import time
import asyncio

import config
from notifications import check_NotificationListener, get_NotificationListener, handle_notif, NotificationKinds

__version__ = "1.2.0"


def validate_config():
    supported_outputs = ['console', 'telegram', 'email']

    assert config.SLEEP_TIME > 0
    assert len(config.OUTPUTS) > 0
    for output in config.OUTPUTS:
        assert output in supported_outputs


async def main():
    check_NotificationListener()
    listener = await get_NotificationListener()

    # Actively listen for new notifications and handle them
    listening = True
    while listening:
        if config.DEBUG:
            print("DEBUG: checking for new notifs")
        
        notifs = await listener.get_notifications_async(NotificationKinds.TOAST)
        if len(notifs) > 0:
            for notif in notifs:
                handle_notif(notif, listener)

        if config.DEBUG:
            print(f"DEBUG: sleeping for {config.SLEEP_TIME}s\n")
        time.sleep(config.SLEEP_TIME)


def run():
    print(f"\nforward - v{__version__}\n\n")

    if config.DEBUG:
        print("DEBUG: validating config.py")
    validate_config()

    asyncio.run(main())

if __name__ == '__main__':
    run()
