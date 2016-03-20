import RPi.GPIO as GPIO
import time

pinNum = input('Enter a GPIO pin number: ')

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNum,GPIO.OUT) #LED
GPIO.setup(5,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Button
GPIO.output(pinNum,True) #Turns LED off to start

while True:
	if (GPIO.input(5) == False):
		GPIO.output(pinNum,False)
		time.sleep(1)
		GPIO.output(pinNum,True)
		time.sleep(1)

GPIO.cleanup()
