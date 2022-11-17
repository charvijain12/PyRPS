import random       # To generate random values
import os          # To use system specific paremeters and functions
import re           # To use Regular Expression

while (1<2):              
    print ("\n")
    print ("Rock, Paper, Scissors - Shoot!")

    userChoice = input("Choose your weapon [R]ock], [P]aper, [S]cissors, [E]xit: ")
    
    
    if (not re.match("[SsRrPpEe]", userChoice)) or (len(userChoice) != 1):
        print ("Please choose a letter:")
        print ("[R]ock, [S]cissors, [P]aper or [E]xit")
        continue

    
    print ("You chose: " + userChoice)

    
    if (userChoice == 'E' or userChoice == 'e' ):
        print('Exiting Game..')
        break

    choices = ['R', 'P', 'S']
    
    opponenetChoice = random.choice(choices)
    
    # Print Computer's Choice
    print ("I chose: " + opponenetChoice)

    
    if opponenetChoice == str.upper(userChoice):         # If both chose same value, it's a tie
        print ("Tie! ")
    
    elif opponenetChoice == 'R' and userChoice.upper() == 'S':            # Rock Vs Scissor - Rock/computer Wins
        print ("Scissors beats rock, I win! ")
        continue
    elif opponenetChoice == 'S' and userChoice.upper() == 'P':            # Scissor Vs Paper - Paper/computer Wins
        print ("Scissors beats paper! I win! ")
        continue
    elif opponenetChoice == 'P' and userChoice.upper() == 'R':            # Paper Vs Rock - Paper/computer Wins
        print ("Paper beat rock, I win! ")
        continue
    else:                                                                 # In all the other cases, user wins!
        print ("You win!")
