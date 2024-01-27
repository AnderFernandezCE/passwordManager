import requests
from .constants import AUTH_API_URL

class AuthAPI:
  def __init__(self, entity):
    self.base_url = AUTH_API_URL
    self.entity = entity

class LoginAPI(AuthAPI):
  def __init__(self, user):
    super().__init__(user)
    self.login_url = self.base_url + "login"

  def login(self):
    x = requests.post(self.login_url, json = self.entity, verify=False)
    if x.status_code == 404:# user not exists
      raise Exception("User not exists")
    if x.status_code == 403:# account not verified
      raise Exception("Account not verified, please check the email")
    if x.status_code == 401:# invalid credentials
      raise Exception("Incorrect email or password.")
    if x.status_code == 200:# ok
      return x.json()

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