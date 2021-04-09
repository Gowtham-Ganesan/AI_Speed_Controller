import Adafruit_BBIO.GPIO as GPIO
from time import sleep
outPin='P9_12'
GPIO.setup(outPin,GPIO.OUT)
GPIO.output(outPin,GPIO.HIGH)
sleep(20)
GPIO.output(outPin,GPIO.LOW)
sleep(20)
GPIO.output(outPin,GPIO.HIGH)
GPIO.cleanup()
