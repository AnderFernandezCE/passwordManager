from ..validators.register import  RegisterValidator

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
      # make the login/ in persistence data?
    except Exception as e:
      self.frame.label_error['text'] = e
