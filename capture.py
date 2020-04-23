from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (800, 600)
camera.framerate = 25
camera.rotation = 180

camera.start_preview()

for loop in range(200):
    camera.start_recording('/home/pi/recordings/pond' + str(loop) + '.h264')
    sleep(45)
    camera.stop_recording()
camera.stop_preview()