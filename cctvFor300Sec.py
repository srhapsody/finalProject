from picamera import PiCamera
from time import sleep
import time
import datetime

camera = PiCamera()
now = datetime.datetime.now()
filename = now.strftime('%Y-%m-%d %H:%M:%S')
camera.start_recording(output = '/home/pi/picam/' + filename + '.h264')
sleep(300)
camera.stop_recording()
