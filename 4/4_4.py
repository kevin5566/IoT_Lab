#When you press the button, LED should turn from on to off, or off to on.
import time
import grovepi

led = 9
button = 6

grovepi.pinMode(led,"OUTPUT")
grovepi.pinMode(button,"INPUT")

flag = False
'''
while(True):
    print grovepi.digitalRead(button)
'''

while(True):
    if grovepi.digitalRead(button) is 1:
        flag=flag ^ True
    grovepi.digitalWrite(led, flag)
    #time.sleep(1)