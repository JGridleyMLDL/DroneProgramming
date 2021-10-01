from djitellopy import tello
from time import sleep
import KeyPressModule as kp

kp.init()
me = tello.Tello()
me.connect()

print(me.get_battery())             # Status Check

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50                      #Default Speed

    # Left and Right Controls
    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    # Forward and Backwards Controls
    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    # Up and Down Controls
    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    # Up and Down Controls
    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("q"): me.land()
    if kp.getKey("e"): me.takeoff()

    return [lr, fb, ud, yv]

# Take Off
me.takeoff()

# Activate Keyboard Controls
while True:
    values = getKeyboardInput()
    me.send_rc_control(values[0], values[1], values[2], values[3])
    sleep(0.05)

