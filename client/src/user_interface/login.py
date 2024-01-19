import tkinter as tk
from src.user_interface.basemodel import Page
from src.utils import validation
from src.encryption import encryptionservice
from src.apicall import requestservice
from src.schemas import response as serverresponse

class LoginInterface(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        login = tk.Label(self, text= "LOGIN", pady=20)
        login.config(font=("Italic", 44))
        login.pack( anchor="center")

        email = tk.Label(self, text="Email")
        email.pack( anchor="center")

        self.emailentry = tk.Entry(self, width=30)
        self.emailentry.pack( anchor="center")

        password = tk.Label(self, text="Password")
        password.pack( anchor="center")

        self.passwordentry = tk.Entry(self, show="*",width=30)
        self.passwordentry.pack( anchor="center")

        self.label_error = tk.Label(self, foreground='red')
        self.label_error.pack(anchor="center")

        loginbutton = tk.Button(self, text="Login", command=self.validate_input)
        loginbutton.pack(anchor="center")

    def validate_input(self):
        email = self.emailentry.get()
        password = self.passwordentry.get()

        if not email or not password:
            self.label_error['text'] = "Fill all the fields"
        elif not validation.check_email_valid(email):
            self.label_error['text'] = "Invalid email"
        else:
            self.login_user(email,password)


    def login_user(self, email, password):
        hash_master_password, master_key = encryptionservice.obtain_hash_master_password_and_master_key(password, email)
        del password
        response = requestservice.login_user(email, hash_master_password)
        self.clear_form()
        if isinstance(response, serverresponse.OkResponse):
            print("NOS VAMOS PARA LA PAGINA PRINCIPAL")
        else:
            self.label_error['text'] = response.get_message()
    
    def clear_form(self):
        self.emailentry.delete(0, "end")
        self.passwordentry.delete(0, "end")
        self.label_error['text'] = ""