import client.prompts as prompts
import client.encryption as encryption
from client.paths import USERS
from client.constants import IV_FILE_NAME

import sys
from models.response import LoginResponse, OkResponse

class Client():

  def __init__(self, server):
    self.start_client()
    self.email = ""
    self.server = server
    self.master_key = None
    self.sym_key = None

  def start_client(self):
    try:
      if not USERS.exists():
        USERS.mkdir()
    except Exception as e:
      print(e)

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
        protected_sym_key = encryption.get_protected_sym_key(response)
        iv = self.get_user_iv(email)
        sym_key = encryption.decrypt_protected_sym_key(protected_sym_key, master_key, iv)
        self.initialize_session(sym_key, master_key, email)
        print("Login succesfully.")
        if self.check_correct_sym_key():
          prompts.main_menu()
        else:
          print("RECEIVED PROTECTED KEY NOT VALID")
      else:
        print(response.get_message())
        self.start()

    except Exception as e:
      print(e)
    pass

  def register(self):
    email, password = prompts.register()
    hash_master_key = encryption.get_hashed_user(email,password)
    master_key = encryption.get_master_key(email,password)
    skey, smac = encryption.generate_symmetric_key()
    fskey = skey + smac
    iv = encryption.generate_iv()
    protected_key = encryption.get_protected_key(fskey, master_key, iv)
    response = self.server.register(email, hash_master_key, protected_key)
    if isinstance(response, OkResponse):
      self.initialize_session(fskey, master_key, email)
      self.create_user_vault(email, iv)
      print("Login succesfully.")
      prompts.main_menu()
    else:
      print(response.get_message())
      self.start()

  def get_user_iv(self, email):
    try:
      user_dir = USERS / email
      with open(user_dir / IV_FILE_NAME, "rb") as f:
        iv = f.readline()
      return iv
    except Exception as e:
      return None
    
    

  def check_correct_sym_key(self):
    return encryption.check_correct_sym_key(self.sym_key)


  def initialize_session(self, fskey, master_key, email):
    self.sym_key = fskey
    self.master_key = master_key
    self.email = email

  def create_user_vault(self, email, iv):
    try:
      user_dir = USERS / email
      if not user_dir.exists():
        user_dir.mkdir()
      with open(user_dir / IV_FILE_NAME , "wb") as f:
        f.write(iv)
      user_vault = user_dir / "vault"
      if not user_vault.exists():
        user_vault.mkdir()
    except Exception as e:
      print(e)

  def new_item(self):
    pass

  def logout(self):
    self.reset()

  def reset(self):
    self.email = ""
    self.master_key = None
    self.sym_key = None