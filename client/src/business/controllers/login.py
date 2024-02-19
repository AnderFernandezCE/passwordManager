from ..validators.login import  LoginValidator
from ..encryption import encryptionservice
from ..models.api.userlogin import LoginModel
from ..exceptions.validation import FormInvalid
from src.persistance.authAPI import LoginAPI
from src.business.models.account.account_data import AccountData

class LoginController:
  def __init__(self, view, model):
    self.model = model
    self.view = view
    self.frame = self.view.frames["login"]
    self.validator = LoginValidator()
    self._bind()

  def _bind(self):
    self.frame.homebutton.config(command=self.home)
    self.frame.registerbutton.config(command=self.register)
    self.frame.loginbutton.config(command=self.login)
  
  def home(self):
    self.view.switch("home")

  def register(self):
    self.view.switch("register")

  def login(self):
    email = self.frame.emailentry.get()
    password = self.frame.passwordentry.get()
    try:
      self.validator.validate(email, password)
      hmp,mk = encryptionservice.obtain_hash_master_password_and_master_key(password,email)
      user = LoginModel(email,hmp)
      loginservice = LoginAPI(user.to_dict())
      response = loginservice.login()
      self.frame.clear_form()
      account_data = AccountData(
        response.get("username"),
        response.get("uuid"),
        response.get("email"),
        response.get("refresh_token"),
        response.get("protectedkey"),
        mk
      )
      self.model.login(account_data)
    except FormInvalid as e:
      self.frame.label_error['text'] = e
    except Exception as e:
      self.frame.clear_form()
      self.frame.label_error['text'] = e
    
    # finally:
      # Clear sensitive data from memory
      # password = " " * len(password)
      # hmp = " " * len(hmp) if hmp else ""
      # del password, hmp, user