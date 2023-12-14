import client.prompts as prompts
import client.encryption as encryption
import sys
from models.response import LoginResponse

class Client():

  def __init__(self, server):
    self.email = ""
    self.server = server
    self.master_key = None
    self.sym_key = None

  def start(self):
    decision = prompts.welcome()
    if decision == "r":
      self.register()
    if decision == "l":
      self.login()
    else:
      sys.exit(0)

  def login(self):
    try:
      email, password = prompts.login()
      hash_master_key = encryption.get_hashed_user(email,password)
      master_key = encryption.get_master_key(email,password)
      response = self.server.login(email, hash_master_key)
      if isinstance(response, LoginResponse):
        self.sym_key = encryption.get_sym_key(response)
        self.master_key = master_key
        self.email = email
        print("Login succesfully.")
        prompts.main_menu()
      else:
        print(response.get_message())
        self.start()

    except Exception as e:
      print(e)
    pass

  def register(self):
    pass

  def new_item(self):
    pass

  def logout(self):
    self.reset()

  def reset(self):
    self.email = ""
    self.master_key = None
    self.sym_key = None