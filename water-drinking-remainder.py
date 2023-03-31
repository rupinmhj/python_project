import time
from plyer import notification

interval=60
x=0
while x==1:
    time.sleep(interval)
    
    #send a desktop notification
    notification.notify(
        title='drink water',
        message='Drink a water!!!!',
        app_name='Water drinking remainder',
        timeout=15
        
    )