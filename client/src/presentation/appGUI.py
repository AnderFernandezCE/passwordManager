import tkinter as tk

class AppInterface(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.logoutbutton = tk.Button(self, text="LOGOUT")
        self.logoutbutton.pack(anchor="e")
        self.welcome = tk.Label(self, text="Hello: User")
        self.welcome.pack( anchor="w")

        self.title = tk.Label(self, text= "Passwords", pady=20)
        self.title.config(font=("Italic", 44))
        self.title.pack( anchor="center")

        self.intro = tk.Label(self, text="Add new password:")
        self.intro.pack( anchor="center")

        
        self.newbutton = tk.Button(self, text="Add new")
        self.newbutton.pack(anchor="center")

