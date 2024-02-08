from src.persistance.authAPI import LogoutAPI, TokenAPI
from src.persistance.vaultAPI import AllDataAPI

class AppController:
  def __init__(self, view, model):
    self.model = model
    self.view = view
    self.frame = self.view.frames["app"]

  def get_access_token(self):
    refresh_token = self.model.account_data.get_refresh_token()
    tokenAPI = TokenAPI(refresh_token)
    access_token = tokenAPI.renew_access_token().get("access_token")
    self.model.account_data.set_access_token(access_token)

  def get_user_data(self):
    refresh_token = self.model.account_data.get_access_token()
    tokenAPI = AllDataAPI(refresh_token)
    user_data = tokenAPI.get_user_data()
    self.model.account_data.set_user_data(user_data.get("user_data"))

  def update_table_data(self):
    user_data = self.model.account_data.get_user_data()
    for count, value in enumerate(user_data):
      print(user_data[value])
    # self.frame.table.in

  def update_view(self):
    if self.model.account_data:
      self.get_access_token()
      self.get_user_data()
      self.frame.welcome["text"] = "Welcome " + self.model.account_data.get_username()
      self.update_table_data()
      self.view.root.geometry("1200x900")
      
    else:
      self.frame.welcome["text"] = ""

  def bind_logout(self):
    self.frame.logoutbutton.config(command = self.logout)

  def logout(self):
    token = self.model.account_data.get_refresh_token()
    logoutservice = LogoutAPI(token)
    logoutservice.logout()
    self.model.logout()