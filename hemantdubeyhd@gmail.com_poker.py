


    
import dice                 #importing provide file dice.py to use the function e.g., to display player's hand
import random               #to generate dice's values



#Defining function rollDie() to generate value of one die's face value,
#rangging from 1 to 6 and returning it to varible of function whuich calls rollDie()function

def rollDie():
    return random.randint(1,6) # generating one random number at a time and returning into function called rollDie()




#Defining function to generate values of player's and dealer's hand/die's values,

def dealHand(listLength):  # function receive argument as length of list so it knos how many random number to be generated
    handValues = [0, 0, 0, 0, 0] #Local list to store random generated number and to use it to return list

    listLength -=1; #setting the list index to maximum index value.

    while listLength >= 0:
        handValues[listLength] = rollDie()
        listLength -= 1
        
    return handValues 


playerHand = [0,0,0,0,0]             # List to store player's hand, 5 dice values in this programm


playerHand = dealHand(len(playerHand))
    
print("Player's hand:")
dice.display_hand(playerHand)
