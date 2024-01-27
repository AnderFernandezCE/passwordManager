import tkinter as tk

class LoginInterface(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.homebutton = tk.Button(self, text="HOME")
        self.homebutton.pack(anchor="w")

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

        self.clearbutton = tk.Button(self, text="Clear", command=self.clear_form)
        self.clearbutton.pack(anchor="center")
        
        self.loginbutton = tk.Button(self, text="Login")
        self.loginbutton.pack(anchor="center")

        self.noaccount = tk.Label(self, text="Don't have a account? register here:")
        self.noaccount.pack( anchor="center", pady=(20,5))
        self.registerbutton = tk.Button(self, text="REGISTER")
        self.registerbutton.pack(anchor="center")
    
    def clear_form(self):
        self.emailentry.delete(0, "end")
        self.passwordentry.delete(0, "end")
        self.label_error['text'] = ""