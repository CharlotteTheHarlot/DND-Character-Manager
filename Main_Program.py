'''
This is a Dungeon's and Dragon's character manager created by none other than Charlotte!
With this manager you will be able to:
Create, save, and load a character.
Keep track of stats like Con, Str, Wis, Int, Chr, and Dex.
Keep track of inventory.
Track useful things like current/max HP, Armor Class, Speed.
Have a built in dice roll function.
Have a built in currency function. (player wallet, purchases, sales, unit converter)
Track quests, allies, enimies, and guilds.
And as I think of more I will add it.
'''

from Startup_Protocall import startup_protocall
from Menu import menu, cap_word
from Character_Things import create_character, save_character, load_character

startup_protocall()
while True:
    print("--------Main Menu--------")
    print("Load Existing Character: ")
    print("Create a New Character: ")
    print("Quit the Program: ")
    user_command = menu(cap_word(input("What would you like to do? > ")))
    if user_command == 3:#This means load character.
        print("Ok! Starting up character creator program!")
        create_character()
    elif user_command == 4:#This means create character.
        print("Ok! Starting up character load program!")
        load_character()
    elif user_command == 5:
        print("Ok! Starting shutdown protocall!")
        shutdown_protocall()
        break
    else:
        print("I'm sorry. I didn't understand what you just said. Please try again.")