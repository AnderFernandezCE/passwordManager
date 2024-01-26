import tkinter as tk

class HomeInterface(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = tk.Label(self, text= "PASSMAN", pady=20)
        self.title.config(font=("Italic", 44))
        self.title.pack( anchor="center")

        self.intro = tk.Label(self, text="Welcome to Passman, your favourite password manager!")
        self.intro.pack( anchor="center")

        
        self.loginbutton = tk.Button(self, text="Login")
        self.loginbutton.pack(side="left")
        self.registerbutton = tk.Button(self, text="Register")
        self.registerbutton.pack(side="right")