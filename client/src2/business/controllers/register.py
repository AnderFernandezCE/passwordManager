from ..validators.register import  RegisterValidator
from ..encryption import encryptionservice
from ..models.api.userregister import User
from ..exceptions.validation import FormInvalid
from src2.persistance.authAPI import RegisterAPI


class RegisterController:
  def __init__(self, view):
    # self.model = model
    self.view = view
    self.frame = self.view.frames["register"]
    self.validator = RegisterValidator()
    self._bind()

  def _bind(self):
    self.frame.homebutton.config(command=self.home)
    self.frame.loginbutton.config(command=self.login)
    self.frame.registerbutton.config(command= self.register)
  
  def home(self):
    self.view.switch("home")

  def login(self):
    self.view.switch("login")

  def register(self):
    user = self.frame.userentry.get()
    email = self.frame.emailentry.get()
    password = self.frame.passwordentry.get()
    confirmpassword = self.frame.confirmpasswordentry.get()
    try:
      self.validator.validate(user,email, password, confirmpassword)
      hmp,mk = encryptionservice.obtain_hash_master_password_and_master_key(password,email)
      key = encryptionservice.generate_protected_sym_key(mk)
      user = User(user,email,hmp,key)
      registerservice = RegisterAPI(user.to_dict())
      response = registerservice.register()
      print(response) # should create a new model - account(protected key etc...)
      self.frame.clear_form()
    except FormInvalid as e:
      self.frame.label_error['text'] = e
    except Exception as e:
      self.frame.clear_form()
      self.frame.label_error['text'] = e
    
    # finally:
        # Clear sensitive data from memory
        # password = " " * len(password)
        # confirmpassword = " " * len(confirmpassword)
        # hmp = " " * len(hmp) if hmp else hmp
        # mk = " " * len(mk) if mk else mk
        # key = " " * len(key) if key else key
        # del password, confirmpassword, hmp, mk, key, user
      
