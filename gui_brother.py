import pickle
import tkinter as tk
from tkinter import scrolledtext

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("file saved")
    label = ttk.Label(popup, text= "file saved", font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    Btn_ok = ttk.Button(popup, text="Okay", command = popup.destroy)
    Btn_ok.pack()
    popup.mainloop()

class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
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
        self.btn_one = tk.Button(self, text = "Hi")
        self.btn_one.grid(row = 0, column = 0)
        self.btn_two = tk.Button(self, text = "Howdy!!")
        self.btn_two.grid(row = 0, column = 1)

        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)


class AddNewMenu():  
    txt_genre = tk.Text(text = "Genre")
    txt_genre.grid(row = 1, column = 0)
    txt_title = tk.Text(text = "Title")
    txt_title.grid(row = 1, column = 1)
    txt_dev = tk.Text(text = "Dev" )
    txt_dev.grid(row = 2, column = 0)
    txt_pub = tk.Text(text = "Pub")
    txt_pub.grid(row = 2, column = 1)
    txt_year = tk.Text(text = "Year")
    txt_year.grid(row = 3, column = 0)
    chckbox_beat_it = tk.Checkbutton(text = "ffff")
    chckbox_beat_it.grid(row = 4, column = 0)
    txt_rating = tk.Text(text = "Rating")



    btn_cancel = tk.Button(text = "cancel")
    btn_cancel.grid(row = 6, column = 0)

    btn_Reset = tk.Button(text = "Reset")
    btn_Reset.grid(row = 6, column = 1)

    btn_confirm = tk.Button(text = "confirm")
    btn_confirm.grid(row = 7, column = 2)

class EditMenu():
    lbl_question = tk.Label(text = "Which Title would you like to change?", row = 0, column = 0)
    entry_1 = tk.Entry(row = 1, column = 0)

        btn_cancel = tk.Button(text = "cancel")
    btn_cancel.grid(row = 4, column = 0)

    btn_confirm = tk.Button(text = "confirm")
    btn_confirm.grid(row = 4, column = 1)

class SearchMenu():
print(" work in progress")

class RemoveMenu():
    lbl_question = tk.Label(text = "Which Title would you like to remove?", row = 0, column = 0)
    entry_1 = tk.Entry(row = 1, column = 0)

    btn_cancel = tk.Button(text = "cancel")
    btn_cancel.grid(row = 4, column = 0)

    btn_confirm = tk.Button(text = "confirm")
    btn_confirm.grid(row = 4, column = 1)

class SaveMenu():
    tk.raise = popupmsg


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
    
    
