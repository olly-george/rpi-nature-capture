from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (800, 600)
camera.framerate = 20
camera.rotation = 270

camera.start_preview()
camera.start_recording('/home/pi/recordings/test3.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()