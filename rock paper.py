##Selam Van Voorhis
##Comp Science Lab_07
##2/15/19
import random
play= input("Do you want to play with the computer? ")
if play== ('yes'):
    choice= (input('rock paper scissor lizard spock' ))
    computer=(random.randint(1,5))
    if computer==1:
        computer='rock'
    elif computer==2:
        compter='scissors'
    elif computer==3:
        computer='paper'
    elif computer==4:
        computer='spock'
    else:
        computer='lizard'

    if (choice == 'rock' and computer == 'scissors'):
        print ("you win.")

    elif (choice == 'rock' and computer == 'rock'):
        print ("Tie")

    elif (choice == 'scissors' and computer == 'paper'):
        print ("you win.")

    elif (choice == 'scissors' and computer == 'scissors'):
        print ("Tie")
        
    elif (choice == 'spock' and computer == 'spock'):
        print ("Tie")
        
    elif (choice == 'paper' and computer == 'paper'):
        print ("Tie")
        
    elif (choice == 'lizard' and computer == 'lizard'):
        print ("Tie")
        
    elif (choice == 'paper' and computer == 'scissors'):
        print ("computer wins.")

    elif (choice == 'rock'and computer == 'paper'):
        print ("computer wins.")

    elif (choice == 'paper' and computer == 'rock'):
        print ("computer wins.")

    elif (choice == 'scissors' and computer == 'rock'):
        print ("computer wins.")

    elif (choice == 'rock' and computer == 'lizard'):
        print ("you win.")
        
    elif (choice == 'lizard' and computer == 'rock'):
        print ("computer wins.")
        
    elif (choice == 'spock' and computer == 'scissors'):
        print ("you win.")
        
    elif (choice == 'scissors' and computer == 'spock'):
        print ("computer wins.")
        
    elif (choice == 'scissors' and computer == 'lizard'):
        print ("computer wins.")
        
    elif (choice == 'lizard' and computer == 'scissors'):
        print ("you win.")
        
    elif (choice == 'lizard' and computer == 'paper'):
        print ("you win.")
        
    elif (choice == 'paper' and computer == 'lizard'):
        print ("computer wins.")

    elif (choice == 'paper' and computer == 'spock'):
        print ("you win.")
        
    elif (choice == 'spock' and computer == 'paper'):
        print ("computer wins.")

    elif (choice == 'spock' and computer == 'rock'):
        print ("you win.")
        
    elif (choice == 'rock' and computer == 'spock'):
        print ("computer wins.")
        
        
    else:
        print ("This is not a valid object selection.")



else:

#Player vs. player
    
    player1= (input('rock paper scissor lizard spock' ))
    player2=(input('rock paper scissor lizard spock' ))

    if (player1 == 'rock' and player2 == 'scissors'):
        print ("you win.")

    elif (player1 == 'rock' and player2 == 'rock'):
        print ("Tie")

    elif (player1 == 'scissors' and player2 == 'paper'):
        print ("player1 wins")

    elif (player1 == 'scissors' and player2 == 'scissors'):
        print ("Tie")
        
    elif (player1 == 'spock' and player2 == 'spock'):
        print ("Tie")
        
    elif (player1 == 'paper' and player2 == 'paper'):
        print ("Tie")
        
    elif (player1 == 'lizard' and player2 == 'lizard'):
        print ("Tie")
        
    elif (player1 == 'paper' and player2 == 'scissors'):
        print ('player2 wins')

    elif (player1 == 'rock'and player2 == 'paper'):
        print ('player2 wins')

    elif (player1 == 'paper' and player2 == 'rock'):
        print ('player2 wins')

    elif (player1 == 'scissors' and player2 == 'rock'):
        print ('player2 wins')

    elif (player1 == 'rock' and player2 == 'lizard'):
        print ("player1 wins")
        
    elif (player1 == 'lizard' and player2 == 'rock'):
        print ('player2 wins')
        
    elif (player1 == 'spock' and player2 == 'scissors'):
        print ("player1 wins")
        
    elif (player1 == 'scissors' and player2 == 'spock'):
        print ('player2 wins')
        
    elif (player1 == 'scissors' and player2 == 'lizard'):
        print ('player2 wins')
        
    elif (player1 == 'lizard' and player2 == 'scissors'):
        print ("player1 wins")
        
    elif (player1 == 'lizard' and player2 == 'paper'):
        print ("player1 wins")
        
    elif (player1 == 'paper' and player2 == 'lizard'):
        print ('player2 wins')

    elif (player1 == 'paper' and player2 == 'spock'):
        print ("player1 wins")
        
    elif (player1 == 'spock' and player2 == 'paper'):
        print ('player2 wins')

    elif (player1 == 'spock' and player2 == 'rock'):
        print ("player1 wins")
        
    elif (player1 == 'rock' and player2 == 'spock'):
        print ('player2 wins')
        
    else:
        print ("This is not a valid object selection.")
