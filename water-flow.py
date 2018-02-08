import RPi.GPIO as GPIO
import time, sys


GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global x
x = 0

def countPulse(channel):
   global x
   x = x + 1

GPIO.add_event_detect(7, GPIO.FALLING, callback=countPulse)

while True:
    try:
        time.sleep(1)
        rate = 2 * x - 10
        if rate < 0:
            rate =0
        volume = rate/60
	print 'volume %d L' %(volume)
    except KeyboardInterrupt:
        print '\ncaught keyboard interrupt!, bye'
        GPIO.cleanup()
        sys.exit()
