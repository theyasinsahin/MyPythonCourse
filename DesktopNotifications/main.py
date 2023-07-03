from notifypy import Notify

notification = Notify()
notification.title = "Call The Ambulance"
notification.message = "But not for me"
#notification.icon = "Image.jpg"
notification.send()

