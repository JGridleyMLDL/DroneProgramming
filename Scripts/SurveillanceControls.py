'''
This is a script that will give you remote access to the drone from the keyboard.
There will also be a video stream on the monitor and the ability to take photos
(or videos) and save them on your computer.
Extension of Keyboard Control and Image Capture
'''

from djitellopy import tello
import time
import KeyPressModule as kp
import cv2

kp.init()
me = tello.Tello()
me.connect()

print(me.get_battery())             # Status Check
me.stream_on()

global img
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

    if kp.getKey("q"): me.land(); time.sleep(3)
    if kp.getKey("e"): me.takeoff()

    if kp.getKey('z'):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg')
        time.sleep(0.3)

    return [lr, fb, ud, yv]

# Take Off
me.takeoff()

# Activate Keyboard Controls
while True:
    values = getKeyboardInput()
    me.send_rc_control(values[0], values[1], values[2], values[3])

    img = me.get_frame_read().frame()
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)

    cv2.waitKey(1)


