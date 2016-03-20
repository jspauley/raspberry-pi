import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(5,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
	input_state = GPIO.input(5)
	if input_state == False:
		GPIO.output(26,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(26,GPIO.LOW)
		time.sleep(1)

GPIO.cleanup()
