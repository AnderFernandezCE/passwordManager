import client.prompts as prompts
import client.encryption as encryption
from client.paths import USERS
from client.constants import IV_FILE_NAME

import sys
import uuid
from models.response import LoginResponse, OkResponse

class Client():

  def __init__(self, server):
    self.start_client()
    self.email = ""
    self.server = server
    self.master_key = None
    self.sym_key = None
    self.iv = None

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
        self.initialize_session(sym_key, master_key, email, iv)
        print("Login succesfully.")
        if self.check_correct_sym_key():
          self.manage_vault()
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
      self.initialize_session(fskey, master_key, email, iv)
      self.create_user_vault(email, iv)
      print("Login succesfully.")
      self.manage_vault()
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


  def initialize_session(self, fskey, master_key, email, iv):
    self.sym_key = fskey
    self.master_key = master_key
    self.email = email
    self.iv = iv

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

  def manage_vault(self):
    decision = prompts.main_menu()
    match(decision):
      case 1:
        self.new_item()
      case 2:
        self.modify_item()
      case 3:
        self.list_items()
      case 4:
        self.logout()  
      case _:
        print("Bad decision")

  def new_item(self):
    name, email, password = prompts.new_item()
    file_name = str(uuid.uuid1())
    user_dir = USERS / self.email / "vault" / file_name
    self.write_item_to_file(name, email, password, user_dir)
    prompts.item_created()
    self.manage_vault()

  def modify_item(self):
    filename = prompts.modify_item()
    file_path= USERS / self.email / "vault" / filename
    if file_path.exists():
      name, email, password = prompts.get_item_data()
      self.write_item_to_file(name, email, password, file_path)
      prompts.item_modified()
      self.manage_vault()
    else:
      print("File path not found")
      self.manage_vault()

  def list_items(self):
    prompts.list_items()
    vault_dir = USERS / self.email / "vault"
    for item in vault_dir.iterdir():
      self.print_item(item)
      print("-"*30)
    self.manage_vault()

  def print_item(self, item):
    print("ITEM ID: ", item.stem)
    with open(item , "rb") as f:
      name = f.readline().strip()
      email = f.readline().strip()
      password = f.readline().strip()
    name_decrypt = encryption.vault_decrypt(name, self.iv, self.sym_key[:32])
    email_decrypt = encryption.vault_decrypt(email, self.iv, self.sym_key[:32])
    password_decrypt = encryption.vault_decrypt(password, self.iv, self.sym_key[:32])
    print("NAME: ", name_decrypt)
    print("EMAIL: ", email_decrypt)
    print("PASSWORD: ", password_decrypt)
    
  def write_item_to_file(self, name, email, password, user_dir):
    name_encrypt = encryption.vault_encrypt(name, self.iv , self.sym_key[:32])
    email_encrypt = encryption.vault_encrypt(email, self.iv , self.sym_key[:32])
    password_encrypt = encryption.vault_encrypt(password, self.iv , self.sym_key[:32])
    with open(user_dir , "wb") as f:
      f.write(name_encrypt +  b'\n')
      f.write(email_encrypt +  b'\n')
      f.write(password_encrypt +  b'\n')

  def logout(self):
    self.reset()
    prompts.logout()

  def reset(self):
    self.email = ""
    self.master_key = None
    self.sym_key = None
    self.iv = None