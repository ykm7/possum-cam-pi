# https://picamera.readthedocs.io/en/release-1.13/recipes1.html
# https://maker.pro/raspberry-pi/tutorial/how-to-interface-a-pir-motion-sensor-with-raspberry-pi-gpio

import RPi.GPIO as GPIO
from picamera import PiCamera
import time
from fractions import Fraction

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)  # Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)  # LED output pin

path = '/home/pi/motion_images/'

def start_camera_system():
    detect_motion()

def detect_motion():
    while True:
        i = GPIO.input(11)
        if (i == 1):
            takeImage()
            time.sleep(10)

def takeImage():
    global path
    # Force sensor mode 3 (the long exposure mode), set
    # the framerate to 1/6fps, the shutter speed to 6s,
    # and ISO to 800 (for maximum gain)
    with PiCamera(resolution=(1280, 720), framerate=Fraction(1, 6), sensor_mode=3) as camera:

            # Disable to LED
        camera.led = False
        camera.shutter_speed = 6000000
        camera.iso = 800
        # Give the camera a good long time to set gains and
        # measure AWB (you may wish to use fixed AWB instead)
        time.sleep(10)
        camera.exposure_mode = 'off'
        # Finally, capture an image with a 6s exposure. Due
        # to mode switching on the still port, this will take
        # longer than 6 seconds
        currentTime = time.asctime(time.localtime(time.time()))
        filename = path + str(currentTime) + ".jpg"
        camera.capture(filename)


