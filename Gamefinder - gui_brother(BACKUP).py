#!/usr/bin/python3
#Logan Triplett

#connor's code
import pickle
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

#classes
class Screen(tk.Frame):
    current =0
    def __init__(self):
        tk.Frame.__init__(self)
            
    def switch_frame():
        screens[Screen.current].tkraise()
                                       
class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)

        self.lbl_title = tk.Label(self,text="Game Library",font=("Arial","25"))
        self.lbl_title.grid(row=0,column=0,sticky="news")
        
        self.btn_add=tk.Button(self,text="Add",bg="red",font=("Arial","15"), command= self.go_add)
        self.btn_add.grid(row=1,column=0)
        
        
        
        self.btn_edit=tk.Button(self,text="Edit",bg="blue",font=("Arial","15"), command= self.go_Edit_Select)
        self.btn_edit.grid(row=2,column=0)
        
        self.btn_search=tk.Button(self,text="Search", bg="red",
                                font=("Arial","15"), command= self.go_search)
        self.btn_search.grid(row=3,column=0)
        
        self.btn_remove=tk.Button(self,text="Remove",bg="blue",font=("Arial","15"), command= self.go_remove)
        self.btn_remove.grid(row=4,column=0)
        
        self.btn_save=tk.Button(self,text="Save",bg="red",font=("Arial","15"), command= self.go_save)
        self.btn_save.grid(row=5,column=0)
            
    def go_add(self):
        Screen.current = 2
        screens[Screen.current].add_Genre.delete(0, "end")
        screens[Screen.current].add_title.delete(0, "end")
        screens[Screen.current].add_Dev.delete(0, "end")
        screens[Screen.current].add_Pub.delete(0, "end")
        screens[Screen.current].add_system.delete(0, "end")
        screens[Screen.current].add_release.delete(0, "end")
        screens[Screen.current].add_rating.delete(0, "end")
        screens[Screen.current].add_coop.delete(0, "end")
        screens[Screen.current].add_price.delete(0, "end")
        screens[Screen.current].add_beaten.delete(0, "end")
        screens[Screen.current].add_pur_date.delete(0, "end")
        
        Screen.switch_frame()

            
    def go_search(self):
        Screen.current=1
        Screen.switch_frame() 
            
    def go_Edit_Select(self):
        popup=tk.Tk()
        popup.title("Edit Select")
        frm_edit=Edit_Select(popup)
        frm_edit.grid(row=0,column=0)
        #Screen.current=3
        #screens[Screen.current].grid()
        #Screen.switch_frame() 
            
            
    def go_remove(self):
        Screen.current=4
        Screen.switch_frame() 
            
    def go_save(self):
        Screen.current=5
        Screen.switch_frame()                 
        
        #self.grid_columnconfigure(0,weight=1)
        #self.grid_columnconfigure(1,weight=1)
        #self.grid_columnconfigure(2,weight=1)
        #self.grid_columnconfigure(3,weight=1)
    #def raise_search(self):
                #search.tkraise(self)
                        
class Search(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.options=["one","two"]
        self.tkvar=tk.StringVar(self)
        self.tkvar.set(self.options[0])

        self.lbl_title = tk.Label(self, text="Search",font=("Arial","25"))
        self.lbl_title.grid(row=0,column=0,sticky="news") 
        
        self.search_by = tk.Label(self,text="Search By:", font=("arial","18"))
        self.search_by.grid(row=1,column=0,sticky="news")
        
        self.search_by2 = tk.OptionMenu(self, self.tkvar,*self.options)                
        self.search_by2.grid(row = 1, column = 1, sticky='news')    
                        
                
        self.search_for = tk.Label(self,text="Search For:", font=("arial","18"))
        self.search_for.grid(row=2,column=0,sticky="news") 
        
        self.ent_search = tk.Entry(self )
        self.ent_search.grid(row = 2, column = 1)
        background = self.ent_search.cget("bg")
        
        self.filters = tk.Label(self,text="Print Filters:", font=("arial","18"))
        self.filters.grid(row=1,column=2,sticky="news")
        
        self.chk1 = tk.Checkbutton( self,text='Title')
        self.chk1.grid(row=1,column=4)
        self.chk2 = tk.Checkbutton( self,text='Genre')
        self.chk2.grid(row=2,column=4)
        self.chk3 = tk.Checkbutton( self,text='Developer')
        self.chk3.grid(row=3,column=4)
        self.chk4 = tk.Checkbutton( self,text='Publisher')
        self.chk4.grid(row=4,column=4)  
        self.chk5 = tk.Checkbutton( self,text='System')
        self.chk5.grid(row=1,column=5)
        self.chk6 = tk.Checkbutton( self,text='Release')
        self.chk6.grid(row=2,column=5)  
        self.chk7 = tk.Checkbutton( self,text='Rating')
        self.chk7.grid(row=3,column=5)
        self.chk8 = tk.Checkbutton( self,text='Co-op')
        self.chk8.grid(row=4,column=5)   
        self.chk9 = tk.Checkbutton( self,text='Price')
        self.chk9.grid(row=1,column=6)
        self.chk10 = tk.Checkbutton( self,text='Beaten')
        self.chk10.grid(row=2,column=6)  
        self.chk11 = tk.Checkbutton( self,text='Purchase')
        self.chk11.grid(row=3,column=6)
                
        
                        
        
        self.edit_space = ScrolledText(self,
        wrap   = 'word',  # wrap text at full words only
        width  = 40,      # characters
        height = 10,      # text lines
        #bg='blue'        # background color of edit area
        )        

        self.edit_space.grid(row=5, column=0)
        mytext = '''\
        
        TEST TEXT
        '''
        self.edit_space.insert('insert', mytext)
        
        self.btn_cancel=tk.Button(self,text="Cancel",font=("Arial","15"),command= self.go_home)
        self.btn_cancel.grid(row=6,column=0)
        
        self.btn_clear=tk.Button(self,text="Clear",font=("Arial","15"))
        self.btn_clear.grid(row=6,column=1)
        
        self.btn_submit=tk.Button(self,text="Submit",font=("Arial","15"))
        self.btn_submit.grid(row=6,column=3) 
        
        
                        
        
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)                 
        self.grid_columnconfigure(3,weight=1)
            
    def go_home(self):
        Screen.current=0
        Screen.switch_frame()    
    
class Add(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.options=["one","two"]
        self.tkvar=tk.StringVar(self)
        self.tkvar.set(self.options[0])
        

        self.lbl_title = tk.Label(self,text="Add Game",font=("Arial","25"))
        self.lbl_title.grid(row=0,column=0,sticky="news", columnspan=3)
        
        self.Genre = tk.Label(self,text="Genre:", font=("arial","18"))
        self.Genre.grid(row=1,column=0,sticky="news")
        
        self.add_Genre = tk.Entry(self)
        self.add_Genre.grid(row = 1, column = 1)
        background = self.add_Genre.cget("bg")                  
        
        self.Title = tk.Label(self,text="Title:", font=("arial","18"))
        self.Title.grid(row=1,column=2,sticky="news") 
        
        self.add_title = tk.Entry(self)
        self.add_title.grid(row = 1, column =3)
        background = self.add_title.cget("bg")        
        
        self.dev = tk.Label(self,text="Dev:", font=("arial","18"))
        self.dev.grid(row=2,column=0,sticky="news")
        
        self.add_Dev = tk.Entry(self)
        self.add_Dev.grid(row = 2, column = 1)
        background = self.add_Dev.cget("bg")        
        
        self.Pub = tk.Label(self,text="Pub:", font=("arial","18"))
        self.Pub.grid(row=2,column=2,sticky="news")
        
        self.add_Pub = tk.Entry(self)
        self.add_Pub.grid(row = 2, column = 3)
        background = self.add_Pub.cget("bg")        
    
        self.system = tk.Label(self,text="System:", font=("arial","18"))
        self.system.grid(row=3,column=0,sticky="news")
        
        self.add_system = tk.Entry(self)
        self.add_system.grid(row = 3, column = 1)
        background = self.add_system.cget("bg") 
        
        self.release = tk.Label(self,text="Release Date:", font=("arial","18"))
        self.release.grid(row=3,column=2,sticky="news")
        
        self.add_release = tk.Entry(self)
        self.add_release.grid(row = 3, column = 3)
        background = self.add_release.cget("bg")
        
        self.rating = tk.Label(self,text="Rating:", font=("arial","18"))
        self.rating.grid(row=4,column=0,sticky="news")
        
        self.add_rating = tk.Entry(self)               
        self.add_rating.grid(row = 4, column = 1, sticky='news') 
        background = self.add_rating.cget("bg")                   
        
        self.coop = tk.Label(self,text="Multiplayer or Single:", font=("arial","18"))
        self.coop.grid(row=4,column=2,sticky="news")
        
        self.add_coop = tk.Entry(self)
        self.add_coop.grid(row = 4, column = 3)
        background = self.add_coop.cget("bg")  
        
        self.price = tk.Label(self,text="Price:", font=("arial","18"))
        self.price.grid(row=5,column=0,sticky="news")
        
        self.add_price = tk.Entry(self)
        self.add_price.grid(row = 5, column = 1)
        background = self.add_price.cget("bg")  
        
        self.beaten = tk.Label(self,text="Beaten Campaign:", font=("arial","18"))
        self.beaten.grid(row=5,column=2,sticky="news")
        
        self.add_beaten = tk.Entry(self)
        self.add_beaten.grid(row = 5, column = 3)
        background = self.add_beaten.cget("bg")  
        
        self.pur_date = tk.Label(self,text="Purchase date:", font=("arial","18"))
        self.pur_date.grid(row=6,column=0,sticky="news")
        
        self.add_pur_date = tk.Entry(self)
        self.add_pur_date.grid(row = 6, column = 1)
        background = self.add_pur_date.cget("bg")                  
        
        self.Notes = tk.Label(self,text="Notes:", font=("arial","18"))
        self.Notes.grid(row=7,column=2,sticky="news")
                        
        
        self.edit_space = ScrolledText(self,
            wrap   = 'word',  # wrap text at full words only
            width  = 40,      # characters
            height = 10,      # text lines
            #bg='blue'        # background color of edit area
        )        
    
        self.edit_space.grid(row=8, column=2)
    
        
        self.btn_cancel=tk.Button(self,text="Cancel",font=("Arial","15"),command= self.go_home)
        self.btn_cancel.grid(row=9,column=0)
        
        self.btn_clear=tk.Button(self,text="Clear",font=("Arial","15"))
        self.btn_clear.grid(row=9,column=1)
        
        self.btn_submit=tk.Button(self,text="Submit",font=("Arial","15"),command = self.add_submit)
        self.btn_submit.grid(row=9,column=2) 
        
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1) 
        self.grid_columnconfigure(3,weight=1) 


    def go_home(self):
        Screen.current=0
        Screen.switch_frame()  
        

    def add_submit(self):
        entry = []
        entry.append(self.add_Genre.get())
        entry.append(self.add_title.get())
        entry.append(self.add_Dev.get())
        entry.append(self.add_Pub.get())
        entry.append(self.add_system.get())
        entry.append(self.add_release.get())
        entry.append(self.add_rating.get())
        entry.append(self.add_coop.get())
        entry.append(self.add_price.get())
        entry.append(self.add_beaten.get())
        entry.append(self.add_pur_date.get())

        games[len(games)+1] = entry

        Screen.current = 0
        Screen.switch_frame()

class Edit_Select(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self,master =  parent)
        self.parent=parent
        self.options=["Select a game"]
        
        for key in games.keys():
                self.options.append(games[key][1])
        self.tkvar=tk.StringVar(self)
        self.tkvar.set(self.options[0])
        
        
        self.Title = tk.Label(self,text="Which Title to edit:", font=("arial","18"))
        self.Title.grid(row=0,column=0,sticky="news")
        
        self.name = tk.OptionMenu(self, self.tkvar,*self.options)                
        self.name.grid(row = 1, column = 0, sticky='news') 
                        
        
        self.btn_cancel=tk.Button(self,text="Cancel",font=("Arial","15"),command= self.cancel)
        self.btn_cancel.grid(row=6,column=0)
        
        self.btn_Go=tk.Button(self,text="Ok",font=("Arial","15"),command= self.go_edit)
        self.btn_Go.grid(row=6,column=1) 
        
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)                
    
    def cancel(self):
        self.parent.destroy()
            
    def go_edit(self):
        if self.tkvar.get()==self.options[0]:
                pass
        else:
                Screen.current=3
                if self.tkvar.get == self.options:
                        pass
                else:
                        
                        for i in range(len(self.options)):
                                if self.tkvar.get()==self.options[i]:
                                        
                                        screens[3].edit_key=i
                                        screens[3].edit_update()
                                        break                        
                Screen.switch_frame()
                self.parent.destroy()
    
    def confirm_edit(self):
        entry = []
        entry.append
                            
class Edit(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.edit_key = 0
        self.options=["one","two"]
        self.tkvar=tk.StringVar(self)
        self.tkvar.set(self.options[0])
        
                        

        self.lbl_title = tk.Label(self,text="Edit Title",font=("Arial","25"))
        self.lbl_title.grid(row=0,column=0,sticky="news", columnspan=3)
        
        self.Title = tk.Label(self,text="Title:", font=("arial","18"))
        self.Title.grid(row=1,column=2,sticky="news") 
        
        self.edit_title = tk.Entry(self)
        self.edit_title.grid(row = 1, column =3)
        background = self.edit_title.cget("bg")        
        
        self.Genre = tk.Label(self,text="Genre:", font=("arial","18"))
        self.Genre.grid(row=1,column=0,sticky="news")
        
        self.edit_Genre = tk.Entry(self)
        self.edit_Genre.grid(row = 1, column = 1)
        background = self.edit_Genre.cget("bg")        
        
        self.dev = tk.Label(self,text="Dev:", font=("arial","18"))
        self.dev.grid(row=2,column=0,sticky="news")
        
        self.edit_Dev = tk.Entry(self)
        self.edit_Dev.grid(row = 2, column = 1)
        background = self.edit_Dev.cget("bg")        
        
        self.Pub = tk.Label(self,text="Pub:", font=("arial","18"))
        self.Pub.grid(row=2,column=2,sticky="news")
        
        self.edit_Pub = tk.Entry(self)
        self.edit_Pub.grid(row = 2, column = 3)
        background = self.edit_Pub.cget("bg")        

        self.Year = tk.Label(self,text="Year:", font=("arial","18"))
        self.Year.grid(row=3,column=0,sticky="news")
        
        self.edit_year = tk.Entry(self)
        self.edit_year.grid(row = 3, column = 1)
        background = self.edit_year.cget("bg") 
        
        self.Notes = tk.Label(self,text="Notes:", font=("arial","18"))
        self.Notes.grid(row=4,column=0,sticky="news")
        

        
        self.rating = tk.Label(self,text="Rating:", font=("arial","18"))
        self.rating.grid(row=4,column=2,sticky="news")
        
        self.Rating = tk.OptionMenu(self, self.tkvar,*self.options)                
        self.Rating.grid(row = 4, column = 3, sticky='news')
        #self.Rating = tk.Entry(self)               
        #self.Rating.grid(row = 4, column = 3, sticky='news') 
        background = self.Rating.cget("bg")                
        
        self.edit_space = ScrolledText(self,
        wrap   = 'word',  # wrap text at full words only
        width  = 40,      # characters
        height = 10,      # text lines
       # bg='blue'        # background color of edit area
        )        

        self.edit_space.grid(row=5, column=0)
        mytext = '''

        TEST TEXT 
        '''
        self.edit_space.insert('insert', mytext)
        
        self.btn_cancel=tk.Button(self,text="Cancel",font=("Arial","15"),command= self.go_home)
        self.btn_cancel.grid(row=6,column=0)
        
        self.btn_clear=tk.Button(self,text="Clear",font=("Arial","15"))
        self.btn_clear.grid(row=6,column=1)
        
        self.btn_submit=tk.Button(self,text="Submit",font=("Arial","15"))
        self.btn_submit.grid(row=6,column=3) 
        
        
        
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1) 
        self.grid_columnconfigure(3,weight=1) 
                
                
                
    def edit_update(self):
        print("updating")
        entry = games[self.edit_key]
        self.edit_Genre.delete(0,"end")
        self.edit_Genre.insert(0,entry[0])
        
        self.edit_Dev.delete(0,"end")
        self.edit_Dev.insert(0,entry[2])
        
        self.edit_Pub.delete(0,"end")
        self.edit_Pub.insert(0,entry[3])
        
        self.edit_title.delete(0,"end")
        self.edit_title.insert(0,entry[1])
        
        self.edit_year.delete(0,"end")
        self.edit_year.insert(0,entry[10])
            
    def go_home(self):
        Screen.current=0
        Screen.switch_frame()

class Remove(tk.Frame):
        def __init__(self):
                tk.Frame.__init__(self)

                self.options=["one","two"]
                self.tkvar=tk.StringVar(self)
                self.tkvar.set(self.options[0])                

                self.Title10 = tk.Label(self,text="Which Title to", font=("arial","18"))
                self.Title10.grid(row=0,column=0,sticky="news")

                self.Title11 = tk.Label(self,text="remove:", font=("arial","18"))
                self.Title11.grid(row=1,column=0,sticky="news") 

                self.game_remove = tk.OptionMenu(self, self.tkvar,*self.options)                
                self.game_remove.grid(row = 2, column = 0, sticky='news')
                background = self.game_remove.cget("bg")                

                self.btn_cancel=tk.Button(self,text="Cancel",font=("Arial","15"),command= self.go_home)
                self.btn_cancel.grid(row=3,column=0)

                self.btn_clear=tk.Button(self,text="Remove",font=("Arial","15"))
                self.btn_clear.grid(row=3,column=1)                

                self.grid_columnconfigure(0,weight=1)
                self.grid_columnconfigure(1,weight=1)

        def go_home(self):
                Screen.current=0
                Screen.switch_frame() 
                             
class Verify(tk.Frame):
    def __init__(self, remove): 
        tk.Frame.__init__(self, master = remove)
        
        self.Title = tk.Label(self,text="These games are ", font=("arial","18"))
        self.Title.grid(row=0,column=0,sticky="news")
        
        self.Title = tk.Label(self,text="Marked for removal:", font=("arial","18"))
        self.Title.grid(row=1,column=0,sticky="news")   
        
        self.edit_space = ScrolledText(self,
        wrap   = 'word',  # wrap text at full words only
        width  = 40,      # characters
        height = 10,      # text lines
       # bg='blue'        # background color of edit area
        )        

        self.edit_space.grid(row=2, column=0)
        mytext = '''
        this is a test text

        '''

        self.edit_space.insert('insert', mytext)                
        
        self.btn_cancel=tk.Button(self,text="Cancel",font=("Arial","15"),command= self.go_home)
        self.btn_cancel.grid(row=6,column=0)
        
        self.btn_clear=tk.Button(self,text="Verify",font=("Arial","15"))
        self.btn_clear.grid(row=6,column=1)                
        
        self.grid_columnconfigure(0,weight=5)
        self.grid_columnconfigure(1,weight=5)
            
    def go_home(self):
        Screen.current=0
        Screen.switch_frame()                 
                
class Save(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.Title = tk.Label(self,text="File saved. ", font=("arial","18"))
        self.Title.grid(row=0,column=0,sticky="news")
        
        self.btn_cancel=tk.Button(self,text="OK",font=("Arial","15"),command= self.go_home)
        self.btn_cancel.grid(row=1,column=0)
            
    def go_home(self):
        Screen.current=0
        Screen.switch_frame()                                        
#main 

#Main Menu->screens[]
if __name__ == "__main__":
    pickle_file = open("saves/game_lib.pickle", "rb")
    games = pickle.load(pickle_file)
    pickle_file.close()
    root = tk.Tk()
    # root.geometry("1280x720")
    root.title("Game Library")
    
    root.grid_columnconfigure(0,weight=1)
    root.grid_rowconfigure(0,weight=1)
    
    
    screens=[]                
    screens.append(MainMenu())
    screens.append(Search())  
    screens.append(Add())  
    #screens.append(Edit_Select())
    screens.append(Edit()) 
    screens.append(Remove())  
    screens.append(Save())  
    
    screens[0].grid(row=0, column=0,sticky="news")
    screens[1].grid(row=0, column=0,sticky="news")
    screens[2].grid(row=0, column=0,sticky="news")
    screens[3].grid(row=0, column=0,sticky="news")
    screens[4].grid(row=0, column=0,sticky="news")
    screens[5].grid(row=0, column=0,sticky="news")
    
    Screen.current=0
    Screen.switch_frame()
    
    root.mainloop()   
        