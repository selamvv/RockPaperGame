##Selam Van Voorhis
##Comp Science Lab_07
##2/15/19
import random
play= input("Do you want to play with the computer? Type yes to play with the computer or no to play with another player")
if play== ('yes'):
    choice= (input('Your options are rock paper scissor lizard spock, enter a selectiom' ))
    computer=(random.randint(1,5))
    if computer==1:
        computer='rock'
        print('computer selection: rock')
    elif computer==2:
        compter='scissors'
        print('computer selection: scissors')
    elif computer==3:
        computer='paper'
         print('computer selection: paper')
    elif computer==4:
        computer='spock'
        print('computer selection: spock')
    else:
        computer='lizard'
         print('computer selection: lizard')
        

    if (choice == 'rock' and computer == 'scissors'):
        print('your selction: rock <br> computer selection: scissors')
        print ("You win!")

    elif (choice == 'rock' and computer == 'rock'):
        print('your selction: rock <br> computer selection: rock')
        print ("Tie")

    elif (choice == 'scissors' and computer == 'paper'):
        print('your selction: scissors <br> computer selection: paper')
        print ("You win!")

    elif (choice == 'scissors' and computer == 'scissors'):
        print('your selction: scissors <br> computer selection: scissors')
        print ("Tie")
        
    elif (choice == 'spock' and computer == 'spock'):
        print('your selction: spock <br> computer selection: spock')
        print ("Tie")
        
    elif (choice == 'paper' and computer == 'paper'):
        print('your selction: paper <br> computer selection: paper')
        print ("Tie")
        
    elif (choice == 'lizard' and computer == 'lizard'):
        print('your selction: lizard <br> computer selection: lizard')
        print ("Tie")
        
    elif (choice == 'paper' and computer == 'scissors'):
        print('your selction: paper <br> computer selection: scissors')
        print ("computer wins.")

    elif (choice == 'rock' and computer == 'paper'):
        print('your selction: rock <br> computer selection: paper')
        print ("computer wins.")

    elif (choice == 'paper' and computer == 'rock'):
        print('your selction: paper <br> computer selection: rock')
        print ("computer wins.")

    elif (choice == 'scissors' and computer == 'rock'):
        print('your selction: scissors <br> computer selection: rock')
        print ("computer wins.")

    elif (choice == 'rock' and computer == 'lizard'):
        print('your selction: scissors <br> computer selection: rock')
        print ("you win.")
        
    elif (choice == 'lizard' and computer == 'rock'):
        print('your selction: lizard <br> computer selection: rock')
        print ("computer wins.")
        
    elif (choice == 'spock' and computer == 'scissors'):
        print('your selction: spock <br> computer selection: scissors')
        print ("you win.")
        
    elif (choice == 'scissors' and computer == 'spock'):
        print('your selction: scissors <br> computer selection: spock')
        print ("computer wins.")
        
    elif (choice == 'scissors' and computer == 'lizard'):
        print('your selction: scissors <br> computer selection: lizard')
        print ("computer wins.")
        
    elif (choice == 'lizard' and computer == 'scissors'):
        print('your selction: lizard <br> computer selection: scissors')
        print ("you win.")
        
    elif (choice == 'lizard' and computer == 'paper'):
        print('your selction: lizard <br> computer selection: paper')
        print ("you win.")
        
    elif (choice == 'paper' and computer == 'lizard'):
        print('your selction: paper <br> computer selection: lizard')
        print ("computer wins.")

    elif (choice == 'paper' and computer == 'spock'):
        print('your selction: paper <br> computer selection: spock')
        print ("you win.")
        
    elif (choice == 'spock' and computer == 'paper'):
        print('your selction: spock <br> computer selection: paper')
        print ("computer wins.")

    elif (choice == 'spock' and computer == 'rock'):
        print('your selction: spock <br> computer selection: rock')
        print ("you win.")
        
    elif (choice == 'rock' and computer == 'spock'):
        print('your selction: rock <br> computer selection: spock')
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
