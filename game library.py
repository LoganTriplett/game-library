#!/usr/bin/python3
# game library.py
# Logan Triplett
# 1/27/2020

import pickle

"Runs a Game library so that you can organize your games"

games = {1:['FPS','Halo 3','Bungie','Mircosoft','xbox 360','2007','8','either','$6','yes','1/15/2008','This game is great`  '],
         2:['rpg','dark souls','from software','bandi namco','xbox 360','2011','8','either','$10','yes','4/15/2015','This game is super hard but also fun'], 
         3:['FPS','Call Of Duty','activision','activision','xbox 360','2000s','6.5','either','$5','yes','1/1/2007','You shoot things']}



keep_going = True

def search_menu():
    print(""" 
        1) Search By Genre
        2) Search By title
        3) Search by Developer
        4) Search by Publisher
        5) Search by Platform
        6) Search by Year Published
        7) Search by Rating
        8) Search by Single, Multiplayer, or Both
        9) Search by Price
        10) Search by Completed
        11) Search by Date of Purchase
        
        q) Quit Search
        """)
    choice2 = input("how do you what to search? ")

    
    if choice2 == '1':
        search_by_genre()
        
    elif choice2 == '2':
        search_by_title()
          
    elif choice2 == '3':
        search_by_dev()

    elif choice2 == '4':
        search_by_pub()
        
    elif choice2 == '5':
        search_by_platform()

    elif choice2 == '6':
        search_by_pub_date()
        
    elif choice2 == '7':
        search_by_rating()

    elif choice2 == '8':
        search_by_playingtype()
        
    elif choice2 == '9':
        search_by_price()

    elif choice2 == '10':
        search_by_completion()
        
    elif choice2 == '11':
        search_by_purchasedate()

def search_by_genre():
        found_one = False
        name = input("  What is the Genre of the game? ")
        for key in games.keys():
            if name == games[key][0]:
                    found_one = True
                    print("")
                    print("Genre: ", games[key][0])
                    print("Title: ", games[key][1])
                    print("Developer: ", games[key][2])
                    print("Publisher: ", games[key][3])
                    print("Platform: ", games[key][4])
                    print("Year Published: ", games[key][5])
                    print("Rating: ", games[key][6])
                    print("Single, Multiplayer, or Both: ", games[key][7])
                    print("Price: ", games[key][8])
                    print("Completed: ", games[key][9])
                    print("Date of Purchase: ", games[key][10])
                    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            if not found_one:
                    print("*** NO MATCHES FOUND!***\n")

def search_by_title():
    found_one = False
    name = input("  What is the title of the game? ")
    for key in games.keys():
        if name == games[key][1]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("Platform: ", games[key][4])
            print("Year Published: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Single, Multiplayer, or Both: ", games[key][7])
            print("Price: ", games[key][8])
            print("Completed: ", games[key][9])
            print("Date of Purchase: ", games[key][10])
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            
        if not found_one:
            print("*** NO MATCHES FOUND!***\n")

def search_by_dev():
        found_one = False
        name = input("  What is the Developer of the game? ")
        for key in games.keys():
            if name == games[key][2]:
                    found_one = True
                    print("")
                    print("Genre: ", games[key][0])
                    print("Title: ", games[key][1])
                    print("Developer: ", games[key][2])
                    print("Publisher: ", games[key][3])
                    print("Platform: ", games[key][4])
                    print("Year Published: ", games[key][5])
                    print("Rating: ", games[key][6])
                    print("Single, Multiplayer, or Both: ", games[key][7])
                    print("Price: ", games[key][8])
                    print("Completed: ", games[key][9])
                    print("Date of Purchase: ", games[key][10])
                    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            if not found_one:
                    print("*** NO MATCHES FOUND!***\n")

def search_by_pub():
        found_one = False
        name = input("  What is the Publisher of the game? ")
        for key in games.keys():
            if name == games[key][3]:
                    found_one = True
                    print("")
                    print("Genre: ", games[key][0])
                    print("Title: ", games[key][1])
                    print("Developer: ", games[key][2])
                    print("Publisher: ", games[key][3])
                    print("Platform: ", games[key][4])
                    print("Year Published: ", games[key][5])
                    print("Rating: ", games[key][6])
                    print("Single, Multiplayer, or Both: ", games[key][7])
                    print("Price: ", games[key][8])
                    print("Completed: ", games[key][9])
                    print("Date of Purchase: ", games[key][10])
                    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            if not found_one:
                    print("*** NO MATCHES FOUND!***\n")

def search_by_platform():
        found_one = False
        name = input("  What is the Platform of the game? ")
        for key in games.keys():
            if name == games[key][4]:
                    found_one = True
                    print("")
                    print("Genre: ", games[key][0])
                    print("Title: ", games[key][1])
                    print("Developer: ", games[key][2])
                    print("Publisher: ", games[key][3])
                    print("Platform: ", games[key][4])
                    print("Year Published: ", games[key][5])
                    print("Rating: ", games[key][6])
                    print("Single, Multiplayer, or Both: ", games[key][7])
                    print("Price: ", games[key][8])
                    print("Completed: ", games[key][9])
                    print("Date of Purchase: ", games[key][10])
                    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            if not found_one:
                    print("*** NO MATCHES FOUND!***\n")

def search_by_pub_date():
        found_one = False
        name = input("  What Year was the game Pubished? ")
        for key in games.keys():
            if name == games[key][5]:
                    found_one = True
                    print("")
                    print("Genre: ", games[key][0])
                    print("Title: ", games[key][1])
                    print("Developer: ", games[key][2])
                    print("Publisher: ", games[key][3])
                    print("Platform: ", games[key][4])
                    print("Year Published: ", games[key][5])
                    print("Rating: ", games[key][6])
                    print("Single, Multiplayer, or Both: ", games[key][7])
                    print("Price: ", games[key][8])
                    print("Completed: ", games[key][9])
                    print("Date of Purchase: ", games[key][10])
                    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            if not found_one:
                    print("*** NO MATCHES FOUND!***\n")

def search_by_rating():
        found_one = False
        name = input("  What is the Rating of the game? ")
        for key in games.keys():
            if name == games[key][6]:
                    found_one = True
                    print("")
                    print("Genre: ", games[key][0])
                    print("Title: ", games[key][1])
                    print("Developer: ", games[key][2])
                    print("Publisher: ", games[key][3])
                    print("Platform: ", games[key][4])
                    print("Year Published: ", games[key][5])
                    print("Rating: ", games[key][6])
                    print("Single, Multiplayer, or Both: ", games[key][7])
                    print("Price: ", games[key][8])
                    print("Completed: ", games[key][9])
                    print("Date of Purchase: ", games[key][10])
                    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            if not found_one:
                    print("*** NO MATCHES FOUND!***\n")

def search_by_playingtype():
        found_one = False
        name = input("is the game Single, Multiplayer, or Both? ")
        for key in games.keys():
            if name == games[key][7]:
                    found_one = True
                    print("")
                    print("Genre: ", games[key][0])
                    print("Title: ", games[key][1])
                    print("Developer: ", games[key][2])
                    print("Publisher: ", games[key][3])
                    print("Platform: ", games[key][4])
                    print("Year Published: ", games[key][5])
                    print("Rating: ", games[key][6])
                    print("Single, Multiplayer, or Both: ", games[key][7])
                    print("Price: ", games[key][8])
                    print("Completed: ", games[key][9])
                    print("Date of Purchase: ", games[key][10])
                    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            if not found_one:
                    print("*** NO MATCHES FOUND!***\n")

def search_by_price():
        found_one = False
        name = input("What is the price of the game? ")
        for key in games.keys():
            if name == games[key][8]:
                    found_one = True
                    print("")
                    print("Genre: ", games[key][0])
                    print("Title: ", games[key][1])
                    print("Developer: ", games[key][2])
                    print("Publisher: ", games[key][3])
                    print("Platform: ", games[key][4])
                    print("Year Published: ", games[key][5])
                    print("Rating: ", games[key][6])
                    print("Single, Multiplayer, or Both: ", games[key][7])
                    print("Price: ", games[key][8])
                    print("Completed: ", games[key][9])
                    print("Date of Purchase: ", games[key][10])
                    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            if not found_one:
                    print("*** NO MATCHES FOUND!***\n")

def search_by_completion():
        found_one = False
        name = input("Have you completed the game? ")
        for key in games.keys():
            if name == games[key][9]:
                    found_one = True
                    print("")
                    print("Genre: ", games[key][0])
                    print("Title: ", games[key][1])
                    print("Developer: ", games[key][2])
                    print("Publisher: ", games[key][3])
                    print("Platform: ", games[key][4])
                    print("Year Published: ", games[key][5])
                    print("Rating: ", games[key][6])
                    print("Single, Multiplayer, or Both: ", games[key][7])
                    print("Price: ", games[key][8])
                    print("Completed: ", games[key][9])
                    print("Date of Purchase: ", games[key][10])
                    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            if not found_one:
                    print("*** NO MATCHES FOUND!***\n")

def search_by_purchasedate():
        found_one = False
        name = input("when was the game purchased? ")
        for key in games.keys():
            if name == games[key][10]:
                    found_one = True
                    print("")
                    print("Genre: ", games[key][0])
                    print("Title: ", games[key][1])
                    print("Developer: ", games[key][2])
                    print("Publisher: ", games[key][3])
                    print("Platform: ", games[key][4])
                    print("Year Published: ", games[key][5])
                    print("Rating: ", games[key][6])
                    print("Single, Multiplayer, or Both: ", games[key][7])
                    print("Price: ", games[key][8])
                    print("Completed: ", games[key][9])
                    print("Date of Purchase: ", games[key][10])
                    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            if not found_one:
                    print("*** NO MATCHES FOUND!***\n")


def add_new():
    entry = []


    valid = False
    while not valid:
        entry.append(input("what is the game Genre?"))
        entry.append(input("what is the game's title"))
        entry.append(input("what is the game's developer"))
        entry.append(input("what is the game's publisher"))
        entry.append(input("what is the game's platform"))
        entry.append(input("what is the game's published year"))
        entry.append(input("what is the game's rating"))
        entry.append(input("is the game Single, Multiplayer, or Both"))
        entry.append(input("what is the game's price "))
        entry.append(input("have you completed it "))
        entry.append(input("when was the date purchase "))


        anwser = input("Is this correct?")
        if anwser in ("Yes","Y","yes","y"):
            valid = True

    lengame = len(games) +1
    games[lengame] = entry
    print("entry added,")

def edit_game():
    pass

def remove_game():
    found = False
    game_removed = input("what game do you want to remove from the library? ")
    for key in games:
        if games[key][1] == game_removed:
            print(games[key][1])
            confirm = input("are you sure this is the game that you want to remove? ")
            if confirm == ("y","Y","Yes","yes"):
                games.pop(key)
                print(game_removed, "has been removed")
                break
            else:
                print("Removal unsuccessful")
    if not found:
        print("That game is not in the library.")


def print_all_games():

    key_list = games.keys()

    for key in key_list:
        print()
        print("Genre: ", games[key][0])
        print("Title: ", games[key][1])
        print("Developer: ", games[key][2])
        print("Publisher: ", games[key][3])
        print("Platform: ", games[key][4])
        print("Year Published: ", games[key][5])
        print("Rating: ", games[key][6])
        print("Single, Multiplayer, or Both: ", games[key][7])
        print("Price: ", games[key][8])
        print("Completed: ", games[key][9])
        print("Date of Purchase: ", games[key][10])
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")


while keep_going:
    print("""
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                 Welcome to Game Library
    

                                        
    MAIN MENU
    1) Add Game
    2) Edit Game
    3) Print All Games
    4) Search by title
    5) Remove a game
    6) Save Database
    
    Q) Quit
    
    """)

    choice = input("What would you like to do?\n ")
   
    
    if choice == "1":
        add_new()

    elif choice == "2":
        edit_game()

    elif choice == "3":
        print_all_games()

    elif choice == "4":
        search_menu()

    
        
    
    elif choice == "5":
        remove_game()

    elif choice == "6":
        #saving_list()
        pickle_file = open("./saves/gamelib.pickle", "wb")
        pickle.dump(games, pickle_file)
        pickle_file.close()

        pickle_file = open("./saves/gamelib.pickle", "rb")
        games = pickle.load(pickle_file)

        print("SAVING...\n")
        print(" ")
        print("SAVING COMPLETE\n")

    elif choice == "Q" or choice == "q":
        quit()
        keep_going = False

    else:
        print("*** NOT A VALID CHOICE ***\n")

