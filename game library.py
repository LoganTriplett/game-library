#!/usr/bin/python3
# game library.py
# Logan Triplett
# 1/27/2020

import pickle

"Runs a Game library so that you can organize your games"

games = {1:['FPS','Halo 3','Bungie','Mircosoft','xbox 360','2007','8','either','$6','yes','1/15/2008','This game is great`  ']}

def print_all(sort_it):
    #print("running print_all()")
    key_list = GameKeys.keys()
    if sort_it:
        sorted_list =[]
        for key in key_list:
            sorted_list.append(key)
        sorted_list.sort()
        key_list = sorted_list

for key in key_list:
        print()
        print("Genre: ", key)
        print("Title: ", GameKeys[key][1]+", "+GameKeys[key][0])
        print("Developer: ", GameKeys[key][2])
        print("publisher: ", GameKeys[key][3])
        print("System: ", GameKeys[keys][4])
        print("Release Date: ", GameKeys[keys][5]) 
        print("Rating: ", GameKeys[keys][6])
        print("Single/multi/either: ", GameKeys[keys][7])

def lookup():
    GameKeys = input("What is the GameName ")
    for Gamekeys in GameKeys.keys():
        if name == GameKeys[key][1]:
            found_one = True
        print()
        print("Genre: ", key)
        print("Title: ", GameKeys[key][1]+", "+GameKeys[key][0])
        print("Developer: ", GameKeys[key][2])
        print("publisher: ", GameKeys[key][3])
        print("System: ", GameKeys[keys][4])
        print("Release Date: ", GameKeys[keys][5]) 
        print("Rating: ", GameKeys[keys][6])
        print("Single/multi/either: ", GameKeys[keys][7])

    
    #if GameName in GameKeys:
       # print()
      #  print("Title: ", GameName)
       # print("Developer: ", GameKeys[GameName][1]+", "+GameKeys[GameName][0])
        #print("Birth Year: ", GameKeys[GameName][2])
        #print("publisher: ", GameKeys[GameName][3])
        #print("System: ", GameKeys[keys][4])
        #print("Release Date: ", GameKeys[keys][5]) 
        #print("Rating: ", GameKeys[keys][6])
        #print("Single/multi/either: ", GameKeys[keys][7])

    else:
        print("*** GAME NOT FOUND! ***\n")


    if not found_one:
        print("*** NO MATCHES FOUND!***\n")

def add_new():
    #print("running add_new()")
    GameKeys = input("What is the SSN of the person to add? ")
    if GameKeys in people:
        print("*** THAT GAME ALREADY EXISTS IN THE LIBRARY! ***\n")
    else:
        first = input("   What is their first name? ")
        last = input("   What is their last name? ")
        year = input("   What is their birth year? ")
        people[ssn] = [first, last, year]     

def edit_record():
   GameKeys = input("What is the SSN of the person to edit? ")
    if ssn not in people:
        print("*** THAT SSN DOES NOT EXIST! ***\n")
    else:
        first = input("  What is their first name? ")
        last = input( "   What is their last name?  ")
        year = input( "   What is their birth year?")
        people[ssn] = [first, last, year]  
        
def delete_record():
    ssn = input("What is the SSN of the person to delete? ")
    if ssn not in people:
        print("*** THAT SSN DOES NOT EXIST! ***\n")
    else:
        entry = people.pop(ssn)
        print(ssn, ":", entry[0], entry[1]+", removed.")

def quit():
    #print("running quit()")
    pickle_file = open("datafile.pickle", "wb")
    pickle.dump(people, pickle_file)
    pickle_file.close()
    
def update_people(GameKeys):
    print()
        print("Genre: ", key)
        print("Title: ", GameKeys[key][1]+", "+GameKeys[key][0])
        print("Developer: ", GameKeys[key][2])
        print("publisher: ", GameKeys[key][3])
        print("System: ", GameKeys[keys][4])
        print("Release Date: ", GameKeys[keys][5]) 
        print("Rating: ", GameKeys[keys][6])
        print("Single/multi/either: ", GameKeys[keys][7])


GameKeys = {}
pickle_file = open("datafile.pickle", "rb")
GameKeys = pickle.load(pickle_file)
pickle_file.close()


keep_going = True

while keep_going:
    print("""
                                 Welcome to Game Library
    

                                        
    MAIN MENU
    1) Add/Edit Game
    2) Print All Games
    3) Search by title
    4) Remove a game
    5) Save Database
    
    Q) Quit
    
    """)

     if choice == "1":
        add_new()

    elif choice == "2":
        print_all(False)

    elif choice == "3"

    elif choice == "4"