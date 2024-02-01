class LoginModel:
  def __init__(self, email, userhash):
    self.email = email
    self.userhash = userhash
  
  def to_dict(self):
    return {
      "email" : self.email,
      "userhash" : self.userhash
    }
