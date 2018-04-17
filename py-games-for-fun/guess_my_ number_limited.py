# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 11:09:06 2018

@author: Abhishek

Modify the Guess My Number game so that the player has a
limited number of guesses. If the player fails to guess in time,
the program should display an appropriately chastising message
"""
# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != the_number:
    # Let's put a limit as per question
    if tries>=5:
        break
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
            
    guess = int(input("Take a guess: "))
    tries += 1

if guess != the_number:
    print("You you finished all your chances. Better luck next time !")
else:
    print("You guessed it!  The number was", the_number)
    print("And it only took you", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
