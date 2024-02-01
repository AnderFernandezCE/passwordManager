class LogoutModel:
  def __init__(self, token):
    self.token = token
  
  def to_dict(self):
    return {
      "token" : self.token
    }
