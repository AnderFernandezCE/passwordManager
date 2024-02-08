from ..persistance.constants import VAULT_API_URL
import requests

class AuthAPI:
  def __init__(self, entity):
    self.base_url = VAULT_API_URL
    self.entity = entity

class AllDataAPI(AuthAPI):
  def __init__(self, token):
    super().__init__(token)
    
  def get_user_data(self):
    data_url = self.base_url + "get-passwords"
    headers = {"Authorization": f"Bearer {self.entity}"}
    x = requests.post(data_url, headers=headers, verify=False)
    if x.status_code == 401:# not valid token
      raise Exception("Not a valid token")
    if x.status_code == 200:# ok
      return x.json()