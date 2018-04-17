# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 09:43:46 2018

@author: Abhishek

Fortune Cookie
--------------
A fortune cookie is a crisp and sugary cookie usually made from flour, sugar, 
vanilla, and sesame seed oil with a piece of paper inside, a "fortune", on which 
is an aphorism, or a vague prophecy.
"""

#Program that simulates a fortune cookie. The program should display one of five 
#unique fortunes, at random, each time it’s run

import random

print("Let's play Fortune Cookie !")
input("Please enter to start")
print("\nYour message")
print("~~~~~~~~~~~~~~")

cookie=random.randint(1,5)

if cookie==1:
    print("Someone is looking up to you.\nDon't let the person down.\n")
elif cookie==2:
    print("Run.")
elif cookie==3:
    print("No snowflakes in an avalanche ever feels responsible.")
elif cookie==4:
    print("About time I got out of that cookie.")
else:
    print("If you eat something and nobody sees \nYou eat it, it has no calories.")




