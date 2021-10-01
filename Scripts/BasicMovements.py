from djitellopy import tello
from time import sleep

me = tello.Tello()          # Creating a new Tello object
me.connect()

print(me.get_battery())

me.takeoff()
me.send_rc_control(0, 50, 0, 0)     # Move forward for 2 seconds
sleep(2)
me.send_rc_control(30, 0, 0, 0)     # Then more right for 2 seconds
sleep(2)
me.send_rc_control(0, 0, 0, 30)     # Rotate right for 2 seconds
sleep(2)
me.send_rc_control(0,0,0,0)         # tell it to stop moving forwards before landing
me.land()

