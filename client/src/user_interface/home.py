import tkinter as tk
from src.user_interface.basemodel import Page

class HomeInterface(Page):
    def __init__(self, *args, **kwargs):
        # delete keyword before initializing the frame as tk.frame has no go_login function
        self.gologin = kwargs.pop('go_login', None)
        self.goregister = kwargs.pop('go_register', None)
        Page.__init__(self, *args, **kwargs)

        title = tk.Label(self, text= "PASSMAN", pady=20)
        title.config(font=("Italic", 44))
        title.pack( anchor="center")

        intro = tk.Label(self, text="Welcome to Passman, your favourite password manager!")
        intro.pack( anchor="center")

        
        loginbutton = tk.Button(self, text="Login", command=self.gologin)
        loginbutton.pack(side="left")
        registerbutton = tk.Button(self, text="Register", command=self.goregister)
        registerbutton.pack(side="right")