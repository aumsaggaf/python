# Rolling the dice
# Auther:

import random
import time

def printDice(num):
    time.sleep(2)
    print("*****")
    print("* " + str(num) + " *")
    print("*****")
    print()

min = 1
max = 6

roll = "yes"

#TODO: write the while condititons
while :
    #TODO: take user input for number of rolls
    numberOfdices = int(input('How many dices you want to roll? '))
    print("Rolling the dices ...")

    #TODO: write the for loop
    for :
        printDice(random.randint(min,max))
    #TODO: take user input for new rolling
    roll =