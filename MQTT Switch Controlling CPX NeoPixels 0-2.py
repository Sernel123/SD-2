from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    if rc == 0:
        cp.red_led = True
        client.subscribe("mqtt-switch")
    elif rc == 1:
        cp.red_led = True
        client.subscribe("mqtt-switch")
    elif rc== 2:
        cp.red_led = True
        client.subscribe("mqtt-switch")
    

def on_message(client, userdata, msg):
    # print(msg.topic+" "+msg.payload.decode())
    if msg.payload.decode() == "on0":
        cp.pixels[0] = (255, 255, 255)   
    elif msg.payload.decode() == "off0":
        cp.pixels[0] = (0, 0, 0)
    
    elif msg.payload.decode() == "on1":
        cp.pixels[1] = (255, 255, 255)
    elif msg.payload.decode() == "off1":
        cp.pixels[1] = (0, 0, 0)  

    elif msg.payload.decode() == "on2":
        cp.pixels[2] = (255, 255, 255)
    elif msg.payload.decode() == "off2":
        cp.pixels[2] = (0, 0, 0)   

cp.red_led = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt