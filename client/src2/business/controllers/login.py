from ..validators.login import  LoginValidator

class LoginController:
  def __init__(self, view):
    # self.model = model
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
      # make the login/ in persistence data?
    except Exception as e:
      self.frame.label_error['text'] = e
    