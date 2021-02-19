from adafruit_clue import clue
from adafruit_clue import time

clue_display = clue.simple_text_display(title="MESSAGE STREAMER", title_scale=2,text_scale=1,title_color=(255,0,0))

msg = "This message moves from right to left" 
msg2= "This message moves from left to right"
while True:
    clue_display[4].text = msg
    clue_display[4].color= clue.YELLOW
    clue_display[4].scale=2

    clue_display[7].text = msg2
    clue_display[7].color=clue.WHITE
    clue_display[7].scale=2

    clue_display[10].text = "This message blinks"
    clue_display[10].color= clue.SKY
    clue_display[10].scale=2
    time.sleep(1)
    clue_display[10].color=clue.BLACK  

    clue_display.show()

    removedFirstLetter = msg[0:1]         
    msg = msg[1:] + removedFirstLetter    

    removedLastLetter=msg2[-1:]          
    msg2=removedLastLetter + msg2[:-1]   