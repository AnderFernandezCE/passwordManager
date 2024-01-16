import tkinter as tk
from src.user_interface.basemodel import Page

class RegisterInterface(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        register = tk.Label(self, text= "REGISTER")
        register.config(font=("Italic", 44))
        register.pack( anchor="center")
        
        username = tk.Label(self, text="Username")
        username.pack( anchor="center")

        userentry = tk.Entry(self, width=30)
        userentry.pack( anchor="center")

        email = tk.Label(self, text="Email")
        email.pack( anchor="center")

        emailentry = tk.Entry(self, width=30)
        emailentry.pack( anchor="center")

        password = tk.Label(self, text="Password")
        password.pack( anchor="center")

        passwordentry = tk.Entry(self, show="*",width=30)
        passwordentry.pack( anchor="center")

        confirmpassword = tk.Label(self, text="Confirm Password")
        confirmpassword.pack( anchor="center")

        confirmpasswordentry = tk.Entry(self, show="*",width=30)
        confirmpasswordentry.pack( anchor="center")

        registerbutton = tk.Button(self, text="Register")
        registerbutton.pack(anchor="center")


