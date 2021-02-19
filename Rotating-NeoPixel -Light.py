"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# import CPX library
from adafruit_circuitplayground import cp
from time import sleep
from random import randint

cp.pixels.brightness = 1


counter = 9

while True:

    if cp.switch:
         
        if counter > 9:
            counter = 0

        else:
            
            cp.pixels[counter] = (255, 255, 255)
            sleep(0.5)
            cp.pixels[counter] = (0, 0, 0)
            counter+=1   
           
    else:
        
        if counter < 0:
            counter = 9
            
        else:
            
            cp.pixels[counter] = (255, 255, 255)
            sleep(0.5)
            cp.pixels[counter] = (0, 0, 0)
            counter-=1

        
        
            
    
        
        