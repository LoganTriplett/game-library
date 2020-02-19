#!/usr/bin/python3
#Logan Triplett


import pickle
import tkinter as tk
from tkinter import scrolledtext



class Screen(tk.Frame):
    current = 0
    def __init__(self):
        tk.Frame.__init__(self)

    def switch_frame():
        screens[Screen.current].tkraise()
       

def popupmsg():
    popup = tk.Tk()
    popup.wm_title("file saved")
    label = tk.Label(popup, text= "file saved")
    Btn_ok = tk.Button(popup, text="Okay", command = popup.destroy)
    popup.mainloop()

class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)

        self.lbl_title = tk.Label(self, text = "Game Library",
                                font = ("Arial", "20"))
        self.lbl_title.grid(row = 0, column = 0)
        self.btn_add = tk.Button(self, text = "Add", command = self.go_add)
        self.btn_add.grid(row = 1, column = 0)
        self.btn_edit = tk.Button(self, text = "Edit", command = self.go_edit)
        self.btn_edit.grid(row = 2, column = 0)
        self.btn_search = tk.Button(self, text = "Search", command = self.go_search)
        self.btn_search.grid(row = 3, column = 0)
        self.btn_remove = tk.Button(self, text = "Remove", command = self.go_remove)
        self.btn_remove.grid(row = 4, column = 0)
        self.btn_save = tk.Button(self, text = "Save", command = self.go_save)
        self.btn_save.grid(row = 5, column = 0)
        
    def go_add(self):
        Screen.current = 1
        Screen.switch_frame()

    def go_edit(self):
        Screen.current = 2
        Screen.switch_frame()
    
    def go_search(self):
        Screen.current = 3
        Screen.switch_frame()

    def go_remove(self):
        Screen.current = 4
        Screen.switch_frame()

    def go_save(self):
        Screen.current = 5
        Screen.switch_frame()


class AddNewMenu(Screen):
    def __init__(self):
        Screen.__init__(self) 
        self.ent_genre = tk.Entry(self)
        self.ent_genre.grid(row = 1, column = 0, sticky = "news")
        self.ent_title = tk.Entry(self)
        self.ent_title.grid(row = 1, column = 1, sticky = "news")
        self.ent_dev = tk.Entry(self)
        self.ent_dev.grid(row = 2, column = 0, sticky = "news")
        self.ent_pub = tk.Entry(self)
        self.ent_pub.grid(row = 2, column = 1, sticky = "news")
        self.ent_year = tk.Entry(self)
        self.ent_year.grid(row = 3, column = 0, sticky = "news")
        self.chckbox_beat_it = tk.Checkbutton(self, text = "")
        self.chckbox_beat_it.grid(row = 4, column = 0, sticky = "news")
        self.ent_rating = tk.Entry(self)



        self.btn_cancel = tk.Button(self, text = "cancel", command = self.go_back)
        self.btn_cancel.grid(row = 6, column = 0)

        self.btn_Reset = tk.Button(self, text = "Reset")
        self.btn_Reset.grid(row = 6, column = 1)

        self.btn_confirm = tk.Button(self, text = "confirm")
        self.btn_confirm.grid(row = 6, column = 2)

    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()

class EditMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_question = tk.Label(self, text = "Which Title would you like to change?")
        self.lbl_question.grid( row = 0, column = 0)
        self.entry_1 = tk.Entry(self)
        self.entry_1.grid(row = 1, column = 0)

        self.btn_cancel = tk.Button(self, text = "cancel", command = self.go_back)
        self.btn_cancel.grid(row = 4, column = 0)

        self.btn_confirm = tk.Button(self, text = "confirm")
        self.btn_confirm.grid(row = 4, column = 1)

    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()

class SearchMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_top = tk.Label(self, text = "search")
        self.lbl_top.grid(row = 0, column = 1)
        self.lbl_searchby = tk.Label(self, text = "Search By: ")
        self.lbl_searchby.grid(row = 1, column = 0)
        self.entry_searchby = tk.Entry(self, text = "")
        self.entry_searchby.grid(row = 2, column = 0)

        self.lbl_searchfor = tk.Label(self, text = "search for: ")
        self.lbl_searchfor.grid(row = 4, column = 0)
        self.entry_searchfor = tk.Entry(self, text = "")
        self.entry_searchfor.grid(row = 5, column = 0)

class RemoveMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_questionz = tk.Label(self, text = "Which Title would you like to remove?")
        self.lbl_questionz.grid(row = 0, column = 0)
        self.entry_2 = tk.Entry(self)
        self.entry_2.grid(row = 1, column = 0)

        self.btn_cancel = tk.Button(self, text = "cancel", command = self.go_back)
        self.btn_cancel.grid(row = 4, column = 0)

        self.btn_confirm = tk.Button(self, text = "confirm")
        self.btn_confirm.grid(row = 4, column = 1)

    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()


class SaveMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.tkraise = popupmsg





if __name__ == "__main__":
    pickle_file = open("saves/datafile.pickle", "rb")
    games = pickle.load(pickle_file)
    pickle_file.close()
    
    root = tk.Tk()
    #root.geometry("500x500")
    root.title("Game Library")
    root.grid_columnconfigure(0, weight =1)
    root.grid_rowconfigure(0, weight = 1)

    screens = []
    screens.append(MainMenu())
    screens.append(AddNewMenu())
    screens.append(EditMenu())
    screens.append(SearchMenu())
    screens.append(RemoveMenu())
    screens.append(SaveMenu())



    screens[0].grid(row = 0, column = 0, sticky = "news")
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")
    screens[3].grid(row = 0, column = 0, sticky = "news")    
    screens[4].grid(row = 0, column = 0, sticky = "news")


    Screen.current = 0
    Screen.switch_frame()
    
    #main_menu = MainMenu()
    #main_menu.grid(row = 0, column = 0, sticky = "news")
    root.mainloop()
    
    
