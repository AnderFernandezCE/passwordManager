import tkinter as tk
from src.user_interface.basemodel import Page
from src.encryption import encryptionservice
from src.utils import validation
from src.apicall import requestservice
from src.schemas import response as serverresponse

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

        self.label_error = tk.Label(self, foreground='red')
        self.label_error.pack(anchor="center")

        clearbutton = tk.Button(self, text="Clear", command=self.clear_form)
        clearbutton.pack(anchor="center")

        registerbutton = tk.Button(self, text="Register", command=self.validate_input)
        registerbutton.pack(anchor="center")

    
    def validate_input(self):
        user = self.userentry.get()
        email = self.emailentry.get()
        password = self.passwordentry.get()
        confirmpassword = self.confirmpasswordentry.get()

        if not user or not password:
            self.label_error['text'] = "Fill all the fields"
        elif not validation.check_email_valid(email):
            self.label_error['text'] = "Invalid email"
        elif not password == confirmpassword:
            self.label_error['text'] = "Passwords are not equal"
        else:
            self.register_user(user,email,password)


    def register_user(self, user, email, password):
        hash_master_password, master_key = encryptionservice.obtain_hash_master_password_and_master_key(password, email)
        del password
        protected_sym_key = encryptionservice.generate_protected_sym_key(master_key)
        response = requestservice.register_user(user,email, hash_master_password, protected_sym_key)
        self.clear_form()
        if isinstance(response, serverresponse.OkResponse):
            print("NOS VAMOS PARA LA PAGINA PRINCIPAL")
        else:
            self.label_error['text'] = response.get_message()
            
    def clear_form(self):
        self.userentry.delete(0, "end")
        self.emailentry.delete(0, "end")
        self.passwordentry.delete(0, "end")
        self.confirmpasswordentry.delete(0, "end")
        self.label_error['text'] = ""