import tkinter as tk
from tkinter import ttk

class AppInterface(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.logoutbutton = tk.Button(self, text="LOGOUT")
        self.logoutbutton.pack(anchor="e")
        self.welcome = tk.Label(self, text="Hello: User")
        self.welcome.pack( anchor="w")

        self.title = tk.Label(self, text= "APP", pady=20)
        self.title.config(font=("Italic", 44))
        self.title.pack( anchor="center")

        self.intro = tk.Label(self, text="Add new password:")
        self.intro.pack( anchor="center")

        
        self.newbutton = tk.Button(self, text="Add new")
        self.newbutton.pack(anchor="center")

        self.table_frame = ttk.Frame(self)
        self.table_frame.pack(pady=20)

        self.verticalscrollbar = ttk.Scrollbar(self.table_frame)
        self.verticalscrollbar.pack(side='right',fill='y')

        self.table = ttk.Treeview(self.table_frame, columns=("Username","Password", "Extra"),selectmode='browse', yscrollcommand=self.verticalscrollbar.set)
        self.table.pack(anchor="center")

        self.verticalscrollbar.config(command=self.table.yview)

        self.table.heading("#0", text='NAME')
        self.table.heading("Username", text='USERNAME')
        self.table.heading("Password", text='PASSWORD')
        self.table.heading("Extra", text='EXTRA')

        self.table.insert('',0,text="passman", values=("anderfernandez156@gmail.com","password","extra"))
        self.table.insert('',0,text="x", values=("anderfernandez156@gmail.com","password","asdf"))
        self.table.insert('',0,text="facebook", values=("anderfernandez156@gmail.com","password","extrfdfdsa"))

