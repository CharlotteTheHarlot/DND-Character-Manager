#!/usr/bin/python3

'''
This is where I will put all the things that create, save, and load characters.
'''

from Menu import confirm_input

def create_character():
    print("Welcome to the charater creator!")
    print("I am going to ask you a few questions in order to build the character.")
    while True:
        print("What is the name of your character?")
        new_character_name = input("> ")
        answer = confirm_input(new_character_name)
        if answer == 1:
            print("Great!")
            break

    while True:
        print("What race is " + new_character_name + "?")
        new_character_race = input("> ")
        answer = confirm_input(new_character_race)
        if answer == 1:
            print("Awesome!")
            break
    
    while True:
        print("What class is " + new_character_name + "?")
        new_character_class = input("> ")
        answer = confirm_input(new_character_class)
        if answer == 1:
            print("Groovy!")
            break
    
    while True:
        print("What level is " + new_character_name + "?")
        new_character_level = input("> ")
        answer = confirm_input(new_character_level)
        if answer == 1:
            print("Amazing!")
            break
    
    while True:
        print("How much EXP does " + new_character_name + " have?")
        new_character_EXP = input("> ")
        answer = confirm_input(new_character_EXP)
        if answer == 1:
            print("Sweet!")
            break

def save_character():
    print("Saving charcter.")

def load_character():
    print("Loading character.")
