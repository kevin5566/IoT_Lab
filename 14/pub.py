## Publish slide msg to subscriber
import paho.mqtt.client as mqtt
import grovepi

client = mqtt.Client()
client.connect('127.0.0.1')

value = float(grovepi.analogRead(15))
bright = int((value/1023)*255)

client.publish('MyHome/Bedroom/AirConditioning/Power', bright)
client.loop()
client.disconnect()

