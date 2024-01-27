import tkinter as tk

class RegisterInterface(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.homebutton = tk.Button(self, text="HOME")
        self.homebutton.pack(anchor="w")

        self.register = tk.Label(self, text= "REGISTER")
        self.register.config(font=("Italic", 44))
        self.register.pack( anchor="center")
        
        self.username = tk.Label(self, text="Username")
        self.username.pack( anchor="center")

        self.userentry = tk.Entry(self, width=30)
        self.userentry.pack( anchor="center")

        self.email = tk.Label(self, text="Email")
        self.email.pack( anchor="center")

        self.emailentry = tk.Entry(self, width=30)
        self.emailentry.pack( anchor="center")

        self.password = tk.Label(self, text="Password")
        self.password.pack( anchor="center")

        self.passwordentry = tk.Entry(self, show="*",width=30)
        self.passwordentry.pack( anchor="center")

        self.confirmpassword = tk.Label(self, text="Confirm Password")
        self.confirmpassword.pack( anchor="center")

        self.confirmpasswordentry = tk.Entry(self, show="*",width=30)
        self.confirmpasswordentry.pack( anchor="center")

        self.label_error = tk.Label(self, foreground='red')
        self.label_error.pack(anchor="center")

        self.clearbutton = tk.Button(self, text="Clear", command=self.clear_form)
        self.clearbutton.pack(anchor="center")

        self.registerbutton = tk.Button(self, text="Register")
        self.registerbutton.pack(anchor="center")
        
        self.haveaccount = tk.Label(self, text="You already have an account? login here:")
        self.haveaccount.pack( anchor="center", pady=(20,5))
        self.loginbutton = tk.Button(self, text="LOGIN")
        self.loginbutton.pack(anchor="center")

    def clear_form(self):
        self.userentry.delete(0, "end")
        self.emailentry.delete(0, "end")
        self.passwordentry.delete(0, "end")
        self.confirmpasswordentry.delete(0, "end")
        self.label_error['text'] = ""