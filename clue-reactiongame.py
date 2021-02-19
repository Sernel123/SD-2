from adafruit_clue import clue
from time import sleep, time
from random import randint 


clue_display = clue.simple_text_display(title="REACTION GAME", title_scale=1, text_scale=2, title_color=(247, 247, 2))

while True:
    clue_display[0].text = "Instructions:"
    clue_display[0].color = clue.GREEN
    clue_display[1].text = "Player 1 press A"
    clue_display[1].color = clue.WHITE
    clue_display[2].text = "Player 2 press B"
    clue_display[2].color = clue.WHITE
    clue_display[3].text = "Press if the number"
    clue_display[3].color = clue.SKY
    clue_display[4].text = "is divisible by 2"
    clue_display[4].color = clue.SKY
    clue_display[5].text = "Maximum score of 5"
    clue_display[5].color = clue.YELLOW
    
   
    for i in range (3, 0, -1):
        clue_display[6].text = "Starts in " + str(i)
        clue_display[6] .color = clue.RED
        sleep(2)
        

        A_score = 0
        B_score = 0
      
        if i == 1:
            while True:
                num =  randint(1, 100)
                clue_display[0].text = ""
                clue_display[1].text = "" 
                clue_display[2].text = "" 
                clue_display[3].text = ""
                clue_display[4].text = "Player A score: " + str(A_score)
                clue_display[5].text = "Player B score: " + str(B_score)
                clue_display[6].text = ""

                clue_display[1].text = "        " + str(num)
                # print("I am here")
            
                measure1 = time()
                measure2 = time()
                counter = 1

                while counter > 0:
                    if measure2 - measure1 >= 1:
                        counter = 0
                    else:
                        measure2 = time()
                    
                    if clue.button_a:
                        print("Button A clicked!")
                        if num % 2 == 0:
                            A_score +=1
                        else: 
                            A_score -=1
                        break

                    if clue.button_b:
                        if num % 2 == 0:
                            B_score +=1
                        else:
                            B_score -=1
                        break
            
                if A_score == 5:
                    clue_display[1].text = ""
                    clue_display[1].text = "PLAYER A WINS!"
                    clue_display[1].color = clue.RED
                    break
                        
                    
                if B_score == 5:
                    clue_display[1].text = ""
                    clue_display[1].text = "PLAYER B WINS!"
                    clue_display[1].color = clue.RED
                    break
                       
            sleep(1)    
        clue_display.show()
   

        
                

                







    


       
       
      
       