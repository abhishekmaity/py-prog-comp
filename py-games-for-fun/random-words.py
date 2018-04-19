# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:13:56 2018

@author: Abhishek

A program that prints a list of words in random order.
The program should print all the words and not repeat any.
"""
import random

words=["run","walk","jog","sit","sleep"]
print("Let's see what words we have in our list\n")

for i in range(len(words)):
    randomWord = random.choice(words)
    print(randomWord)
    words.remove(randomWord)

    
    

