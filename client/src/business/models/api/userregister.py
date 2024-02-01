class RegisterModel:
  def __init__(self, username, email, hash_master_password, key):
    self.username =  username
    self.email = email
    self.hash_master_password = hash_master_password
    self.key = key
  
  def to_dict(self):
    return {
    "user" : {
        "username" : self.username,
        "email" : self.email,
        "hash_master_password" : self.hash_master_password,
        "key" : self.key
      }
    }
