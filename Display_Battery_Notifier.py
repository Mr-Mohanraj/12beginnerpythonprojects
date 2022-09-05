# # pip install plyer psutil
# from plyer import notification
# import psutil
# battery = psutil.sensors_battery() 
# percent = battery.percent

# if percent < 30:
import time
from plyer import notification
import psutil

class DesktopBatteryNotifier:
    def __init__(self) -> None:
        #  psutil.sensors_battery() return tuple of values are (percent=39, secsleft=4863, power_plugged=False)
        self.batteryPercentage = psutil.sensors_battery()[0]
        self.power_plugged = psutil.sensors_battery()[2]
    
    
    def notification_checker(self):
        if self.power_plugged:
            print("Your now plugged in.")
        elif self.batteryPercentage < 30:
            self.notification_sender()
    
    def notification_sender(self):
        notification.notify(
                title = "Battery Low",
                message="Your battery percentage is {0}".format(self.batteryPercentage) ,
                # displaying time
                timeout=10
    )
        # waiting time
        time.sleep(7)

if __name__=="__main__":
    notification_battery = DesktopBatteryNotifier()
    notification_battery.notification_checker()
