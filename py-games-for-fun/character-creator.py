# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:52:42 2018

@author: Abhishek

Write a Character Creator program for a role-playing game. The
player should be given a pool of 30 points to spend on four
attributes: Strength, Health, Wisdom, and Dexterity. The
player should be able to spend points from the pool on any
attribute and should also be able to take points from an
attribute and put them back into the pool.

partial credits : persepolis
"""

def add_character_points():
    attribute = input("\nWhich attribute? Strength, Health, Wisdom or Dexterity?\n")

    if attribute in my_character.keys():
        amount = int(input("By how much?"))

        if (amount > my_character['points']) or (my_character['points'] <= 0):
            print ("Not enough points!")
        else:
            my_character[attribute] += amount
            my_character['points'] -= amount
    else:
        print ("\nThat attribute doesn't exist!\n")


def print_character():
    for attribute in my_character.keys():
        print (attribute, " : ", my_character[attribute])



my_character = {'name': '', 'strength': 0, 'health': 0, 'wisdom': 0, 'dexterity': 0, 'points': 20}
running = True

print ("Create a character! You have points to assign to strength, health, wisdom, and dexterity.")

my_character['name'] = input("What is your character's name? ")

while running:
    print ("\nYou have ", my_character['points'], " points left.\n")
    print ("1. Add points\n2. Remove points\n3. See current attributes\n4. Exit\n")

    choice = input("Choice:")

    if choice == "1":
        add_character_points()
    elif choice == "3":
        print_character()
    elif choice == "4":
        running = False         
    else:
        pass