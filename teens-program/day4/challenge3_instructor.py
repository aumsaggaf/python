# Guess the number
# Auther: Asmaa Alsaggaf

import random

play = "yes"
count = 0

while play.lower() == "yes" or play.lower() == "y":
    numberOfrounds = int(input('How many rounds you want to play? '))
    if numberOfrounds != 0:
        for round in range(numberOfrounds):
            print("******** Round: " + str(round+1) + " ********")
            user = int(input("Choose number between 1 and 5: "))
            computer = random.randint(1,5)
            print("Computer: ", computer)
            print("User: ", user)
            if(user == computer):
                count = count + 1

        print("You Won " + str(count) + " times!")
    play = input('Do you want to play again? (yes/no) ')