class AccountData:
  def __init__(self, username, uuid, email, refresh_token, protected_key):
    self.email = email
    self.username = username
    self.uuid = uuid
    self.protected_key = protected_key
    self.refresh_token = refresh_token

  def get_username(self):
    return self.username