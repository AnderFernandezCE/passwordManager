import tkinter as tk
from src.user_interface.basemodel import Page
from src.encryption import encryptionservice     

class RegisterInterface(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        register = tk.Label(self, text= "REGISTER")
        register.config(font=("Italic", 44))
        register.pack( anchor="center")
        
        username = tk.Label(self, text="Username")
        username.pack( anchor="center")

        self.userentry = tk.Entry(self, width=30)
        self.userentry.pack( anchor="center")

        email = tk.Label(self, text="Email")
        email.pack( anchor="center")

        self.emailentry = tk.Entry(self, width=30)
        self.emailentry.pack( anchor="center")

        password = tk.Label(self, text="Password")
        password.pack( anchor="center")

        self.passwordentry = tk.Entry(self, show="*",width=30)
        self.passwordentry.pack( anchor="center")

        confirmpassword = tk.Label(self, text="Confirm Password")
        confirmpassword.pack( anchor="center")

        self.confirmpasswordentry = tk.Entry(self, show="*",width=30)
        self.confirmpasswordentry.pack( anchor="center")

        registerbutton = tk.Button(self, text="Register", command=self.register_user)
        registerbutton.pack(anchor="center")

    
    def validate_input(self):
        user = self.userentry.get()
        email = self.emailentry.get()
        password = self.passwordentry.get()
        confirmpassword = self.confirmpasswordentry.get()

        
    def register_user(self):
        email = self.emailentry.get()
        password = self.passwordentry.get()
        result = encryptionservice.obtain_hash_master_password(password, email)
        print(result)


