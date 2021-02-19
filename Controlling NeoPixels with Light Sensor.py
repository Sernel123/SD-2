"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# import CPX library
# from adafruit_circuitplayground import cp


# while True:
#     color = int(255 * cp.light / 320)
#     if (0 < cp.light <= 32):
#         cp.pixels[0]= (color, color, color)
#     elif (33 < cp.light <= 64):
#         cp.pixels[1]= (color, color, color)
#     elif (65 < cp.light <= 96):
#         cp.pixels[2]= (color, color, color)
#     elif (97 < cp.light <= 128):
#         cp.pixels[3]= (color, color, color)
#     elif (129 < cp.light <= 160):
#         cp.pixels[4]= (color, color, color)
#     elif (161 < cp.light <= 192):
#         cp.pixels[5]= (color, color, color)
#     elif (193 < cp.light <= 224):
#         cp.pixels[6]= (color, color, color)
#     elif (225 < cp.light <= 256):
#         cp.pixels[7]= (color, color, color)
#     elif (257 < cp.light <= 288):
#         cp.pixels[8]= (color, color, color)
#     elif (289 < cp.light <= 320):
#         cp.pixels[9]= (color, color, color)
    


from adafruit_circuitplayground import time
import cp 

def scale_range(value):   
    return value / 288 * 9 
    while True:
        peak = scale_range(cp.light) 
        for i in range(10): 
            if i <= peak: 
                if(peak < 1): 
                    color = int(255*cp.light/32) 
                    cp.pixels[0] = (color, color, color) 
                elif(peak < 2 and peak >= 1): 
                    color = int(255*(cp.light-32)/32) 
                    cp.pixels[1] = (color, color, color) 
                elif(peak < 3 and peak >= 2): 
                    color = int(255*(cp.light-64)/32) 
                    cp.pixels[2] = (color, color, color) 
                elif(peak < 4 and peak >= 3): 
                    color = int(255*(cp.light-96)/32) 
                    cp.pixels[3] = (color, color, color) 
                elif(peak < 5 and peak >= 4): 
                    color = int(255*(cp.light-128)/32) 
                    cp.pixels[4] = (color, color, color) 
                elif(peak < 6 and peak >= 5): 
                    color = int(255*(cp.light-160)/32) 
                    cp.pixels[5] = (color, color, color) 
                elif(peak < 7 and peak >= 6): 
                    color = int(255*(cp.light-192)/32) 
                    cp.pixels[6] = (color, color, color) 
                elif(peak < 8 and peak >= 7): 
                    color = int(255*(cp.light-224)/32) 
                    cp.pixels[7] = (color, color, color) 
                elif(peak < 9 and peak >= 8): 
                    color = int(255*(cp.light-256)/32) 
                    cp.pixels[8] = (color, color, color) 
                elif(peak < 10 and peak >= 2): 
                    color = int(255*(cp.light-288)/32) 
                    cp.pixels[9] = (color, color, color) 
                else: 
                    cp.pixels[i] = (0, 0, 0) 
                    cp.pixels.show() 
                    time.sleep(0.05)