from ..persistance.constants import VAULT_API_URL
import requests

class VaultAPI:
  def __init__(self, entity):
    self.base_url = VAULT_API_URL
    self.entity = entity

  def get_user_data(self):
    data_url = self.base_url + "get-passwords"
    headers = {"Authorization": f"Bearer {self.entity}"}
    x = requests.post(data_url, headers=headers, verify=False)
    if x.status_code == 401:# not valid token
      raise Exception("Not a valid token")
    if x.status_code == 200:# ok
      return x.json()
    
  def delete_item(self, item_id):
    data_url = self.base_url + "delete-item"
    headers = {"Authorization": f"Bearer {self.entity}"}
    json = {
      "id": str(item_id)
    }
    x = requests.delete(data_url, headers=headers, json=json ,verify=False)
    if x.status_code == 401:# not valid token
      raise Exception("Not a valid token")
    if x.status_code == 404:# item not found
      raise Exception("Not a valid item id")
    if x.status_code == 204:# ok
      return 
    
  def add_item(self, name, data):
    data_url = self.base_url + "create-item"
    headers = {"Authorization": f"Bearer {self.entity}"}
    json = {
      "name": name,
      "data": data
    }
    x = requests.post(data_url, headers=headers, json=json ,verify=False)
    if x.status_code == 401:# not valid token
      raise Exception("Not a valid token")
    if x.status_code == 201:# ok
      return x.json()
    
  def modify_item(self,id, name, data):
    data_url = self.base_url + "update-item"
    headers = {"Authorization": f"Bearer {self.entity}"}
    json = {
      "id": id,
      "name": name,
      "data": data
    }
    x = requests.put(data_url, headers=headers, json=json ,verify=False)
    if x.status_code == 401:# not valid token
      raise Exception("Not a valid token")
    if x.status_code == 404:# item not found
      raise Exception("Item id not found")
    if x.status_code == 200:# ok
      return x.json()