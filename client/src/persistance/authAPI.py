import requests
from .constants import AUTH_API_URL

class AuthAPI:
  def __init__(self, entity):
    self.base_url = AUTH_API_URL
    self.entity = entity

class LoginAPI(AuthAPI):
  def __init__(self, user):
    super().__init__(user)

  def login(self):
    login_url = self.base_url + "login"
    x = requests.post(login_url, json = self.entity, verify=False)
    if x.status_code == 404:# user not exists
      raise Exception("User not exists")
    if x.status_code == 403:# account not verified
      raise Exception("Account not verified, please check the email")
    if x.status_code == 401:# invalid credentials
      raise Exception("Incorrect email or password.")
    if x.status_code == 200:# ok
      return x.json()
    

class LogoutAPI(AuthAPI):
  def __init__(self, token):
    super().__init__(token)

    
  def logout(self):
    logout_url = self.base_url + "revoke-token"
    headers = {"Authorization": f"Bearer {self.entity}"}
    x = requests.post(logout_url, headers=headers, verify=False)
    if x.status_code == 401:# not valid token
      raise Exception("Not a valid token")
    if x.status_code == 200:# ok
      return 

class RegisterAPI(AuthAPI):
  def __init__(self, user):
    super().__init__(user)
    self.register_url = self.base_url + "register"

  def register(self):
    x = requests.post(self.register_url, json = self.entity, verify=False)
    if x.status_code == 409:# user exists
      raise Exception("Email is already in use.")
    if x.status_code == 500:# server error
      raise Exception("Server has encountered an error")
    if x.status_code == 201:# created
      return x.json()
    
class TokenAPI(AuthAPI):
  def __init__(self, user):
    super().__init__(user)
    self.renew_token = self.base_url + "get-access-token"

  def renew_access_token(self):
    headers = {"Authorization": f"Bearer {self.entity}"}
    x = requests.post(self.renew_token, headers=headers, verify=False)
    if x.status_code == 401:# not valid token
      raise Exception("Not a valid token")
    if x.status_code == 200:# ok
      return x.json()