from src.persistance.authAPI import LogoutAPI
from src.persistance.vaultAPI import AllDataAPI

class AppController:
  def __init__(self, view, model):
    self.model = model
    self.view = view
    self.frame = self.view.frames["app"]
    self._bind()

  def _bind(self):
    self.frame.table.bind('<ButtonRelease-1>', self.select_item)
  
  def select_item(self,_):
    curItem = self.frame.table.focus()
    item = self.frame.table.item(curItem)
    self.frame.name.set(item.get("text", "nada"))
    item_values = item.get('values')
    self.frame.username.set(item_values[1])
    self.frame.password.set(item_values[2])
    self.frame.extra.set(item_values[3])

  def get_user_data(self):
    refresh_token = self.model.account_data.get_access_token()
    tokenAPI = AllDataAPI(refresh_token)
    user_data = tokenAPI.get_user_data()
    self.model.account_data.set_user_data(user_data.get("user_data"))

  def update_table_data(self):
    user_data = self.model.account_data.get_user_data()
    email = self.model.account_data.get_email()
    for count, value in enumerate(user_data):
      # decipher data and insert into table
      self.frame.table.insert('',count, text=user_data[value]["name"], values=(value,email, user_data[value]["data"], "extra"))

  def update_view(self):
    if self.model.account_data:
      self.get_user_data()
      self.frame.welcome["text"] = "Welcome " + self.model.account_data.get_username()
      self.update_table_data()
      self.view.root.geometry("800x900")
      
    else:
      self.frame.welcome["text"] = ""

  def bind_logout(self):
    self.frame.logoutbutton.config(command = self.logout)

  def logout(self):
    token = self.model.account_data.get_refresh_token()
    logoutservice = LogoutAPI(token)
    logoutservice.logout()
    self.model.logout()