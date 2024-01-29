from src.business.controllers.home import HomeController
from src.business.controllers.login import LoginController
from src.business.controllers.register import RegisterController
from src.business.controllers.app import AppController

class Controller:
  def __init__(self, view, model):
    self.model = model
    self.view = view
    self.home_controller = HomeController(view, model)
    self.login_controller = LoginController(view, model)
    self.register_controller = RegisterController(view, model)
    self.app_controller = AppController(view, model)

  def start(self):
    self.view.switch("home")
    self.view.start_mainloop()