import tkinter as tk

class LoginInterface(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.login = tk.Label(self, text= "LOGIN", pady=20)
        self.login.config(font=("Italic", 44))
        self.login.pack( anchor="center")

        self.email = tk.Label(self, text="Email")
        self.email.pack( anchor="center")

        self.emailentry = tk.Entry(self, width=30)
        self.emailentry.pack( anchor="center")

        self.password = tk.Label(self, text="Password")
        self.password.pack( anchor="center")

        self.passwordentry = tk.Entry(self, show="*",width=30)
        self.passwordentry.pack( anchor="center")

        self.label_error = tk.Label(self, foreground='red')
        self.label_error.pack(anchor="center")

        self.loginbutton = tk.Button(self, text="Login")
        self.loginbutton.pack(anchor="center")