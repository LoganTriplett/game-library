import pickle
import tkinter as tk
from tkinter import scrolledtext

class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        lbl_title = tk.Label(text = "Game Library",
                             font = ("Arial", "20"))
        lbl_title.grid(row = 0, column = 0, sticky = "news")
        btn_add = tk.Button(text = "Add", command = addscreen)
        btn_add.grid(row = 1, column = 0)
        btn_edit = tk.Button(text = "Edit")
        btn_edit.grid(row = 2, column = 0)
        btn_search = tk.Button(text = "Search")
        btn_search.grid(row = 3, column = 0)
        btn_remove = tk.Button(text = "Remove")
        btn_remove.grid(row = 4, column = 0)
        btn_save = tk.Button(text = "Save")
        btn_save.grid(row = 5, column = 0)
    

class addscreen():
    def __init__(self):
        lbl_title = tk.Label(text = "Game Library",
                             font = ("Arial", "20"))
        lbl_title.grid(row = 0, column = 0, sticky = "news")
        btn_add = tk.Button(text = "Add")
        btn_add.grid(row = 1, column = 0)
        btn_edit = tk.Button(text = "Edit")
        btn_edit.grid(row = 2, column = 0)
        btn_search = tk.Button(text = "Search")
        btn_search.grid(row = 3, column = 0)
        btn_remove = tk.Button(text = "Remove")
        btn_remove.grid(row = 4, column = 0)
        btn_save = tk.Button(text = "Save")
        btn_save.grid(row = 5, column = 0)


if __name__ == "__main__":
    pickle_file = open("datafile.pickle", "rb")
    games = pickle.load(pickle_file)
    pickle_file.close()
    
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Game Library")
    main_menu = MainMenu()
    main_menu.grid(row = 0, column = 0, sticky = "news")
    root.mainloop()
    
    
