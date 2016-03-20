import RPi.GPIO as GPIO
import time

red = 26
ourdelay = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)

def activateLED(pin,delay):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(pin,GPIO.LOW)
	return;

activateLED(red,ourdelay)

GPIO.cleanup()
