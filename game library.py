#!/usr/bin/python3
# game library.py
# Logan Triplett
# 1/27/2020

import pickle

"Runs a Game library so that you can organize your games"

games = {1:['FPS','Halo 3','Bungie','Mircosoft','xbox 360','2007','8','either','$6','yes','1/15/2008','This game is great`  ']}



pickle_file = open("./saves/gamelib.pickle", "rb")
games = pickle.load(pickle_file)
pickle_file.close()



keep_going = True


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
    1) Add/Edit Game
    2) Print All Games
    3) Search by title
    4) Remove a game
    5) Save Database
    
    Q) Quit
    
    """)


    choice = input("What would you like to do?\n ")
    print(" ")

    if choice == "1":
        print("Work in progress")
    elif choice == "2":
       print_all_games()
    elif choice == "3":
        print("Work in progress")
    elif choice == "4":
       print("Work in progress")

    elif choice == "5":
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