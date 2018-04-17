# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:07:24 2018

@author: Abhishek

Improve “Word Jumble” so that each word is paired with a hint.
The player should be able to see the hint if he or she is stuck.
Add a scoring system that rewards players who solve a jumble
without asking for the hint
"""
# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# create some hints
HINTS=("A kind of snake", "Mixing something", "Simple to perform", 
       "Hard to perform", "Antonym for question", "A kind of musical instrument")
# pick one word randomly from the sequence
word = random.choice(WORDS)
z= WORDS.index(word)
# create a variable to use later to see if the guess is correct
correct = word
score=0
# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    h=input("Do you want a hint ? Press [y] ")
    if h == "y" or "Y":
        print(HINTS[z])
        score+=-1
    guess = input("Your guess: ")
    
if guess == correct:
    print("That's it!  You guessed it!\n")
    score+=2
print("Your score is :",score)
print("SCORING: For correct answer with HINT = 1 point and without HINT = 2 points !")
print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
