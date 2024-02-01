from src.business.models.account.account_data import AccountData
from src.business.models.account.observable_base import ObservableModel

class UserAccount(ObservableModel):
  def __init__(self):
    super().__init__()
    self.logged_in = False
    self.account_data = None

  def login(self, account_data):
    self.logged_in = True
    self.account_data = account_data
    self.trigger_event("login")
  
  def logout(self):
    self.logged_in = False
    self.account_data = None
    self.trigger_event("logout")

