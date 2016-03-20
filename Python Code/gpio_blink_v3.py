import RPi.GPIO as GPIO
import time

pinNum = input('Enter a GPIO pin number: ')

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNum,GPIO.OUT)
while True:
	GPIO.output(pinNum,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(pinNum,GPIO.LOW)
	time.sleep(1)

GPIO.cleanup()
