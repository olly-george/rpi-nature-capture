from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (800, 600)
camera.framerate = 20
camera.rotation = 90

camera.start_preview()

loop = 0
while loop < 10
    camera.start_recording('/home/pi/recordings/test' + loop + '.h264')
    sleep(3)
    camera.stop_recording()
    loop++
camera.stop_preview()