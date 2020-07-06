# Guess the number
# Auther:

import random

play = "yes"
count = 0

#TODO: write the while condititons
while :
    # TODO: take user input for number of rounds
    numberOfrounds = int(input('How many rounds you want to play? '))


    if numberOfrounds != 0:

        # TODO: write the for loop
        for :
            print("******** Round: " + str(round+1) + " ********")
            user = int(input("Choose number between 1 and 5: "))
            computer = random.randint(1,5)
            print("Computer: ", computer)
            print("User: ", user)

            # TODO: write if condition
            if :
                # TODO: add 1 to the count
                count = count + 1

        print("You Won " + str(count) + " times!")

    # TODO: take user input for new game
    play =