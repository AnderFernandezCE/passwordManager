class AccountData:
  def __init__(self, username, uuid, email, refresh_token, protected_key):
    self.email = email
    self.username = username
    self.uuid = uuid
    self.protected_key = protected_key
    self.refresh_token = refresh_token
    self.access_token = None
    self.data = {}

  def get_username(self):
    return self.username
  
  def get_refresh_token(self):
    return self.refresh_token
  
  def set_access_token(self, token):
    self.access_token = token

  def get_access_token(self):
    return self.access_token
  
  def set_user_data(self, data):
    self.data = data

  def get_user_data(self):
    return self.data
  