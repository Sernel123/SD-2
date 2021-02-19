from microbit import *
from time import sleep

# counter = 0

while True:
    for y in range (0,5):
        for x in range (0,5):
            display.set_pixel(x,y,9)
            sleep(0.5)
            display.set_pixel(x,y,0)
    
    
        



