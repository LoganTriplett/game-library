games = {1:['FPS','Halo 3','Bungie','Mircosoft','xbox 360','2007','8','either','$6','yes','1/15/2008','This game is great`  '],
         2:['rpg','dark souls','from software','bandi namco','xbox 360','2011','8','either','$10','yes','4/15/2015','This game is super hard but also fun'], 
         3:['FPS','Call Of Duty','activision','activision','xbox 360','2000s','6.5','either','$5','yes','1/1/2007','You shoot things']}

search_menu_running = True
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
        12) Quit Search
        """)

choice = input("how do you what to search? ")

if choice == '1':
        print("working")

elif choice == '2':
    def search_by_name():
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
            elif not found_one:
                print("*** NO MATCHES FOUND!***\n")
    search_by_name()        

elif choice == '3':
        found_one = False
        name = input("  What is the Developer of the game? ")
        for key in games.keys():
            if name == games[key][1]:
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

    
elif choice == '12':
    search_menu_running = False