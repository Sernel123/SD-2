"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.
To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython
Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue
import paho.mqtt.client as mqtt
import json

controller = {
    "accelerometer" : [0,0,0],
    "gyroscope" : [0,0,0] ,
    "magnetometer" : [0,0,0] ,
    "pressure" : 1013,
    "altitude" : 0, #Bonus
    "temperature" : 0,
    "humidity": 0,
    "proximity" : 0,
    "color" : [0,0,0,0],

}
def display_text(value):
    clue_data[0].text = "Accel: {} {} {} m/s^2".format(*controller["accelerometer"])
    clue_data[1].text = "Gyro: {} {} {} dps".format(*controller["gyroscope"])
    clue_data[2].text = "Magnetic: {} {} {} uTesla".format(*controller["magnetometer"])
    clue_data[3].text = "Pressure: {} hPa".format(controller["pressure"])
    clue_data[4].text = "Altitude: {:.0f} m".format(clue.altitude) #Bonus
    clue_data[5].text = "Temperature: {} C".format(controller["temperature"])
    clue_data[6].text = "Humidity: {} %".format(controller["humidity"])
    clue_data[7].text = "Proximity: {}".format(controller["proximity"])
    clue_data[8].text = "Color: R:{} G:{} B:{} C:{}".format(*controller["color"])
    clue_data.show()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("clue-slider")
        display_text(0)

def on_message(client, userdata, msg):
    # display_text(int(msg.payload.decode()))
    payload = json.loads(msg.payload)
    if (payload["checker"] == "accX"):
        controller["accelerometer"][0] = payload["value"]
        display_text(controller["accelerometer"][0])
    elif (payload["checker"] == "accY"):
        controller["accelerometer"][1] = payload["value"]
        display_text(controller["accelerometer"][1])
    elif (payload["checker"] == "accZ"):
        controller["accelerometer"][2] = payload["value"]
        display_text(controller["accelerometer"][2])
    elif (payload["checker"] == "gyroX"):
        controller["gyroscope"][0] = payload["value"]
        display_text(controller["gyroscope"][0])
    elif (payload["checker"] == "gyroY"):
        controller["gyroscope"][1] = payload["value"]
        display_text(controller["gyroscope"][1])
    elif (payload["checker"] == "gyroZ"):
        controller["gyroscope"][2] = payload["value"]
        display_text(controller["gyroscope"][2])
    elif (payload["checker"] == "magnetX"):
        controller["magnetometer"][0] = payload["value"]
        display_text(controller["magnetometer"][0])
    elif (payload["checker"] == "magnetY"):
        controller["magnetometer"][1] = payload["value"]
        display_text(controller["magnetometer"][1])
    elif (payload["checker"] == "magnetZ"):
        controller["magnetometer"][2] = payload["value"]
        display_text(controller["magnetometer"][2])
    elif (payload["checker"] == "press"):
        controller["pressure"] = payload["value"]
        display_text(controller["pressure"])
    elif (payload["checker"] == "temp"):
        controller["temperature"] = payload["value"]
        display_text(controller["temperature"])
    elif (payload["checker"] == "humid"):
        controller["humidity"] = payload["value"]
        display_text(controller["humidity"])
    elif (payload["checker"] == "proxim"):
        controller["proximity"] = payload["value"]
        display_text(controller["proximity"])
    elif (payload["checker"] == "colorR"):
        controller["color"][0] = payload["value"]
        display_text(controller["color"][0])
    elif (payload["checker"] == "colorG"):
        controller["color"][1] = payload["value"]
        display_text(controller["color"][1])
    elif (payload["checker"] == "colorB"):
        controller["color"][2] = payload["value"]
        display_text(controller["color"][2])
    elif (payload["checker"] == "colorC"):
        controller["color"][3] = payload["value"]
        display_text(controller["color"][3])
    else:
        print("Not subscribed!")
    
        
    
clue.sea_level_pressure = 1020

clue_data = clue.simple_text_display(text_scale=2)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()