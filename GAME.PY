import random

def rock_paper_scissor():
    choice=["rock","paper","scissor"]
    
    player_score=0
    computer_score=0
    
    while True:
        computer=random.choice(choice)
        player=input(" rock , paper , scissor : ").lower()
         
        if player=="0" or  player=="exit":
           break

        if player!= "rock" and player!= "paper" and player!= "scissor":
            print(" only rock, paper and scissor are allowed :) ")
            player=input(" rock , paper , scissor : ")

        if player=="rock" and computer=="paper":
           print("computer :"+computer)
           print("player :"+player)
           print("<<< computer won! >>>")
           computer_score+=1

        if player=="rock" and computer=="scissor":
           print("computer :"+computer)
           print("player :"+player)
           print("<<< you won! >>>")
           player_score+=1
    
        if player==computer:
           print("computer :"+computer)
           print("player :"+player)
           print("<<< Tie! >>>")
 
        if player=="paper" and computer=="rock":
           print("computer :"+computer)
           print("player :"+player)
           print("<<< You won! >>>")
           player_score+=1

        if player=="paper" and computer=="scissor":
           print("computer :"+computer)
           print("player :"+player)
           print("<<< computer won! >>>")
           computer_score+=1

        
        if player=="scissor" and computer=="paper":
           print("computer :"+computer)
           print("player :"+player)
           print("<<< YOU WON! >>>")
           player_score+=1

        if player=="scissor" and computer=="rock":
           print("computer :"+computer)
           print("player :"+player)
           print("<<< COMPUTER WON! >>>")
           computer_score+=1


        
        print("                      computer : "+str(computer_score)+" | "+" player :"+str(player_score))


        if player_score==3:
           print("                      YOU ARE THE WINNER! :) ")
           break
        elif computer_score==3:
           print("                      GAME OVER!  :( ")
           break
        
rock_paper_scissor()