#!/usr/bin/python3

'''
This is the menu that determines what the user types and outputs a number. 
'''

def menu(user_input):
    if user_input in ['Yes', 'Y', 'Confirm']:
        return 1
    elif user_input in ['No', 'N', 'Deny']:
        return 2
    elif user_input in ['Load', 'Load character']:
        return 3
    elif user_input in ['New', 'New character', 'Create', 'Create new', 'Create new character', 'Create character']:
        return 4
    elif user_input in ['Quit', 'Exit', 'Terminate', 'Terminate program']:
        return 5
#    elif user_input in []:
#        return 6
#    elif user_input in []:
#        return 7
#    elif user_input in []:
#        return 8
#    elif user_input in []:
#        return 9
#    elif user_input in []:
#        return 10
#    elif user_input in []:
#        return 11
#    elif user_input in []:
#        return 12
#    elif user_input in []:
#        return 13
#    elif user_input in []:
#        return 14
#    elif user_input in []:
#        return 15
#    elif user_input in []:
#        return 16
#    elif user_input in []:
#        return 17
#    elif user_input in []:
#        return 18
#    elif user_input in []:
#        return 19
    else:
        return 0#This means the input was not recognized.

def cap_word(word):
    word = str(word)
    first_half = word.upper()[0]
    second_half = word.lower()[1:]
    return first_half + second_half