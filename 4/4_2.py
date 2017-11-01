#When you press the button, LED should turn from on to off, or off to on.
import RPi.GPIO as GPIO

led = 22
button = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)

GPIO.setup(button, GPIO.IN)
GPIO.add_event_detect(button, GPIO.RISING, bouncetime=200)
'''
while(1):
    GPIO.output(led, GPIO.LOW)
'''

while(True):
    if GPIO.event_detected(button):
        activate = True
        while ( activate ):
            GPIO.output(led, True)
            if GPIO.event_detected(button):
                activate = False
    else:
        GPIO.output(led, GPIO.LOW)