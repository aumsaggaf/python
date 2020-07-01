# Rolling the dice
# Auther: Asmaa Alsaggaf

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

while roll.lower() == "yes" or roll.lower() == "y":
    numberOfdices = int(input('How many dices you want to roll? '))
    if numberOfdices != 0:
        print("Rolling the dices ...")
        for dice in range(numberOfdices):
            printDice(random.randint(min,max))
    roll = input('Do you want to roll again? (yes/no) ')