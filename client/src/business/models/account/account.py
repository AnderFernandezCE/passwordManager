from src.business.models.account.account_data import AccountData

class UserAccount:
  def __init__(self):
    self.logged_in = False
    self.account_data = None

  def login(self, account_data):
    self.logged_in = True
    self.account_data = account_data
  
  def logout(self):
    self.logged_in = False
    self.account_data = None

