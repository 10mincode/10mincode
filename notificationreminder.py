from plyer import notification
import time
while True:
    notification.notify(
        title="Dummy notification",
        message="Dummy notification message",
        app_icon=None,
        timeout=10
    )
    time.sleep(60*60)