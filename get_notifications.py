# from win10toast import ToastNotifier

# toast = ToastNotifier()
# toast.show_toast(
#     "Mr_M",
#     "hey megzz time to study dont be lazy son of bit**",
#     duration = 10,
#     icon_path = "icon.ico",
#     threaded = True,
# )
import schedule
import time
from plyer import notification

def notifications():
    notification.notify(
    title = "Mr_DUP",
    message = "Wake him UPPPPPPPPPP",
    timeout = 20
    )
schedule.every(2).hours.do(notifications)


while True:
    schedule.run_pending()
    time.sleep(1)

'''this for scheduling notifications'''