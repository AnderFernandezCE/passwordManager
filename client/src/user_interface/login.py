import tkinter as tk
from src.user_interface.basemodel import Page

class LoginInterface(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        login = tk.Label(self, text= "LOGIN", pady=20)
        login.config(font=("Italic", 44))
        login.pack( anchor="center")

        email = tk.Label(self, text="Email")
        email.pack( anchor="center")

        emailentry = tk.Entry(self, width=30)
        emailentry.pack( anchor="center")

        password = tk.Label(self, text="Password")
        password.pack( anchor="center")

        passwordentry = tk.Entry(self, show="*",width=30)
        passwordentry.pack( anchor="center")

        loginbutton = tk.Button(self, text="Login")
        loginbutton.pack(anchor="center")