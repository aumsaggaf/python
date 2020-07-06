# Rock, paper, scissors
# Auther: Asmaa Alsaggaf

import random

def computer_turn():
    RPS = ["rock", "paper", "scissors"]
    return RPS[random.randint(0,2)]

play = "yes"

while play.lower() == "yes" or play.lower() == "y":
    numberOfrounds = int(input('How many rounds you want to play? '))
    if numberOfrounds != 0:
        print("Rolling the dices ...")
        for round in range(numberOfrounds):
            user = input("Type rock, paper, or scissors: ")
            computer = computer_turn()
            if((user.lower() == "rock" and computer.lower == "paper") or
                (user.lower() == "rock" and computer.lower == "paper") or
                (user.lower() == "rock" and computer.lower == "paper"))
    play = input('Do you want to play again? (yes/no) ')