from src.persistance.authAPI import LogoutAPI

class AppController:
  def __init__(self, view, model):
    self.model = model
    self.view = view
    self.frame = self.view.frames["app"]

  def update_view(self):
    if self.model.account_data:
      self.frame.welcome["text"] = "Welcome " + self.model.account_data.get_username()
    else:
      self.frame.welcome["text"] = ""

  def bind_logout(self):
    self.frame.logoutbutton.config(command = self.logout)

  def logout(self):
    token = self.model.account_data.get_refresh_token()
    logoutservice = LogoutAPI(token)
    logoutservice.logout()
    self.model.logout()