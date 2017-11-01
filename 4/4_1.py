#If you are pushing the button, turn on LED. Otherwise, turn off LED.
import RPi.GPIO as GPIO

led = 22
button = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)

GPIO.setup(button, GPIO.IN)

##GPIO.add_event_detect(button, GPIO.RISING)

while(True):
    input = GPIO.input(button)
    if input > 0:
        GPIO.output(led, GPIO.HIGH)
    else:
        GPIO.output(led, GPIO.LOW)