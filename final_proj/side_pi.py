import grovepi
import requests
import time

url = 'http://10.5.0.152:8080/5/6'  ## Center Pi IP

signal_in = 3
grovepi.pinMode(signal_in, "INPUT")

## cnt = 0

while True:
    if grovepi.digitalRead(signal_in) is 1:
        resp = requests.get(url)
        print resp.content
        time.sleep(1)
        ## DEBUG ##        
        #cnt=cnt+1
        #cnt=cnt%10
        #print cnt
