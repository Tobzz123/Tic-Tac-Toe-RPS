#I, Olaoluwa Anthony-Egorp, 000776467, certify that all code submitted is my
#own work; that I have not copied it from any other source. I also certify that
#I have not allowed my work to be copied by others.

import random


def rpsls(player):

    import random

    print("In order to win your square you must win a game of Rock, Scissors, Paper, Lizard, Spock!")
    decision = input(player + " pick one of Rock, Paper, Scissors, Lizard, Spock: ")
    decision = decision.lower()

    dec_celebrity = ["rock", "paper", "scissors", "lizard", "spock"]
    c_decision = dec_celebrity[random.randint(2,3)]

    while (decision == c_decision):
        c_decision = dec_celebrity[random.randint(0,4)]

    interactions = ["crushes", "covers", "disproves", "cuts", "decapitates", "eats", "poisons", "smashes", "vaporizes"]

    winner1 = False

    #Player wins with rock
    if decision == "rock" and c_decision == "scissors":
        i = 0
        winner1 = True
    elif decision == "rock" and c_decision == "lizard":
        i = 0
        winner1 = True
    #Computer wins with rock
    elif c_decision == "rock" and decision == "scissors":
        
        i = 0

    elif c_decision == "rock" and decision == "lizard":
        i = 0
       
   #Player wins with paper
    elif decision == "paper" and c_decision == "rock":
        i = 1
        winner1 = True
    elif decision == "paper" and c_decision == "spock":
        i = 2
        winner1 = True
   #Computer wins with paper
    elif c_decision == "paper" and decision == "rock":
        i = 1
    elif c_decision == "paper" and decision == "spock":
        i = 2
       
   #Player wins with scissors    
    elif decision == "scissors" and c_decision == "paper":
        i = 3
        winner1 = True
    elif decision == "scissors" and c_decision == "lizard":
        i = 4
        winner1 = True
   #Computer wins with scissors    
    elif c_decision == "scissors" and decision == "paper":
        i = 3
    elif c_decision == "scissors" and decision == "lizard":
        i = 4
       
   #Player wins with lizard
    elif decision == "lizard" and c_decision == "paper":
        i = 5
        winner1 = True
    elif decision == "lizard" and c_decision == "spock":
        i = 6
        winner1 = True
   #Computer wins with lizard    
    elif c_decision == "lizard" and decision == "paper":
        i = 5
    elif c_decision == "lizard" and decision == "spock":
        i = 6

   #Player wins with spock    
    elif decision == "spock" and c_decision == "scissors":
        winner1 = True
        i = 7
    elif decision == "spock" and c_decision == "rock":
        i = 8
        winner1 = True
   #Computer wins with spock    
    elif c_decision == "spock" and decision == "scissors":
        i = 7
    elif c_decision == "spock" and decision == "rock":
        i = 8

    if winner1 == True:
        print("Our celebrity guest picked " + c_decision + "! " + decision + " " + str(interactions[i]) + " " + c_decision + ", " + player + ", you win the square!")
    else:
        print("Our celebrity guess picked " + c_decision + "! " + c_decision + " " + str(interactions[i]) + " " + decision + ", I'm sorry " + player + ", you lost the square!")

    return winner1

#drawing board
def tic_board(rc):
    print(rc[0][0] + "|" + rc[0][1] + "|" + rc[0][2])
    print("-----")
    print(rc[1][0] + "|" + rc[1][1] + "|" + rc[1][2])
    print("-----")
    print(rc[2][0] + "|" + rc[2][1] + "|" + rc[2][2])

def restart(choice_p):
    if choice_p == 0:
        startOver = input("Would you like to start over? Yes or No:")
        startOver = startOver.lower()
        if (startOver == "no"):
            dec = False
        else:
            dec = True
    else:
        dec = True
    return dec
   
            

#user input
def choice():
    row = int(input("Row: ")) - 1
    column = int(input("Column: ")) - 1
    return row, column

#module for spot on board
def xOrO(r, c, value):
    spot[r][c] = value
    tic_board(spot)
    print(" ")

#determining who wins
def whoWins(x, player, guest):
    if (x == 1):
        print(player + ", you win!")
        print(guest + ", you lose!")
    else:
        print(guest + ", you win!")
        print(player + ", you lose!")

#START
choice_p = 1

while restart(choice_p) != False:
    print("Hi I'm Proggie McFundy and welcome to the CompSci Squares!")
    choice_p = 0
    player = input("Player 1 enter your name: ")
    guest = input("Player 2 enter your name: ")

            
    winner = False
    x = random.randint(1,2)
        

    if x == 2:
        print(guest + " will be playing X today, and gets to pick the first spot on the board.")

    else:
        print(player + " will be playing X today, and gets to pick the first spot on the board.")

    spot = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
   

    playerTurn = 1
    counter = 0
    tic_board(spot)

        #Guest goes first, checking for winner everytime X or O is played
    while winner == False:
        if x == 2 and playerTurn == 1:
            
            print(guest + ", where would you like to play your X?")
            place = choice()
            if (rpsls(guest) == True):
                xOrO(place[0], place[1], "X")
                counter+=1
                playerTurn = 2

                if (spot[0][0] == spot[1][1] and spot[1][1] == spot[2][2] or  spot[0][2] == spot[1][1] and spot [1][1] == spot[2][0] and spot[1][1] != " "):
                    winner = True
                    whoWins(x, player, guest)

            

                elif (counter == 9 and winner != True):
                    winner == True
                    print("The game has ended in a draw!")
        
                else:
                    i = 0
                    for i in range(3):
                      if (spot[i][0] == spot[i][1]== spot[i][2] != " " or spot[0][i] == spot[1][i]== spot[2][i] != " "):                          
                          whoWins(x, player, guest)
                          i+=1
            else:
                xOrO(place[0], place[1], "O")
                if (spot[0][0] == spot[1][1] and spot[1][1] == spot[2][2] or  spot[0][2] == spot[1][1] and spot [1][1] == spot[2][0] and spot[1][1] != " "):
                    xOrO(place[0], place[1], " ")
                    

            

                elif (counter == 9 and winner != True):
                    winner == True
                    print("The game has ended in a draw!")
                    
        
                else:
                    i = 0
                    for i in range(3):
                      while (spot[i][0] == spot[i][1]== spot[i][2] != " " or spot[0][i] == spot[1][i]== spot[2][i] != " "):                          
                          xOrO(place[0], place[1], " ")
                          i+=1
                playerTurn = 2
                counter+=1
         
#Player goes first, checking for winner everytime X or O is played
        if x == 1 and playerTurn == 1:
            
            print(player + ", where would you like to play your X?")
            place = choice()
            if (rpsls(player) == True):
                xOrO(place[0], place[1], "X")
                counter+=1               
                playerTurn = 2

                if (spot[0][0] == spot[1][1] and spot[1][1] == spot[2][2] or  spot[0][2] == spot[1][1] and spot [1][1] == spot[2][0] and spot[1][1] != " "):
                    winner = True
                    whoWins(x, player, guest)

            

                elif (counter == 9 and winner != True):
                    winner == True
                    print("The game has ended in a draw!")
        
                else:
                    i = 0
                    for i in range(3):
                      if (spot[i][0] == spot[i][1]== spot[i][2] != " " or spot[0][i] == spot[1][i]== spot[2][i] != " "):                          
                          whoWins(x, player, guest)
                          i+=1
            else:
                xOrO(place[0], place[1], "O")
                if (spot[0][0] == spot[1][1] and spot[1][1] == spot[2][2] or  spot[0][2] == spot[1][1] and spot [1][1] == spot[2][0] and spot[1][1] != " "):
                    xOrO(place[0], place[1], " ")
                  
                    

            

                elif (counter == 9 and winner != True):
                    winner == True
                    print("The game has ended in a draw!")
                    
        
                else:
                    i = 0
                    for i in range(3):
                      if (spot[i][0] == spot[i][1]== spot[i][2] != " " or spot[0][i] == spot[1][i]== spot[2][i] != " "):                          
                          xOrO(place[0], place[1], " ")
                         
                      i+=1
                playerTurn = 2
                counter+=1             
                
#Guest goes first, checking for winner everytime X or O is played. Now it is Player's turn
        if x == 2 and playerTurn == 2:
           
            print(player + ", where would you like to play your O?")
            place = choice()
            if (rpsls(player) == True):
                xOrO(place[0], place[1], "O")
                counter+=1
                playerTurn = 1
                
                if (spot[0][0] == spot[1][1] and spot[1][1] == spot[2][2] or  spot[0][2] == spot[1][1] and spot [1][1] == spot[2][0] and spot[1][1] != " "):
                    winner = True
                    whoWins(x, player, guest)

            

                elif (counter == 9 and winner != True):
                    winner == True
                    print("The game has ended in a draw!")
        
                else:
                    i = 0
                    for i in range(3):
                      if (spot[i][0] == spot[i][1]== spot[i][2] != " " or spot[0][i] == spot[1][i]== spot[2][i] != " "):                          
                          whoWins(x, player, guest)
                          i+=1
            else:
                xOrO(place[0], place[1], "X")
                if (spot[0][0] == spot[1][1] and spot[1][1] == spot[2][2] or  spot[0][2] == spot[1][1] and spot [1][1] == spot[2][0] and spot[1][1] != " "):
                    xOrO(place[0], place[1], " ")
                    

            

                elif (counter == 9 and winner != True):
                    winner == True
                    print("The game has ended in a draw!")
                    
        
                else:
                    i = 0
                    for i in range(3):
                      if (spot[i][0] == spot[i][1]== spot[i][2] != " " or spot[0][i] == spot[1][i]== spot[2][i] != " "):                          
                          xOrO(place[0], place[1], " ")
                          i+=1
                
                playerTurn = 1
                counter+=1
                
#Guest goes first, checking for winner everytime X or O is played. Now it is guest's turn
        if x == 1 and playerTurn == 2:
              
            print(guest + ", where would you like to play your O?")
            place = choice()
            
            if (rpsls(guest) == True):
                xOrO(place[0], place[1], "O")
                counter+=1
                playerTurn = 1

                if (spot[0][0] == spot[1][1] and spot[1][1] == spot[2][2] or  spot[0][2] == spot[1][1] and spot [1][1] == spot[2][0] and spot[1][1] != " "):
                    winner = True
                    whoWins(x, player, guest)

            

                elif (counter == 9 and winner != True):
                    winner == True
                    print("The game has ended in a draw!")
        
                else:
                    i = 0
                    for i in range(3):
                      if (spot[i][0] == spot[i][1]== spot[i][2] != " " or spot[0][i] == spot[1][i]== spot[2][i] != " "):                          
                          whoWins(x, player, guest)
                          i+=1
            else:
                xOrO(place[0], place[1], "X")
                if (spot[0][0] == spot[1][1] and spot[1][1] == spot[2][2] or  spot[0][2] == spot[1][1] and spot [1][1] == spot[2][0] and spot[1][1] != " "):
                    xOrO(place[0], place[1], " ")
                    

            

                elif (counter == 9 and winner != True):
                    winner == True
                    print("The game has ended in a draw!")
                    
        
                else:
                    i = 0
                    for i in range(3):
                      if (spot[i][0] == spot[i][1]== spot[i][2] != " " or spot[0][i] == spot[1][i]== spot[2][i] != " "):                          
                          xOrO(place[0], place[1], " ")
                          i+=1
                playerTurn = 1
                counter+=1
               

        
            
        
            

         
