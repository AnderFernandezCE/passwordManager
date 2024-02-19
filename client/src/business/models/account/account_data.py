import sched
import time
import threading
from src.persistance.authAPI import  TokenAPI

class AccountData:
  def __init__(self, username, uuid, email, refresh_token, protected_key, master_key):
    self.email = email
    self.username = username
    self.uuid = uuid
    self.protected_key = protected_key
    self.refresh_token = refresh_token
    self.master_key = master_key
    self.access_token = None
    self.data = {}
    self.scheduler = sched.scheduler(time.time, time.sleep)
    self.scheduler_thread = None

  def get_username(self):
    return self.username
  
  def get_email(self):
    return self.email
  
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
  
  def add_item(self,item_id,item_content):
    self.data[item_id] = item_content

  def update_item(self,item_id,item_content):
    if item_id not in self.data:
      raise Exception("item not found")
    self.data[item_id] = item_content

  def get_protected_key(self):
    return self.protected_key
  
  def get_master_key(self):
    return self.master_key
  
  def refresh_access_token(self):
    if not self.scheduler_thread or not self.scheduler_thread.is_alive():
      self.scheduler_thread = threading.Thread(target=self.scheduler.run, daemon=True)
    self.update_access_token()
    self.scheduler_thread.start()
    # threading.Thread(target=self.scheduler.run).start()

  def update_access_token(self):
    tokenAPI = TokenAPI(self.get_refresh_token())
    access_token = tokenAPI.renew_access_token().get("access_token")
    self.set_access_token(access_token)
    print("access token renewed")
    self.scheduler.enter(260,1,self.update_access_token)
  
  def delete_schedule(self):
    for event in self.scheduler.queue:
      self.scheduler.cancel(event)
    if self.scheduler_thread and self.scheduler_thread.is_alive():
      self.scheduler_thread.join(timeout=1)