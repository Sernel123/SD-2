from microbit import *
import paho.mqtt.client as mqtt

circle = Image('09990:90009:90009:90009:09990')


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("joystick-microbit")
        display.show(Image.YES)

def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode())
    if msg.payload.decode() == "N":
        display.show(Image.ARROW_N)

    elif msg.payload.decode() == "W":
        display.show(Image.ARROW_W)

    elif msg.payload.decode() == "E":
        display.show(Image.ARROW_E)

    elif msg.payload.decode() == "S":
        display.show(Image.ARROW_S)

    elif msg.payload.decode() == "NW":
        display.show(Image.ARROW_NW)
        
    elif msg.payload.decode() == "NE":
        display.show(Image.ARROW_NE)

    elif msg.payload.decode() == "SE":
        display.show(Image.ARROW_SE)

    elif msg.payload.decode() == "SW":
        display.show(Image.ARROW_SW)
    
    elif msg.payload.decode() == "C":
        display.show(circle)



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt