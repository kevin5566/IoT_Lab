#If you are pushing the button, turn on LED. Otherwise, turn off LED.
import time
import grovepi

led = 9
button = 6

grovepi.pinMode(led,"OUTPUT")
grovepi.pinMode(button,"INPUT")

while(True):
    grovepi.digitalWrite(led, grovepi.digitalRead(button))
    #time.sleep(1)