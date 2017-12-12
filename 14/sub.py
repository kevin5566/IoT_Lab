## Busy wait message
import paho.mqtt.client as mqtt
import grovepi

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.subscribe("MyHome/Bedroom/AirConditioning/#")

def on_message(client, userdata, message):
    print(str(message.payload))
    value = int(message.payload)
    grovepi.analogWrite(3, value)

client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost")

while True:
    client.loop()
