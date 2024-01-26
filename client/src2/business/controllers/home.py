class HomeController:
  def __init__(self, view):
    # self.model = model
    self.view = view
    self.frame = self.view.frames["home"]
    self._bind()

  def _bind(self):
    self.frame.loginbutton.config(command=self.login)
    self.frame.registerbutton.config(command=self.register)
  
  def login(self):
    self.view.switch("login")

  def register(self):
    self.view.switch("register")

